from pyschedule import Scenario, solvers, plotters, alt

def solve_sparse_mul1_add4_3(ConstStep, ExpStep):
	horizon = 154
	S=Scenario("sparse_mul1_add4_3",horizon = horizon)

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
	T6_1T0_in = S.Task('T6_1T0_in', length=1, delay_cost=1)
	S += T6_1T0_in >= 0
	T6_1T0_in += MUL_in[0]

	T6_1T0_mem0 = S.Task('T6_1T0_mem0', length=1, delay_cost=1)
	S += T6_1T0_mem0 >= 0
	T6_1T0_mem0 += INPUT_mem_r

	T6_1T0_mem1 = S.Task('T6_1T0_mem1', length=1, delay_cost=1)
	S += T6_1T0_mem1 >= 0
	T6_1T0_mem1 += INPUT_mem_r

	T6_1T0 = S.Task('T6_1T0', length=7, delay_cost=1)
	S += T6_1T0 >= 1
	T6_1T0 += MUL[0]

	T6_1T1_in = S.Task('T6_1T1_in', length=1, delay_cost=1)
	S += T6_1T1_in >= 1
	T6_1T1_in += MUL_in[0]

	T6_1T1_mem0 = S.Task('T6_1T1_mem0', length=1, delay_cost=1)
	S += T6_1T1_mem0 >= 1
	T6_1T1_mem0 += INPUT_mem_r

	T6_1T1_mem1 = S.Task('T6_1T1_mem1', length=1, delay_cost=1)
	S += T6_1T1_mem1 >= 1
	T6_1T1_mem1 += INPUT_mem_r

	T4T1_in = S.Task('T4T1_in', length=1, delay_cost=1)
	S += T4T1_in >= 2
	T4T1_in += MUL_in[0]

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	S += T4T1_mem0 >= 2
	T4T1_mem0 += INPUT_mem_r

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	S += T4T1_mem1 >= 2
	T4T1_mem1 += INPUT_mem_r

	T6_1T1 = S.Task('T6_1T1', length=7, delay_cost=1)
	S += T6_1T1 >= 2
	T6_1T1 += MUL[0]

	T3T1_in = S.Task('T3T1_in', length=1, delay_cost=1)
	S += T3T1_in >= 3
	T3T1_in += MUL_in[0]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 3
	T3T1_mem0 += INPUT_mem_r

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 3
	T3T1_mem1 += INPUT_mem_r

	T4T1 = S.Task('T4T1', length=7, delay_cost=1)
	S += T4T1 >= 3
	T4T1 += MUL[0]

	T3T0_in = S.Task('T3T0_in', length=1, delay_cost=1)
	S += T3T0_in >= 4
	T3T0_in += MUL_in[0]

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 4
	T3T0_mem0 += INPUT_mem_r

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 4
	T3T0_mem1 += INPUT_mem_r

	T3T1 = S.Task('T3T1', length=7, delay_cost=1)
	S += T3T1 >= 4
	T3T1 += MUL[0]

	T2T1_in = S.Task('T2T1_in', length=1, delay_cost=1)
	S += T2T1_in >= 5
	T2T1_in += MUL_in[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 5
	T2T1_mem0 += INPUT_mem_r

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 5
	T2T1_mem1 += INPUT_mem_r

	T3T0 = S.Task('T3T0', length=7, delay_cost=1)
	S += T3T0 >= 5
	T3T0 += MUL[0]

	T1T1_in = S.Task('T1T1_in', length=1, delay_cost=1)
	S += T1T1_in >= 6
	T1T1_in += MUL_in[0]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 6
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 6
	T1T1_mem1 += INPUT_mem_r

	T2T1 = S.Task('T2T1', length=7, delay_cost=1)
	S += T2T1 >= 6
	T2T1 += MUL[0]

	T1T0_in = S.Task('T1T0_in', length=1, delay_cost=1)
	S += T1T0_in >= 7
	T1T0_in += MUL_in[0]

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 7
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 7
	T1T0_mem1 += INPUT_mem_r

	T1T1 = S.Task('T1T1', length=7, delay_cost=1)
	S += T1T1 >= 7
	T1T1 += MUL[0]

	T0T1_in = S.Task('T0T1_in', length=1, delay_cost=1)
	S += T0T1_in >= 8
	T0T1_in += MUL_in[0]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 8
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 8
	T0T1_mem1 += INPUT_mem_r

	T1T0 = S.Task('T1T0', length=7, delay_cost=1)
	S += T1T0 >= 8
	T1T0 += MUL[0]

	T0T1 = S.Task('T0T1', length=7, delay_cost=1)
	S += T0T1 >= 9
	T0T1 += MUL[0]

	T5T1_in = S.Task('T5T1_in', length=1, delay_cost=1)
	S += T5T1_in >= 9
	T5T1_in += MUL_in[0]

	T5T1_mem0 = S.Task('T5T1_mem0', length=1, delay_cost=1)
	S += T5T1_mem0 >= 9
	T5T1_mem0 += INPUT_mem_r

	T5T1_mem1 = S.Task('T5T1_mem1', length=1, delay_cost=1)
	S += T5T1_mem1 >= 9
	T5T1_mem1 += INPUT_mem_r

	T6_1T5_mem0 = S.Task('T6_1T5_mem0', length=1, delay_cost=1)
	S += T6_1T5_mem0 >= 9
	T6_1T5_mem0 += MUL_mem[0]

	T6_1T5_mem1 = S.Task('T6_1T5_mem1', length=1, delay_cost=1)
	S += T6_1T5_mem1 >= 9
	T6_1T5_mem1 += MUL_mem[0]

	T5T0_in = S.Task('T5T0_in', length=1, delay_cost=1)
	S += T5T0_in >= 10
	T5T0_in += MUL_in[0]

	T5T0_mem0 = S.Task('T5T0_mem0', length=1, delay_cost=1)
	S += T5T0_mem0 >= 10
	T5T0_mem0 += INPUT_mem_r

	T5T0_mem1 = S.Task('T5T0_mem1', length=1, delay_cost=1)
	S += T5T0_mem1 >= 10
	T5T0_mem1 += INPUT_mem_r

	T5T1 = S.Task('T5T1', length=7, delay_cost=1)
	S += T5T1 >= 10
	T5T1 += MUL[0]

	T6_10_mem0 = S.Task('T6_10_mem0', length=1, delay_cost=1)
	S += T6_10_mem0 >= 10
	T6_10_mem0 += MUL_mem[0]

	T6_10_mem1 = S.Task('T6_10_mem1', length=1, delay_cost=1)
	S += T6_10_mem1 >= 10
	T6_10_mem1 += MUL_mem[0]

	T6_1T5 = S.Task('T6_1T5', length=1, delay_cost=1)
	S += T6_1T5 >= 10
	T6_1T5 += ADD[1]

	T4T0_in = S.Task('T4T0_in', length=1, delay_cost=1)
	S += T4T0_in >= 11
	T4T0_in += MUL_in[0]

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	S += T4T0_mem0 >= 11
	T4T0_mem0 += INPUT_mem_r

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	S += T4T0_mem1 >= 11
	T4T0_mem1 += INPUT_mem_r

	T5T0 = S.Task('T5T0', length=7, delay_cost=1)
	S += T5T0 >= 11
	T5T0 += MUL[0]

	T6_10 = S.Task('T6_10', length=1, delay_cost=1)
	S += T6_10 >= 11
	T6_10 += ADD[0]

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	S += T2T0_in >= 12
	T2T0_in += MUL_in[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 12
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 12
	T2T0_mem1 += INPUT_mem_r

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 12
	T30_mem0 += MUL_mem[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 12
	T30_mem1 += MUL_mem[0]

	T4T0 = S.Task('T4T0', length=7, delay_cost=1)
	S += T4T0 >= 12
	T4T0 += MUL[0]

	T0T0_in = S.Task('T0T0_in', length=1, delay_cost=1)
	S += T0T0_in >= 13
	T0T0_in += MUL_in[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 13
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 13
	T0T0_mem1 += INPUT_mem_r

	T2T0 = S.Task('T2T0', length=7, delay_cost=1)
	S += T2T0 >= 13
	T2T0 += MUL[0]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 13
	T30 += ADD[3]

	T3T5_mem0 = S.Task('T3T5_mem0', length=1, delay_cost=1)
	S += T3T5_mem0 >= 13
	T3T5_mem0 += MUL_mem[0]

	T3T5_mem1 = S.Task('T3T5_mem1', length=1, delay_cost=1)
	S += T3T5_mem1 >= 13
	T3T5_mem1 += MUL_mem[0]

	T0T0 = S.Task('T0T0', length=7, delay_cost=1)
	S += T0T0 >= 14
	T0T0 += MUL[0]

	T3T5 = S.Task('T3T5', length=1, delay_cost=1)
	S += T3T5 >= 14
	T3T5 += ADD[1]

	T9_1T2_mem0 = S.Task('T9_1T2_mem0', length=1, delay_cost=1)
	S += T9_1T2_mem0 >= 14
	T9_1T2_mem0 += INPUT_mem_r

	T9_1T2_mem1 = S.Task('T9_1T2_mem1', length=1, delay_cost=1)
	S += T9_1T2_mem1 >= 14
	T9_1T2_mem1 += INPUT_mem_r

	T0T3_mem0 = S.Task('T0T3_mem0', length=1, delay_cost=1)
	S += T0T3_mem0 >= 15
	T0T3_mem0 += INPUT_mem_r

	T0T3_mem1 = S.Task('T0T3_mem1', length=1, delay_cost=1)
	S += T0T3_mem1 >= 15
	T0T3_mem1 += INPUT_mem_r

	T1T5_mem0 = S.Task('T1T5_mem0', length=1, delay_cost=1)
	S += T1T5_mem0 >= 15
	T1T5_mem0 += MUL_mem[0]

	T1T5_mem1 = S.Task('T1T5_mem1', length=1, delay_cost=1)
	S += T1T5_mem1 >= 15
	T1T5_mem1 += MUL_mem[0]

	T9_1T2 = S.Task('T9_1T2', length=1, delay_cost=1)
	S += T9_1T2 >= 15
	T9_1T2 += ADD[3]

	T0T3 = S.Task('T0T3', length=1, delay_cost=1)
	S += T0T3 >= 16
	T0T3 += ADD[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 16
	T10_mem0 += MUL_mem[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 16
	T10_mem1 += MUL_mem[0]

	T1T5 = S.Task('T1T5', length=1, delay_cost=1)
	S += T1T5 >= 16
	T1T5 += ADD[3]

	T3T3_mem0 = S.Task('T3T3_mem0', length=1, delay_cost=1)
	S += T3T3_mem0 >= 16
	T3T3_mem0 += INPUT_mem_r

	T3T3_mem1 = S.Task('T3T3_mem1', length=1, delay_cost=1)
	S += T3T3_mem1 >= 16
	T3T3_mem1 += INPUT_mem_r

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 17
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 17
	T0T2_mem1 += INPUT_mem_r

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 17
	T10 += ADD[1]

	T3T3 = S.Task('T3T3', length=1, delay_cost=1)
	S += T3T3 >= 17
	T3T3 += ADD[0]

	T0T2 = S.Task('T0T2', length=1, delay_cost=1)
	S += T0T2 >= 18
	T0T2 += ADD[0]

	T2T3_mem0 = S.Task('T2T3_mem0', length=1, delay_cost=1)
	S += T2T3_mem0 >= 18
	T2T3_mem0 += INPUT_mem_r

	T2T3_mem1 = S.Task('T2T3_mem1', length=1, delay_cost=1)
	S += T2T3_mem1 >= 18
	T2T3_mem1 += INPUT_mem_r

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 18
	T50_mem0 += MUL_mem[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 18
	T50_mem1 += MUL_mem[0]

	T0T4_in = S.Task('T0T4_in', length=1, delay_cost=1)
	S += T0T4_in >= 19
	T0T4_in += MUL_in[0]

	T0T4_mem0 = S.Task('T0T4_mem0', length=1, delay_cost=1)
	S += T0T4_mem0 >= 19
	T0T4_mem0 += ADD_mem[0]

	T0T4_mem1 = S.Task('T0T4_mem1', length=1, delay_cost=1)
	S += T0T4_mem1 >= 19
	T0T4_mem1 += ADD_mem[0]

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	S += T2T3 >= 19
	T2T3 += ADD[0]

	T3_T2_mem0 = S.Task('T3_T2_mem0', length=1, delay_cost=1)
	S += T3_T2_mem0 >= 19
	T3_T2_mem0 += INPUT_mem_r

	T3_T2_mem1 = S.Task('T3_T2_mem1', length=1, delay_cost=1)
	S += T3_T2_mem1 >= 19
	T3_T2_mem1 += INPUT_mem_r

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 19
	T50 += ADD[2]

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	S += T5T5_mem0 >= 19
	T5T5_mem0 += MUL_mem[0]

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	S += T5T5_mem1 >= 19
	T5T5_mem1 += MUL_mem[0]

	T0T4 = S.Task('T0T4', length=7, delay_cost=1)
	S += T0T4 >= 20
	T0T4 += MUL[0]

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	S += T160_mem0 >= 20
	T160_mem0 += INPUT_mem_r

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	S += T160_mem1 >= 20
	T160_mem1 += INPUT_mem_r

	T2T5_mem0 = S.Task('T2T5_mem0', length=1, delay_cost=1)
	S += T2T5_mem0 >= 20
	T2T5_mem0 += MUL_mem[0]

	T2T5_mem1 = S.Task('T2T5_mem1', length=1, delay_cost=1)
	S += T2T5_mem1 >= 20
	T2T5_mem1 += MUL_mem[0]

	T3_T2 = S.Task('T3_T2', length=1, delay_cost=1)
	S += T3_T2 >= 20
	T3_T2 += ADD[0]

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	S += T5T5 >= 20
	T5T5 += ADD[2]

	T160 = S.Task('T160', length=1, delay_cost=1)
	S += T160 >= 21
	T160 += ADD[1]

	T2T5 = S.Task('T2T5', length=1, delay_cost=1)
	S += T2T5 >= 21
	T2T5 += ADD[0]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 21
	T3T2_mem0 += INPUT_mem_r

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 21
	T3T2_mem1 += INPUT_mem_r

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	S += T4T5_mem0 >= 21
	T4T5_mem0 += MUL_mem[0]

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	S += T4T5_mem1 >= 21
	T4T5_mem1 += MUL_mem[0]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 22
	T151_mem0 += INPUT_mem_r

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 22
	T151_mem1 += INPUT_mem_r

	T3T2 = S.Task('T3T2', length=1, delay_cost=1)
	S += T3T2 >= 22
	T3T2 += ADD[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 22
	T40_mem0 += MUL_mem[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 22
	T40_mem1 += MUL_mem[0]

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	S += T4T5 >= 22
	T4T5 += ADD[3]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 23
	T00_mem0 += MUL_mem[0]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 23
	T00_mem1 += MUL_mem[0]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 23
	T150_mem0 += INPUT_mem_r

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 23
	T150_mem1 += INPUT_mem_r

	T151 = S.Task('T151', length=1, delay_cost=1)
	S += T151 >= 23
	T151 += ADD[0]

	T3T4_in = S.Task('T3T4_in', length=1, delay_cost=1)
	S += T3T4_in >= 23
	T3T4_in += MUL_in[0]

	T3T4_mem0 = S.Task('T3T4_mem0', length=1, delay_cost=1)
	S += T3T4_mem0 >= 23
	T3T4_mem0 += ADD_mem[0]

	T3T4_mem1 = S.Task('T3T4_mem1', length=1, delay_cost=1)
	S += T3T4_mem1 >= 23
	T3T4_mem1 += ADD_mem[0]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 23
	T40 += ADD[1]

	T00 = S.Task('T00', length=1, delay_cost=1)
	S += T00 >= 24
	T00 += ADD[1]

	T150 = S.Task('T150', length=1, delay_cost=1)
	S += T150 >= 24
	T150 += ADD[0]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	S += T161_mem0 >= 24
	T161_mem0 += INPUT_mem_r

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	S += T161_mem1 >= 24
	T161_mem1 += INPUT_mem_r

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 24
	T20_mem0 += MUL_mem[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 24
	T20_mem1 += MUL_mem[0]

	T3T4 = S.Task('T3T4', length=7, delay_cost=1)
	S += T3T4 >= 24
	T3T4 += MUL[0]

	T6_20_mem0 = S.Task('T6_20_mem0', length=1, delay_cost=1)
	S += T6_20_mem0 >= 24
	T6_20_mem0 += ADD_mem[0]

	T6_20_mem1 = S.Task('T6_20_mem1', length=1, delay_cost=1)
	S += T6_20_mem1 >= 24
	T6_20_mem1 += ADD_mem[1]

	T7_0_mem0 = S.Task('T7_0_mem0', length=1, delay_cost=1)
	S += T7_0_mem0 >= 24
	T7_0_mem0 += ADD_mem[3]

	T7_0_mem1 = S.Task('T7_0_mem1', length=1, delay_cost=1)
	S += T7_0_mem1 >= 24
	T7_0_mem1 += ADD_mem[1]

	T0T5_mem0 = S.Task('T0T5_mem0', length=1, delay_cost=1)
	S += T0T5_mem0 >= 25
	T0T5_mem0 += MUL_mem[0]

	T0T5_mem1 = S.Task('T0T5_mem1', length=1, delay_cost=1)
	S += T0T5_mem1 >= 25
	T0T5_mem1 += MUL_mem[0]

	T161 = S.Task('T161', length=1, delay_cost=1)
	S += T161 >= 25
	T161 += ADD[1]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 25
	T20 += ADD[3]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 25
	T2T2_mem0 += INPUT_mem_r

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 25
	T2T2_mem1 += INPUT_mem_r

	T4_T3_mem0 = S.Task('T4_T3_mem0', length=1, delay_cost=1)
	S += T4_T3_mem0 >= 25
	T4_T3_mem0 += ADD_mem[0]

	T4_T3_mem1 = S.Task('T4_T3_mem1', length=1, delay_cost=1)
	S += T4_T3_mem1 >= 25
	T4_T3_mem1 += ADD_mem[0]

	T6_20 = S.Task('T6_20', length=1, delay_cost=1)
	S += T6_20 >= 25
	T6_20 += ADD[0]

	T7_0 = S.Task('T7_0', length=1, delay_cost=1)
	S += T7_0 >= 25
	T7_0 += ADD[2]

	T0T5 = S.Task('T0T5', length=1, delay_cost=1)
	S += T0T5 >= 26
	T0T5 += ADD[2]

	T13_0_mem0 = S.Task('T13_0_mem0', length=1, delay_cost=1)
	S += T13_0_mem0 >= 26
	T13_0_mem0 += ADD_mem[3]

	T13_0_mem1 = S.Task('T13_0_mem1', length=1, delay_cost=1)
	S += T13_0_mem1 >= 26
	T13_0_mem1 += ADD_mem[0]

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	S += T2T2 >= 26
	T2T2 += ADD[0]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 26
	T4T2_mem0 += INPUT_mem_r

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 26
	T4T2_mem1 += INPUT_mem_r

	T4_T3 = S.Task('T4_T3', length=1, delay_cost=1)
	S += T4_T3 >= 26
	T4_T3 += ADD[1]

	T9_1T3_mem0 = S.Task('T9_1T3_mem0', length=1, delay_cost=1)
	S += T9_1T3_mem0 >= 26
	T9_1T3_mem0 += ADD_mem[1]

	T9_1T3_mem1 = S.Task('T9_1T3_mem1', length=1, delay_cost=1)
	S += T9_1T3_mem1 >= 26
	T9_1T3_mem1 += ADD_mem[1]

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 27
	T01_mem0 += MUL_mem[0]

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	S += T01_mem1 >= 27
	T01_mem1 += ADD_mem[2]

	T13_0 = S.Task('T13_0', length=1, delay_cost=1)
	S += T13_0 >= 27
	T13_0 += ADD[2]

	T2T4_in = S.Task('T2T4_in', length=1, delay_cost=1)
	S += T2T4_in >= 27
	T2T4_in += MUL_in[0]

	T2T4_mem0 = S.Task('T2T4_mem0', length=1, delay_cost=1)
	S += T2T4_mem0 >= 27
	T2T4_mem0 += ADD_mem[0]

	T2T4_mem1 = S.Task('T2T4_mem1', length=1, delay_cost=1)
	S += T2T4_mem1 >= 27
	T2T4_mem1 += ADD_mem[0]

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	S += T4T2 >= 27
	T4T2 += ADD[1]

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	S += T4T3_mem0 >= 27
	T4T3_mem0 += INPUT_mem_r

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	S += T4T3_mem1 >= 27
	T4T3_mem1 += INPUT_mem_r

	T8T3_mem0 = S.Task('T8T3_mem0', length=1, delay_cost=1)
	S += T8T3_mem0 >= 27
	T8T3_mem0 += ADD_mem[1]

	T8T3_mem1 = S.Task('T8T3_mem1', length=1, delay_cost=1)
	S += T8T3_mem1 >= 27
	T8T3_mem1 += ADD_mem[1]

	T9_1T3 = S.Task('T9_1T3', length=1, delay_cost=1)
	S += T9_1T3 >= 27
	T9_1T3 += ADD[0]

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 28
	T01 += ADD[0]

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	S += T0_0_mem0 >= 28
	T0_0_mem0 += ADD_mem[1]

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	S += T0_0_mem1 >= 28
	T0_0_mem1 += ADD_mem[0]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 28
	T141_mem0 += INPUT_mem_r

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 28
	T141_mem1 += INPUT_mem_r

	T2T4 = S.Task('T2T4', length=7, delay_cost=1)
	S += T2T4 >= 28
	T2T4 += MUL[0]

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	S += T4T3 >= 28
	T4T3 += ADD[2]

	T8T3 = S.Task('T8T3', length=1, delay_cost=1)
	S += T8T3 >= 28
	T8T3 += ADD[1]

	T9_1T4_in = S.Task('T9_1T4_in', length=1, delay_cost=1)
	S += T9_1T4_in >= 28
	T9_1T4_in += MUL_in[0]

	T9_1T4_mem0 = S.Task('T9_1T4_mem0', length=1, delay_cost=1)
	S += T9_1T4_mem0 >= 28
	T9_1T4_mem0 += ADD_mem[3]

	T9_1T4_mem1 = S.Task('T9_1T4_mem1', length=1, delay_cost=1)
	S += T9_1T4_mem1 >= 28
	T9_1T4_mem1 += ADD_mem[0]

	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	S += T0_0 >= 29
	T0_0 += ADD[0]

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	S += T0_1_mem0 >= 29
	T0_1_mem0 += ADD_mem[1]

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	S += T0_1_mem1 >= 29
	T0_1_mem1 += ADD_mem[0]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 29
	T140_mem0 += INPUT_mem_r

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 29
	T140_mem1 += INPUT_mem_r

	T141 = S.Task('T141', length=1, delay_cost=1)
	S += T141 >= 29
	T141 += ADD[2]

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	S += T4T4_in >= 29
	T4T4_in += MUL_in[0]

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	S += T4T4_mem0 >= 29
	T4T4_mem0 += ADD_mem[1]

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	S += T4T4_mem1 >= 29
	T4T4_mem1 += ADD_mem[2]

	T9_1T4 = S.Task('T9_1T4', length=7, delay_cost=1)
	S += T9_1T4 >= 29
	T9_1T4 += MUL[0]

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	S += T0_1 >= 30
	T0_1 += ADD[3]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 30
	T101_mem0 += ADD_mem[2]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 30
	T101_mem1 += ADD_mem[0]

	T140 = S.Task('T140', length=1, delay_cost=1)
	S += T140 >= 30
	T140 += ADD[1]

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	S += T1T2_mem0 >= 30
	T1T2_mem0 += INPUT_mem_r

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	S += T1T2_mem1 >= 30
	T1T2_mem1 += INPUT_mem_r

	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	S += T4T4 >= 30
	T4T4 += MUL[0]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 31
	T100_mem0 += ADD_mem[1]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 31
	T100_mem1 += ADD_mem[0]

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 31
	T101 += ADD[0]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 31
	T131_mem0 += INPUT_mem_r

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 31
	T131_mem1 += INPUT_mem_r

	T1T2 = S.Task('T1T2', length=1, delay_cost=1)
	S += T1T2 >= 31
	T1T2 += ADD[3]

	T3_T3_mem0 = S.Task('T3_T3_mem0', length=1, delay_cost=1)
	S += T3_T3_mem0 >= 31
	T3_T3_mem0 += ADD_mem[1]

	T3_T3_mem1 = S.Task('T3_T3_mem1', length=1, delay_cost=1)
	S += T3_T3_mem1 >= 31
	T3_T3_mem1 += ADD_mem[2]

	T100 = S.Task('T100', length=1, delay_cost=1)
	S += T100 >= 32
	T100 += ADD[3]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 32
	T130_mem0 += INPUT_mem_r

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 32
	T130_mem1 += INPUT_mem_r

	T131 = S.Task('T131', length=1, delay_cost=1)
	S += T131 >= 32
	T131 += ADD[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 32
	T31_mem0 += MUL_mem[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 32
	T31_mem1 += ADD_mem[1]

	T3_T3 = S.Task('T3_T3', length=1, delay_cost=1)
	S += T3_T3 >= 32
	T3_T3 += ADD[2]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 33
	T130 += ADD[0]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 33
	T31 += ADD[2]

	T4_T1_in = S.Task('T4_T1_in', length=1, delay_cost=1)
	S += T4_T1_in >= 33
	T4_T1_in += MUL_in[0]

	T4_T1_mem0 = S.Task('T4_T1_mem0', length=1, delay_cost=1)
	S += T4_T1_mem0 >= 33
	T4_T1_mem0 += ADD_mem[0]

	T4_T1_mem1 = S.Task('T4_T1_mem1', length=1, delay_cost=1)
	S += T4_T1_mem1 >= 33
	T4_T1_mem1 += ADD_mem[0]

	T6_1T3_mem0 = S.Task('T6_1T3_mem0', length=1, delay_cost=1)
	S += T6_1T3_mem0 >= 33
	T6_1T3_mem0 += INPUT_mem_r

	T6_1T3_mem1 = S.Task('T6_1T3_mem1', length=1, delay_cost=1)
	S += T6_1T3_mem1 >= 33
	T6_1T3_mem1 += INPUT_mem_r

	T4_T1 = S.Task('T4_T1', length=7, delay_cost=1)
	S += T4_T1 >= 34
	T4_T1 += MUL[0]

	T6_1T2_mem0 = S.Task('T6_1T2_mem0', length=1, delay_cost=1)
	S += T6_1T2_mem0 >= 34
	T6_1T2_mem0 += INPUT_mem_r

	T6_1T2_mem1 = S.Task('T6_1T2_mem1', length=1, delay_cost=1)
	S += T6_1T2_mem1 >= 34
	T6_1T2_mem1 += INPUT_mem_r

	T6_1T3 = S.Task('T6_1T3', length=1, delay_cost=1)
	S += T6_1T3 >= 34
	T6_1T3 += ADD[1]

	T8T0_in = S.Task('T8T0_in', length=1, delay_cost=1)
	S += T8T0_in >= 34
	T8T0_in += MUL_in[0]

	T8T0_mem0 = S.Task('T8T0_mem0', length=1, delay_cost=1)
	S += T8T0_mem0 >= 34
	T8T0_mem0 += ADD_mem[0]

	T8T0_mem1 = S.Task('T8T0_mem1', length=1, delay_cost=1)
	S += T8T0_mem1 >= 34
	T8T0_mem1 += ADD_mem[1]

	T9_T3_mem0 = S.Task('T9_T3_mem0', length=1, delay_cost=1)
	S += T9_T3_mem0 >= 34
	T9_T3_mem0 += ADD_mem[3]

	T9_T3_mem1 = S.Task('T9_T3_mem1', length=1, delay_cost=1)
	S += T9_T3_mem1 >= 34
	T9_T3_mem1 += ADD_mem[0]

	T4_T0_in = S.Task('T4_T0_in', length=1, delay_cost=1)
	S += T4_T0_in >= 35
	T4_T0_in += MUL_in[0]

	T4_T0_mem0 = S.Task('T4_T0_mem0', length=1, delay_cost=1)
	S += T4_T0_mem0 >= 35
	T4_T0_mem0 += ADD_mem[0]

	T4_T0_mem1 = S.Task('T4_T0_mem1', length=1, delay_cost=1)
	S += T4_T0_mem1 >= 35
	T4_T0_mem1 += ADD_mem[0]

	T6_1T2 = S.Task('T6_1T2', length=1, delay_cost=1)
	S += T6_1T2 >= 35
	T6_1T2 += ADD[0]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 35
	T71_mem0 += INPUT_mem_r

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 35
	T71_mem1 += INPUT_mem_r

	T8T0 = S.Task('T8T0', length=7, delay_cost=1)
	S += T8T0 >= 35
	T8T0 += MUL[0]

	T9_T3 = S.Task('T9_T3', length=1, delay_cost=1)
	S += T9_T3 >= 35
	T9_T3 += ADD[3]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 36
	T21_mem0 += MUL_mem[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 36
	T21_mem1 += ADD_mem[0]

	T4_T0 = S.Task('T4_T0', length=7, delay_cost=1)
	S += T4_T0 >= 36
	T4_T0 += MUL[0]

	T6_1T4_in = S.Task('T6_1T4_in', length=1, delay_cost=1)
	S += T6_1T4_in >= 36
	T6_1T4_in += MUL_in[0]

	T6_1T4_mem0 = S.Task('T6_1T4_mem0', length=1, delay_cost=1)
	S += T6_1T4_mem0 >= 36
	T6_1T4_mem0 += ADD_mem[0]

	T6_1T4_mem1 = S.Task('T6_1T4_mem1', length=1, delay_cost=1)
	S += T6_1T4_mem1 >= 36
	T6_1T4_mem1 += ADD_mem[1]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 36
	T70_mem0 += INPUT_mem_r

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 36
	T70_mem1 += INPUT_mem_r

	T71 = S.Task('T71', length=1, delay_cost=1)
	S += T71 >= 36
	T71 += ADD[3]

	T1T3_mem0 = S.Task('T1T3_mem0', length=1, delay_cost=1)
	S += T1T3_mem0 >= 37
	T1T3_mem0 += INPUT_mem_r

	T1T3_mem1 = S.Task('T1T3_mem1', length=1, delay_cost=1)
	S += T1T3_mem1 >= 37
	T1T3_mem1 += INPUT_mem_r

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 37
	T21 += ADD[0]

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	S += T2_0_mem0 >= 37
	T2_0_mem0 += ADD_mem[3]

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	S += T2_0_mem1 >= 37
	T2_0_mem1 += ADD_mem[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 37
	T41_mem0 += MUL_mem[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 37
	T41_mem1 += ADD_mem[3]

	T6_1T4 = S.Task('T6_1T4', length=7, delay_cost=1)
	S += T6_1T4 >= 37
	T6_1T4 += MUL[0]

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 37
	T70 += ADD[3]

	T8T1_in = S.Task('T8T1_in', length=1, delay_cost=1)
	S += T8T1_in >= 37
	T8T1_in += MUL_in[0]

	T8T1_mem0 = S.Task('T8T1_mem0', length=1, delay_cost=1)
	S += T8T1_mem0 >= 37
	T8T1_mem0 += ADD_mem[0]

	T8T1_mem1 = S.Task('T8T1_mem1', length=1, delay_cost=1)
	S += T8T1_mem1 >= 37
	T8T1_mem1 += ADD_mem[1]

	T1T3 = S.Task('T1T3', length=1, delay_cost=1)
	S += T1T3 >= 38
	T1T3 += ADD[3]

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	S += T2_0 >= 38
	T2_0 += ADD[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 38
	T41 += ADD[2]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 38
	T61_mem0 += INPUT_mem_r

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 38
	T61_mem1 += INPUT_mem_r

	T6_T3_mem0 = S.Task('T6_T3_mem0', length=1, delay_cost=1)
	S += T6_T3_mem0 >= 38
	T6_T3_mem0 += ADD_mem[3]

	T6_T3_mem1 = S.Task('T6_T3_mem1', length=1, delay_cost=1)
	S += T6_T3_mem1 >= 38
	T6_T3_mem1 += ADD_mem[3]

	T7_1_mem0 = S.Task('T7_1_mem0', length=1, delay_cost=1)
	S += T7_1_mem0 >= 38
	T7_1_mem0 += ADD_mem[2]

	T7_1_mem1 = S.Task('T7_1_mem1', length=1, delay_cost=1)
	S += T7_1_mem1 >= 38
	T7_1_mem1 += ADD_mem[2]

	T8T1 = S.Task('T8T1', length=7, delay_cost=1)
	S += T8T1 >= 38
	T8T1 += MUL[0]

	T8T2_mem0 = S.Task('T8T2_mem0', length=1, delay_cost=1)
	S += T8T2_mem0 >= 38
	T8T2_mem0 += ADD_mem[0]

	T8T2_mem1 = S.Task('T8T2_mem1', length=1, delay_cost=1)
	S += T8T2_mem1 >= 38
	T8T2_mem1 += ADD_mem[0]

	T1T4_in = S.Task('T1T4_in', length=1, delay_cost=1)
	S += T1T4_in >= 39
	T1T4_in += MUL_in[0]

	T1T4_mem0 = S.Task('T1T4_mem0', length=1, delay_cost=1)
	S += T1T4_mem0 >= 39
	T1T4_mem0 += ADD_mem[3]

	T1T4_mem1 = S.Task('T1T4_mem1', length=1, delay_cost=1)
	S += T1T4_mem1 >= 39
	T1T4_mem1 += ADD_mem[3]

	T4_T2_mem0 = S.Task('T4_T2_mem0', length=1, delay_cost=1)
	S += T4_T2_mem0 >= 39
	T4_T2_mem0 += ADD_mem[0]

	T4_T2_mem1 = S.Task('T4_T2_mem1', length=1, delay_cost=1)
	S += T4_T2_mem1 >= 39
	T4_T2_mem1 += ADD_mem[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 39
	T60_mem0 += INPUT_mem_r

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 39
	T60_mem1 += INPUT_mem_r

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 39
	T61 += ADD[0]

	T6_T3 = S.Task('T6_T3', length=1, delay_cost=1)
	S += T6_T3 >= 39
	T6_T3 += ADD[1]

	T7_1 = S.Task('T7_1', length=1, delay_cost=1)
	S += T7_1 >= 39
	T7_1 += ADD[2]

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	S += T8T2 >= 39
	T8T2 += ADD[3]

	T1T4 = S.Task('T1T4', length=7, delay_cost=1)
	S += T1T4 >= 40
	T1T4 += MUL[0]

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	S += T2_1_mem0 >= 40
	T2_1_mem0 += ADD_mem[3]

	T2_1_mem1 = S.Task('T2_1_mem1', length=1, delay_cost=1)
	S += T2_1_mem1 >= 40
	T2_1_mem1 += ADD_mem[0]

	T4_T2 = S.Task('T4_T2', length=1, delay_cost=1)
	S += T4_T2 >= 40
	T4_T2 += ADD[3]

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	S += T5T3_mem0 >= 40
	T5T3_mem0 += INPUT_mem_r

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	S += T5T3_mem1 >= 40
	T5T3_mem1 += INPUT_mem_r

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 40
	T60 += ADD[0]

	T6_T1_in = S.Task('T6_T1_in', length=1, delay_cost=1)
	S += T6_T1_in >= 40
	T6_T1_in += MUL_in[0]

	T6_T1_mem0 = S.Task('T6_T1_mem0', length=1, delay_cost=1)
	S += T6_T1_mem0 >= 40
	T6_T1_mem0 += ADD_mem[0]

	T6_T1_mem1 = S.Task('T6_T1_mem1', length=1, delay_cost=1)
	S += T6_T1_mem1 >= 40
	T6_T1_mem1 += ADD_mem[3]

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	S += T2_1 >= 41
	T2_1 += ADD[2]

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	S += T5T2_mem0 >= 41
	T5T2_mem0 += INPUT_mem_r

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	S += T5T2_mem1 >= 41
	T5T2_mem1 += INPUT_mem_r

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	S += T5T3 >= 41
	T5T3 += ADD[1]

	T6_T0_in = S.Task('T6_T0_in', length=1, delay_cost=1)
	S += T6_T0_in >= 41
	T6_T0_in += MUL_in[0]

	T6_T0_mem0 = S.Task('T6_T0_mem0', length=1, delay_cost=1)
	S += T6_T0_mem0 >= 41
	T6_T0_mem0 += ADD_mem[0]

	T6_T0_mem1 = S.Task('T6_T0_mem1', length=1, delay_cost=1)
	S += T6_T0_mem1 >= 41
	T6_T0_mem1 += ADD_mem[3]

	T6_T1 = S.Task('T6_T1', length=7, delay_cost=1)
	S += T6_T1 >= 41
	T6_T1 += MUL[0]

	T3_T0_in = S.Task('T3_T0_in', length=1, delay_cost=1)
	S += T3_T0_in >= 42
	T3_T0_in += MUL_in[0]

	T3_T0_mem0 = S.Task('T3_T0_mem0', length=1, delay_cost=1)
	S += T3_T0_mem0 >= 42
	T3_T0_mem0 += INPUT_mem_r

	T3_T0_mem1 = S.Task('T3_T0_mem1', length=1, delay_cost=1)
	S += T3_T0_mem1 >= 42
	T3_T0_mem1 += ADD_mem[1]

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	S += T5T2 >= 42
	T5T2 += ADD[2]

	T6_T0 = S.Task('T6_T0', length=7, delay_cost=1)
	S += T6_T0 >= 42
	T6_T0 += MUL[0]

	T6_T2_mem0 = S.Task('T6_T2_mem0', length=1, delay_cost=1)
	S += T6_T2_mem0 >= 42
	T6_T2_mem0 += ADD_mem[0]

	T6_T2_mem1 = S.Task('T6_T2_mem1', length=1, delay_cost=1)
	S += T6_T2_mem1 >= 42
	T6_T2_mem1 += ADD_mem[0]

	T3_T0 = S.Task('T3_T0', length=7, delay_cost=1)
	S += T3_T0 >= 43
	T3_T0 += MUL[0]

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	S += T4_0_mem0 >= 43
	T4_0_mem0 += MUL_mem[0]

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	S += T4_0_mem1 >= 43
	T4_0_mem1 += MUL_mem[0]

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	S += T5T4_in >= 43
	T5T4_in += MUL_in[0]

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	S += T5T4_mem0 >= 43
	T5T4_mem0 += ADD_mem[2]

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	S += T5T4_mem1 >= 43
	T5T4_mem1 += ADD_mem[1]

	T6_T2 = S.Task('T6_T2', length=1, delay_cost=1)
	S += T6_T2 >= 43
	T6_T2 += ADD[2]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 43
	T90_mem0 += INPUT_mem_r

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 43
	T90_mem1 += ADD_mem[0]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 43
	T91_mem0 += INPUT_mem_r

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 43
	T91_mem1 += ADD_mem[0]

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	S += T4_0 >= 44
	T4_0 += ADD[1]

	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	S += T5T4 >= 44
	T5T4 += MUL[0]

	T6_11_mem0 = S.Task('T6_11_mem0', length=1, delay_cost=1)
	S += T6_11_mem0 >= 44
	T6_11_mem0 += MUL_mem[0]

	T6_11_mem1 = S.Task('T6_11_mem1', length=1, delay_cost=1)
	S += T6_11_mem1 >= 44
	T6_11_mem1 += ADD_mem[1]

	T90 = S.Task('T90', length=1, delay_cost=1)
	S += T90 >= 44
	T90 += ADD[2]

	T91 = S.Task('T91', length=1, delay_cost=1)
	S += T91 >= 44
	T91 += ADD[3]

	T9_1T0_in = S.Task('T9_1T0_in', length=1, delay_cost=1)
	S += T9_1T0_in >= 44
	T9_1T0_in += MUL_in[0]

	T9_1T0_mem0 = S.Task('T9_1T0_mem0', length=1, delay_cost=1)
	S += T9_1T0_mem0 >= 44
	T9_1T0_mem0 += INPUT_mem_r

	T9_1T0_mem1 = S.Task('T9_1T0_mem1', length=1, delay_cost=1)
	S += T9_1T0_mem1 >= 44
	T9_1T0_mem1 += ADD_mem[1]

	T6_11 = S.Task('T6_11', length=1, delay_cost=1)
	S += T6_11 >= 45
	T6_11 += ADD[0]

	T6_21_mem0 = S.Task('T6_21_mem0', length=1, delay_cost=1)
	S += T6_21_mem0 >= 45
	T6_21_mem0 += ADD_mem[0]

	T6_21_mem1 = S.Task('T6_21_mem1', length=1, delay_cost=1)
	S += T6_21_mem1 >= 45
	T6_21_mem1 += ADD_mem[2]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 45
	T80_mem0 += MUL_mem[0]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 45
	T80_mem1 += MUL_mem[0]

	T9_1T0 = S.Task('T9_1T0', length=7, delay_cost=1)
	S += T9_1T0 >= 45
	T9_1T0 += MUL[0]

	T9_1T1_in = S.Task('T9_1T1_in', length=1, delay_cost=1)
	S += T9_1T1_in >= 45
	T9_1T1_in += MUL_in[0]

	T9_1T1_mem0 = S.Task('T9_1T1_mem0', length=1, delay_cost=1)
	S += T9_1T1_mem0 >= 45
	T9_1T1_mem0 += INPUT_mem_r

	T9_1T1_mem1 = S.Task('T9_1T1_mem1', length=1, delay_cost=1)
	S += T9_1T1_mem1 >= 45
	T9_1T1_mem1 += ADD_mem[1]

	T9_T2_mem0 = S.Task('T9_T2_mem0', length=1, delay_cost=1)
	S += T9_T2_mem0 >= 45
	T9_T2_mem0 += ADD_mem[2]

	T9_T2_mem1 = S.Task('T9_T2_mem1', length=1, delay_cost=1)
	S += T9_T2_mem1 >= 45
	T9_T2_mem1 += ADD_mem[3]

	T13_1_mem0 = S.Task('T13_1_mem0', length=1, delay_cost=1)
	S += T13_1_mem0 >= 46
	T13_1_mem0 += ADD_mem[0]

	T13_1_mem1 = S.Task('T13_1_mem1', length=1, delay_cost=1)
	S += T13_1_mem1 >= 46
	T13_1_mem1 += ADD_mem[2]

	T3_T1_in = S.Task('T3_T1_in', length=1, delay_cost=1)
	S += T3_T1_in >= 46
	T3_T1_in += MUL_in[0]

	T3_T1_mem0 = S.Task('T3_T1_mem0', length=1, delay_cost=1)
	S += T3_T1_mem0 >= 46
	T3_T1_mem0 += INPUT_mem_r

	T3_T1_mem1 = S.Task('T3_T1_mem1', length=1, delay_cost=1)
	S += T3_T1_mem1 >= 46
	T3_T1_mem1 += ADD_mem[2]

	T4_T5_mem0 = S.Task('T4_T5_mem0', length=1, delay_cost=1)
	S += T4_T5_mem0 >= 46
	T4_T5_mem0 += MUL_mem[0]

	T4_T5_mem1 = S.Task('T4_T5_mem1', length=1, delay_cost=1)
	S += T4_T5_mem1 >= 46
	T4_T5_mem1 += MUL_mem[0]

	T6_21 = S.Task('T6_21', length=1, delay_cost=1)
	S += T6_21 >= 46
	T6_21 += ADD[2]

	T80 = S.Task('T80', length=1, delay_cost=1)
	S += T80 >= 46
	T80 += ADD[3]

	T9_1T1 = S.Task('T9_1T1', length=7, delay_cost=1)
	S += T9_1T1 >= 46
	T9_1T1 += MUL[0]

	T9_T2 = S.Task('T9_T2', length=1, delay_cost=1)
	S += T9_T2 >= 46
	T9_T2 += ADD[0]

	T13_1 = S.Task('T13_1', length=1, delay_cost=1)
	S += T13_1 >= 47
	T13_1 += ADD[2]

	T3_T1 = S.Task('T3_T1', length=7, delay_cost=1)
	S += T3_T1 >= 47
	T3_T1 += MUL[0]

	T4_T5 = S.Task('T4_T5', length=1, delay_cost=1)
	S += T4_T5 >= 47
	T4_T5 += ADD[1]

	T6_T4_in = S.Task('T6_T4_in', length=1, delay_cost=1)
	S += T6_T4_in >= 47
	T6_T4_in += MUL_in[0]

	T6_T4_mem0 = S.Task('T6_T4_mem0', length=1, delay_cost=1)
	S += T6_T4_mem0 >= 47
	T6_T4_mem0 += ADD_mem[2]

	T6_T4_mem1 = S.Task('T6_T4_mem1', length=1, delay_cost=1)
	S += T6_T4_mem1 >= 47
	T6_T4_mem1 += ADD_mem[1]

	T8T5_mem0 = S.Task('T8T5_mem0', length=1, delay_cost=1)
	S += T8T5_mem0 >= 47
	T8T5_mem0 += MUL_mem[0]

	T8T5_mem1 = S.Task('T8T5_mem1', length=1, delay_cost=1)
	S += T8T5_mem1 >= 47
	T8T5_mem1 += MUL_mem[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 48
	T11_mem0 += MUL_mem[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 48
	T11_mem1 += ADD_mem[3]

	T6_T4 = S.Task('T6_T4', length=7, delay_cost=1)
	S += T6_T4 >= 48
	T6_T4 += MUL[0]

	T8T4_in = S.Task('T8T4_in', length=1, delay_cost=1)
	S += T8T4_in >= 48
	T8T4_in += MUL_in[0]

	T8T4_mem0 = S.Task('T8T4_mem0', length=1, delay_cost=1)
	S += T8T4_mem0 >= 48
	T8T4_mem0 += ADD_mem[3]

	T8T4_mem1 = S.Task('T8T4_mem1', length=1, delay_cost=1)
	S += T8T4_mem1 >= 48
	T8T4_mem1 += ADD_mem[1]

	T8T5 = S.Task('T8T5', length=1, delay_cost=1)
	S += T8T5 >= 48
	T8T5 += ADD[0]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 49
	T11 += ADD[2]

	T4_T4_in = S.Task('T4_T4_in', length=1, delay_cost=1)
	S += T4_T4_in >= 49
	T4_T4_in += MUL_in[0]

	T4_T4_mem0 = S.Task('T4_T4_mem0', length=1, delay_cost=1)
	S += T4_T4_mem0 >= 49
	T4_T4_mem0 += ADD_mem[3]

	T4_T4_mem1 = S.Task('T4_T4_mem1', length=1, delay_cost=1)
	S += T4_T4_mem1 >= 49
	T4_T4_mem1 += ADD_mem[1]

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	S += T6_0_mem0 >= 49
	T6_0_mem0 += MUL_mem[0]

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	S += T6_0_mem1 >= 49
	T6_0_mem1 += MUL_mem[0]

	T8T4 = S.Task('T8T4', length=7, delay_cost=1)
	S += T8T4 >= 49
	T8T4 += MUL[0]

	T4_T4 = S.Task('T4_T4', length=7, delay_cost=1)
	S += T4_T4 >= 50
	T4_T4 += MUL[0]

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	S += T6_0 >= 50
	T6_0 += ADD[0]

	T6_T5_mem0 = S.Task('T6_T5_mem0', length=1, delay_cost=1)
	S += T6_T5_mem0 >= 50
	T6_T5_mem0 += MUL_mem[0]

	T6_T5_mem1 = S.Task('T6_T5_mem1', length=1, delay_cost=1)
	S += T6_T5_mem1 >= 50
	T6_T5_mem1 += MUL_mem[0]

	T7_10_mem0 = S.Task('T7_10_mem0', length=1, delay_cost=1)
	S += T7_10_mem0 >= 50
	T7_10_mem0 += ADD_mem[0]

	T7_10_mem1 = S.Task('T7_10_mem1', length=1, delay_cost=1)
	S += T7_10_mem1 >= 50
	T7_10_mem1 += ADD_mem[2]

	T9_T1_in = S.Task('T9_T1_in', length=1, delay_cost=1)
	S += T9_T1_in >= 50
	T9_T1_in += MUL_in[0]

	T9_T1_mem0 = S.Task('T9_T1_mem0', length=1, delay_cost=1)
	S += T9_T1_mem0 >= 50
	T9_T1_mem0 += ADD_mem[3]

	T9_T1_mem1 = S.Task('T9_T1_mem1', length=1, delay_cost=1)
	S += T9_T1_mem1 >= 50
	T9_T1_mem1 += ADD_mem[0]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 51
	T120_mem0 += ADD_mem[1]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 51
	T120_mem1 += ADD_mem[0]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 51
	T51_mem0 += MUL_mem[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 51
	T51_mem1 += ADD_mem[2]

	T6_T5 = S.Task('T6_T5', length=1, delay_cost=1)
	S += T6_T5 >= 51
	T6_T5 += ADD[3]

	T7_10 = S.Task('T7_10', length=1, delay_cost=1)
	S += T7_10 >= 51
	T7_10 += ADD[0]

	T9_T0_in = S.Task('T9_T0_in', length=1, delay_cost=1)
	S += T9_T0_in >= 51
	T9_T0_in += MUL_in[0]

	T9_T0_mem0 = S.Task('T9_T0_mem0', length=1, delay_cost=1)
	S += T9_T0_mem0 >= 51
	T9_T0_mem0 += ADD_mem[2]

	T9_T0_mem1 = S.Task('T9_T0_mem1', length=1, delay_cost=1)
	S += T9_T0_mem1 >= 51
	T9_T0_mem1 += ADD_mem[3]

	T9_T1 = S.Task('T9_T1', length=7, delay_cost=1)
	S += T9_T1 >= 51
	T9_T1 += MUL[0]

	T120 = S.Task('T120', length=1, delay_cost=1)
	S += T120 >= 52
	T120 += ADD[2]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 52
	T51 += ADD[1]

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	S += T5_0_mem0 >= 52
	T5_0_mem0 += ADD_mem[2]

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	S += T5_0_mem1 >= 52
	T5_0_mem1 += ADD_mem[1]

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	S += T5_1_mem0 >= 52
	T5_1_mem0 += ADD_mem[2]

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	S += T5_1_mem1 >= 52
	T5_1_mem1 += ADD_mem[1]

	T9_T0 = S.Task('T9_T0', length=7, delay_cost=1)
	S += T9_T0 >= 52
	T9_T0 += MUL[0]

	T9_T4_in = S.Task('T9_T4_in', length=1, delay_cost=1)
	S += T9_T4_in >= 52
	T9_T4_in += MUL_in[0]

	T9_T4_mem0 = S.Task('T9_T4_mem0', length=1, delay_cost=1)
	S += T9_T4_mem0 >= 52
	T9_T4_mem0 += ADD_mem[0]

	T9_T4_mem1 = S.Task('T9_T4_mem1', length=1, delay_cost=1)
	S += T9_T4_mem1 >= 52
	T9_T4_mem1 += ADD_mem[3]

	T3_T4_in = S.Task('T3_T4_in', length=1, delay_cost=1)
	S += T3_T4_in >= 53
	T3_T4_in += MUL_in[0]

	T3_T4_mem0 = S.Task('T3_T4_mem0', length=1, delay_cost=1)
	S += T3_T4_mem0 >= 53
	T3_T4_mem0 += ADD_mem[0]

	T3_T4_mem1 = S.Task('T3_T4_mem1', length=1, delay_cost=1)
	S += T3_T4_mem1 >= 53
	T3_T4_mem1 += ADD_mem[2]

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	S += T5_0 >= 53
	T5_0 += ADD[1]

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	S += T5_1 >= 53
	T5_1 += ADD[0]

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	S += T5_10_mem0 >= 53
	T5_10_mem0 += ADD_mem[3]

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	S += T5_10_mem1 >= 53
	T5_10_mem1 += ADD_mem[1]

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	S += T5_11_mem0 >= 53
	T5_11_mem0 += ADD_mem[2]

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	S += T5_11_mem1 >= 53
	T5_11_mem1 += ADD_mem[0]

	T9_10_mem0 = S.Task('T9_10_mem0', length=1, delay_cost=1)
	S += T9_10_mem0 >= 53
	T9_10_mem0 += MUL_mem[0]

	T9_10_mem1 = S.Task('T9_10_mem1', length=1, delay_cost=1)
	S += T9_10_mem1 >= 53
	T9_10_mem1 += MUL_mem[0]

	T9_T4 = S.Task('T9_T4', length=7, delay_cost=1)
	S += T9_T4 >= 53
	T9_T4 += MUL[0]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 54
	T3_0_mem0 += MUL_mem[0]

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 54
	T3_0_mem1 += MUL_mem[0]

	T3_T4 = S.Task('T3_T4', length=7, delay_cost=1)
	S += T3_T4 >= 54
	T3_T4 += MUL[0]

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	S += T5_10 >= 54
	T5_10 += ADD[1]

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	S += T5_11 >= 54
	T5_11 += ADD[2]

	T9_10 = S.Task('T9_10', length=1, delay_cost=1)
	S += T9_10 >= 54
	T9_10 += ADD[3]

	T9_20_mem0 = S.Task('T9_20_mem0', length=1, delay_cost=1)
	S += T9_20_mem0 >= 54
	T9_20_mem0 += ADD_mem[3]

	T9_20_mem1 = S.Task('T9_20_mem1', length=1, delay_cost=1)
	S += T9_20_mem1 >= 54
	T9_20_mem1 += ADD_mem[1]

	T10_0_mem0 = S.Task('T10_0_mem0', length=1, delay_cost=1)
	S += T10_0_mem0 >= 55
	T10_0_mem0 += ADD_mem[0]

	T10_0_mem1 = S.Task('T10_0_mem1', length=1, delay_cost=1)
	S += T10_0_mem1 >= 55
	T10_0_mem1 += ADD_mem[1]

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 55
	T3_0 += ADD[0]

	T6_1_mem0 = S.Task('T6_1_mem0', length=1, delay_cost=1)
	S += T6_1_mem0 >= 55
	T6_1_mem0 += MUL_mem[0]

	T6_1_mem1 = S.Task('T6_1_mem1', length=1, delay_cost=1)
	S += T6_1_mem1 >= 55
	T6_1_mem1 += ADD_mem[3]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 55
	T81_mem0 += MUL_mem[0]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 55
	T81_mem1 += ADD_mem[0]

	T9_20 = S.Task('T9_20', length=1, delay_cost=1)
	S += T9_20 >= 55
	T9_20 += ADD[3]

	T10_0 = S.Task('T10_0', length=1, delay_cost=1)
	S += T10_0 >= 56
	T10_0 += ADD[2]

	T6_1 = S.Task('T6_1', length=1, delay_cost=1)
	S += T6_1 >= 56
	T6_1 += ADD[1]

	T7_11_mem0 = S.Task('T7_11_mem0', length=1, delay_cost=1)
	S += T7_11_mem0 >= 56
	T7_11_mem0 += ADD_mem[1]

	T7_11_mem1 = S.Task('T7_11_mem1', length=1, delay_cost=1)
	S += T7_11_mem1 >= 56
	T7_11_mem1 += ADD_mem[2]

	T81 = S.Task('T81', length=1, delay_cost=1)
	S += T81 >= 56
	T81 += ADD[0]

	T8_0_mem0 = S.Task('T8_0_mem0', length=1, delay_cost=1)
	S += T8_0_mem0 >= 56
	T8_0_mem0 += ADD_mem[3]

	T8_0_mem1 = S.Task('T8_0_mem1', length=1, delay_cost=1)
	S += T8_0_mem1 >= 56
	T8_0_mem1 += ADD_mem[0]

	T8_1_mem0 = S.Task('T8_1_mem0', length=1, delay_cost=1)
	S += T8_1_mem0 >= 56
	T8_1_mem0 += ADD_mem[3]

	T8_1_mem1 = S.Task('T8_1_mem1', length=1, delay_cost=1)
	S += T8_1_mem1 >= 56
	T8_1_mem1 += ADD_mem[0]

	T9_1T5_mem0 = S.Task('T9_1T5_mem0', length=1, delay_cost=1)
	S += T9_1T5_mem0 >= 56
	T9_1T5_mem0 += MUL_mem[0]

	T9_1T5_mem1 = S.Task('T9_1T5_mem1', length=1, delay_cost=1)
	S += T9_1T5_mem1 >= 56
	T9_1T5_mem1 += MUL_mem[0]

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	S += T4_1_mem0 >= 57
	T4_1_mem0 += MUL_mem[0]

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	S += T4_1_mem1 >= 57
	T4_1_mem1 += ADD_mem[1]

	T7_11 = S.Task('T7_11', length=1, delay_cost=1)
	S += T7_11 >= 57
	T7_11 += ADD[2]

	T8_0 = S.Task('T8_0', length=1, delay_cost=1)
	S += T8_0 >= 57
	T8_0 += ADD[3]

	T8_1 = S.Task('T8_1', length=1, delay_cost=1)
	S += T8_1 >= 57
	T8_1 += ADD[0]

	T9_11_mem0 = S.Task('T9_11_mem0', length=1, delay_cost=1)
	S += T9_11_mem0 >= 57
	T9_11_mem0 += MUL_mem[0]

	T9_11_mem1 = S.Task('T9_11_mem1', length=1, delay_cost=1)
	S += T9_11_mem1 >= 57
	T9_11_mem1 += ADD_mem[1]

	T9_1T5 = S.Task('T9_1T5', length=1, delay_cost=1)
	S += T9_1T5 >= 57
	T9_1T5 += ADD[1]

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	S += T4_1 >= 58
	T4_1 += ADD[2]

	T9_0_mem0 = S.Task('T9_0_mem0', length=1, delay_cost=1)
	S += T9_0_mem0 >= 58
	T9_0_mem0 += MUL_mem[0]

	T9_0_mem1 = S.Task('T9_0_mem1', length=1, delay_cost=1)
	S += T9_0_mem1 >= 58
	T9_0_mem1 += MUL_mem[0]

	T9_11 = S.Task('T9_11', length=1, delay_cost=1)
	S += T9_11 >= 58
	T9_11 += ADD[0]

	T9_21_mem0 = S.Task('T9_21_mem0', length=1, delay_cost=1)
	S += T9_21_mem0 >= 58
	T9_21_mem0 += ADD_mem[0]

	T9_21_mem1 = S.Task('T9_21_mem1', length=1, delay_cost=1)
	S += T9_21_mem1 >= 58
	T9_21_mem1 += ADD_mem[2]

	T10_10_mem0 = S.Task('T10_10_mem0', length=1, delay_cost=1)
	S += T10_10_mem0 >= 59
	T10_10_mem0 += ADD_mem[0]

	T10_10_mem1 = S.Task('T10_10_mem1', length=1, delay_cost=1)
	S += T10_10_mem1 >= 59
	T10_10_mem1 += ADD_mem[2]

	T3_T5_mem0 = S.Task('T3_T5_mem0', length=1, delay_cost=1)
	S += T3_T5_mem0 >= 59
	T3_T5_mem0 += MUL_mem[0]

	T3_T5_mem1 = S.Task('T3_T5_mem1', length=1, delay_cost=1)
	S += T3_T5_mem1 >= 59
	T3_T5_mem1 += MUL_mem[0]

	T9_0 = S.Task('T9_0', length=1, delay_cost=1)
	S += T9_0 >= 59
	T9_0 += ADD[0]

	T9_21 = S.Task('T9_21', length=1, delay_cost=1)
	S += T9_21 >= 59
	T9_21 += ADD[2]

	T10_10 = S.Task('T10_10', length=1, delay_cost=1)
	S += T10_10 >= 60
	T10_10 += ADD[0]

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	S += T3_1_mem0 >= 60
	T3_1_mem0 += MUL_mem[0]

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	S += T3_1_mem1 >= 60
	T3_1_mem1 += ADD_mem[3]

	T3_T5 = S.Task('T3_T5', length=1, delay_cost=1)
	S += T3_T5 >= 60
	T3_T5 += ADD[3]

	T10_1_mem0 = S.Task('T10_1_mem0', length=1, delay_cost=1)
	S += T10_1_mem0 >= 61
	T10_1_mem0 += ADD_mem[0]

	T10_1_mem1 = S.Task('T10_1_mem1', length=1, delay_cost=1)
	S += T10_1_mem1 >= 61
	T10_1_mem1 += ADD_mem[2]

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 61
	T3_1 += ADD[0]

	T9_T5_mem0 = S.Task('T9_T5_mem0', length=1, delay_cost=1)
	S += T9_T5_mem0 >= 61
	T9_T5_mem0 += MUL_mem[0]

	T9_T5_mem1 = S.Task('T9_T5_mem1', length=1, delay_cost=1)
	S += T9_T5_mem1 >= 61
	T9_T5_mem1 += MUL_mem[0]

	T10_1 = S.Task('T10_1', length=1, delay_cost=1)
	S += T10_1 >= 62
	T10_1 += ADD[3]

	T9_1_mem0 = S.Task('T9_1_mem0', length=1, delay_cost=1)
	S += T9_1_mem0 >= 62
	T9_1_mem0 += MUL_mem[0]

	T9_1_mem1 = S.Task('T9_1_mem1', length=1, delay_cost=1)
	S += T9_1_mem1 >= 62
	T9_1_mem1 += ADD_mem[1]

	T9_T5 = S.Task('T9_T5', length=1, delay_cost=1)
	S += T9_T5 >= 62
	T9_T5 += ADD[1]

	T9_1 = S.Task('T9_1', length=1, delay_cost=1)
	S += T9_1 >= 63
	T9_1 += ADD[1]


	# new tasks
	T8_10 = S.Task('T8_10', length=1, delay_cost=1)
	T8_10 += alt(ADD)

	T8_10_mem0 = S.Task('T8_10_mem0', length=1, delay_cost=1)
	T8_10_mem0 += ADD_mem[0]
	S += T3_0<T8_10_mem0
	S += T8_10_mem0<=T8_10

	T8_10_mem1 = S.Task('T8_10_mem1', length=1, delay_cost=1)
	T8_10_mem1 += ADD_mem[3]
	S += T8_0<T8_10_mem1
	S += T8_10_mem1<=T8_10

	T8_11 = S.Task('T8_11', length=1, delay_cost=1)
	T8_11 += alt(ADD)

	T8_11_mem0 = S.Task('T8_11_mem0', length=1, delay_cost=1)
	T8_11_mem0 += ADD_mem[0]
	S += T3_1<T8_11_mem0
	S += T8_11_mem0<=T8_11

	T8_11_mem1 = S.Task('T8_11_mem1', length=1, delay_cost=1)
	T8_11_mem1 += ADD_mem[0]
	S += T8_1<T8_11_mem1
	S += T8_11_mem1<=T8_11

	T10_11 = S.Task('T10_11', length=1, delay_cost=1)
	T10_11 += alt(ADD)

	T10_11_mem0 = S.Task('T10_11_mem0', length=1, delay_cost=1)
	T10_11_mem0 += ADD_mem[1]
	S += T9_1<T10_11_mem0
	S += T10_11_mem0<=T10_11

	T10_11_mem1 = S.Task('T10_11_mem1', length=1, delay_cost=1)
	T10_11_mem1 += ADD_mem[3]
	S += T10_1<T10_11_mem1
	S += T10_11_mem1<=T10_11

	T110 = S.Task('T110', length=1, delay_cost=1)
	T110 += alt(ADD)

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	T110_mem0 += ADD_mem[0]
	S += T0_0<T110_mem0
	S += T110_mem0<=T110

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	T110_mem1 += ADD_mem[1]
	S += T5_10<T110_mem1
	S += T110_mem1<=T110

	T111 = S.Task('T111', length=1, delay_cost=1)
	T111 += alt(ADD)

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	T111_mem0 += ADD_mem[3]
	S += T0_1<T111_mem0
	S += T111_mem0<=T111

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	T111_mem1 += ADD_mem[2]
	S += T5_11<T111_mem1
	S += T111_mem1<=T111

	T121 = S.Task('T121', length=1, delay_cost=1)
	T121 += alt(ADD)

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	T121_mem0 += ADD_mem[2]
	S += T11<T121_mem0
	S += T121_mem0<=T121

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	T121_mem1 += ADD_mem[2]
	S += T7_11<T121_mem1
	S += T121_mem1<=T121

	C110 = S.Task('C110', length=1, delay_cost=1)
	C110 += alt(ADD)

	C110_mem0 = S.Task('C110_mem0', length=1, delay_cost=1)
	C110_mem0 += ADD_mem[1]
	S += T10<C110_mem0
	S += C110_mem0<=C110

	C110_mem1 = S.Task('C110_mem1', length=1, delay_cost=1)
	C110_mem1 += ADD_mem[0]
	S += T6_20<C110_mem1
	S += C110_mem1<=C110

	C110_w = S.Task('C110_w', length=1, delay_cost=1)
	C110_w += alt(INPUT_mem_w)
	S += 47 < C110_w
	S += C110-1 <= C110_w

	C210 = S.Task('C210', length=1, delay_cost=1)
	C210 += alt(ADD)

	C210_mem0 = S.Task('C210_mem0', length=1, delay_cost=1)
	C210_mem0 += ADD_mem[3]
	S += T9_20<C210_mem0
	S += C210_mem0<=C210

	C210_mem1 = S.Task('C210_mem1', length=1, delay_cost=1)
	C210_mem1 += ADD_mem[2]
	S += T13_0<C210_mem1
	S += C210_mem1<=C210

	C210_w = S.Task('C210_w', length=1, delay_cost=1)
	C210_w += alt(INPUT_mem_w)
	S += 47 < C210_w
	S += C210-1 <= C210_w

	C200 = S.Task('C200', length=1, delay_cost=1)
	C200 += alt(ADD)

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	C200_mem0 += ADD_mem[0]
	S += T0_0<C200_mem0
	S += C200_mem0<=C200

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	C200_mem1 += ADD_mem[0]
	S += T7_10<C200_mem1
	S += C200_mem1<=C200

	C200_w = S.Task('C200_w', length=1, delay_cost=1)
	C200_w += alt(INPUT_mem_w)
	S += 47 < C200_w
	S += C200-1 <= C200_w

	C111 = S.Task('C111', length=1, delay_cost=1)
	C111 += alt(ADD)

	C111_mem0 = S.Task('C111_mem0', length=1, delay_cost=1)
	C111_mem0 += ADD_mem[2]
	S += T11<C111_mem0
	S += C111_mem0<=C111

	C111_mem1 = S.Task('C111_mem1', length=1, delay_cost=1)
	C111_mem1 += ADD_mem[2]
	S += T6_21<C111_mem1
	S += C111_mem1<=C111

	C111_w = S.Task('C111_w', length=1, delay_cost=1)
	C111_w += alt(INPUT_mem_w)
	S += 47 < C111_w
	S += C111-1 <= C111_w

	C010 = S.Task('C010', length=1, delay_cost=1)
	C010 += alt(ADD)

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	C010_mem0 += ADD_mem[0]
	S += T10_10<C010_mem0
	S += C010_mem0<=C010

	C010_mem1 = S.Task('C010_mem1', length=1, delay_cost=1)
	C010_mem1 += ADD_mem[2]
	S += T120<C010_mem1
	S += C010_mem1<=C010

	C010_w = S.Task('C010_w', length=1, delay_cost=1)
	C010_w += alt(INPUT_mem_w)
	S += 47 < C010_w
	S += C010-1 <= C010_w

	C211 = S.Task('C211', length=1, delay_cost=1)
	C211 += alt(ADD)

	C211_mem0 = S.Task('C211_mem0', length=1, delay_cost=1)
	C211_mem0 += ADD_mem[2]
	S += T9_21<C211_mem0
	S += C211_mem0<=C211

	C211_mem1 = S.Task('C211_mem1', length=1, delay_cost=1)
	C211_mem1 += ADD_mem[2]
	S += T13_1<C211_mem1
	S += C211_mem1<=C211

	C211_w = S.Task('C211_w', length=1, delay_cost=1)
	C211_w += alt(INPUT_mem_w)
	S += 47 < C211_w
	S += C211-1 <= C211_w

	C000 = S.Task('C000', length=1, delay_cost=1)
	C000 += alt(ADD)

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	C000_mem0 += ADD_mem[0]
	S += T2_0<C000_mem0
	S += C000_mem0<=C000

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	C000_mem1 += ADD_mem[1]
	S += T5_10<C000_mem1
	S += C000_mem1<=C000

	C000_w = S.Task('C000_w', length=1, delay_cost=1)
	C000_w += alt(INPUT_mem_w)
	S += 47 < C000_w
	S += C000-1 <= C000_w

	C001 = S.Task('C001', length=1, delay_cost=1)
	C001 += alt(ADD)

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	C001_mem0 += ADD_mem[2]
	S += T2_1<C001_mem0
	S += C001_mem0<=C001

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	C001_mem1 += ADD_mem[2]
	S += T5_11<C001_mem1
	S += C001_mem1<=C001

	C001_w = S.Task('C001_w', length=1, delay_cost=1)
	C001_w += alt(INPUT_mem_w)
	S += 47 < C001_w
	S += C001-1 <= C001_w

	C201 = S.Task('C201', length=1, delay_cost=1)
	C201 += alt(ADD)

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	C201_mem0 += ADD_mem[3]
	S += T0_1<C201_mem0
	S += C201_mem0<=C201

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	C201_mem1 += ADD_mem[2]
	S += T7_11<C201_mem1
	S += C201_mem1<=C201

	C201_w = S.Task('C201_w', length=1, delay_cost=1)
	C201_w += alt(INPUT_mem_w)
	S += 47 < C201_w
	S += C201-1 <= C201_w

	C100 = S.Task('C100', length=1, delay_cost=1)
	C100 += alt(ADD)

	C100_mem0 = S.Task('C100_mem0', length=1, delay_cost=1)
	C100_mem0 += alt(ADD_mem)
	S += (T8_10*ADD[0])-1<C100_mem0*ADD_mem[0]
	S += (T8_10*ADD[1])-1<C100_mem0*ADD_mem[1]
	S += (T8_10*ADD[2])-1<C100_mem0*ADD_mem[2]
	S += (T8_10*ADD[3])-1<C100_mem0*ADD_mem[3]
	S += C100_mem0<=C100

	C100_mem1 = S.Task('C100_mem1', length=1, delay_cost=1)
	C100_mem1 += alt(ADD_mem)
	S += (T110*ADD[0])-1<C100_mem1*ADD_mem[0]
	S += (T110*ADD[1])-1<C100_mem1*ADD_mem[1]
	S += (T110*ADD[2])-1<C100_mem1*ADD_mem[2]
	S += (T110*ADD[3])-1<C100_mem1*ADD_mem[3]
	S += C100_mem1<=C100

	C100_w = S.Task('C100_w', length=1, delay_cost=1)
	C100_w += alt(INPUT_mem_w)
	S += 47 < C100_w
	S += C100-1 <= C100_w

	C101 = S.Task('C101', length=1, delay_cost=1)
	C101 += alt(ADD)

	C101_mem0 = S.Task('C101_mem0', length=1, delay_cost=1)
	C101_mem0 += alt(ADD_mem)
	S += (T8_11*ADD[0])-1<C101_mem0*ADD_mem[0]
	S += (T8_11*ADD[1])-1<C101_mem0*ADD_mem[1]
	S += (T8_11*ADD[2])-1<C101_mem0*ADD_mem[2]
	S += (T8_11*ADD[3])-1<C101_mem0*ADD_mem[3]
	S += C101_mem0<=C101

	C101_mem1 = S.Task('C101_mem1', length=1, delay_cost=1)
	C101_mem1 += alt(ADD_mem)
	S += (T111*ADD[0])-1<C101_mem1*ADD_mem[0]
	S += (T111*ADD[1])-1<C101_mem1*ADD_mem[1]
	S += (T111*ADD[2])-1<C101_mem1*ADD_mem[2]
	S += (T111*ADD[3])-1<C101_mem1*ADD_mem[3]
	S += C101_mem1<=C101

	C101_w = S.Task('C101_w', length=1, delay_cost=1)
	C101_w += alt(INPUT_mem_w)
	S += 47 < C101_w
	S += C101-1 <= C101_w

	C011 = S.Task('C011', length=1, delay_cost=1)
	C011 += alt(ADD)

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	C011_mem0 += alt(ADD_mem)
	S += (T10_11*ADD[0])-1<C011_mem0*ADD_mem[0]
	S += (T10_11*ADD[1])-1<C011_mem0*ADD_mem[1]
	S += (T10_11*ADD[2])-1<C011_mem0*ADD_mem[2]
	S += (T10_11*ADD[3])-1<C011_mem0*ADD_mem[3]
	S += C011_mem0<=C011

	C011_mem1 = S.Task('C011_mem1', length=1, delay_cost=1)
	C011_mem1 += alt(ADD_mem)
	S += (T121*ADD[0])-1<C011_mem1*ADD_mem[0]
	S += (T121*ADD[1])-1<C011_mem1*ADD_mem[1]
	S += (T121*ADD[2])-1<C011_mem1*ADD_mem[2]
	S += (T121*ADD[3])-1<C011_mem1*ADD_mem[3]
	S += C011_mem1<=C011

	C011_w = S.Task('C011_w', length=1, delay_cost=1)
	C011_w += alt(INPUT_mem_w)
	S += 47 < C011_w
	S += C011-1 <= C011_w

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sparse_mul1_add4/sparse_mul1_add4_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sparse_mul1_add4_3(0, 0)