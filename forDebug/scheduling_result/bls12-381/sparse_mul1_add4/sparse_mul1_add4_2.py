from pyschedule import Scenario, solvers, plotters, alt

def solve_sparse_mul1_add4_2(ConstStep, ExpStep):
	horizon = 144
	S=Scenario("sparse_mul1_add4_2",horizon = horizon)

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

	T0T5 = S.Task('T0T5', length=1, delay_cost=1)
	S += T0T5 >= 26
	T0T5 += ADD[2]

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

	T3_T3 = S.Task('T3_T3', length=1, delay_cost=1)
	S += T3_T3 >= 32
	T3_T3 += ADD[2]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 33
	T130 += ADD[0]

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

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	S += T8T2 >= 39
	T8T2 += ADD[3]

	T1T4 = S.Task('T1T4', length=7, delay_cost=1)
	S += T1T4 >= 40
	T1T4 += MUL[0]

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

	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	S += T5T4 >= 44
	T5T4 += MUL[0]

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

	T3_T1_in = S.Task('T3_T1_in', length=1, delay_cost=1)
	S += T3_T1_in >= 46
	T3_T1_in += MUL_in[0]

	T3_T1_mem0 = S.Task('T3_T1_mem0', length=1, delay_cost=1)
	S += T3_T1_mem0 >= 46
	T3_T1_mem0 += INPUT_mem_r

	T3_T1_mem1 = S.Task('T3_T1_mem1', length=1, delay_cost=1)
	S += T3_T1_mem1 >= 46
	T3_T1_mem1 += ADD_mem[2]

	T9_1T1 = S.Task('T9_1T1', length=7, delay_cost=1)
	S += T9_1T1 >= 46
	T9_1T1 += MUL[0]

	T3_T1 = S.Task('T3_T1', length=7, delay_cost=1)
	S += T3_T1 >= 47
	T3_T1 += MUL[0]


	# new tasks
	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(ADD)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MUL_mem[0]
	S += T1T4<T11_mem0
	S += T11_mem0<=T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += ADD_mem[3]
	S += T1T5<T11_mem1
	S += T11_mem1<=T11

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(ADD)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += MUL_mem[0]
	S += T2T4<T21_mem0
	S += T21_mem0<=T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += ADD_mem[0]
	S += T2T5<T21_mem1
	S += T21_mem1<=T21

	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += MUL_mem[0]
	S += T0T4<T01_mem0
	S += T01_mem0<=T01

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	T01_mem1 += ADD_mem[2]
	S += T0T5<T01_mem1
	S += T01_mem1<=T01

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += MUL_mem[0]
	S += T3T4<T31_mem0
	S += T31_mem0<=T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += ADD_mem[1]
	S += T3T5<T31_mem1
	S += T31_mem1<=T31

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += MUL_mem[0]
	S += T4T4<T41_mem0
	S += T41_mem0<=T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += ADD_mem[3]
	S += T4T5<T41_mem1
	S += T41_mem1<=T41

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(ADD)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += MUL_mem[0]
	S += T5T4<T51_mem0
	S += T51_mem0<=T51

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	T51_mem1 += ADD_mem[2]
	S += T5T5<T51_mem1
	S += T51_mem1<=T51

	T6_T4_in = S.Task('T6_T4_in', length=1, delay_cost=1)
	T6_T4_in += alt(MUL_in)
	T6_T4 = S.Task('T6_T4', length=7, delay_cost=1)
	T6_T4 += alt(MUL)
	S+=T6_T4>=T6_T4_in

	T6_T4_mem0 = S.Task('T6_T4_mem0', length=1, delay_cost=1)
	T6_T4_mem0 += ADD_mem[2]
	S += T6_T2<T6_T4_mem0
	S += T6_T4_mem0<=T6_T4

	T6_T4_mem1 = S.Task('T6_T4_mem1', length=1, delay_cost=1)
	T6_T4_mem1 += ADD_mem[1]
	S += T6_T3<T6_T4_mem1
	S += T6_T4_mem1<=T6_T4

	T6_T5 = S.Task('T6_T5', length=1, delay_cost=1)
	T6_T5 += alt(ADD)

	T6_T5_mem0 = S.Task('T6_T5_mem0', length=1, delay_cost=1)
	T6_T5_mem0 += MUL_mem[0]
	S += T6_T0<T6_T5_mem0
	S += T6_T5_mem0<=T6_T5

	T6_T5_mem1 = S.Task('T6_T5_mem1', length=1, delay_cost=1)
	T6_T5_mem1 += MUL_mem[0]
	S += T6_T1<T6_T5_mem1
	S += T6_T5_mem1<=T6_T5

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	T6_0 += alt(ADD)

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	T6_0_mem0 += MUL_mem[0]
	S += T6_T0<T6_0_mem0
	S += T6_0_mem0<=T6_0

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	T6_0_mem1 += MUL_mem[0]
	S += T6_T1<T6_0_mem1
	S += T6_0_mem1<=T6_0

	T7_0 = S.Task('T7_0', length=1, delay_cost=1)
	T7_0 += alt(ADD)

	T7_0_mem0 = S.Task('T7_0_mem0', length=1, delay_cost=1)
	T7_0_mem0 += ADD_mem[3]
	S += T30<T7_0_mem0
	S += T7_0_mem0<=T7_0

	T7_0_mem1 = S.Task('T7_0_mem1', length=1, delay_cost=1)
	T7_0_mem1 += ADD_mem[1]
	S += T40<T7_0_mem1
	S += T7_0_mem1<=T7_0

	T6_11 = S.Task('T6_11', length=1, delay_cost=1)
	T6_11 += alt(ADD)

	T6_11_mem0 = S.Task('T6_11_mem0', length=1, delay_cost=1)
	T6_11_mem0 += MUL_mem[0]
	S += T6_1T4<T6_11_mem0
	S += T6_11_mem0<=T6_11

	T6_11_mem1 = S.Task('T6_11_mem1', length=1, delay_cost=1)
	T6_11_mem1 += ADD_mem[1]
	S += T6_1T5<T6_11_mem1
	S += T6_11_mem1<=T6_11

	T6_20 = S.Task('T6_20', length=1, delay_cost=1)
	T6_20 += alt(ADD)

	T6_20_mem0 = S.Task('T6_20_mem0', length=1, delay_cost=1)
	T6_20_mem0 += ADD_mem[0]
	S += T6_10<T6_20_mem0
	S += T6_20_mem0<=T6_20

	T6_20_mem1 = S.Task('T6_20_mem1', length=1, delay_cost=1)
	T6_20_mem1 += ADD_mem[1]
	S += T40<T6_20_mem1
	S += T6_20_mem1<=T6_20

	T3_T4_in = S.Task('T3_T4_in', length=1, delay_cost=1)
	T3_T4_in += alt(MUL_in)
	T3_T4 = S.Task('T3_T4', length=7, delay_cost=1)
	T3_T4 += alt(MUL)
	S+=T3_T4>=T3_T4_in

	T3_T4_mem0 = S.Task('T3_T4_mem0', length=1, delay_cost=1)
	T3_T4_mem0 += ADD_mem[0]
	S += T3_T2<T3_T4_mem0
	S += T3_T4_mem0<=T3_T4

	T3_T4_mem1 = S.Task('T3_T4_mem1', length=1, delay_cost=1)
	T3_T4_mem1 += ADD_mem[2]
	S += T3_T3<T3_T4_mem1
	S += T3_T4_mem1<=T3_T4

	T3_T5 = S.Task('T3_T5', length=1, delay_cost=1)
	T3_T5 += alt(ADD)

	T3_T5_mem0 = S.Task('T3_T5_mem0', length=1, delay_cost=1)
	T3_T5_mem0 += MUL_mem[0]
	S += T3_T0<T3_T5_mem0
	S += T3_T5_mem0<=T3_T5

	T3_T5_mem1 = S.Task('T3_T5_mem1', length=1, delay_cost=1)
	T3_T5_mem1 += MUL_mem[0]
	S += T3_T1<T3_T5_mem1
	S += T3_T5_mem1<=T3_T5

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	T3_0 += alt(ADD)

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	T3_0_mem0 += MUL_mem[0]
	S += T3_T0<T3_0_mem0
	S += T3_0_mem0<=T3_0

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	T3_0_mem1 += MUL_mem[0]
	S += T3_T1<T3_0_mem1
	S += T3_0_mem1<=T3_0

	T4_T4_in = S.Task('T4_T4_in', length=1, delay_cost=1)
	T4_T4_in += alt(MUL_in)
	T4_T4 = S.Task('T4_T4', length=7, delay_cost=1)
	T4_T4 += alt(MUL)
	S+=T4_T4>=T4_T4_in

	T4_T4_mem0 = S.Task('T4_T4_mem0', length=1, delay_cost=1)
	T4_T4_mem0 += ADD_mem[3]
	S += T4_T2<T4_T4_mem0
	S += T4_T4_mem0<=T4_T4

	T4_T4_mem1 = S.Task('T4_T4_mem1', length=1, delay_cost=1)
	T4_T4_mem1 += ADD_mem[1]
	S += T4_T3<T4_T4_mem1
	S += T4_T4_mem1<=T4_T4

	T4_T5 = S.Task('T4_T5', length=1, delay_cost=1)
	T4_T5 += alt(ADD)

	T4_T5_mem0 = S.Task('T4_T5_mem0', length=1, delay_cost=1)
	T4_T5_mem0 += MUL_mem[0]
	S += T4_T0<T4_T5_mem0
	S += T4_T5_mem0<=T4_T5

	T4_T5_mem1 = S.Task('T4_T5_mem1', length=1, delay_cost=1)
	T4_T5_mem1 += MUL_mem[0]
	S += T4_T1<T4_T5_mem1
	S += T4_T5_mem1<=T4_T5

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	T4_0 += alt(ADD)

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	T4_0_mem0 += MUL_mem[0]
	S += T4_T0<T4_0_mem0
	S += T4_0_mem0<=T4_0

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	T4_0_mem1 += MUL_mem[0]
	S += T4_T1<T4_0_mem1
	S += T4_0_mem1<=T4_0

	T8T4_in = S.Task('T8T4_in', length=1, delay_cost=1)
	T8T4_in += alt(MUL_in)
	T8T4 = S.Task('T8T4', length=7, delay_cost=1)
	T8T4 += alt(MUL)
	S+=T8T4>=T8T4_in

	T8T4_mem0 = S.Task('T8T4_mem0', length=1, delay_cost=1)
	T8T4_mem0 += ADD_mem[3]
	S += T8T2<T8T4_mem0
	S += T8T4_mem0<=T8T4

	T8T4_mem1 = S.Task('T8T4_mem1', length=1, delay_cost=1)
	T8T4_mem1 += ADD_mem[1]
	S += T8T3<T8T4_mem1
	S += T8T4_mem1<=T8T4

	T8T5 = S.Task('T8T5', length=1, delay_cost=1)
	T8T5 += alt(ADD)

	T8T5_mem0 = S.Task('T8T5_mem0', length=1, delay_cost=1)
	T8T5_mem0 += MUL_mem[0]
	S += T8T0<T8T5_mem0
	S += T8T5_mem0<=T8T5

	T8T5_mem1 = S.Task('T8T5_mem1', length=1, delay_cost=1)
	T8T5_mem1 += MUL_mem[0]
	S += T8T1<T8T5_mem1
	S += T8T5_mem1<=T8T5

	T80 = S.Task('T80', length=1, delay_cost=1)
	T80 += alt(ADD)

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	T80_mem0 += MUL_mem[0]
	S += T8T0<T80_mem0
	S += T80_mem0<=T80

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	T80_mem1 += MUL_mem[0]
	S += T8T1<T80_mem1
	S += T80_mem1<=T80

	T9_T0_in = S.Task('T9_T0_in', length=1, delay_cost=1)
	T9_T0_in += alt(MUL_in)
	T9_T0 = S.Task('T9_T0', length=7, delay_cost=1)
	T9_T0 += alt(MUL)
	S+=T9_T0>=T9_T0_in

	T9_T0_mem0 = S.Task('T9_T0_mem0', length=1, delay_cost=1)
	T9_T0_mem0 += ADD_mem[2]
	S += T90<T9_T0_mem0
	S += T9_T0_mem0<=T9_T0

	T9_T0_mem1 = S.Task('T9_T0_mem1', length=1, delay_cost=1)
	T9_T0_mem1 += ADD_mem[3]
	S += T100<T9_T0_mem1
	S += T9_T0_mem1<=T9_T0

	T9_T1_in = S.Task('T9_T1_in', length=1, delay_cost=1)
	T9_T1_in += alt(MUL_in)
	T9_T1 = S.Task('T9_T1', length=7, delay_cost=1)
	T9_T1 += alt(MUL)
	S+=T9_T1>=T9_T1_in

	T9_T1_mem0 = S.Task('T9_T1_mem0', length=1, delay_cost=1)
	T9_T1_mem0 += ADD_mem[3]
	S += T91<T9_T1_mem0
	S += T9_T1_mem0<=T9_T1

	T9_T1_mem1 = S.Task('T9_T1_mem1', length=1, delay_cost=1)
	T9_T1_mem1 += ADD_mem[0]
	S += T101<T9_T1_mem1
	S += T9_T1_mem1<=T9_T1

	T9_T2 = S.Task('T9_T2', length=1, delay_cost=1)
	T9_T2 += alt(ADD)

	T9_T2_mem0 = S.Task('T9_T2_mem0', length=1, delay_cost=1)
	T9_T2_mem0 += ADD_mem[2]
	S += T90<T9_T2_mem0
	S += T9_T2_mem0<=T9_T2

	T9_T2_mem1 = S.Task('T9_T2_mem1', length=1, delay_cost=1)
	T9_T2_mem1 += ADD_mem[3]
	S += T91<T9_T2_mem1
	S += T9_T2_mem1<=T9_T2

	T9_T3 = S.Task('T9_T3', length=1, delay_cost=1)
	T9_T3 += alt(ADD)

	T9_T3_mem0 = S.Task('T9_T3_mem0', length=1, delay_cost=1)
	T9_T3_mem0 += ADD_mem[3]
	S += T100<T9_T3_mem0
	S += T9_T3_mem0<=T9_T3

	T9_T3_mem1 = S.Task('T9_T3_mem1', length=1, delay_cost=1)
	T9_T3_mem1 += ADD_mem[0]
	S += T101<T9_T3_mem1
	S += T9_T3_mem1<=T9_T3

	T9_1T4_in = S.Task('T9_1T4_in', length=1, delay_cost=1)
	T9_1T4_in += alt(MUL_in)
	T9_1T4 = S.Task('T9_1T4', length=7, delay_cost=1)
	T9_1T4 += alt(MUL)
	S+=T9_1T4>=T9_1T4_in

	T9_1T4_mem0 = S.Task('T9_1T4_mem0', length=1, delay_cost=1)
	T9_1T4_mem0 += ADD_mem[3]
	S += T9_1T2<T9_1T4_mem0
	S += T9_1T4_mem0<=T9_1T4

	T9_1T4_mem1 = S.Task('T9_1T4_mem1', length=1, delay_cost=1)
	T9_1T4_mem1 += ADD_mem[0]
	S += T9_1T3<T9_1T4_mem1
	S += T9_1T4_mem1<=T9_1T4

	T9_1T5 = S.Task('T9_1T5', length=1, delay_cost=1)
	T9_1T5 += alt(ADD)

	T9_1T5_mem0 = S.Task('T9_1T5_mem0', length=1, delay_cost=1)
	T9_1T5_mem0 += MUL_mem[0]
	S += T9_1T0<T9_1T5_mem0
	S += T9_1T5_mem0<=T9_1T5

	T9_1T5_mem1 = S.Task('T9_1T5_mem1', length=1, delay_cost=1)
	T9_1T5_mem1 += MUL_mem[0]
	S += T9_1T1<T9_1T5_mem1
	S += T9_1T5_mem1<=T9_1T5

	T9_10 = S.Task('T9_10', length=1, delay_cost=1)
	T9_10 += alt(ADD)

	T9_10_mem0 = S.Task('T9_10_mem0', length=1, delay_cost=1)
	T9_10_mem0 += MUL_mem[0]
	S += T9_1T0<T9_10_mem0
	S += T9_10_mem0<=T9_10

	T9_10_mem1 = S.Task('T9_10_mem1', length=1, delay_cost=1)
	T9_10_mem1 += MUL_mem[0]
	S += T9_1T1<T9_10_mem1
	S += T9_10_mem1<=T9_10

	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	T0_0 += alt(ADD)

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	T0_0_mem0 += ADD_mem[1]
	S += T00<T0_0_mem0
	S += T0_0_mem0<=T0_0

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	T0_0_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<T0_0_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<T0_0_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<T0_0_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<T0_0_mem1*ADD_mem[3]
	S += T0_0_mem1<=T0_0

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	T0_1 += alt(ADD)

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	T0_1_mem0 += ADD_mem[1]
	S += T00<T0_1_mem0
	S += T0_1_mem0<=T0_1

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	T0_1_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<T0_1_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<T0_1_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<T0_1_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<T0_1_mem1*ADD_mem[3]
	S += T0_1_mem1<=T0_1

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	T5_0 += alt(ADD)

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	T5_0_mem0 += ADD_mem[2]
	S += T50<T5_0_mem0
	S += T5_0_mem0<=T5_0

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	T5_0_mem1 += alt(ADD_mem)
	S += (T51*ADD[0])-1<T5_0_mem1*ADD_mem[0]
	S += (T51*ADD[1])-1<T5_0_mem1*ADD_mem[1]
	S += (T51*ADD[2])-1<T5_0_mem1*ADD_mem[2]
	S += (T51*ADD[3])-1<T5_0_mem1*ADD_mem[3]
	S += T5_0_mem1<=T5_0

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	T5_1 += alt(ADD)

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	T5_1_mem0 += ADD_mem[2]
	S += T50<T5_1_mem0
	S += T5_1_mem0<=T5_1

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	T5_1_mem1 += alt(ADD_mem)
	S += (T51*ADD[0])-1<T5_1_mem1*ADD_mem[0]
	S += (T51*ADD[1])-1<T5_1_mem1*ADD_mem[1]
	S += (T51*ADD[2])-1<T5_1_mem1*ADD_mem[2]
	S += (T51*ADD[3])-1<T5_1_mem1*ADD_mem[3]
	S += T5_1_mem1<=T5_1

	T6_1 = S.Task('T6_1', length=1, delay_cost=1)
	T6_1 += alt(ADD)

	T6_1_mem0 = S.Task('T6_1_mem0', length=1, delay_cost=1)
	T6_1_mem0 += alt(MUL_mem)
	S += (T6_T4*MUL[0])-1<T6_1_mem0*MUL_mem[0]
	S += T6_1_mem0<=T6_1

	T6_1_mem1 = S.Task('T6_1_mem1', length=1, delay_cost=1)
	T6_1_mem1 += alt(ADD_mem)
	S += (T6_T5*ADD[0])-1<T6_1_mem1*ADD_mem[0]
	S += (T6_T5*ADD[1])-1<T6_1_mem1*ADD_mem[1]
	S += (T6_T5*ADD[2])-1<T6_1_mem1*ADD_mem[2]
	S += (T6_T5*ADD[3])-1<T6_1_mem1*ADD_mem[3]
	S += T6_1_mem1<=T6_1

	T7_1 = S.Task('T7_1', length=1, delay_cost=1)
	T7_1 += alt(ADD)

	T7_1_mem0 = S.Task('T7_1_mem0', length=1, delay_cost=1)
	T7_1_mem0 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T7_1_mem0*ADD_mem[0]
	S += (T31*ADD[1])-1<T7_1_mem0*ADD_mem[1]
	S += (T31*ADD[2])-1<T7_1_mem0*ADD_mem[2]
	S += (T31*ADD[3])-1<T7_1_mem0*ADD_mem[3]
	S += T7_1_mem0<=T7_1

	T7_1_mem1 = S.Task('T7_1_mem1', length=1, delay_cost=1)
	T7_1_mem1 += alt(ADD_mem)
	S += (T41*ADD[0])-1<T7_1_mem1*ADD_mem[0]
	S += (T41*ADD[1])-1<T7_1_mem1*ADD_mem[1]
	S += (T41*ADD[2])-1<T7_1_mem1*ADD_mem[2]
	S += (T41*ADD[3])-1<T7_1_mem1*ADD_mem[3]
	S += T7_1_mem1<=T7_1

	T7_10 = S.Task('T7_10', length=1, delay_cost=1)
	T7_10 += alt(ADD)

	T7_10_mem0 = S.Task('T7_10_mem0', length=1, delay_cost=1)
	T7_10_mem0 += alt(ADD_mem)
	S += (T6_0*ADD[0])-1<T7_10_mem0*ADD_mem[0]
	S += (T6_0*ADD[1])-1<T7_10_mem0*ADD_mem[1]
	S += (T6_0*ADD[2])-1<T7_10_mem0*ADD_mem[2]
	S += (T6_0*ADD[3])-1<T7_10_mem0*ADD_mem[3]
	S += T7_10_mem0<=T7_10

	T7_10_mem1 = S.Task('T7_10_mem1', length=1, delay_cost=1)
	T7_10_mem1 += alt(ADD_mem)
	S += (T7_0*ADD[0])-1<T7_10_mem1*ADD_mem[0]
	S += (T7_0*ADD[1])-1<T7_10_mem1*ADD_mem[1]
	S += (T7_0*ADD[2])-1<T7_10_mem1*ADD_mem[2]
	S += (T7_0*ADD[3])-1<T7_10_mem1*ADD_mem[3]
	S += T7_10_mem1<=T7_10

	T6_21 = S.Task('T6_21', length=1, delay_cost=1)
	T6_21 += alt(ADD)

	T6_21_mem0 = S.Task('T6_21_mem0', length=1, delay_cost=1)
	T6_21_mem0 += alt(ADD_mem)
	S += (T6_11*ADD[0])-1<T6_21_mem0*ADD_mem[0]
	S += (T6_11*ADD[1])-1<T6_21_mem0*ADD_mem[1]
	S += (T6_11*ADD[2])-1<T6_21_mem0*ADD_mem[2]
	S += (T6_11*ADD[3])-1<T6_21_mem0*ADD_mem[3]
	S += T6_21_mem0<=T6_21

	T6_21_mem1 = S.Task('T6_21_mem1', length=1, delay_cost=1)
	T6_21_mem1 += alt(ADD_mem)
	S += (T41*ADD[0])-1<T6_21_mem1*ADD_mem[0]
	S += (T41*ADD[1])-1<T6_21_mem1*ADD_mem[1]
	S += (T41*ADD[2])-1<T6_21_mem1*ADD_mem[2]
	S += (T41*ADD[3])-1<T6_21_mem1*ADD_mem[3]
	S += T6_21_mem1<=T6_21

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

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	T4_1 += alt(ADD)

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	T4_1_mem0 += alt(MUL_mem)
	S += (T4_T4*MUL[0])-1<T4_1_mem0*MUL_mem[0]
	S += T4_1_mem0<=T4_1

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	T4_1_mem1 += alt(ADD_mem)
	S += (T4_T5*ADD[0])-1<T4_1_mem1*ADD_mem[0]
	S += (T4_T5*ADD[1])-1<T4_1_mem1*ADD_mem[1]
	S += (T4_T5*ADD[2])-1<T4_1_mem1*ADD_mem[2]
	S += (T4_T5*ADD[3])-1<T4_1_mem1*ADD_mem[3]
	S += T4_1_mem1<=T4_1

	T81 = S.Task('T81', length=1, delay_cost=1)
	T81 += alt(ADD)

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	T81_mem0 += alt(MUL_mem)
	S += (T8T4*MUL[0])-1<T81_mem0*MUL_mem[0]
	S += T81_mem0<=T81

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	T81_mem1 += alt(ADD_mem)
	S += (T8T5*ADD[0])-1<T81_mem1*ADD_mem[0]
	S += (T8T5*ADD[1])-1<T81_mem1*ADD_mem[1]
	S += (T8T5*ADD[2])-1<T81_mem1*ADD_mem[2]
	S += (T8T5*ADD[3])-1<T81_mem1*ADD_mem[3]
	S += T81_mem1<=T81

	T9_T4_in = S.Task('T9_T4_in', length=1, delay_cost=1)
	T9_T4_in += alt(MUL_in)
	T9_T4 = S.Task('T9_T4', length=7, delay_cost=1)
	T9_T4 += alt(MUL)
	S+=T9_T4>=T9_T4_in

	T9_T4_mem0 = S.Task('T9_T4_mem0', length=1, delay_cost=1)
	T9_T4_mem0 += alt(ADD_mem)
	S += (T9_T2*ADD[0])-1<T9_T4_mem0*ADD_mem[0]
	S += (T9_T2*ADD[1])-1<T9_T4_mem0*ADD_mem[1]
	S += (T9_T2*ADD[2])-1<T9_T4_mem0*ADD_mem[2]
	S += (T9_T2*ADD[3])-1<T9_T4_mem0*ADD_mem[3]
	S += T9_T4_mem0<=T9_T4

	T9_T4_mem1 = S.Task('T9_T4_mem1', length=1, delay_cost=1)
	T9_T4_mem1 += alt(ADD_mem)
	S += (T9_T3*ADD[0])-1<T9_T4_mem1*ADD_mem[0]
	S += (T9_T3*ADD[1])-1<T9_T4_mem1*ADD_mem[1]
	S += (T9_T3*ADD[2])-1<T9_T4_mem1*ADD_mem[2]
	S += (T9_T3*ADD[3])-1<T9_T4_mem1*ADD_mem[3]
	S += T9_T4_mem1<=T9_T4

	T9_T5 = S.Task('T9_T5', length=1, delay_cost=1)
	T9_T5 += alt(ADD)

	T9_T5_mem0 = S.Task('T9_T5_mem0', length=1, delay_cost=1)
	T9_T5_mem0 += alt(MUL_mem)
	S += (T9_T0*MUL[0])-1<T9_T5_mem0*MUL_mem[0]
	S += T9_T5_mem0<=T9_T5

	T9_T5_mem1 = S.Task('T9_T5_mem1', length=1, delay_cost=1)
	T9_T5_mem1 += alt(MUL_mem)
	S += (T9_T1*MUL[0])-1<T9_T5_mem1*MUL_mem[0]
	S += T9_T5_mem1<=T9_T5

	T9_0 = S.Task('T9_0', length=1, delay_cost=1)
	T9_0 += alt(ADD)

	T9_0_mem0 = S.Task('T9_0_mem0', length=1, delay_cost=1)
	T9_0_mem0 += alt(MUL_mem)
	S += (T9_T0*MUL[0])-1<T9_0_mem0*MUL_mem[0]
	S += T9_0_mem0<=T9_0

	T9_0_mem1 = S.Task('T9_0_mem1', length=1, delay_cost=1)
	T9_0_mem1 += alt(MUL_mem)
	S += (T9_T1*MUL[0])-1<T9_0_mem1*MUL_mem[0]
	S += T9_0_mem1<=T9_0

	T10_0 = S.Task('T10_0', length=1, delay_cost=1)
	T10_0 += alt(ADD)

	T10_0_mem0 = S.Task('T10_0_mem0', length=1, delay_cost=1)
	T10_0_mem0 += alt(ADD_mem)
	S += (T3_0*ADD[0])-1<T10_0_mem0*ADD_mem[0]
	S += (T3_0*ADD[1])-1<T10_0_mem0*ADD_mem[1]
	S += (T3_0*ADD[2])-1<T10_0_mem0*ADD_mem[2]
	S += (T3_0*ADD[3])-1<T10_0_mem0*ADD_mem[3]
	S += T10_0_mem0<=T10_0

	T10_0_mem1 = S.Task('T10_0_mem1', length=1, delay_cost=1)
	T10_0_mem1 += alt(ADD_mem)
	S += (T4_0*ADD[0])-1<T10_0_mem1*ADD_mem[0]
	S += (T4_0*ADD[1])-1<T10_0_mem1*ADD_mem[1]
	S += (T4_0*ADD[2])-1<T10_0_mem1*ADD_mem[2]
	S += (T4_0*ADD[3])-1<T10_0_mem1*ADD_mem[3]
	S += T10_0_mem1<=T10_0

	T9_11 = S.Task('T9_11', length=1, delay_cost=1)
	T9_11 += alt(ADD)

	T9_11_mem0 = S.Task('T9_11_mem0', length=1, delay_cost=1)
	T9_11_mem0 += alt(MUL_mem)
	S += (T9_1T4*MUL[0])-1<T9_11_mem0*MUL_mem[0]
	S += T9_11_mem0<=T9_11

	T9_11_mem1 = S.Task('T9_11_mem1', length=1, delay_cost=1)
	T9_11_mem1 += alt(ADD_mem)
	S += (T9_1T5*ADD[0])-1<T9_11_mem1*ADD_mem[0]
	S += (T9_1T5*ADD[1])-1<T9_11_mem1*ADD_mem[1]
	S += (T9_1T5*ADD[2])-1<T9_11_mem1*ADD_mem[2]
	S += (T9_1T5*ADD[3])-1<T9_11_mem1*ADD_mem[3]
	S += T9_11_mem1<=T9_11

	T9_20 = S.Task('T9_20', length=1, delay_cost=1)
	T9_20 += alt(ADD)

	T9_20_mem0 = S.Task('T9_20_mem0', length=1, delay_cost=1)
	T9_20_mem0 += alt(ADD_mem)
	S += (T9_10*ADD[0])-1<T9_20_mem0*ADD_mem[0]
	S += (T9_10*ADD[1])-1<T9_20_mem0*ADD_mem[1]
	S += (T9_10*ADD[2])-1<T9_20_mem0*ADD_mem[2]
	S += (T9_10*ADD[3])-1<T9_20_mem0*ADD_mem[3]
	S += T9_20_mem0<=T9_20

	T9_20_mem1 = S.Task('T9_20_mem1', length=1, delay_cost=1)
	T9_20_mem1 += alt(ADD_mem)
	S += (T4_0*ADD[0])-1<T9_20_mem1*ADD_mem[0]
	S += (T4_0*ADD[1])-1<T9_20_mem1*ADD_mem[1]
	S += (T4_0*ADD[2])-1<T9_20_mem1*ADD_mem[2]
	S += (T4_0*ADD[3])-1<T9_20_mem1*ADD_mem[3]
	S += T9_20_mem1<=T9_20

	T13_0 = S.Task('T13_0', length=1, delay_cost=1)
	T13_0 += alt(ADD)

	T13_0_mem0 = S.Task('T13_0_mem0', length=1, delay_cost=1)
	T13_0_mem0 += ADD_mem[3]
	S += T20<T13_0_mem0
	S += T13_0_mem0<=T13_0

	T13_0_mem1 = S.Task('T13_0_mem1', length=1, delay_cost=1)
	T13_0_mem1 += alt(ADD_mem)
	S += (T6_20*ADD[0])-1<T13_0_mem1*ADD_mem[0]
	S += (T6_20*ADD[1])-1<T13_0_mem1*ADD_mem[1]
	S += (T6_20*ADD[2])-1<T13_0_mem1*ADD_mem[2]
	S += (T6_20*ADD[3])-1<T13_0_mem1*ADD_mem[3]
	S += T13_0_mem1<=T13_0

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	T2_0 += alt(ADD)

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	T2_0_mem0 += ADD_mem[3]
	S += T20<T2_0_mem0
	S += T2_0_mem0<=T2_0

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	T2_0_mem1 += alt(ADD_mem)
	S += (T21*ADD[0])-1<T2_0_mem1*ADD_mem[0]
	S += (T21*ADD[1])-1<T2_0_mem1*ADD_mem[1]
	S += (T21*ADD[2])-1<T2_0_mem1*ADD_mem[2]
	S += (T21*ADD[3])-1<T2_0_mem1*ADD_mem[3]
	S += T2_0_mem1<=T2_0

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	T2_1 += alt(ADD)

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	T2_1_mem0 += ADD_mem[3]
	S += T20<T2_1_mem0
	S += T2_1_mem0<=T2_1

	T2_1_mem1 = S.Task('T2_1_mem1', length=1, delay_cost=1)
	T2_1_mem1 += alt(ADD_mem)
	S += (T21*ADD[0])-1<T2_1_mem1*ADD_mem[0]
	S += (T21*ADD[1])-1<T2_1_mem1*ADD_mem[1]
	S += (T21*ADD[2])-1<T2_1_mem1*ADD_mem[2]
	S += (T21*ADD[3])-1<T2_1_mem1*ADD_mem[3]
	S += T2_1_mem1<=T2_1

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	T5_10 += alt(ADD)

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	T5_10_mem0 += ADD_mem[3]
	S += T30<T5_10_mem0
	S += T5_10_mem0<=T5_10

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	T5_10_mem1 += alt(ADD_mem)
	S += (T5_0*ADD[0])-1<T5_10_mem1*ADD_mem[0]
	S += (T5_0*ADD[1])-1<T5_10_mem1*ADD_mem[1]
	S += (T5_0*ADD[2])-1<T5_10_mem1*ADD_mem[2]
	S += (T5_0*ADD[3])-1<T5_10_mem1*ADD_mem[3]
	S += T5_10_mem1<=T5_10

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	T5_11 += alt(ADD)

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	T5_11_mem0 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T5_11_mem0*ADD_mem[0]
	S += (T31*ADD[1])-1<T5_11_mem0*ADD_mem[1]
	S += (T31*ADD[2])-1<T5_11_mem0*ADD_mem[2]
	S += (T31*ADD[3])-1<T5_11_mem0*ADD_mem[3]
	S += T5_11_mem0<=T5_11

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	T5_11_mem1 += alt(ADD_mem)
	S += (T5_1*ADD[0])-1<T5_11_mem1*ADD_mem[0]
	S += (T5_1*ADD[1])-1<T5_11_mem1*ADD_mem[1]
	S += (T5_1*ADD[2])-1<T5_11_mem1*ADD_mem[2]
	S += (T5_1*ADD[3])-1<T5_11_mem1*ADD_mem[3]
	S += T5_11_mem1<=T5_11

	T7_11 = S.Task('T7_11', length=1, delay_cost=1)
	T7_11 += alt(ADD)

	T7_11_mem0 = S.Task('T7_11_mem0', length=1, delay_cost=1)
	T7_11_mem0 += alt(ADD_mem)
	S += (T6_1*ADD[0])-1<T7_11_mem0*ADD_mem[0]
	S += (T6_1*ADD[1])-1<T7_11_mem0*ADD_mem[1]
	S += (T6_1*ADD[2])-1<T7_11_mem0*ADD_mem[2]
	S += (T6_1*ADD[3])-1<T7_11_mem0*ADD_mem[3]
	S += T7_11_mem0<=T7_11

	T7_11_mem1 = S.Task('T7_11_mem1', length=1, delay_cost=1)
	T7_11_mem1 += alt(ADD_mem)
	S += (T7_1*ADD[0])-1<T7_11_mem1*ADD_mem[0]
	S += (T7_1*ADD[1])-1<T7_11_mem1*ADD_mem[1]
	S += (T7_1*ADD[2])-1<T7_11_mem1*ADD_mem[2]
	S += (T7_1*ADD[3])-1<T7_11_mem1*ADD_mem[3]
	S += T7_11_mem1<=T7_11

	T8_0 = S.Task('T8_0', length=1, delay_cost=1)
	T8_0 += alt(ADD)

	T8_0_mem0 = S.Task('T8_0_mem0', length=1, delay_cost=1)
	T8_0_mem0 += alt(ADD_mem)
	S += (T80*ADD[0])-1<T8_0_mem0*ADD_mem[0]
	S += (T80*ADD[1])-1<T8_0_mem0*ADD_mem[1]
	S += (T80*ADD[2])-1<T8_0_mem0*ADD_mem[2]
	S += (T80*ADD[3])-1<T8_0_mem0*ADD_mem[3]
	S += T8_0_mem0<=T8_0

	T8_0_mem1 = S.Task('T8_0_mem1', length=1, delay_cost=1)
	T8_0_mem1 += alt(ADD_mem)
	S += (T81*ADD[0])-1<T8_0_mem1*ADD_mem[0]
	S += (T81*ADD[1])-1<T8_0_mem1*ADD_mem[1]
	S += (T81*ADD[2])-1<T8_0_mem1*ADD_mem[2]
	S += (T81*ADD[3])-1<T8_0_mem1*ADD_mem[3]
	S += T8_0_mem1<=T8_0

	T8_1 = S.Task('T8_1', length=1, delay_cost=1)
	T8_1 += alt(ADD)

	T8_1_mem0 = S.Task('T8_1_mem0', length=1, delay_cost=1)
	T8_1_mem0 += alt(ADD_mem)
	S += (T80*ADD[0])-1<T8_1_mem0*ADD_mem[0]
	S += (T80*ADD[1])-1<T8_1_mem0*ADD_mem[1]
	S += (T80*ADD[2])-1<T8_1_mem0*ADD_mem[2]
	S += (T80*ADD[3])-1<T8_1_mem0*ADD_mem[3]
	S += T8_1_mem0<=T8_1

	T8_1_mem1 = S.Task('T8_1_mem1', length=1, delay_cost=1)
	T8_1_mem1 += alt(ADD_mem)
	S += (T81*ADD[0])-1<T8_1_mem1*ADD_mem[0]
	S += (T81*ADD[1])-1<T8_1_mem1*ADD_mem[1]
	S += (T81*ADD[2])-1<T8_1_mem1*ADD_mem[2]
	S += (T81*ADD[3])-1<T8_1_mem1*ADD_mem[3]
	S += T8_1_mem1<=T8_1

	T9_1 = S.Task('T9_1', length=1, delay_cost=1)
	T9_1 += alt(ADD)

	T9_1_mem0 = S.Task('T9_1_mem0', length=1, delay_cost=1)
	T9_1_mem0 += alt(MUL_mem)
	S += (T9_T4*MUL[0])-1<T9_1_mem0*MUL_mem[0]
	S += T9_1_mem0<=T9_1

	T9_1_mem1 = S.Task('T9_1_mem1', length=1, delay_cost=1)
	T9_1_mem1 += alt(ADD_mem)
	S += (T9_T5*ADD[0])-1<T9_1_mem1*ADD_mem[0]
	S += (T9_T5*ADD[1])-1<T9_1_mem1*ADD_mem[1]
	S += (T9_T5*ADD[2])-1<T9_1_mem1*ADD_mem[2]
	S += (T9_T5*ADD[3])-1<T9_1_mem1*ADD_mem[3]
	S += T9_1_mem1<=T9_1

	T10_1 = S.Task('T10_1', length=1, delay_cost=1)
	T10_1 += alt(ADD)

	T10_1_mem0 = S.Task('T10_1_mem0', length=1, delay_cost=1)
	T10_1_mem0 += alt(ADD_mem)
	S += (T3_1*ADD[0])-1<T10_1_mem0*ADD_mem[0]
	S += (T3_1*ADD[1])-1<T10_1_mem0*ADD_mem[1]
	S += (T3_1*ADD[2])-1<T10_1_mem0*ADD_mem[2]
	S += (T3_1*ADD[3])-1<T10_1_mem0*ADD_mem[3]
	S += T10_1_mem0<=T10_1

	T10_1_mem1 = S.Task('T10_1_mem1', length=1, delay_cost=1)
	T10_1_mem1 += alt(ADD_mem)
	S += (T4_1*ADD[0])-1<T10_1_mem1*ADD_mem[0]
	S += (T4_1*ADD[1])-1<T10_1_mem1*ADD_mem[1]
	S += (T4_1*ADD[2])-1<T10_1_mem1*ADD_mem[2]
	S += (T4_1*ADD[3])-1<T10_1_mem1*ADD_mem[3]
	S += T10_1_mem1<=T10_1

	T10_10 = S.Task('T10_10', length=1, delay_cost=1)
	T10_10 += alt(ADD)

	T10_10_mem0 = S.Task('T10_10_mem0', length=1, delay_cost=1)
	T10_10_mem0 += alt(ADD_mem)
	S += (T9_0*ADD[0])-1<T10_10_mem0*ADD_mem[0]
	S += (T9_0*ADD[1])-1<T10_10_mem0*ADD_mem[1]
	S += (T9_0*ADD[2])-1<T10_10_mem0*ADD_mem[2]
	S += (T9_0*ADD[3])-1<T10_10_mem0*ADD_mem[3]
	S += T10_10_mem0<=T10_10

	T10_10_mem1 = S.Task('T10_10_mem1', length=1, delay_cost=1)
	T10_10_mem1 += alt(ADD_mem)
	S += (T10_0*ADD[0])-1<T10_10_mem1*ADD_mem[0]
	S += (T10_0*ADD[1])-1<T10_10_mem1*ADD_mem[1]
	S += (T10_0*ADD[2])-1<T10_10_mem1*ADD_mem[2]
	S += (T10_0*ADD[3])-1<T10_10_mem1*ADD_mem[3]
	S += T10_10_mem1<=T10_10

	T9_21 = S.Task('T9_21', length=1, delay_cost=1)
	T9_21 += alt(ADD)

	T9_21_mem0 = S.Task('T9_21_mem0', length=1, delay_cost=1)
	T9_21_mem0 += alt(ADD_mem)
	S += (T9_11*ADD[0])-1<T9_21_mem0*ADD_mem[0]
	S += (T9_11*ADD[1])-1<T9_21_mem0*ADD_mem[1]
	S += (T9_11*ADD[2])-1<T9_21_mem0*ADD_mem[2]
	S += (T9_11*ADD[3])-1<T9_21_mem0*ADD_mem[3]
	S += T9_21_mem0<=T9_21

	T9_21_mem1 = S.Task('T9_21_mem1', length=1, delay_cost=1)
	T9_21_mem1 += alt(ADD_mem)
	S += (T4_1*ADD[0])-1<T9_21_mem1*ADD_mem[0]
	S += (T4_1*ADD[1])-1<T9_21_mem1*ADD_mem[1]
	S += (T4_1*ADD[2])-1<T9_21_mem1*ADD_mem[2]
	S += (T4_1*ADD[3])-1<T9_21_mem1*ADD_mem[3]
	S += T9_21_mem1<=T9_21

	T120 = S.Task('T120', length=1, delay_cost=1)
	T120 += alt(ADD)

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	T120_mem0 += ADD_mem[1]
	S += T10<T120_mem0
	S += T120_mem0<=T120

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	T120_mem1 += alt(ADD_mem)
	S += (T7_10*ADD[0])-1<T120_mem1*ADD_mem[0]
	S += (T7_10*ADD[1])-1<T120_mem1*ADD_mem[1]
	S += (T7_10*ADD[2])-1<T120_mem1*ADD_mem[2]
	S += (T7_10*ADD[3])-1<T120_mem1*ADD_mem[3]
	S += T120_mem1<=T120

	T13_1 = S.Task('T13_1', length=1, delay_cost=1)
	T13_1 += alt(ADD)

	T13_1_mem0 = S.Task('T13_1_mem0', length=1, delay_cost=1)
	T13_1_mem0 += alt(ADD_mem)
	S += (T21*ADD[0])-1<T13_1_mem0*ADD_mem[0]
	S += (T21*ADD[1])-1<T13_1_mem0*ADD_mem[1]
	S += (T21*ADD[2])-1<T13_1_mem0*ADD_mem[2]
	S += (T21*ADD[3])-1<T13_1_mem0*ADD_mem[3]
	S += T13_1_mem0<=T13_1

	T13_1_mem1 = S.Task('T13_1_mem1', length=1, delay_cost=1)
	T13_1_mem1 += alt(ADD_mem)
	S += (T6_21*ADD[0])-1<T13_1_mem1*ADD_mem[0]
	S += (T6_21*ADD[1])-1<T13_1_mem1*ADD_mem[1]
	S += (T6_21*ADD[2])-1<T13_1_mem1*ADD_mem[2]
	S += (T6_21*ADD[3])-1<T13_1_mem1*ADD_mem[3]
	S += T13_1_mem1<=T13_1

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sparse_mul1_add4/sparse_mul1_add4_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sparse_mul1_add4_2(0, 0)