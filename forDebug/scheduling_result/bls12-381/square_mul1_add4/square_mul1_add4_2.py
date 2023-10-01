from pyschedule import Scenario, solvers, plotters, alt

def solve_square_mul1_add4_2(ConstStep, ExpStep):
	horizon = 131
	S=Scenario("square_mul1_add4_2",horizon = horizon)

	# resource
	MUL = S.Resources('MUL', num=1, size=7)
	MUL_in = S.Resources('MUL_in', num=1)
	INV = S.Resource('INV')
	ADD = S.Resources('ADD', num=4, periods=range(1, horizon))
	MUL_mem = S.Resources('MUL_mem', num=1, size=2)
	ADD_mem = S.Resources('ADD_mem', num=4, size=2)
	INPUT_mem_w = S.Resource('INPUT_mem_w', size=2)
	INPUT_mem_r = S.Resource('INPUT_mem_r', size=2)

	# result of previous scheduling
	T8_1T0_in = S.Task('T8_1T0_in', length=1, delay_cost=1)
	S += T8_1T0_in >= 0
	T8_1T0_in += MUL_in[0]

	T8_1T0_mem0 = S.Task('T8_1T0_mem0', length=1, delay_cost=1)
	S += T8_1T0_mem0 >= 0
	T8_1T0_mem0 += INPUT_mem_r

	T8_1T0_mem1 = S.Task('T8_1T0_mem1', length=1, delay_cost=1)
	S += T8_1T0_mem1 >= 0
	T8_1T0_mem1 += INPUT_mem_r

	T7_T1_in = S.Task('T7_T1_in', length=1, delay_cost=1)
	S += T7_T1_in >= 1
	T7_T1_in += MUL_in[0]

	T7_T1_mem0 = S.Task('T7_T1_mem0', length=1, delay_cost=1)
	S += T7_T1_mem0 >= 1
	T7_T1_mem0 += INPUT_mem_r

	T7_T1_mem1 = S.Task('T7_T1_mem1', length=1, delay_cost=1)
	S += T7_T1_mem1 >= 1
	T7_T1_mem1 += INPUT_mem_r

	T8_1T0 = S.Task('T8_1T0', length=7, delay_cost=1)
	S += T8_1T0 >= 1
	T8_1T0 += MUL[0]

	T7_T1 = S.Task('T7_T1', length=7, delay_cost=1)
	S += T7_T1 >= 2
	T7_T1 += MUL[0]

	T8_1T1_in = S.Task('T8_1T1_in', length=1, delay_cost=1)
	S += T8_1T1_in >= 2
	T8_1T1_in += MUL_in[0]

	T8_1T1_mem0 = S.Task('T8_1T1_mem0', length=1, delay_cost=1)
	S += T8_1T1_mem0 >= 2
	T8_1T1_mem0 += INPUT_mem_r

	T8_1T1_mem1 = S.Task('T8_1T1_mem1', length=1, delay_cost=1)
	S += T8_1T1_mem1 >= 2
	T8_1T1_mem1 += INPUT_mem_r

	T7_T0_in = S.Task('T7_T0_in', length=1, delay_cost=1)
	S += T7_T0_in >= 3
	T7_T0_in += MUL_in[0]

	T7_T0_mem0 = S.Task('T7_T0_mem0', length=1, delay_cost=1)
	S += T7_T0_mem0 >= 3
	T7_T0_mem0 += INPUT_mem_r

	T7_T0_mem1 = S.Task('T7_T0_mem1', length=1, delay_cost=1)
	S += T7_T0_mem1 >= 3
	T7_T0_mem1 += INPUT_mem_r

	T8_1T1 = S.Task('T8_1T1', length=7, delay_cost=1)
	S += T8_1T1 >= 3
	T8_1T1 += MUL[0]

	T6_T1_in = S.Task('T6_T1_in', length=1, delay_cost=1)
	S += T6_T1_in >= 4
	T6_T1_in += MUL_in[0]

	T6_T1_mem0 = S.Task('T6_T1_mem0', length=1, delay_cost=1)
	S += T6_T1_mem0 >= 4
	T6_T1_mem0 += INPUT_mem_r

	T6_T1_mem1 = S.Task('T6_T1_mem1', length=1, delay_cost=1)
	S += T6_T1_mem1 >= 4
	T6_T1_mem1 += INPUT_mem_r

	T7_T0 = S.Task('T7_T0', length=7, delay_cost=1)
	S += T7_T0 >= 4
	T7_T0 += MUL[0]

	T6_T0_in = S.Task('T6_T0_in', length=1, delay_cost=1)
	S += T6_T0_in >= 5
	T6_T0_in += MUL_in[0]

	T6_T0_mem0 = S.Task('T6_T0_mem0', length=1, delay_cost=1)
	S += T6_T0_mem0 >= 5
	T6_T0_mem0 += INPUT_mem_r

	T6_T0_mem1 = S.Task('T6_T0_mem1', length=1, delay_cost=1)
	S += T6_T0_mem1 >= 5
	T6_T0_mem1 += INPUT_mem_r

	T6_T1 = S.Task('T6_T1', length=7, delay_cost=1)
	S += T6_T1 >= 5
	T6_T1 += MUL[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 6
	T41_mem0 += INPUT_mem_r

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 6
	T41_mem1 += INPUT_mem_r

	T6_T0 = S.Task('T6_T0', length=7, delay_cost=1)
	S += T6_T0 >= 6
	T6_T0 += MUL[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 7
	T41 += ADD[1]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 7
	T50_mem0 += INPUT_mem_r

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 7
	T50_mem1 += INPUT_mem_r

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 8
	T21_mem0 += INPUT_mem_r

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 8
	T21_mem1 += INPUT_mem_r

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 8
	T50 += ADD[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 9
	T21 += ADD[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 9
	T40_mem0 += INPUT_mem_r

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 9
	T40_mem1 += INPUT_mem_r

	T8_10_mem0 = S.Task('T8_10_mem0', length=1, delay_cost=1)
	S += T8_10_mem0 >= 9
	T8_10_mem0 += MUL_mem[0]

	T8_10_mem1 = S.Task('T8_10_mem1', length=1, delay_cost=1)
	S += T8_10_mem1 >= 9
	T8_10_mem1 += MUL_mem[0]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 10
	T40 += ADD[3]

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	S += T4_0_mem0 >= 10
	T4_0_mem0 += ADD_mem[3]

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	S += T4_0_mem1 >= 10
	T4_0_mem1 += ADD_mem[0]

	T4_10_mem0 = S.Task('T4_10_mem0', length=1, delay_cost=1)
	S += T4_10_mem0 >= 10
	T4_10_mem0 += INPUT_mem_r

	T4_10_mem1 = S.Task('T4_10_mem1', length=1, delay_cost=1)
	S += T4_10_mem1 >= 10
	T4_10_mem1 += INPUT_mem_r

	T7T3_mem0 = S.Task('T7T3_mem0', length=1, delay_cost=1)
	S += T7T3_mem0 >= 10
	T7T3_mem0 += ADD_mem[3]

	T7T3_mem1 = S.Task('T7T3_mem1', length=1, delay_cost=1)
	S += T7T3_mem1 >= 10
	T7T3_mem1 += ADD_mem[1]

	T7_0_mem0 = S.Task('T7_0_mem0', length=1, delay_cost=1)
	S += T7_0_mem0 >= 10
	T7_0_mem0 += MUL_mem[0]

	T7_0_mem1 = S.Task('T7_0_mem1', length=1, delay_cost=1)
	S += T7_0_mem1 >= 10
	T7_0_mem1 += MUL_mem[0]

	T8_10 = S.Task('T8_10', length=1, delay_cost=1)
	S += T8_10 >= 10
	T8_10 += ADD[0]

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	S += T4_0 >= 11
	T4_0 += ADD[3]

	T4_10 = S.Task('T4_10', length=1, delay_cost=1)
	S += T4_10 >= 11
	T4_10 += ADD[0]

	T4_11_mem0 = S.Task('T4_11_mem0', length=1, delay_cost=1)
	S += T4_11_mem0 >= 11
	T4_11_mem0 += INPUT_mem_r

	T4_11_mem1 = S.Task('T4_11_mem1', length=1, delay_cost=1)
	S += T4_11_mem1 >= 11
	T4_11_mem1 += INPUT_mem_r

	T7T3 = S.Task('T7T3', length=1, delay_cost=1)
	S += T7T3 >= 11
	T7T3 += ADD[2]

	T7_0 = S.Task('T7_0', length=1, delay_cost=1)
	S += T7_0 >= 11
	T7_0 += ADD[1]

	T8_1T5_mem0 = S.Task('T8_1T5_mem0', length=1, delay_cost=1)
	S += T8_1T5_mem0 >= 11
	T8_1T5_mem0 += MUL_mem[0]

	T8_1T5_mem1 = S.Task('T8_1T5_mem1', length=1, delay_cost=1)
	S += T8_1T5_mem1 >= 11
	T8_1T5_mem1 += MUL_mem[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 12
	T20_mem0 += INPUT_mem_r

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 12
	T20_mem1 += INPUT_mem_r

	T3_1T3_mem0 = S.Task('T3_1T3_mem0', length=1, delay_cost=1)
	S += T3_1T3_mem0 >= 12
	T3_1T3_mem0 += ADD_mem[0]

	T3_1T3_mem1 = S.Task('T3_1T3_mem1', length=1, delay_cost=1)
	S += T3_1T3_mem1 >= 12
	T3_1T3_mem1 += ADD_mem[1]

	T4_11 = S.Task('T4_11', length=1, delay_cost=1)
	S += T4_11 >= 12
	T4_11 += ADD[1]

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	S += T6_0_mem0 >= 12
	T6_0_mem0 += MUL_mem[0]

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	S += T6_0_mem1 >= 12
	T6_0_mem1 += MUL_mem[0]

	T8_1T5 = S.Task('T8_1T5', length=1, delay_cost=1)
	S += T8_1T5 >= 12
	T8_1T5 += ADD[3]

	T10_0_mem0 = S.Task('T10_0_mem0', length=1, delay_cost=1)
	S += T10_0_mem0 >= 13
	T10_0_mem0 += INPUT_mem_r

	T10_0_mem1 = S.Task('T10_0_mem1', length=1, delay_cost=1)
	S += T10_0_mem1 >= 13
	T10_0_mem1 += INPUT_mem_r

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 13
	T20 += ADD[0]

	T3_1T3 = S.Task('T3_1T3', length=1, delay_cost=1)
	S += T3_1T3 >= 13
	T3_1T3 += ADD[3]

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	S += T6_0 >= 13
	T6_0 += ADD[1]

	T6_T5_mem0 = S.Task('T6_T5_mem0', length=1, delay_cost=1)
	S += T6_T5_mem0 >= 13
	T6_T5_mem0 += MUL_mem[0]

	T6_T5_mem1 = S.Task('T6_T5_mem1', length=1, delay_cost=1)
	S += T6_T5_mem1 >= 13
	T6_T5_mem1 += MUL_mem[0]

	T8T0_in = S.Task('T8T0_in', length=1, delay_cost=1)
	S += T8T0_in >= 13
	T8T0_in += MUL_in[0]

	T8T0_mem0 = S.Task('T8T0_mem0', length=1, delay_cost=1)
	S += T8T0_mem0 >= 13
	T8T0_mem0 += ADD_mem[0]

	T8T0_mem1 = S.Task('T8T0_mem1', length=1, delay_cost=1)
	S += T8T0_mem1 >= 13
	T8T0_mem1 += ADD_mem[0]

	T10_0 = S.Task('T10_0', length=1, delay_cost=1)
	S += T10_0 >= 14
	T10_0 += ADD[0]

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	S += T5_11_mem0 >= 14
	T5_11_mem0 += INPUT_mem_r

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	S += T5_11_mem1 >= 14
	T5_11_mem1 += INPUT_mem_r

	T6_T5 = S.Task('T6_T5', length=1, delay_cost=1)
	S += T6_T5 >= 14
	T6_T5 += ADD[2]

	T7_T5_mem0 = S.Task('T7_T5_mem0', length=1, delay_cost=1)
	S += T7_T5_mem0 >= 14
	T7_T5_mem0 += MUL_mem[0]

	T7_T5_mem1 = S.Task('T7_T5_mem1', length=1, delay_cost=1)
	S += T7_T5_mem1 >= 14
	T7_T5_mem1 += MUL_mem[0]

	T8T0 = S.Task('T8T0', length=7, delay_cost=1)
	S += T8T0 >= 14
	T8T0 += MUL[0]

	T8T2_mem0 = S.Task('T8T2_mem0', length=1, delay_cost=1)
	S += T8T2_mem0 >= 14
	T8T2_mem0 += ADD_mem[0]

	T8T2_mem1 = S.Task('T8T2_mem1', length=1, delay_cost=1)
	S += T8T2_mem1 >= 14
	T8T2_mem1 += ADD_mem[0]

	T10_1_mem0 = S.Task('T10_1_mem0', length=1, delay_cost=1)
	S += T10_1_mem0 >= 15
	T10_1_mem0 += INPUT_mem_r

	T10_1_mem1 = S.Task('T10_1_mem1', length=1, delay_cost=1)
	S += T10_1_mem1 >= 15
	T10_1_mem1 += INPUT_mem_r

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	S += T5_11 >= 15
	T5_11 += ADD[2]

	T7_T5 = S.Task('T7_T5', length=1, delay_cost=1)
	S += T7_T5 >= 15
	T7_T5 += ADD[3]

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	S += T8T2 >= 15
	T8T2 += ADD[1]

	T10_1 = S.Task('T10_1', length=1, delay_cost=1)
	S += T10_1 >= 16
	T10_1 += ADD[3]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 16
	T30_mem0 += INPUT_mem_r

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 16
	T30_mem1 += INPUT_mem_r

	T9_4T3_mem0 = S.Task('T9_4T3_mem0', length=1, delay_cost=1)
	S += T9_4T3_mem0 >= 16
	T9_4T3_mem0 += ADD_mem[0]

	T9_4T3_mem1 = S.Task('T9_4T3_mem1', length=1, delay_cost=1)
	S += T9_4T3_mem1 >= 16
	T9_4T3_mem1 += ADD_mem[3]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 17
	T00_mem0 += INPUT_mem_r

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 17
	T00_mem1 += INPUT_mem_r

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 17
	T100_mem0 += ADD_mem[0]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 17
	T100_mem1 += ADD_mem[3]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 17
	T30 += ADD[0]

	T9_4T3 = S.Task('T9_4T3', length=1, delay_cost=1)
	S += T9_4T3 >= 17
	T9_4T3 += ADD[2]

	T00 = S.Task('T00', length=1, delay_cost=1)
	S += T00 >= 18
	T00 += ADD[0]

	T100 = S.Task('T100', length=1, delay_cost=1)
	S += T100 >= 18
	T100 += ADD[3]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 18
	T3_0_mem0 += INPUT_mem_r

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 18
	T3_0_mem1 += INPUT_mem_r

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	S += T5_0_mem0 >= 18
	T5_0_mem0 += ADD_mem[0]

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	S += T5_0_mem1 >= 18
	T5_0_mem1 += ADD_mem[0]

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 19
	T3_0 += ADD[0]

	T3_1T0_in = S.Task('T3_1T0_in', length=1, delay_cost=1)
	S += T3_1T0_in >= 19
	T3_1T0_in += MUL_in[0]

	T3_1T0_mem0 = S.Task('T3_1T0_mem0', length=1, delay_cost=1)
	S += T3_1T0_mem0 >= 19
	T3_1T0_mem0 += ADD_mem[0]

	T3_1T0_mem1 = S.Task('T3_1T0_mem1', length=1, delay_cost=1)
	S += T3_1T0_mem1 >= 19
	T3_1T0_mem1 += ADD_mem[0]

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	S += T5_0 >= 19
	T5_0 += ADD[2]

	T9_31_mem0 = S.Task('T9_31_mem0', length=1, delay_cost=1)
	S += T9_31_mem0 >= 19
	T9_31_mem0 += INPUT_mem_r

	T9_31_mem1 = S.Task('T9_31_mem1', length=1, delay_cost=1)
	S += T9_31_mem1 >= 19
	T9_31_mem1 += INPUT_mem_r

	T3_1T0 = S.Task('T3_1T0', length=7, delay_cost=1)
	S += T3_1T0 >= 20
	T3_1T0 += MUL[0]

	T8_1T3_mem0 = S.Task('T8_1T3_mem0', length=1, delay_cost=1)
	S += T8_1T3_mem0 >= 20
	T8_1T3_mem0 += INPUT_mem_r

	T8_1T3_mem1 = S.Task('T8_1T3_mem1', length=1, delay_cost=1)
	S += T8_1T3_mem1 >= 20
	T8_1T3_mem1 += INPUT_mem_r

	T9_31 = S.Task('T9_31', length=1, delay_cost=1)
	S += T9_31 >= 20
	T9_31 += ADD[0]

	T9_4T1_in = S.Task('T9_4T1_in', length=1, delay_cost=1)
	S += T9_4T1_in >= 20
	T9_4T1_in += MUL_in[0]

	T9_4T1_mem0 = S.Task('T9_4T1_mem0', length=1, delay_cost=1)
	S += T9_4T1_mem0 >= 20
	T9_4T1_mem0 += ADD_mem[0]

	T9_4T1_mem1 = S.Task('T9_4T1_mem1', length=1, delay_cost=1)
	S += T9_4T1_mem1 >= 20
	T9_4T1_mem1 += ADD_mem[3]

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	S += T3_1_mem0 >= 21
	T3_1_mem0 += INPUT_mem_r

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	S += T3_1_mem1 >= 21
	T3_1_mem1 += INPUT_mem_r

	T8_1T3 = S.Task('T8_1T3', length=1, delay_cost=1)
	S += T8_1T3 >= 21
	T8_1T3 += ADD[2]

	T9_4T1 = S.Task('T9_4T1', length=7, delay_cost=1)
	S += T9_4T1 >= 21
	T9_4T1 += MUL[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 22
	T31_mem0 += INPUT_mem_r

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 22
	T31_mem1 += INPUT_mem_r

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 22
	T3_1 += ADD[0]

	T3_1T1_in = S.Task('T3_1T1_in', length=1, delay_cost=1)
	S += T3_1T1_in >= 22
	T3_1T1_in += MUL_in[0]

	T3_1T1_mem0 = S.Task('T3_1T1_mem0', length=1, delay_cost=1)
	S += T3_1T1_mem0 >= 22
	T3_1T1_mem0 += ADD_mem[0]

	T3_1T1_mem1 = S.Task('T3_1T1_mem1', length=1, delay_cost=1)
	S += T3_1T1_mem1 >= 22
	T3_1T1_mem1 += ADD_mem[1]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 23
	T101_mem0 += ADD_mem[1]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 23
	T101_mem1 += ADD_mem[1]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 23
	T31 += ADD[1]

	T3_1T1 = S.Task('T3_1T1', length=7, delay_cost=1)
	S += T3_1T1 >= 23
	T3_1T1 += MUL[0]

	T3_1T2_mem0 = S.Task('T3_1T2_mem0', length=1, delay_cost=1)
	S += T3_1T2_mem0 >= 23
	T3_1T2_mem0 += ADD_mem[0]

	T3_1T2_mem1 = S.Task('T3_1T2_mem1', length=1, delay_cost=1)
	S += T3_1T2_mem1 >= 23
	T3_1T2_mem1 += ADD_mem[0]

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	S += T5_10_mem0 >= 23
	T5_10_mem0 += INPUT_mem_r

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	S += T5_10_mem1 >= 23
	T5_10_mem1 += INPUT_mem_r

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 24
	T101 += ADD[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 24
	T11_mem0 += INPUT_mem_r

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 24
	T11_mem1 += INPUT_mem_r

	T3_1T2 = S.Task('T3_1T2', length=1, delay_cost=1)
	S += T3_1T2 >= 24
	T3_1T2 += ADD[2]

	T4_3T3_mem0 = S.Task('T4_3T3_mem0', length=1, delay_cost=1)
	S += T4_3T3_mem0 >= 24
	T4_3T3_mem0 += ADD_mem[1]

	T4_3T3_mem1 = S.Task('T4_3T3_mem1', length=1, delay_cost=1)
	S += T4_3T3_mem1 >= 24
	T4_3T3_mem1 += ADD_mem[2]

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	S += T5_10 >= 24
	T5_10 += ADD[1]

	T6T3_mem0 = S.Task('T6T3_mem0', length=1, delay_cost=1)
	S += T6T3_mem0 >= 24
	T6T3_mem0 += ADD_mem[0]

	T6T3_mem1 = S.Task('T6T3_mem1', length=1, delay_cost=1)
	S += T6T3_mem1 >= 24
	T6T3_mem1 += ADD_mem[1]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 25
	T10_mem0 += INPUT_mem_r

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 25
	T10_mem1 += INPUT_mem_r

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 25
	T11 += ADD[1]

	T4_3T3 = S.Task('T4_3T3', length=1, delay_cost=1)
	S += T4_3T3 >= 25
	T4_3T3 += ADD[0]

	T6T3 = S.Task('T6T3', length=1, delay_cost=1)
	S += T6T3 >= 25
	T6T3 += ADD[2]

	T7T1_in = S.Task('T7T1_in', length=1, delay_cost=1)
	S += T7T1_in >= 25
	T7T1_in += MUL_in[0]

	T7T1_mem0 = S.Task('T7T1_mem0', length=1, delay_cost=1)
	S += T7T1_mem0 >= 25
	T7T1_mem0 += ADD_mem[1]

	T7T1_mem1 = S.Task('T7T1_mem1', length=1, delay_cost=1)
	S += T7T1_mem1 >= 25
	T7T1_mem1 += ADD_mem[1]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 26
	T10 += ADD[0]

	T7T0_in = S.Task('T7T0_in', length=1, delay_cost=1)
	S += T7T0_in >= 26
	T7T0_in += MUL_in[0]

	T7T0_mem0 = S.Task('T7T0_mem0', length=1, delay_cost=1)
	S += T7T0_mem0 >= 26
	T7T0_mem0 += ADD_mem[0]

	T7T0_mem1 = S.Task('T7T0_mem1', length=1, delay_cost=1)
	S += T7T0_mem1 >= 26
	T7T0_mem1 += ADD_mem[3]

	T7T1 = S.Task('T7T1', length=7, delay_cost=1)
	S += T7T1 >= 26
	T7T1 += MUL[0]

	T7T2_mem0 = S.Task('T7T2_mem0', length=1, delay_cost=1)
	S += T7T2_mem0 >= 26
	T7T2_mem0 += ADD_mem[0]

	T7T2_mem1 = S.Task('T7T2_mem1', length=1, delay_cost=1)
	S += T7T2_mem1 >= 26
	T7T2_mem1 += ADD_mem[1]

	T9_30_mem0 = S.Task('T9_30_mem0', length=1, delay_cost=1)
	S += T9_30_mem0 >= 26
	T9_30_mem0 += INPUT_mem_r

	T9_30_mem1 = S.Task('T9_30_mem1', length=1, delay_cost=1)
	S += T9_30_mem1 >= 26
	T9_30_mem1 += INPUT_mem_r

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 27
	T1_1_mem0 += ADD_mem[1]

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	S += T1_1_mem1 >= 27
	T1_1_mem1 += ADD_mem[0]

	T7T0 = S.Task('T7T0', length=7, delay_cost=1)
	S += T7T0 >= 27
	T7T0 += MUL[0]

	T7T2 = S.Task('T7T2', length=1, delay_cost=1)
	S += T7T2 >= 27
	T7T2 += ADD[0]

	T8_1T2_mem0 = S.Task('T8_1T2_mem0', length=1, delay_cost=1)
	S += T8_1T2_mem0 >= 27
	T8_1T2_mem0 += INPUT_mem_r

	T8_1T2_mem1 = S.Task('T8_1T2_mem1', length=1, delay_cost=1)
	S += T8_1T2_mem1 >= 27
	T8_1T2_mem1 += INPUT_mem_r

	T9_30 = S.Task('T9_30', length=1, delay_cost=1)
	S += T9_30 >= 27
	T9_30 += ADD[2]

	T9_4T0_in = S.Task('T9_4T0_in', length=1, delay_cost=1)
	S += T9_4T0_in >= 27
	T9_4T0_in += MUL_in[0]

	T9_4T0_mem0 = S.Task('T9_4T0_mem0', length=1, delay_cost=1)
	S += T9_4T0_mem0 >= 27
	T9_4T0_mem0 += ADD_mem[2]

	T9_4T0_mem1 = S.Task('T9_4T0_mem1', length=1, delay_cost=1)
	S += T9_4T0_mem1 >= 27
	T9_4T0_mem1 += ADD_mem[0]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 28
	T1_0_mem0 += ADD_mem[0]

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 28
	T1_0_mem1 += ADD_mem[0]

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 28
	T1_1 += ADD[2]

	T4_20_mem0 = S.Task('T4_20_mem0', length=1, delay_cost=1)
	S += T4_20_mem0 >= 28
	T4_20_mem0 += INPUT_mem_r

	T4_20_mem1 = S.Task('T4_20_mem1', length=1, delay_cost=1)
	S += T4_20_mem1 >= 28
	T4_20_mem1 += INPUT_mem_r

	T8_1T2 = S.Task('T8_1T2', length=1, delay_cost=1)
	S += T8_1T2 >= 28
	T8_1T2 += ADD[1]

	T8_1T4_in = S.Task('T8_1T4_in', length=1, delay_cost=1)
	S += T8_1T4_in >= 28
	T8_1T4_in += MUL_in[0]

	T8_1T4_mem0 = S.Task('T8_1T4_mem0', length=1, delay_cost=1)
	S += T8_1T4_mem0 >= 28
	T8_1T4_mem0 += ADD_mem[1]

	T8_1T4_mem1 = S.Task('T8_1T4_mem1', length=1, delay_cost=1)
	S += T8_1T4_mem1 >= 28
	T8_1T4_mem1 += ADD_mem[2]

	T9_4T0 = S.Task('T9_4T0', length=7, delay_cost=1)
	S += T9_4T0 >= 28
	T9_4T0 += MUL[0]

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	S += T1_0 >= 29
	T1_0 += ADD[2]

	T4_20 = S.Task('T4_20', length=1, delay_cost=1)
	S += T4_20 >= 29
	T4_20 += ADD[0]

	T4_21_mem0 = S.Task('T4_21_mem0', length=1, delay_cost=1)
	S += T4_21_mem0 >= 29
	T4_21_mem0 += INPUT_mem_r

	T4_21_mem1 = S.Task('T4_21_mem1', length=1, delay_cost=1)
	S += T4_21_mem1 >= 29
	T4_21_mem1 += INPUT_mem_r

	T4_3T0_in = S.Task('T4_3T0_in', length=1, delay_cost=1)
	S += T4_3T0_in >= 29
	T4_3T0_in += MUL_in[0]

	T4_3T0_mem0 = S.Task('T4_3T0_mem0', length=1, delay_cost=1)
	S += T4_3T0_mem0 >= 29
	T4_3T0_mem0 += ADD_mem[0]

	T4_3T0_mem1 = S.Task('T4_3T0_mem1', length=1, delay_cost=1)
	S += T4_3T0_mem1 >= 29
	T4_3T0_mem1 += ADD_mem[1]

	T8_1T4 = S.Task('T8_1T4', length=7, delay_cost=1)
	S += T8_1T4 >= 29
	T8_1T4 += MUL[0]

	T9_4T2_mem0 = S.Task('T9_4T2_mem0', length=1, delay_cost=1)
	S += T9_4T2_mem0 >= 29
	T9_4T2_mem0 += ADD_mem[2]

	T9_4T2_mem1 = S.Task('T9_4T2_mem1', length=1, delay_cost=1)
	S += T9_4T2_mem1 >= 29
	T9_4T2_mem1 += ADD_mem[0]

	T4_21 = S.Task('T4_21', length=1, delay_cost=1)
	S += T4_21 >= 30
	T4_21 += ADD[0]

	T4_3T0 = S.Task('T4_3T0', length=7, delay_cost=1)
	S += T4_3T0 >= 30
	T4_3T0 += MUL[0]

	T4_3T1_in = S.Task('T4_3T1_in', length=1, delay_cost=1)
	S += T4_3T1_in >= 30
	T4_3T1_in += MUL_in[0]

	T4_3T1_mem0 = S.Task('T4_3T1_mem0', length=1, delay_cost=1)
	S += T4_3T1_mem0 >= 30
	T4_3T1_mem0 += ADD_mem[0]

	T4_3T1_mem1 = S.Task('T4_3T1_mem1', length=1, delay_cost=1)
	S += T4_3T1_mem1 >= 30
	T4_3T1_mem1 += ADD_mem[2]

	T7_T3_mem0 = S.Task('T7_T3_mem0', length=1, delay_cost=1)
	S += T7_T3_mem0 >= 30
	T7_T3_mem0 += INPUT_mem_r

	T7_T3_mem1 = S.Task('T7_T3_mem1', length=1, delay_cost=1)
	S += T7_T3_mem1 >= 30
	T7_T3_mem1 += INPUT_mem_r

	T9_4T2 = S.Task('T9_4T2', length=1, delay_cost=1)
	S += T9_4T2 >= 30
	T9_4T2 += ADD[3]

	T4_3T1 = S.Task('T4_3T1', length=7, delay_cost=1)
	S += T4_3T1 >= 31
	T4_3T1 += MUL[0]

	T4_3T2_mem0 = S.Task('T4_3T2_mem0', length=1, delay_cost=1)
	S += T4_3T2_mem0 >= 31
	T4_3T2_mem0 += ADD_mem[0]

	T4_3T2_mem1 = S.Task('T4_3T2_mem1', length=1, delay_cost=1)
	S += T4_3T2_mem1 >= 31
	T4_3T2_mem1 += ADD_mem[0]

	T7_T2_mem0 = S.Task('T7_T2_mem0', length=1, delay_cost=1)
	S += T7_T2_mem0 >= 31
	T7_T2_mem0 += INPUT_mem_r

	T7_T2_mem1 = S.Task('T7_T2_mem1', length=1, delay_cost=1)
	S += T7_T2_mem1 >= 31
	T7_T2_mem1 += INPUT_mem_r

	T7_T3 = S.Task('T7_T3', length=1, delay_cost=1)
	S += T7_T3 >= 31
	T7_T3 += ADD[3]

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 32
	T01_mem0 += INPUT_mem_r

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	S += T01_mem1 >= 32
	T01_mem1 += INPUT_mem_r

	T4_3T2 = S.Task('T4_3T2', length=1, delay_cost=1)
	S += T4_3T2 >= 32
	T4_3T2 += ADD[2]

	T7_T2 = S.Task('T7_T2', length=1, delay_cost=1)
	S += T7_T2 >= 32
	T7_T2 += ADD[1]

	T7_T4_in = S.Task('T7_T4_in', length=1, delay_cost=1)
	S += T7_T4_in >= 32
	T7_T4_in += MUL_in[0]

	T7_T4_mem0 = S.Task('T7_T4_mem0', length=1, delay_cost=1)
	S += T7_T4_mem0 >= 32
	T7_T4_mem0 += ADD_mem[1]

	T7_T4_mem1 = S.Task('T7_T4_mem1', length=1, delay_cost=1)
	S += T7_T4_mem1 >= 32
	T7_T4_mem1 += ADD_mem[3]

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 33
	T01 += ADD[2]

	T6_T3_mem0 = S.Task('T6_T3_mem0', length=1, delay_cost=1)
	S += T6_T3_mem0 >= 33
	T6_T3_mem0 += INPUT_mem_r

	T6_T3_mem1 = S.Task('T6_T3_mem1', length=1, delay_cost=1)
	S += T6_T3_mem1 >= 33
	T6_T3_mem1 += INPUT_mem_r

	T7_T4 = S.Task('T7_T4', length=7, delay_cost=1)
	S += T7_T4 >= 33
	T7_T4 += MUL[0]

	T6_T2_mem0 = S.Task('T6_T2_mem0', length=1, delay_cost=1)
	S += T6_T2_mem0 >= 34
	T6_T2_mem0 += INPUT_mem_r

	T6_T2_mem1 = S.Task('T6_T2_mem1', length=1, delay_cost=1)
	S += T6_T2_mem1 >= 34
	T6_T2_mem1 += INPUT_mem_r

	T6_T3 = S.Task('T6_T3', length=1, delay_cost=1)
	S += T6_T3 >= 34
	T6_T3 += ADD[0]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 35
	T51_mem0 += INPUT_mem_r

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 35
	T51_mem1 += INPUT_mem_r

	T6_T2 = S.Task('T6_T2', length=1, delay_cost=1)
	S += T6_T2 >= 35
	T6_T2 += ADD[2]

	T6_T4_in = S.Task('T6_T4_in', length=1, delay_cost=1)
	S += T6_T4_in >= 35
	T6_T4_in += MUL_in[0]

	T6_T4_mem0 = S.Task('T6_T4_mem0', length=1, delay_cost=1)
	S += T6_T4_mem0 >= 35
	T6_T4_mem0 += ADD_mem[2]

	T6_T4_mem1 = S.Task('T6_T4_mem1', length=1, delay_cost=1)
	S += T6_T4_mem1 >= 35
	T6_T4_mem1 += ADD_mem[0]

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	S += T0_1_mem0 >= 36
	T0_1_mem0 += INPUT_mem_r

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	S += T0_1_mem1 >= 36
	T0_1_mem1 += ADD_mem[2]

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	S += T4_1_mem0 >= 36
	T4_1_mem0 += ADD_mem[1]

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	S += T4_1_mem1 >= 36
	T4_1_mem1 += ADD_mem[0]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 36
	T51 += ADD[0]

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	S += T5_1_mem0 >= 36
	T5_1_mem0 += ADD_mem[1]

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	S += T5_1_mem1 >= 36
	T5_1_mem1 += ADD_mem[0]

	T6_T4 = S.Task('T6_T4', length=7, delay_cost=1)
	S += T6_T4 >= 36
	T6_T4 += MUL[0]

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	S += T0_1 >= 37
	T0_1 += ADD[0]

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	S += T4_1 >= 37
	T4_1 += ADD[2]

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	S += T5_1 >= 37
	T5_1 += ADD[1]

	T8T1_in = S.Task('T8T1_in', length=1, delay_cost=1)
	S += T8T1_in >= 37
	T8T1_in += MUL_in[0]

	T8T1_mem0 = S.Task('T8T1_mem0', length=1, delay_cost=1)
	S += T8T1_mem0 >= 37
	T8T1_mem0 += ADD_mem[0]

	T8T1_mem1 = S.Task('T8T1_mem1', length=1, delay_cost=1)
	S += T8T1_mem1 >= 37
	T8T1_mem1 += ADD_mem[0]

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	S += T0_0_mem0 >= 38
	T0_0_mem0 += INPUT_mem_r

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	S += T0_0_mem1 >= 38
	T0_0_mem1 += ADD_mem[0]

	T8T1 = S.Task('T8T1', length=7, delay_cost=1)
	S += T8T1 >= 38
	T8T1 += MUL[0]

	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	S += T0_0 >= 39
	T0_0 += ADD[0]

	T8T3_mem0 = S.Task('T8T3_mem0', length=1, delay_cost=1)
	S += T8T3_mem0 >= 39
	T8T3_mem0 += ADD_mem[0]

	T8T3_mem1 = S.Task('T8T3_mem1', length=1, delay_cost=1)
	S += T8T3_mem1 >= 39
	T8T3_mem1 += ADD_mem[0]

	T8T3 = S.Task('T8T3', length=1, delay_cost=1)
	S += T8T3 >= 40
	T8T3 += ADD[3]


	# new tasks
	T6T0_in = S.Task('T6T0_in', length=1, delay_cost=1)
	T6T0_in += alt(MUL_in)
	T6T0 = S.Task('T6T0', length=7, delay_cost=1)
	T6T0 += alt(MUL)
	S+=T6T0>=T6T0_in

	T6T0_mem0 = S.Task('T6T0_mem0', length=1, delay_cost=1)
	T6T0_mem0 += ADD_mem[0]
	S += 39<T6T0_mem0
	S += T6T0_mem0<=T6T0

	T6T0_mem1 = S.Task('T6T0_mem1', length=1, delay_cost=1)
	T6T0_mem1 += ADD_mem[0]
	S += 17<T6T0_mem1
	S += T6T0_mem1<=T6T0

	T6T1_in = S.Task('T6T1_in', length=1, delay_cost=1)
	T6T1_in += alt(MUL_in)
	T6T1 = S.Task('T6T1', length=7, delay_cost=1)
	T6T1 += alt(MUL)
	S+=T6T1>=T6T1_in

	T6T1_mem0 = S.Task('T6T1_mem0', length=1, delay_cost=1)
	T6T1_mem0 += ADD_mem[0]
	S += 37<T6T1_mem0
	S += T6T1_mem0<=T6T1

	T6T1_mem1 = S.Task('T6T1_mem1', length=1, delay_cost=1)
	T6T1_mem1 += ADD_mem[1]
	S += 23<T6T1_mem1
	S += T6T1_mem1<=T6T1

	T6T2 = S.Task('T6T2', length=1, delay_cost=1)
	T6T2 += alt(ADD)

	T6T2_mem0 = S.Task('T6T2_mem0', length=1, delay_cost=1)
	T6T2_mem0 += ADD_mem[0]
	S += 39<T6T2_mem0
	S += T6T2_mem0<=T6T2

	T6T2_mem1 = S.Task('T6T2_mem1', length=1, delay_cost=1)
	T6T2_mem1 += ADD_mem[0]
	S += 37<T6T2_mem1
	S += T6T2_mem1<=T6T2

	T7T4_in = S.Task('T7T4_in', length=1, delay_cost=1)
	T7T4_in += alt(MUL_in)
	T7T4 = S.Task('T7T4', length=7, delay_cost=1)
	T7T4 += alt(MUL)
	S+=T7T4>=T7T4_in

	T7T4_mem0 = S.Task('T7T4_mem0', length=1, delay_cost=1)
	T7T4_mem0 += ADD_mem[0]
	S += 27<T7T4_mem0
	S += T7T4_mem0<=T7T4

	T7T4_mem1 = S.Task('T7T4_mem1', length=1, delay_cost=1)
	T7T4_mem1 += ADD_mem[2]
	S += 11<T7T4_mem1
	S += T7T4_mem1<=T7T4

	T7T5 = S.Task('T7T5', length=1, delay_cost=1)
	T7T5 += alt(ADD)

	T7T5_mem0 = S.Task('T7T5_mem0', length=1, delay_cost=1)
	T7T5_mem0 += MUL_mem[0]
	S += 33<T7T5_mem0
	S += T7T5_mem0<=T7T5

	T7T5_mem1 = S.Task('T7T5_mem1', length=1, delay_cost=1)
	T7T5_mem1 += MUL_mem[0]
	S += 32<T7T5_mem1
	S += T7T5_mem1<=T7T5

	T70 = S.Task('T70', length=1, delay_cost=1)
	T70 += alt(ADD)

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	T70_mem0 += MUL_mem[0]
	S += 33<T70_mem0
	S += T70_mem0<=T70

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	T70_mem1 += MUL_mem[0]
	S += 32<T70_mem1
	S += T70_mem1<=T70

	T8T4_in = S.Task('T8T4_in', length=1, delay_cost=1)
	T8T4_in += alt(MUL_in)
	T8T4 = S.Task('T8T4', length=7, delay_cost=1)
	T8T4 += alt(MUL)
	S+=T8T4>=T8T4_in

	T8T4_mem0 = S.Task('T8T4_mem0', length=1, delay_cost=1)
	T8T4_mem0 += ADD_mem[1]
	S += 15<T8T4_mem0
	S += T8T4_mem0<=T8T4

	T8T4_mem1 = S.Task('T8T4_mem1', length=1, delay_cost=1)
	T8T4_mem1 += ADD_mem[3]
	S += 40<T8T4_mem1
	S += T8T4_mem1<=T8T4

	T8T5 = S.Task('T8T5', length=1, delay_cost=1)
	T8T5 += alt(ADD)

	T8T5_mem0 = S.Task('T8T5_mem0', length=1, delay_cost=1)
	T8T5_mem0 += MUL_mem[0]
	S += 20<T8T5_mem0
	S += T8T5_mem0<=T8T5

	T8T5_mem1 = S.Task('T8T5_mem1', length=1, delay_cost=1)
	T8T5_mem1 += MUL_mem[0]
	S += 44<T8T5_mem1
	S += T8T5_mem1<=T8T5

	T80 = S.Task('T80', length=1, delay_cost=1)
	T80 += alt(ADD)

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	T80_mem0 += MUL_mem[0]
	S += 20<T80_mem0
	S += T80_mem0<=T80

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	T80_mem1 += MUL_mem[0]
	S += 44<T80_mem1
	S += T80_mem1<=T80

	T90 = S.Task('T90', length=1, delay_cost=1)
	T90 += alt(ADD)

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	T90_mem0 += ADD_mem[0]
	S += 39<T90_mem0
	S += T90_mem0<=T90

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	T90_mem1 += ADD_mem[0]
	S += 26<T90_mem1
	S += T90_mem1<=T90

	T91 = S.Task('T91', length=1, delay_cost=1)
	T91 += alt(ADD)

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	T91_mem0 += ADD_mem[0]
	S += 37<T91_mem0
	S += T91_mem0<=T91

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	T91_mem1 += ADD_mem[1]
	S += 25<T91_mem1
	S += T91_mem1<=T91

	T9_T3 = S.Task('T9_T3', length=1, delay_cost=1)
	T9_T3 += alt(ADD)

	T9_T3_mem0 = S.Task('T9_T3_mem0', length=1, delay_cost=1)
	T9_T3_mem0 += ADD_mem[3]
	S += 18<T9_T3_mem0
	S += T9_T3_mem0<=T9_T3

	T9_T3_mem1 = S.Task('T9_T3_mem1', length=1, delay_cost=1)
	T9_T3_mem1 += ADD_mem[0]
	S += 24<T9_T3_mem1
	S += T9_T3_mem1<=T9_T3

	T1_1T0_in = S.Task('T1_1T0_in', length=1, delay_cost=1)
	T1_1T0_in += alt(MUL_in)
	T1_1T0 = S.Task('T1_1T0', length=7, delay_cost=1)
	T1_1T0 += alt(MUL)
	S+=T1_1T0>=T1_1T0_in

	T1_1T0_mem0 = S.Task('T1_1T0_mem0', length=1, delay_cost=1)
	T1_1T0_mem0 += ADD_mem[2]
	S += 29<T1_1T0_mem0
	S += T1_1T0_mem0<=T1_1T0

	T1_1T0_mem1 = S.Task('T1_1T0_mem1', length=1, delay_cost=1)
	T1_1T0_mem1 += ADD_mem[3]
	S += 11<T1_1T0_mem1
	S += T1_1T0_mem1<=T1_1T0

	T1_1T1_in = S.Task('T1_1T1_in', length=1, delay_cost=1)
	T1_1T1_in += alt(MUL_in)
	T1_1T1 = S.Task('T1_1T1', length=7, delay_cost=1)
	T1_1T1 += alt(MUL)
	S+=T1_1T1>=T1_1T1_in

	T1_1T1_mem0 = S.Task('T1_1T1_mem0', length=1, delay_cost=1)
	T1_1T1_mem0 += ADD_mem[2]
	S += 28<T1_1T1_mem0
	S += T1_1T1_mem0<=T1_1T1

	T1_1T1_mem1 = S.Task('T1_1T1_mem1', length=1, delay_cost=1)
	T1_1T1_mem1 += ADD_mem[2]
	S += 37<T1_1T1_mem1
	S += T1_1T1_mem1<=T1_1T1

	T1_1T2 = S.Task('T1_1T2', length=1, delay_cost=1)
	T1_1T2 += alt(ADD)

	T1_1T2_mem0 = S.Task('T1_1T2_mem0', length=1, delay_cost=1)
	T1_1T2_mem0 += ADD_mem[2]
	S += 29<T1_1T2_mem0
	S += T1_1T2_mem0<=T1_1T2

	T1_1T2_mem1 = S.Task('T1_1T2_mem1', length=1, delay_cost=1)
	T1_1T2_mem1 += ADD_mem[2]
	S += 28<T1_1T2_mem1
	S += T1_1T2_mem1<=T1_1T2

	T1_1T3 = S.Task('T1_1T3', length=1, delay_cost=1)
	T1_1T3 += alt(ADD)

	T1_1T3_mem0 = S.Task('T1_1T3_mem0', length=1, delay_cost=1)
	T1_1T3_mem0 += ADD_mem[3]
	S += 11<T1_1T3_mem0
	S += T1_1T3_mem0<=T1_1T3

	T1_1T3_mem1 = S.Task('T1_1T3_mem1', length=1, delay_cost=1)
	T1_1T3_mem1 += ADD_mem[2]
	S += 37<T1_1T3_mem1
	S += T1_1T3_mem1<=T1_1T3

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	T2_0 += alt(ADD)

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	T2_0_mem0 += ADD_mem[0]
	S += 39<T2_0_mem0
	S += T2_0_mem0<=T2_0

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	T2_0_mem1 += ADD_mem[0]
	S += 13<T2_0_mem1
	S += T2_0_mem1<=T2_0

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	T2_1 += alt(ADD)

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	T2_1_mem0 += ADD_mem[0]
	S += 37<T2_1_mem0
	S += T2_1_mem0<=T2_1

	T2_1_mem1 = S.Task('T2_1_mem1', length=1, delay_cost=1)
	T2_1_mem1 += ADD_mem[0]
	S += 9<T2_1_mem1
	S += T2_1_mem1<=T2_1

	T2_1T3 = S.Task('T2_1T3', length=1, delay_cost=1)
	T2_1T3 += alt(ADD)

	T2_1T3_mem0 = S.Task('T2_1T3_mem0', length=1, delay_cost=1)
	T2_1T3_mem0 += ADD_mem[2]
	S += 19<T2_1T3_mem0
	S += T2_1T3_mem0<=T2_1T3

	T2_1T3_mem1 = S.Task('T2_1T3_mem1', length=1, delay_cost=1)
	T2_1T3_mem1 += ADD_mem[1]
	S += 37<T2_1T3_mem1
	S += T2_1T3_mem1<=T2_1T3

	T6_1 = S.Task('T6_1', length=1, delay_cost=1)
	T6_1 += alt(ADD)

	T6_1_mem0 = S.Task('T6_1_mem0', length=1, delay_cost=1)
	T6_1_mem0 += MUL_mem[0]
	S += 42<T6_1_mem0
	S += T6_1_mem0<=T6_1

	T6_1_mem1 = S.Task('T6_1_mem1', length=1, delay_cost=1)
	T6_1_mem1 += ADD_mem[2]
	S += 14<T6_1_mem1
	S += T6_1_mem1<=T6_1

	T7_1 = S.Task('T7_1', length=1, delay_cost=1)
	T7_1 += alt(ADD)

	T7_1_mem0 = S.Task('T7_1_mem0', length=1, delay_cost=1)
	T7_1_mem0 += MUL_mem[0]
	S += 39<T7_1_mem0
	S += T7_1_mem0<=T7_1

	T7_1_mem1 = S.Task('T7_1_mem1', length=1, delay_cost=1)
	T7_1_mem1 += ADD_mem[3]
	S += 15<T7_1_mem1
	S += T7_1_mem1<=T7_1

	T8_11 = S.Task('T8_11', length=1, delay_cost=1)
	T8_11 += alt(ADD)

	T8_11_mem0 = S.Task('T8_11_mem0', length=1, delay_cost=1)
	T8_11_mem0 += MUL_mem[0]
	S += 35<T8_11_mem0
	S += T8_11_mem0<=T8_11

	T8_11_mem1 = S.Task('T8_11_mem1', length=1, delay_cost=1)
	T8_11_mem1 += ADD_mem[3]
	S += 12<T8_11_mem1
	S += T8_11_mem1<=T8_11

	T9_4T4_in = S.Task('T9_4T4_in', length=1, delay_cost=1)
	T9_4T4_in += alt(MUL_in)
	T9_4T4 = S.Task('T9_4T4', length=7, delay_cost=1)
	T9_4T4 += alt(MUL)
	S+=T9_4T4>=T9_4T4_in

	T9_4T4_mem0 = S.Task('T9_4T4_mem0', length=1, delay_cost=1)
	T9_4T4_mem0 += ADD_mem[3]
	S += 30<T9_4T4_mem0
	S += T9_4T4_mem0<=T9_4T4

	T9_4T4_mem1 = S.Task('T9_4T4_mem1', length=1, delay_cost=1)
	T9_4T4_mem1 += ADD_mem[2]
	S += 17<T9_4T4_mem1
	S += T9_4T4_mem1<=T9_4T4

	T9_4T5 = S.Task('T9_4T5', length=1, delay_cost=1)
	T9_4T5 += alt(ADD)

	T9_4T5_mem0 = S.Task('T9_4T5_mem0', length=1, delay_cost=1)
	T9_4T5_mem0 += MUL_mem[0]
	S += 34<T9_4T5_mem0
	S += T9_4T5_mem0<=T9_4T5

	T9_4T5_mem1 = S.Task('T9_4T5_mem1', length=1, delay_cost=1)
	T9_4T5_mem1 += MUL_mem[0]
	S += 27<T9_4T5_mem1
	S += T9_4T5_mem1<=T9_4T5

	T9_40 = S.Task('T9_40', length=1, delay_cost=1)
	T9_40 += alt(ADD)

	T9_40_mem0 = S.Task('T9_40_mem0', length=1, delay_cost=1)
	T9_40_mem0 += MUL_mem[0]
	S += 34<T9_40_mem0
	S += T9_40_mem0<=T9_40

	T9_40_mem1 = S.Task('T9_40_mem1', length=1, delay_cost=1)
	T9_40_mem1 += MUL_mem[0]
	S += 27<T9_40_mem1
	S += T9_40_mem1<=T9_40

	T3_1T4_in = S.Task('T3_1T4_in', length=1, delay_cost=1)
	T3_1T4_in += alt(MUL_in)
	T3_1T4 = S.Task('T3_1T4', length=7, delay_cost=1)
	T3_1T4 += alt(MUL)
	S+=T3_1T4>=T3_1T4_in

	T3_1T4_mem0 = S.Task('T3_1T4_mem0', length=1, delay_cost=1)
	T3_1T4_mem0 += ADD_mem[2]
	S += 24<T3_1T4_mem0
	S += T3_1T4_mem0<=T3_1T4

	T3_1T4_mem1 = S.Task('T3_1T4_mem1', length=1, delay_cost=1)
	T3_1T4_mem1 += ADD_mem[3]
	S += 13<T3_1T4_mem1
	S += T3_1T4_mem1<=T3_1T4

	T3_1T5 = S.Task('T3_1T5', length=1, delay_cost=1)
	T3_1T5 += alt(ADD)

	T3_1T5_mem0 = S.Task('T3_1T5_mem0', length=1, delay_cost=1)
	T3_1T5_mem0 += MUL_mem[0]
	S += 26<T3_1T5_mem0
	S += T3_1T5_mem0<=T3_1T5

	T3_1T5_mem1 = S.Task('T3_1T5_mem1', length=1, delay_cost=1)
	T3_1T5_mem1 += MUL_mem[0]
	S += 29<T3_1T5_mem1
	S += T3_1T5_mem1<=T3_1T5

	T3_10 = S.Task('T3_10', length=1, delay_cost=1)
	T3_10 += alt(ADD)

	T3_10_mem0 = S.Task('T3_10_mem0', length=1, delay_cost=1)
	T3_10_mem0 += MUL_mem[0]
	S += 26<T3_10_mem0
	S += T3_10_mem0<=T3_10

	T3_10_mem1 = S.Task('T3_10_mem1', length=1, delay_cost=1)
	T3_10_mem1 += MUL_mem[0]
	S += 29<T3_10_mem1
	S += T3_10_mem1<=T3_10

	T4_3T4_in = S.Task('T4_3T4_in', length=1, delay_cost=1)
	T4_3T4_in += alt(MUL_in)
	T4_3T4 = S.Task('T4_3T4', length=7, delay_cost=1)
	T4_3T4 += alt(MUL)
	S+=T4_3T4>=T4_3T4_in

	T4_3T4_mem0 = S.Task('T4_3T4_mem0', length=1, delay_cost=1)
	T4_3T4_mem0 += ADD_mem[2]
	S += 32<T4_3T4_mem0
	S += T4_3T4_mem0<=T4_3T4

	T4_3T4_mem1 = S.Task('T4_3T4_mem1', length=1, delay_cost=1)
	T4_3T4_mem1 += ADD_mem[0]
	S += 25<T4_3T4_mem1
	S += T4_3T4_mem1<=T4_3T4

	T4_3T5 = S.Task('T4_3T5', length=1, delay_cost=1)
	T4_3T5 += alt(ADD)

	T4_3T5_mem0 = S.Task('T4_3T5_mem0', length=1, delay_cost=1)
	T4_3T5_mem0 += MUL_mem[0]
	S += 36<T4_3T5_mem0
	S += T4_3T5_mem0<=T4_3T5

	T4_3T5_mem1 = S.Task('T4_3T5_mem1', length=1, delay_cost=1)
	T4_3T5_mem1 += MUL_mem[0]
	S += 37<T4_3T5_mem1
	S += T4_3T5_mem1<=T4_3T5

	T4_30 = S.Task('T4_30', length=1, delay_cost=1)
	T4_30 += alt(ADD)

	T4_30_mem0 = S.Task('T4_30_mem0', length=1, delay_cost=1)
	T4_30_mem0 += MUL_mem[0]
	S += 36<T4_30_mem0
	S += T4_30_mem0<=T4_30

	T4_30_mem1 = S.Task('T4_30_mem1', length=1, delay_cost=1)
	T4_30_mem1 += MUL_mem[0]
	S += 37<T4_30_mem1
	S += T4_30_mem1<=T4_30

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "square_mul1_add4/square_mul1_add4_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_square_mul1_add4_2(0, 0)