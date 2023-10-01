from pyschedule import Scenario, solvers, plotters, alt

def solve_pdbl_mul1_add4_1(ConstStep, ExpStep):
	horizon = 120
	S=Scenario("pdbl_mul1_add4_1",horizon = horizon)

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
	T3T2_in = S.Task('T3T2_in', length=1, delay_cost=1)
	S += T3T2_in >= 0
	T3T2_in += MUL_in[0]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 0
	T3T2_mem0 += INPUT_mem_r

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 0
	T3T2_mem1 += INPUT_mem_r

	T0T2_in = S.Task('T0T2_in', length=1, delay_cost=1)
	S += T0T2_in >= 1
	T0T2_in += MUL_in[0]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 1
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 1
	T0T2_mem1 += INPUT_mem_r

	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	S += T3T2 >= 1
	T3T2 += MUL[0]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 2
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 2
	T0T1_mem1 += INPUT_mem_r

	T0T2 = S.Task('T0T2', length=7, delay_cost=1)
	S += T0T2 >= 2
	T0T2 += MUL[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 3
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 3
	T0T0_mem1 += INPUT_mem_r

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	S += T0T1 >= 3
	T0T1 += ADD[2]

	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	S += T00_in >= 4
	T00_in += MUL_in[0]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 4
	T00_mem0 += ADD_mem[3]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 4
	T00_mem1 += ADD_mem[2]

	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	S += T0T0 >= 4
	T0T0 += ADD[3]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 4
	T4T2_mem0 += INPUT_mem_r

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 4
	T4T2_mem1 += INPUT_mem_r

	T00 = S.Task('T00', length=7, delay_cost=1)
	S += T00 >= 5
	T00 += MUL[0]

	T4T1_in = S.Task('T4T1_in', length=1, delay_cost=1)
	S += T4T1_in >= 5
	T4T1_in += MUL_in[0]

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	S += T4T1_mem0 >= 5
	T4T1_mem0 += INPUT_mem_r

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	S += T4T1_mem1 >= 5
	T4T1_mem1 += INPUT_mem_r

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	S += T4T2 >= 5
	T4T2 += ADD[0]

	T4T0_in = S.Task('T4T0_in', length=1, delay_cost=1)
	S += T4T0_in >= 6
	T4T0_in += MUL_in[0]

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	S += T4T0_mem0 >= 6
	T4T0_mem0 += INPUT_mem_r

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	S += T4T0_mem1 >= 6
	T4T0_mem1 += INPUT_mem_r

	T4T1 = S.Task('T4T1', length=7, delay_cost=1)
	S += T4T1 >= 6
	T4T1 += MUL[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 7
	T31_mem0 += MUL_mem[0]

	T4T0 = S.Task('T4T0', length=7, delay_cost=1)
	S += T4T0 >= 7
	T4T0 += MUL[0]

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	S += T4T3_mem0 >= 7
	T4T3_mem0 += INPUT_mem_r

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	S += T4T3_mem1 >= 7
	T4T3_mem1 += INPUT_mem_r

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 8
	T01_mem0 += MUL_mem[0]

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 8
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 8
	T1T0_mem1 += INPUT_mem_r

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 8
	T31 += ADD[2]

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	S += T4T3 >= 8
	T4T3 += ADD[0]

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	S += T4T4_in >= 8
	T4T4_in += MUL_in[0]

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	S += T4T4_mem0 >= 8
	T4T4_mem0 += ADD_mem[0]

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	S += T4T4_mem1 >= 8
	T4T4_mem1 += ADD_mem[0]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 8
	T61_mem0 += ADD_mem[2]

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 9
	T01 += ADD[0]

	T1T0 = S.Task('T1T0', length=1, delay_cost=1)
	S += T1T0 >= 9
	T1T0 += ADD[3]

	T1T2_in = S.Task('T1T2_in', length=1, delay_cost=1)
	S += T1T2_in >= 9
	T1T2_in += MUL_in[0]

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	S += T1T2_mem0 >= 9
	T1T2_mem0 += INPUT_mem_r

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	S += T1T2_mem1 >= 9
	T1T2_mem1 += INPUT_mem_r

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	S += T3_1_mem0 >= 9
	T3_1_mem0 += ADD_mem[1]

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	S += T3_1_mem1 >= 9
	T3_1_mem1 += ADD_mem[2]

	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	S += T4T4 >= 9
	T4T4 += MUL[0]

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 9
	T61 += ADD[1]

	T1T2 = S.Task('T1T2', length=7, delay_cost=1)
	S += T1T2 >= 10
	T1T2 += MUL[0]

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	S += T2T0_in >= 10
	T2T0_in += MUL_in[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 10
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 10
	T2T0_mem1 += INPUT_mem_r

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 10
	T3_1 += ADD[0]

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	S += T0_T0_mem0 >= 11
	T0_T0_mem0 += MUL_mem[0]

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	S += T0_T0_mem1 >= 11
	T0_T0_mem1 += ADD_mem[0]

	T0_T2_in = S.Task('T0_T2_in', length=1, delay_cost=1)
	S += T0_T2_in >= 11
	T0_T2_in += MUL_in[0]

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	S += T0_T2_mem0 >= 11
	T0_T2_mem0 += MUL_mem[0]

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	S += T0_T2_mem1 >= 11
	T0_T2_mem1 += ADD_mem[0]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 11
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 11
	T1T1_mem1 += INPUT_mem_r

	T2T0 = S.Task('T2T0', length=7, delay_cost=1)
	S += T2T0 >= 11
	T2T0 += MUL[0]

	NEW_TZT2_mem0 = S.Task('NEW_TZT2_mem0', length=1, delay_cost=1)
	S += NEW_TZT2_mem0 >= 12
	NEW_TZT2_mem0 += MUL_mem[0]

	NEW_TZT2_mem1 = S.Task('NEW_TZT2_mem1', length=1, delay_cost=1)
	S += NEW_TZT2_mem1 >= 12
	NEW_TZT2_mem1 += ADD_mem[0]

	T0_T0 = S.Task('T0_T0', length=1, delay_cost=1)
	S += T0_T0 >= 12
	T0_T0 += ADD[0]

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	S += T0_T1_mem0 >= 12
	T0_T1_mem0 += MUL_mem[0]

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	S += T0_T1_mem1 >= 12
	T0_T1_mem1 += ADD_mem[0]

	T0_T2 = S.Task('T0_T2', length=7, delay_cost=1)
	S += T0_T2 >= 12
	T0_T2 += MUL[0]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 12
	T10_in += MUL_in[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 12
	T10_mem0 += ADD_mem[3]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 12
	T10_mem1 += ADD_mem[1]

	T1T1 = S.Task('T1T1', length=1, delay_cost=1)
	S += T1T1 >= 12
	T1T1 += ADD[1]

	T2T3_mem0 = S.Task('T2T3_mem0', length=1, delay_cost=1)
	S += T2T3_mem0 >= 12
	T2T3_mem0 += INPUT_mem_r

	T2T3_mem1 = S.Task('T2T3_mem1', length=1, delay_cost=1)
	S += T2T3_mem1 >= 12
	T2T3_mem1 += INPUT_mem_r

	NEW_TZT2 = S.Task('NEW_TZT2', length=1, delay_cost=1)
	S += NEW_TZT2 >= 13
	NEW_TZT2 += ADD[1]

	T0_T1 = S.Task('T0_T1', length=1, delay_cost=1)
	S += T0_T1 >= 13
	T0_T1 += ADD[0]

	T10 = S.Task('T10', length=7, delay_cost=1)
	S += T10 >= 13
	T10 += MUL[0]

	T2T1_in = S.Task('T2T1_in', length=1, delay_cost=1)
	S += T2T1_in >= 13
	T2T1_in += MUL_in[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 13
	T2T1_mem0 += INPUT_mem_r

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 13
	T2T1_mem1 += INPUT_mem_r

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	S += T2T3 >= 13
	T2T3 += ADD[2]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 13
	T40_mem0 += MUL_mem[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 13
	T40_mem1 += MUL_mem[0]

	T0_0_in = S.Task('T0_0_in', length=1, delay_cost=1)
	S += T0_0_in >= 14
	T0_0_in += MUL_in[0]

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	S += T0_0_mem0 >= 14
	T0_0_mem0 += ADD_mem[0]

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	S += T0_0_mem1 >= 14
	T0_0_mem1 += ADD_mem[0]

	T2T1 = S.Task('T2T1', length=7, delay_cost=1)
	S += T2T1 >= 14
	T2T1 += MUL[0]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 14
	T2T2_mem0 += INPUT_mem_r

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 14
	T2T2_mem1 += INPUT_mem_r

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 14
	T40 += ADD[1]

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	S += T4T5_mem0 >= 14
	T4T5_mem0 += MUL_mem[0]

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	S += T4T5_mem1 >= 14
	T4T5_mem1 += MUL_mem[0]

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	S += T4_0_mem0 >= 14
	T4_0_mem0 += ADD_mem[1]

	T0_0 = S.Task('T0_0', length=7, delay_cost=1)
	S += T0_0 >= 15
	T0_0 += MUL[0]

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	S += T2T2 >= 15
	T2T2 += ADD[1]

	T2T4_in = S.Task('T2T4_in', length=1, delay_cost=1)
	S += T2T4_in >= 15
	T2T4_in += MUL_in[0]

	T2T4_mem0 = S.Task('T2T4_mem0', length=1, delay_cost=1)
	S += T2T4_mem0 >= 15
	T2T4_mem0 += ADD_mem[1]

	T2T4_mem1 = S.Task('T2T4_mem1', length=1, delay_cost=1)
	S += T2T4_mem1 >= 15
	T2T4_mem1 += ADD_mem[2]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 15
	T3T1_mem0 += INPUT_mem_r

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 15
	T3T1_mem1 += INPUT_mem_r

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 15
	T41_mem0 += MUL_mem[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 15
	T41_mem1 += ADD_mem[0]

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	S += T4T5 >= 15
	T4T5 += ADD[0]

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	S += T4_0 >= 15
	T4_0 += ADD[3]

	NEW_TZT0_in = S.Task('NEW_TZT0_in', length=1, delay_cost=1)
	S += NEW_TZT0_in >= 16
	NEW_TZT0_in += MUL_in[0]

	NEW_TZT0_mem0 = S.Task('NEW_TZT0_mem0', length=1, delay_cost=1)
	S += NEW_TZT0_mem0 >= 16
	NEW_TZT0_mem0 += MUL_mem[0]

	NEW_TZT0_mem1 = S.Task('NEW_TZT0_mem1', length=1, delay_cost=1)
	S += NEW_TZT0_mem1 >= 16
	NEW_TZT0_mem1 += ADD_mem[3]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 16
	T11_mem0 += MUL_mem[0]

	T2T4 = S.Task('T2T4', length=7, delay_cost=1)
	S += T2T4 >= 16
	T2T4 += MUL[0]

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 16
	T3T0_mem0 += INPUT_mem_r

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 16
	T3T0_mem1 += INPUT_mem_r

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	S += T3T1 >= 16
	T3T1 += ADD[3]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 16
	T41 += ADD[0]

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	S += T4_1_mem0 >= 16
	T4_1_mem0 += ADD_mem[0]

	NEW_TZT0 = S.Task('NEW_TZT0', length=7, delay_cost=1)
	S += NEW_TZT0 >= 17
	NEW_TZT0 += MUL[0]

	NEW_TZT3_mem0 = S.Task('NEW_TZT3_mem0', length=1, delay_cost=1)
	S += NEW_TZT3_mem0 >= 17
	NEW_TZT3_mem0 += ADD_mem[3]

	NEW_TZT3_mem1 = S.Task('NEW_TZT3_mem1', length=1, delay_cost=1)
	S += NEW_TZT3_mem1 >= 17
	NEW_TZT3_mem1 += ADD_mem[0]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 17
	T11 += ADD[3]

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	S += T1_T2_mem0 >= 17
	T1_T2_mem0 += INPUT_mem_r

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	S += T1_T2_mem1 >= 17
	T1_T2_mem1 += INPUT_mem_r

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 17
	T30_in += MUL_in[0]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 17
	T30_mem0 += ADD_mem[1]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 17
	T30_mem1 += ADD_mem[3]

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	S += T3T0 >= 17
	T3T0 += ADD[1]

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	S += T4_1 >= 17
	T4_1 += ADD[0]

	NEW_TZT3 = S.Task('NEW_TZT3', length=1, delay_cost=1)
	S += NEW_TZT3 >= 18
	NEW_TZT3 += ADD[0]

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	S += T0_1_mem0 >= 18
	T0_1_mem0 += MUL_mem[0]

	T1_T1_in = S.Task('T1_T1_in', length=1, delay_cost=1)
	S += T1_T1_in >= 18
	T1_T1_in += MUL_in[0]

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	S += T1_T1_mem0 >= 18
	T1_T1_mem0 += INPUT_mem_r

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	S += T1_T1_mem1 >= 18
	T1_T1_mem1 += ADD_mem[3]

	T1_T2 = S.Task('T1_T2', length=1, delay_cost=1)
	S += T1_T2 >= 18
	T1_T2 += ADD[1]

	T30 = S.Task('T30', length=7, delay_cost=1)
	S += T30 >= 18
	T30 += MUL[0]

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	S += T0_1 >= 19
	T0_1 += ADD[0]

	T1_T0_in = S.Task('T1_T0_in', length=1, delay_cost=1)
	S += T1_T0_in >= 19
	T1_T0_in += MUL_in[0]

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	S += T1_T0_mem0 >= 19
	T1_T0_mem0 += INPUT_mem_r

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	S += T1_T0_mem1 >= 19
	T1_T0_mem1 += MUL_mem[0]

	T1_T1 = S.Task('T1_T1', length=7, delay_cost=1)
	S += T1_T1 >= 19
	T1_T1 += MUL[0]

	T1_T3_mem0 = S.Task('T1_T3_mem0', length=1, delay_cost=1)
	S += T1_T3_mem0 >= 19
	T1_T3_mem0 += MUL_mem[0]

	T1_T3_mem1 = S.Task('T1_T3_mem1', length=1, delay_cost=1)
	S += T1_T3_mem1 >= 19
	T1_T3_mem1 += ADD_mem[3]

	T1_T0 = S.Task('T1_T0', length=7, delay_cost=1)
	S += T1_T0 >= 20
	T1_T0 += MUL[0]

	T1_T3 = S.Task('T1_T3', length=1, delay_cost=1)
	S += T1_T3 >= 20
	T1_T3 += ADD[1]

	T1_T4_in = S.Task('T1_T4_in', length=1, delay_cost=1)
	S += T1_T4_in >= 20
	T1_T4_in += MUL_in[0]

	T1_T4_mem0 = S.Task('T1_T4_mem0', length=1, delay_cost=1)
	S += T1_T4_mem0 >= 20
	T1_T4_mem0 += ADD_mem[1]

	T1_T4_mem1 = S.Task('T1_T4_mem1', length=1, delay_cost=1)
	S += T1_T4_mem1 >= 20
	T1_T4_mem1 += ADD_mem[1]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 20
	T20_mem0 += MUL_mem[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 20
	T20_mem1 += MUL_mem[0]

	NEW_TZT1_in = S.Task('NEW_TZT1_in', length=1, delay_cost=1)
	S += NEW_TZT1_in >= 21
	NEW_TZT1_in += MUL_in[0]

	NEW_TZT1_mem0 = S.Task('NEW_TZT1_mem0', length=1, delay_cost=1)
	S += NEW_TZT1_mem0 >= 21
	NEW_TZT1_mem0 += ADD_mem[0]

	NEW_TZT1_mem1 = S.Task('NEW_TZT1_mem1', length=1, delay_cost=1)
	S += NEW_TZT1_mem1 >= 21
	NEW_TZT1_mem1 += ADD_mem[0]

	T1_T4 = S.Task('T1_T4', length=7, delay_cost=1)
	S += T1_T4 >= 21
	T1_T4 += MUL[0]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 21
	T20 += ADD[3]

	T2T5_mem0 = S.Task('T2T5_mem0', length=1, delay_cost=1)
	S += T2T5_mem0 >= 21
	T2T5_mem0 += MUL_mem[0]

	T2T5_mem1 = S.Task('T2T5_mem1', length=1, delay_cost=1)
	S += T2T5_mem1 >= 21
	T2T5_mem1 += MUL_mem[0]

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	S += T2_0_mem0 >= 21
	T2_0_mem0 += ADD_mem[3]

	NEW_TZT1 = S.Task('NEW_TZT1', length=7, delay_cost=1)
	S += NEW_TZT1 >= 22
	NEW_TZT1 += MUL[0]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 22
	T21_mem0 += MUL_mem[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 22
	T21_mem1 += ADD_mem[2]

	T2T5 = S.Task('T2T5', length=1, delay_cost=1)
	S += T2T5 >= 22
	T2T5 += ADD[2]

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	S += T2_0 >= 22
	T2_0 += ADD[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 23
	T21 += ADD[1]

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	S += T2_1_mem0 >= 23
	T2_1_mem0 += ADD_mem[1]

	NEW_TX_T3_mem0 = S.Task('NEW_TX_T3_mem0', length=1, delay_cost=1)
	S += NEW_TX_T3_mem0 >= 24
	NEW_TX_T3_mem0 += ADD_mem[0]

	NEW_TX_T3_mem1 = S.Task('NEW_TX_T3_mem1', length=1, delay_cost=1)
	S += NEW_TX_T3_mem1 >= 24
	NEW_TX_T3_mem1 += ADD_mem[0]

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	S += T2_1 >= 24
	T2_1 += ADD[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 24
	T60_mem0 += MUL_mem[0]

	NEW_TX_T3 = S.Task('NEW_TX_T3', length=1, delay_cost=1)
	S += NEW_TX_T3 >= 25
	NEW_TX_T3 += ADD[0]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 25
	T3_0_mem0 += ADD_mem[1]

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 25
	T3_0_mem1 += MUL_mem[0]

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 25
	T60 += ADD[1]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 26
	T1_0_mem0 += MUL_mem[0]

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 26
	T1_0_mem1 += MUL_mem[0]

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 26
	T3_0 += ADD[0]

	B_0_mem0 = S.Task('B_0_mem0', length=1, delay_cost=1)
	S += B_0_mem0 >= 27
	B_0_mem0 += ADD_mem[0]

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	S += T1_0 >= 27
	T1_0 += ADD[0]

	T1_T5_mem0 = S.Task('T1_T5_mem0', length=1, delay_cost=1)
	S += T1_T5_mem0 >= 27
	T1_T5_mem0 += MUL_mem[0]

	T1_T5_mem1 = S.Task('T1_T5_mem1', length=1, delay_cost=1)
	S += T1_T5_mem1 >= 27
	T1_T5_mem1 += MUL_mem[0]

	B_0 = S.Task('B_0', length=1, delay_cost=1)
	S += B_0 >= 28
	B_0 += ADD[2]

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 28
	T1_1_mem0 += MUL_mem[0]

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	S += T1_1_mem1 >= 28
	T1_1_mem1 += ADD_mem[0]

	T1_T5 = S.Task('T1_T5', length=1, delay_cost=1)
	S += T1_T5 >= 28
	T1_T5 += ADD[0]

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 29
	T1_1 += ADD[1]


	# new tasks
	B_1 = S.Task('B_1', length=1, delay_cost=1)
	B_1 += alt(ADD)

	B_1_mem0 = S.Task('B_1_mem0', length=1, delay_cost=1)
	B_1_mem0 += ADD_mem[1]
	S += T1_1<B_1_mem0
	S += B_1_mem0<=B_1

	T1_10 = S.Task('T1_10', length=1, delay_cost=1)
	T1_10 += alt(ADD)

	T1_10_mem0 = S.Task('T1_10_mem0', length=1, delay_cost=1)
	T1_10_mem0 += ADD_mem[2]
	S += B_0<T1_10_mem0
	S += T1_10_mem0<=T1_10

	T1_10_mem1 = S.Task('T1_10_mem1', length=1, delay_cost=1)
	T1_10_mem1 += ADD_mem[0]
	S += T1_0<T1_10_mem1
	S += T1_10_mem1<=T1_10

	NEW_TZT4_in = S.Task('NEW_TZT4_in', length=1, delay_cost=1)
	NEW_TZT4_in += alt(MUL_in)
	NEW_TZT4 = S.Task('NEW_TZT4', length=7, delay_cost=1)
	NEW_TZT4 += alt(MUL)
	S+=NEW_TZT4>=NEW_TZT4_in

	NEW_TZT4_mem0 = S.Task('NEW_TZT4_mem0', length=1, delay_cost=1)
	NEW_TZT4_mem0 += ADD_mem[1]
	S += NEW_TZT2<NEW_TZT4_mem0
	S += NEW_TZT4_mem0<=NEW_TZT4

	NEW_TZT4_mem1 = S.Task('NEW_TZT4_mem1', length=1, delay_cost=1)
	NEW_TZT4_mem1 += ADD_mem[0]
	S += NEW_TZT3<NEW_TZT4_mem1
	S += NEW_TZT4_mem1<=NEW_TZT4

	NEW_TZT5 = S.Task('NEW_TZT5', length=1, delay_cost=1)
	NEW_TZT5 += alt(ADD)

	NEW_TZT5_mem0 = S.Task('NEW_TZT5_mem0', length=1, delay_cost=1)
	NEW_TZT5_mem0 += MUL_mem[0]
	S += NEW_TZT0<NEW_TZT5_mem0
	S += NEW_TZT5_mem0<=NEW_TZT5

	NEW_TZT5_mem1 = S.Task('NEW_TZT5_mem1', length=1, delay_cost=1)
	NEW_TZT5_mem1 += MUL_mem[0]
	S += NEW_TZT1<NEW_TZT5_mem1
	S += NEW_TZT5_mem1<=NEW_TZT5

	NEW_TZ0 = S.Task('NEW_TZ0', length=1, delay_cost=1)
	NEW_TZ0 += alt(ADD)

	NEW_TZ0_mem0 = S.Task('NEW_TZ0_mem0', length=1, delay_cost=1)
	NEW_TZ0_mem0 += MUL_mem[0]
	S += NEW_TZT0<NEW_TZ0_mem0
	S += NEW_TZ0_mem0<=NEW_TZ0

	NEW_TZ0_mem1 = S.Task('NEW_TZ0_mem1', length=1, delay_cost=1)
	NEW_TZ0_mem1 += MUL_mem[0]
	S += NEW_TZT1<NEW_TZ0_mem1
	S += NEW_TZ0_mem1<=NEW_TZ0

	T1_11 = S.Task('T1_11', length=1, delay_cost=1)
	T1_11 += alt(ADD)

	T1_11_mem0 = S.Task('T1_11_mem0', length=1, delay_cost=1)
	T1_11_mem0 += alt(ADD_mem)
	S += (B_1*ADD[0])-1<T1_11_mem0*ADD_mem[0]
	S += (B_1*ADD[1])-1<T1_11_mem0*ADD_mem[1]
	S += (B_1*ADD[2])-1<T1_11_mem0*ADD_mem[2]
	S += (B_1*ADD[3])-1<T1_11_mem0*ADD_mem[3]
	S += T1_11_mem0<=T1_11

	T1_11_mem1 = S.Task('T1_11_mem1', length=1, delay_cost=1)
	T1_11_mem1 += ADD_mem[1]
	S += T1_1<T1_11_mem1
	S += T1_11_mem1<=T1_11

	NEW_TZ1 = S.Task('NEW_TZ1', length=1, delay_cost=1)
	NEW_TZ1 += alt(ADD)

	NEW_TZ1_mem0 = S.Task('NEW_TZ1_mem0', length=1, delay_cost=1)
	NEW_TZ1_mem0 += alt(MUL_mem)
	S += (NEW_TZT4*MUL[0])-1<NEW_TZ1_mem0*MUL_mem[0]
	S += NEW_TZ1_mem0<=NEW_TZ1

	NEW_TZ1_mem1 = S.Task('NEW_TZ1_mem1', length=1, delay_cost=1)
	NEW_TZ1_mem1 += alt(ADD_mem)
	S += (NEW_TZT5*ADD[0])-1<NEW_TZ1_mem1*ADD_mem[0]
	S += (NEW_TZT5*ADD[1])-1<NEW_TZ1_mem1*ADD_mem[1]
	S += (NEW_TZT5*ADD[2])-1<NEW_TZ1_mem1*ADD_mem[2]
	S += (NEW_TZT5*ADD[3])-1<NEW_TZ1_mem1*ADD_mem[3]
	S += NEW_TZ1_mem1<=NEW_TZ1

	NEW_TZ_0 = S.Task('NEW_TZ_0', length=1, delay_cost=1)
	NEW_TZ_0 += alt(ADD)

	NEW_TZ_0_mem0 = S.Task('NEW_TZ_0_mem0', length=1, delay_cost=1)
	NEW_TZ_0_mem0 += alt(ADD_mem)
	S += (NEW_TZ0*ADD[0])-1<NEW_TZ_0_mem0*ADD_mem[0]
	S += (NEW_TZ0*ADD[1])-1<NEW_TZ_0_mem0*ADD_mem[1]
	S += (NEW_TZ0*ADD[2])-1<NEW_TZ_0_mem0*ADD_mem[2]
	S += (NEW_TZ0*ADD[3])-1<NEW_TZ_0_mem0*ADD_mem[3]
	S += NEW_TZ_0_mem0<=NEW_TZ_0

	C000 = S.Task('C000', length=1, delay_cost=1)
	C000 += alt(ADD)

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	C000_mem0 += MUL_mem[0]
	S += T00<C000_mem0
	S += C000_mem0<=C000

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	C000_mem1 += alt(ADD_mem)
	S += (T1_10*ADD[0])-1<C000_mem1*ADD_mem[0]
	S += (T1_10*ADD[1])-1<C000_mem1*ADD_mem[1]
	S += (T1_10*ADD[2])-1<C000_mem1*ADD_mem[2]
	S += (T1_10*ADD[3])-1<C000_mem1*ADD_mem[3]
	S += C000_mem1<=C000

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(ADD)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += alt(ADD_mem)
	S += (T1_10*ADD[0])-1<T50_mem0*ADD_mem[0]
	S += (T1_10*ADD[1])-1<T50_mem0*ADD_mem[1]
	S += (T1_10*ADD[2])-1<T50_mem0*ADD_mem[2]
	S += (T1_10*ADD[3])-1<T50_mem0*ADD_mem[3]
	S += T50_mem0<=T50

	NEW_TZ_1 = S.Task('NEW_TZ_1', length=1, delay_cost=1)
	NEW_TZ_1 += alt(ADD)

	NEW_TZ_1_mem0 = S.Task('NEW_TZ_1_mem0', length=1, delay_cost=1)
	NEW_TZ_1_mem0 += alt(ADD_mem)
	S += (NEW_TZ1*ADD[0])-1<NEW_TZ_1_mem0*ADD_mem[0]
	S += (NEW_TZ1*ADD[1])-1<NEW_TZ_1_mem0*ADD_mem[1]
	S += (NEW_TZ1*ADD[2])-1<NEW_TZ_1_mem0*ADD_mem[2]
	S += (NEW_TZ1*ADD[3])-1<NEW_TZ_1_mem0*ADD_mem[3]
	S += NEW_TZ_1_mem0<=NEW_TZ_1

	C001 = S.Task('C001', length=1, delay_cost=1)
	C001 += alt(ADD)

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	C001_mem0 += ADD_mem[0]
	S += T01<C001_mem0
	S += C001_mem0<=C001

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	C001_mem1 += alt(ADD_mem)
	S += (T1_11*ADD[0])-1<C001_mem1*ADD_mem[0]
	S += (T1_11*ADD[1])-1<C001_mem1*ADD_mem[1]
	S += (T1_11*ADD[2])-1<C001_mem1*ADD_mem[2]
	S += (T1_11*ADD[3])-1<C001_mem1*ADD_mem[3]
	S += C001_mem1<=C001

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(ADD)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += alt(ADD_mem)
	S += (T1_11*ADD[0])-1<T51_mem0*ADD_mem[0]
	S += (T1_11*ADD[1])-1<T51_mem0*ADD_mem[1]
	S += (T1_11*ADD[2])-1<T51_mem0*ADD_mem[2]
	S += (T1_11*ADD[3])-1<T51_mem0*ADD_mem[3]
	S += T51_mem0<=T51

	NEW_TX0 = S.Task('NEW_TX0', length=1, delay_cost=1)
	NEW_TX0 += alt(ADD)

	NEW_TX0_mem0 = S.Task('NEW_TX0_mem0', length=1, delay_cost=1)
	NEW_TX0_mem0 += alt(ADD_mem)
	S += (C000*ADD[0])-1<NEW_TX0_mem0*ADD_mem[0]
	S += (C000*ADD[1])-1<NEW_TX0_mem0*ADD_mem[1]
	S += (C000*ADD[2])-1<NEW_TX0_mem0*ADD_mem[2]
	S += (C000*ADD[3])-1<NEW_TX0_mem0*ADD_mem[3]
	S += NEW_TX0_mem0<=NEW_TX0

	NEW_TX0_mem1 = S.Task('NEW_TX0_mem1', length=1, delay_cost=1)
	NEW_TX0_mem1 += alt(ADD_mem)
	S += (T50*ADD[0])-1<NEW_TX0_mem1*ADD_mem[0]
	S += (T50*ADD[1])-1<NEW_TX0_mem1*ADD_mem[1]
	S += (T50*ADD[2])-1<NEW_TX0_mem1*ADD_mem[2]
	S += (T50*ADD[3])-1<NEW_TX0_mem1*ADD_mem[3]
	S += NEW_TX0_mem1<=NEW_TX0

	NEW_TY0 = S.Task('NEW_TY0', length=1, delay_cost=1)
	NEW_TY0 += alt(ADD)

	NEW_TY0_mem0 = S.Task('NEW_TY0_mem0', length=1, delay_cost=1)
	NEW_TY0_mem0 += MUL_mem[0]
	S += T00<NEW_TY0_mem0
	S += NEW_TY0_mem0<=NEW_TY0

	NEW_TY0_mem1 = S.Task('NEW_TY0_mem1', length=1, delay_cost=1)
	NEW_TY0_mem1 += alt(ADD_mem)
	S += (C000*ADD[0])-1<NEW_TY0_mem1*ADD_mem[0]
	S += (C000*ADD[1])-1<NEW_TY0_mem1*ADD_mem[1]
	S += (C000*ADD[2])-1<NEW_TY0_mem1*ADD_mem[2]
	S += (C000*ADD[3])-1<NEW_TY0_mem1*ADD_mem[3]
	S += NEW_TY0_mem1<=NEW_TY0

	B30 = S.Task('B30', length=1, delay_cost=1)
	B30 += alt(ADD)

	B30_mem0 = S.Task('B30_mem0', length=1, delay_cost=1)
	B30_mem0 += alt(ADD_mem)
	S += (T50*ADD[0])-1<B30_mem0*ADD_mem[0]
	S += (T50*ADD[1])-1<B30_mem0*ADD_mem[1]
	S += (T50*ADD[2])-1<B30_mem0*ADD_mem[2]
	S += (T50*ADD[3])-1<B30_mem0*ADD_mem[3]
	S += B30_mem0<=B30

	B30_mem1 = S.Task('B30_mem1', length=1, delay_cost=1)
	B30_mem1 += alt(ADD_mem)
	S += (T1_10*ADD[0])-1<B30_mem1*ADD_mem[0]
	S += (T1_10*ADD[1])-1<B30_mem1*ADD_mem[1]
	S += (T1_10*ADD[2])-1<B30_mem1*ADD_mem[2]
	S += (T1_10*ADD[3])-1<B30_mem1*ADD_mem[3]
	S += B30_mem1<=B30

	NEW_TX1 = S.Task('NEW_TX1', length=1, delay_cost=1)
	NEW_TX1 += alt(ADD)

	NEW_TX1_mem0 = S.Task('NEW_TX1_mem0', length=1, delay_cost=1)
	NEW_TX1_mem0 += alt(ADD_mem)
	S += (C001*ADD[0])-1<NEW_TX1_mem0*ADD_mem[0]
	S += (C001*ADD[1])-1<NEW_TX1_mem0*ADD_mem[1]
	S += (C001*ADD[2])-1<NEW_TX1_mem0*ADD_mem[2]
	S += (C001*ADD[3])-1<NEW_TX1_mem0*ADD_mem[3]
	S += NEW_TX1_mem0<=NEW_TX1

	NEW_TX1_mem1 = S.Task('NEW_TX1_mem1', length=1, delay_cost=1)
	NEW_TX1_mem1 += alt(ADD_mem)
	S += (T51*ADD[0])-1<NEW_TX1_mem1*ADD_mem[0]
	S += (T51*ADD[1])-1<NEW_TX1_mem1*ADD_mem[1]
	S += (T51*ADD[2])-1<NEW_TX1_mem1*ADD_mem[2]
	S += (T51*ADD[3])-1<NEW_TX1_mem1*ADD_mem[3]
	S += NEW_TX1_mem1<=NEW_TX1

	NEW_TX_T0_in = S.Task('NEW_TX_T0_in', length=1, delay_cost=1)
	NEW_TX_T0_in += alt(MUL_in)
	NEW_TX_T0 = S.Task('NEW_TX_T0', length=7, delay_cost=1)
	NEW_TX_T0 += alt(MUL)
	S+=NEW_TX_T0>=NEW_TX_T0_in

	NEW_TX_T0_mem0 = S.Task('NEW_TX_T0_mem0', length=1, delay_cost=1)
	NEW_TX_T0_mem0 += alt(ADD_mem)
	S += (NEW_TX0*ADD[0])-1<NEW_TX_T0_mem0*ADD_mem[0]
	S += (NEW_TX0*ADD[1])-1<NEW_TX_T0_mem0*ADD_mem[1]
	S += (NEW_TX0*ADD[2])-1<NEW_TX_T0_mem0*ADD_mem[2]
	S += (NEW_TX0*ADD[3])-1<NEW_TX_T0_mem0*ADD_mem[3]
	S += NEW_TX_T0_mem0<=NEW_TX_T0

	NEW_TX_T0_mem1 = S.Task('NEW_TX_T0_mem1', length=1, delay_cost=1)
	NEW_TX_T0_mem1 += ADD_mem[0]
	S += T2_0<NEW_TX_T0_mem1
	S += NEW_TX_T0_mem1<=NEW_TX_T0

	NEW_TY1 = S.Task('NEW_TY1', length=1, delay_cost=1)
	NEW_TY1 += alt(ADD)

	NEW_TY1_mem0 = S.Task('NEW_TY1_mem0', length=1, delay_cost=1)
	NEW_TY1_mem0 += ADD_mem[0]
	S += T01<NEW_TY1_mem0
	S += NEW_TY1_mem0<=NEW_TY1

	NEW_TY1_mem1 = S.Task('NEW_TY1_mem1', length=1, delay_cost=1)
	NEW_TY1_mem1 += alt(ADD_mem)
	S += (C001*ADD[0])-1<NEW_TY1_mem1*ADD_mem[0]
	S += (C001*ADD[1])-1<NEW_TY1_mem1*ADD_mem[1]
	S += (C001*ADD[2])-1<NEW_TY1_mem1*ADD_mem[2]
	S += (C001*ADD[3])-1<NEW_TY1_mem1*ADD_mem[3]
	S += NEW_TY1_mem1<=NEW_TY1

	B31 = S.Task('B31', length=1, delay_cost=1)
	B31 += alt(ADD)

	B31_mem0 = S.Task('B31_mem0', length=1, delay_cost=1)
	B31_mem0 += alt(ADD_mem)
	S += (T51*ADD[0])-1<B31_mem0*ADD_mem[0]
	S += (T51*ADD[1])-1<B31_mem0*ADD_mem[1]
	S += (T51*ADD[2])-1<B31_mem0*ADD_mem[2]
	S += (T51*ADD[3])-1<B31_mem0*ADD_mem[3]
	S += B31_mem0<=B31

	B31_mem1 = S.Task('B31_mem1', length=1, delay_cost=1)
	B31_mem1 += alt(ADD_mem)
	S += (T1_11*ADD[0])-1<B31_mem1*ADD_mem[0]
	S += (T1_11*ADD[1])-1<B31_mem1*ADD_mem[1]
	S += (T1_11*ADD[2])-1<B31_mem1*ADD_mem[2]
	S += (T1_11*ADD[3])-1<B31_mem1*ADD_mem[3]
	S += B31_mem1<=B31

	NEW_TY_T0_in = S.Task('NEW_TY_T0_in', length=1, delay_cost=1)
	NEW_TY_T0_in += alt(MUL_in)
	NEW_TY_T0 = S.Task('NEW_TY_T0', length=7, delay_cost=1)
	NEW_TY_T0 += alt(MUL)
	S+=NEW_TY_T0>=NEW_TY_T0_in

	NEW_TY_T0_mem0 = S.Task('NEW_TY_T0_mem0', length=1, delay_cost=1)
	NEW_TY_T0_mem0 += alt(ADD_mem)
	S += (B30*ADD[0])-1<NEW_TY_T0_mem0*ADD_mem[0]
	S += (B30*ADD[1])-1<NEW_TY_T0_mem0*ADD_mem[1]
	S += (B30*ADD[2])-1<NEW_TY_T0_mem0*ADD_mem[2]
	S += (B30*ADD[3])-1<NEW_TY_T0_mem0*ADD_mem[3]
	S += NEW_TY_T0_mem0<=NEW_TY_T0

	NEW_TY_T0_mem1 = S.Task('NEW_TY_T0_mem1', length=1, delay_cost=1)
	NEW_TY_T0_mem1 += alt(ADD_mem)
	S += (NEW_TY0*ADD[0])-1<NEW_TY_T0_mem1*ADD_mem[0]
	S += (NEW_TY0*ADD[1])-1<NEW_TY_T0_mem1*ADD_mem[1]
	S += (NEW_TY0*ADD[2])-1<NEW_TY_T0_mem1*ADD_mem[2]
	S += (NEW_TY0*ADD[3])-1<NEW_TY_T0_mem1*ADD_mem[3]
	S += NEW_TY_T0_mem1<=NEW_TY_T0

	NEW_TX_T1_in = S.Task('NEW_TX_T1_in', length=1, delay_cost=1)
	NEW_TX_T1_in += alt(MUL_in)
	NEW_TX_T1 = S.Task('NEW_TX_T1', length=7, delay_cost=1)
	NEW_TX_T1 += alt(MUL)
	S+=NEW_TX_T1>=NEW_TX_T1_in

	NEW_TX_T1_mem0 = S.Task('NEW_TX_T1_mem0', length=1, delay_cost=1)
	NEW_TX_T1_mem0 += alt(ADD_mem)
	S += (NEW_TX1*ADD[0])-1<NEW_TX_T1_mem0*ADD_mem[0]
	S += (NEW_TX1*ADD[1])-1<NEW_TX_T1_mem0*ADD_mem[1]
	S += (NEW_TX1*ADD[2])-1<NEW_TX_T1_mem0*ADD_mem[2]
	S += (NEW_TX1*ADD[3])-1<NEW_TX_T1_mem0*ADD_mem[3]
	S += NEW_TX_T1_mem0<=NEW_TX_T1

	NEW_TX_T1_mem1 = S.Task('NEW_TX_T1_mem1', length=1, delay_cost=1)
	NEW_TX_T1_mem1 += ADD_mem[0]
	S += T2_1<NEW_TX_T1_mem1
	S += NEW_TX_T1_mem1<=NEW_TX_T1

	NEW_TX_T2 = S.Task('NEW_TX_T2', length=1, delay_cost=1)
	NEW_TX_T2 += alt(ADD)

	NEW_TX_T2_mem0 = S.Task('NEW_TX_T2_mem0', length=1, delay_cost=1)
	NEW_TX_T2_mem0 += alt(ADD_mem)
	S += (NEW_TX0*ADD[0])-1<NEW_TX_T2_mem0*ADD_mem[0]
	S += (NEW_TX0*ADD[1])-1<NEW_TX_T2_mem0*ADD_mem[1]
	S += (NEW_TX0*ADD[2])-1<NEW_TX_T2_mem0*ADD_mem[2]
	S += (NEW_TX0*ADD[3])-1<NEW_TX_T2_mem0*ADD_mem[3]
	S += NEW_TX_T2_mem0<=NEW_TX_T2

	NEW_TX_T2_mem1 = S.Task('NEW_TX_T2_mem1', length=1, delay_cost=1)
	NEW_TX_T2_mem1 += alt(ADD_mem)
	S += (NEW_TX1*ADD[0])-1<NEW_TX_T2_mem1*ADD_mem[0]
	S += (NEW_TX1*ADD[1])-1<NEW_TX_T2_mem1*ADD_mem[1]
	S += (NEW_TX1*ADD[2])-1<NEW_TX_T2_mem1*ADD_mem[2]
	S += (NEW_TX1*ADD[3])-1<NEW_TX_T2_mem1*ADD_mem[3]
	S += NEW_TX_T2_mem1<=NEW_TX_T2

	NEW_TY_T1_in = S.Task('NEW_TY_T1_in', length=1, delay_cost=1)
	NEW_TY_T1_in += alt(MUL_in)
	NEW_TY_T1 = S.Task('NEW_TY_T1', length=7, delay_cost=1)
	NEW_TY_T1 += alt(MUL)
	S+=NEW_TY_T1>=NEW_TY_T1_in

	NEW_TY_T1_mem0 = S.Task('NEW_TY_T1_mem0', length=1, delay_cost=1)
	NEW_TY_T1_mem0 += alt(ADD_mem)
	S += (B31*ADD[0])-1<NEW_TY_T1_mem0*ADD_mem[0]
	S += (B31*ADD[1])-1<NEW_TY_T1_mem0*ADD_mem[1]
	S += (B31*ADD[2])-1<NEW_TY_T1_mem0*ADD_mem[2]
	S += (B31*ADD[3])-1<NEW_TY_T1_mem0*ADD_mem[3]
	S += NEW_TY_T1_mem0<=NEW_TY_T1

	NEW_TY_T1_mem1 = S.Task('NEW_TY_T1_mem1', length=1, delay_cost=1)
	NEW_TY_T1_mem1 += alt(ADD_mem)
	S += (NEW_TY1*ADD[0])-1<NEW_TY_T1_mem1*ADD_mem[0]
	S += (NEW_TY1*ADD[1])-1<NEW_TY_T1_mem1*ADD_mem[1]
	S += (NEW_TY1*ADD[2])-1<NEW_TY_T1_mem1*ADD_mem[2]
	S += (NEW_TY1*ADD[3])-1<NEW_TY_T1_mem1*ADD_mem[3]
	S += NEW_TY_T1_mem1<=NEW_TY_T1

	NEW_TY_T2 = S.Task('NEW_TY_T2', length=1, delay_cost=1)
	NEW_TY_T2 += alt(ADD)

	NEW_TY_T2_mem0 = S.Task('NEW_TY_T2_mem0', length=1, delay_cost=1)
	NEW_TY_T2_mem0 += alt(ADD_mem)
	S += (B30*ADD[0])-1<NEW_TY_T2_mem0*ADD_mem[0]
	S += (B30*ADD[1])-1<NEW_TY_T2_mem0*ADD_mem[1]
	S += (B30*ADD[2])-1<NEW_TY_T2_mem0*ADD_mem[2]
	S += (B30*ADD[3])-1<NEW_TY_T2_mem0*ADD_mem[3]
	S += NEW_TY_T2_mem0<=NEW_TY_T2

	NEW_TY_T2_mem1 = S.Task('NEW_TY_T2_mem1', length=1, delay_cost=1)
	NEW_TY_T2_mem1 += alt(ADD_mem)
	S += (B31*ADD[0])-1<NEW_TY_T2_mem1*ADD_mem[0]
	S += (B31*ADD[1])-1<NEW_TY_T2_mem1*ADD_mem[1]
	S += (B31*ADD[2])-1<NEW_TY_T2_mem1*ADD_mem[2]
	S += (B31*ADD[3])-1<NEW_TY_T2_mem1*ADD_mem[3]
	S += NEW_TY_T2_mem1<=NEW_TY_T2

	NEW_TY_T3 = S.Task('NEW_TY_T3', length=1, delay_cost=1)
	NEW_TY_T3 += alt(ADD)

	NEW_TY_T3_mem0 = S.Task('NEW_TY_T3_mem0', length=1, delay_cost=1)
	NEW_TY_T3_mem0 += alt(ADD_mem)
	S += (NEW_TY0*ADD[0])-1<NEW_TY_T3_mem0*ADD_mem[0]
	S += (NEW_TY0*ADD[1])-1<NEW_TY_T3_mem0*ADD_mem[1]
	S += (NEW_TY0*ADD[2])-1<NEW_TY_T3_mem0*ADD_mem[2]
	S += (NEW_TY0*ADD[3])-1<NEW_TY_T3_mem0*ADD_mem[3]
	S += NEW_TY_T3_mem0<=NEW_TY_T3

	NEW_TY_T3_mem1 = S.Task('NEW_TY_T3_mem1', length=1, delay_cost=1)
	NEW_TY_T3_mem1 += alt(ADD_mem)
	S += (NEW_TY1*ADD[0])-1<NEW_TY_T3_mem1*ADD_mem[0]
	S += (NEW_TY1*ADD[1])-1<NEW_TY_T3_mem1*ADD_mem[1]
	S += (NEW_TY1*ADD[2])-1<NEW_TY_T3_mem1*ADD_mem[2]
	S += (NEW_TY1*ADD[3])-1<NEW_TY_T3_mem1*ADD_mem[3]
	S += NEW_TY_T3_mem1<=NEW_TY_T3

	NEW_TX_T4_in = S.Task('NEW_TX_T4_in', length=1, delay_cost=1)
	NEW_TX_T4_in += alt(MUL_in)
	NEW_TX_T4 = S.Task('NEW_TX_T4', length=7, delay_cost=1)
	NEW_TX_T4 += alt(MUL)
	S+=NEW_TX_T4>=NEW_TX_T4_in

	NEW_TX_T4_mem0 = S.Task('NEW_TX_T4_mem0', length=1, delay_cost=1)
	NEW_TX_T4_mem0 += alt(ADD_mem)
	S += (NEW_TX_T2*ADD[0])-1<NEW_TX_T4_mem0*ADD_mem[0]
	S += (NEW_TX_T2*ADD[1])-1<NEW_TX_T4_mem0*ADD_mem[1]
	S += (NEW_TX_T2*ADD[2])-1<NEW_TX_T4_mem0*ADD_mem[2]
	S += (NEW_TX_T2*ADD[3])-1<NEW_TX_T4_mem0*ADD_mem[3]
	S += NEW_TX_T4_mem0<=NEW_TX_T4

	NEW_TX_T4_mem1 = S.Task('NEW_TX_T4_mem1', length=1, delay_cost=1)
	NEW_TX_T4_mem1 += ADD_mem[0]
	S += NEW_TX_T3<NEW_TX_T4_mem1
	S += NEW_TX_T4_mem1<=NEW_TX_T4

	NEW_TX_T5 = S.Task('NEW_TX_T5', length=1, delay_cost=1)
	NEW_TX_T5 += alt(ADD)

	NEW_TX_T5_mem0 = S.Task('NEW_TX_T5_mem0', length=1, delay_cost=1)
	NEW_TX_T5_mem0 += alt(MUL_mem)
	S += (NEW_TX_T0*MUL[0])-1<NEW_TX_T5_mem0*MUL_mem[0]
	S += NEW_TX_T5_mem0<=NEW_TX_T5

	NEW_TX_T5_mem1 = S.Task('NEW_TX_T5_mem1', length=1, delay_cost=1)
	NEW_TX_T5_mem1 += alt(MUL_mem)
	S += (NEW_TX_T1*MUL[0])-1<NEW_TX_T5_mem1*MUL_mem[0]
	S += NEW_TX_T5_mem1<=NEW_TX_T5

	NEW_TY_T4_in = S.Task('NEW_TY_T4_in', length=1, delay_cost=1)
	NEW_TY_T4_in += alt(MUL_in)
	NEW_TY_T4 = S.Task('NEW_TY_T4', length=7, delay_cost=1)
	NEW_TY_T4 += alt(MUL)
	S+=NEW_TY_T4>=NEW_TY_T4_in

	NEW_TY_T4_mem0 = S.Task('NEW_TY_T4_mem0', length=1, delay_cost=1)
	NEW_TY_T4_mem0 += alt(ADD_mem)
	S += (NEW_TY_T2*ADD[0])-1<NEW_TY_T4_mem0*ADD_mem[0]
	S += (NEW_TY_T2*ADD[1])-1<NEW_TY_T4_mem0*ADD_mem[1]
	S += (NEW_TY_T2*ADD[2])-1<NEW_TY_T4_mem0*ADD_mem[2]
	S += (NEW_TY_T2*ADD[3])-1<NEW_TY_T4_mem0*ADD_mem[3]
	S += NEW_TY_T4_mem0<=NEW_TY_T4

	NEW_TY_T4_mem1 = S.Task('NEW_TY_T4_mem1', length=1, delay_cost=1)
	NEW_TY_T4_mem1 += alt(ADD_mem)
	S += (NEW_TY_T3*ADD[0])-1<NEW_TY_T4_mem1*ADD_mem[0]
	S += (NEW_TY_T3*ADD[1])-1<NEW_TY_T4_mem1*ADD_mem[1]
	S += (NEW_TY_T3*ADD[2])-1<NEW_TY_T4_mem1*ADD_mem[2]
	S += (NEW_TY_T3*ADD[3])-1<NEW_TY_T4_mem1*ADD_mem[3]
	S += NEW_TY_T4_mem1<=NEW_TY_T4

	NEW_TY_T5 = S.Task('NEW_TY_T5', length=1, delay_cost=1)
	NEW_TY_T5 += alt(ADD)

	NEW_TY_T5_mem0 = S.Task('NEW_TY_T5_mem0', length=1, delay_cost=1)
	NEW_TY_T5_mem0 += alt(MUL_mem)
	S += (NEW_TY_T0*MUL[0])-1<NEW_TY_T5_mem0*MUL_mem[0]
	S += NEW_TY_T5_mem0<=NEW_TY_T5

	NEW_TY_T5_mem1 = S.Task('NEW_TY_T5_mem1', length=1, delay_cost=1)
	NEW_TY_T5_mem1 += alt(MUL_mem)
	S += (NEW_TY_T1*MUL[0])-1<NEW_TY_T5_mem1*MUL_mem[0]
	S += NEW_TY_T5_mem1<=NEW_TY_T5

	NEW_TY_0 = S.Task('NEW_TY_0', length=1, delay_cost=1)
	NEW_TY_0 += alt(ADD)

	NEW_TY_0_mem0 = S.Task('NEW_TY_0_mem0', length=1, delay_cost=1)
	NEW_TY_0_mem0 += alt(MUL_mem)
	S += (NEW_TY_T0*MUL[0])-1<NEW_TY_0_mem0*MUL_mem[0]
	S += NEW_TY_0_mem0<=NEW_TY_0

	NEW_TY_0_mem1 = S.Task('NEW_TY_0_mem1', length=1, delay_cost=1)
	NEW_TY_0_mem1 += alt(MUL_mem)
	S += (NEW_TY_T1*MUL[0])-1<NEW_TY_0_mem1*MUL_mem[0]
	S += NEW_TY_0_mem1<=NEW_TY_0

	NEW_TY_1 = S.Task('NEW_TY_1', length=1, delay_cost=1)
	NEW_TY_1 += alt(ADD)

	NEW_TY_1_mem0 = S.Task('NEW_TY_1_mem0', length=1, delay_cost=1)
	NEW_TY_1_mem0 += alt(MUL_mem)
	S += (NEW_TY_T4*MUL[0])-1<NEW_TY_1_mem0*MUL_mem[0]
	S += NEW_TY_1_mem0<=NEW_TY_1

	NEW_TY_1_mem1 = S.Task('NEW_TY_1_mem1', length=1, delay_cost=1)
	NEW_TY_1_mem1 += alt(ADD_mem)
	S += (NEW_TY_T5*ADD[0])-1<NEW_TY_1_mem1*ADD_mem[0]
	S += (NEW_TY_T5*ADD[1])-1<NEW_TY_1_mem1*ADD_mem[1]
	S += (NEW_TY_T5*ADD[2])-1<NEW_TY_1_mem1*ADD_mem[2]
	S += (NEW_TY_T5*ADD[3])-1<NEW_TY_1_mem1*ADD_mem[3]
	S += NEW_TY_1_mem1<=NEW_TY_1

	C010_in = S.Task('C010_in', length=1, delay_cost=1)
	C010_in += alt(MUL_in)
	C010 = S.Task('C010', length=7, delay_cost=1)
	C010 += alt(MUL)
	S+=C010>=C010_in

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	C010_mem0 += ADD_mem[3]
	S += T4_0<C010_mem0
	S += C010_mem0<=C010

	C010_mem1 = S.Task('C010_mem1', length=1, delay_cost=1)
	C010_mem1 += INPUT_mem_r
	S += C010_mem1<=C010

	C010_w = S.Task('C010_w', length=1, delay_cost=1)
	C010_w += alt(INPUT_mem_w)
	S += 0 < C010_w
	S += C010-1 <= C010_w

	C011_in = S.Task('C011_in', length=1, delay_cost=1)
	C011_in += alt(MUL_in)
	C011 = S.Task('C011', length=7, delay_cost=1)
	C011 += alt(MUL)
	S+=C011>=C011_in

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	C011_mem0 += ADD_mem[0]
	S += T4_1<C011_mem0
	S += C011_mem0<=C011

	C011_mem1 = S.Task('C011_mem1', length=1, delay_cost=1)
	C011_mem1 += INPUT_mem_r
	S += C011_mem1<=C011

	C011_w = S.Task('C011_w', length=1, delay_cost=1)
	C011_w += alt(INPUT_mem_w)
	S += 0 < C011_w
	S += C011-1 <= C011_w

	C200_in = S.Task('C200_in', length=1, delay_cost=1)
	C200_in += alt(MUL_in)
	C200 = S.Task('C200', length=7, delay_cost=1)
	C200 += alt(MUL)
	S+=C200>=C200_in

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	C200_mem0 += ADD_mem[0]
	S += T3_0<C200_mem0
	S += C200_mem0<=C200

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	C200_mem1 += INPUT_mem_r
	S += C200_mem1<=C200

	C200_w = S.Task('C200_w', length=1, delay_cost=1)
	C200_w += alt(INPUT_mem_w)
	S += 0 < C200_w
	S += C200-1 <= C200_w

	C201_in = S.Task('C201_in', length=1, delay_cost=1)
	C201_in += alt(MUL_in)
	C201 = S.Task('C201', length=7, delay_cost=1)
	C201 += alt(MUL)
	S+=C201>=C201_in

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	C201_mem0 += ADD_mem[0]
	S += T3_1<C201_mem0
	S += C201_mem0<=C201

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	C201_mem1 += INPUT_mem_r
	S += C201_mem1<=C201

	C201_w = S.Task('C201_w', length=1, delay_cost=1)
	C201_w += alt(INPUT_mem_w)
	S += 0 < C201_w
	S += C201-1 <= C201_w

	NEW_TZ_10 = S.Task('NEW_TZ_10', length=1, delay_cost=1)
	NEW_TZ_10 += alt(ADD)

	NEW_TZ_10_mem0 = S.Task('NEW_TZ_10_mem0', length=1, delay_cost=1)
	NEW_TZ_10_mem0 += alt(ADD_mem)
	S += (NEW_TZ_0*ADD[0])-1<NEW_TZ_10_mem0*ADD_mem[0]
	S += (NEW_TZ_0*ADD[1])-1<NEW_TZ_10_mem0*ADD_mem[1]
	S += (NEW_TZ_0*ADD[2])-1<NEW_TZ_10_mem0*ADD_mem[2]
	S += (NEW_TZ_0*ADD[3])-1<NEW_TZ_10_mem0*ADD_mem[3]
	S += NEW_TZ_10_mem0<=NEW_TZ_10

	NEW_TZ_10_w = S.Task('NEW_TZ_10_w', length=1, delay_cost=1)
	NEW_TZ_10_w += alt(INPUT_mem_w)
	S += 0 < NEW_TZ_10_w
	S += NEW_TZ_10-1 <= NEW_TZ_10_w

	NEW_TZ_11 = S.Task('NEW_TZ_11', length=1, delay_cost=1)
	NEW_TZ_11 += alt(ADD)

	NEW_TZ_11_mem0 = S.Task('NEW_TZ_11_mem0', length=1, delay_cost=1)
	NEW_TZ_11_mem0 += alt(ADD_mem)
	S += (NEW_TZ_1*ADD[0])-1<NEW_TZ_11_mem0*ADD_mem[0]
	S += (NEW_TZ_1*ADD[1])-1<NEW_TZ_11_mem0*ADD_mem[1]
	S += (NEW_TZ_1*ADD[2])-1<NEW_TZ_11_mem0*ADD_mem[2]
	S += (NEW_TZ_1*ADD[3])-1<NEW_TZ_11_mem0*ADD_mem[3]
	S += NEW_TZ_11_mem0<=NEW_TZ_11

	NEW_TZ_11_w = S.Task('NEW_TZ_11_w', length=1, delay_cost=1)
	NEW_TZ_11_w += alt(INPUT_mem_w)
	S += 0 < NEW_TZ_11_w
	S += NEW_TZ_11-1 <= NEW_TZ_11_w

	NEW_TX_0 = S.Task('NEW_TX_0', length=1, delay_cost=1)
	NEW_TX_0 += alt(ADD)

	NEW_TX_0_mem0 = S.Task('NEW_TX_0_mem0', length=1, delay_cost=1)
	NEW_TX_0_mem0 += alt(MUL_mem)
	S += (NEW_TX_T0*MUL[0])-1<NEW_TX_0_mem0*MUL_mem[0]
	S += NEW_TX_0_mem0<=NEW_TX_0

	NEW_TX_0_mem1 = S.Task('NEW_TX_0_mem1', length=1, delay_cost=1)
	NEW_TX_0_mem1 += alt(MUL_mem)
	S += (NEW_TX_T1*MUL[0])-1<NEW_TX_0_mem1*MUL_mem[0]
	S += NEW_TX_0_mem1<=NEW_TX_0

	NEW_TX_0_w = S.Task('NEW_TX_0_w', length=1, delay_cost=1)
	NEW_TX_0_w += alt(INPUT_mem_w)
	S += 0 < NEW_TX_0_w
	S += NEW_TX_0-1 <= NEW_TX_0_w

	NEW_TX_1 = S.Task('NEW_TX_1', length=1, delay_cost=1)
	NEW_TX_1 += alt(ADD)

	NEW_TX_1_mem0 = S.Task('NEW_TX_1_mem0', length=1, delay_cost=1)
	NEW_TX_1_mem0 += alt(MUL_mem)
	S += (NEW_TX_T4*MUL[0])-1<NEW_TX_1_mem0*MUL_mem[0]
	S += NEW_TX_1_mem0<=NEW_TX_1

	NEW_TX_1_mem1 = S.Task('NEW_TX_1_mem1', length=1, delay_cost=1)
	NEW_TX_1_mem1 += alt(ADD_mem)
	S += (NEW_TX_T5*ADD[0])-1<NEW_TX_1_mem1*ADD_mem[0]
	S += (NEW_TX_T5*ADD[1])-1<NEW_TX_1_mem1*ADD_mem[1]
	S += (NEW_TX_T5*ADD[2])-1<NEW_TX_1_mem1*ADD_mem[2]
	S += (NEW_TX_T5*ADD[3])-1<NEW_TX_1_mem1*ADD_mem[3]
	S += NEW_TX_1_mem1<=NEW_TX_1

	NEW_TX_1_w = S.Task('NEW_TX_1_w', length=1, delay_cost=1)
	NEW_TX_1_w += alt(INPUT_mem_w)
	S += 0 < NEW_TX_1_w
	S += NEW_TX_1-1 <= NEW_TX_1_w

	NEW_TY_10 = S.Task('NEW_TY_10', length=1, delay_cost=1)
	NEW_TY_10 += alt(ADD)

	NEW_TY_10_mem0 = S.Task('NEW_TY_10_mem0', length=1, delay_cost=1)
	NEW_TY_10_mem0 += alt(ADD_mem)
	S += (NEW_TY_0*ADD[0])-1<NEW_TY_10_mem0*ADD_mem[0]
	S += (NEW_TY_0*ADD[1])-1<NEW_TY_10_mem0*ADD_mem[1]
	S += (NEW_TY_0*ADD[2])-1<NEW_TY_10_mem0*ADD_mem[2]
	S += (NEW_TY_0*ADD[3])-1<NEW_TY_10_mem0*ADD_mem[3]
	S += NEW_TY_10_mem0<=NEW_TY_10

	NEW_TY_10_mem1 = S.Task('NEW_TY_10_mem1', length=1, delay_cost=1)
	NEW_TY_10_mem1 += MUL_mem[0]
	S += T0_0<NEW_TY_10_mem1
	S += NEW_TY_10_mem1<=NEW_TY_10

	NEW_TY_10_w = S.Task('NEW_TY_10_w', length=1, delay_cost=1)
	NEW_TY_10_w += alt(INPUT_mem_w)
	S += 0 < NEW_TY_10_w
	S += NEW_TY_10-1 <= NEW_TY_10_w

	NEW_TY_11 = S.Task('NEW_TY_11', length=1, delay_cost=1)
	NEW_TY_11 += alt(ADD)

	NEW_TY_11_mem0 = S.Task('NEW_TY_11_mem0', length=1, delay_cost=1)
	NEW_TY_11_mem0 += alt(ADD_mem)
	S += (NEW_TY_1*ADD[0])-1<NEW_TY_11_mem0*ADD_mem[0]
	S += (NEW_TY_1*ADD[1])-1<NEW_TY_11_mem0*ADD_mem[1]
	S += (NEW_TY_1*ADD[2])-1<NEW_TY_11_mem0*ADD_mem[2]
	S += (NEW_TY_1*ADD[3])-1<NEW_TY_11_mem0*ADD_mem[3]
	S += NEW_TY_11_mem0<=NEW_TY_11

	NEW_TY_11_mem1 = S.Task('NEW_TY_11_mem1', length=1, delay_cost=1)
	NEW_TY_11_mem1 += ADD_mem[0]
	S += T0_1<NEW_TY_11_mem1
	S += NEW_TY_11_mem1<=NEW_TY_11

	NEW_TY_11_w = S.Task('NEW_TY_11_w', length=1, delay_cost=1)
	NEW_TY_11_w += alt(INPUT_mem_w)
	S += 0 < NEW_TY_11_w
	S += NEW_TY_11-1 <= NEW_TY_11_w

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "pdbl_mul1_add4/pdbl_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_pdbl_mul1_add4_1(0, 0)