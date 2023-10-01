from pyschedule import Scenario, solvers, plotters, alt

def solve_SQR012345_mul1_add4_3(ConstStep, ExpStep):
	horizon = 129
	S=Scenario("SQR012345_mul1_add4_3",horizon = horizon)

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
	T0T2_in = S.Task('T0T2_in', length=1, delay_cost=1)
	S += T0T2_in >= 0
	T0T2_in += MUL_in[0]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 0
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 0
	T0T2_mem1 += INPUT_mem_r

	T0T2 = S.Task('T0T2', length=7, delay_cost=1)
	S += T0T2 >= 1
	T0T2 += MUL[0]

	T4T2_in = S.Task('T4T2_in', length=1, delay_cost=1)
	S += T4T2_in >= 1
	T4T2_in += MUL_in[0]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 1
	T4T2_mem0 += INPUT_mem_r

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 1
	T4T2_mem1 += INPUT_mem_r

	T3T0_in = S.Task('T3T0_in', length=1, delay_cost=1)
	S += T3T0_in >= 2
	T3T0_in += MUL_in[0]

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 2
	T3T0_mem0 += INPUT_mem_r

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 2
	T3T0_mem1 += INPUT_mem_r

	T4T2 = S.Task('T4T2', length=7, delay_cost=1)
	S += T4T2 >= 2
	T4T2 += MUL[0]

	T3T0 = S.Task('T3T0', length=7, delay_cost=1)
	S += T3T0 >= 3
	T3T0 += MUL[0]

	T3T1_in = S.Task('T3T1_in', length=1, delay_cost=1)
	S += T3T1_in >= 3
	T3T1_in += MUL_in[0]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 3
	T3T1_mem0 += INPUT_mem_r

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 3
	T3T1_mem1 += INPUT_mem_r

	T3T1 = S.Task('T3T1', length=7, delay_cost=1)
	S += T3T1 >= 4
	T3T1 += MUL[0]

	T5T1_in = S.Task('T5T1_in', length=1, delay_cost=1)
	S += T5T1_in >= 4
	T5T1_in += MUL_in[0]

	T5T1_mem0 = S.Task('T5T1_mem0', length=1, delay_cost=1)
	S += T5T1_mem0 >= 4
	T5T1_mem0 += INPUT_mem_r

	T5T1_mem1 = S.Task('T5T1_mem1', length=1, delay_cost=1)
	S += T5T1_mem1 >= 4
	T5T1_mem1 += INPUT_mem_r

	T5T0_in = S.Task('T5T0_in', length=1, delay_cost=1)
	S += T5T0_in >= 5
	T5T0_in += MUL_in[0]

	T5T0_mem0 = S.Task('T5T0_mem0', length=1, delay_cost=1)
	S += T5T0_mem0 >= 5
	T5T0_mem0 += INPUT_mem_r

	T5T0_mem1 = S.Task('T5T0_mem1', length=1, delay_cost=1)
	S += T5T0_mem1 >= 5
	T5T0_mem1 += INPUT_mem_r

	T5T1 = S.Task('T5T1', length=7, delay_cost=1)
	S += T5T1 >= 5
	T5T1 += MUL[0]

	T5T0 = S.Task('T5T0', length=7, delay_cost=1)
	S += T5T0 >= 6
	T5T0 += MUL[0]

	T7T0_in = S.Task('T7T0_in', length=1, delay_cost=1)
	S += T7T0_in >= 6
	T7T0_in += MUL_in[0]

	T7T0_mem0 = S.Task('T7T0_mem0', length=1, delay_cost=1)
	S += T7T0_mem0 >= 6
	T7T0_mem0 += INPUT_mem_r

	T7T0_mem1 = S.Task('T7T0_mem1', length=1, delay_cost=1)
	S += T7T0_mem1 >= 6
	T7T0_mem1 += INPUT_mem_r

	T7T0 = S.Task('T7T0', length=7, delay_cost=1)
	S += T7T0 >= 7
	T7T0 += MUL[0]

	T7T1_in = S.Task('T7T1_in', length=1, delay_cost=1)
	S += T7T1_in >= 7
	T7T1_in += MUL_in[0]

	T7T1_mem0 = S.Task('T7T1_mem0', length=1, delay_cost=1)
	S += T7T1_mem0 >= 7
	T7T1_mem0 += INPUT_mem_r

	T7T1_mem1 = S.Task('T7T1_mem1', length=1, delay_cost=1)
	S += T7T1_mem1 >= 7
	T7T1_mem1 += INPUT_mem_r

	T6T0_in = S.Task('T6T0_in', length=1, delay_cost=1)
	S += T6T0_in >= 8
	T6T0_in += MUL_in[0]

	T6T0_mem0 = S.Task('T6T0_mem0', length=1, delay_cost=1)
	S += T6T0_mem0 >= 8
	T6T0_mem0 += INPUT_mem_r

	T6T0_mem1 = S.Task('T6T0_mem1', length=1, delay_cost=1)
	S += T6T0_mem1 >= 8
	T6T0_mem1 += INPUT_mem_r

	T7T1 = S.Task('T7T1', length=7, delay_cost=1)
	S += T7T1 >= 8
	T7T1 += MUL[0]

	C111_mem0 = S.Task('C111_mem0', length=1, delay_cost=1)
	S += C111_mem0 >= 9
	C111_mem0 += ADD_mem[0]

	C111_mem1 = S.Task('C111_mem1', length=1, delay_cost=1)
	S += C111_mem1 >= 9
	C111_mem1 += ADD_mem[3]

	T6T0 = S.Task('T6T0', length=7, delay_cost=1)
	S += T6T0 >= 9
	T6T0 += MUL[0]

	T6T1_in = S.Task('T6T1_in', length=1, delay_cost=1)
	S += T6T1_in >= 9
	T6T1_in += MUL_in[0]

	T6T1_mem0 = S.Task('T6T1_mem0', length=1, delay_cost=1)
	S += T6T1_mem0 >= 9
	T6T1_mem0 += INPUT_mem_r

	T6T1_mem1 = S.Task('T6T1_mem1', length=1, delay_cost=1)
	S += T6T1_mem1 >= 9
	T6T1_mem1 += INPUT_mem_r

	C111 = S.Task('C111', length=1, delay_cost=1)
	S += C111 >= 10
	C111 += ADD[0]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 10
	T30_mem0 += MUL_mem[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 10
	T30_mem1 += MUL_mem[0]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 10
	T3T2_mem0 += INPUT_mem_r

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 10
	T3T2_mem1 += INPUT_mem_r

	T6T1 = S.Task('T6T1', length=7, delay_cost=1)
	S += T6T1 >= 10
	T6T1 += MUL[0]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 11
	T30 += ADD[2]

	T3T2 = S.Task('T3T2', length=1, delay_cost=1)
	S += T3T2 >= 11
	T3T2 += ADD[1]

	T3T3_mem0 = S.Task('T3T3_mem0', length=1, delay_cost=1)
	S += T3T3_mem0 >= 11
	T3T3_mem0 += INPUT_mem_r

	T3T3_mem1 = S.Task('T3T3_mem1', length=1, delay_cost=1)
	S += T3T3_mem1 >= 11
	T3T3_mem1 += INPUT_mem_r

	T3T5_mem0 = S.Task('T3T5_mem0', length=1, delay_cost=1)
	S += T3T5_mem0 >= 11
	T3T5_mem0 += MUL_mem[0]

	T3T5_mem1 = S.Task('T3T5_mem1', length=1, delay_cost=1)
	S += T3T5_mem1 >= 11
	T3T5_mem1 += MUL_mem[0]

	T3T3 = S.Task('T3T3', length=1, delay_cost=1)
	S += T3T3 >= 12
	T3T3 += ADD[1]

	T3T4_in = S.Task('T3T4_in', length=1, delay_cost=1)
	S += T3T4_in >= 12
	T3T4_in += MUL_in[0]

	T3T4_mem0 = S.Task('T3T4_mem0', length=1, delay_cost=1)
	S += T3T4_mem0 >= 12
	T3T4_mem0 += ADD_mem[1]

	T3T4_mem1 = S.Task('T3T4_mem1', length=1, delay_cost=1)
	S += T3T4_mem1 >= 12
	T3T4_mem1 += ADD_mem[1]

	T3T5 = S.Task('T3T5', length=1, delay_cost=1)
	S += T3T5 >= 12
	T3T5 += ADD[3]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 12
	T50_mem0 += MUL_mem[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 12
	T50_mem1 += MUL_mem[0]

	T7T3_mem0 = S.Task('T7T3_mem0', length=1, delay_cost=1)
	S += T7T3_mem0 >= 12
	T7T3_mem0 += INPUT_mem_r

	T7T3_mem1 = S.Task('T7T3_mem1', length=1, delay_cost=1)
	S += T7T3_mem1 >= 12
	T7T3_mem1 += INPUT_mem_r

	T3T4 = S.Task('T3T4', length=7, delay_cost=1)
	S += T3T4 >= 13
	T3T4 += MUL[0]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 13
	T50 += ADD[2]

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	S += T5T5_mem0 >= 13
	T5T5_mem0 += MUL_mem[0]

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	S += T5T5_mem1 >= 13
	T5T5_mem1 += MUL_mem[0]

	T7T2_mem0 = S.Task('T7T2_mem0', length=1, delay_cost=1)
	S += T7T2_mem0 >= 13
	T7T2_mem0 += INPUT_mem_r

	T7T2_mem1 = S.Task('T7T2_mem1', length=1, delay_cost=1)
	S += T7T2_mem1 >= 13
	T7T2_mem1 += INPUT_mem_r

	T7T3 = S.Task('T7T3', length=1, delay_cost=1)
	S += T7T3 >= 13
	T7T3 += ADD[0]

	C01_0_mem0 = S.Task('C01_0_mem0', length=1, delay_cost=1)
	S += C01_0_mem0 >= 14
	C01_0_mem0 += ADD_mem[2]

	C01_0_mem1 = S.Task('C01_0_mem1', length=1, delay_cost=1)
	S += C01_0_mem1 >= 14
	C01_0_mem1 += ADD_mem[2]

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	S += T5T5 >= 14
	T5T5 += ADD[0]

	T6T3_mem0 = S.Task('T6T3_mem0', length=1, delay_cost=1)
	S += T6T3_mem0 >= 14
	T6T3_mem0 += INPUT_mem_r

	T6T3_mem1 = S.Task('T6T3_mem1', length=1, delay_cost=1)
	S += T6T3_mem1 >= 14
	T6T3_mem1 += INPUT_mem_r

	T7T2 = S.Task('T7T2', length=1, delay_cost=1)
	S += T7T2 >= 14
	T7T2 += ADD[1]

	T7T4_in = S.Task('T7T4_in', length=1, delay_cost=1)
	S += T7T4_in >= 14
	T7T4_in += MUL_in[0]

	T7T4_mem0 = S.Task('T7T4_mem0', length=1, delay_cost=1)
	S += T7T4_mem0 >= 14
	T7T4_mem0 += ADD_mem[1]

	T7T4_mem1 = S.Task('T7T4_mem1', length=1, delay_cost=1)
	S += T7T4_mem1 >= 14
	T7T4_mem1 += ADD_mem[0]

	T7T5_mem0 = S.Task('T7T5_mem0', length=1, delay_cost=1)
	S += T7T5_mem0 >= 14
	T7T5_mem0 += MUL_mem[0]

	T7T5_mem1 = S.Task('T7T5_mem1', length=1, delay_cost=1)
	S += T7T5_mem1 >= 14
	T7T5_mem1 += MUL_mem[0]

	C01_0 = S.Task('C01_0', length=1, delay_cost=1)
	S += C01_0 >= 15
	C01_0 += ADD[2]

	T6T2_mem0 = S.Task('T6T2_mem0', length=1, delay_cost=1)
	S += T6T2_mem0 >= 15
	T6T2_mem0 += INPUT_mem_r

	T6T2_mem1 = S.Task('T6T2_mem1', length=1, delay_cost=1)
	S += T6T2_mem1 >= 15
	T6T2_mem1 += INPUT_mem_r

	T6T3 = S.Task('T6T3', length=1, delay_cost=1)
	S += T6T3 >= 15
	T6T3 += ADD[1]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 15
	T70_mem0 += MUL_mem[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 15
	T70_mem1 += MUL_mem[0]

	T7T4 = S.Task('T7T4', length=7, delay_cost=1)
	S += T7T4 >= 15
	T7T4 += MUL[0]

	T7T5 = S.Task('T7T5', length=1, delay_cost=1)
	S += T7T5 >= 15
	T7T5 += ADD[0]

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	S += T5T2_mem0 >= 16
	T5T2_mem0 += INPUT_mem_r

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	S += T5T2_mem1 >= 16
	T5T2_mem1 += INPUT_mem_r

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 16
	T60_mem0 += MUL_mem[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 16
	T60_mem1 += MUL_mem[0]

	T6T2 = S.Task('T6T2', length=1, delay_cost=1)
	S += T6T2 >= 16
	T6T2 += ADD[0]

	T6T4_in = S.Task('T6T4_in', length=1, delay_cost=1)
	S += T6T4_in >= 16
	T6T4_in += MUL_in[0]

	T6T4_mem0 = S.Task('T6T4_mem0', length=1, delay_cost=1)
	S += T6T4_mem0 >= 16
	T6T4_mem0 += ADD_mem[0]

	T6T4_mem1 = S.Task('T6T4_mem1', length=1, delay_cost=1)
	S += T6T4_mem1 >= 16
	T6T4_mem1 += ADD_mem[1]

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 16
	T70 += ADD[3]

	C21_0_mem0 = S.Task('C21_0_mem0', length=1, delay_cost=1)
	S += C21_0_mem0 >= 17
	C21_0_mem0 += ADD_mem[0]

	C21_0_mem1 = S.Task('C21_0_mem1', length=1, delay_cost=1)
	S += C21_0_mem1 >= 17
	C21_0_mem1 += ADD_mem[3]

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	S += T5T2 >= 17
	T5T2 += ADD[3]

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	S += T5T3_mem0 >= 17
	T5T3_mem0 += INPUT_mem_r

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	S += T5T3_mem1 >= 17
	T5T3_mem1 += INPUT_mem_r

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 17
	T60 += ADD[2]

	T6T4 = S.Task('T6T4', length=7, delay_cost=1)
	S += T6T4 >= 17
	T6T4 += MUL[0]

	T6T5_mem0 = S.Task('T6T5_mem0', length=1, delay_cost=1)
	S += T6T5_mem0 >= 17
	T6T5_mem0 += MUL_mem[0]

	T6T5_mem1 = S.Task('T6T5_mem1', length=1, delay_cost=1)
	S += T6T5_mem1 >= 17
	T6T5_mem1 += MUL_mem[0]

	C10_0_mem0 = S.Task('C10_0_mem0', length=1, delay_cost=1)
	S += C10_0_mem0 >= 18
	C10_0_mem0 += ADD_mem[1]

	C10_0_mem1 = S.Task('C10_0_mem1', length=1, delay_cost=1)
	S += C10_0_mem1 >= 18
	C10_0_mem1 += ADD_mem[2]

	C21_0 = S.Task('C21_0', length=1, delay_cost=1)
	S += C21_0 >= 18
	C21_0 += ADD[0]

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	S += T4T0_mem0 >= 18
	T4T0_mem0 += INPUT_mem_r

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	S += T4T0_mem1 >= 18
	T4T0_mem1 += INPUT_mem_r

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	S += T5T3 >= 18
	T5T3 += ADD[3]

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	S += T5T4_in >= 18
	T5T4_in += MUL_in[0]

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	S += T5T4_mem0 >= 18
	T5T4_mem0 += ADD_mem[3]

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	S += T5T4_mem1 >= 18
	T5T4_mem1 += ADD_mem[3]

	T6T5 = S.Task('T6T5', length=1, delay_cost=1)
	S += T6T5 >= 18
	T6T5 += ADD[2]

	C10_0 = S.Task('C10_0', length=1, delay_cost=1)
	S += C10_0 >= 19
	C10_0 += ADD[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 19
	T31_mem0 += MUL_mem[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 19
	T31_mem1 += ADD_mem[3]

	T4T0 = S.Task('T4T0', length=1, delay_cost=1)
	S += T4T0 >= 19
	T4T0 += ADD[1]

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	S += T4T1_mem0 >= 19
	T4T1_mem0 += INPUT_mem_r

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	S += T4T1_mem1 >= 19
	T4T1_mem1 += INPUT_mem_r

	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	S += T5T4 >= 19
	T5T4 += MUL[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 20
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 20
	T0T0_mem1 += INPUT_mem_r

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 20
	T31 += ADD[2]

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	S += T40_in >= 20
	T40_in += MUL_in[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 20
	T40_mem0 += ADD_mem[1]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 20
	T40_mem1 += ADD_mem[0]

	T4T1 = S.Task('T4T1', length=1, delay_cost=1)
	S += T4T1 >= 20
	T4T1 += ADD[0]

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	S += C000_mem0 >= 21
	C000_mem0 += ADD_mem[2]

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	S += C000_mem1 >= 21
	C000_mem1 += ADD_mem[1]

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	S += C001_mem0 >= 21
	C001_mem0 += ADD_mem[2]

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	S += C001_mem1 >= 21
	C001_mem1 += ADD_mem[1]

	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	S += T0T0 >= 21
	T0T0 += ADD[3]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 21
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 21
	T0T1_mem1 += INPUT_mem_r

	T40 = S.Task('T40', length=7, delay_cost=1)
	S += T40 >= 21
	T40 += MUL[0]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 21
	T71_mem0 += MUL_mem[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 21
	T71_mem1 += ADD_mem[0]

	C000 = S.Task('C000', length=1, delay_cost=1)
	S += C000 >= 22
	C000 += ADD[3]

	C001 = S.Task('C001', length=1, delay_cost=1)
	S += C001 >= 22
	C001 += ADD[1]

	C00_1_mem0 = S.Task('C00_1_mem0', length=1, delay_cost=1)
	S += C00_1_mem0 >= 22
	C00_1_mem0 += ADD_mem[1]

	C00_1_mem1 = S.Task('C00_1_mem1', length=1, delay_cost=1)
	S += C00_1_mem1 >= 22
	C00_1_mem1 += ADD_mem[1]

	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	S += T00_in >= 22
	T00_in += MUL_in[0]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 22
	T00_mem0 += ADD_mem[3]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 22
	T00_mem1 += ADD_mem[2]

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	S += T0T1 >= 22
	T0T1 += ADD[2]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 22
	T11_mem0 += INPUT_mem_r

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 22
	T11_mem1 += INPUT_mem_r

	T71 = S.Task('T71', length=1, delay_cost=1)
	S += T71 >= 22
	T71 += ADD[0]

	C00_1 = S.Task('C00_1', length=1, delay_cost=1)
	S += C00_1 >= 23
	C00_1 += ADD[2]

	C21_1_mem0 = S.Task('C21_1_mem0', length=1, delay_cost=1)
	S += C21_1_mem0 >= 23
	C21_1_mem0 += ADD_mem[2]

	C21_1_mem1 = S.Task('C21_1_mem1', length=1, delay_cost=1)
	S += C21_1_mem1 >= 23
	C21_1_mem1 += ADD_mem[0]

	T00 = S.Task('T00', length=7, delay_cost=1)
	S += T00 >= 23
	T00 += MUL[0]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 23
	T11 += ADD[1]

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 23
	T1_1_mem0 += ADD_mem[1]

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	S += T1_1_mem1 >= 23
	T1_1_mem1 += INPUT_mem_r

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 23
	T21_mem0 += ADD_mem[1]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 23
	T21_mem1 += INPUT_mem_r

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 23
	T61_mem0 += MUL_mem[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 23
	T61_mem1 += ADD_mem[2]

	C21_1 = S.Task('C21_1', length=1, delay_cost=1)
	S += C21_1 >= 24
	C21_1 += ADD[3]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 24
	T10_mem0 += INPUT_mem_r

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 24
	T10_mem1 += INPUT_mem_r

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 24
	T1_1 += ADD[1]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 24
	T21 += ADD[2]

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 24
	T61 += ADD[0]

	C10_1_mem0 = S.Task('C10_1_mem0', length=1, delay_cost=1)
	S += C10_1_mem0 >= 25
	C10_1_mem0 += ADD_mem[2]

	C10_1_mem1 = S.Task('C10_1_mem1', length=1, delay_cost=1)
	S += C10_1_mem1 >= 25
	C10_1_mem1 += ADD_mem[0]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 25
	T10 += ADD[3]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 25
	T1_0_mem0 += ADD_mem[3]

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 25
	T1_0_mem1 += INPUT_mem_r

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 25
	T20_mem0 += ADD_mem[3]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 25
	T20_mem1 += INPUT_mem_r

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 25
	T51_mem0 += MUL_mem[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 25
	T51_mem1 += ADD_mem[0]

	C01_10_mem0 = S.Task('C01_10_mem0', length=1, delay_cost=1)
	S += C01_10_mem0 >= 26
	C01_10_mem0 += ADD_mem[2]

	C01_10_mem1 = S.Task('C01_10_mem1', length=1, delay_cost=1)
	S += C01_10_mem1 >= 26
	C01_10_mem1 += INPUT_mem_r

	C10_1 = S.Task('C10_1', length=1, delay_cost=1)
	S += C10_1 >= 26
	C10_1 += ADD[2]

	C21_10_mem0 = S.Task('C21_10_mem0', length=1, delay_cost=1)
	S += C21_10_mem0 >= 26
	C21_10_mem0 += ADD_mem[0]

	C21_10_mem1 = S.Task('C21_10_mem1', length=1, delay_cost=1)
	S += C21_10_mem1 >= 26
	C21_10_mem1 += INPUT_mem_r

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	S += T1_0 >= 26
	T1_0 += ADD[3]

	T1_1T1_mem0 = S.Task('T1_1T1_mem0', length=1, delay_cost=1)
	S += T1_1T1_mem0 >= 26
	T1_1T1_mem0 += ADD_mem[3]

	T1_1T1_mem1 = S.Task('T1_1T1_mem1', length=1, delay_cost=1)
	S += T1_1T1_mem1 >= 26
	T1_1T1_mem1 += ADD_mem[1]

	T1_1T2_in = S.Task('T1_1T2_in', length=1, delay_cost=1)
	S += T1_1T2_in >= 26
	T1_1T2_in += MUL_in[0]

	T1_1T2_mem0 = S.Task('T1_1T2_mem0', length=1, delay_cost=1)
	S += T1_1T2_mem0 >= 26
	T1_1T2_mem0 += ADD_mem[3]

	T1_1T2_mem1 = S.Task('T1_1T2_mem1', length=1, delay_cost=1)
	S += T1_1T2_mem1 >= 26
	T1_1T2_mem1 += ADD_mem[1]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 26
	T20 += ADD[0]

	T2_T1_mem0 = S.Task('T2_T1_mem0', length=1, delay_cost=1)
	S += T2_T1_mem0 >= 26
	T2_T1_mem0 += ADD_mem[0]

	T2_T1_mem1 = S.Task('T2_T1_mem1', length=1, delay_cost=1)
	S += T2_T1_mem1 >= 26
	T2_T1_mem1 += ADD_mem[2]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 26
	T51 += ADD[1]

	C01_10 = S.Task('C01_10', length=1, delay_cost=1)
	S += C01_10 >= 27
	C01_10 += ADD[1]

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	S += C200_mem0 >= 27
	C200_mem0 += MUL_mem[0]

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	S += C200_mem1 >= 27
	C200_mem1 += ADD_mem[3]

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	S += C201_mem0 >= 27
	C201_mem0 += MUL_mem[0]

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	S += C201_mem1 >= 27
	C201_mem1 += ADD_mem[3]

	C21_10 = S.Task('C21_10', length=1, delay_cost=1)
	S += C21_10 >= 27
	C21_10 += ADD[2]

	T1_1T1 = S.Task('T1_1T1', length=1, delay_cost=1)
	S += T1_1T1 >= 27
	T1_1T1 += ADD[3]

	T1_1T2 = S.Task('T1_1T2', length=7, delay_cost=1)
	S += T1_1T2 >= 27
	T1_1T2 += MUL[0]

	T2_T0_mem0 = S.Task('T2_T0_mem0', length=1, delay_cost=1)
	S += T2_T0_mem0 >= 27
	T2_T0_mem0 += ADD_mem[0]

	T2_T0_mem1 = S.Task('T2_T0_mem1', length=1, delay_cost=1)
	S += T2_T0_mem1 >= 27
	T2_T0_mem1 += ADD_mem[2]

	T2_T1 = S.Task('T2_T1', length=1, delay_cost=1)
	S += T2_T1 >= 27
	T2_T1 += ADD[0]

	T2_T2_in = S.Task('T2_T2_in', length=1, delay_cost=1)
	S += T2_T2_in >= 27
	T2_T2_in += MUL_in[0]

	T2_T2_mem0 = S.Task('T2_T2_mem0', length=1, delay_cost=1)
	S += T2_T2_mem0 >= 27
	T2_T2_mem0 += ADD_mem[0]

	T2_T2_mem1 = S.Task('T2_T2_mem1', length=1, delay_cost=1)
	S += T2_T2_mem1 >= 27
	T2_T2_mem1 += ADD_mem[2]

	C01_1_mem0 = S.Task('C01_1_mem0', length=1, delay_cost=1)
	S += C01_1_mem0 >= 28
	C01_1_mem0 += ADD_mem[3]

	C01_1_mem1 = S.Task('C01_1_mem1', length=1, delay_cost=1)
	S += C01_1_mem1 >= 28
	C01_1_mem1 += ADD_mem[1]

	C200 = S.Task('C200', length=1, delay_cost=1)
	S += C200 >= 28
	C200 += ADD[0]

	C201 = S.Task('C201', length=1, delay_cost=1)
	S += C201 >= 28
	C201 += ADD[1]

	C20_0_mem0 = S.Task('C20_0_mem0', length=1, delay_cost=1)
	S += C20_0_mem0 >= 28
	C20_0_mem0 += ADD_mem[0]

	C20_0_mem1 = S.Task('C20_0_mem1', length=1, delay_cost=1)
	S += C20_0_mem1 >= 28
	C20_0_mem1 += ADD_mem[2]

	T1_1T0_mem0 = S.Task('T1_1T0_mem0', length=1, delay_cost=1)
	S += T1_1T0_mem0 >= 28
	T1_1T0_mem0 += ADD_mem[3]

	T1_1T0_mem1 = S.Task('T1_1T0_mem1', length=1, delay_cost=1)
	S += T1_1T0_mem1 >= 28
	T1_1T0_mem1 += ADD_mem[1]

	T2_0_in = S.Task('T2_0_in', length=1, delay_cost=1)
	S += T2_0_in >= 28
	T2_0_in += MUL_in[0]

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	S += T2_0_mem0 >= 28
	T2_0_mem0 += ADD_mem[2]

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	S += T2_0_mem1 >= 28
	T2_0_mem1 += ADD_mem[0]

	T2_T0 = S.Task('T2_T0', length=1, delay_cost=1)
	S += T2_T0 >= 28
	T2_T0 += ADD[2]

	T2_T2 = S.Task('T2_T2', length=7, delay_cost=1)
	S += T2_T2 >= 28
	T2_T2 += MUL[0]

	C01_1 = S.Task('C01_1', length=1, delay_cost=1)
	S += C01_1 >= 29
	C01_1 += ADD[3]

	C01_11_mem0 = S.Task('C01_11_mem0', length=1, delay_cost=1)
	S += C01_11_mem0 >= 29
	C01_11_mem0 += ADD_mem[3]

	C01_11_mem1 = S.Task('C01_11_mem1', length=1, delay_cost=1)
	S += C01_11_mem1 >= 29
	C01_11_mem1 += INPUT_mem_r

	C110_mem0 = S.Task('C110_mem0', length=1, delay_cost=1)
	S += C110_mem0 >= 29
	C110_mem0 += MUL_mem[0]

	C110_mem1 = S.Task('C110_mem1', length=1, delay_cost=1)
	S += C110_mem1 >= 29
	C110_mem1 += MUL_mem[0]

	C20_0 = S.Task('C20_0', length=1, delay_cost=1)
	S += C20_0 >= 29
	C20_0 += ADD[2]

	C20_1_mem0 = S.Task('C20_1_mem0', length=1, delay_cost=1)
	S += C20_1_mem0 >= 29
	C20_1_mem0 += ADD_mem[1]

	C20_1_mem1 = S.Task('C20_1_mem1', length=1, delay_cost=1)
	S += C20_1_mem1 >= 29
	C20_1_mem1 += ADD_mem[1]

	T1_10_in = S.Task('T1_10_in', length=1, delay_cost=1)
	S += T1_10_in >= 29
	T1_10_in += MUL_in[0]

	T1_10_mem0 = S.Task('T1_10_mem0', length=1, delay_cost=1)
	S += T1_10_mem0 >= 29
	T1_10_mem0 += ADD_mem[0]

	T1_10_mem1 = S.Task('T1_10_mem1', length=1, delay_cost=1)
	S += T1_10_mem1 >= 29
	T1_10_mem1 += ADD_mem[3]

	T1_1T0 = S.Task('T1_1T0', length=1, delay_cost=1)
	S += T1_1T0 >= 29
	T1_1T0 += ADD[0]

	T2_0 = S.Task('T2_0', length=7, delay_cost=1)
	S += T2_0 >= 29
	T2_0 += MUL[0]

	C00_0_mem0 = S.Task('C00_0_mem0', length=1, delay_cost=1)
	S += C00_0_mem0 >= 30
	C00_0_mem0 += MUL_mem[0]

	C00_0_mem1 = S.Task('C00_0_mem1', length=1, delay_cost=1)
	S += C00_0_mem1 >= 30
	C00_0_mem1 += ADD_mem[3]

	C01_11 = S.Task('C01_11', length=1, delay_cost=1)
	S += C01_11 >= 30
	C01_11 += ADD[3]

	C10_10_mem0 = S.Task('C10_10_mem0', length=1, delay_cost=1)
	S += C10_10_mem0 >= 30
	C10_10_mem0 += ADD_mem[0]

	C10_10_mem1 = S.Task('C10_10_mem1', length=1, delay_cost=1)
	S += C10_10_mem1 >= 30
	C10_10_mem1 += ADD_mem[2]

	C10_11_mem0 = S.Task('C10_11_mem0', length=1, delay_cost=1)
	S += C10_11_mem0 >= 30
	C10_11_mem0 += ADD_mem[0]

	C10_11_mem1 = S.Task('C10_11_mem1', length=1, delay_cost=1)
	S += C10_11_mem1 >= 30
	C10_11_mem1 += ADD_mem[2]

	C110 = S.Task('C110', length=1, delay_cost=1)
	S += C110 >= 30
	C110 += ADD[0]

	C20_1 = S.Task('C20_1', length=1, delay_cost=1)
	S += C20_1 >= 30
	C20_1 += ADD[1]

	C21_11_mem0 = S.Task('C21_11_mem0', length=1, delay_cost=1)
	S += C21_11_mem0 >= 30
	C21_11_mem0 += ADD_mem[3]

	C21_11_mem1 = S.Task('C21_11_mem1', length=1, delay_cost=1)
	S += C21_11_mem1 >= 30
	C21_11_mem1 += INPUT_mem_r

	T1_10 = S.Task('T1_10', length=7, delay_cost=1)
	S += T1_10 >= 30
	T1_10 += MUL[0]

	C00_0 = S.Task('C00_0', length=1, delay_cost=1)
	S += C00_0 >= 31
	C00_0 += ADD[3]

	C10_10 = S.Task('C10_10', length=1, delay_cost=1)
	S += C10_10 >= 31
	C10_10 += ADD[1]

	C10_11 = S.Task('C10_11', length=1, delay_cost=1)
	S += C10_11 >= 31
	C10_11 += ADD[2]

	C10_20_mem0 = S.Task('C10_20_mem0', length=1, delay_cost=1)
	S += C10_20_mem0 >= 31
	C10_20_mem0 += ADD_mem[1]

	C10_20_mem1 = S.Task('C10_20_mem1', length=1, delay_cost=1)
	S += C10_20_mem1 >= 31
	C10_20_mem1 += INPUT_mem_r

	C10_21_mem0 = S.Task('C10_21_mem0', length=1, delay_cost=1)
	S += C10_21_mem0 >= 31
	C10_21_mem0 += ADD_mem[2]

	C10_21_mem1 = S.Task('C10_21_mem1', length=1, delay_cost=1)
	S += C10_21_mem1 >= 31
	C10_21_mem1 += INPUT_mem_r

	C21_11 = S.Task('C21_11', length=1, delay_cost=1)
	S += C21_11 >= 31
	C21_11 += ADD[0]

	C10_20 = S.Task('C10_20', length=1, delay_cost=1)
	S += C10_20 >= 32
	C10_20 += ADD[2]

	C10_21 = S.Task('C10_21', length=1, delay_cost=1)
	S += C10_21 >= 32
	C10_21 += ADD[0]

	C00_20_mem0 = S.Task('C00_20_mem0', length=1, delay_cost=1)
	S += C00_20_mem0 >= 33
	C00_20_mem0 += ADD_mem[2]

	C00_20_mem1 = S.Task('C00_20_mem1', length=1, delay_cost=1)
	S += C00_20_mem1 >= 33
	C00_20_mem1 += INPUT_mem_r

	C00_20 = S.Task('C00_20', length=1, delay_cost=1)
	S += C00_20 >= 34
	C00_20 += ADD[3]

	C00_20_w = S.Task('C00_20_w', length=1, delay_cost=1)
	S += C00_20_w >= 34
	C00_20_w += INPUT_mem_w

	C11_11_mem0 = S.Task('C11_11_mem0', length=1, delay_cost=1)
	S += C11_11_mem0 >= 34
	C11_11_mem0 += ADD_mem[0]

	C11_11_mem1 = S.Task('C11_11_mem1', length=1, delay_cost=1)
	S += C11_11_mem1 >= 34
	C11_11_mem1 += ADD_mem[0]

	C20_21_mem0 = S.Task('C20_21_mem0', length=1, delay_cost=1)
	S += C20_21_mem0 >= 34
	C20_21_mem0 += ADD_mem[3]

	C20_21_mem1 = S.Task('C20_21_mem1', length=1, delay_cost=1)
	S += C20_21_mem1 >= 34
	C20_21_mem1 += ADD_mem[1]

	C11_11 = S.Task('C11_11', length=1, delay_cost=1)
	S += C11_11 >= 35
	C11_11 += ADD[2]

	C11_21_mem0 = S.Task('C11_21_mem0', length=1, delay_cost=1)
	S += C11_21_mem0 >= 35
	C11_21_mem0 += ADD_mem[2]

	C11_21_mem1 = S.Task('C11_21_mem1', length=1, delay_cost=1)
	S += C11_21_mem1 >= 35
	C11_21_mem1 += ADD_mem[3]

	C20_21 = S.Task('C20_21', length=1, delay_cost=1)
	S += C20_21 >= 35
	C20_21 += ADD[0]

	C20_31_mem0 = S.Task('C20_31_mem0', length=1, delay_cost=1)
	S += C20_31_mem0 >= 35
	C20_31_mem0 += ADD_mem[0]

	C20_31_mem1 = S.Task('C20_31_mem1', length=1, delay_cost=1)
	S += C20_31_mem1 >= 35
	C20_31_mem1 += ADD_mem[3]

	C11_10_mem0 = S.Task('C11_10_mem0', length=1, delay_cost=1)
	S += C11_10_mem0 >= 36
	C11_10_mem0 += MUL_mem[0]

	C11_10_mem1 = S.Task('C11_10_mem1', length=1, delay_cost=1)
	S += C11_10_mem1 >= 36
	C11_10_mem1 += ADD_mem[0]

	C11_21 = S.Task('C11_21', length=1, delay_cost=1)
	S += C11_21 >= 36
	C11_21 += ADD[1]

	C11_21_w = S.Task('C11_21_w', length=1, delay_cost=1)
	S += C11_21_w >= 36
	C11_21_w += INPUT_mem_w

	C20_20_mem0 = S.Task('C20_20_mem0', length=1, delay_cost=1)
	S += C20_20_mem0 >= 36
	C20_20_mem0 += ADD_mem[1]

	C20_20_mem1 = S.Task('C20_20_mem1', length=1, delay_cost=1)
	S += C20_20_mem1 >= 36
	C20_20_mem1 += MUL_mem[0]

	C20_31 = S.Task('C20_31', length=1, delay_cost=1)
	S += C20_31 >= 36
	C20_31 += ADD[0]

	C20_31_w = S.Task('C20_31_w', length=1, delay_cost=1)
	S += C20_31_w >= 36
	C20_31_w += INPUT_mem_w

	C11_10 = S.Task('C11_10', length=1, delay_cost=1)
	S += C11_10 >= 37
	C11_10 += ADD[0]

	C11_20_mem0 = S.Task('C11_20_mem0', length=1, delay_cost=1)
	S += C11_20_mem0 >= 37
	C11_20_mem0 += ADD_mem[0]

	C11_20_mem1 = S.Task('C11_20_mem1', length=1, delay_cost=1)
	S += C11_20_mem1 >= 37
	C11_20_mem1 += MUL_mem[0]

	C20_20 = S.Task('C20_20', length=1, delay_cost=1)
	S += C20_20 >= 37
	C20_20 += ADD[2]

	C20_30_mem0 = S.Task('C20_30_mem0', length=1, delay_cost=1)
	S += C20_30_mem0 >= 37
	C20_30_mem0 += ADD_mem[2]

	C20_30_mem1 = S.Task('C20_30_mem1', length=1, delay_cost=1)
	S += C20_30_mem1 >= 37
	C20_30_mem1 += MUL_mem[0]

	C11_20 = S.Task('C11_20', length=1, delay_cost=1)
	S += C11_20 >= 38
	C11_20 += ADD[1]

	C11_20_w = S.Task('C11_20_w', length=1, delay_cost=1)
	S += C11_20_w >= 38
	C11_20_w += INPUT_mem_w

	C20_30 = S.Task('C20_30', length=1, delay_cost=1)
	S += C20_30 >= 38
	C20_30 += ADD[0]

	C20_30_w = S.Task('C20_30_w', length=1, delay_cost=1)
	S += C20_30_w >= 38
	C20_30_w += INPUT_mem_w


	# new tasks
	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += MUL_mem[0]
	S += 7<T01_mem0
	S += T01_mem0<=T01

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	T01_mem1 += MUL_mem[0]
	S += 7<T01_mem1
	S += T01_mem1<=T01

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += MUL_mem[0]
	S += 8<T41_mem0
	S += T41_mem0<=T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += MUL_mem[0]
	S += 8<T41_mem1
	S += T41_mem1<=T41

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	T3_0 += alt(ADD)

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	T3_0_mem0 += ADD_mem[2]
	S += 11<T3_0_mem0
	S += T3_0_mem0<=T3_0

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	T3_0_mem1 += ADD_mem[2]
	S += 11<T3_0_mem1
	S += T3_0_mem1<=T3_0

	C010 = S.Task('C010', length=1, delay_cost=1)
	C010 += alt(ADD)

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	C010_mem0 += ADD_mem[2]
	S += 13<C010_mem0
	S += C010_mem0<=C010

	C010_mem1 = S.Task('C010_mem1', length=1, delay_cost=1)
	C010_mem1 += ADD_mem[2]
	S += 13<C010_mem1
	S += C010_mem1<=C010

	C100 = S.Task('C100', length=1, delay_cost=1)
	C100 += alt(ADD)

	C100_mem0 = S.Task('C100_mem0', length=1, delay_cost=1)
	C100_mem0 += ADD_mem[2]
	S += 17<C100_mem0
	S += C100_mem0<=C100

	C100_mem1 = S.Task('C100_mem1', length=1, delay_cost=1)
	C100_mem1 += ADD_mem[2]
	S += 17<C100_mem1
	S += C100_mem1<=C100

	C210 = S.Task('C210', length=1, delay_cost=1)
	C210 += alt(ADD)

	C210_mem0 = S.Task('C210_mem0', length=1, delay_cost=1)
	C210_mem0 += ADD_mem[3]
	S += 16<C210_mem0
	S += C210_mem0<=C210

	C210_mem1 = S.Task('C210_mem1', length=1, delay_cost=1)
	C210_mem1 += ADD_mem[3]
	S += 16<C210_mem1
	S += C210_mem1<=C210

	T1_11 = S.Task('T1_11', length=1, delay_cost=1)
	T1_11 += alt(ADD)

	T1_11_mem0 = S.Task('T1_11_mem0', length=1, delay_cost=1)
	T1_11_mem0 += MUL_mem[0]
	S += 33<T1_11_mem0
	S += T1_11_mem0<=T1_11

	T1_11_mem1 = S.Task('T1_11_mem1', length=1, delay_cost=1)
	T1_11_mem1 += MUL_mem[0]
	S += 33<T1_11_mem1
	S += T1_11_mem1<=T1_11

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	T2_1 += alt(ADD)

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	T2_1_mem0 += MUL_mem[0]
	S += 34<T2_1_mem0
	S += T2_1_mem0<=T2_1

	T2_1_mem1 = S.Task('T2_1_mem1', length=1, delay_cost=1)
	T2_1_mem1 += MUL_mem[0]
	S += 34<T2_1_mem1
	S += T2_1_mem1<=T2_1

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	T3_1 += alt(ADD)

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	T3_1_mem0 += ADD_mem[2]
	S += 20<T3_1_mem0
	S += T3_1_mem0<=T3_1

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	T3_1_mem1 += ADD_mem[2]
	S += 20<T3_1_mem1
	S += T3_1_mem1<=T3_1

	C011 = S.Task('C011', length=1, delay_cost=1)
	C011 += alt(ADD)

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	C011_mem0 += ADD_mem[1]
	S += 26<C011_mem0
	S += C011_mem0<=C011

	C011_mem1 = S.Task('C011_mem1', length=1, delay_cost=1)
	C011_mem1 += ADD_mem[1]
	S += 26<C011_mem1
	S += C011_mem1<=C011

	C101 = S.Task('C101', length=1, delay_cost=1)
	C101 += alt(ADD)

	C101_mem0 = S.Task('C101_mem0', length=1, delay_cost=1)
	C101_mem0 += ADD_mem[0]
	S += 24<C101_mem0
	S += C101_mem0<=C101

	C101_mem1 = S.Task('C101_mem1', length=1, delay_cost=1)
	C101_mem1 += ADD_mem[0]
	S += 24<C101_mem1
	S += C101_mem1<=C101

	C11_0 = S.Task('C11_0', length=1, delay_cost=1)
	C11_0 += alt(ADD)

	C11_0_mem0 = S.Task('C11_0_mem0', length=1, delay_cost=1)
	C11_0_mem0 += ADD_mem[0]
	S += 30<C11_0_mem0
	S += C11_0_mem0<=C11_0

	C11_0_mem1 = S.Task('C11_0_mem1', length=1, delay_cost=1)
	C11_0_mem1 += ADD_mem[0]
	S += 30<C11_0_mem1
	S += C11_0_mem1<=C11_0

	C11_1 = S.Task('C11_1', length=1, delay_cost=1)
	C11_1 += alt(ADD)

	C11_1_mem0 = S.Task('C11_1_mem0', length=1, delay_cost=1)
	C11_1_mem0 += ADD_mem[0]
	S += 10<C11_1_mem0
	S += C11_1_mem0<=C11_1

	C11_1_mem1 = S.Task('C11_1_mem1', length=1, delay_cost=1)
	C11_1_mem1 += ADD_mem[0]
	S += 10<C11_1_mem1
	S += C11_1_mem1<=C11_1

	C211 = S.Task('C211', length=1, delay_cost=1)
	C211 += alt(ADD)

	C211_mem0 = S.Task('C211_mem0', length=1, delay_cost=1)
	C211_mem0 += ADD_mem[0]
	S += 22<C211_mem0
	S += C211_mem0<=C211

	C211_mem1 = S.Task('C211_mem1', length=1, delay_cost=1)
	C211_mem1 += ADD_mem[0]
	S += 22<C211_mem1
	S += C211_mem1<=C211

	C20_10 = S.Task('C20_10', length=1, delay_cost=1)
	C20_10 += alt(ADD)

	C20_10_mem0 = S.Task('C20_10_mem0', length=1, delay_cost=1)
	C20_10_mem0 += ADD_mem[2]
	S += 29<C20_10_mem0
	S += C20_10_mem0<=C20_10

	C20_10_mem1 = S.Task('C20_10_mem1', length=1, delay_cost=1)
	C20_10_mem1 += ADD_mem[2]
	S += 29<C20_10_mem1
	S += C20_10_mem1<=C20_10

	C20_11 = S.Task('C20_11', length=1, delay_cost=1)
	C20_11 += alt(ADD)

	C20_11_mem0 = S.Task('C20_11_mem0', length=1, delay_cost=1)
	C20_11_mem0 += ADD_mem[1]
	S += 30<C20_11_mem0
	S += C20_11_mem0<=C20_11

	C20_11_mem1 = S.Task('C20_11_mem1', length=1, delay_cost=1)
	C20_11_mem1 += ADD_mem[1]
	S += 30<C20_11_mem1
	S += C20_11_mem1<=C20_11

	C00_10 = S.Task('C00_10', length=1, delay_cost=1)
	C00_10 += alt(ADD)

	C00_10_mem0 = S.Task('C00_10_mem0', length=1, delay_cost=1)
	C00_10_mem0 += ADD_mem[3]
	S += 31<C00_10_mem0
	S += C00_10_mem0<=C00_10

	C00_10_mem1 = S.Task('C00_10_mem1', length=1, delay_cost=1)
	C00_10_mem1 += ADD_mem[3]
	S += 31<C00_10_mem1
	S += C00_10_mem1<=C00_10

	C01_20 = S.Task('C01_20', length=1, delay_cost=1)
	C01_20 += alt(ADD)

	C01_20_mem0 = S.Task('C01_20_mem0', length=1, delay_cost=1)
	C01_20_mem0 += ADD_mem[1]
	S += 27<C01_20_mem0
	S += C01_20_mem0<=C01_20

	C01_20_mem1 = S.Task('C01_20_mem1', length=1, delay_cost=1)
	C01_20_mem1 += ADD_mem[1]
	S += 27<C01_20_mem1
	S += C01_20_mem1<=C01_20

	C01_20_w = S.Task('C01_20_w', length=1, delay_cost=1)
	C01_20_w += alt(INPUT_mem_w)
	S += 0 < C01_20_w
	S += C01_20-1 <= C01_20_w

	C21_20 = S.Task('C21_20', length=1, delay_cost=1)
	C21_20 += alt(ADD)

	C21_20_mem0 = S.Task('C21_20_mem0', length=1, delay_cost=1)
	C21_20_mem0 += ADD_mem[2]
	S += 27<C21_20_mem0
	S += C21_20_mem0<=C21_20

	C21_20_mem1 = S.Task('C21_20_mem1', length=1, delay_cost=1)
	C21_20_mem1 += ADD_mem[2]
	S += 27<C21_20_mem1
	S += C21_20_mem1<=C21_20

	C21_20_w = S.Task('C21_20_w', length=1, delay_cost=1)
	C21_20_w += alt(INPUT_mem_w)
	S += 0 < C21_20_w
	S += C21_20-1 <= C21_20_w

	C00_11 = S.Task('C00_11', length=1, delay_cost=1)
	C00_11 += alt(ADD)

	C00_11_mem0 = S.Task('C00_11_mem0', length=1, delay_cost=1)
	C00_11_mem0 += ADD_mem[2]
	S += 23<C00_11_mem0
	S += C00_11_mem0<=C00_11

	C00_11_mem1 = S.Task('C00_11_mem1', length=1, delay_cost=1)
	C00_11_mem1 += ADD_mem[2]
	S += 23<C00_11_mem1
	S += C00_11_mem1<=C00_11

	C00_11_w = S.Task('C00_11_w', length=1, delay_cost=1)
	C00_11_w += alt(INPUT_mem_w)
	S += 0 < C00_11_w
	S += C00_11-1 <= C00_11_w

	C01_21 = S.Task('C01_21', length=1, delay_cost=1)
	C01_21 += alt(ADD)

	C01_21_mem0 = S.Task('C01_21_mem0', length=1, delay_cost=1)
	C01_21_mem0 += ADD_mem[3]
	S += 30<C01_21_mem0
	S += C01_21_mem0<=C01_21

	C01_21_mem1 = S.Task('C01_21_mem1', length=1, delay_cost=1)
	C01_21_mem1 += ADD_mem[3]
	S += 30<C01_21_mem1
	S += C01_21_mem1<=C01_21

	C01_21_w = S.Task('C01_21_w', length=1, delay_cost=1)
	C01_21_w += alt(INPUT_mem_w)
	S += 0 < C01_21_w
	S += C01_21-1 <= C01_21_w

	C21_21 = S.Task('C21_21', length=1, delay_cost=1)
	C21_21 += alt(ADD)

	C21_21_mem0 = S.Task('C21_21_mem0', length=1, delay_cost=1)
	C21_21_mem0 += ADD_mem[0]
	S += 31<C21_21_mem0
	S += C21_21_mem0<=C21_21

	C21_21_mem1 = S.Task('C21_21_mem1', length=1, delay_cost=1)
	C21_21_mem1 += ADD_mem[0]
	S += 31<C21_21_mem1
	S += C21_21_mem1<=C21_21

	C21_21_w = S.Task('C21_21_w', length=1, delay_cost=1)
	C21_21_w += alt(INPUT_mem_w)
	S += 0 < C21_21_w
	S += C21_21-1 <= C21_21_w

	C10_30 = S.Task('C10_30', length=1, delay_cost=1)
	C10_30 += alt(ADD)

	C10_30_mem0 = S.Task('C10_30_mem0', length=1, delay_cost=1)
	C10_30_mem0 += ADD_mem[2]
	S += 32<C10_30_mem0
	S += C10_30_mem0<=C10_30

	C10_30_mem1 = S.Task('C10_30_mem1', length=1, delay_cost=1)
	C10_30_mem1 += ADD_mem[2]
	S += 32<C10_30_mem1
	S += C10_30_mem1<=C10_30

	C10_30_w = S.Task('C10_30_w', length=1, delay_cost=1)
	C10_30_w += alt(INPUT_mem_w)
	S += 0 < C10_30_w
	S += C10_30-1 <= C10_30_w

	C10_31 = S.Task('C10_31', length=1, delay_cost=1)
	C10_31 += alt(ADD)

	C10_31_mem0 = S.Task('C10_31_mem0', length=1, delay_cost=1)
	C10_31_mem0 += ADD_mem[0]
	S += 32<C10_31_mem0
	S += C10_31_mem0<=C10_31

	C10_31_mem1 = S.Task('C10_31_mem1', length=1, delay_cost=1)
	C10_31_mem1 += ADD_mem[0]
	S += 32<C10_31_mem1
	S += C10_31_mem1<=C10_31

	C10_31_w = S.Task('C10_31_w', length=1, delay_cost=1)
	C10_31_w += alt(INPUT_mem_w)
	S += 0 < C10_31_w
	S += C10_31-1 <= C10_31_w

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "SQR012345_mul1_add4/SQR012345_mul1_add4_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_SQR012345_mul1_add4_3(0, 0)