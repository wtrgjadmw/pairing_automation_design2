from pyschedule import Scenario, solvers, plotters, alt

def solve_pdbl_mul1_add4_2(ConstStep, ExpStep):
	horizon = 137
	S=Scenario("pdbl_mul1_add4_2",horizon = horizon)

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

	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	S += T3T2 >= 1
	T3T2 += MUL[0]

	T4T0_in = S.Task('T4T0_in', length=1, delay_cost=1)
	S += T4T0_in >= 1
	T4T0_in += MUL_in[0]

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	S += T4T0_mem0 >= 1
	T4T0_mem0 += INPUT_mem_r

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	S += T4T0_mem1 >= 1
	T4T0_mem1 += INPUT_mem_r

	T4T0 = S.Task('T4T0', length=7, delay_cost=1)
	S += T4T0 >= 2
	T4T0 += MUL[0]

	T4T1_in = S.Task('T4T1_in', length=1, delay_cost=1)
	S += T4T1_in >= 2
	T4T1_in += MUL_in[0]

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	S += T4T1_mem0 >= 2
	T4T1_mem0 += INPUT_mem_r

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	S += T4T1_mem1 >= 2
	T4T1_mem1 += INPUT_mem_r

	T2T1_in = S.Task('T2T1_in', length=1, delay_cost=1)
	S += T2T1_in >= 3
	T2T1_in += MUL_in[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 3
	T2T1_mem0 += INPUT_mem_r

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 3
	T2T1_mem1 += INPUT_mem_r

	T4T1 = S.Task('T4T1', length=7, delay_cost=1)
	S += T4T1 >= 3
	T4T1 += MUL[0]

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	S += T2T0_in >= 4
	T2T0_in += MUL_in[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 4
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 4
	T2T0_mem1 += INPUT_mem_r

	T2T1 = S.Task('T2T1', length=7, delay_cost=1)
	S += T2T1 >= 4
	T2T1 += MUL[0]

	T0T2_in = S.Task('T0T2_in', length=1, delay_cost=1)
	S += T0T2_in >= 5
	T0T2_in += MUL_in[0]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 5
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 5
	T0T2_mem1 += INPUT_mem_r

	T2T0 = S.Task('T2T0', length=7, delay_cost=1)
	S += T2T0 >= 5
	T2T0 += MUL[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 6
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 6
	T0T0_mem1 += INPUT_mem_r

	T0T2 = S.Task('T0T2', length=7, delay_cost=1)
	S += T0T2 >= 6
	T0T2 += MUL[0]

	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	S += T0T0 >= 7
	T0T0 += ADD[3]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 7
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 7
	T0T1_mem1 += INPUT_mem_r

	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	S += T00_in >= 8
	T00_in += MUL_in[0]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 8
	T00_mem0 += ADD_mem[3]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 8
	T00_mem1 += ADD_mem[3]

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	S += T0T1 >= 8
	T0T1 += ADD[3]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 8
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 8
	T1T1_mem1 += INPUT_mem_r

	T00 = S.Task('T00', length=7, delay_cost=1)
	S += T00 >= 9
	T00 += MUL[0]

	T1T1 = S.Task('T1T1', length=1, delay_cost=1)
	S += T1T1 >= 9
	T1T1 += ADD[0]

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
	T3_1_mem1 += ADD_mem[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 9
	T40_mem0 += MUL_mem[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 9
	T40_mem1 += MUL_mem[0]

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 10
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 10
	T1T0_mem1 += INPUT_mem_r

	T1T2 = S.Task('T1T2', length=7, delay_cost=1)
	S += T1T2 >= 10
	T1T2 += MUL[0]

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 10
	T3_1 += ADD[1]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 10
	T40 += ADD[0]

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	S += T4T5_mem0 >= 10
	T4T5_mem0 += MUL_mem[0]

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	S += T4T5_mem1 >= 10
	T4T5_mem1 += MUL_mem[0]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 11
	T10_in += MUL_in[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 11
	T10_mem0 += ADD_mem[1]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 11
	T10_mem1 += ADD_mem[0]

	T1T0 = S.Task('T1T0', length=1, delay_cost=1)
	S += T1T0 >= 11
	T1T0 += ADD[1]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 11
	T20_mem0 += MUL_mem[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 11
	T20_mem1 += MUL_mem[0]

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	S += T4T3_mem0 >= 11
	T4T3_mem0 += INPUT_mem_r

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	S += T4T3_mem1 >= 11
	T4T3_mem1 += INPUT_mem_r

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	S += T4T5 >= 11
	T4T5 += ADD[3]

	T10 = S.Task('T10', length=7, delay_cost=1)
	S += T10 >= 12
	T10 += MUL[0]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 12
	T20 += ADD[1]

	T2T5_mem0 = S.Task('T2T5_mem0', length=1, delay_cost=1)
	S += T2T5_mem0 >= 12
	T2T5_mem0 += MUL_mem[0]

	T2T5_mem1 = S.Task('T2T5_mem1', length=1, delay_cost=1)
	S += T2T5_mem1 >= 12
	T2T5_mem1 += MUL_mem[0]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 12
	T4T2_mem0 += INPUT_mem_r

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 12
	T4T2_mem1 += INPUT_mem_r

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	S += T4T3 >= 12
	T4T3 += ADD[2]

	T2T5 = S.Task('T2T5', length=1, delay_cost=1)
	S += T2T5 >= 13
	T2T5 += ADD[1]

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 13
	T3T0_mem0 += INPUT_mem_r

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 13
	T3T0_mem1 += INPUT_mem_r

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	S += T4T2 >= 13
	T4T2 += ADD[3]

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	S += T4T4_in >= 13
	T4T4_in += MUL_in[0]

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	S += T4T4_mem0 >= 13
	T4T4_mem0 += ADD_mem[3]

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	S += T4T4_mem1 >= 13
	T4T4_mem1 += ADD_mem[2]

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	S += T3T0 >= 14
	T3T0 += ADD[3]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 14
	T3T1_mem0 += INPUT_mem_r

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 14
	T3T1_mem1 += INPUT_mem_r

	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	S += T4T4 >= 14
	T4T4 += MUL[0]

	NEW_TZT2_mem0 = S.Task('NEW_TZT2_mem0', length=1, delay_cost=1)
	S += NEW_TZT2_mem0 >= 15
	NEW_TZT2_mem0 += MUL_mem[0]

	NEW_TZT2_mem1 = S.Task('NEW_TZT2_mem1', length=1, delay_cost=1)
	S += NEW_TZT2_mem1 >= 15
	NEW_TZT2_mem1 += ADD_mem[1]

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	S += T0_T0_mem0 >= 15
	T0_T0_mem0 += MUL_mem[0]

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	S += T0_T0_mem1 >= 15
	T0_T0_mem1 += ADD_mem[1]

	T2T3_mem0 = S.Task('T2T3_mem0', length=1, delay_cost=1)
	S += T2T3_mem0 >= 15
	T2T3_mem0 += INPUT_mem_r

	T2T3_mem1 = S.Task('T2T3_mem1', length=1, delay_cost=1)
	S += T2T3_mem1 >= 15
	T2T3_mem1 += INPUT_mem_r

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 15
	T30_in += MUL_in[0]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 15
	T30_mem0 += ADD_mem[3]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 15
	T30_mem1 += ADD_mem[0]

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	S += T3T1 >= 15
	T3T1 += ADD[0]

	NEW_TZT2 = S.Task('NEW_TZT2', length=1, delay_cost=1)
	S += NEW_TZT2 >= 16
	NEW_TZT2 += ADD[0]

	T0_T0 = S.Task('T0_T0', length=1, delay_cost=1)
	S += T0_T0 >= 16
	T0_T0 += ADD[1]

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	S += T0_T1_mem0 >= 16
	T0_T1_mem0 += MUL_mem[0]

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	S += T0_T1_mem1 >= 16
	T0_T1_mem1 += ADD_mem[1]

	T0_T2_in = S.Task('T0_T2_in', length=1, delay_cost=1)
	S += T0_T2_in >= 16
	T0_T2_in += MUL_in[0]

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	S += T0_T2_mem0 >= 16
	T0_T2_mem0 += MUL_mem[0]

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	S += T0_T2_mem1 >= 16
	T0_T2_mem1 += ADD_mem[1]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 16
	T2T2_mem0 += INPUT_mem_r

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 16
	T2T2_mem1 += INPUT_mem_r

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	S += T2T3 >= 16
	T2T3 += ADD[2]

	T30 = S.Task('T30', length=7, delay_cost=1)
	S += T30 >= 16
	T30 += MUL[0]

	T0_T1 = S.Task('T0_T1', length=1, delay_cost=1)
	S += T0_T1 >= 17
	T0_T1 += ADD[1]

	T0_T2 = S.Task('T0_T2', length=7, delay_cost=1)
	S += T0_T2 >= 17
	T0_T2 += MUL[0]

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	S += T1_T2_mem0 >= 17
	T1_T2_mem0 += INPUT_mem_r

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	S += T1_T2_mem1 >= 17
	T1_T2_mem1 += INPUT_mem_r

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	S += T2T2 >= 17
	T2T2 += ADD[2]

	T2T4_in = S.Task('T2T4_in', length=1, delay_cost=1)
	S += T2T4_in >= 17
	T2T4_in += MUL_in[0]

	T2T4_mem0 = S.Task('T2T4_mem0', length=1, delay_cost=1)
	S += T2T4_mem0 >= 17
	T2T4_mem0 += ADD_mem[2]

	T2T4_mem1 = S.Task('T2T4_mem1', length=1, delay_cost=1)
	S += T2T4_mem1 >= 17
	T2T4_mem1 += ADD_mem[2]

	T1_T0_in = S.Task('T1_T0_in', length=1, delay_cost=1)
	S += T1_T0_in >= 18
	T1_T0_in += MUL_in[0]

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	S += T1_T0_mem0 >= 18
	T1_T0_mem0 += INPUT_mem_r

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	S += T1_T0_mem1 >= 18
	T1_T0_mem1 += MUL_mem[0]

	T1_T2 = S.Task('T1_T2', length=1, delay_cost=1)
	S += T1_T2 >= 18
	T1_T2 += ADD[0]

	T1_T3_mem0 = S.Task('T1_T3_mem0', length=1, delay_cost=1)
	S += T1_T3_mem0 >= 18
	T1_T3_mem0 += MUL_mem[0]

	T1_T3_mem1 = S.Task('T1_T3_mem1', length=1, delay_cost=1)
	S += T1_T3_mem1 >= 18
	T1_T3_mem1 += ADD_mem[1]

	T2T4 = S.Task('T2T4', length=7, delay_cost=1)
	S += T2T4 >= 18
	T2T4 += MUL[0]

	T1_T0 = S.Task('T1_T0', length=7, delay_cost=1)
	S += T1_T0 >= 19
	T1_T0 += MUL[0]

	T1_T1_in = S.Task('T1_T1_in', length=1, delay_cost=1)
	S += T1_T1_in >= 19
	T1_T1_in += MUL_in[0]

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	S += T1_T1_mem0 >= 19
	T1_T1_mem0 += INPUT_mem_r

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	S += T1_T1_mem1 >= 19
	T1_T1_mem1 += ADD_mem[1]

	T1_T3 = S.Task('T1_T3', length=1, delay_cost=1)
	S += T1_T3 >= 19
	T1_T3 += ADD[0]

	T1_T1 = S.Task('T1_T1', length=7, delay_cost=1)
	S += T1_T1 >= 20
	T1_T1 += MUL[0]

	T1_T4_in = S.Task('T1_T4_in', length=1, delay_cost=1)
	S += T1_T4_in >= 20
	T1_T4_in += MUL_in[0]

	T1_T4_mem0 = S.Task('T1_T4_mem0', length=1, delay_cost=1)
	S += T1_T4_mem0 >= 20
	T1_T4_mem0 += ADD_mem[0]

	T1_T4_mem1 = S.Task('T1_T4_mem1', length=1, delay_cost=1)
	S += T1_T4_mem1 >= 20
	T1_T4_mem1 += ADD_mem[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 20
	T41_mem0 += MUL_mem[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 20
	T41_mem1 += ADD_mem[3]

	NEW_TZT0_in = S.Task('NEW_TZT0_in', length=1, delay_cost=1)
	S += NEW_TZT0_in >= 21
	NEW_TZT0_in += MUL_in[0]

	NEW_TZT0_mem0 = S.Task('NEW_TZT0_mem0', length=1, delay_cost=1)
	S += NEW_TZT0_mem0 >= 21
	NEW_TZT0_mem0 += MUL_mem[0]

	NEW_TZT0_mem1 = S.Task('NEW_TZT0_mem1', length=1, delay_cost=1)
	S += NEW_TZT0_mem1 >= 21
	NEW_TZT0_mem1 += ADD_mem[2]

	T1_T4 = S.Task('T1_T4', length=7, delay_cost=1)
	S += T1_T4 >= 21
	T1_T4 += MUL[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 21
	T41 += ADD[0]

	C011_in = S.Task('C011_in', length=1, delay_cost=1)
	S += C011_in >= 22
	C011_in += MUL_in[0]

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	S += C011_mem0 >= 22
	C011_mem0 += ADD_mem[0]

	C011_mem1 = S.Task('C011_mem1', length=1, delay_cost=1)
	S += C011_mem1 >= 22
	C011_mem1 += INPUT_mem_r

	NEW_TZT0 = S.Task('NEW_TZT0', length=7, delay_cost=1)
	S += NEW_TZT0 >= 22
	NEW_TZT0 += MUL[0]

	NEW_TZT3_mem0 = S.Task('NEW_TZT3_mem0', length=1, delay_cost=1)
	S += NEW_TZT3_mem0 >= 22
	NEW_TZT3_mem0 += ADD_mem[2]

	NEW_TZT3_mem1 = S.Task('NEW_TZT3_mem1', length=1, delay_cost=1)
	S += NEW_TZT3_mem1 >= 22
	NEW_TZT3_mem1 += ADD_mem[0]

	C011 = S.Task('C011', length=7, delay_cost=1)
	S += C011 >= 23
	C011 += MUL[0]

	NEW_TZT1_in = S.Task('NEW_TZT1_in', length=1, delay_cost=1)
	S += NEW_TZT1_in >= 23
	NEW_TZT1_in += MUL_in[0]

	NEW_TZT1_mem0 = S.Task('NEW_TZT1_mem0', length=1, delay_cost=1)
	S += NEW_TZT1_mem0 >= 23
	NEW_TZT1_mem0 += ADD_mem[2]

	NEW_TZT1_mem1 = S.Task('NEW_TZT1_mem1', length=1, delay_cost=1)
	S += NEW_TZT1_mem1 >= 23
	NEW_TZT1_mem1 += ADD_mem[0]

	NEW_TZT3 = S.Task('NEW_TZT3', length=1, delay_cost=1)
	S += NEW_TZT3 >= 23
	NEW_TZT3 += ADD[3]

	NEW_TZT1 = S.Task('NEW_TZT1', length=7, delay_cost=1)
	S += NEW_TZT1 >= 24
	NEW_TZT1 += MUL[0]

	NEW_TZT4_in = S.Task('NEW_TZT4_in', length=1, delay_cost=1)
	S += NEW_TZT4_in >= 24
	NEW_TZT4_in += MUL_in[0]

	NEW_TZT4_mem0 = S.Task('NEW_TZT4_mem0', length=1, delay_cost=1)
	S += NEW_TZT4_mem0 >= 24
	NEW_TZT4_mem0 += ADD_mem[0]

	NEW_TZT4_mem1 = S.Task('NEW_TZT4_mem1', length=1, delay_cost=1)
	S += NEW_TZT4_mem1 >= 24
	NEW_TZT4_mem1 += ADD_mem[3]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 24
	T21_mem0 += MUL_mem[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 24
	T21_mem1 += ADD_mem[1]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 24
	T3_0_mem0 += ADD_mem[0]

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 24
	T3_0_mem1 += MUL_mem[0]

	C200_in = S.Task('C200_in', length=1, delay_cost=1)
	S += C200_in >= 25
	C200_in += MUL_in[0]

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	S += C200_mem0 >= 25
	C200_mem0 += ADD_mem[0]

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	S += C200_mem1 >= 25
	C200_mem1 += INPUT_mem_r

	NEW_TZT4 = S.Task('NEW_TZT4', length=7, delay_cost=1)
	S += NEW_TZT4 >= 25
	NEW_TZT4 += MUL[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 25
	T21 += ADD[3]

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 25
	T3_0 += ADD[0]

	C010_in = S.Task('C010_in', length=1, delay_cost=1)
	S += C010_in >= 26
	C010_in += MUL_in[0]

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	S += C010_mem0 >= 26
	C010_mem0 += ADD_mem[2]

	C010_mem1 = S.Task('C010_mem1', length=1, delay_cost=1)
	S += C010_mem1 >= 26
	C010_mem1 += INPUT_mem_r

	C200 = S.Task('C200', length=7, delay_cost=1)
	S += C200 >= 26
	C200 += MUL[0]

	NEW_TX_T3_mem0 = S.Task('NEW_TX_T3_mem0', length=1, delay_cost=1)
	S += NEW_TX_T3_mem0 >= 26
	NEW_TX_T3_mem0 += ADD_mem[0]

	NEW_TX_T3_mem1 = S.Task('NEW_TX_T3_mem1', length=1, delay_cost=1)
	S += NEW_TX_T3_mem1 >= 26
	NEW_TX_T3_mem1 += ADD_mem[1]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 26
	T1_0_mem0 += MUL_mem[0]

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 26
	T1_0_mem1 += MUL_mem[0]

	C010 = S.Task('C010', length=7, delay_cost=1)
	S += C010 >= 27
	C010 += MUL[0]

	C201_in = S.Task('C201_in', length=1, delay_cost=1)
	S += C201_in >= 27
	C201_in += MUL_in[0]

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	S += C201_mem0 >= 27
	C201_mem0 += ADD_mem[1]

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	S += C201_mem1 >= 27
	C201_mem1 += INPUT_mem_r

	NEW_TX_T3 = S.Task('NEW_TX_T3', length=1, delay_cost=1)
	S += NEW_TX_T3 >= 27
	NEW_TX_T3 += ADD[2]

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	S += T1_0 >= 27
	T1_0 += ADD[3]

	T1_T5_mem0 = S.Task('T1_T5_mem0', length=1, delay_cost=1)
	S += T1_T5_mem0 >= 27
	T1_T5_mem0 += MUL_mem[0]

	T1_T5_mem1 = S.Task('T1_T5_mem1', length=1, delay_cost=1)
	S += T1_T5_mem1 >= 27
	T1_T5_mem1 += MUL_mem[0]

	C201 = S.Task('C201', length=7, delay_cost=1)
	S += C201 >= 28
	C201 += MUL[0]

	T0_0_in = S.Task('T0_0_in', length=1, delay_cost=1)
	S += T0_0_in >= 28
	T0_0_in += MUL_in[0]

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	S += T0_0_mem0 >= 28
	T0_0_mem0 += ADD_mem[1]

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	S += T0_0_mem1 >= 28
	T0_0_mem1 += ADD_mem[1]

	T1_10_mem0 = S.Task('T1_10_mem0', length=1, delay_cost=1)
	S += T1_10_mem0 >= 28
	T1_10_mem0 += ADD_mem[3]

	T1_10_mem1 = S.Task('T1_10_mem1', length=1, delay_cost=1)
	S += T1_10_mem1 >= 28
	T1_10_mem1 += ADD_mem[3]

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 28
	T1_1_mem0 += MUL_mem[0]

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	S += T1_1_mem1 >= 28
	T1_1_mem1 += ADD_mem[0]

	T1_T5 = S.Task('T1_T5', length=1, delay_cost=1)
	S += T1_T5 >= 28
	T1_T5 += ADD[0]

	B30_mem0 = S.Task('B30_mem0', length=1, delay_cost=1)
	S += B30_mem0 >= 29
	B30_mem0 += INPUT_mem_r

	B30_mem1 = S.Task('B30_mem1', length=1, delay_cost=1)
	S += B30_mem1 >= 29
	B30_mem1 += ADD_mem[2]

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	S += C000_mem0 >= 29
	C000_mem0 += MUL_mem[0]

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	S += C000_mem1 >= 29
	C000_mem1 += ADD_mem[2]

	C011_w = S.Task('C011_w', length=1, delay_cost=1)
	S += C011_w >= 29
	C011_w += INPUT_mem_w

	T0_0 = S.Task('T0_0', length=7, delay_cost=1)
	S += T0_0 >= 29
	T0_0 += MUL[0]

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 29
	T1_1 += ADD[0]

	T1_10 = S.Task('T1_10', length=1, delay_cost=1)
	S += T1_10 >= 29
	T1_10 += ADD[2]

	B30 = S.Task('B30', length=1, delay_cost=1)
	S += B30 >= 30
	B30 += ADD[0]

	C000 = S.Task('C000', length=1, delay_cost=1)
	S += C000 >= 30
	C000 += ADD[1]

	NEW_TX0_mem0 = S.Task('NEW_TX0_mem0', length=1, delay_cost=1)
	S += NEW_TX0_mem0 >= 30
	NEW_TX0_mem0 += ADD_mem[1]

	NEW_TX0_mem1 = S.Task('NEW_TX0_mem1', length=1, delay_cost=1)
	S += NEW_TX0_mem1 >= 30
	NEW_TX0_mem1 += INPUT_mem_r

	NEW_TZT5_mem0 = S.Task('NEW_TZT5_mem0', length=1, delay_cost=1)
	S += NEW_TZT5_mem0 >= 30
	NEW_TZT5_mem0 += MUL_mem[0]

	NEW_TZT5_mem1 = S.Task('NEW_TZT5_mem1', length=1, delay_cost=1)
	S += NEW_TZT5_mem1 >= 30
	NEW_TZT5_mem1 += MUL_mem[0]

	T1_11_mem0 = S.Task('T1_11_mem0', length=1, delay_cost=1)
	S += T1_11_mem0 >= 30
	T1_11_mem0 += ADD_mem[2]

	T1_11_mem1 = S.Task('T1_11_mem1', length=1, delay_cost=1)
	S += T1_11_mem1 >= 30
	T1_11_mem1 += ADD_mem[0]

	B31_mem0 = S.Task('B31_mem0', length=1, delay_cost=1)
	S += B31_mem0 >= 31
	B31_mem0 += INPUT_mem_r

	B31_mem1 = S.Task('B31_mem1', length=1, delay_cost=1)
	S += B31_mem1 >= 31
	B31_mem1 += ADD_mem[3]

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	S += C001_mem0 >= 31
	C001_mem0 += ADD_mem[2]

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	S += C001_mem1 >= 31
	C001_mem1 += ADD_mem[3]

	NEW_TX0 = S.Task('NEW_TX0', length=1, delay_cost=1)
	S += NEW_TX0 >= 31
	NEW_TX0 += ADD[1]

	NEW_TX_T0_in = S.Task('NEW_TX_T0_in', length=1, delay_cost=1)
	S += NEW_TX_T0_in >= 31
	NEW_TX_T0_in += MUL_in[0]

	NEW_TX_T0_mem0 = S.Task('NEW_TX_T0_mem0', length=1, delay_cost=1)
	S += NEW_TX_T0_mem0 >= 31
	NEW_TX_T0_mem0 += ADD_mem[1]

	NEW_TX_T0_mem1 = S.Task('NEW_TX_T0_mem1', length=1, delay_cost=1)
	S += NEW_TX_T0_mem1 >= 31
	NEW_TX_T0_mem1 += ADD_mem[0]

	NEW_TY0_mem0 = S.Task('NEW_TY0_mem0', length=1, delay_cost=1)
	S += NEW_TY0_mem0 >= 31
	NEW_TY0_mem0 += MUL_mem[0]

	NEW_TY0_mem1 = S.Task('NEW_TY0_mem1', length=1, delay_cost=1)
	S += NEW_TY0_mem1 >= 31
	NEW_TY0_mem1 += ADD_mem[1]

	NEW_TZ1_mem0 = S.Task('NEW_TZ1_mem0', length=1, delay_cost=1)
	S += NEW_TZ1_mem0 >= 31
	NEW_TZ1_mem0 += MUL_mem[0]

	NEW_TZ1_mem1 = S.Task('NEW_TZ1_mem1', length=1, delay_cost=1)
	S += NEW_TZ1_mem1 >= 31
	NEW_TZ1_mem1 += ADD_mem[2]

	NEW_TZT5 = S.Task('NEW_TZT5', length=1, delay_cost=1)
	S += NEW_TZT5 >= 31
	NEW_TZT5 += ADD[2]

	T1_11 = S.Task('T1_11', length=1, delay_cost=1)
	S += T1_11 >= 31
	T1_11 += ADD[3]

	B31 = S.Task('B31', length=1, delay_cost=1)
	S += B31 >= 32
	B31 += ADD[2]

	C001 = S.Task('C001', length=1, delay_cost=1)
	S += C001 >= 32
	C001 += ADD[3]

	C200_w = S.Task('C200_w', length=1, delay_cost=1)
	S += C200_w >= 32
	C200_w += INPUT_mem_w

	NEW_TX1_mem0 = S.Task('NEW_TX1_mem0', length=1, delay_cost=1)
	S += NEW_TX1_mem0 >= 32
	NEW_TX1_mem0 += ADD_mem[3]

	NEW_TX1_mem1 = S.Task('NEW_TX1_mem1', length=1, delay_cost=1)
	S += NEW_TX1_mem1 >= 32
	NEW_TX1_mem1 += INPUT_mem_r

	NEW_TX_T0 = S.Task('NEW_TX_T0', length=7, delay_cost=1)
	S += NEW_TX_T0 >= 32
	NEW_TX_T0 += MUL[0]

	NEW_TY0 = S.Task('NEW_TY0', length=1, delay_cost=1)
	S += NEW_TY0 >= 32
	NEW_TY0 += ADD[0]

	NEW_TY1_mem0 = S.Task('NEW_TY1_mem0', length=1, delay_cost=1)
	S += NEW_TY1_mem0 >= 32
	NEW_TY1_mem0 += ADD_mem[2]

	NEW_TY1_mem1 = S.Task('NEW_TY1_mem1', length=1, delay_cost=1)
	S += NEW_TY1_mem1 >= 32
	NEW_TY1_mem1 += ADD_mem[3]

	NEW_TY_T0_in = S.Task('NEW_TY_T0_in', length=1, delay_cost=1)
	S += NEW_TY_T0_in >= 32
	NEW_TY_T0_in += MUL_in[0]

	NEW_TY_T0_mem0 = S.Task('NEW_TY_T0_mem0', length=1, delay_cost=1)
	S += NEW_TY_T0_mem0 >= 32
	NEW_TY_T0_mem0 += ADD_mem[0]

	NEW_TY_T0_mem1 = S.Task('NEW_TY_T0_mem1', length=1, delay_cost=1)
	S += NEW_TY_T0_mem1 >= 32
	NEW_TY_T0_mem1 += ADD_mem[0]

	NEW_TZ0_mem0 = S.Task('NEW_TZ0_mem0', length=1, delay_cost=1)
	S += NEW_TZ0_mem0 >= 32
	NEW_TZ0_mem0 += MUL_mem[0]

	NEW_TZ0_mem1 = S.Task('NEW_TZ0_mem1', length=1, delay_cost=1)
	S += NEW_TZ0_mem1 >= 32
	NEW_TZ0_mem1 += MUL_mem[0]

	NEW_TZ1 = S.Task('NEW_TZ1', length=1, delay_cost=1)
	S += NEW_TZ1 >= 32
	NEW_TZ1 += ADD[1]

	C010_w = S.Task('C010_w', length=1, delay_cost=1)
	S += C010_w >= 33
	C010_w += INPUT_mem_w

	NEW_TX1 = S.Task('NEW_TX1', length=1, delay_cost=1)
	S += NEW_TX1 >= 33
	NEW_TX1 += ADD[2]

	NEW_TY1 = S.Task('NEW_TY1', length=1, delay_cost=1)
	S += NEW_TY1 >= 33
	NEW_TY1 += ADD[0]

	NEW_TY_T0 = S.Task('NEW_TY_T0', length=7, delay_cost=1)
	S += NEW_TY_T0 >= 33
	NEW_TY_T0 += MUL[0]

	NEW_TY_T1_in = S.Task('NEW_TY_T1_in', length=1, delay_cost=1)
	S += NEW_TY_T1_in >= 33
	NEW_TY_T1_in += MUL_in[0]

	NEW_TY_T1_mem0 = S.Task('NEW_TY_T1_mem0', length=1, delay_cost=1)
	S += NEW_TY_T1_mem0 >= 33
	NEW_TY_T1_mem0 += ADD_mem[2]

	NEW_TY_T1_mem1 = S.Task('NEW_TY_T1_mem1', length=1, delay_cost=1)
	S += NEW_TY_T1_mem1 >= 33
	NEW_TY_T1_mem1 += ADD_mem[0]

	NEW_TY_T2_mem0 = S.Task('NEW_TY_T2_mem0', length=1, delay_cost=1)
	S += NEW_TY_T2_mem0 >= 33
	NEW_TY_T2_mem0 += ADD_mem[0]

	NEW_TY_T2_mem1 = S.Task('NEW_TY_T2_mem1', length=1, delay_cost=1)
	S += NEW_TY_T2_mem1 >= 33
	NEW_TY_T2_mem1 += ADD_mem[2]

	NEW_TZ0 = S.Task('NEW_TZ0', length=1, delay_cost=1)
	S += NEW_TZ0 >= 33
	NEW_TZ0 += ADD[3]

	C201_w = S.Task('C201_w', length=1, delay_cost=1)
	S += C201_w >= 34
	C201_w += INPUT_mem_w

	NEW_TX_T1_in = S.Task('NEW_TX_T1_in', length=1, delay_cost=1)
	S += NEW_TX_T1_in >= 34
	NEW_TX_T1_in += MUL_in[0]

	NEW_TX_T1_mem0 = S.Task('NEW_TX_T1_mem0', length=1, delay_cost=1)
	S += NEW_TX_T1_mem0 >= 34
	NEW_TX_T1_mem0 += ADD_mem[2]

	NEW_TX_T1_mem1 = S.Task('NEW_TX_T1_mem1', length=1, delay_cost=1)
	S += NEW_TX_T1_mem1 >= 34
	NEW_TX_T1_mem1 += ADD_mem[1]

	NEW_TX_T2_mem0 = S.Task('NEW_TX_T2_mem0', length=1, delay_cost=1)
	S += NEW_TX_T2_mem0 >= 34
	NEW_TX_T2_mem0 += ADD_mem[1]

	NEW_TX_T2_mem1 = S.Task('NEW_TX_T2_mem1', length=1, delay_cost=1)
	S += NEW_TX_T2_mem1 >= 34
	NEW_TX_T2_mem1 += ADD_mem[2]

	NEW_TY_T1 = S.Task('NEW_TY_T1', length=7, delay_cost=1)
	S += NEW_TY_T1 >= 34
	NEW_TY_T1 += MUL[0]

	NEW_TY_T2 = S.Task('NEW_TY_T2', length=1, delay_cost=1)
	S += NEW_TY_T2 >= 34
	NEW_TY_T2 += ADD[2]

	NEW_TY_T3_mem0 = S.Task('NEW_TY_T3_mem0', length=1, delay_cost=1)
	S += NEW_TY_T3_mem0 >= 34
	NEW_TY_T3_mem0 += ADD_mem[0]

	NEW_TY_T3_mem1 = S.Task('NEW_TY_T3_mem1', length=1, delay_cost=1)
	S += NEW_TY_T3_mem1 >= 34
	NEW_TY_T3_mem1 += ADD_mem[0]

	NEW_TX_T1 = S.Task('NEW_TX_T1', length=7, delay_cost=1)
	S += NEW_TX_T1 >= 35
	NEW_TX_T1 += MUL[0]

	NEW_TX_T2 = S.Task('NEW_TX_T2', length=1, delay_cost=1)
	S += NEW_TX_T2 >= 35
	NEW_TX_T2 += ADD[2]

	NEW_TY_T3 = S.Task('NEW_TY_T3', length=1, delay_cost=1)
	S += NEW_TY_T3 >= 35
	NEW_TY_T3 += ADD[0]

	NEW_TY_T4_in = S.Task('NEW_TY_T4_in', length=1, delay_cost=1)
	S += NEW_TY_T4_in >= 35
	NEW_TY_T4_in += MUL_in[0]

	NEW_TY_T4_mem0 = S.Task('NEW_TY_T4_mem0', length=1, delay_cost=1)
	S += NEW_TY_T4_mem0 >= 35
	NEW_TY_T4_mem0 += ADD_mem[2]

	NEW_TY_T4_mem1 = S.Task('NEW_TY_T4_mem1', length=1, delay_cost=1)
	S += NEW_TY_T4_mem1 >= 35
	NEW_TY_T4_mem1 += ADD_mem[0]

	NEW_TX_T4_in = S.Task('NEW_TX_T4_in', length=1, delay_cost=1)
	S += NEW_TX_T4_in >= 36
	NEW_TX_T4_in += MUL_in[0]

	NEW_TX_T4_mem0 = S.Task('NEW_TX_T4_mem0', length=1, delay_cost=1)
	S += NEW_TX_T4_mem0 >= 36
	NEW_TX_T4_mem0 += ADD_mem[2]

	NEW_TX_T4_mem1 = S.Task('NEW_TX_T4_mem1', length=1, delay_cost=1)
	S += NEW_TX_T4_mem1 >= 36
	NEW_TX_T4_mem1 += ADD_mem[2]

	NEW_TY_T4 = S.Task('NEW_TY_T4', length=7, delay_cost=1)
	S += NEW_TY_T4 >= 36
	NEW_TY_T4 += MUL[0]

	NEW_TX_T4 = S.Task('NEW_TX_T4', length=7, delay_cost=1)
	S += NEW_TX_T4 >= 37
	NEW_TX_T4 += MUL[0]

	NEW_TY_T5_mem0 = S.Task('NEW_TY_T5_mem0', length=1, delay_cost=1)
	S += NEW_TY_T5_mem0 >= 40
	NEW_TY_T5_mem0 += MUL_mem[0]

	NEW_TY_T5_mem1 = S.Task('NEW_TY_T5_mem1', length=1, delay_cost=1)
	S += NEW_TY_T5_mem1 >= 40
	NEW_TY_T5_mem1 += MUL_mem[0]

	NEW_TY_0_mem0 = S.Task('NEW_TY_0_mem0', length=1, delay_cost=1)
	S += NEW_TY_0_mem0 >= 41
	NEW_TY_0_mem0 += MUL_mem[0]

	NEW_TY_0_mem1 = S.Task('NEW_TY_0_mem1', length=1, delay_cost=1)
	S += NEW_TY_0_mem1 >= 41
	NEW_TY_0_mem1 += MUL_mem[0]

	NEW_TY_T5 = S.Task('NEW_TY_T5', length=1, delay_cost=1)
	S += NEW_TY_T5 >= 41
	NEW_TY_T5 += ADD[3]

	NEW_TY_0 = S.Task('NEW_TY_0', length=1, delay_cost=1)
	S += NEW_TY_0 >= 42
	NEW_TY_0 += ADD[0]

	NEW_TY_10_mem0 = S.Task('NEW_TY_10_mem0', length=1, delay_cost=1)
	S += NEW_TY_10_mem0 >= 42
	NEW_TY_10_mem0 += ADD_mem[0]

	NEW_TY_10_mem1 = S.Task('NEW_TY_10_mem1', length=1, delay_cost=1)
	S += NEW_TY_10_mem1 >= 42
	NEW_TY_10_mem1 += MUL_mem[0]

	NEW_TY_1_mem0 = S.Task('NEW_TY_1_mem0', length=1, delay_cost=1)
	S += NEW_TY_1_mem0 >= 42
	NEW_TY_1_mem0 += MUL_mem[0]

	NEW_TY_1_mem1 = S.Task('NEW_TY_1_mem1', length=1, delay_cost=1)
	S += NEW_TY_1_mem1 >= 42
	NEW_TY_1_mem1 += ADD_mem[3]

	NEW_TX_0_mem0 = S.Task('NEW_TX_0_mem0', length=1, delay_cost=1)
	S += NEW_TX_0_mem0 >= 43
	NEW_TX_0_mem0 += MUL_mem[0]

	NEW_TX_0_mem1 = S.Task('NEW_TX_0_mem1', length=1, delay_cost=1)
	S += NEW_TX_0_mem1 >= 43
	NEW_TX_0_mem1 += MUL_mem[0]

	NEW_TY_1 = S.Task('NEW_TY_1', length=1, delay_cost=1)
	S += NEW_TY_1 >= 43
	NEW_TY_1 += ADD[0]

	NEW_TY_10 = S.Task('NEW_TY_10', length=1, delay_cost=1)
	S += NEW_TY_10 >= 43
	NEW_TY_10 += ADD[1]

	NEW_TY_10_w = S.Task('NEW_TY_10_w', length=1, delay_cost=1)
	S += NEW_TY_10_w >= 43
	NEW_TY_10_w += INPUT_mem_w

	NEW_TY_11_mem0 = S.Task('NEW_TY_11_mem0', length=1, delay_cost=1)
	S += NEW_TY_11_mem0 >= 43
	NEW_TY_11_mem0 += ADD_mem[0]

	NEW_TY_11_mem1 = S.Task('NEW_TY_11_mem1', length=1, delay_cost=1)
	S += NEW_TY_11_mem1 >= 43
	NEW_TY_11_mem1 += ADD_mem[3]

	NEW_TX_0 = S.Task('NEW_TX_0', length=1, delay_cost=1)
	S += NEW_TX_0 >= 44
	NEW_TX_0 += ADD[0]

	NEW_TX_0_w = S.Task('NEW_TX_0_w', length=1, delay_cost=1)
	S += NEW_TX_0_w >= 44
	NEW_TX_0_w += INPUT_mem_w

	NEW_TX_T5_mem0 = S.Task('NEW_TX_T5_mem0', length=1, delay_cost=1)
	S += NEW_TX_T5_mem0 >= 44
	NEW_TX_T5_mem0 += MUL_mem[0]

	NEW_TX_T5_mem1 = S.Task('NEW_TX_T5_mem1', length=1, delay_cost=1)
	S += NEW_TX_T5_mem1 >= 44
	NEW_TX_T5_mem1 += MUL_mem[0]

	NEW_TY_11 = S.Task('NEW_TY_11', length=1, delay_cost=1)
	S += NEW_TY_11 >= 44
	NEW_TY_11 += ADD[2]

	NEW_TY_11_w = S.Task('NEW_TY_11_w', length=1, delay_cost=1)
	S += NEW_TY_11_w >= 44
	NEW_TY_11_w += INPUT_mem_w

	NEW_TX_1_mem0 = S.Task('NEW_TX_1_mem0', length=1, delay_cost=1)
	S += NEW_TX_1_mem0 >= 45
	NEW_TX_1_mem0 += MUL_mem[0]

	NEW_TX_1_mem1 = S.Task('NEW_TX_1_mem1', length=1, delay_cost=1)
	S += NEW_TX_1_mem1 >= 45
	NEW_TX_1_mem1 += ADD_mem[0]

	NEW_TX_T5 = S.Task('NEW_TX_T5', length=1, delay_cost=1)
	S += NEW_TX_T5 >= 45
	NEW_TX_T5 += ADD[0]

	NEW_TX_1 = S.Task('NEW_TX_1', length=1, delay_cost=1)
	S += NEW_TX_1 >= 46
	NEW_TX_1 += ADD[0]

	NEW_TX_1_w = S.Task('NEW_TX_1_w', length=1, delay_cost=1)
	S += NEW_TX_1_w >= 46
	NEW_TX_1_w += INPUT_mem_w


	# new tasks
	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += MUL_mem[0]
	S += 12<T01_mem0
	S += T01_mem0<=T01

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	T01_mem1 += MUL_mem[0]
	S += 12<T01_mem1
	S += T01_mem1<=T01

	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(ADD)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MUL_mem[0]
	S += 16<T11_mem0
	S += T11_mem0<=T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += MUL_mem[0]
	S += 16<T11_mem1
	S += T11_mem1<=T11

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += MUL_mem[0]
	S += 7<T31_mem0
	S += T31_mem0<=T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += MUL_mem[0]
	S += 7<T31_mem1
	S += T31_mem1<=T31

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	T2_0 += alt(ADD)

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	T2_0_mem0 += ADD_mem[1]
	S += 12<T2_0_mem0
	S += T2_0_mem0<=T2_0

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	T2_0_mem1 += ADD_mem[1]
	S += 12<T2_0_mem1
	S += T2_0_mem1<=T2_0

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += MUL_mem[0]
	S += 22<T60_mem0
	S += T60_mem0<=T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += MUL_mem[0]
	S += 22<T60_mem1
	S += T60_mem1<=T60

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T61_mem0*ADD_mem[0]
	S += (T31*ADD[1])-1<T61_mem0*ADD_mem[1]
	S += (T31*ADD[2])-1<T61_mem0*ADD_mem[2]
	S += (T31*ADD[3])-1<T61_mem0*ADD_mem[3]
	S += T61_mem0<=T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T61_mem1*ADD_mem[0]
	S += (T31*ADD[1])-1<T61_mem1*ADD_mem[1]
	S += (T31*ADD[2])-1<T61_mem1*ADD_mem[2]
	S += (T31*ADD[3])-1<T61_mem1*ADD_mem[3]
	S += T61_mem1<=T61

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	T4_0 += alt(ADD)

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	T4_0_mem0 += ADD_mem[0]
	S += 10<T4_0_mem0
	S += T4_0_mem0<=T4_0

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	T4_0_mem1 += ADD_mem[0]
	S += 10<T4_0_mem1
	S += T4_0_mem1<=T4_0

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	T2_1 += alt(ADD)

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	T2_1_mem0 += ADD_mem[3]
	S += 25<T2_1_mem0
	S += T2_1_mem0<=T2_1

	T2_1_mem1 = S.Task('T2_1_mem1', length=1, delay_cost=1)
	T2_1_mem1 += ADD_mem[3]
	S += 25<T2_1_mem1
	S += T2_1_mem1<=T2_1

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	T4_1 += alt(ADD)

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	T4_1_mem0 += ADD_mem[0]
	S += 21<T4_1_mem0
	S += T4_1_mem0<=T4_1

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	T4_1_mem1 += ADD_mem[0]
	S += 21<T4_1_mem1
	S += T4_1_mem1<=T4_1

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	T0_1 += alt(ADD)

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	T0_1_mem0 += MUL_mem[0]
	S += 23<T0_1_mem0
	S += T0_1_mem0<=T0_1

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	T0_1_mem1 += MUL_mem[0]
	S += 23<T0_1_mem1
	S += T0_1_mem1<=T0_1

	B_0 = S.Task('B_0', length=1, delay_cost=1)
	B_0 += alt(ADD)

	B_0_mem0 = S.Task('B_0_mem0', length=1, delay_cost=1)
	B_0_mem0 += ADD_mem[3]
	S += 27<B_0_mem0
	S += B_0_mem0<=B_0

	B_0_mem1 = S.Task('B_0_mem1', length=1, delay_cost=1)
	B_0_mem1 += ADD_mem[3]
	S += 27<B_0_mem1
	S += B_0_mem1<=B_0

	B_1 = S.Task('B_1', length=1, delay_cost=1)
	B_1 += alt(ADD)

	B_1_mem0 = S.Task('B_1_mem0', length=1, delay_cost=1)
	B_1_mem0 += ADD_mem[0]
	S += 29<B_1_mem0
	S += B_1_mem0<=B_1

	B_1_mem1 = S.Task('B_1_mem1', length=1, delay_cost=1)
	B_1_mem1 += ADD_mem[0]
	S += 29<B_1_mem1
	S += B_1_mem1<=B_1

	NEW_TZ_0 = S.Task('NEW_TZ_0', length=1, delay_cost=1)
	NEW_TZ_0 += alt(ADD)

	NEW_TZ_0_mem0 = S.Task('NEW_TZ_0_mem0', length=1, delay_cost=1)
	NEW_TZ_0_mem0 += ADD_mem[3]
	S += 33<NEW_TZ_0_mem0
	S += NEW_TZ_0_mem0<=NEW_TZ_0

	NEW_TZ_0_mem1 = S.Task('NEW_TZ_0_mem1', length=1, delay_cost=1)
	NEW_TZ_0_mem1 += ADD_mem[3]
	S += 33<NEW_TZ_0_mem1
	S += NEW_TZ_0_mem1<=NEW_TZ_0

	NEW_TZ_1 = S.Task('NEW_TZ_1', length=1, delay_cost=1)
	NEW_TZ_1 += alt(ADD)

	NEW_TZ_1_mem0 = S.Task('NEW_TZ_1_mem0', length=1, delay_cost=1)
	NEW_TZ_1_mem0 += ADD_mem[1]
	S += 32<NEW_TZ_1_mem0
	S += NEW_TZ_1_mem0<=NEW_TZ_1

	NEW_TZ_1_mem1 = S.Task('NEW_TZ_1_mem1', length=1, delay_cost=1)
	NEW_TZ_1_mem1 += ADD_mem[1]
	S += 32<NEW_TZ_1_mem1
	S += NEW_TZ_1_mem1<=NEW_TZ_1

	NEW_TZ_10 = S.Task('NEW_TZ_10', length=1, delay_cost=1)
	NEW_TZ_10 += alt(ADD)

	NEW_TZ_10_mem0 = S.Task('NEW_TZ_10_mem0', length=1, delay_cost=1)
	NEW_TZ_10_mem0 += alt(ADD_mem)
	S += (NEW_TZ_0*ADD[0])-1<NEW_TZ_10_mem0*ADD_mem[0]
	S += (NEW_TZ_0*ADD[1])-1<NEW_TZ_10_mem0*ADD_mem[1]
	S += (NEW_TZ_0*ADD[2])-1<NEW_TZ_10_mem0*ADD_mem[2]
	S += (NEW_TZ_0*ADD[3])-1<NEW_TZ_10_mem0*ADD_mem[3]
	S += NEW_TZ_10_mem0<=NEW_TZ_10

	NEW_TZ_10_mem1 = S.Task('NEW_TZ_10_mem1', length=1, delay_cost=1)
	NEW_TZ_10_mem1 += alt(ADD_mem)
	S += (NEW_TZ_0*ADD[0])-1<NEW_TZ_10_mem1*ADD_mem[0]
	S += (NEW_TZ_0*ADD[1])-1<NEW_TZ_10_mem1*ADD_mem[1]
	S += (NEW_TZ_0*ADD[2])-1<NEW_TZ_10_mem1*ADD_mem[2]
	S += (NEW_TZ_0*ADD[3])-1<NEW_TZ_10_mem1*ADD_mem[3]
	S += NEW_TZ_10_mem1<=NEW_TZ_10

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

	NEW_TZ_11_mem1 = S.Task('NEW_TZ_11_mem1', length=1, delay_cost=1)
	NEW_TZ_11_mem1 += alt(ADD_mem)
	S += (NEW_TZ_1*ADD[0])-1<NEW_TZ_11_mem1*ADD_mem[0]
	S += (NEW_TZ_1*ADD[1])-1<NEW_TZ_11_mem1*ADD_mem[1]
	S += (NEW_TZ_1*ADD[2])-1<NEW_TZ_11_mem1*ADD_mem[2]
	S += (NEW_TZ_1*ADD[3])-1<NEW_TZ_11_mem1*ADD_mem[3]
	S += NEW_TZ_11_mem1<=NEW_TZ_11

	NEW_TZ_11_w = S.Task('NEW_TZ_11_w', length=1, delay_cost=1)
	NEW_TZ_11_w += alt(INPUT_mem_w)
	S += 0 < NEW_TZ_11_w
	S += NEW_TZ_11-1 <= NEW_TZ_11_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01, time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "pdbl_mul1_add4/pdbl_mul1_add4_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_pdbl_mul1_add4_2(0, 0)