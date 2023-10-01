from pyschedule import Scenario, solvers, plotters, alt

def solve_padd_mul1_add4_1(ConstStep, ExpStep):
	horizon = 111
	S=Scenario("padd_mul1_add4_1",horizon = horizon)

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
	T1T1_in = S.Task('T1T1_in', length=1, delay_cost=1)
	S += T1T1_in >= 0
	T1T1_in += MUL_in[0]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 0
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 0
	T1T1_mem1 += INPUT_mem_r

	T1T0_in = S.Task('T1T0_in', length=1, delay_cost=1)
	S += T1T0_in >= 1
	T1T0_in += MUL_in[0]

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 1
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 1
	T1T0_mem1 += INPUT_mem_r

	T1T1 = S.Task('T1T1', length=7, delay_cost=1)
	S += T1T1 >= 1
	T1T1 += MUL[0]

	T1T0 = S.Task('T1T0', length=7, delay_cost=1)
	S += T1T0 >= 2
	T1T0 += MUL[0]

	T1T3_mem0 = S.Task('T1T3_mem0', length=1, delay_cost=1)
	S += T1T3_mem0 >= 2
	T1T3_mem0 += INPUT_mem_r

	T1T3_mem1 = S.Task('T1T3_mem1', length=1, delay_cost=1)
	S += T1T3_mem1 >= 2
	T1T3_mem1 += INPUT_mem_r

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	S += T1T2_mem0 >= 3
	T1T2_mem0 += INPUT_mem_r

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	S += T1T2_mem1 >= 3
	T1T2_mem1 += INPUT_mem_r

	T1T3 = S.Task('T1T3', length=1, delay_cost=1)
	S += T1T3 >= 3
	T1T3 += ADD[3]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 4
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 4
	T0T2_mem1 += INPUT_mem_r

	T1T2 = S.Task('T1T2', length=1, delay_cost=1)
	S += T1T2 >= 4
	T1T2 += ADD[2]

	T1T4_in = S.Task('T1T4_in', length=1, delay_cost=1)
	S += T1T4_in >= 4
	T1T4_in += MUL_in[0]

	T1T4_mem0 = S.Task('T1T4_mem0', length=1, delay_cost=1)
	S += T1T4_mem0 >= 4
	T1T4_mem0 += ADD_mem[2]

	T1T4_mem1 = S.Task('T1T4_mem1', length=1, delay_cost=1)
	S += T1T4_mem1 >= 4
	T1T4_mem1 += ADD_mem[3]

	T0T1_in = S.Task('T0T1_in', length=1, delay_cost=1)
	S += T0T1_in >= 5
	T0T1_in += MUL_in[0]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 5
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 5
	T0T1_mem1 += INPUT_mem_r

	T0T2 = S.Task('T0T2', length=1, delay_cost=1)
	S += T0T2 >= 5
	T0T2 += ADD[1]

	T1T4 = S.Task('T1T4', length=7, delay_cost=1)
	S += T1T4 >= 5
	T1T4 += MUL[0]

	T0T0_in = S.Task('T0T0_in', length=1, delay_cost=1)
	S += T0T0_in >= 6
	T0T0_in += MUL_in[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 6
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 6
	T0T0_mem1 += INPUT_mem_r

	T0T1 = S.Task('T0T1', length=7, delay_cost=1)
	S += T0T1 >= 6
	T0T1 += MUL[0]

	T0T0 = S.Task('T0T0', length=7, delay_cost=1)
	S += T0T0 >= 7
	T0T0 += MUL[0]

	T0T3_mem0 = S.Task('T0T3_mem0', length=1, delay_cost=1)
	S += T0T3_mem0 >= 7
	T0T3_mem0 += INPUT_mem_r

	T0T3_mem1 = S.Task('T0T3_mem1', length=1, delay_cost=1)
	S += T0T3_mem1 >= 7
	T0T3_mem1 += INPUT_mem_r

	C00T2_mem0 = S.Task('C00T2_mem0', length=1, delay_cost=1)
	S += C00T2_mem0 >= 8
	C00T2_mem0 += INPUT_mem_r

	C00T2_mem1 = S.Task('C00T2_mem1', length=1, delay_cost=1)
	S += C00T2_mem1 >= 8
	C00T2_mem1 += INPUT_mem_r

	T0T3 = S.Task('T0T3', length=1, delay_cost=1)
	S += T0T3 >= 8
	T0T3 += ADD[3]

	T0T4_in = S.Task('T0T4_in', length=1, delay_cost=1)
	S += T0T4_in >= 8
	T0T4_in += MUL_in[0]

	T0T4_mem0 = S.Task('T0T4_mem0', length=1, delay_cost=1)
	S += T0T4_mem0 >= 8
	T0T4_mem0 += ADD_mem[1]

	T0T4_mem1 = S.Task('T0T4_mem1', length=1, delay_cost=1)
	S += T0T4_mem1 >= 8
	T0T4_mem1 += ADD_mem[3]

	T1T5_mem0 = S.Task('T1T5_mem0', length=1, delay_cost=1)
	S += T1T5_mem0 >= 8
	T1T5_mem0 += MUL_mem[0]

	T1T5_mem1 = S.Task('T1T5_mem1', length=1, delay_cost=1)
	S += T1T5_mem1 >= 8
	T1T5_mem1 += MUL_mem[0]

	C00T2 = S.Task('C00T2', length=1, delay_cost=1)
	S += C00T2 >= 9
	C00T2 += ADD[3]

	T0T4 = S.Task('T0T4', length=7, delay_cost=1)
	S += T0T4 >= 9
	T0T4 += MUL[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 9
	T10_mem0 += MUL_mem[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 9
	T10_mem1 += MUL_mem[0]

	T1T5 = S.Task('T1T5', length=1, delay_cost=1)
	S += T1T5 >= 9
	T1T5 += ADD[2]

	T3_T2_mem0 = S.Task('T3_T2_mem0', length=1, delay_cost=1)
	S += T3_T2_mem0 >= 9
	T3_T2_mem0 += INPUT_mem_r

	T3_T2_mem1 = S.Task('T3_T2_mem1', length=1, delay_cost=1)
	S += T3_T2_mem1 >= 9
	T3_T2_mem1 += INPUT_mem_r

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 10
	T10 += ADD[2]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 10
	T1_0_mem0 += INPUT_mem_r

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 10
	T1_0_mem1 += ADD_mem[2]

	T3_T2 = S.Task('T3_T2', length=1, delay_cost=1)
	S += T3_T2 >= 10
	T3_T2 += ADD[1]

	NEW_TZT2_mem0 = S.Task('NEW_TZT2_mem0', length=1, delay_cost=1)
	S += NEW_TZT2_mem0 >= 11
	NEW_TZT2_mem0 += INPUT_mem_r

	NEW_TZT2_mem1 = S.Task('NEW_TZT2_mem1', length=1, delay_cost=1)
	S += NEW_TZT2_mem1 >= 11
	NEW_TZT2_mem1 += INPUT_mem_r

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 11
	T11_mem0 += MUL_mem[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 11
	T11_mem1 += ADD_mem[2]

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	S += T1_0 >= 11
	T1_0 += ADD[3]

	C00T0_in = S.Task('C00T0_in', length=1, delay_cost=1)
	S += C00T0_in >= 12
	C00T0_in += MUL_in[0]

	C00T0_mem0 = S.Task('C00T0_mem0', length=1, delay_cost=1)
	S += C00T0_mem0 >= 12
	C00T0_mem0 += INPUT_mem_r

	C00T0_mem1 = S.Task('C00T0_mem1', length=1, delay_cost=1)
	S += C00T0_mem1 >= 12
	C00T0_mem1 += ADD_mem[3]

	NEW_TZT2 = S.Task('NEW_TZT2', length=1, delay_cost=1)
	S += NEW_TZT2 >= 12
	NEW_TZT2 += ADD[0]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 12
	T11 += ADD[1]

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 12
	T1_1_mem0 += INPUT_mem_r

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	S += T1_1_mem1 >= 12
	T1_1_mem1 += ADD_mem[1]

	C00T0 = S.Task('C00T0', length=7, delay_cost=1)
	S += C00T0 >= 13
	C00T0 += MUL[0]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 13
	T00_mem0 += MUL_mem[0]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 13
	T00_mem1 += MUL_mem[0]

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 13
	T1_1 += ADD[1]

	T3T2_in = S.Task('T3T2_in', length=1, delay_cost=1)
	S += T3T2_in >= 13
	T3T2_in += MUL_in[0]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 13
	T3T2_mem0 += ADD_mem[3]

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 13
	T3T2_mem1 += ADD_mem[1]

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	S += T5T2_mem0 >= 13
	T5T2_mem0 += INPUT_mem_r

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	S += T5T2_mem1 >= 13
	T5T2_mem1 += INPUT_mem_r

	C00T1_in = S.Task('C00T1_in', length=1, delay_cost=1)
	S += C00T1_in >= 14
	C00T1_in += MUL_in[0]

	C00T1_mem0 = S.Task('C00T1_mem0', length=1, delay_cost=1)
	S += C00T1_mem0 >= 14
	C00T1_mem0 += INPUT_mem_r

	C00T1_mem1 = S.Task('C00T1_mem1', length=1, delay_cost=1)
	S += C00T1_mem1 >= 14
	C00T1_mem1 += ADD_mem[1]

	T00 = S.Task('T00', length=1, delay_cost=1)
	S += T00 >= 14
	T00 += ADD[0]

	T0T5_mem0 = S.Task('T0T5_mem0', length=1, delay_cost=1)
	S += T0T5_mem0 >= 14
	T0T5_mem0 += MUL_mem[0]

	T0T5_mem1 = S.Task('T0T5_mem1', length=1, delay_cost=1)
	S += T0T5_mem1 >= 14
	T0T5_mem1 += MUL_mem[0]

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	S += T0_0_mem0 >= 14
	T0_0_mem0 += INPUT_mem_r

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	S += T0_0_mem1 >= 14
	T0_0_mem1 += ADD_mem[0]

	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	S += T3T2 >= 14
	T3T2 += MUL[0]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 14
	T4T2_mem0 += ADD_mem[3]

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 14
	T4T2_mem1 += ADD_mem[1]

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	S += T5T2 >= 14
	T5T2 += ADD[2]

	C00T1 = S.Task('C00T1', length=7, delay_cost=1)
	S += C00T1 >= 15
	C00T1 += MUL[0]

	NEW_TXT2_mem0 = S.Task('NEW_TXT2_mem0', length=1, delay_cost=1)
	S += NEW_TXT2_mem0 >= 15
	NEW_TXT2_mem0 += ADD_mem[3]

	NEW_TXT2_mem1 = S.Task('NEW_TXT2_mem1', length=1, delay_cost=1)
	S += NEW_TXT2_mem1 >= 15
	NEW_TXT2_mem1 += ADD_mem[1]

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 15
	T01_mem0 += MUL_mem[0]

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	S += T01_mem1 >= 15
	T01_mem1 += ADD_mem[0]

	T0T5 = S.Task('T0T5', length=1, delay_cost=1)
	S += T0T5 >= 15
	T0T5 += ADD[0]

	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	S += T0_0 >= 15
	T0_0 += ADD[2]

	T0_1T2_mem0 = S.Task('T0_1T2_mem0', length=1, delay_cost=1)
	S += T0_1T2_mem0 >= 15
	T0_1T2_mem0 += INPUT_mem_r

	T0_1T2_mem1 = S.Task('T0_1T2_mem1', length=1, delay_cost=1)
	S += T0_1T2_mem1 >= 15
	T0_1T2_mem1 += INPUT_mem_r

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 15
	T3T0_mem0 += ADD_mem[3]

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 15
	T3T0_mem1 += ADD_mem[1]

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	S += T4T2 >= 15
	T4T2 += ADD[3]

	NEW_TXT2 = S.Task('NEW_TXT2', length=1, delay_cost=1)
	S += NEW_TXT2 >= 16
	NEW_TXT2 += ADD[0]

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 16
	T01 += ADD[1]

	T0_1T0_in = S.Task('T0_1T0_in', length=1, delay_cost=1)
	S += T0_1T0_in >= 16
	T0_1T0_in += MUL_in[0]

	T0_1T0_mem0 = S.Task('T0_1T0_mem0', length=1, delay_cost=1)
	S += T0_1T0_mem0 >= 16
	T0_1T0_mem0 += INPUT_mem_r

	T0_1T0_mem1 = S.Task('T0_1T0_mem1', length=1, delay_cost=1)
	S += T0_1T0_mem1 >= 16
	T0_1T0_mem1 += ADD_mem[2]

	T0_1T2 = S.Task('T0_1T2', length=1, delay_cost=1)
	S += T0_1T2 >= 16
	T0_1T2 += ADD[2]

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	S += T0_1_mem0 >= 16
	T0_1_mem0 += INPUT_mem_r

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	S += T0_1_mem1 >= 16
	T0_1_mem1 += ADD_mem[1]

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	S += T3T0 >= 16
	T3T0 += ADD[3]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 16
	T3T1_mem0 += ADD_mem[3]

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 16
	T3T1_mem1 += ADD_mem[1]

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	S += T0_1 >= 17
	T0_1 += ADD[0]

	T0_1T0 = S.Task('T0_1T0', length=7, delay_cost=1)
	S += T0_1T0 >= 17
	T0_1T0 += MUL[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 17
	T2T0_mem0 += ADD_mem[2]

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 17
	T2T0_mem1 += ADD_mem[0]

	T2T2_in = S.Task('T2T2_in', length=1, delay_cost=1)
	S += T2T2_in >= 17
	T2T2_in += MUL_in[0]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 17
	T2T2_mem0 += ADD_mem[2]

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 17
	T2T2_mem1 += ADD_mem[0]

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	S += T3T1 >= 17
	T3T1 += ADD[1]

	T8T2_mem0 = S.Task('T8T2_mem0', length=1, delay_cost=1)
	S += T8T2_mem0 >= 17
	T8T2_mem0 += INPUT_mem_r

	T8T2_mem1 = S.Task('T8T2_mem1', length=1, delay_cost=1)
	S += T8T2_mem1 >= 17
	T8T2_mem1 += INPUT_mem_r

	T0_1T1_in = S.Task('T0_1T1_in', length=1, delay_cost=1)
	S += T0_1T1_in >= 18
	T0_1T1_in += MUL_in[0]

	T0_1T1_mem0 = S.Task('T0_1T1_mem0', length=1, delay_cost=1)
	S += T0_1T1_mem0 >= 18
	T0_1T1_mem0 += INPUT_mem_r

	T0_1T1_mem1 = S.Task('T0_1T1_mem1', length=1, delay_cost=1)
	S += T0_1T1_mem1 >= 18
	T0_1T1_mem1 += ADD_mem[0]

	T2T0 = S.Task('T2T0', length=1, delay_cost=1)
	S += T2T0 >= 18
	T2T0 += ADD[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 18
	T2T1_mem0 += ADD_mem[2]

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 18
	T2T1_mem1 += ADD_mem[0]

	T2T2 = S.Task('T2T2', length=7, delay_cost=1)
	S += T2T2 >= 18
	T2T2 += MUL[0]

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	S += T8T2 >= 18
	T8T2 += ADD[3]

	T0_1T1 = S.Task('T0_1T1', length=7, delay_cost=1)
	S += T0_1T1 >= 19
	T0_1T1 += MUL[0]

	T0_1T3_mem0 = S.Task('T0_1T3_mem0', length=1, delay_cost=1)
	S += T0_1T3_mem0 >= 19
	T0_1T3_mem0 += ADD_mem[2]

	T0_1T3_mem1 = S.Task('T0_1T3_mem1', length=1, delay_cost=1)
	S += T0_1T3_mem1 >= 19
	T0_1T3_mem1 += ADD_mem[0]

	T2T1 = S.Task('T2T1', length=1, delay_cost=1)
	S += T2T1 >= 19
	T2T1 += ADD[0]

	T7_T2_mem0 = S.Task('T7_T2_mem0', length=1, delay_cost=1)
	S += T7_T2_mem0 >= 19
	T7_T2_mem0 += ADD_mem[2]

	T7_T2_mem1 = S.Task('T7_T2_mem1', length=1, delay_cost=1)
	S += T7_T2_mem1 >= 19
	T7_T2_mem1 += ADD_mem[0]

	T0_1T3 = S.Task('T0_1T3', length=1, delay_cost=1)
	S += T0_1T3 >= 20
	T0_1T3 += ADD[0]

	T7_T2 = S.Task('T7_T2', length=1, delay_cost=1)
	S += T7_T2 >= 20
	T7_T2 += ADD[3]


	# new tasks
	C00T3 = S.Task('C00T3', length=1, delay_cost=1)
	C00T3 += alt(ADD)

	C00T3_mem0 = S.Task('C00T3_mem0', length=1, delay_cost=1)
	C00T3_mem0 += ADD_mem[3]
	S += 11<C00T3_mem0
	S += C00T3_mem0<=C00T3

	C00T3_mem1 = S.Task('C00T3_mem1', length=1, delay_cost=1)
	C00T3_mem1 += ADD_mem[1]
	S += 13<C00T3_mem1
	S += C00T3_mem1<=C00T3

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	T20_in += alt(MUL_in)
	T20 = S.Task('T20', length=7, delay_cost=1)
	T20 += alt(MUL)
	S+=T20>=T20_in

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += ADD_mem[0]
	S += 18<T20_mem0
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += ADD_mem[0]
	S += 19<T20_mem1
	S += T20_mem1<=T20

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(ADD)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += MUL_mem[0]
	S += 24<T21_mem0
	S += T21_mem0<=T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += MUL_mem[0]
	S += 24<T21_mem1
	S += T21_mem1<=T21

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	T30_in += alt(MUL_in)
	T30 = S.Task('T30', length=7, delay_cost=1)
	T30 += alt(MUL)
	S+=T30>=T30_in

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += ADD_mem[3]
	S += 16<T30_mem0
	S += T30_mem0<=T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += ADD_mem[1]
	S += 17<T30_mem1
	S += T30_mem1<=T30

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += MUL_mem[0]
	S += 20<T31_mem0
	S += T31_mem0<=T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += MUL_mem[0]
	S += 20<T31_mem1
	S += T31_mem1<=T31

	C00T4_in = S.Task('C00T4_in', length=1, delay_cost=1)
	C00T4_in += alt(MUL_in)
	C00T4 = S.Task('C00T4', length=7, delay_cost=1)
	C00T4 += alt(MUL)
	S+=C00T4>=C00T4_in

	C00T4_mem0 = S.Task('C00T4_mem0', length=1, delay_cost=1)
	C00T4_mem0 += ADD_mem[3]
	S += 9<C00T4_mem0
	S += C00T4_mem0<=C00T4

	C00T4_mem1 = S.Task('C00T4_mem1', length=1, delay_cost=1)
	C00T4_mem1 += alt(ADD_mem)
	S += (C00T3*ADD[0])-1<C00T4_mem1*ADD_mem[0]
	S += (C00T3*ADD[1])-1<C00T4_mem1*ADD_mem[1]
	S += (C00T3*ADD[2])-1<C00T4_mem1*ADD_mem[2]
	S += (C00T3*ADD[3])-1<C00T4_mem1*ADD_mem[3]
	S += C00T4_mem1<=C00T4

	C00T5 = S.Task('C00T5', length=1, delay_cost=1)
	C00T5 += alt(ADD)

	C00T5_mem0 = S.Task('C00T5_mem0', length=1, delay_cost=1)
	C00T5_mem0 += MUL_mem[0]
	S += 19<C00T5_mem0
	S += C00T5_mem0<=C00T5

	C00T5_mem1 = S.Task('C00T5_mem1', length=1, delay_cost=1)
	C00T5_mem1 += MUL_mem[0]
	S += 21<C00T5_mem1
	S += C00T5_mem1<=C00T5

	C000 = S.Task('C000', length=1, delay_cost=1)
	C000 += alt(ADD)

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	C000_mem0 += MUL_mem[0]
	S += 19<C000_mem0
	S += C000_mem0<=C000

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	C000_mem1 += MUL_mem[0]
	S += 21<C000_mem1
	S += C000_mem1<=C000

	T0_1T4_in = S.Task('T0_1T4_in', length=1, delay_cost=1)
	T0_1T4_in += alt(MUL_in)
	T0_1T4 = S.Task('T0_1T4', length=7, delay_cost=1)
	T0_1T4 += alt(MUL)
	S+=T0_1T4>=T0_1T4_in

	T0_1T4_mem0 = S.Task('T0_1T4_mem0', length=1, delay_cost=1)
	T0_1T4_mem0 += ADD_mem[2]
	S += 16<T0_1T4_mem0
	S += T0_1T4_mem0<=T0_1T4

	T0_1T4_mem1 = S.Task('T0_1T4_mem1', length=1, delay_cost=1)
	T0_1T4_mem1 += ADD_mem[0]
	S += 20<T0_1T4_mem1
	S += T0_1T4_mem1<=T0_1T4

	T0_1T5 = S.Task('T0_1T5', length=1, delay_cost=1)
	T0_1T5 += alt(ADD)

	T0_1T5_mem0 = S.Task('T0_1T5_mem0', length=1, delay_cost=1)
	T0_1T5_mem0 += MUL_mem[0]
	S += 23<T0_1T5_mem0
	S += T0_1T5_mem0<=T0_1T5

	T0_1T5_mem1 = S.Task('T0_1T5_mem1', length=1, delay_cost=1)
	T0_1T5_mem1 += MUL_mem[0]
	S += 25<T0_1T5_mem1
	S += T0_1T5_mem1<=T0_1T5

	T0_10 = S.Task('T0_10', length=1, delay_cost=1)
	T0_10 += alt(ADD)

	T0_10_mem0 = S.Task('T0_10_mem0', length=1, delay_cost=1)
	T0_10_mem0 += MUL_mem[0]
	S += 23<T0_10_mem0
	S += T0_10_mem0<=T0_10

	T0_10_mem1 = S.Task('T0_10_mem1', length=1, delay_cost=1)
	T0_10_mem1 += MUL_mem[0]
	S += 25<T0_10_mem1
	S += T0_10_mem1<=T0_10

	T4T0_in = S.Task('T4T0_in', length=1, delay_cost=1)
	T4T0_in += alt(MUL_in)
	T4T0 = S.Task('T4T0', length=7, delay_cost=1)
	T4T0 += alt(MUL)
	S+=T4T0>=T4T0_in

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	T4T0_mem0 += ADD_mem[3]
	S += 11<T4T0_mem0
	S += T4T0_mem0<=T4T0

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	T4T0_mem1 += alt(MUL_mem)
	S += (T30*MUL[0])-1<T4T0_mem1*MUL_mem[0]
	S += T4T0_mem1<=T4T0

	T4T1_in = S.Task('T4T1_in', length=1, delay_cost=1)
	T4T1_in += alt(MUL_in)
	T4T1 = S.Task('T4T1', length=7, delay_cost=1)
	T4T1 += alt(MUL)
	S+=T4T1>=T4T1_in

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	T4T1_mem0 += ADD_mem[1]
	S += 13<T4T1_mem0
	S += T4T1_mem0<=T4T1

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	T4T1_mem1 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T4T1_mem1*ADD_mem[0]
	S += (T31*ADD[1])-1<T4T1_mem1*ADD_mem[1]
	S += (T31*ADD[2])-1<T4T1_mem1*ADD_mem[2]
	S += (T31*ADD[3])-1<T4T1_mem1*ADD_mem[3]
	S += T4T1_mem1<=T4T1

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	T4T3 += alt(ADD)

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	T4T3_mem0 += alt(MUL_mem)
	S += (T30*MUL[0])-1<T4T3_mem0*MUL_mem[0]
	S += T4T3_mem0<=T4T3

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	T4T3_mem1 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T4T3_mem1*ADD_mem[0]
	S += (T31*ADD[1])-1<T4T3_mem1*ADD_mem[1]
	S += (T31*ADD[2])-1<T4T3_mem1*ADD_mem[2]
	S += (T31*ADD[3])-1<T4T3_mem1*ADD_mem[3]
	S += T4T3_mem1<=T4T3

	T5T0_in = S.Task('T5T0_in', length=1, delay_cost=1)
	T5T0_in += alt(MUL_in)
	T5T0 = S.Task('T5T0', length=7, delay_cost=1)
	T5T0 += alt(MUL)
	S+=T5T0>=T5T0_in

	T5T0_mem0 = S.Task('T5T0_mem0', length=1, delay_cost=1)
	T5T0_mem0 += INPUT_mem_r
	S += T5T0_mem0<=T5T0

	T5T0_mem1 = S.Task('T5T0_mem1', length=1, delay_cost=1)
	T5T0_mem1 += alt(MUL_mem)
	S += (T20*MUL[0])-1<T5T0_mem1*MUL_mem[0]
	S += T5T0_mem1<=T5T0

	T5T1_in = S.Task('T5T1_in', length=1, delay_cost=1)
	T5T1_in += alt(MUL_in)
	T5T1 = S.Task('T5T1', length=7, delay_cost=1)
	T5T1 += alt(MUL)
	S+=T5T1>=T5T1_in

	T5T1_mem0 = S.Task('T5T1_mem0', length=1, delay_cost=1)
	T5T1_mem0 += INPUT_mem_r
	S += T5T1_mem0<=T5T1

	T5T1_mem1 = S.Task('T5T1_mem1', length=1, delay_cost=1)
	T5T1_mem1 += alt(ADD_mem)
	S += (T21*ADD[0])-1<T5T1_mem1*ADD_mem[0]
	S += (T21*ADD[1])-1<T5T1_mem1*ADD_mem[1]
	S += (T21*ADD[2])-1<T5T1_mem1*ADD_mem[2]
	S += (T21*ADD[3])-1<T5T1_mem1*ADD_mem[3]
	S += T5T1_mem1<=T5T1

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	T5T3 += alt(ADD)

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	T5T3_mem0 += alt(MUL_mem)
	S += (T20*MUL[0])-1<T5T3_mem0*MUL_mem[0]
	S += T5T3_mem0<=T5T3

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	T5T3_mem1 += alt(ADD_mem)
	S += (T21*ADD[0])-1<T5T3_mem1*ADD_mem[0]
	S += (T21*ADD[1])-1<T5T3_mem1*ADD_mem[1]
	S += (T21*ADD[2])-1<T5T3_mem1*ADD_mem[2]
	S += (T21*ADD[3])-1<T5T3_mem1*ADD_mem[3]
	S += T5T3_mem1<=T5T3

	T3_T0_in = S.Task('T3_T0_in', length=1, delay_cost=1)
	T3_T0_in += alt(MUL_in)
	T3_T0 = S.Task('T3_T0', length=7, delay_cost=1)
	T3_T0 += alt(MUL)
	S+=T3_T0>=T3_T0_in

	T3_T0_mem0 = S.Task('T3_T0_mem0', length=1, delay_cost=1)
	T3_T0_mem0 += INPUT_mem_r
	S += T3_T0_mem0<=T3_T0

	T3_T0_mem1 = S.Task('T3_T0_mem1', length=1, delay_cost=1)
	T3_T0_mem1 += alt(MUL_mem)
	S += (T30*MUL[0])-1<T3_T0_mem1*MUL_mem[0]
	S += T3_T0_mem1<=T3_T0

	T3_T1_in = S.Task('T3_T1_in', length=1, delay_cost=1)
	T3_T1_in += alt(MUL_in)
	T3_T1 = S.Task('T3_T1', length=7, delay_cost=1)
	T3_T1 += alt(MUL)
	S+=T3_T1>=T3_T1_in

	T3_T1_mem0 = S.Task('T3_T1_mem0', length=1, delay_cost=1)
	T3_T1_mem0 += INPUT_mem_r
	S += T3_T1_mem0<=T3_T1

	T3_T1_mem1 = S.Task('T3_T1_mem1', length=1, delay_cost=1)
	T3_T1_mem1 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T3_T1_mem1*ADD_mem[0]
	S += (T31*ADD[1])-1<T3_T1_mem1*ADD_mem[1]
	S += (T31*ADD[2])-1<T3_T1_mem1*ADD_mem[2]
	S += (T31*ADD[3])-1<T3_T1_mem1*ADD_mem[3]
	S += T3_T1_mem1<=T3_T1

	T3_T3 = S.Task('T3_T3', length=1, delay_cost=1)
	T3_T3 += alt(ADD)

	T3_T3_mem0 = S.Task('T3_T3_mem0', length=1, delay_cost=1)
	T3_T3_mem0 += alt(MUL_mem)
	S += (T30*MUL[0])-1<T3_T3_mem0*MUL_mem[0]
	S += T3_T3_mem0<=T3_T3

	T3_T3_mem1 = S.Task('T3_T3_mem1', length=1, delay_cost=1)
	T3_T3_mem1 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T3_T3_mem1*ADD_mem[0]
	S += (T31*ADD[1])-1<T3_T3_mem1*ADD_mem[1]
	S += (T31*ADD[2])-1<T3_T3_mem1*ADD_mem[2]
	S += (T31*ADD[3])-1<T3_T3_mem1*ADD_mem[3]
	S += T3_T3_mem1<=T3_T3

	C001 = S.Task('C001', length=1, delay_cost=1)
	C001 += alt(ADD)

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	C001_mem0 += alt(MUL_mem)
	S += (C00T4*MUL[0])-1<C001_mem0*MUL_mem[0]
	S += C001_mem0<=C001

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	C001_mem1 += alt(ADD_mem)
	S += (C00T5*ADD[0])-1<C001_mem1*ADD_mem[0]
	S += (C00T5*ADD[1])-1<C001_mem1*ADD_mem[1]
	S += (C00T5*ADD[2])-1<C001_mem1*ADD_mem[2]
	S += (C00T5*ADD[3])-1<C001_mem1*ADD_mem[3]
	S += C001_mem1<=C001

	T0_11 = S.Task('T0_11', length=1, delay_cost=1)
	T0_11 += alt(ADD)

	T0_11_mem0 = S.Task('T0_11_mem0', length=1, delay_cost=1)
	T0_11_mem0 += alt(MUL_mem)
	S += (T0_1T4*MUL[0])-1<T0_11_mem0*MUL_mem[0]
	S += T0_11_mem0<=T0_11

	T0_11_mem1 = S.Task('T0_11_mem1', length=1, delay_cost=1)
	T0_11_mem1 += alt(ADD_mem)
	S += (T0_1T5*ADD[0])-1<T0_11_mem1*ADD_mem[0]
	S += (T0_1T5*ADD[1])-1<T0_11_mem1*ADD_mem[1]
	S += (T0_1T5*ADD[2])-1<T0_11_mem1*ADD_mem[2]
	S += (T0_1T5*ADD[3])-1<T0_11_mem1*ADD_mem[3]
	S += T0_11_mem1<=T0_11

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	T4T4_in += alt(MUL_in)
	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	T4T4 += alt(MUL)
	S+=T4T4>=T4T4_in

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	T4T4_mem0 += ADD_mem[3]
	S += 15<T4T4_mem0
	S += T4T4_mem0<=T4T4

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	T4T4_mem1 += alt(ADD_mem)
	S += (T4T3*ADD[0])-1<T4T4_mem1*ADD_mem[0]
	S += (T4T3*ADD[1])-1<T4T4_mem1*ADD_mem[1]
	S += (T4T3*ADD[2])-1<T4T4_mem1*ADD_mem[2]
	S += (T4T3*ADD[3])-1<T4T4_mem1*ADD_mem[3]
	S += T4T4_mem1<=T4T4

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	T4T5 += alt(ADD)

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	T4T5_mem0 += alt(MUL_mem)
	S += (T4T0*MUL[0])-1<T4T5_mem0*MUL_mem[0]
	S += T4T5_mem0<=T4T5

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	T4T5_mem1 += alt(MUL_mem)
	S += (T4T1*MUL[0])-1<T4T5_mem1*MUL_mem[0]
	S += T4T5_mem1<=T4T5

	T40 = S.Task('T40', length=1, delay_cost=1)
	T40 += alt(ADD)

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += alt(MUL_mem)
	S += (T4T0*MUL[0])-1<T40_mem0*MUL_mem[0]
	S += T40_mem0<=T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += alt(MUL_mem)
	S += (T4T1*MUL[0])-1<T40_mem1*MUL_mem[0]
	S += T40_mem1<=T40

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	T5T4_in += alt(MUL_in)
	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	T5T4 += alt(MUL)
	S+=T5T4>=T5T4_in

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	T5T4_mem0 += ADD_mem[2]
	S += 14<T5T4_mem0
	S += T5T4_mem0<=T5T4

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	T5T4_mem1 += alt(ADD_mem)
	S += (T5T3*ADD[0])-1<T5T4_mem1*ADD_mem[0]
	S += (T5T3*ADD[1])-1<T5T4_mem1*ADD_mem[1]
	S += (T5T3*ADD[2])-1<T5T4_mem1*ADD_mem[2]
	S += (T5T3*ADD[3])-1<T5T4_mem1*ADD_mem[3]
	S += T5T4_mem1<=T5T4

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	T5T5 += alt(ADD)

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	T5T5_mem0 += alt(MUL_mem)
	S += (T5T0*MUL[0])-1<T5T5_mem0*MUL_mem[0]
	S += T5T5_mem0<=T5T5

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	T5T5_mem1 += alt(MUL_mem)
	S += (T5T1*MUL[0])-1<T5T5_mem1*MUL_mem[0]
	S += T5T5_mem1<=T5T5

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(ADD)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += alt(MUL_mem)
	S += (T5T0*MUL[0])-1<T50_mem0*MUL_mem[0]
	S += T50_mem0<=T50

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	T50_mem1 += alt(MUL_mem)
	S += (T5T1*MUL[0])-1<T50_mem1*MUL_mem[0]
	S += T50_mem1<=T50

	T3_T4_in = S.Task('T3_T4_in', length=1, delay_cost=1)
	T3_T4_in += alt(MUL_in)
	T3_T4 = S.Task('T3_T4', length=7, delay_cost=1)
	T3_T4 += alt(MUL)
	S+=T3_T4>=T3_T4_in

	T3_T4_mem0 = S.Task('T3_T4_mem0', length=1, delay_cost=1)
	T3_T4_mem0 += ADD_mem[1]
	S += 10<T3_T4_mem0
	S += T3_T4_mem0<=T3_T4

	T3_T4_mem1 = S.Task('T3_T4_mem1', length=1, delay_cost=1)
	T3_T4_mem1 += alt(ADD_mem)
	S += (T3_T3*ADD[0])-1<T3_T4_mem1*ADD_mem[0]
	S += (T3_T3*ADD[1])-1<T3_T4_mem1*ADD_mem[1]
	S += (T3_T3*ADD[2])-1<T3_T4_mem1*ADD_mem[2]
	S += (T3_T3*ADD[3])-1<T3_T4_mem1*ADD_mem[3]
	S += T3_T4_mem1<=T3_T4

	T3_T5 = S.Task('T3_T5', length=1, delay_cost=1)
	T3_T5 += alt(ADD)

	T3_T5_mem0 = S.Task('T3_T5_mem0', length=1, delay_cost=1)
	T3_T5_mem0 += alt(MUL_mem)
	S += (T3_T0*MUL[0])-1<T3_T5_mem0*MUL_mem[0]
	S += T3_T5_mem0<=T3_T5

	T3_T5_mem1 = S.Task('T3_T5_mem1', length=1, delay_cost=1)
	T3_T5_mem1 += alt(MUL_mem)
	S += (T3_T1*MUL[0])-1<T3_T5_mem1*MUL_mem[0]
	S += T3_T5_mem1<=T3_T5

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	T3_0 += alt(ADD)

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	T3_0_mem0 += alt(MUL_mem)
	S += (T3_T0*MUL[0])-1<T3_0_mem0*MUL_mem[0]
	S += T3_0_mem0<=T3_0

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	T3_0_mem1 += alt(MUL_mem)
	S += (T3_T1*MUL[0])-1<T3_0_mem1*MUL_mem[0]
	S += T3_0_mem1<=T3_0

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += alt(MUL_mem)
	S += (T4T4*MUL[0])-1<T41_mem0*MUL_mem[0]
	S += T41_mem0<=T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += alt(ADD_mem)
	S += (T4T5*ADD[0])-1<T41_mem1*ADD_mem[0]
	S += (T4T5*ADD[1])-1<T41_mem1*ADD_mem[1]
	S += (T4T5*ADD[2])-1<T41_mem1*ADD_mem[2]
	S += (T4T5*ADD[3])-1<T41_mem1*ADD_mem[3]
	S += T41_mem1<=T41

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(ADD)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += alt(MUL_mem)
	S += (T5T4*MUL[0])-1<T51_mem0*MUL_mem[0]
	S += T51_mem0<=T51

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	T51_mem1 += alt(ADD_mem)
	S += (T5T5*ADD[0])-1<T51_mem1*ADD_mem[0]
	S += (T5T5*ADD[1])-1<T51_mem1*ADD_mem[1]
	S += (T5T5*ADD[2])-1<T51_mem1*ADD_mem[2]
	S += (T5T5*ADD[3])-1<T51_mem1*ADD_mem[3]
	S += T51_mem1<=T51

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	T5_0 += alt(ADD)

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	T5_0_mem0 += alt(ADD_mem)
	S += (T40*ADD[0])-1<T5_0_mem0*ADD_mem[0]
	S += (T40*ADD[1])-1<T5_0_mem0*ADD_mem[1]
	S += (T40*ADD[2])-1<T5_0_mem0*ADD_mem[2]
	S += (T40*ADD[3])-1<T5_0_mem0*ADD_mem[3]
	S += T5_0_mem0<=T5_0

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	T5_0_mem1 += alt(ADD_mem)
	S += (T50*ADD[0])-1<T5_0_mem1*ADD_mem[0]
	S += (T50*ADD[1])-1<T5_0_mem1*ADD_mem[1]
	S += (T50*ADD[2])-1<T5_0_mem1*ADD_mem[2]
	S += (T50*ADD[3])-1<T5_0_mem1*ADD_mem[3]
	S += T5_0_mem1<=T5_0

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	T3_1 += alt(ADD)

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	T3_1_mem0 += alt(MUL_mem)
	S += (T3_T4*MUL[0])-1<T3_1_mem0*MUL_mem[0]
	S += T3_1_mem0<=T3_1

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	T3_1_mem1 += alt(ADD_mem)
	S += (T3_T5*ADD[0])-1<T3_1_mem1*ADD_mem[0]
	S += (T3_T5*ADD[1])-1<T3_1_mem1*ADD_mem[1]
	S += (T3_T5*ADD[2])-1<T3_1_mem1*ADD_mem[2]
	S += (T3_T5*ADD[3])-1<T3_1_mem1*ADD_mem[3]
	S += T3_1_mem1<=T3_1

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += alt(ADD_mem)
	S += (T3_0*ADD[0])-1<T60_mem0*ADD_mem[0]
	S += (T3_0*ADD[1])-1<T60_mem0*ADD_mem[1]
	S += (T3_0*ADD[2])-1<T60_mem0*ADD_mem[2]
	S += (T3_0*ADD[3])-1<T60_mem0*ADD_mem[3]
	S += T60_mem0<=T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += alt(ADD_mem)
	S += (T3_0*ADD[0])-1<T60_mem1*ADD_mem[0]
	S += (T3_0*ADD[1])-1<T60_mem1*ADD_mem[1]
	S += (T3_0*ADD[2])-1<T60_mem1*ADD_mem[2]
	S += (T3_0*ADD[3])-1<T60_mem1*ADD_mem[3]
	S += T60_mem1<=T60

	T8T0_in = S.Task('T8T0_in', length=1, delay_cost=1)
	T8T0_in += alt(MUL_in)
	T8T0 = S.Task('T8T0', length=7, delay_cost=1)
	T8T0 += alt(MUL)
	S+=T8T0>=T8T0_in

	T8T0_mem0 = S.Task('T8T0_mem0', length=1, delay_cost=1)
	T8T0_mem0 += INPUT_mem_r
	S += T8T0_mem0<=T8T0

	T8T0_mem1 = S.Task('T8T0_mem1', length=1, delay_cost=1)
	T8T0_mem1 += alt(ADD_mem)
	S += (T40*ADD[0])-1<T8T0_mem1*ADD_mem[0]
	S += (T40*ADD[1])-1<T8T0_mem1*ADD_mem[1]
	S += (T40*ADD[2])-1<T8T0_mem1*ADD_mem[2]
	S += (T40*ADD[3])-1<T8T0_mem1*ADD_mem[3]
	S += T8T0_mem1<=T8T0

	NEW_TZT0_in = S.Task('NEW_TZT0_in', length=1, delay_cost=1)
	NEW_TZT0_in += alt(MUL_in)
	NEW_TZT0 = S.Task('NEW_TZT0', length=7, delay_cost=1)
	NEW_TZT0 += alt(MUL)
	S+=NEW_TZT0>=NEW_TZT0_in

	NEW_TZT0_mem0 = S.Task('NEW_TZT0_mem0', length=1, delay_cost=1)
	NEW_TZT0_mem0 += INPUT_mem_r
	S += NEW_TZT0_mem0<=NEW_TZT0

	NEW_TZT0_mem1 = S.Task('NEW_TZT0_mem1', length=1, delay_cost=1)
	NEW_TZT0_mem1 += alt(ADD_mem)
	S += (T40*ADD[0])-1<NEW_TZT0_mem1*ADD_mem[0]
	S += (T40*ADD[1])-1<NEW_TZT0_mem1*ADD_mem[1]
	S += (T40*ADD[2])-1<NEW_TZT0_mem1*ADD_mem[2]
	S += (T40*ADD[3])-1<NEW_TZT0_mem1*ADD_mem[3]
	S += NEW_TZT0_mem1<=NEW_TZT0

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	T5_1 += alt(ADD)

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	T5_1_mem0 += alt(ADD_mem)
	S += (T41*ADD[0])-1<T5_1_mem0*ADD_mem[0]
	S += (T41*ADD[1])-1<T5_1_mem0*ADD_mem[1]
	S += (T41*ADD[2])-1<T5_1_mem0*ADD_mem[2]
	S += (T41*ADD[3])-1<T5_1_mem0*ADD_mem[3]
	S += T5_1_mem0<=T5_1

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	T5_1_mem1 += alt(ADD_mem)
	S += (T51*ADD[0])-1<T5_1_mem1*ADD_mem[0]
	S += (T51*ADD[1])-1<T5_1_mem1*ADD_mem[1]
	S += (T51*ADD[2])-1<T5_1_mem1*ADD_mem[2]
	S += (T51*ADD[3])-1<T5_1_mem1*ADD_mem[3]
	S += T5_1_mem1<=T5_1

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += alt(ADD_mem)
	S += (T3_1*ADD[0])-1<T61_mem0*ADD_mem[0]
	S += (T3_1*ADD[1])-1<T61_mem0*ADD_mem[1]
	S += (T3_1*ADD[2])-1<T61_mem0*ADD_mem[2]
	S += (T3_1*ADD[3])-1<T61_mem0*ADD_mem[3]
	S += T61_mem0<=T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += alt(ADD_mem)
	S += (T3_1*ADD[0])-1<T61_mem1*ADD_mem[0]
	S += (T3_1*ADD[1])-1<T61_mem1*ADD_mem[1]
	S += (T3_1*ADD[2])-1<T61_mem1*ADD_mem[2]
	S += (T3_1*ADD[3])-1<T61_mem1*ADD_mem[3]
	S += T61_mem1<=T61

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	T5_10 += alt(ADD)

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	T5_10_mem0 += alt(ADD_mem)
	S += (T5_0*ADD[0])-1<T5_10_mem0*ADD_mem[0]
	S += (T5_0*ADD[1])-1<T5_10_mem0*ADD_mem[1]
	S += (T5_0*ADD[2])-1<T5_10_mem0*ADD_mem[2]
	S += (T5_0*ADD[3])-1<T5_10_mem0*ADD_mem[3]
	S += T5_10_mem0<=T5_10

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	T5_10_mem1 += alt(ADD_mem)
	S += (T60*ADD[0])-1<T5_10_mem1*ADD_mem[0]
	S += (T60*ADD[1])-1<T5_10_mem1*ADD_mem[1]
	S += (T60*ADD[2])-1<T5_10_mem1*ADD_mem[2]
	S += (T60*ADD[3])-1<T5_10_mem1*ADD_mem[3]
	S += T5_10_mem1<=T5_10

	T8T1_in = S.Task('T8T1_in', length=1, delay_cost=1)
	T8T1_in += alt(MUL_in)
	T8T1 = S.Task('T8T1', length=7, delay_cost=1)
	T8T1 += alt(MUL)
	S+=T8T1>=T8T1_in

	T8T1_mem0 = S.Task('T8T1_mem0', length=1, delay_cost=1)
	T8T1_mem0 += INPUT_mem_r
	S += T8T1_mem0<=T8T1

	T8T1_mem1 = S.Task('T8T1_mem1', length=1, delay_cost=1)
	T8T1_mem1 += alt(ADD_mem)
	S += (T41*ADD[0])-1<T8T1_mem1*ADD_mem[0]
	S += (T41*ADD[1])-1<T8T1_mem1*ADD_mem[1]
	S += (T41*ADD[2])-1<T8T1_mem1*ADD_mem[2]
	S += (T41*ADD[3])-1<T8T1_mem1*ADD_mem[3]
	S += T8T1_mem1<=T8T1

	T8T3 = S.Task('T8T3', length=1, delay_cost=1)
	T8T3 += alt(ADD)

	T8T3_mem0 = S.Task('T8T3_mem0', length=1, delay_cost=1)
	T8T3_mem0 += alt(ADD_mem)
	S += (T40*ADD[0])-1<T8T3_mem0*ADD_mem[0]
	S += (T40*ADD[1])-1<T8T3_mem0*ADD_mem[1]
	S += (T40*ADD[2])-1<T8T3_mem0*ADD_mem[2]
	S += (T40*ADD[3])-1<T8T3_mem0*ADD_mem[3]
	S += T8T3_mem0<=T8T3

	T8T3_mem1 = S.Task('T8T3_mem1', length=1, delay_cost=1)
	T8T3_mem1 += alt(ADD_mem)
	S += (T41*ADD[0])-1<T8T3_mem1*ADD_mem[0]
	S += (T41*ADD[1])-1<T8T3_mem1*ADD_mem[1]
	S += (T41*ADD[2])-1<T8T3_mem1*ADD_mem[2]
	S += (T41*ADD[3])-1<T8T3_mem1*ADD_mem[3]
	S += T8T3_mem1<=T8T3

	NEW_TZT1_in = S.Task('NEW_TZT1_in', length=1, delay_cost=1)
	NEW_TZT1_in += alt(MUL_in)
	NEW_TZT1 = S.Task('NEW_TZT1', length=7, delay_cost=1)
	NEW_TZT1 += alt(MUL)
	S+=NEW_TZT1>=NEW_TZT1_in

	NEW_TZT1_mem0 = S.Task('NEW_TZT1_mem0', length=1, delay_cost=1)
	NEW_TZT1_mem0 += INPUT_mem_r
	S += NEW_TZT1_mem0<=NEW_TZT1

	NEW_TZT1_mem1 = S.Task('NEW_TZT1_mem1', length=1, delay_cost=1)
	NEW_TZT1_mem1 += alt(ADD_mem)
	S += (T41*ADD[0])-1<NEW_TZT1_mem1*ADD_mem[0]
	S += (T41*ADD[1])-1<NEW_TZT1_mem1*ADD_mem[1]
	S += (T41*ADD[2])-1<NEW_TZT1_mem1*ADD_mem[2]
	S += (T41*ADD[3])-1<NEW_TZT1_mem1*ADD_mem[3]
	S += NEW_TZT1_mem1<=NEW_TZT1

	NEW_TZT3 = S.Task('NEW_TZT3', length=1, delay_cost=1)
	NEW_TZT3 += alt(ADD)

	NEW_TZT3_mem0 = S.Task('NEW_TZT3_mem0', length=1, delay_cost=1)
	NEW_TZT3_mem0 += alt(ADD_mem)
	S += (T40*ADD[0])-1<NEW_TZT3_mem0*ADD_mem[0]
	S += (T40*ADD[1])-1<NEW_TZT3_mem0*ADD_mem[1]
	S += (T40*ADD[2])-1<NEW_TZT3_mem0*ADD_mem[2]
	S += (T40*ADD[3])-1<NEW_TZT3_mem0*ADD_mem[3]
	S += NEW_TZT3_mem0<=NEW_TZT3

	NEW_TZT3_mem1 = S.Task('NEW_TZT3_mem1', length=1, delay_cost=1)
	NEW_TZT3_mem1 += alt(ADD_mem)
	S += (T41*ADD[0])-1<NEW_TZT3_mem1*ADD_mem[0]
	S += (T41*ADD[1])-1<NEW_TZT3_mem1*ADD_mem[1]
	S += (T41*ADD[2])-1<NEW_TZT3_mem1*ADD_mem[2]
	S += (T41*ADD[3])-1<NEW_TZT3_mem1*ADD_mem[3]
	S += NEW_TZT3_mem1<=NEW_TZT3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01, time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "padd_mul1_add4/padd_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_padd_mul1_add4_1(0, 0)