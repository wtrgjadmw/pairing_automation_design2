`include "./include/parameter.vh"
`include "./include/CalcCore_param.vh"

module CalculationCore (
	input wire clk,
	input wire rst_n,
	input wire [`I_INPUTMODE_SIZE-1: 0] I_INPUTMODE,
	input wire [`CMD_SIZE-1: 0] top_cmd,
	input wire [`RAM_ADDR_SIZE-1: 0] I_WADDR1, I_WADDR2,
	input wire [`WORD_SIZE-1: 0] I_WDATA1, I_WDATA2,
	input wire [`RAM_ADDR_SIZE-1: 0] I_RADDR1, I_RADDR2,
	output wire [`WORD_SIZE-1: 0] outdata1, outdata2,
	output wire finished_flag
);

wire [`MODE_SIZE-1: 0] mode;
wire [`RAM_ADDR_SIZE-1: 0] inst_addr_opr1, inst_addr_opr2, ret_addr;

assign mode = top_cmd[`CMD_SIZE-1: `RAM_ADDR_SIZE * 3];
assign inst_addr_opr1 = top_cmd[`RAM_ADDR_SIZE*3-1: `RAM_ADDR_SIZE*2];
assign inst_addr_opr2 = top_cmd[`RAM_ADDR_SIZE*2-1: `RAM_ADDR_SIZE];
assign ret_addr = top_cmd[`RAM_ADDR_SIZE-1: 0];

reg [`CALC_STATE_SIZE-1: 0] state;
reg [`OPR_NUM_SIZE-1: 0] wdata_s1, wdata_s2;
wire [`WORD_SIZE-1: 0] result1, result2;

wire w1_n, w2_n;
reg w1_n_reg, w2_n_reg;
reg [`RAM_ADDR_SIZE-1: 0] ram_input_raddr1, ram_input_raddr2, waddr1_reg, waddr2_reg;
wire [`RAM_ADDR_SIZE-1: 0] raddr1, raddr2, waddr1, waddr2;
wire [`WORD_SIZE-1: 0] ram_input_out1, ram_input_out2, wdata1, wdata2;

assign w1_n = (I_INPUTMODE == `INPUT_COORD_CORE) ? 0 : w1_n_reg;
assign w2_n = (I_INPUTMODE == `INPUT_COORD_CORE) ? 0 : w2_n_reg;

assign waddr1 = (I_INPUTMODE == `INPUT_COORD_CORE) ? I_WADDR1 : waddr1_reg;
assign waddr2 = (I_INPUTMODE == `INPUT_COORD_CORE) ? I_WADDR2 : waddr2_reg;

assign wdata1 = (I_INPUTMODE == `INPUT_COORD_CORE) ? I_WDATA1 : result1;
assign wdata2 = (I_INPUTMODE == `INPUT_COORD_CORE) ? I_WDATA2 : result2;

// TODO: 読み出しアドレスはシーケンサで制御できるようにする
assign raddr1 = (I_INPUTMODE == `REF_RESULT) ? I_RADDR1 : ram_input_raddr1;
assign raddr2 = (I_INPUTMODE == `REF_RESULT) ? I_RADDR2 : ram_input_raddr2;

assign outdata1 = (I_INPUTMODE == `REF_RESULT) ? ram_input_out1 : {`WORD_SIZE{1'b0}};
assign outdata2 = (I_INPUTMODE == `REF_RESULT) ? ram_input_out2 : {`WORD_SIZE{1'b0}};

DW_ram_2r_2w_s_dff #(`WORD_SIZE, `RAM_ADDR_SIZE, 1'b0) RAM(
    .clk(clk),
	.rst_n(rst_n),
	.en_r1_n(1'b0),
    	.addr_r1(raddr1), // log2(RAM_BLOCKS)
        .data_r1(ram_input_out1),
	.en_r2_n(1'b0),
    	.addr_r2(raddr2), // log2(RAM_BLOCKS)
        .data_r2(ram_input_out2),
	.en_w1_n(w1_n),
    	.addr_w1(waddr1),
        .data_w1(wdata1),
	.en_w2_n(w2_n),
    	.addr_w2(waddr2),
        .data_w2(wdata2)
);


wire [`WORD_SIZE-1: 0] mm0_out;
reg [`WORD_SIZE-1: 0] mm0_opr1, mm0_opr2, mm0_out_reg;
reg ram_mm0_wr_n;
wire ram_mm0_wr_n_;
reg [`MM_RAM_SIZE-1:0] ram_mm0_raddr1, ram_mm0_raddr2, ram_mm0_waddr;
wire [`MM_RAM_SIZE-1:0] ram_mm0_raddr1_, ram_mm0_raddr2_, ram_mm0_waddr_;
wire [`WORD_SIZE-1: 0] ram_mm0_out1, ram_mm0_out2;

assign ram_mm0_wr_n_ = ram_mm0_wr_n;
assign ram_mm0_raddr1_ = ram_mm0_raddr1;
assign ram_mm0_raddr2_ = ram_mm0_raddr2;
assign ram_mm0_waddr_ = ram_mm0_waddr;

MontMul mm0(.clk(clk), .rst_n(rst_n), .X(mm0_opr1), .Y(mm0_opr2), .Z(mm0_out));
DW_ram_2r_w_s_dff #(`WORD_SIZE, `MM_RAM_DEPTH, 1'b0) RAM_mm0(
    .clk(clk),
        .rst_n(rst_n),
        .cs_n(1'b0),
        .wr_n(ram_mm0_wr_n_),
    .rd1_addr(ram_mm0_raddr1_), // log2(RAM_BLOCKS)
        .data_rd1_out(ram_mm0_out1),
    .rd2_addr(ram_mm0_raddr2_),
        .data_rd2_out(ram_mm0_out2),
    .wr_addr(ram_mm0_waddr_),
        .data_in(mm0_out_reg)
);

wire [`WORD_SIZE-1: 0] add0_out, add1_out, add2_out, add3_out;
reg [`WORD_SIZE-1: 0] add0_opr1, add0_opr2, add0_out_reg, add1_opr1, add1_opr2, add1_out_reg, add2_opr1, add2_opr2, add2_out_reg, add3_opr1, add3_opr2, add3_out_reg;
reg issub0, issub1, issub2, issub3;

reg ram_add0_wr_n, ram_add1_wr_n, ram_add2_wr_n, ram_add3_wr_n;
wire ram_add0_wr_n_, ram_add1_wr_n_, ram_add2_wr_n_, ram_add3_wr_n_;
reg [`ADD0_RAM_SIZE-1:0] ram_add0_raddr1, ram_add0_raddr2, ram_add0_waddr;
wire [`ADD0_RAM_SIZE-1:0] ram_add0_raddr1_, ram_add0_raddr2_, ram_add0_waddr_;
reg [`ADD1_RAM_SIZE-1:0] ram_add1_raddr1, ram_add1_raddr2, ram_add1_waddr;
wire [`ADD1_RAM_SIZE-1:0] ram_add1_raddr1_, ram_add1_raddr2_, ram_add1_waddr_;
reg [`ADD2_RAM_SIZE-1:0] ram_add2_raddr1, ram_add2_raddr2, ram_add2_waddr;
wire [`ADD2_RAM_SIZE-1:0] ram_add2_raddr1_, ram_add2_raddr2_, ram_add2_waddr_;
reg [`ADD3_RAM_SIZE-1:0] ram_add3_raddr1, ram_add3_raddr2, ram_add3_waddr;
wire [`ADD3_RAM_SIZE-1:0] ram_add3_raddr1_, ram_add3_raddr2_, ram_add3_waddr_;
wire [`WORD_SIZE-1: 0] ram_add0_out1, ram_add0_out2, ram_add1_out1, ram_add1_out2, ram_add2_out1, ram_add2_out2, ram_add3_out1, ram_add3_out2;

assign ram_add0_wr_n_ = ram_add0_wr_n;
assign ram_add0_raddr1_ = ram_add0_raddr1;
assign ram_add0_raddr2_ = ram_add0_raddr2;
assign ram_add0_waddr_ = ram_add0_waddr;

assign ram_add1_wr_n_ = ram_add1_wr_n;
assign ram_add1_raddr1_ = ram_add1_raddr1;
assign ram_add1_raddr2_ = ram_add1_raddr2;
assign ram_add1_waddr_ = ram_add1_waddr;

assign ram_add2_wr_n_ = ram_add2_wr_n;
assign ram_add2_raddr1_ = ram_add2_raddr1;
assign ram_add2_raddr2_ = ram_add2_raddr2;
assign ram_add2_waddr_ = ram_add2_waddr;

assign ram_add3_wr_n_ = ram_add3_wr_n;
assign ram_add3_raddr1_ = ram_add3_raddr1;
assign ram_add3_raddr2_ = ram_add3_raddr2;
assign ram_add3_waddr_ = ram_add3_waddr;

AddSubMod add0(.inA(add0_opr1), .inB(add0_opr2), .issub(issub0), .out(add0_out));
DW_ram_2r_w_s_dff #(`WORD_SIZE, `ADD0_RAM_DEPTH, 1'b0) RAM_add0(
    .clk(clk),
        .rst_n(rst_n),
        .cs_n(1'b0),
        .wr_n(ram_add0_wr_n_),
    .rd1_addr(ram_add0_raddr1_), // log2(RAM_BLOCKS)
        .data_rd1_out(ram_add0_out1),
    .rd2_addr(ram_add0_raddr2_),
        .data_rd2_out(ram_add0_out2),
    .wr_addr(ram_add0_waddr_),
        .data_in(add0_out_reg)
);
AddSubMod add1(.inA(add1_opr1), .inB(add1_opr2), .issub(issub1), .out(add1_out));
DW_ram_2r_w_s_dff #(`WORD_SIZE, `ADD1_RAM_DEPTH, 1'b0) RAM_add1(
    .clk(clk),
        .rst_n(rst_n),
        .cs_n(1'b0),
        .wr_n(ram_add1_wr_n_),
    .rd1_addr(ram_add1_raddr1_), // log2(RAM_BLOCKS)
        .data_rd1_out(ram_add1_out1),
    .rd2_addr(ram_add1_raddr2_),
        .data_rd2_out(ram_add1_out2),
    .wr_addr(ram_add1_waddr_),
        .data_in(add1_out_reg)
);
AddSubMod add2(.inA(add2_opr1), .inB(add2_opr2), .issub(issub2), .out(add2_out));
DW_ram_2r_w_s_dff #(`WORD_SIZE, `ADD2_RAM_DEPTH, 1'b0) RAM_add2(
    .clk(clk),
        .rst_n(rst_n),
        .cs_n(1'b0),
        .wr_n(ram_add2_wr_n_),
    .rd1_addr(ram_add2_raddr1_), // log2(RAM_BLOCKS)
        .data_rd1_out(ram_add2_out1),
    .rd2_addr(ram_add2_raddr2_),
        .data_rd2_out(ram_add2_out2),
    .wr_addr(ram_add2_waddr_),
        .data_in(add2_out_reg)
);
AddSubMod add3(.inA(add3_opr1), .inB(add3_opr2), .issub(issub3), .out(add3_out));
DW_ram_2r_w_s_dff #(`WORD_SIZE, `ADD3_RAM_DEPTH, 1'b0) RAM_add3(
    .clk(clk),
        .rst_n(rst_n),
        .cs_n(1'b0),
        .wr_n(ram_add3_wr_n_),
    .rd1_addr(ram_add3_raddr1_), // log2(RAM_BLOCKS)
        .data_rd1_out(ram_add3_out1),
    .rd2_addr(ram_add3_raddr2_),
        .data_rd2_out(ram_add3_out2),
    .wr_addr(ram_add3_waddr_),
        .data_in(add3_out_reg)
);

// for Inv
reg start;
wire inv_comp;
reg [`WORD_SIZE-1: 0] inv_opr;
wire [`WORD_SIZE-1: 0] inv_out;
reg [`WORD_SIZE-1: 0] inv_out_reg;

MontgomeryInverter MontInv(clk, rst_n, start, inv_opr, inv_out, inv_comp);

`include "./CalcCore_func.v"
assign finished_flag = calc_finised(mode, state);
assign result1 = wdata_func1(mm0_out_reg, add0_out_reg, add1_out_reg, add2_out_reg, add3_out_reg, wdata_s1);
assign result2 = wdata_func2(mm0_out_reg, add0_out_reg, add1_out_reg, add2_out_reg, add3_out_reg, wdata_s2);

always @(posedge clk or negedge rst_n) begin
	if (!rst_n) begin
		state <= 0;
		start <= 0;
		w1_n_reg <= 1;
		w2_n_reg <= 1;
		ram_mm0_wr_n <= 1;
		ram_add0_wr_n <= 1;
		ram_add1_wr_n <= 1;
		ram_add2_wr_n <= 1;
		ram_add3_wr_n <= 1;
	end
	else begin
		mm0_out_reg <= mm0_out;
		add0_out_reg <= add0_out;
		add1_out_reg <= add1_out;
		add2_out_reg <= add2_out;
		add3_out_reg <= add3_out;
		//inv_out_reg <= inv_out;
		if (I_INPUTMODE == `EXEC_CORE) begin
			case (mode)
				`MODE_PDBL: begin
					`include "./include/ALU_mode/seq_PDBL.v"
				end 
				`MODE_PADD: begin
					`include "./include/ALU_mode/seq_PADD.v"
				end 
				`MODE_PMINUS: begin
					`include "./include/ALU_mode/seq_PMINUS.v"
				end 
				`MODE_FROB: begin
					`include "./include/ALU_mode/seq_FROB.v"
				end 
				`MODE_CONJ: begin
					`include "./include/ALU_mode/seq_CONJ.v"
				end 
				`MODE_SQR012345: begin
					`include "./include/ALU_mode/seq_SQR012345.v"
				end 
				`MODE_SPARSE_MUL: begin
					`include "./include/ALU_mode/seq_SPARSE.v"
				end 
				`MODE_SQUARE: begin
					`include "./include/ALU_mode/seq_SQR.v"
				end 
				`MODE_MUL: begin
					`include "./include/ALU_mode/seq_MUL.v"
				end 
				`MODE_MUL_CONJ: begin
					`include "./include/ALU_mode/seq_MUL_CONJ.v"
				end 
				`MODE_INV: begin
					`include "./include/ALU_mode/seq_INV.v"
				end 
			endcase
		end
	end
end
endmodule
