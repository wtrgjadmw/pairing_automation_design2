from pyschedule import Scenario, solvers, plotters, alt

def solve_sparse_mul1_add4_1(ConstStep, ExpStep):
	horizon = 133
	S=Scenario("sparse_mul1_add4_1",horizon = horizon)

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

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	S += T2T0_in >= 12
	T2T0_in += MUL_in[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 12
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 12
	T2T0_mem1 += INPUT_mem_r

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

	T0T0 = S.Task('T0T0', length=7, delay_cost=1)
	S += T0T0 >= 14
	T0T0 += MUL[0]

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

	T9_1T2 = S.Task('T9_1T2', length=1, delay_cost=1)
	S += T9_1T2 >= 15
	T9_1T2 += ADD[3]

	T0T3 = S.Task('T0T3', length=1, delay_cost=1)
	S += T0T3 >= 16
	T0T3 += ADD[0]

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

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	S += T2T3 >= 19
	T2T3 += ADD[0]

	T3_T2_mem0 = S.Task('T3_T2_mem0', length=1, delay_cost=1)
	S += T3_T2_mem0 >= 19
	T3_T2_mem0 += INPUT_mem_r

	T3_T2_mem1 = S.Task('T3_T2_mem1', length=1, delay_cost=1)
	S += T3_T2_mem1 >= 19
	T3_T2_mem1 += INPUT_mem_r

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	S += T160_mem0 >= 20
	T160_mem0 += INPUT_mem_r

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	S += T160_mem1 >= 20
	T160_mem1 += INPUT_mem_r

	T3_T2 = S.Task('T3_T2', length=1, delay_cost=1)
	S += T3_T2 >= 20
	T3_T2 += ADD[0]

	T160 = S.Task('T160', length=1, delay_cost=1)
	S += T160 >= 21
	T160 += ADD[1]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 21
	T3T2_mem0 += INPUT_mem_r

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 21
	T3T2_mem1 += INPUT_mem_r

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 22
	T151_mem0 += INPUT_mem_r

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 22
	T151_mem1 += INPUT_mem_r

	T3T2 = S.Task('T3T2', length=1, delay_cost=1)
	S += T3T2 >= 22
	T3T2 += ADD[0]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 23
	T150_mem0 += INPUT_mem_r

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 23
	T150_mem1 += INPUT_mem_r

	T151 = S.Task('T151', length=1, delay_cost=1)
	S += T151 >= 23
	T151 += ADD[0]

	T150 = S.Task('T150', length=1, delay_cost=1)
	S += T150 >= 24
	T150 += ADD[0]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	S += T161_mem0 >= 24
	T161_mem0 += INPUT_mem_r

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	S += T161_mem1 >= 24
	T161_mem1 += INPUT_mem_r

	T161 = S.Task('T161', length=1, delay_cost=1)
	S += T161 >= 25
	T161 += ADD[1]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 25
	T2T2_mem0 += INPUT_mem_r

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 25
	T2T2_mem1 += INPUT_mem_r

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	S += T2T2 >= 26
	T2T2 += ADD[0]

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	S += T4T2_mem0 >= 26
	T4T2_mem0 += INPUT_mem_r

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	S += T4T2_mem1 >= 26
	T4T2_mem1 += INPUT_mem_r

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	S += T4T2 >= 27
	T4T2 += ADD[1]

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	S += T4T3_mem0 >= 27
	T4T3_mem0 += INPUT_mem_r

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	S += T4T3_mem1 >= 27
	T4T3_mem1 += INPUT_mem_r

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 28
	T141_mem0 += INPUT_mem_r

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 28
	T141_mem1 += INPUT_mem_r

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	S += T4T3 >= 28
	T4T3 += ADD[2]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 29
	T140_mem0 += INPUT_mem_r

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 29
	T140_mem1 += INPUT_mem_r

	T141 = S.Task('T141', length=1, delay_cost=1)
	S += T141 >= 29
	T141 += ADD[2]

	T140 = S.Task('T140', length=1, delay_cost=1)
	S += T140 >= 30
	T140 += ADD[1]

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	S += T1T2_mem0 >= 30
	T1T2_mem0 += INPUT_mem_r

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	S += T1T2_mem1 >= 30
	T1T2_mem1 += INPUT_mem_r

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 31
	T131_mem0 += INPUT_mem_r

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 31
	T131_mem1 += INPUT_mem_r

	T1T2 = S.Task('T1T2', length=1, delay_cost=1)
	S += T1T2 >= 31
	T1T2 += ADD[3]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 32
	T130_mem0 += INPUT_mem_r

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 32
	T130_mem1 += INPUT_mem_r

	T131 = S.Task('T131', length=1, delay_cost=1)
	S += T131 >= 32
	T131 += ADD[0]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 33
	T130 += ADD[0]

	T6_1T3_mem0 = S.Task('T6_1T3_mem0', length=1, delay_cost=1)
	S += T6_1T3_mem0 >= 33
	T6_1T3_mem0 += INPUT_mem_r

	T6_1T3_mem1 = S.Task('T6_1T3_mem1', length=1, delay_cost=1)
	S += T6_1T3_mem1 >= 33
	T6_1T3_mem1 += INPUT_mem_r

	T6_1T2_mem0 = S.Task('T6_1T2_mem0', length=1, delay_cost=1)
	S += T6_1T2_mem0 >= 34
	T6_1T2_mem0 += INPUT_mem_r

	T6_1T2_mem1 = S.Task('T6_1T2_mem1', length=1, delay_cost=1)
	S += T6_1T2_mem1 >= 34
	T6_1T2_mem1 += INPUT_mem_r

	T6_1T3 = S.Task('T6_1T3', length=1, delay_cost=1)
	S += T6_1T3 >= 34
	T6_1T3 += ADD[1]

	T6_1T2 = S.Task('T6_1T2', length=1, delay_cost=1)
	S += T6_1T2 >= 35
	T6_1T2 += ADD[0]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 35
	T71_mem0 += INPUT_mem_r

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 35
	T71_mem1 += INPUT_mem_r

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

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 37
	T70 += ADD[3]

	T1T3 = S.Task('T1T3', length=1, delay_cost=1)
	S += T1T3 >= 38
	T1T3 += ADD[3]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 38
	T61_mem0 += INPUT_mem_r

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 38
	T61_mem1 += INPUT_mem_r

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 39
	T60_mem0 += INPUT_mem_r

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 39
	T60_mem1 += INPUT_mem_r

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 39
	T61 += ADD[0]

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	S += T5T3_mem0 >= 40
	T5T3_mem0 += INPUT_mem_r

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	S += T5T3_mem1 >= 40
	T5T3_mem1 += INPUT_mem_r

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 40
	T60 += ADD[0]

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	S += T5T2_mem0 >= 41
	T5T2_mem0 += INPUT_mem_r

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	S += T5T2_mem1 >= 41
	T5T2_mem1 += INPUT_mem_r

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	S += T5T3 >= 41
	T5T3 += ADD[1]

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	S += T5T2 >= 42
	T5T2 += ADD[2]


	# new tasks
	T1T4_in = S.Task('T1T4_in', length=1, delay_cost=1)
	T1T4_in += alt(MUL_in)
	T1T4 = S.Task('T1T4', length=7, delay_cost=1)
	T1T4 += alt(MUL)
	S+=T1T4>=T1T4_in

	T1T4_mem0 = S.Task('T1T4_mem0', length=1, delay_cost=1)
	T1T4_mem0 += ADD_mem[3]
	S += T1T2<T1T4_mem0
	S += T1T4_mem0<=T1T4

	T1T4_mem1 = S.Task('T1T4_mem1', length=1, delay_cost=1)
	T1T4_mem1 += ADD_mem[3]
	S += T1T3<T1T4_mem1
	S += T1T4_mem1<=T1T4

	T1T5 = S.Task('T1T5', length=1, delay_cost=1)
	T1T5 += alt(ADD)

	T1T5_mem0 = S.Task('T1T5_mem0', length=1, delay_cost=1)
	T1T5_mem0 += MUL_mem[0]
	S += T1T0<T1T5_mem0
	S += T1T5_mem0<=T1T5

	T1T5_mem1 = S.Task('T1T5_mem1', length=1, delay_cost=1)
	T1T5_mem1 += MUL_mem[0]
	S += T1T1<T1T5_mem1
	S += T1T5_mem1<=T1T5

	T10 = S.Task('T10', length=1, delay_cost=1)
	T10 += alt(ADD)

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += MUL_mem[0]
	S += T1T0<T10_mem0
	S += T10_mem0<=T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += MUL_mem[0]
	S += T1T1<T10_mem1
	S += T10_mem1<=T10

	T2T4_in = S.Task('T2T4_in', length=1, delay_cost=1)
	T2T4_in += alt(MUL_in)
	T2T4 = S.Task('T2T4', length=7, delay_cost=1)
	T2T4 += alt(MUL)
	S+=T2T4>=T2T4_in

	T2T4_mem0 = S.Task('T2T4_mem0', length=1, delay_cost=1)
	T2T4_mem0 += ADD_mem[0]
	S += T2T2<T2T4_mem0
	S += T2T4_mem0<=T2T4

	T2T4_mem1 = S.Task('T2T4_mem1', length=1, delay_cost=1)
	T2T4_mem1 += ADD_mem[0]
	S += T2T3<T2T4_mem1
	S += T2T4_mem1<=T2T4

	T2T5 = S.Task('T2T5', length=1, delay_cost=1)
	T2T5 += alt(ADD)

	T2T5_mem0 = S.Task('T2T5_mem0', length=1, delay_cost=1)
	T2T5_mem0 += MUL_mem[0]
	S += T2T0<T2T5_mem0
	S += T2T5_mem0<=T2T5

	T2T5_mem1 = S.Task('T2T5_mem1', length=1, delay_cost=1)
	T2T5_mem1 += MUL_mem[0]
	S += T2T1<T2T5_mem1
	S += T2T5_mem1<=T2T5

	T20 = S.Task('T20', length=1, delay_cost=1)
	T20 += alt(ADD)

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += MUL_mem[0]
	S += T2T0<T20_mem0
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += MUL_mem[0]
	S += T2T1<T20_mem1
	S += T20_mem1<=T20

	T0T4_in = S.Task('T0T4_in', length=1, delay_cost=1)
	T0T4_in += alt(MUL_in)
	T0T4 = S.Task('T0T4', length=7, delay_cost=1)
	T0T4 += alt(MUL)
	S+=T0T4>=T0T4_in

	T0T4_mem0 = S.Task('T0T4_mem0', length=1, delay_cost=1)
	T0T4_mem0 += ADD_mem[0]
	S += T0T2<T0T4_mem0
	S += T0T4_mem0<=T0T4

	T0T4_mem1 = S.Task('T0T4_mem1', length=1, delay_cost=1)
	T0T4_mem1 += ADD_mem[0]
	S += T0T3<T0T4_mem1
	S += T0T4_mem1<=T0T4

	T0T5 = S.Task('T0T5', length=1, delay_cost=1)
	T0T5 += alt(ADD)

	T0T5_mem0 = S.Task('T0T5_mem0', length=1, delay_cost=1)
	T0T5_mem0 += MUL_mem[0]
	S += T0T0<T0T5_mem0
	S += T0T5_mem0<=T0T5

	T0T5_mem1 = S.Task('T0T5_mem1', length=1, delay_cost=1)
	T0T5_mem1 += MUL_mem[0]
	S += T0T1<T0T5_mem1
	S += T0T5_mem1<=T0T5

	T00 = S.Task('T00', length=1, delay_cost=1)
	T00 += alt(ADD)

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	T00_mem0 += MUL_mem[0]
	S += T0T0<T00_mem0
	S += T00_mem0<=T00

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	T00_mem1 += MUL_mem[0]
	S += T0T1<T00_mem1
	S += T00_mem1<=T00

	T3T4_in = S.Task('T3T4_in', length=1, delay_cost=1)
	T3T4_in += alt(MUL_in)
	T3T4 = S.Task('T3T4', length=7, delay_cost=1)
	T3T4 += alt(MUL)
	S+=T3T4>=T3T4_in

	T3T4_mem0 = S.Task('T3T4_mem0', length=1, delay_cost=1)
	T3T4_mem0 += ADD_mem[0]
	S += T3T2<T3T4_mem0
	S += T3T4_mem0<=T3T4

	T3T4_mem1 = S.Task('T3T4_mem1', length=1, delay_cost=1)
	T3T4_mem1 += ADD_mem[0]
	S += T3T3<T3T4_mem1
	S += T3T4_mem1<=T3T4

	T3T5 = S.Task('T3T5', length=1, delay_cost=1)
	T3T5 += alt(ADD)

	T3T5_mem0 = S.Task('T3T5_mem0', length=1, delay_cost=1)
	T3T5_mem0 += MUL_mem[0]
	S += T3T0<T3T5_mem0
	S += T3T5_mem0<=T3T5

	T3T5_mem1 = S.Task('T3T5_mem1', length=1, delay_cost=1)
	T3T5_mem1 += MUL_mem[0]
	S += T3T1<T3T5_mem1
	S += T3T5_mem1<=T3T5

	T30 = S.Task('T30', length=1, delay_cost=1)
	T30 += alt(ADD)

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += MUL_mem[0]
	S += T3T0<T30_mem0
	S += T30_mem0<=T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += MUL_mem[0]
	S += T3T1<T30_mem1
	S += T30_mem1<=T30

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	T4T4_in += alt(MUL_in)
	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	T4T4 += alt(MUL)
	S+=T4T4>=T4T4_in

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	T4T4_mem0 += ADD_mem[1]
	S += T4T2<T4T4_mem0
	S += T4T4_mem0<=T4T4

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	T4T4_mem1 += ADD_mem[2]
	S += T4T3<T4T4_mem1
	S += T4T4_mem1<=T4T4

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	T4T5 += alt(ADD)

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	T4T5_mem0 += MUL_mem[0]
	S += T4T0<T4T5_mem0
	S += T4T5_mem0<=T4T5

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	T4T5_mem1 += MUL_mem[0]
	S += T4T1<T4T5_mem1
	S += T4T5_mem1<=T4T5

	T40 = S.Task('T40', length=1, delay_cost=1)
	T40 += alt(ADD)

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += MUL_mem[0]
	S += T4T0<T40_mem0
	S += T40_mem0<=T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += MUL_mem[0]
	S += T4T1<T40_mem1
	S += T40_mem1<=T40

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	T5T4_in += alt(MUL_in)
	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	T5T4 += alt(MUL)
	S+=T5T4>=T5T4_in

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	T5T4_mem0 += ADD_mem[2]
	S += T5T2<T5T4_mem0
	S += T5T4_mem0<=T5T4

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	T5T4_mem1 += ADD_mem[1]
	S += T5T3<T5T4_mem1
	S += T5T4_mem1<=T5T4

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	T5T5 += alt(ADD)

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	T5T5_mem0 += MUL_mem[0]
	S += T5T0<T5T5_mem0
	S += T5T5_mem0<=T5T5

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	T5T5_mem1 += MUL_mem[0]
	S += T5T1<T5T5_mem1
	S += T5T5_mem1<=T5T5

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(ADD)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += MUL_mem[0]
	S += T5T0<T50_mem0
	S += T50_mem0<=T50

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	T50_mem1 += MUL_mem[0]
	S += T5T1<T50_mem1
	S += T50_mem1<=T50

	T6_T0_in = S.Task('T6_T0_in', length=1, delay_cost=1)
	T6_T0_in += alt(MUL_in)
	T6_T0 = S.Task('T6_T0', length=7, delay_cost=1)
	T6_T0 += alt(MUL)
	S+=T6_T0>=T6_T0_in

	T6_T0_mem0 = S.Task('T6_T0_mem0', length=1, delay_cost=1)
	T6_T0_mem0 += ADD_mem[0]
	S += T60<T6_T0_mem0
	S += T6_T0_mem0<=T6_T0

	T6_T0_mem1 = S.Task('T6_T0_mem1', length=1, delay_cost=1)
	T6_T0_mem1 += ADD_mem[3]
	S += T70<T6_T0_mem1
	S += T6_T0_mem1<=T6_T0

	T6_T1_in = S.Task('T6_T1_in', length=1, delay_cost=1)
	T6_T1_in += alt(MUL_in)
	T6_T1 = S.Task('T6_T1', length=7, delay_cost=1)
	T6_T1 += alt(MUL)
	S+=T6_T1>=T6_T1_in

	T6_T1_mem0 = S.Task('T6_T1_mem0', length=1, delay_cost=1)
	T6_T1_mem0 += ADD_mem[0]
	S += T61<T6_T1_mem0
	S += T6_T1_mem0<=T6_T1

	T6_T1_mem1 = S.Task('T6_T1_mem1', length=1, delay_cost=1)
	T6_T1_mem1 += ADD_mem[3]
	S += T71<T6_T1_mem1
	S += T6_T1_mem1<=T6_T1

	T6_T2 = S.Task('T6_T2', length=1, delay_cost=1)
	T6_T2 += alt(ADD)

	T6_T2_mem0 = S.Task('T6_T2_mem0', length=1, delay_cost=1)
	T6_T2_mem0 += ADD_mem[0]
	S += T60<T6_T2_mem0
	S += T6_T2_mem0<=T6_T2

	T6_T2_mem1 = S.Task('T6_T2_mem1', length=1, delay_cost=1)
	T6_T2_mem1 += ADD_mem[0]
	S += T61<T6_T2_mem1
	S += T6_T2_mem1<=T6_T2

	T6_T3 = S.Task('T6_T3', length=1, delay_cost=1)
	T6_T3 += alt(ADD)

	T6_T3_mem0 = S.Task('T6_T3_mem0', length=1, delay_cost=1)
	T6_T3_mem0 += ADD_mem[3]
	S += T70<T6_T3_mem0
	S += T6_T3_mem0<=T6_T3

	T6_T3_mem1 = S.Task('T6_T3_mem1', length=1, delay_cost=1)
	T6_T3_mem1 += ADD_mem[3]
	S += T71<T6_T3_mem1
	S += T6_T3_mem1<=T6_T3

	T6_1T4_in = S.Task('T6_1T4_in', length=1, delay_cost=1)
	T6_1T4_in += alt(MUL_in)
	T6_1T4 = S.Task('T6_1T4', length=7, delay_cost=1)
	T6_1T4 += alt(MUL)
	S+=T6_1T4>=T6_1T4_in

	T6_1T4_mem0 = S.Task('T6_1T4_mem0', length=1, delay_cost=1)
	T6_1T4_mem0 += ADD_mem[0]
	S += T6_1T2<T6_1T4_mem0
	S += T6_1T4_mem0<=T6_1T4

	T6_1T4_mem1 = S.Task('T6_1T4_mem1', length=1, delay_cost=1)
	T6_1T4_mem1 += ADD_mem[1]
	S += T6_1T3<T6_1T4_mem1
	S += T6_1T4_mem1<=T6_1T4

	T6_1T5 = S.Task('T6_1T5', length=1, delay_cost=1)
	T6_1T5 += alt(ADD)

	T6_1T5_mem0 = S.Task('T6_1T5_mem0', length=1, delay_cost=1)
	T6_1T5_mem0 += MUL_mem[0]
	S += T6_1T0<T6_1T5_mem0
	S += T6_1T5_mem0<=T6_1T5

	T6_1T5_mem1 = S.Task('T6_1T5_mem1', length=1, delay_cost=1)
	T6_1T5_mem1 += MUL_mem[0]
	S += T6_1T1<T6_1T5_mem1
	S += T6_1T5_mem1<=T6_1T5

	T6_10 = S.Task('T6_10', length=1, delay_cost=1)
	T6_10 += alt(ADD)

	T6_10_mem0 = S.Task('T6_10_mem0', length=1, delay_cost=1)
	T6_10_mem0 += MUL_mem[0]
	S += T6_1T0<T6_10_mem0
	S += T6_10_mem0<=T6_10

	T6_10_mem1 = S.Task('T6_10_mem1', length=1, delay_cost=1)
	T6_10_mem1 += MUL_mem[0]
	S += T6_1T1<T6_10_mem1
	S += T6_10_mem1<=T6_10

	T3_T0_in = S.Task('T3_T0_in', length=1, delay_cost=1)
	T3_T0_in += alt(MUL_in)
	T3_T0 = S.Task('T3_T0', length=7, delay_cost=1)
	T3_T0 += alt(MUL)
	S+=T3_T0>=T3_T0_in

	T3_T0_mem0 = S.Task('T3_T0_mem0', length=1, delay_cost=1)
	T3_T0_mem0 += INPUT_mem_r
	S += T3_T0_mem0<=T3_T0

	T3_T0_mem1 = S.Task('T3_T0_mem1', length=1, delay_cost=1)
	T3_T0_mem1 += ADD_mem[1]
	S += T140<T3_T0_mem1
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
	T3_T1_mem1 += ADD_mem[2]
	S += T141<T3_T1_mem1
	S += T3_T1_mem1<=T3_T1

	T3_T3 = S.Task('T3_T3', length=1, delay_cost=1)
	T3_T3 += alt(ADD)

	T3_T3_mem0 = S.Task('T3_T3_mem0', length=1, delay_cost=1)
	T3_T3_mem0 += ADD_mem[1]
	S += T140<T3_T3_mem0
	S += T3_T3_mem0<=T3_T3

	T3_T3_mem1 = S.Task('T3_T3_mem1', length=1, delay_cost=1)
	T3_T3_mem1 += ADD_mem[2]
	S += T141<T3_T3_mem1
	S += T3_T3_mem1<=T3_T3

	T4_T0_in = S.Task('T4_T0_in', length=1, delay_cost=1)
	T4_T0_in += alt(MUL_in)
	T4_T0 = S.Task('T4_T0', length=7, delay_cost=1)
	T4_T0 += alt(MUL)
	S+=T4_T0>=T4_T0_in

	T4_T0_mem0 = S.Task('T4_T0_mem0', length=1, delay_cost=1)
	T4_T0_mem0 += ADD_mem[0]
	S += T130<T4_T0_mem0
	S += T4_T0_mem0<=T4_T0

	T4_T0_mem1 = S.Task('T4_T0_mem1', length=1, delay_cost=1)
	T4_T0_mem1 += ADD_mem[0]
	S += T150<T4_T0_mem1
	S += T4_T0_mem1<=T4_T0

	T4_T1_in = S.Task('T4_T1_in', length=1, delay_cost=1)
	T4_T1_in += alt(MUL_in)
	T4_T1 = S.Task('T4_T1', length=7, delay_cost=1)
	T4_T1 += alt(MUL)
	S+=T4_T1>=T4_T1_in

	T4_T1_mem0 = S.Task('T4_T1_mem0', length=1, delay_cost=1)
	T4_T1_mem0 += ADD_mem[0]
	S += T131<T4_T1_mem0
	S += T4_T1_mem0<=T4_T1

	T4_T1_mem1 = S.Task('T4_T1_mem1', length=1, delay_cost=1)
	T4_T1_mem1 += ADD_mem[0]
	S += T151<T4_T1_mem1
	S += T4_T1_mem1<=T4_T1

	T4_T2 = S.Task('T4_T2', length=1, delay_cost=1)
	T4_T2 += alt(ADD)

	T4_T2_mem0 = S.Task('T4_T2_mem0', length=1, delay_cost=1)
	T4_T2_mem0 += ADD_mem[0]
	S += T130<T4_T2_mem0
	S += T4_T2_mem0<=T4_T2

	T4_T2_mem1 = S.Task('T4_T2_mem1', length=1, delay_cost=1)
	T4_T2_mem1 += ADD_mem[0]
	S += T131<T4_T2_mem1
	S += T4_T2_mem1<=T4_T2

	T4_T3 = S.Task('T4_T3', length=1, delay_cost=1)
	T4_T3 += alt(ADD)

	T4_T3_mem0 = S.Task('T4_T3_mem0', length=1, delay_cost=1)
	T4_T3_mem0 += ADD_mem[0]
	S += T150<T4_T3_mem0
	S += T4_T3_mem0<=T4_T3

	T4_T3_mem1 = S.Task('T4_T3_mem1', length=1, delay_cost=1)
	T4_T3_mem1 += ADD_mem[0]
	S += T151<T4_T3_mem1
	S += T4_T3_mem1<=T4_T3

	T8T0_in = S.Task('T8T0_in', length=1, delay_cost=1)
	T8T0_in += alt(MUL_in)
	T8T0 = S.Task('T8T0', length=7, delay_cost=1)
	T8T0 += alt(MUL)
	S+=T8T0>=T8T0_in

	T8T0_mem0 = S.Task('T8T0_mem0', length=1, delay_cost=1)
	T8T0_mem0 += ADD_mem[0]
	S += T130<T8T0_mem0
	S += T8T0_mem0<=T8T0

	T8T0_mem1 = S.Task('T8T0_mem1', length=1, delay_cost=1)
	T8T0_mem1 += ADD_mem[1]
	S += T160<T8T0_mem1
	S += T8T0_mem1<=T8T0

	T8T1_in = S.Task('T8T1_in', length=1, delay_cost=1)
	T8T1_in += alt(MUL_in)
	T8T1 = S.Task('T8T1', length=7, delay_cost=1)
	T8T1 += alt(MUL)
	S+=T8T1>=T8T1_in

	T8T1_mem0 = S.Task('T8T1_mem0', length=1, delay_cost=1)
	T8T1_mem0 += ADD_mem[0]
	S += T131<T8T1_mem0
	S += T8T1_mem0<=T8T1

	T8T1_mem1 = S.Task('T8T1_mem1', length=1, delay_cost=1)
	T8T1_mem1 += ADD_mem[1]
	S += T161<T8T1_mem1
	S += T8T1_mem1<=T8T1

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	T8T2 += alt(ADD)

	T8T2_mem0 = S.Task('T8T2_mem0', length=1, delay_cost=1)
	T8T2_mem0 += ADD_mem[0]
	S += T130<T8T2_mem0
	S += T8T2_mem0<=T8T2

	T8T2_mem1 = S.Task('T8T2_mem1', length=1, delay_cost=1)
	T8T2_mem1 += ADD_mem[0]
	S += T131<T8T2_mem1
	S += T8T2_mem1<=T8T2

	T8T3 = S.Task('T8T3', length=1, delay_cost=1)
	T8T3 += alt(ADD)

	T8T3_mem0 = S.Task('T8T3_mem0', length=1, delay_cost=1)
	T8T3_mem0 += ADD_mem[1]
	S += T160<T8T3_mem0
	S += T8T3_mem0<=T8T3

	T8T3_mem1 = S.Task('T8T3_mem1', length=1, delay_cost=1)
	T8T3_mem1 += ADD_mem[1]
	S += T161<T8T3_mem1
	S += T8T3_mem1<=T8T3

	T90 = S.Task('T90', length=1, delay_cost=1)
	T90 += alt(ADD)

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	T90_mem0 += INPUT_mem_r
	S += T90_mem0<=T90

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	T90_mem1 += ADD_mem[0]
	S += T130<T90_mem1
	S += T90_mem1<=T90

	T91 = S.Task('T91', length=1, delay_cost=1)
	T91 += alt(ADD)

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	T91_mem0 += INPUT_mem_r
	S += T91_mem0<=T91

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	T91_mem1 += ADD_mem[0]
	S += T131<T91_mem1
	S += T91_mem1<=T91

	T100 = S.Task('T100', length=1, delay_cost=1)
	T100 += alt(ADD)

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	T100_mem0 += ADD_mem[1]
	S += T140<T100_mem0
	S += T100_mem0<=T100

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	T100_mem1 += ADD_mem[0]
	S += T150<T100_mem1
	S += T100_mem1<=T100

	T101 = S.Task('T101', length=1, delay_cost=1)
	T101 += alt(ADD)

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	T101_mem0 += ADD_mem[2]
	S += T141<T101_mem0
	S += T101_mem0<=T101

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	T101_mem1 += ADD_mem[0]
	S += T151<T101_mem1
	S += T101_mem1<=T101

	T9_1T0_in = S.Task('T9_1T0_in', length=1, delay_cost=1)
	T9_1T0_in += alt(MUL_in)
	T9_1T0 = S.Task('T9_1T0', length=7, delay_cost=1)
	T9_1T0 += alt(MUL)
	S+=T9_1T0>=T9_1T0_in

	T9_1T0_mem0 = S.Task('T9_1T0_mem0', length=1, delay_cost=1)
	T9_1T0_mem0 += INPUT_mem_r
	S += T9_1T0_mem0<=T9_1T0

	T9_1T0_mem1 = S.Task('T9_1T0_mem1', length=1, delay_cost=1)
	T9_1T0_mem1 += ADD_mem[1]
	S += T160<T9_1T0_mem1
	S += T9_1T0_mem1<=T9_1T0

	T9_1T1_in = S.Task('T9_1T1_in', length=1, delay_cost=1)
	T9_1T1_in += alt(MUL_in)
	T9_1T1 = S.Task('T9_1T1', length=7, delay_cost=1)
	T9_1T1 += alt(MUL)
	S+=T9_1T1>=T9_1T1_in

	T9_1T1_mem0 = S.Task('T9_1T1_mem0', length=1, delay_cost=1)
	T9_1T1_mem0 += INPUT_mem_r
	S += T9_1T1_mem0<=T9_1T1

	T9_1T1_mem1 = S.Task('T9_1T1_mem1', length=1, delay_cost=1)
	T9_1T1_mem1 += ADD_mem[1]
	S += T161<T9_1T1_mem1
	S += T9_1T1_mem1<=T9_1T1

	T9_1T3 = S.Task('T9_1T3', length=1, delay_cost=1)
	T9_1T3 += alt(ADD)

	T9_1T3_mem0 = S.Task('T9_1T3_mem0', length=1, delay_cost=1)
	T9_1T3_mem0 += ADD_mem[1]
	S += T160<T9_1T3_mem0
	S += T9_1T3_mem0<=T9_1T3

	T9_1T3_mem1 = S.Task('T9_1T3_mem1', length=1, delay_cost=1)
	T9_1T3_mem1 += ADD_mem[1]
	S += T161<T9_1T3_mem1
	S += T9_1T3_mem1<=T9_1T3

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sparse_mul1_add4/sparse_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sparse_mul1_add4_1(0, 0)