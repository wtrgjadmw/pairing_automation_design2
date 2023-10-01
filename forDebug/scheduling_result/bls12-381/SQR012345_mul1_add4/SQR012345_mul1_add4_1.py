from pyschedule import Scenario, solvers, plotters, alt

def solve_SQR012345_mul1_add4_1(ConstStep, ExpStep):
	horizon = 117
	S=Scenario("SQR012345_mul1_add4_1",horizon = horizon)

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
	T6T1_in = S.Task('T6T1_in', length=1, delay_cost=1)
	S += T6T1_in >= 0
	T6T1_in += MUL_in[0]

	T6T1_mem0 = S.Task('T6T1_mem0', length=1, delay_cost=1)
	S += T6T1_mem0 >= 0
	T6T1_mem0 += INPUT_mem_r

	T6T1_mem1 = S.Task('T6T1_mem1', length=1, delay_cost=1)
	S += T6T1_mem1 >= 0
	T6T1_mem1 += INPUT_mem_r

	T6T0_in = S.Task('T6T0_in', length=1, delay_cost=1)
	S += T6T0_in >= 1
	T6T0_in += MUL_in[0]

	T6T0_mem0 = S.Task('T6T0_mem0', length=1, delay_cost=1)
	S += T6T0_mem0 >= 1
	T6T0_mem0 += INPUT_mem_r

	T6T0_mem1 = S.Task('T6T0_mem1', length=1, delay_cost=1)
	S += T6T0_mem1 >= 1
	T6T0_mem1 += INPUT_mem_r

	T6T1 = S.Task('T6T1', length=7, delay_cost=1)
	S += T6T1 >= 1
	T6T1 += MUL[0]

	T6T0 = S.Task('T6T0', length=7, delay_cost=1)
	S += T6T0 >= 2
	T6T0 += MUL[0]

	T7T1_in = S.Task('T7T1_in', length=1, delay_cost=1)
	S += T7T1_in >= 2
	T7T1_in += MUL_in[0]

	T7T1_mem0 = S.Task('T7T1_mem0', length=1, delay_cost=1)
	S += T7T1_mem0 >= 2
	T7T1_mem0 += INPUT_mem_r

	T7T1_mem1 = S.Task('T7T1_mem1', length=1, delay_cost=1)
	S += T7T1_mem1 >= 2
	T7T1_mem1 += INPUT_mem_r

	T7T0_in = S.Task('T7T0_in', length=1, delay_cost=1)
	S += T7T0_in >= 3
	T7T0_in += MUL_in[0]

	T7T0_mem0 = S.Task('T7T0_mem0', length=1, delay_cost=1)
	S += T7T0_mem0 >= 3
	T7T0_mem0 += INPUT_mem_r

	T7T0_mem1 = S.Task('T7T0_mem1', length=1, delay_cost=1)
	S += T7T0_mem1 >= 3
	T7T0_mem1 += INPUT_mem_r

	T7T1 = S.Task('T7T1', length=7, delay_cost=1)
	S += T7T1 >= 3
	T7T1 += MUL[0]

	T5T0_in = S.Task('T5T0_in', length=1, delay_cost=1)
	S += T5T0_in >= 4
	T5T0_in += MUL_in[0]

	T5T0_mem0 = S.Task('T5T0_mem0', length=1, delay_cost=1)
	S += T5T0_mem0 >= 4
	T5T0_mem0 += INPUT_mem_r

	T5T0_mem1 = S.Task('T5T0_mem1', length=1, delay_cost=1)
	S += T5T0_mem1 >= 4
	T5T0_mem1 += INPUT_mem_r

	T7T0 = S.Task('T7T0', length=7, delay_cost=1)
	S += T7T0 >= 4
	T7T0 += MUL[0]

	T5T0 = S.Task('T5T0', length=7, delay_cost=1)
	S += T5T0 >= 5
	T5T0 += MUL[0]

	T5T1_in = S.Task('T5T1_in', length=1, delay_cost=1)
	S += T5T1_in >= 5
	T5T1_in += MUL_in[0]

	T5T1_mem0 = S.Task('T5T1_mem0', length=1, delay_cost=1)
	S += T5T1_mem0 >= 5
	T5T1_mem0 += INPUT_mem_r

	T5T1_mem1 = S.Task('T5T1_mem1', length=1, delay_cost=1)
	S += T5T1_mem1 >= 5
	T5T1_mem1 += INPUT_mem_r

	T3T1_in = S.Task('T3T1_in', length=1, delay_cost=1)
	S += T3T1_in >= 6
	T3T1_in += MUL_in[0]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 6
	T3T1_mem0 += INPUT_mem_r

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 6
	T3T1_mem1 += INPUT_mem_r

	T5T1 = S.Task('T5T1', length=7, delay_cost=1)
	S += T5T1 >= 6
	T5T1 += MUL[0]

	T3T0_in = S.Task('T3T0_in', length=1, delay_cost=1)
	S += T3T0_in >= 7
	T3T0_in += MUL_in[0]

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 7
	T3T0_mem0 += INPUT_mem_r

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 7
	T3T0_mem1 += INPUT_mem_r

	T3T1 = S.Task('T3T1', length=7, delay_cost=1)
	S += T3T1 >= 7
	T3T1 += MUL[0]

	T0T2_in = S.Task('T0T2_in', length=1, delay_cost=1)
	S += T0T2_in >= 8
	T0T2_in += MUL_in[0]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 8
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 8
	T0T2_mem1 += INPUT_mem_r

	T3T0 = S.Task('T3T0', length=7, delay_cost=1)
	S += T3T0 >= 8
	T3T0 += MUL[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 8
	T60_mem0 += MUL_mem[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 8
	T60_mem1 += MUL_mem[0]

	T0T2 = S.Task('T0T2', length=7, delay_cost=1)
	S += T0T2 >= 9
	T0T2 += MUL[0]

	T4T2_in = S.Task('T4T2_in', length=1, delay_cost=1)
	S += T4T2_in >= 9
	T4T2_in += MUL_in[0]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 9
	T4T2_mem0 += INPUT_mem_r

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 9
	T4T2_mem1 += INPUT_mem_r

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 9
	T60 += ADD[1]

	T6T5_mem0 = S.Task('T6T5_mem0', length=1, delay_cost=1)
	S += T6T5_mem0 >= 9
	T6T5_mem0 += MUL_mem[0]

	T6T5_mem1 = S.Task('T6T5_mem1', length=1, delay_cost=1)
	S += T6T5_mem1 >= 9
	T6T5_mem1 += MUL_mem[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 10
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 10
	T0T0_mem1 += INPUT_mem_r

	T4T2 = S.Task('T4T2', length=7, delay_cost=1)
	S += T4T2 >= 10
	T4T2 += MUL[0]

	T6T5 = S.Task('T6T5', length=1, delay_cost=1)
	S += T6T5 >= 10
	T6T5 += ADD[1]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 10
	T70_mem0 += MUL_mem[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 10
	T70_mem1 += MUL_mem[0]

	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	S += T0T0 >= 11
	T0T0 += ADD[3]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 11
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 11
	T0T1_mem1 += INPUT_mem_r

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 11
	T70 += ADD[2]

	T7T5_mem0 = S.Task('T7T5_mem0', length=1, delay_cost=1)
	S += T7T5_mem0 >= 11
	T7T5_mem0 += MUL_mem[0]

	T7T5_mem1 = S.Task('T7T5_mem1', length=1, delay_cost=1)
	S += T7T5_mem1 >= 11
	T7T5_mem1 += MUL_mem[0]

	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	S += T00_in >= 12
	T00_in += MUL_in[0]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 12
	T00_mem0 += ADD_mem[3]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 12
	T00_mem1 += ADD_mem[3]

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	S += T0T1 >= 12
	T0T1 += ADD[3]

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	S += T5T5_mem0 >= 12
	T5T5_mem0 += MUL_mem[0]

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	S += T5T5_mem1 >= 12
	T5T5_mem1 += MUL_mem[0]

	T6T2_mem0 = S.Task('T6T2_mem0', length=1, delay_cost=1)
	S += T6T2_mem0 >= 12
	T6T2_mem0 += INPUT_mem_r

	T6T2_mem1 = S.Task('T6T2_mem1', length=1, delay_cost=1)
	S += T6T2_mem1 >= 12
	T6T2_mem1 += INPUT_mem_r

	T7T5 = S.Task('T7T5', length=1, delay_cost=1)
	S += T7T5 >= 12
	T7T5 += ADD[2]

	T00 = S.Task('T00', length=7, delay_cost=1)
	S += T00 >= 13
	T00 += MUL[0]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 13
	T50_mem0 += MUL_mem[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 13
	T50_mem1 += MUL_mem[0]

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	S += T5T5 >= 13
	T5T5 += ADD[1]

	T6T2 = S.Task('T6T2', length=1, delay_cost=1)
	S += T6T2 >= 13
	T6T2 += ADD[2]

	T6T3_mem0 = S.Task('T6T3_mem0', length=1, delay_cost=1)
	S += T6T3_mem0 >= 13
	T6T3_mem0 += INPUT_mem_r

	T6T3_mem1 = S.Task('T6T3_mem1', length=1, delay_cost=1)
	S += T6T3_mem1 >= 13
	T6T3_mem1 += INPUT_mem_r

	T3T3_mem0 = S.Task('T3T3_mem0', length=1, delay_cost=1)
	S += T3T3_mem0 >= 14
	T3T3_mem0 += INPUT_mem_r

	T3T3_mem1 = S.Task('T3T3_mem1', length=1, delay_cost=1)
	S += T3T3_mem1 >= 14
	T3T3_mem1 += INPUT_mem_r

	T3T5_mem0 = S.Task('T3T5_mem0', length=1, delay_cost=1)
	S += T3T5_mem0 >= 14
	T3T5_mem0 += MUL_mem[0]

	T3T5_mem1 = S.Task('T3T5_mem1', length=1, delay_cost=1)
	S += T3T5_mem1 >= 14
	T3T5_mem1 += MUL_mem[0]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 14
	T50 += ADD[1]

	T6T3 = S.Task('T6T3', length=1, delay_cost=1)
	S += T6T3 >= 14
	T6T3 += ADD[3]

	T6T4_in = S.Task('T6T4_in', length=1, delay_cost=1)
	S += T6T4_in >= 14
	T6T4_in += MUL_in[0]

	T6T4_mem0 = S.Task('T6T4_mem0', length=1, delay_cost=1)
	S += T6T4_mem0 >= 14
	T6T4_mem0 += ADD_mem[2]

	T6T4_mem1 = S.Task('T6T4_mem1', length=1, delay_cost=1)
	S += T6T4_mem1 >= 14
	T6T4_mem1 += ADD_mem[3]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 15
	T30_mem0 += MUL_mem[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 15
	T30_mem1 += MUL_mem[0]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 15
	T3T2_mem0 += INPUT_mem_r

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 15
	T3T2_mem1 += INPUT_mem_r

	T3T3 = S.Task('T3T3', length=1, delay_cost=1)
	S += T3T3 >= 15
	T3T3 += ADD[1]

	T3T5 = S.Task('T3T5', length=1, delay_cost=1)
	S += T3T5 >= 15
	T3T5 += ADD[0]

	T6T4 = S.Task('T6T4', length=7, delay_cost=1)
	S += T6T4 >= 15
	T6T4 += MUL[0]

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 16
	T01_mem0 += MUL_mem[0]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 16
	T30 += ADD[3]

	T3T2 = S.Task('T3T2', length=1, delay_cost=1)
	S += T3T2 >= 16
	T3T2 += ADD[1]

	T3T4_in = S.Task('T3T4_in', length=1, delay_cost=1)
	S += T3T4_in >= 16
	T3T4_in += MUL_in[0]

	T3T4_mem0 = S.Task('T3T4_mem0', length=1, delay_cost=1)
	S += T3T4_mem0 >= 16
	T3T4_mem0 += ADD_mem[1]

	T3T4_mem1 = S.Task('T3T4_mem1', length=1, delay_cost=1)
	S += T3T4_mem1 >= 16
	T3T4_mem1 += ADD_mem[1]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 16
	T41_mem0 += MUL_mem[0]

	T7T3_mem0 = S.Task('T7T3_mem0', length=1, delay_cost=1)
	S += T7T3_mem0 >= 16
	T7T3_mem0 += INPUT_mem_r

	T7T3_mem1 = S.Task('T7T3_mem1', length=1, delay_cost=1)
	S += T7T3_mem1 >= 16
	T7T3_mem1 += INPUT_mem_r

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 17
	T01 += ADD[1]

	T3T4 = S.Task('T3T4', length=7, delay_cost=1)
	S += T3T4 >= 17
	T3T4 += MUL[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 17
	T41 += ADD[2]

	T7T2_mem0 = S.Task('T7T2_mem0', length=1, delay_cost=1)
	S += T7T2_mem0 >= 17
	T7T2_mem0 += INPUT_mem_r

	T7T2_mem1 = S.Task('T7T2_mem1', length=1, delay_cost=1)
	S += T7T2_mem1 >= 17
	T7T2_mem1 += INPUT_mem_r

	T7T3 = S.Task('T7T3', length=1, delay_cost=1)
	S += T7T3 >= 17
	T7T3 += ADD[0]

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	S += T4T0_mem0 >= 18
	T4T0_mem0 += INPUT_mem_r

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	S += T4T0_mem1 >= 18
	T4T0_mem1 += INPUT_mem_r

	T7T2 = S.Task('T7T2', length=1, delay_cost=1)
	S += T7T2 >= 18
	T7T2 += ADD[0]

	T7T4_in = S.Task('T7T4_in', length=1, delay_cost=1)
	S += T7T4_in >= 18
	T7T4_in += MUL_in[0]

	T7T4_mem0 = S.Task('T7T4_mem0', length=1, delay_cost=1)
	S += T7T4_mem0 >= 18
	T7T4_mem0 += ADD_mem[0]

	T7T4_mem1 = S.Task('T7T4_mem1', length=1, delay_cost=1)
	S += T7T4_mem1 >= 18
	T7T4_mem1 += ADD_mem[0]

	T4T0 = S.Task('T4T0', length=1, delay_cost=1)
	S += T4T0 >= 19
	T4T0 += ADD[2]

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	S += T4T1_mem0 >= 19
	T4T1_mem0 += INPUT_mem_r

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	S += T4T1_mem1 >= 19
	T4T1_mem1 += INPUT_mem_r

	T7T4 = S.Task('T7T4', length=7, delay_cost=1)
	S += T7T4 >= 19
	T7T4 += MUL[0]

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	S += T40_in >= 20
	T40_in += MUL_in[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 20
	T40_mem0 += ADD_mem[2]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 20
	T40_mem1 += ADD_mem[0]

	T4T1 = S.Task('T4T1', length=1, delay_cost=1)
	S += T4T1 >= 20
	T4T1 += ADD[0]

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	S += T5T3_mem0 >= 20
	T5T3_mem0 += INPUT_mem_r

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	S += T5T3_mem1 >= 20
	T5T3_mem1 += INPUT_mem_r

	T40 = S.Task('T40', length=7, delay_cost=1)
	S += T40 >= 21
	T40 += MUL[0]

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	S += T5T2_mem0 >= 21
	T5T2_mem0 += INPUT_mem_r

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	S += T5T2_mem1 >= 21
	T5T2_mem1 += INPUT_mem_r

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	S += T5T3 >= 21
	T5T3 += ADD[1]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 22
	T11_mem0 += INPUT_mem_r

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 22
	T11_mem1 += INPUT_mem_r

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	S += T5T2 >= 22
	T5T2 += ADD[3]

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	S += T5T4_in >= 22
	T5T4_in += MUL_in[0]

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	S += T5T4_mem0 >= 22
	T5T4_mem0 += ADD_mem[3]

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	S += T5T4_mem1 >= 22
	T5T4_mem1 += ADD_mem[1]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 23
	T11 += ADD[3]

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 23
	T1_1_mem0 += ADD_mem[3]

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	S += T1_1_mem1 >= 23
	T1_1_mem1 += INPUT_mem_r

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 23
	T21_mem0 += ADD_mem[3]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 23
	T21_mem1 += INPUT_mem_r

	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	S += T5T4 >= 23
	T5T4 += MUL[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 24
	T10_mem0 += INPUT_mem_r

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 24
	T10_mem1 += INPUT_mem_r

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 24
	T1_1 += ADD[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 24
	T21 += ADD[2]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 25
	T10 += ADD[2]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 25
	T1_0_mem0 += ADD_mem[2]

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 25
	T1_0_mem1 += INPUT_mem_r

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 25
	T20_mem0 += ADD_mem[2]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 25
	T20_mem1 += INPUT_mem_r

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	S += T1_0 >= 26
	T1_0 += ADD[0]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 26
	T20 += ADD[1]


	# new tasks
	T1_1T0 = S.Task('T1_1T0', length=1, delay_cost=1)
	T1_1T0 += alt(ADD)

	T1_1T0_mem0 = S.Task('T1_1T0_mem0', length=1, delay_cost=1)
	T1_1T0_mem0 += ADD_mem[0]
	S += 26<T1_1T0_mem0
	S += T1_1T0_mem0<=T1_1T0

	T1_1T0_mem1 = S.Task('T1_1T0_mem1', length=1, delay_cost=1)
	T1_1T0_mem1 += ADD_mem[0]
	S += 24<T1_1T0_mem1
	S += T1_1T0_mem1<=T1_1T0

	T1_1T1 = S.Task('T1_1T1', length=1, delay_cost=1)
	T1_1T1 += alt(ADD)

	T1_1T1_mem0 = S.Task('T1_1T1_mem0', length=1, delay_cost=1)
	T1_1T1_mem0 += ADD_mem[0]
	S += 26<T1_1T1_mem0
	S += T1_1T1_mem0<=T1_1T1

	T1_1T1_mem1 = S.Task('T1_1T1_mem1', length=1, delay_cost=1)
	T1_1T1_mem1 += ADD_mem[0]
	S += 24<T1_1T1_mem1
	S += T1_1T1_mem1<=T1_1T1

	T1_1T2_in = S.Task('T1_1T2_in', length=1, delay_cost=1)
	T1_1T2_in += alt(MUL_in)
	T1_1T2 = S.Task('T1_1T2', length=7, delay_cost=1)
	T1_1T2 += alt(MUL)
	S+=T1_1T2>=T1_1T2_in

	T1_1T2_mem0 = S.Task('T1_1T2_mem0', length=1, delay_cost=1)
	T1_1T2_mem0 += ADD_mem[0]
	S += 26<T1_1T2_mem0
	S += T1_1T2_mem0<=T1_1T2

	T1_1T2_mem1 = S.Task('T1_1T2_mem1', length=1, delay_cost=1)
	T1_1T2_mem1 += ADD_mem[0]
	S += 24<T1_1T2_mem1
	S += T1_1T2_mem1<=T1_1T2

	T2_T0 = S.Task('T2_T0', length=1, delay_cost=1)
	T2_T0 += alt(ADD)

	T2_T0_mem0 = S.Task('T2_T0_mem0', length=1, delay_cost=1)
	T2_T0_mem0 += ADD_mem[1]
	S += 26<T2_T0_mem0
	S += T2_T0_mem0<=T2_T0

	T2_T0_mem1 = S.Task('T2_T0_mem1', length=1, delay_cost=1)
	T2_T0_mem1 += ADD_mem[2]
	S += 24<T2_T0_mem1
	S += T2_T0_mem1<=T2_T0

	T2_T1 = S.Task('T2_T1', length=1, delay_cost=1)
	T2_T1 += alt(ADD)

	T2_T1_mem0 = S.Task('T2_T1_mem0', length=1, delay_cost=1)
	T2_T1_mem0 += ADD_mem[1]
	S += 26<T2_T1_mem0
	S += T2_T1_mem0<=T2_T1

	T2_T1_mem1 = S.Task('T2_T1_mem1', length=1, delay_cost=1)
	T2_T1_mem1 += ADD_mem[2]
	S += 24<T2_T1_mem1
	S += T2_T1_mem1<=T2_T1

	T2_T2_in = S.Task('T2_T2_in', length=1, delay_cost=1)
	T2_T2_in += alt(MUL_in)
	T2_T2 = S.Task('T2_T2', length=7, delay_cost=1)
	T2_T2 += alt(MUL)
	S+=T2_T2>=T2_T2_in

	T2_T2_mem0 = S.Task('T2_T2_mem0', length=1, delay_cost=1)
	T2_T2_mem0 += ADD_mem[1]
	S += 26<T2_T2_mem0
	S += T2_T2_mem0<=T2_T2

	T2_T2_mem1 = S.Task('T2_T2_mem1', length=1, delay_cost=1)
	T2_T2_mem1 += ADD_mem[2]
	S += 24<T2_T2_mem1
	S += T2_T2_mem1<=T2_T2

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += MUL_mem[0]
	S += 23<T31_mem0
	S += T31_mem0<=T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += ADD_mem[0]
	S += 15<T31_mem1
	S += T31_mem1<=T31

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	T3_0 += alt(ADD)

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	T3_0_mem0 += ADD_mem[3]
	S += 16<T3_0_mem0
	S += T3_0_mem0<=T3_0

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(ADD)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += MUL_mem[0]
	S += 29<T51_mem0
	S += T51_mem0<=T51

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	T51_mem1 += ADD_mem[1]
	S += 13<T51_mem1
	S += T51_mem1<=T51

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += MUL_mem[0]
	S += 21<T61_mem0
	S += T61_mem0<=T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += ADD_mem[1]
	S += 10<T61_mem1
	S += T61_mem1<=T61

	T71 = S.Task('T71', length=1, delay_cost=1)
	T71 += alt(ADD)

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	T71_mem0 += MUL_mem[0]
	S += 25<T71_mem0
	S += T71_mem0<=T71

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	T71_mem1 += ADD_mem[2]
	S += 12<T71_mem1
	S += T71_mem1<=T71

	C010 = S.Task('C010', length=1, delay_cost=1)
	C010 += alt(ADD)

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	C010_mem0 += ADD_mem[1]
	S += 14<C010_mem0
	S += C010_mem0<=C010

	C100 = S.Task('C100', length=1, delay_cost=1)
	C100 += alt(ADD)

	C100_mem0 = S.Task('C100_mem0', length=1, delay_cost=1)
	C100_mem0 += ADD_mem[1]
	S += 9<C100_mem0
	S += C100_mem0<=C100

	C110 = S.Task('C110', length=1, delay_cost=1)
	C110 += alt(ADD)

	C110_mem0 = S.Task('C110_mem0', length=1, delay_cost=1)
	C110_mem0 += MUL_mem[0]
	S += 19<C110_mem0
	S += C110_mem0<=C110

	C110_mem1 = S.Task('C110_mem1', length=1, delay_cost=1)
	C110_mem1 += MUL_mem[0]
	S += 27<C110_mem1
	S += C110_mem1<=C110

	C111 = S.Task('C111', length=1, delay_cost=1)
	C111 += alt(ADD)

	C111_mem0 = S.Task('C111_mem0', length=1, delay_cost=1)
	C111_mem0 += ADD_mem[1]
	S += 17<C111_mem0
	S += C111_mem0<=C111

	C111_mem1 = S.Task('C111_mem1', length=1, delay_cost=1)
	C111_mem1 += ADD_mem[2]
	S += 17<C111_mem1
	S += C111_mem1<=C111

	C200 = S.Task('C200', length=1, delay_cost=1)
	C200 += alt(ADD)

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	C200_mem0 += MUL_mem[0]
	S += 27<C200_mem0
	S += C200_mem0<=C200

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	C200_mem1 += ADD_mem[2]
	S += 17<C200_mem1
	S += C200_mem1<=C200

	C201 = S.Task('C201', length=1, delay_cost=1)
	C201 += alt(ADD)

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	C201_mem0 += MUL_mem[0]
	S += 27<C201_mem0
	S += C201_mem0<=C201

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	C201_mem1 += ADD_mem[2]
	S += 17<C201_mem1
	S += C201_mem1<=C201

	C210 = S.Task('C210', length=1, delay_cost=1)
	C210 += alt(ADD)

	C210_mem0 = S.Task('C210_mem0', length=1, delay_cost=1)
	C210_mem0 += ADD_mem[2]
	S += 11<C210_mem0
	S += C210_mem0<=C210

	T1_10_in = S.Task('T1_10_in', length=1, delay_cost=1)
	T1_10_in += alt(MUL_in)
	T1_10 = S.Task('T1_10', length=7, delay_cost=1)
	T1_10 += alt(MUL)
	S+=T1_10>=T1_10_in

	T1_10_mem0 = S.Task('T1_10_mem0', length=1, delay_cost=1)
	T1_10_mem0 += alt(ADD_mem)
	S += (T1_1T0*ADD[0])-1<T1_10_mem0*ADD_mem[0]
	S += (T1_1T0*ADD[1])-1<T1_10_mem0*ADD_mem[1]
	S += (T1_1T0*ADD[2])-1<T1_10_mem0*ADD_mem[2]
	S += (T1_1T0*ADD[3])-1<T1_10_mem0*ADD_mem[3]
	S += T1_10_mem0<=T1_10

	T1_10_mem1 = S.Task('T1_10_mem1', length=1, delay_cost=1)
	T1_10_mem1 += alt(ADD_mem)
	S += (T1_1T1*ADD[0])-1<T1_10_mem1*ADD_mem[0]
	S += (T1_1T1*ADD[1])-1<T1_10_mem1*ADD_mem[1]
	S += (T1_1T1*ADD[2])-1<T1_10_mem1*ADD_mem[2]
	S += (T1_1T1*ADD[3])-1<T1_10_mem1*ADD_mem[3]
	S += T1_10_mem1<=T1_10

	T1_11 = S.Task('T1_11', length=1, delay_cost=1)
	T1_11 += alt(ADD)

	T1_11_mem0 = S.Task('T1_11_mem0', length=1, delay_cost=1)
	T1_11_mem0 += alt(MUL_mem)
	S += (T1_1T2*MUL[0])-1<T1_11_mem0*MUL_mem[0]
	S += T1_11_mem0<=T1_11

	T2_0_in = S.Task('T2_0_in', length=1, delay_cost=1)
	T2_0_in += alt(MUL_in)
	T2_0 = S.Task('T2_0', length=7, delay_cost=1)
	T2_0 += alt(MUL)
	S+=T2_0>=T2_0_in

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	T2_0_mem0 += alt(ADD_mem)
	S += (T2_T0*ADD[0])-1<T2_0_mem0*ADD_mem[0]
	S += (T2_T0*ADD[1])-1<T2_0_mem0*ADD_mem[1]
	S += (T2_T0*ADD[2])-1<T2_0_mem0*ADD_mem[2]
	S += (T2_T0*ADD[3])-1<T2_0_mem0*ADD_mem[3]
	S += T2_0_mem0<=T2_0

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	T2_0_mem1 += alt(ADD_mem)
	S += (T2_T1*ADD[0])-1<T2_0_mem1*ADD_mem[0]
	S += (T2_T1*ADD[1])-1<T2_0_mem1*ADD_mem[1]
	S += (T2_T1*ADD[2])-1<T2_0_mem1*ADD_mem[2]
	S += (T2_T1*ADD[3])-1<T2_0_mem1*ADD_mem[3]
	S += T2_0_mem1<=T2_0

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	T2_1 += alt(ADD)

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	T2_1_mem0 += alt(MUL_mem)
	S += (T2_T2*MUL[0])-1<T2_1_mem0*MUL_mem[0]
	S += T2_1_mem0<=T2_1

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	T3_1 += alt(ADD)

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	T3_1_mem0 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T3_1_mem0*ADD_mem[0]
	S += (T31*ADD[1])-1<T3_1_mem0*ADD_mem[1]
	S += (T31*ADD[2])-1<T3_1_mem0*ADD_mem[2]
	S += (T31*ADD[3])-1<T3_1_mem0*ADD_mem[3]
	S += T3_1_mem0<=T3_1

	C011 = S.Task('C011', length=1, delay_cost=1)
	C011 += alt(ADD)

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	C011_mem0 += alt(ADD_mem)
	S += (T51*ADD[0])-1<C011_mem0*ADD_mem[0]
	S += (T51*ADD[1])-1<C011_mem0*ADD_mem[1]
	S += (T51*ADD[2])-1<C011_mem0*ADD_mem[2]
	S += (T51*ADD[3])-1<C011_mem0*ADD_mem[3]
	S += C011_mem0<=C011

	C01_0 = S.Task('C01_0', length=1, delay_cost=1)
	C01_0 += alt(ADD)

	C01_0_mem0 = S.Task('C01_0_mem0', length=1, delay_cost=1)
	C01_0_mem0 += alt(ADD_mem)
	S += (C010*ADD[0])-1<C01_0_mem0*ADD_mem[0]
	S += (C010*ADD[1])-1<C01_0_mem0*ADD_mem[1]
	S += (C010*ADD[2])-1<C01_0_mem0*ADD_mem[2]
	S += (C010*ADD[3])-1<C01_0_mem0*ADD_mem[3]
	S += C01_0_mem0<=C01_0

	C01_0_mem1 = S.Task('C01_0_mem1', length=1, delay_cost=1)
	C01_0_mem1 += ADD_mem[1]
	S += 14<C01_0_mem1
	S += C01_0_mem1<=C01_0

	C101 = S.Task('C101', length=1, delay_cost=1)
	C101 += alt(ADD)

	C101_mem0 = S.Task('C101_mem0', length=1, delay_cost=1)
	C101_mem0 += alt(ADD_mem)
	S += (T61*ADD[0])-1<C101_mem0*ADD_mem[0]
	S += (T61*ADD[1])-1<C101_mem0*ADD_mem[1]
	S += (T61*ADD[2])-1<C101_mem0*ADD_mem[2]
	S += (T61*ADD[3])-1<C101_mem0*ADD_mem[3]
	S += C101_mem0<=C101

	C10_0 = S.Task('C10_0', length=1, delay_cost=1)
	C10_0 += alt(ADD)

	C10_0_mem0 = S.Task('C10_0_mem0', length=1, delay_cost=1)
	C10_0_mem0 += alt(ADD_mem)
	S += (C100*ADD[0])-1<C10_0_mem0*ADD_mem[0]
	S += (C100*ADD[1])-1<C10_0_mem0*ADD_mem[1]
	S += (C100*ADD[2])-1<C10_0_mem0*ADD_mem[2]
	S += (C100*ADD[3])-1<C10_0_mem0*ADD_mem[3]
	S += C10_0_mem0<=C10_0

	C10_0_mem1 = S.Task('C10_0_mem1', length=1, delay_cost=1)
	C10_0_mem1 += ADD_mem[1]
	S += 9<C10_0_mem1
	S += C10_0_mem1<=C10_0

	C11_0 = S.Task('C11_0', length=1, delay_cost=1)
	C11_0 += alt(ADD)

	C11_0_mem0 = S.Task('C11_0_mem0', length=1, delay_cost=1)
	C11_0_mem0 += alt(ADD_mem)
	S += (C110*ADD[0])-1<C11_0_mem0*ADD_mem[0]
	S += (C110*ADD[1])-1<C11_0_mem0*ADD_mem[1]
	S += (C110*ADD[2])-1<C11_0_mem0*ADD_mem[2]
	S += (C110*ADD[3])-1<C11_0_mem0*ADD_mem[3]
	S += C11_0_mem0<=C11_0

	C11_1 = S.Task('C11_1', length=1, delay_cost=1)
	C11_1 += alt(ADD)

	C11_1_mem0 = S.Task('C11_1_mem0', length=1, delay_cost=1)
	C11_1_mem0 += alt(ADD_mem)
	S += (C111*ADD[0])-1<C11_1_mem0*ADD_mem[0]
	S += (C111*ADD[1])-1<C11_1_mem0*ADD_mem[1]
	S += (C111*ADD[2])-1<C11_1_mem0*ADD_mem[2]
	S += (C111*ADD[3])-1<C11_1_mem0*ADD_mem[3]
	S += C11_1_mem0<=C11_1

	C20_0 = S.Task('C20_0', length=1, delay_cost=1)
	C20_0 += alt(ADD)

	C20_0_mem0 = S.Task('C20_0_mem0', length=1, delay_cost=1)
	C20_0_mem0 += alt(ADD_mem)
	S += (C200*ADD[0])-1<C20_0_mem0*ADD_mem[0]
	S += (C200*ADD[1])-1<C20_0_mem0*ADD_mem[1]
	S += (C200*ADD[2])-1<C20_0_mem0*ADD_mem[2]
	S += (C200*ADD[3])-1<C20_0_mem0*ADD_mem[3]
	S += C20_0_mem0<=C20_0

	C20_0_mem1 = S.Task('C20_0_mem1', length=1, delay_cost=1)
	C20_0_mem1 += alt(ADD_mem)
	S += (T3_0*ADD[0])-1<C20_0_mem1*ADD_mem[0]
	S += (T3_0*ADD[1])-1<C20_0_mem1*ADD_mem[1]
	S += (T3_0*ADD[2])-1<C20_0_mem1*ADD_mem[2]
	S += (T3_0*ADD[3])-1<C20_0_mem1*ADD_mem[3]
	S += C20_0_mem1<=C20_0

	C211 = S.Task('C211', length=1, delay_cost=1)
	C211 += alt(ADD)

	C211_mem0 = S.Task('C211_mem0', length=1, delay_cost=1)
	C211_mem0 += alt(ADD_mem)
	S += (T71*ADD[0])-1<C211_mem0*ADD_mem[0]
	S += (T71*ADD[1])-1<C211_mem0*ADD_mem[1]
	S += (T71*ADD[2])-1<C211_mem0*ADD_mem[2]
	S += (T71*ADD[3])-1<C211_mem0*ADD_mem[3]
	S += C211_mem0<=C211

	C21_0 = S.Task('C21_0', length=1, delay_cost=1)
	C21_0 += alt(ADD)

	C21_0_mem0 = S.Task('C21_0_mem0', length=1, delay_cost=1)
	C21_0_mem0 += alt(ADD_mem)
	S += (C210*ADD[0])-1<C21_0_mem0*ADD_mem[0]
	S += (C210*ADD[1])-1<C21_0_mem0*ADD_mem[1]
	S += (C210*ADD[2])-1<C21_0_mem0*ADD_mem[2]
	S += (C210*ADD[3])-1<C21_0_mem0*ADD_mem[3]
	S += C21_0_mem0<=C21_0

	C21_0_mem1 = S.Task('C21_0_mem1', length=1, delay_cost=1)
	C21_0_mem1 += ADD_mem[2]
	S += 11<C21_0_mem1
	S += C21_0_mem1<=C21_0

	C000 = S.Task('C000', length=1, delay_cost=1)
	C000 += alt(ADD)

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	C000_mem0 += alt(ADD_mem)
	S += (T3_0*ADD[0])-1<C000_mem0*ADD_mem[0]
	S += (T3_0*ADD[1])-1<C000_mem0*ADD_mem[1]
	S += (T3_0*ADD[2])-1<C000_mem0*ADD_mem[2]
	S += (T3_0*ADD[3])-1<C000_mem0*ADD_mem[3]
	S += C000_mem0<=C000

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	C000_mem1 += alt(ADD_mem)
	S += (T3_1*ADD[0])-1<C000_mem1*ADD_mem[0]
	S += (T3_1*ADD[1])-1<C000_mem1*ADD_mem[1]
	S += (T3_1*ADD[2])-1<C000_mem1*ADD_mem[2]
	S += (T3_1*ADD[3])-1<C000_mem1*ADD_mem[3]
	S += C000_mem1<=C000

	C001 = S.Task('C001', length=1, delay_cost=1)
	C001 += alt(ADD)

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	C001_mem0 += alt(ADD_mem)
	S += (T3_0*ADD[0])-1<C001_mem0*ADD_mem[0]
	S += (T3_0*ADD[1])-1<C001_mem0*ADD_mem[1]
	S += (T3_0*ADD[2])-1<C001_mem0*ADD_mem[2]
	S += (T3_0*ADD[3])-1<C001_mem0*ADD_mem[3]
	S += C001_mem0<=C001

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	C001_mem1 += alt(ADD_mem)
	S += (T3_1*ADD[0])-1<C001_mem1*ADD_mem[0]
	S += (T3_1*ADD[1])-1<C001_mem1*ADD_mem[1]
	S += (T3_1*ADD[2])-1<C001_mem1*ADD_mem[2]
	S += (T3_1*ADD[3])-1<C001_mem1*ADD_mem[3]
	S += C001_mem1<=C001

	C01_1 = S.Task('C01_1', length=1, delay_cost=1)
	C01_1 += alt(ADD)

	C01_1_mem0 = S.Task('C01_1_mem0', length=1, delay_cost=1)
	C01_1_mem0 += alt(ADD_mem)
	S += (C011*ADD[0])-1<C01_1_mem0*ADD_mem[0]
	S += (C011*ADD[1])-1<C01_1_mem0*ADD_mem[1]
	S += (C011*ADD[2])-1<C01_1_mem0*ADD_mem[2]
	S += (C011*ADD[3])-1<C01_1_mem0*ADD_mem[3]
	S += C01_1_mem0<=C01_1

	C01_1_mem1 = S.Task('C01_1_mem1', length=1, delay_cost=1)
	C01_1_mem1 += alt(ADD_mem)
	S += (T51*ADD[0])-1<C01_1_mem1*ADD_mem[0]
	S += (T51*ADD[1])-1<C01_1_mem1*ADD_mem[1]
	S += (T51*ADD[2])-1<C01_1_mem1*ADD_mem[2]
	S += (T51*ADD[3])-1<C01_1_mem1*ADD_mem[3]
	S += C01_1_mem1<=C01_1

	C01_10 = S.Task('C01_10', length=1, delay_cost=1)
	C01_10 += alt(ADD)

	C01_10_mem0 = S.Task('C01_10_mem0', length=1, delay_cost=1)
	C01_10_mem0 += alt(ADD_mem)
	S += (C01_0*ADD[0])-1<C01_10_mem0*ADD_mem[0]
	S += (C01_0*ADD[1])-1<C01_10_mem0*ADD_mem[1]
	S += (C01_0*ADD[2])-1<C01_10_mem0*ADD_mem[2]
	S += (C01_0*ADD[3])-1<C01_10_mem0*ADD_mem[3]
	S += C01_10_mem0<=C01_10

	C01_10_mem1 = S.Task('C01_10_mem1', length=1, delay_cost=1)
	C01_10_mem1 += INPUT_mem_r
	S += C01_10_mem1<=C01_10

	C10_1 = S.Task('C10_1', length=1, delay_cost=1)
	C10_1 += alt(ADD)

	C10_1_mem0 = S.Task('C10_1_mem0', length=1, delay_cost=1)
	C10_1_mem0 += alt(ADD_mem)
	S += (C101*ADD[0])-1<C10_1_mem0*ADD_mem[0]
	S += (C101*ADD[1])-1<C10_1_mem0*ADD_mem[1]
	S += (C101*ADD[2])-1<C10_1_mem0*ADD_mem[2]
	S += (C101*ADD[3])-1<C10_1_mem0*ADD_mem[3]
	S += C10_1_mem0<=C10_1

	C10_1_mem1 = S.Task('C10_1_mem1', length=1, delay_cost=1)
	C10_1_mem1 += alt(ADD_mem)
	S += (T61*ADD[0])-1<C10_1_mem1*ADD_mem[0]
	S += (T61*ADD[1])-1<C10_1_mem1*ADD_mem[1]
	S += (T61*ADD[2])-1<C10_1_mem1*ADD_mem[2]
	S += (T61*ADD[3])-1<C10_1_mem1*ADD_mem[3]
	S += C10_1_mem1<=C10_1

	C11_10 = S.Task('C11_10', length=1, delay_cost=1)
	C11_10 += alt(ADD)

	C11_10_mem0 = S.Task('C11_10_mem0', length=1, delay_cost=1)
	C11_10_mem0 += alt(MUL_mem)
	S += (T1_10*MUL[0])-1<C11_10_mem0*MUL_mem[0]
	S += C11_10_mem0<=C11_10

	C11_10_mem1 = S.Task('C11_10_mem1', length=1, delay_cost=1)
	C11_10_mem1 += alt(ADD_mem)
	S += (C11_0*ADD[0])-1<C11_10_mem1*ADD_mem[0]
	S += (C11_0*ADD[1])-1<C11_10_mem1*ADD_mem[1]
	S += (C11_0*ADD[2])-1<C11_10_mem1*ADD_mem[2]
	S += (C11_0*ADD[3])-1<C11_10_mem1*ADD_mem[3]
	S += C11_10_mem1<=C11_10

	C11_11 = S.Task('C11_11', length=1, delay_cost=1)
	C11_11 += alt(ADD)

	C11_11_mem0 = S.Task('C11_11_mem0', length=1, delay_cost=1)
	C11_11_mem0 += alt(ADD_mem)
	S += (T1_11*ADD[0])-1<C11_11_mem0*ADD_mem[0]
	S += (T1_11*ADD[1])-1<C11_11_mem0*ADD_mem[1]
	S += (T1_11*ADD[2])-1<C11_11_mem0*ADD_mem[2]
	S += (T1_11*ADD[3])-1<C11_11_mem0*ADD_mem[3]
	S += C11_11_mem0<=C11_11

	C11_11_mem1 = S.Task('C11_11_mem1', length=1, delay_cost=1)
	C11_11_mem1 += alt(ADD_mem)
	S += (C11_1*ADD[0])-1<C11_11_mem1*ADD_mem[0]
	S += (C11_1*ADD[1])-1<C11_11_mem1*ADD_mem[1]
	S += (C11_1*ADD[2])-1<C11_11_mem1*ADD_mem[2]
	S += (C11_1*ADD[3])-1<C11_11_mem1*ADD_mem[3]
	S += C11_11_mem1<=C11_11

	C20_1 = S.Task('C20_1', length=1, delay_cost=1)
	C20_1 += alt(ADD)

	C20_1_mem0 = S.Task('C20_1_mem0', length=1, delay_cost=1)
	C20_1_mem0 += alt(ADD_mem)
	S += (C201*ADD[0])-1<C20_1_mem0*ADD_mem[0]
	S += (C201*ADD[1])-1<C20_1_mem0*ADD_mem[1]
	S += (C201*ADD[2])-1<C20_1_mem0*ADD_mem[2]
	S += (C201*ADD[3])-1<C20_1_mem0*ADD_mem[3]
	S += C20_1_mem0<=C20_1

	C20_1_mem1 = S.Task('C20_1_mem1', length=1, delay_cost=1)
	C20_1_mem1 += alt(ADD_mem)
	S += (T3_1*ADD[0])-1<C20_1_mem1*ADD_mem[0]
	S += (T3_1*ADD[1])-1<C20_1_mem1*ADD_mem[1]
	S += (T3_1*ADD[2])-1<C20_1_mem1*ADD_mem[2]
	S += (T3_1*ADD[3])-1<C20_1_mem1*ADD_mem[3]
	S += C20_1_mem1<=C20_1

	C20_10 = S.Task('C20_10', length=1, delay_cost=1)
	C20_10 += alt(ADD)

	C20_10_mem0 = S.Task('C20_10_mem0', length=1, delay_cost=1)
	C20_10_mem0 += alt(ADD_mem)
	S += (C20_0*ADD[0])-1<C20_10_mem0*ADD_mem[0]
	S += (C20_0*ADD[1])-1<C20_10_mem0*ADD_mem[1]
	S += (C20_0*ADD[2])-1<C20_10_mem0*ADD_mem[2]
	S += (C20_0*ADD[3])-1<C20_10_mem0*ADD_mem[3]
	S += C20_10_mem0<=C20_10

	C21_1 = S.Task('C21_1', length=1, delay_cost=1)
	C21_1 += alt(ADD)

	C21_1_mem0 = S.Task('C21_1_mem0', length=1, delay_cost=1)
	C21_1_mem0 += alt(ADD_mem)
	S += (C211*ADD[0])-1<C21_1_mem0*ADD_mem[0]
	S += (C211*ADD[1])-1<C21_1_mem0*ADD_mem[1]
	S += (C211*ADD[2])-1<C21_1_mem0*ADD_mem[2]
	S += (C211*ADD[3])-1<C21_1_mem0*ADD_mem[3]
	S += C21_1_mem0<=C21_1

	C21_1_mem1 = S.Task('C21_1_mem1', length=1, delay_cost=1)
	C21_1_mem1 += alt(ADD_mem)
	S += (T71*ADD[0])-1<C21_1_mem1*ADD_mem[0]
	S += (T71*ADD[1])-1<C21_1_mem1*ADD_mem[1]
	S += (T71*ADD[2])-1<C21_1_mem1*ADD_mem[2]
	S += (T71*ADD[3])-1<C21_1_mem1*ADD_mem[3]
	S += C21_1_mem1<=C21_1

	C21_10 = S.Task('C21_10', length=1, delay_cost=1)
	C21_10 += alt(ADD)

	C21_10_mem0 = S.Task('C21_10_mem0', length=1, delay_cost=1)
	C21_10_mem0 += alt(ADD_mem)
	S += (C21_0*ADD[0])-1<C21_10_mem0*ADD_mem[0]
	S += (C21_0*ADD[1])-1<C21_10_mem0*ADD_mem[1]
	S += (C21_0*ADD[2])-1<C21_10_mem0*ADD_mem[2]
	S += (C21_0*ADD[3])-1<C21_10_mem0*ADD_mem[3]
	S += C21_10_mem0<=C21_10

	C21_10_mem1 = S.Task('C21_10_mem1', length=1, delay_cost=1)
	C21_10_mem1 += INPUT_mem_r
	S += C21_10_mem1<=C21_10

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "SQR012345_mul1_add4/SQR012345_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_SQR012345_mul1_add4_1(0, 0)