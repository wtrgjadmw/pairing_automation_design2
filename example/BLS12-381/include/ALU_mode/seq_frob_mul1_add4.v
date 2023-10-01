case (state)
0: begin
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd4;
	ram_input_raddr2 <= `RAM_XI10;
	state <= state + 1;
end
1: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd5;
	ram_input_raddr2 <= `RAM_XI11;
	state <= state + 1;
end
2: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd2;
	ram_input_raddr2 <= `RAM_XI30;
	state <= state + 1;
end
3: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd3;
	ram_input_raddr2 <= `RAM_XI31;
	state <= state + 1;
end
4: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd11;
	ram_input_raddr2 <= `RAM_XI51;
	state <= state + 1;
end
5: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd6;
	ram_input_raddr2 <= `RAM_XI40;
	state <= state + 1;
end
6: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd7;
	ram_input_raddr2 <= `RAM_XI41;
	state <= state + 1;
end
7: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd10;
	ram_input_raddr2 <= `RAM_XI50;
	state <= state + 1;
end
8: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 4;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd9;
	ram_input_raddr2 <= `RAM_XI21;
	state <= state + 1;
end
9: begin
	add0_opr1 <= mm0_out_reg; add0_opr2 <= mm0_out; issub0 <= 1;
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 5;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd8;
	ram_input_raddr2 <= `RAM_XI20;
	state <= state + 1;
end
10: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 2;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd2;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd3;
	state <= state + 1;
end
11: begin
	add2_opr1 <= mm0_out_reg; add2_opr2 <= mm0_out; issub2 <= 0;
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 1;
	ram_mm0_wr_n <= 1;
	ram_add0_wr_n <= 1;
	ram_mm0_raddr1 <= 0;
	ram_input_raddr1 <= `RAM_XI20;
	ram_input_raddr2 <= `RAM_XI21;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd2;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
12: begin
	add0_opr1 <= ram_mm0_out1; add0_opr2 <= mm0_out_reg; issub0 <= 1;
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 0;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd10;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd11;
	w1_n_reg <= 1;
	state <= state + 1;
end
13: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 1;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 1;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 3;
	ram_input_raddr1 <= `RAM_XI50;
	ram_input_raddr2 <= `RAM_XI51;
	state <= state + 1;
end
14: begin
	add2_opr1 <= mm0_out_reg; add2_opr2 <= mm0_out; issub2 <= 1;
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 2;
	ram_add1_wr_n <= 1;
	ram_add0_wr_n <= 1;
	ram_input_raddr1 <= `RAM_XI40;
	ram_input_raddr2 <= `RAM_XI41;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
15: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 0;
	add0_opr1 <= mm0_out; add0_opr2 <= ram_mm0_out1; issub0 <= 0;
	mm0_opr1 <= add2_out_reg; mm0_opr2 <= add0_out; 
	ram_mm0_wr_n <= 1;
	ram_add2_wr_n <= 0;
	ram_add2_waddr <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd6;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd7;
	ram_mm0_raddr1 <= 0;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd10;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
16: begin
	add3_opr1 <= ram_input_out1; add3_opr2 <= ram_input_out2; issub3 <= 1;
	add0_opr1 <= mm0_out_reg; add0_opr2 <= ram_mm0_out1; issub0 <= 1;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add2_wr_n <= 1;
	ram_input_raddr1 <= `RAM_XI10;
	ram_input_raddr2 <= `RAM_XI11;
	w1_n_reg <= 1;
	state <= state + 1;
end
17: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	mm0_opr1 <= add3_out; mm0_opr2 <= add2_out_reg; 
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 3;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 1;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd4;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd5;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
18: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 1;
	add3_opr1 <= mm0_out_reg; add3_opr2 <= ram_mm0_out1; issub3 <= 1;
	ram_mm0_wr_n <= 1;
	ram_add0_wr_n <= 1;
	ram_mm0_raddr1 <= 1;
	ram_mm0_raddr2 <= 2;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd8;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd9;
	state <= state + 1;
end
19: begin
	add0_opr1 <= ram_mm0_out1; add0_opr2 <= ram_mm0_out2; issub0 <= 0;
	mm0_opr1 <= add2_out; mm0_opr2 <= add0_out_reg; 
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 1;
	ram_add3_wr_n <= 0;
	ram_add3_waddr <= 0;
	ram_add1_raddr1 <= 0;
	ram_input_raddr1 <= `RAM_XI30;
	ram_input_raddr2 <= `RAM_XI31;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd6;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
20: begin
	mm0_opr1 <= add1_out; mm0_opr2 <= ram_add1_out1; 
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 0;
	ram_add3_wr_n <= 1;
	ram_mm0_raddr1 <= 3;
	ram_mm0_raddr2 <= 0;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd1;
	w1_n_reg <= 1;
	state <= state + 1;
end
21: begin
	add2_opr1 <= ram_mm0_out1; add2_opr2 <= ram_mm0_out2; issub2 <= 0;
	add3_opr1 <= ram_input_out1; add3_opr2 <= ram_input_out2; issub3 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd0;
	ram_add0_raddr1 <= 0;
	ram_add0_raddr2 <= 1;
	w2_n_reg <= 0;
	waddr2_reg <= ret_addr + `RAM_ADDR_SIZE'd1;
	wdata_s2 <= `ADD3;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd8;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
22: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	mm0_opr1 <= ram_add0_out1; mm0_opr2 <= add1_out_reg; 
	add3_opr1 <= mm0_out; add3_opr2 <= ram_add0_out2; issub3 <= 1;
	ram_mm0_raddr1 <= 4;
	ram_mm0_raddr2 <= 5;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd0;
	wdata_s1 <= `ADD0;
	w2_n_reg <= 0;
	waddr2_reg <= ret_addr + `RAM_ADDR_SIZE'd11;
	wdata_s2 <= `ADD3;
	state <= state + 1;
end
23: begin
	add1_opr1 <= ram_mm0_out1; add1_opr2 <= ram_mm0_out2; issub1 <= 0;
	ram_add2_raddr1 <= 0;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd4;
	wdata_s1 <= `ADD1;
	w2_n_reg <= 1;
	state <= state + 1;
end
24: begin
	add3_opr1 <= mm0_out; add3_opr2 <= ram_add2_out1; issub3 <= 1;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd7;
	wdata_s1 <= `ADD3;
	state <= state + 1;
end
25: begin
	ram_add0_raddr1 <= 2;
	w1_n_reg <= 1;
	state <= state + 1;
end
26: begin
	add2_opr1 <= mm0_out; add2_opr2 <= ram_add0_out1; issub2 <= 1;
	ram_add3_raddr1 <= 0;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd5;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
27: begin
	add0_opr1 <= mm0_out; add0_opr2 <= ram_add3_out1; issub0 <= 1;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd9;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
28: begin
	ram_add0_raddr1 <= 3;
	w1_n_reg <= 1;
	state <= state + 1;
end
29: begin
	add1_opr1 <= mm0_out; add1_opr2 <= ram_add0_out1; issub1 <= 1;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd3;
	wdata_s1 <= `ADD1;
	state <= state + 1;
end
30: begin
	w1_n_reg <= 1;
	state <= 0;
end
endcase
