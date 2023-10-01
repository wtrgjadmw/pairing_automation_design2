from pyschedule import Scenario, solvers, plotters, alt

def solve_padd_mul1_add4_3(ConstStep, ExpStep):
	horizon = 148
	S=Scenario("padd_mul1_add4_3",horizon = horizon)

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

	C00T3_mem0 = S.Task('C00T3_mem0', length=1, delay_cost=1)
	S += C00T3_mem0 >= 13
	C00T3_mem0 += ADD_mem[3]

	C00T3_mem1 = S.Task('C00T3_mem1', length=1, delay_cost=1)
	S += C00T3_mem1 >= 13
	C00T3_mem1 += ADD_mem[1]

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

	C00T3 = S.Task('C00T3', length=1, delay_cost=1)
	S += C00T3 >= 14
	C00T3 += ADD[3]

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

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 19
	T30_in += MUL_in[0]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 19
	T30_mem0 += ADD_mem[3]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 19
	T30_mem1 += ADD_mem[1]

	T7_T2_mem0 = S.Task('T7_T2_mem0', length=1, delay_cost=1)
	S += T7_T2_mem0 >= 19
	T7_T2_mem0 += ADD_mem[2]

	T7_T2_mem1 = S.Task('T7_T2_mem1', length=1, delay_cost=1)
	S += T7_T2_mem1 >= 19
	T7_T2_mem1 += ADD_mem[0]

	T0_1T3 = S.Task('T0_1T3', length=1, delay_cost=1)
	S += T0_1T3 >= 20
	T0_1T3 += ADD[0]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 20
	T20_in += MUL_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 20
	T20_mem0 += ADD_mem[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 20
	T20_mem1 += ADD_mem[0]

	T30 = S.Task('T30', length=7, delay_cost=1)
	S += T30 >= 20
	T30 += MUL[0]

	T7_T2 = S.Task('T7_T2', length=1, delay_cost=1)
	S += T7_T2 >= 20
	T7_T2 += ADD[3]

	C00T5_mem0 = S.Task('C00T5_mem0', length=1, delay_cost=1)
	S += C00T5_mem0 >= 21
	C00T5_mem0 += MUL_mem[0]

	C00T5_mem1 = S.Task('C00T5_mem1', length=1, delay_cost=1)
	S += C00T5_mem1 >= 21
	C00T5_mem1 += MUL_mem[0]

	T0_1T4_in = S.Task('T0_1T4_in', length=1, delay_cost=1)
	S += T0_1T4_in >= 21
	T0_1T4_in += MUL_in[0]

	T0_1T4_mem0 = S.Task('T0_1T4_mem0', length=1, delay_cost=1)
	S += T0_1T4_mem0 >= 21
	T0_1T4_mem0 += ADD_mem[2]

	T0_1T4_mem1 = S.Task('T0_1T4_mem1', length=1, delay_cost=1)
	S += T0_1T4_mem1 >= 21
	T0_1T4_mem1 += ADD_mem[0]

	T20 = S.Task('T20', length=7, delay_cost=1)
	S += T20 >= 21
	T20 += MUL[0]

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	S += C000_mem0 >= 22
	C000_mem0 += MUL_mem[0]

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	S += C000_mem1 >= 22
	C000_mem1 += MUL_mem[0]

	C00T4_in = S.Task('C00T4_in', length=1, delay_cost=1)
	S += C00T4_in >= 22
	C00T4_in += MUL_in[0]

	C00T4_mem0 = S.Task('C00T4_mem0', length=1, delay_cost=1)
	S += C00T4_mem0 >= 22
	C00T4_mem0 += ADD_mem[3]

	C00T4_mem1 = S.Task('C00T4_mem1', length=1, delay_cost=1)
	S += C00T4_mem1 >= 22
	C00T4_mem1 += ADD_mem[3]

	C00T5 = S.Task('C00T5', length=1, delay_cost=1)
	S += C00T5 >= 22
	C00T5 += ADD[0]

	T0_1T4 = S.Task('T0_1T4', length=7, delay_cost=1)
	S += T0_1T4 >= 22
	T0_1T4 += MUL[0]

	C000 = S.Task('C000', length=1, delay_cost=1)
	S += C000 >= 23
	C000 += ADD[2]

	C00T4 = S.Task('C00T4', length=7, delay_cost=1)
	S += C00T4 >= 23
	C00T4 += MUL[0]

	T4T1_in = S.Task('T4T1_in', length=1, delay_cost=1)
	S += T4T1_in >= 23
	T4T1_in += MUL_in[0]

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	S += T4T1_mem0 >= 23
	T4T1_mem0 += ADD_mem[1]

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	S += T4T1_mem1 >= 23
	T4T1_mem1 += ADD_mem[2]

	T3_T1_in = S.Task('T3_T1_in', length=1, delay_cost=1)
	S += T3_T1_in >= 24
	T3_T1_in += MUL_in[0]

	T3_T1_mem0 = S.Task('T3_T1_mem0', length=1, delay_cost=1)
	S += T3_T1_mem0 >= 24
	T3_T1_mem0 += INPUT_mem_r

	T3_T1_mem1 = S.Task('T3_T1_mem1', length=1, delay_cost=1)
	S += T3_T1_mem1 >= 24
	T3_T1_mem1 += ADD_mem[2]

	T4T1 = S.Task('T4T1', length=7, delay_cost=1)
	S += T4T1 >= 24
	T4T1 += MUL[0]

	T0_1T5_mem0 = S.Task('T0_1T5_mem0', length=1, delay_cost=1)
	S += T0_1T5_mem0 >= 25
	T0_1T5_mem0 += MUL_mem[0]

	T0_1T5_mem1 = S.Task('T0_1T5_mem1', length=1, delay_cost=1)
	S += T0_1T5_mem1 >= 25
	T0_1T5_mem1 += MUL_mem[0]

	T3_T1 = S.Task('T3_T1', length=7, delay_cost=1)
	S += T3_T1 >= 25
	T3_T1 += MUL[0]

	T5T1_in = S.Task('T5T1_in', length=1, delay_cost=1)
	S += T5T1_in >= 25
	T5T1_in += MUL_in[0]

	T5T1_mem0 = S.Task('T5T1_mem0', length=1, delay_cost=1)
	S += T5T1_mem0 >= 25
	T5T1_mem0 += INPUT_mem_r

	T5T1_mem1 = S.Task('T5T1_mem1', length=1, delay_cost=1)
	S += T5T1_mem1 >= 25
	T5T1_mem1 += ADD_mem[2]

	T0_1T5 = S.Task('T0_1T5', length=1, delay_cost=1)
	S += T0_1T5 >= 26
	T0_1T5 += ADD[1]

	T3_T3_mem0 = S.Task('T3_T3_mem0', length=1, delay_cost=1)
	S += T3_T3_mem0 >= 26
	T3_T3_mem0 += MUL_mem[0]

	T3_T3_mem1 = S.Task('T3_T3_mem1', length=1, delay_cost=1)
	S += T3_T3_mem1 >= 26
	T3_T3_mem1 += ADD_mem[2]

	T4T0_in = S.Task('T4T0_in', length=1, delay_cost=1)
	S += T4T0_in >= 26
	T4T0_in += MUL_in[0]

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	S += T4T0_mem0 >= 26
	T4T0_mem0 += ADD_mem[3]

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	S += T4T0_mem1 >= 26
	T4T0_mem1 += MUL_mem[0]

	T5T1 = S.Task('T5T1', length=7, delay_cost=1)
	S += T5T1 >= 26
	T5T1 += MUL[0]

	T3_T3 = S.Task('T3_T3', length=1, delay_cost=1)
	S += T3_T3 >= 27
	T3_T3 += ADD[0]

	T3_T4_in = S.Task('T3_T4_in', length=1, delay_cost=1)
	S += T3_T4_in >= 27
	T3_T4_in += MUL_in[0]

	T3_T4_mem0 = S.Task('T3_T4_mem0', length=1, delay_cost=1)
	S += T3_T4_mem0 >= 27
	T3_T4_mem0 += ADD_mem[1]

	T3_T4_mem1 = S.Task('T3_T4_mem1', length=1, delay_cost=1)
	S += T3_T4_mem1 >= 27
	T3_T4_mem1 += ADD_mem[0]

	T4T0 = S.Task('T4T0', length=7, delay_cost=1)
	S += T4T0 >= 27
	T4T0 += MUL[0]

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	S += T4T3_mem0 >= 27
	T4T3_mem0 += MUL_mem[0]

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	S += T4T3_mem1 >= 27
	T4T3_mem1 += ADD_mem[2]

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	S += T5T3_mem0 >= 27
	T5T3_mem0 += MUL_mem[0]

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	S += T5T3_mem1 >= 27
	T5T3_mem1 += ADD_mem[2]

	T0_11_mem0 = S.Task('T0_11_mem0', length=1, delay_cost=1)
	S += T0_11_mem0 >= 28
	T0_11_mem0 += MUL_mem[0]

	T0_11_mem1 = S.Task('T0_11_mem1', length=1, delay_cost=1)
	S += T0_11_mem1 >= 28
	T0_11_mem1 += ADD_mem[1]

	T3_T0_in = S.Task('T3_T0_in', length=1, delay_cost=1)
	S += T3_T0_in >= 28
	T3_T0_in += MUL_in[0]

	T3_T0_mem0 = S.Task('T3_T0_mem0', length=1, delay_cost=1)
	S += T3_T0_mem0 >= 28
	T3_T0_mem0 += INPUT_mem_r

	T3_T0_mem1 = S.Task('T3_T0_mem1', length=1, delay_cost=1)
	S += T3_T0_mem1 >= 28
	T3_T0_mem1 += MUL_mem[0]

	T3_T4 = S.Task('T3_T4', length=7, delay_cost=1)
	S += T3_T4 >= 28
	T3_T4 += MUL[0]

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	S += T4T3 >= 28
	T4T3 += ADD[2]

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	S += T5T3 >= 28
	T5T3 += ADD[0]

	T0_10_mem0 = S.Task('T0_10_mem0', length=1, delay_cost=1)
	S += T0_10_mem0 >= 29
	T0_10_mem0 += MUL_mem[0]

	T0_10_mem1 = S.Task('T0_10_mem1', length=1, delay_cost=1)
	S += T0_10_mem1 >= 29
	T0_10_mem1 += MUL_mem[0]

	T0_11 = S.Task('T0_11', length=1, delay_cost=1)
	S += T0_11 >= 29
	T0_11 += ADD[1]

	T3_T0 = S.Task('T3_T0', length=7, delay_cost=1)
	S += T3_T0 >= 29
	T3_T0 += MUL[0]

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	S += T4T4_in >= 29
	T4T4_in += MUL_in[0]

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	S += T4T4_mem0 >= 29
	T4T4_mem0 += ADD_mem[3]

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	S += T4T4_mem1 >= 29
	T4T4_mem1 += ADD_mem[2]

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	S += C001_mem0 >= 30
	C001_mem0 += MUL_mem[0]

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	S += C001_mem1 >= 30
	C001_mem1 += ADD_mem[0]

	C00_0_mem0 = S.Task('C00_0_mem0', length=1, delay_cost=1)
	S += C00_0_mem0 >= 30
	C00_0_mem0 += ADD_mem[2]

	C00_0_mem1 = S.Task('C00_0_mem1', length=1, delay_cost=1)
	S += C00_0_mem1 >= 30
	C00_0_mem1 += ADD_mem[1]

	T0_10 = S.Task('T0_10', length=1, delay_cost=1)
	S += T0_10 >= 30
	T0_10 += ADD[1]

	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	S += T4T4 >= 30
	T4T4 += MUL[0]

	T5T0_in = S.Task('T5T0_in', length=1, delay_cost=1)
	S += T5T0_in >= 30
	T5T0_in += MUL_in[0]

	T5T0_mem0 = S.Task('T5T0_mem0', length=1, delay_cost=1)
	S += T5T0_mem0 >= 30
	T5T0_mem0 += INPUT_mem_r

	T5T0_mem1 = S.Task('T5T0_mem1', length=1, delay_cost=1)
	S += T5T0_mem1 >= 30
	T5T0_mem1 += MUL_mem[0]

	C001 = S.Task('C001', length=1, delay_cost=1)
	S += C001 >= 31
	C001 += ADD[2]

	C00_0 = S.Task('C00_0', length=1, delay_cost=1)
	S += C00_0 >= 31
	C00_0 += ADD[0]

	C00_0_w = S.Task('C00_0_w', length=1, delay_cost=1)
	S += C00_0_w >= 31
	C00_0_w += INPUT_mem_w

	C00_1_mem0 = S.Task('C00_1_mem0', length=1, delay_cost=1)
	S += C00_1_mem0 >= 31
	C00_1_mem0 += ADD_mem[2]

	C00_1_mem1 = S.Task('C00_1_mem1', length=1, delay_cost=1)
	S += C00_1_mem1 >= 31
	C00_1_mem1 += ADD_mem[1]

	T5T0 = S.Task('T5T0', length=7, delay_cost=1)
	S += T5T0 >= 31
	T5T0 += MUL[0]

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	S += T5T4_in >= 31
	T5T4_in += MUL_in[0]

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	S += T5T4_mem0 >= 31
	T5T4_mem0 += ADD_mem[2]

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	S += T5T4_mem1 >= 31
	T5T4_mem1 += ADD_mem[0]

	C010_in = S.Task('C010_in', length=1, delay_cost=1)
	S += C010_in >= 32
	C010_in += MUL_in[0]

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	S += C010_mem0 >= 32
	C010_mem0 += ADD_mem[3]

	C010_mem1 = S.Task('C010_mem1', length=1, delay_cost=1)
	S += C010_mem1 >= 32
	C010_mem1 += INPUT_mem_r

	C00_1 = S.Task('C00_1', length=1, delay_cost=1)
	S += C00_1 >= 32
	C00_1 += ADD[0]

	C00_1_w = S.Task('C00_1_w', length=1, delay_cost=1)
	S += C00_1_w >= 32
	C00_1_w += INPUT_mem_w

	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	S += T5T4 >= 32
	T5T4 += MUL[0]

	C010 = S.Task('C010', length=7, delay_cost=1)
	S += C010 >= 33
	C010 += MUL[0]

	C201_in = S.Task('C201_in', length=1, delay_cost=1)
	S += C201_in >= 33
	C201_in += MUL_in[0]

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	S += C201_mem0 >= 33
	C201_mem0 += ADD_mem[0]

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	S += C201_mem1 >= 33
	C201_mem1 += INPUT_mem_r

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 33
	T40_mem0 += MUL_mem[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 33
	T40_mem1 += MUL_mem[0]

	C201 = S.Task('C201', length=7, delay_cost=1)
	S += C201 >= 34
	C201 += MUL[0]

	NEW_TZT0_in = S.Task('NEW_TZT0_in', length=1, delay_cost=1)
	S += NEW_TZT0_in >= 34
	NEW_TZT0_in += MUL_in[0]

	NEW_TZT0_mem0 = S.Task('NEW_TZT0_mem0', length=1, delay_cost=1)
	S += NEW_TZT0_mem0 >= 34
	NEW_TZT0_mem0 += INPUT_mem_r

	NEW_TZT0_mem1 = S.Task('NEW_TZT0_mem1', length=1, delay_cost=1)
	S += NEW_TZT0_mem1 >= 34
	NEW_TZT0_mem1 += ADD_mem[1]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 34
	T40 += ADD[1]

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	S += T4T5_mem0 >= 34
	T4T5_mem0 += MUL_mem[0]

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	S += T4T5_mem1 >= 34
	T4T5_mem1 += MUL_mem[0]

	NEW_TZT0 = S.Task('NEW_TZT0', length=7, delay_cost=1)
	S += NEW_TZT0 >= 35
	NEW_TZT0 += MUL[0]

	T3_T5_mem0 = S.Task('T3_T5_mem0', length=1, delay_cost=1)
	S += T3_T5_mem0 >= 35
	T3_T5_mem0 += MUL_mem[0]

	T3_T5_mem1 = S.Task('T3_T5_mem1', length=1, delay_cost=1)
	S += T3_T5_mem1 >= 35
	T3_T5_mem1 += MUL_mem[0]

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	S += T4T5 >= 35
	T4T5 += ADD[3]

	T8T0_in = S.Task('T8T0_in', length=1, delay_cost=1)
	S += T8T0_in >= 35
	T8T0_in += MUL_in[0]

	T8T0_mem0 = S.Task('T8T0_mem0', length=1, delay_cost=1)
	S += T8T0_mem0 >= 35
	T8T0_mem0 += INPUT_mem_r

	T8T0_mem1 = S.Task('T8T0_mem1', length=1, delay_cost=1)
	S += T8T0_mem1 >= 35
	T8T0_mem1 += ADD_mem[1]

	C200_in = S.Task('C200_in', length=1, delay_cost=1)
	S += C200_in >= 36
	C200_in += MUL_in[0]

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	S += C200_mem0 >= 36
	C200_mem0 += ADD_mem[2]

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	S += C200_mem1 >= 36
	C200_mem1 += INPUT_mem_r

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	S += T3_1_mem0 >= 36
	T3_1_mem0 += MUL_mem[0]

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	S += T3_1_mem1 >= 36
	T3_1_mem1 += ADD_mem[3]

	T3_T5 = S.Task('T3_T5', length=1, delay_cost=1)
	S += T3_T5 >= 36
	T3_T5 += ADD[3]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 36
	T41_mem0 += MUL_mem[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 36
	T41_mem1 += ADD_mem[3]

	T8T0 = S.Task('T8T0', length=7, delay_cost=1)
	S += T8T0 >= 36
	T8T0 += MUL[0]

	C200 = S.Task('C200', length=7, delay_cost=1)
	S += C200 >= 37
	C200 += MUL[0]

	NEW_TZT1_in = S.Task('NEW_TZT1_in', length=1, delay_cost=1)
	S += NEW_TZT1_in >= 37
	NEW_TZT1_in += MUL_in[0]

	NEW_TZT1_mem0 = S.Task('NEW_TZT1_mem0', length=1, delay_cost=1)
	S += NEW_TZT1_mem0 >= 37
	NEW_TZT1_mem0 += INPUT_mem_r

	NEW_TZT1_mem1 = S.Task('NEW_TZT1_mem1', length=1, delay_cost=1)
	S += NEW_TZT1_mem1 >= 37
	NEW_TZT1_mem1 += ADD_mem[3]

	NEW_TZT3_mem0 = S.Task('NEW_TZT3_mem0', length=1, delay_cost=1)
	S += NEW_TZT3_mem0 >= 37
	NEW_TZT3_mem0 += ADD_mem[1]

	NEW_TZT3_mem1 = S.Task('NEW_TZT3_mem1', length=1, delay_cost=1)
	S += NEW_TZT3_mem1 >= 37
	NEW_TZT3_mem1 += ADD_mem[3]

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 37
	T3_1 += ADD[2]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 37
	T41 += ADD[3]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 37
	T50_mem0 += MUL_mem[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 37
	T50_mem1 += MUL_mem[0]

	NEW_TZT1 = S.Task('NEW_TZT1', length=7, delay_cost=1)
	S += NEW_TZT1 >= 38
	NEW_TZT1 += MUL[0]

	NEW_TZT3 = S.Task('NEW_TZT3', length=1, delay_cost=1)
	S += NEW_TZT3 >= 38
	NEW_TZT3 += ADD[3]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 38
	T3_0_mem0 += MUL_mem[0]

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 38
	T3_0_mem1 += MUL_mem[0]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 38
	T50 += ADD[0]

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	S += T5_0_mem0 >= 38
	T5_0_mem0 += ADD_mem[1]

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	S += T5_0_mem1 >= 38
	T5_0_mem1 += ADD_mem[0]

	T8T1_in = S.Task('T8T1_in', length=1, delay_cost=1)
	S += T8T1_in >= 38
	T8T1_in += MUL_in[0]

	T8T1_mem0 = S.Task('T8T1_mem0', length=1, delay_cost=1)
	S += T8T1_mem0 >= 38
	T8T1_mem0 += INPUT_mem_r

	T8T1_mem1 = S.Task('T8T1_mem1', length=1, delay_cost=1)
	S += T8T1_mem1 >= 38
	T8T1_mem1 += ADD_mem[3]

	T8T3_mem0 = S.Task('T8T3_mem0', length=1, delay_cost=1)
	S += T8T3_mem0 >= 38
	T8T3_mem0 += ADD_mem[1]

	T8T3_mem1 = S.Task('T8T3_mem1', length=1, delay_cost=1)
	S += T8T3_mem1 >= 38
	T8T3_mem1 += ADD_mem[3]

	C010_w = S.Task('C010_w', length=1, delay_cost=1)
	S += C010_w >= 39
	C010_w += INPUT_mem_w

	C011_in = S.Task('C011_in', length=1, delay_cost=1)
	S += C011_in >= 39
	C011_in += MUL_in[0]

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	S += C011_mem0 >= 39
	C011_mem0 += ADD_mem[1]

	C011_mem1 = S.Task('C011_mem1', length=1, delay_cost=1)
	S += C011_mem1 >= 39
	C011_mem1 += INPUT_mem_r

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 39
	T3_0 += ADD[3]

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	S += T5T5_mem0 >= 39
	T5T5_mem0 += MUL_mem[0]

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	S += T5T5_mem1 >= 39
	T5T5_mem1 += MUL_mem[0]

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	S += T5_0 >= 39
	T5_0 += ADD[0]

	T8T1 = S.Task('T8T1', length=7, delay_cost=1)
	S += T8T1 >= 39
	T8T1 += MUL[0]

	T8T3 = S.Task('T8T3', length=1, delay_cost=1)
	S += T8T3 >= 39
	T8T3 += ADD[2]

	C011 = S.Task('C011', length=7, delay_cost=1)
	S += C011 >= 40
	C011 += MUL[0]

	C201_w = S.Task('C201_w', length=1, delay_cost=1)
	S += C201_w >= 40
	C201_w += INPUT_mem_w

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 40
	T51_mem0 += MUL_mem[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 40
	T51_mem1 += ADD_mem[0]

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	S += T5T5 >= 40
	T5T5 += ADD[0]

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	S += T5_10_mem0 >= 40
	T5_10_mem0 += ADD_mem[0]

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	S += T5_10_mem1 >= 40
	T5_10_mem1 += ADD_mem[1]

	T8T4_in = S.Task('T8T4_in', length=1, delay_cost=1)
	S += T8T4_in >= 40
	T8T4_in += MUL_in[0]

	T8T4_mem0 = S.Task('T8T4_mem0', length=1, delay_cost=1)
	S += T8T4_mem0 >= 40
	T8T4_mem0 += ADD_mem[3]

	T8T4_mem1 = S.Task('T8T4_mem1', length=1, delay_cost=1)
	S += T8T4_mem1 >= 40
	T8T4_mem1 += ADD_mem[2]

	NEW_TZT4_in = S.Task('NEW_TZT4_in', length=1, delay_cost=1)
	S += NEW_TZT4_in >= 41
	NEW_TZT4_in += MUL_in[0]

	NEW_TZT4_mem0 = S.Task('NEW_TZT4_mem0', length=1, delay_cost=1)
	S += NEW_TZT4_mem0 >= 41
	NEW_TZT4_mem0 += ADD_mem[0]

	NEW_TZT4_mem1 = S.Task('NEW_TZT4_mem1', length=1, delay_cost=1)
	S += NEW_TZT4_mem1 >= 41
	NEW_TZT4_mem1 += ADD_mem[3]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 41
	T51 += ADD[1]

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	S += T5_10 >= 41
	T5_10 += ADD[0]

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	S += T5_1_mem0 >= 41
	T5_1_mem0 += ADD_mem[3]

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	S += T5_1_mem1 >= 41
	T5_1_mem1 += ADD_mem[1]

	T8T4 = S.Task('T8T4', length=7, delay_cost=1)
	S += T8T4 >= 41
	T8T4 += MUL[0]

	NEW_TXT0_in = S.Task('NEW_TXT0_in', length=1, delay_cost=1)
	S += NEW_TXT0_in >= 42
	NEW_TXT0_in += MUL_in[0]

	NEW_TXT0_mem0 = S.Task('NEW_TXT0_mem0', length=1, delay_cost=1)
	S += NEW_TXT0_mem0 >= 42
	NEW_TXT0_mem0 += ADD_mem[3]

	NEW_TXT0_mem1 = S.Task('NEW_TXT0_mem1', length=1, delay_cost=1)
	S += NEW_TXT0_mem1 >= 42
	NEW_TXT0_mem1 += ADD_mem[0]

	NEW_TZT4 = S.Task('NEW_TZT4', length=7, delay_cost=1)
	S += NEW_TZT4 >= 42
	NEW_TZT4 += MUL[0]

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	S += T5_1 >= 42
	T5_1 += ADD[1]

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	S += T5_11_mem0 >= 42
	T5_11_mem0 += ADD_mem[1]

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	S += T5_11_mem1 >= 42
	T5_11_mem1 += ADD_mem[1]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 42
	T70_mem0 += ADD_mem[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 42
	T70_mem1 += ADD_mem[3]

	C200_w = S.Task('C200_w', length=1, delay_cost=1)
	S += C200_w >= 43
	C200_w += INPUT_mem_w

	NEW_TXT0 = S.Task('NEW_TXT0', length=7, delay_cost=1)
	S += NEW_TXT0 >= 43
	NEW_TXT0 += MUL[0]

	NEW_TXT1_in = S.Task('NEW_TXT1_in', length=1, delay_cost=1)
	S += NEW_TXT1_in >= 43
	NEW_TXT1_in += MUL_in[0]

	NEW_TXT1_mem0 = S.Task('NEW_TXT1_mem0', length=1, delay_cost=1)
	S += NEW_TXT1_mem0 >= 43
	NEW_TXT1_mem0 += ADD_mem[1]

	NEW_TXT1_mem1 = S.Task('NEW_TXT1_mem1', length=1, delay_cost=1)
	S += NEW_TXT1_mem1 >= 43
	NEW_TXT1_mem1 += ADD_mem[3]

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	S += T5_11 >= 43
	T5_11 += ADD[3]

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 43
	T70 += ADD[1]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 43
	T71_mem0 += ADD_mem[3]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 43
	T71_mem1 += ADD_mem[2]

	NEW_TXT1 = S.Task('NEW_TXT1', length=7, delay_cost=1)
	S += NEW_TXT1 >= 44
	NEW_TXT1 += MUL[0]

	NEW_TXT3_mem0 = S.Task('NEW_TXT3_mem0', length=1, delay_cost=1)
	S += NEW_TXT3_mem0 >= 44
	NEW_TXT3_mem0 += ADD_mem[0]

	NEW_TXT3_mem1 = S.Task('NEW_TXT3_mem1', length=1, delay_cost=1)
	S += NEW_TXT3_mem1 >= 44
	NEW_TXT3_mem1 += ADD_mem[3]

	NEW_TZ0_mem0 = S.Task('NEW_TZ0_mem0', length=1, delay_cost=1)
	S += NEW_TZ0_mem0 >= 44
	NEW_TZ0_mem0 += MUL_mem[0]

	NEW_TZ0_mem1 = S.Task('NEW_TZ0_mem1', length=1, delay_cost=1)
	S += NEW_TZ0_mem1 >= 44
	NEW_TZ0_mem1 += MUL_mem[0]

	T71 = S.Task('T71', length=1, delay_cost=1)
	S += T71 >= 44
	T71 += ADD[2]

	T7_T1_in = S.Task('T7_T1_in', length=1, delay_cost=1)
	S += T7_T1_in >= 44
	T7_T1_in += MUL_in[0]

	T7_T1_mem0 = S.Task('T7_T1_mem0', length=1, delay_cost=1)
	S += T7_T1_mem0 >= 44
	T7_T1_mem0 += ADD_mem[0]

	T7_T1_mem1 = S.Task('T7_T1_mem1', length=1, delay_cost=1)
	S += T7_T1_mem1 >= 44
	T7_T1_mem1 += ADD_mem[2]

	T7_T3_mem0 = S.Task('T7_T3_mem0', length=1, delay_cost=1)
	S += T7_T3_mem0 >= 44
	T7_T3_mem0 += ADD_mem[1]

	T7_T3_mem1 = S.Task('T7_T3_mem1', length=1, delay_cost=1)
	S += T7_T3_mem1 >= 44
	T7_T3_mem1 += ADD_mem[2]

	NEW_TXT3 = S.Task('NEW_TXT3', length=1, delay_cost=1)
	S += NEW_TXT3 >= 45
	NEW_TXT3 += ADD[0]

	NEW_TZ0 = S.Task('NEW_TZ0', length=1, delay_cost=1)
	S += NEW_TZ0 >= 45
	NEW_TZ0 += ADD[1]

	NEW_TZ0_w = S.Task('NEW_TZ0_w', length=1, delay_cost=1)
	S += NEW_TZ0_w >= 45
	NEW_TZ0_w += INPUT_mem_w

	NEW_TZT5_mem0 = S.Task('NEW_TZT5_mem0', length=1, delay_cost=1)
	S += NEW_TZT5_mem0 >= 45
	NEW_TZT5_mem0 += MUL_mem[0]

	NEW_TZT5_mem1 = S.Task('NEW_TZT5_mem1', length=1, delay_cost=1)
	S += NEW_TZT5_mem1 >= 45
	NEW_TZT5_mem1 += MUL_mem[0]

	T7_T0_in = S.Task('T7_T0_in', length=1, delay_cost=1)
	S += T7_T0_in >= 45
	T7_T0_in += MUL_in[0]

	T7_T0_mem0 = S.Task('T7_T0_mem0', length=1, delay_cost=1)
	S += T7_T0_mem0 >= 45
	T7_T0_mem0 += ADD_mem[2]

	T7_T0_mem1 = S.Task('T7_T0_mem1', length=1, delay_cost=1)
	S += T7_T0_mem1 >= 45
	T7_T0_mem1 += ADD_mem[1]

	T7_T1 = S.Task('T7_T1', length=7, delay_cost=1)
	S += T7_T1 >= 45
	T7_T1 += MUL[0]

	T7_T3 = S.Task('T7_T3', length=1, delay_cost=1)
	S += T7_T3 >= 45
	T7_T3 += ADD[3]

	C011_w = S.Task('C011_w', length=1, delay_cost=1)
	S += C011_w >= 46
	C011_w += INPUT_mem_w

	NEW_TXT4_in = S.Task('NEW_TXT4_in', length=1, delay_cost=1)
	S += NEW_TXT4_in >= 46
	NEW_TXT4_in += MUL_in[0]

	NEW_TXT4_mem0 = S.Task('NEW_TXT4_mem0', length=1, delay_cost=1)
	S += NEW_TXT4_mem0 >= 46
	NEW_TXT4_mem0 += ADD_mem[0]

	NEW_TXT4_mem1 = S.Task('NEW_TXT4_mem1', length=1, delay_cost=1)
	S += NEW_TXT4_mem1 >= 46
	NEW_TXT4_mem1 += ADD_mem[0]

	NEW_TZT5 = S.Task('NEW_TZT5', length=1, delay_cost=1)
	S += NEW_TZT5 >= 46
	NEW_TZT5 += ADD[0]

	T7_T0 = S.Task('T7_T0', length=7, delay_cost=1)
	S += T7_T0 >= 46
	T7_T0 += MUL[0]

	T8T5_mem0 = S.Task('T8T5_mem0', length=1, delay_cost=1)
	S += T8T5_mem0 >= 46
	T8T5_mem0 += MUL_mem[0]

	T8T5_mem1 = S.Task('T8T5_mem1', length=1, delay_cost=1)
	S += T8T5_mem1 >= 46
	T8T5_mem1 += MUL_mem[0]

	NEW_TXT4 = S.Task('NEW_TXT4', length=7, delay_cost=1)
	S += NEW_TXT4 >= 47
	NEW_TXT4 += MUL[0]

	T7_T4_in = S.Task('T7_T4_in', length=1, delay_cost=1)
	S += T7_T4_in >= 47
	T7_T4_in += MUL_in[0]

	T7_T4_mem0 = S.Task('T7_T4_mem0', length=1, delay_cost=1)
	S += T7_T4_mem0 >= 47
	T7_T4_mem0 += ADD_mem[3]

	T7_T4_mem1 = S.Task('T7_T4_mem1', length=1, delay_cost=1)
	S += T7_T4_mem1 >= 47
	T7_T4_mem1 += ADD_mem[3]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 47
	T80_mem0 += MUL_mem[0]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 47
	T80_mem1 += MUL_mem[0]

	T8T5 = S.Task('T8T5', length=1, delay_cost=1)
	S += T8T5 >= 47
	T8T5 += ADD[0]

	NEW_TZ1_mem0 = S.Task('NEW_TZ1_mem0', length=1, delay_cost=1)
	S += NEW_TZ1_mem0 >= 48
	NEW_TZ1_mem0 += MUL_mem[0]

	NEW_TZ1_mem1 = S.Task('NEW_TZ1_mem1', length=1, delay_cost=1)
	S += NEW_TZ1_mem1 >= 48
	NEW_TZ1_mem1 += ADD_mem[0]

	T7_T4 = S.Task('T7_T4', length=7, delay_cost=1)
	S += T7_T4 >= 48
	T7_T4 += MUL[0]

	T80 = S.Task('T80', length=1, delay_cost=1)
	S += T80 >= 48
	T80 += ADD[1]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 48
	T81_mem0 += MUL_mem[0]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 48
	T81_mem1 += ADD_mem[0]

	NEW_TZ1 = S.Task('NEW_TZ1', length=1, delay_cost=1)
	S += NEW_TZ1 >= 49
	NEW_TZ1 += ADD[0]

	NEW_TZ1_w = S.Task('NEW_TZ1_w', length=1, delay_cost=1)
	S += NEW_TZ1_w >= 49
	NEW_TZ1_w += INPUT_mem_w

	T81 = S.Task('T81', length=1, delay_cost=1)
	S += T81 >= 49
	T81 += ADD[2]

	NEW_TX0_mem0 = S.Task('NEW_TX0_mem0', length=1, delay_cost=1)
	S += NEW_TX0_mem0 >= 50
	NEW_TX0_mem0 += MUL_mem[0]

	NEW_TX0_mem1 = S.Task('NEW_TX0_mem1', length=1, delay_cost=1)
	S += NEW_TX0_mem1 >= 50
	NEW_TX0_mem1 += MUL_mem[0]

	NEW_TX0 = S.Task('NEW_TX0', length=1, delay_cost=1)
	S += NEW_TX0 >= 51
	NEW_TX0 += ADD[1]

	NEW_TX0_w = S.Task('NEW_TX0_w', length=1, delay_cost=1)
	S += NEW_TX0_w >= 51
	NEW_TX0_w += INPUT_mem_w

	NEW_TXT5_mem0 = S.Task('NEW_TXT5_mem0', length=1, delay_cost=1)
	S += NEW_TXT5_mem0 >= 51
	NEW_TXT5_mem0 += MUL_mem[0]

	NEW_TXT5_mem1 = S.Task('NEW_TXT5_mem1', length=1, delay_cost=1)
	S += NEW_TXT5_mem1 >= 51
	NEW_TXT5_mem1 += MUL_mem[0]

	NEW_TXT5 = S.Task('NEW_TXT5', length=1, delay_cost=1)
	S += NEW_TXT5 >= 52
	NEW_TXT5 += ADD[3]

	T7_0_mem0 = S.Task('T7_0_mem0', length=1, delay_cost=1)
	S += T7_0_mem0 >= 52
	T7_0_mem0 += MUL_mem[0]

	T7_0_mem1 = S.Task('T7_0_mem1', length=1, delay_cost=1)
	S += T7_0_mem1 >= 52
	T7_0_mem1 += MUL_mem[0]

	NEW_TY0_mem0 = S.Task('NEW_TY0_mem0', length=1, delay_cost=1)
	S += NEW_TY0_mem0 >= 53
	NEW_TY0_mem0 += ADD_mem[0]

	NEW_TY0_mem1 = S.Task('NEW_TY0_mem1', length=1, delay_cost=1)
	S += NEW_TY0_mem1 >= 53
	NEW_TY0_mem1 += ADD_mem[1]

	T7_0 = S.Task('T7_0', length=1, delay_cost=1)
	S += T7_0 >= 53
	T7_0 += ADD[0]

	T7_T5_mem0 = S.Task('T7_T5_mem0', length=1, delay_cost=1)
	S += T7_T5_mem0 >= 53
	T7_T5_mem0 += MUL_mem[0]

	T7_T5_mem1 = S.Task('T7_T5_mem1', length=1, delay_cost=1)
	S += T7_T5_mem1 >= 53
	T7_T5_mem1 += MUL_mem[0]

	NEW_TX1_mem0 = S.Task('NEW_TX1_mem0', length=1, delay_cost=1)
	S += NEW_TX1_mem0 >= 54
	NEW_TX1_mem0 += MUL_mem[0]

	NEW_TX1_mem1 = S.Task('NEW_TX1_mem1', length=1, delay_cost=1)
	S += NEW_TX1_mem1 >= 54
	NEW_TX1_mem1 += ADD_mem[3]

	NEW_TY0 = S.Task('NEW_TY0', length=1, delay_cost=1)
	S += NEW_TY0 >= 54
	NEW_TY0 += ADD[1]

	NEW_TY_0_mem0 = S.Task('NEW_TY_0_mem0', length=1, delay_cost=1)
	S += NEW_TY_0_mem0 >= 54
	NEW_TY_0_mem0 += INPUT_mem_r

	NEW_TY_0_mem1 = S.Task('NEW_TY_0_mem1', length=1, delay_cost=1)
	S += NEW_TY_0_mem1 >= 54
	NEW_TY_0_mem1 += ADD_mem[1]

	T7_1_mem0 = S.Task('T7_1_mem0', length=1, delay_cost=1)
	S += T7_1_mem0 >= 54
	T7_1_mem0 += MUL_mem[0]

	T7_1_mem1 = S.Task('T7_1_mem1', length=1, delay_cost=1)
	S += T7_1_mem1 >= 54
	T7_1_mem1 += ADD_mem[0]

	T7_T5 = S.Task('T7_T5', length=1, delay_cost=1)
	S += T7_T5 >= 54
	T7_T5 += ADD[0]

	NEW_TX1 = S.Task('NEW_TX1', length=1, delay_cost=1)
	S += NEW_TX1 >= 55
	NEW_TX1 += ADD[3]

	NEW_TX1_w = S.Task('NEW_TX1_w', length=1, delay_cost=1)
	S += NEW_TX1_w >= 55
	NEW_TX1_w += INPUT_mem_w

	NEW_TY1_mem0 = S.Task('NEW_TY1_mem0', length=1, delay_cost=1)
	S += NEW_TY1_mem0 >= 55
	NEW_TY1_mem0 += ADD_mem[1]

	NEW_TY1_mem1 = S.Task('NEW_TY1_mem1', length=1, delay_cost=1)
	S += NEW_TY1_mem1 >= 55
	NEW_TY1_mem1 += ADD_mem[2]

	NEW_TY_0 = S.Task('NEW_TY_0', length=1, delay_cost=1)
	S += NEW_TY_0 >= 55
	NEW_TY_0 += ADD[2]

	NEW_TY_0_w = S.Task('NEW_TY_0_w', length=1, delay_cost=1)
	S += NEW_TY_0_w >= 55
	NEW_TY_0_w += INPUT_mem_w

	T7_1 = S.Task('T7_1', length=1, delay_cost=1)
	S += T7_1 >= 55
	T7_1 += ADD[1]

	NEW_TY1 = S.Task('NEW_TY1', length=1, delay_cost=1)
	S += NEW_TY1 >= 56
	NEW_TY1 += ADD[3]

	NEW_TY_1_mem0 = S.Task('NEW_TY_1_mem0', length=1, delay_cost=1)
	S += NEW_TY_1_mem0 >= 56
	NEW_TY_1_mem0 += INPUT_mem_r

	NEW_TY_1_mem1 = S.Task('NEW_TY_1_mem1', length=1, delay_cost=1)
	S += NEW_TY_1_mem1 >= 56
	NEW_TY_1_mem1 += ADD_mem[3]

	NEW_TY_1 = S.Task('NEW_TY_1', length=1, delay_cost=1)
	S += NEW_TY_1 >= 57
	NEW_TY_1 += ADD[1]

	NEW_TY_1_w = S.Task('NEW_TY_1_w', length=1, delay_cost=1)
	S += NEW_TY_1_w >= 57
	NEW_TY_1_w += INPUT_mem_w


	# new tasks
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

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += ADD_mem[3]
	S += 39<T60_mem0
	S += T60_mem0<=T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += ADD_mem[3]
	S += 39<T60_mem1
	S += T60_mem1<=T60

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += ADD_mem[2]
	S += 37<T61_mem0
	S += T61_mem0<=T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += ADD_mem[2]
	S += 37<T61_mem1
	S += T61_mem1<=T61

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01, time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "padd_mul1_add4/padd_mul1_add4_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_padd_mul1_add4_3(0, 0)