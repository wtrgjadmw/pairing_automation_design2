case (state)
0: begin
	ram_input_raddr1 <= `RAM_TY1;
	ram_input_raddr2 <= `RAM_TZ1;
	state <= state + 1;
end
1: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_TY0;
	ram_input_raddr2 <= `RAM_TZ0;
	state <= state + 1;
end
2: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_TZ0;
	ram_input_raddr2 <= `RAM_TZ1;
	state <= state + 1;
end
3: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_TX1;
	ram_input_raddr2 <= `RAM_TY1;
	state <= state + 1;
end
4: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_TX0;
	ram_input_raddr2 <= `RAM_TX1;
	state <= state + 1;
end
5: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_TX0;
	ram_input_raddr2 <= `RAM_TY0;
	state <= state + 1;
end
6: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_TY0;
	ram_input_raddr2 <= `RAM_TY1;
	state <= state + 1;
end
7: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_input_out2; 
	ram_input_raddr1 <= `RAM_BT0;
	ram_input_raddr2 <= `RAM_BT1;
	state <= state + 1;
end
8: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 1;
	ram_input_raddr1 <= `RAM_TY0;
	ram_input_raddr2 <= `RAM_TY1;
	state <= state + 1;
end
9: begin
	add1_opr1 <= mm0_out; add1_opr2 <= mm0_out_reg; issub1 <= 1;
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 3;
	ram_input_raddr1 <= `RAM_TX0;
	ram_input_raddr2 <= `RAM_TX1;
	state <= state + 1;
end
10: begin
	add1_opr1 <= mm0_out; add1_opr2 <= mm0_out; issub1 <= 0;
	add3_opr1 <= add1_out; add3_opr2 <= add1_out; issub3 <= 0;
	add2_opr1 <= mm0_out; add2_opr2 <= mm0_out; issub2 <= 1;
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_mm0_wr_n <= 1;
	ram_add0_wr_n <= 1;
	ram_mm0_raddr1 <= 0;
	ram_mm0_raddr2 <= 1;
	ram_input_raddr1 <= `RAM_TX0;
	ram_input_raddr2 <= `RAM_TX1;
	state <= state + 1;
end
11: begin
	add0_opr1 <= ram_mm0_out1; add0_opr2 <= ram_mm0_out2; issub0 <= 0;
	mm0_opr1 <= add0_out; mm0_opr2 <= add0_out_reg; 
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 1;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 1;
	ram_add3_wr_n <= 0;
	ram_add3_waddr <= 1;
	ram_add2_wr_n <= 0;
	ram_add2_waddr <= 0;
	ram_input_raddr1 <= `RAM_TZ0;
	ram_input_raddr2 <= `RAM_TZ1;
	state <= state + 1;
end
12: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	add2_opr1 <= mm0_out; add2_opr2 <= mm0_out; issub2 <= 0;
	add1_opr1 <= mm0_out; add1_opr2 <= mm0_out; issub1 <= 1;
	ram_mm0_wr_n <= 1;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 0;
	ram_add3_wr_n <= 1;
	ram_add2_wr_n <= 1;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 2;
	ram_input_raddr1 <= `RAM_TY0;
	ram_input_raddr2 <= `RAM_TY1;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
13: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	add1_opr1 <= mm0_out; add1_opr2 <= ram_mm0_out1; issub1 <= 1;
	add2_opr1 <= add2_out; add2_opr2 <= add2_out; issub2 <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 0;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 2;
	ram_input_raddr1 <= `RAM_TZ0;
	ram_input_raddr2 <= `RAM_TZ1;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
14: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 1;
	add3_opr1 <= mm0_out_reg; add3_opr2 <= ram_mm0_out1; issub3 <= 0;
	add0_opr1 <= add1_out; add0_opr2 <= add1_out; issub0 <= 0;
	add1_opr1 <= add2_out; add1_opr2 <= add2_out_reg; issub1 <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 0;
	ram_add1_wr_n <= 1;
	ram_add0_raddr1 <= 0;
	ram_input_raddr1 <= `RAM_TX0;
	ram_input_raddr2 <= `RAM_TX1;
	state <= state + 1;
end
15: begin
	add1_opr1 <= mm0_out_reg; add1_opr2 <= mm0_out_reg; issub1 <= 0;
	add3_opr1 <= mm0_out_reg; add3_opr2 <= mm0_out_reg; issub3 <= 1;
	mm0_opr1 <= add2_out; mm0_opr2 <= ram_add0_out1; 
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_add0_wr_n <= 0;
	ram_add3_wr_n <= 0;
	ram_add3_waddr <= 0;
	ram_add0_waddr <= 1;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 0;
	ram_input_raddr1 <= `RAM_TZ0;
	ram_input_raddr2 <= `RAM_TZ1;
	ram_add1_raddr1 <= 0;
	state <= state + 1;
end
16: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 0;
	mm0_opr1 <= ram_add1_out1; mm0_opr2 <= add0_out; 
	ram_add3_wr_n <= 0;
	ram_add0_wr_n <= 1;
	ram_add1_wr_n <= 0;
	ram_add3_waddr <= 2;
	ram_add1_waddr <= 3;
	ram_input_raddr1 <= `RAM_TY0;
	ram_input_raddr2 <= `RAM_TY1;
	ram_add0_raddr1 <= 0;
	state <= state + 1;
end
17: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 1;
	mm0_opr1 <= ram_add0_out1; mm0_opr2 <= add2_out; 
	ram_add3_wr_n <= 1;
	ram_add1_wr_n <= 1;
	ram_input_raddr1 <= `RAM_TY0;
	ram_input_raddr2 <= `RAM_TY1;
	ram_add3_raddr1 <= 0;
	state <= state + 1;
end
18: begin
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 0;
	add0_opr1 <= mm0_out; add0_opr2 <= ram_add3_out1; issub0 <= 1;
	state <= state + 1;
end
19: begin
	mm0_opr1 <= add0_out_reg; mm0_opr2 <= add1_out; 
	add0_opr1 <= add0_out; add0_opr2 <= add0_out; issub0 <= 0;
	ram_add0_raddr1 <= 1;
	ram_input_raddr1 <= `RAM_BT1;
	ram_add1_raddr1 <= 1;
	state <= state + 1;
end
20: begin
	add3_opr1 <= ram_add0_out1; add3_opr2 <= add0_out; issub3 <= 0;
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= ram_add1_out1; 
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 4;
	ram_add1_raddr1 <= 0;
	ram_input_raddr1 <= `RAM_PX_;
	state <= state + 1;
end
21: begin
	mm0_opr1 <= ram_add1_out1; mm0_opr2 <= ram_input_out1; 
	ram_add0_wr_n <= 1;
	ram_add3_wr_n <= 0;
	ram_add3_waddr <= 3;
	ram_add3_raddr1 <= 1;
	ram_input_raddr1 <= `RAM_PY;
	ram_add2_raddr1 <= 0;
	state <= state + 1;
end
22: begin
	mm0_opr1 <= ram_add3_out1; mm0_opr2 <= ram_input_out1; 
	add0_opr1 <= mm0_out; add0_opr2 <= ram_add2_out1; issub0 <= 1;
	ram_add3_wr_n <= 1;
	ram_input_raddr1 <= `RAM_BT0;
	ram_add1_raddr1 <= 1;
	ram_add1_raddr2 <= 2;
	state <= state + 1;
end
23: begin
	mm0_opr1 <= ram_input_out1; mm0_opr2 <= add0_out; 
	add1_opr1 <= add0_out; add1_opr2 <= ram_add1_out1; issub1 <= 0;
	add3_opr1 <= mm0_out; add3_opr2 <= ram_add1_out2; issub3 <= 1;
	ram_add0_raddr1 <= 2;
	ram_add0_raddr2 <= 3;
	state <= state + 1;
end
24: begin
	add1_opr1 <= mm0_out; add1_opr2 <= ram_add0_out1; issub1 <= 1;
	mm0_opr1 <= ram_add0_out2; mm0_opr2 <= add1_out; 
	add0_opr1 <= add3_out; add0_opr2 <= add3_out; issub0 <= 0;
	state <= state + 1;
end
25: begin
	add0_opr1 <= add1_out; add0_opr2 <= add1_out; issub0 <= 0;
	add2_opr1 <= add0_out; add2_opr2 <= add3_out_reg; issub2 <= 0;
	ram_add3_raddr1 <= 2;
	ram_add1_raddr1 <= 3;
	ram_add3_raddr2 <= 1;
	state <= state + 1;
end
26: begin
	add2_opr1 <= mm0_out; add2_opr2 <= ram_add3_out1; issub2 <= 1;
	mm0_opr1 <= ram_add1_out1; mm0_opr2 <= add0_out; 
	add3_opr1 <= ram_add3_out2; add3_opr2 <= add0_out; issub3 <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 0;
	ram_add2_wr_n <= 0;
	ram_add2_waddr <= 1;
	ram_add3_raddr1 <= 1;
	ram_add1_raddr1 <= 3;
	state <= state + 1;
end
27: begin
	mm0_opr1 <= add2_out; mm0_opr2 <= ram_add3_out1; 
	add0_opr1 <= add2_out; add0_opr2 <= ram_add1_out1; issub0 <= 0;
	ram_add2_wr_n <= 0;
	ram_add2_waddr <= 0;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add0_wr_n <= 1;
	ram_add1_raddr1 <= 3;
	ram_add1_raddr2 <= 3;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd9;
	wdata_s1 <= `MM0;
	state <= state + 1;
end
28: begin
	mm0_opr1 <= add0_out; mm0_opr2 <= add3_out_reg; 
	add3_opr1 <= add2_out_reg; add3_opr2 <= ram_add1_out1; issub3 <= 1;
	add0_opr1 <= add2_out_reg; add0_opr2 <= ram_add1_out2; issub0 <= 0;
	ram_add2_wr_n <= 1;
	ram_mm0_wr_n <= 1;
	ram_add2_raddr1 <= 0;
	ram_add1_raddr1 <= 3;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd2;
	wdata_s1 <= `MM0;
	state <= state + 1;
end
29: begin
	mm0_opr1 <= ram_add2_out1; mm0_opr2 <= ram_add1_out1; 
	ram_mm0_raddr1 <= 0;
	w1_n_reg <= 1;
	state <= state + 1;
end
30: begin
	mm0_opr1 <= add3_out_reg; mm0_opr2 <= add0_out_reg; 
	add0_opr1 <= mm0_out; add0_opr2 <= ram_mm0_out1; issub0 <= 1;
	ram_add0_raddr1 <= 0;
	ram_input_raddr1 <= `RAM_PY;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
31: begin
	mm0_opr1 <= ram_add0_out1; mm0_opr2 <= ram_input_out1; 
	add0_opr1 <= mm0_out_reg; add0_opr2 <= ram_mm0_out1; issub0 <= 0;
	add2_opr1 <= add0_out; add2_opr2 <= add0_out; issub2 <= 0;
	ram_add2_raddr1 <= 1;
	ram_input_raddr1 <= `RAM_PX_;
	state <= state + 1;
end
32: begin
	mm0_opr1 <= ram_add2_out1; mm0_opr2 <= ram_input_out1; 
	add2_opr1 <= mm0_out_reg; add2_opr2 <= add0_out; issub2 <= 1;
	add1_opr1 <= add2_out; add1_opr2 <= add0_out_reg; issub1 <= 0;
	ram_add2_raddr1 <= 0;
	state <= state + 1;
end
33: begin
	add3_opr1 <= ram_add2_out1; add3_opr2 <= add1_out; issub3 <= 1;
	add0_opr1 <= add1_out; add0_opr2 <= add1_out; issub0 <= 0;
	add1_opr1 <= add2_out; add1_opr2 <= add2_out; issub1 <= 0;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 0;
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	ram_add2_raddr1 <= 0;
	state <= state + 1;
end
34: begin
	add1_opr1 <= mm0_out; add1_opr2 <= mm0_out_reg; issub1 <= 1;
	add2_opr1 <= add3_out; add2_opr2 <= add0_out; issub2 <= 1;
	add0_opr1 <= ram_add2_out1; add0_opr2 <= add3_out; issub0 <= 0;
	add3_opr1 <= add1_out; add3_opr2 <= add2_out_reg; issub3 <= 0;
	ram_add1_wr_n <= 1;
	ram_mm0_wr_n <= 1;
	ram_add1_raddr1 <= 0;
	ram_add1_raddr2 <= 3;
	ram_add0_raddr1 <= 1;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
35: begin
	add3_opr1 <= add0_out_reg; add3_opr2 <= ram_add1_out1; issub3 <= 0;
	add1_opr1 <= ram_add1_out2; add1_opr2 <= add3_out; issub1 <= 1;
	mm0_opr1 <= add2_out; mm0_opr2 <= ram_add0_out1; 
	add0_opr1 <= mm0_out_reg; add0_opr2 <= ram_mm0_out1; issub0 <= 0;
	add2_opr1 <= add3_out; add2_opr2 <= add3_out; issub2 <= 0;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 0;
	ram_add2_wr_n <= 0;
	ram_add2_waddr <= 0;
	ram_add1_raddr1 <= 3;
	state <= state + 1;
end
36: begin
	add0_opr1 <= add2_out; add0_opr2 <= add3_out_reg; issub0 <= 0;
	add2_opr1 <= mm0_out_reg; add2_opr2 <= add0_out; issub2 <= 1;
	add3_opr1 <= ram_add1_out1; add3_opr2 <= add1_out; issub3 <= 0;
	mm0_opr1 <= add3_out; mm0_opr2 <= add0_out_reg; 
	add1_opr1 <= mm0_out; add1_opr2 <= mm0_out; issub1 <= 1;
	ram_add1_wr_n <= 1;
	ram_add3_wr_n <= 0;
	ram_add3_waddr <= 0;
	ram_add0_wr_n <= 1;
	ram_add2_wr_n <= 1;
	state <= state + 1;
end
37: begin
	add2_opr1 <= add2_out; add2_opr2 <= add2_out; issub2 <= 0;
	add3_opr1 <= add1_out_reg; add3_opr2 <= add2_out_reg; issub3 <= 1;
	mm0_opr1 <= add0_out; mm0_opr2 <= add3_out; 
	add1_opr1 <= mm0_out; add1_opr2 <= add1_out; issub1 <= 1;
	add0_opr1 <= mm0_out_reg; add0_opr2 <= mm0_out_reg; issub0 <= 0;
	ram_add3_wr_n <= 1;
	ram_add1_raddr1 <= 0;
	ram_add3_raddr1 <= 0;
	ram_add0_raddr1 <= 0;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd3;
	wdata_s1 <= `MM0;
	state <= state + 1;
end
38: begin
	add0_opr1 <= add2_out; add0_opr2 <= add2_out; issub0 <= 0;
	add3_opr1 <= ram_add1_out1; add3_opr2 <= ram_add1_out1; issub3 <= 0;
	add2_opr1 <= ram_add3_out1; add2_opr2 <= add0_out_reg; issub2 <= 0;
	add1_opr1 <= ram_add0_out1; add1_opr2 <= add3_out_reg; issub1 <= 0;
	ram_add3_wr_n <= 0;
	ram_add3_waddr <= 0;
	ram_add1_wr_n <= 0;
	ram_add1_waddr <= 0;
	ram_add0_wr_n <= 0;
	ram_add0_waddr <= 0;
	ram_add2_raddr1 <= 0;
	w2_n_reg <= 0;
	waddr2_reg <= `RAM_TZ1;
	wdata_s2 <= `ADD0;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd8;
	wdata_s1 <= `MM0;
	state <= state + 1;
end
39: begin
	add2_opr1 <= ram_add2_out1; add2_opr2 <= add3_out_reg; issub2 <= 0;
	add1_opr1 <= add3_out; add1_opr2 <= add3_out; issub1 <= 0;
	mm0_opr1 <= add2_out; mm0_opr2 <= add1_out; 
	ram_add3_wr_n <= 1;
	ram_add1_wr_n <= 1;
	ram_add0_wr_n <= 1;
	ram_add3_raddr1 <= 0;
	ram_add0_raddr1 <= 4;
	w1_n_reg <= 0;
	waddr1_reg <= `RAM_TZ0;
	wdata_s1 <= `ADD1;
	w2_n_reg <= 1;
	state <= state + 1;
end
40: begin
	mm0_opr1 <= ram_add3_out1; mm0_opr2 <= ram_add0_out1; 
	ram_add3_raddr1 <= 3;
	w1_n_reg <= 1;
	state <= state + 1;
end
41: begin
	mm0_opr1 <= add2_out_reg; mm0_opr2 <= ram_add3_out1; 
	state <= state + 1;
end
42: begin
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 1;
	state <= state + 1;
end
43: begin
	ram_mm0_wr_n <= 0;
	ram_mm0_waddr <= 0;
	state <= state + 1;
end
44: begin
	add0_opr1 <= mm0_out_reg; add0_opr2 <= mm0_out; issub0 <= 1;
	ram_mm0_wr_n <= 1;
	ram_add1_raddr1 <= 0;
	ram_mm0_raddr1 <= 0;
	state <= state + 1;
end
45: begin
	add0_opr1 <= add0_out; add0_opr2 <= ram_add1_out1; issub0 <= 0;
	add2_opr1 <= ram_mm0_out1; add2_opr2 <= mm0_out_reg; issub2 <= 0;
	w1_n_reg <= 0;
	waddr1_reg <= `RAM_TY0;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
46: begin
	add0_opr1 <= mm0_out; add0_opr2 <= add2_out; issub0 <= 1;
	ram_mm0_raddr1 <= 1;
	ram_add0_raddr1 <= 0;
	w1_n_reg <= 1;
	state <= state + 1;
end
47: begin
	add0_opr1 <= ram_mm0_out1; add0_opr2 <= mm0_out; issub0 <= 1;
	add1_opr1 <= add0_out; add1_opr2 <= ram_add0_out1; issub1 <= 0;
	ram_mm0_raddr1 <= 1;
	w1_n_reg <= 0;
	waddr1_reg <= `RAM_TX0;
	wdata_s1 <= `ADD0;
	w2_n_reg <= 0;
	waddr2_reg <= `RAM_TY1;
	wdata_s2 <= `ADD1;
	state <= state + 1;
end
48: begin
	add1_opr1 <= ram_mm0_out1; add1_opr2 <= mm0_out_reg; issub1 <= 0;
	w1_n_reg <= 1;
	w2_n_reg <= 1;
	state <= state + 1;
end
49: begin
	add0_opr1 <= mm0_out_reg; add0_opr2 <= add1_out; issub0 <= 1;
	w1_n_reg <= 0;
	waddr1_reg <= `RAM_TX1;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
50: begin
	w1_n_reg <= 1;
	state <= 0;
end
endcase
