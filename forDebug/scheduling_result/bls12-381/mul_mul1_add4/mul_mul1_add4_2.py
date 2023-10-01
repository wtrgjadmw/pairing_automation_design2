from pyschedule import Scenario, solvers, plotters, alt

def solve_mul_mul1_add4_2(ConstStep, ExpStep):
	horizon = 151
	S=Scenario("mul_mul1_add4_2",horizon = horizon)

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
	T2_1T1_in = S.Task('T2_1T1_in', length=1, delay_cost=1)
	S += T2_1T1_in >= 0
	T2_1T1_in += MUL_in[0]

	T2_1T1_mem0 = S.Task('T2_1T1_mem0', length=1, delay_cost=1)
	S += T2_1T1_mem0 >= 0
	T2_1T1_mem0 += INPUT_mem_r

	T2_1T1_mem1 = S.Task('T2_1T1_mem1', length=1, delay_cost=1)
	S += T2_1T1_mem1 >= 0
	T2_1T1_mem1 += INPUT_mem_r

	T2T1_in = S.Task('T2T1_in', length=1, delay_cost=1)
	S += T2T1_in >= 1
	T2T1_in += MUL_in[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 1
	T2T1_mem0 += INPUT_mem_r

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 1
	T2T1_mem1 += INPUT_mem_r

	T2_1T1 = S.Task('T2_1T1', length=7, delay_cost=1)
	S += T2_1T1 >= 1
	T2_1T1 += MUL[0]

	T2T1 = S.Task('T2T1', length=7, delay_cost=1)
	S += T2T1 >= 2
	T2T1 += MUL[0]

	T2_1T0_in = S.Task('T2_1T0_in', length=1, delay_cost=1)
	S += T2_1T0_in >= 2
	T2_1T0_in += MUL_in[0]

	T2_1T0_mem0 = S.Task('T2_1T0_mem0', length=1, delay_cost=1)
	S += T2_1T0_mem0 >= 2
	T2_1T0_mem0 += INPUT_mem_r

	T2_1T0_mem1 = S.Task('T2_1T0_mem1', length=1, delay_cost=1)
	S += T2_1T0_mem1 >= 2
	T2_1T0_mem1 += INPUT_mem_r

	T1_T1_in = S.Task('T1_T1_in', length=1, delay_cost=1)
	S += T1_T1_in >= 3
	T1_T1_in += MUL_in[0]

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	S += T1_T1_mem0 >= 3
	T1_T1_mem0 += INPUT_mem_r

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	S += T1_T1_mem1 >= 3
	T1_T1_mem1 += INPUT_mem_r

	T2_1T0 = S.Task('T2_1T0', length=7, delay_cost=1)
	S += T2_1T0 >= 3
	T2_1T0 += MUL[0]

	T1T1_in = S.Task('T1T1_in', length=1, delay_cost=1)
	S += T1T1_in >= 4
	T1T1_in += MUL_in[0]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 4
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 4
	T1T1_mem1 += INPUT_mem_r

	T1_T1 = S.Task('T1_T1', length=7, delay_cost=1)
	S += T1_T1 >= 4
	T1_T1 += MUL[0]

	T1T0_in = S.Task('T1T0_in', length=1, delay_cost=1)
	S += T1T0_in >= 5
	T1T0_in += MUL_in[0]

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 5
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 5
	T1T0_mem1 += INPUT_mem_r

	T1T1 = S.Task('T1T1', length=7, delay_cost=1)
	S += T1T1 >= 5
	T1T1 += MUL[0]

	T0_T1_in = S.Task('T0_T1_in', length=1, delay_cost=1)
	S += T0_T1_in >= 6
	T0_T1_in += MUL_in[0]

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	S += T0_T1_mem0 >= 6
	T0_T1_mem0 += INPUT_mem_r

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	S += T0_T1_mem1 >= 6
	T0_T1_mem1 += INPUT_mem_r

	T1T0 = S.Task('T1T0', length=7, delay_cost=1)
	S += T1T0 >= 6
	T1T0 += MUL[0]

	T0_T0_in = S.Task('T0_T0_in', length=1, delay_cost=1)
	S += T0_T0_in >= 7
	T0_T0_in += MUL_in[0]

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	S += T0_T0_mem0 >= 7
	T0_T0_mem0 += INPUT_mem_r

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	S += T0_T0_mem1 >= 7
	T0_T0_mem1 += INPUT_mem_r

	T0_T1 = S.Task('T0_T1', length=7, delay_cost=1)
	S += T0_T1 >= 7
	T0_T1 += MUL[0]

	T0T1_in = S.Task('T0T1_in', length=1, delay_cost=1)
	S += T0T1_in >= 8
	T0T1_in += MUL_in[0]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 8
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 8
	T0T1_mem1 += INPUT_mem_r

	T0_T0 = S.Task('T0_T0', length=7, delay_cost=1)
	S += T0_T0 >= 8
	T0_T0 += MUL[0]

	T0T1 = S.Task('T0T1', length=7, delay_cost=1)
	S += T0T1 >= 9
	T0T1 += MUL[0]

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	S += T2T0_in >= 9
	T2T0_in += MUL_in[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 9
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 9
	T2T0_mem1 += INPUT_mem_r

	T1_T0_in = S.Task('T1_T0_in', length=1, delay_cost=1)
	S += T1_T0_in >= 10
	T1_T0_in += MUL_in[0]

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	S += T1_T0_mem0 >= 10
	T1_T0_mem0 += INPUT_mem_r

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	S += T1_T0_mem1 >= 10
	T1_T0_mem1 += INPUT_mem_r

	T2T0 = S.Task('T2T0', length=7, delay_cost=1)
	S += T2T0 >= 10
	T2T0 += MUL[0]

	T0T0_in = S.Task('T0T0_in', length=1, delay_cost=1)
	S += T0T0_in >= 11
	T0T0_in += MUL_in[0]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 11
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 11
	T0T0_mem1 += INPUT_mem_r

	T1_T0 = S.Task('T1_T0', length=7, delay_cost=1)
	S += T1_T0 >= 11
	T1_T0 += MUL[0]

	T0T0 = S.Task('T0T0', length=7, delay_cost=1)
	S += T0T0 >= 12
	T0T0 += MUL[0]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 12
	T2T2_mem0 += INPUT_mem_r

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 12
	T2T2_mem1 += INPUT_mem_r

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	S += T2T2 >= 13
	T2T2 += ADD[0]

	T2T3_mem0 = S.Task('T2T3_mem0', length=1, delay_cost=1)
	S += T2T3_mem0 >= 13
	T2T3_mem0 += INPUT_mem_r

	T2T3_mem1 = S.Task('T2T3_mem1', length=1, delay_cost=1)
	S += T2T3_mem1 >= 13
	T2T3_mem1 += INPUT_mem_r

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 14
	T131_mem0 += INPUT_mem_r

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 14
	T131_mem1 += INPUT_mem_r

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	S += T2T3 >= 14
	T2T3 += ADD[1]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 15
	T130_mem0 += INPUT_mem_r

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 15
	T130_mem1 += INPUT_mem_r

	T131 = S.Task('T131', length=1, delay_cost=1)
	S += T131 >= 15
	T131 += ADD[0]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 16
	T130 += ADD[1]

	T6_1_mem0 = S.Task('T6_1_mem0', length=1, delay_cost=1)
	S += T6_1_mem0 >= 16
	T6_1_mem0 += INPUT_mem_r

	T6_1_mem1 = S.Task('T6_1_mem1', length=1, delay_cost=1)
	S += T6_1_mem1 >= 16
	T6_1_mem1 += INPUT_mem_r

	T1T3_mem0 = S.Task('T1T3_mem0', length=1, delay_cost=1)
	S += T1T3_mem0 >= 17
	T1T3_mem0 += INPUT_mem_r

	T1T3_mem1 = S.Task('T1T3_mem1', length=1, delay_cost=1)
	S += T1T3_mem1 >= 17
	T1T3_mem1 += INPUT_mem_r

	T6_1 = S.Task('T6_1', length=1, delay_cost=1)
	S += T6_1 >= 17
	T6_1 += ADD[3]

	T1T3 = S.Task('T1T3', length=1, delay_cost=1)
	S += T1T3 >= 18
	T1T3 += ADD[2]

	T5_51_mem0 = S.Task('T5_51_mem0', length=1, delay_cost=1)
	S += T5_51_mem0 >= 18
	T5_51_mem0 += INPUT_mem_r

	T5_51_mem1 = S.Task('T5_51_mem1', length=1, delay_cost=1)
	S += T5_51_mem1 >= 18
	T5_51_mem1 += INPUT_mem_r

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 19
	T30_mem0 += INPUT_mem_r

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 19
	T30_mem1 += INPUT_mem_r

	T5_51 = S.Task('T5_51', length=1, delay_cost=1)
	S += T5_51 >= 19
	T5_51 += ADD[0]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 20
	T30 += ADD[3]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 20
	T40_mem0 += INPUT_mem_r

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 20
	T40_mem1 += INPUT_mem_r

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 21
	T40 += ADD[0]

	T5_50_mem0 = S.Task('T5_50_mem0', length=1, delay_cost=1)
	S += T5_50_mem0 >= 21
	T5_50_mem0 += INPUT_mem_r

	T5_50_mem1 = S.Task('T5_50_mem1', length=1, delay_cost=1)
	S += T5_50_mem1 >= 21
	T5_50_mem1 += INPUT_mem_r

	T5_50 = S.Task('T5_50', length=1, delay_cost=1)
	S += T5_50 >= 22
	T5_50 += ADD[0]

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	S += T6_0_mem0 >= 22
	T6_0_mem0 += INPUT_mem_r

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	S += T6_0_mem1 >= 22
	T6_0_mem1 += INPUT_mem_r

	T5_41_mem0 = S.Task('T5_41_mem0', length=1, delay_cost=1)
	S += T5_41_mem0 >= 23
	T5_41_mem0 += INPUT_mem_r

	T5_41_mem1 = S.Task('T5_41_mem1', length=1, delay_cost=1)
	S += T5_41_mem1 >= 23
	T5_41_mem1 += INPUT_mem_r

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	S += T6_0 >= 23
	T6_0 += ADD[1]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 24
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 24
	T0T2_mem1 += INPUT_mem_r

	T5_41 = S.Task('T5_41', length=1, delay_cost=1)
	S += T5_41 >= 24
	T5_41 += ADD[0]

	T0T2 = S.Task('T0T2', length=1, delay_cost=1)
	S += T0T2 >= 25
	T0T2 += ADD[1]

	T5_40_mem0 = S.Task('T5_40_mem0', length=1, delay_cost=1)
	S += T5_40_mem0 >= 25
	T5_40_mem0 += INPUT_mem_r

	T5_40_mem1 = S.Task('T5_40_mem1', length=1, delay_cost=1)
	S += T5_40_mem1 >= 25
	T5_40_mem1 += INPUT_mem_r

	T4_61_mem0 = S.Task('T4_61_mem0', length=1, delay_cost=1)
	S += T4_61_mem0 >= 26
	T4_61_mem0 += INPUT_mem_r

	T4_61_mem1 = S.Task('T4_61_mem1', length=1, delay_cost=1)
	S += T4_61_mem1 >= 26
	T4_61_mem1 += INPUT_mem_r

	T5_40 = S.Task('T5_40', length=1, delay_cost=1)
	S += T5_40 >= 26
	T5_40 += ADD[3]

	T4_51_mem0 = S.Task('T4_51_mem0', length=1, delay_cost=1)
	S += T4_51_mem0 >= 27
	T4_51_mem0 += INPUT_mem_r

	T4_51_mem1 = S.Task('T4_51_mem1', length=1, delay_cost=1)
	S += T4_51_mem1 >= 27
	T4_51_mem1 += INPUT_mem_r

	T4_61 = S.Task('T4_61', length=1, delay_cost=1)
	S += T4_61 >= 27
	T4_61 += ADD[0]

	T2_1T3_mem0 = S.Task('T2_1T3_mem0', length=1, delay_cost=1)
	S += T2_1T3_mem0 >= 28
	T2_1T3_mem0 += INPUT_mem_r

	T2_1T3_mem1 = S.Task('T2_1T3_mem1', length=1, delay_cost=1)
	S += T2_1T3_mem1 >= 28
	T2_1T3_mem1 += INPUT_mem_r

	T4_51 = S.Task('T4_51', length=1, delay_cost=1)
	S += T4_51 >= 28
	T4_51 += ADD[2]

	T2_1T3 = S.Task('T2_1T3', length=1, delay_cost=1)
	S += T2_1T3 >= 29
	T2_1T3 += ADD[0]

	T4_60_mem0 = S.Task('T4_60_mem0', length=1, delay_cost=1)
	S += T4_60_mem0 >= 29
	T4_60_mem0 += INPUT_mem_r

	T4_60_mem1 = S.Task('T4_60_mem1', length=1, delay_cost=1)
	S += T4_60_mem1 >= 29
	T4_60_mem1 += INPUT_mem_r

	T4_50_mem0 = S.Task('T4_50_mem0', length=1, delay_cost=1)
	S += T4_50_mem0 >= 30
	T4_50_mem0 += INPUT_mem_r

	T4_50_mem1 = S.Task('T4_50_mem1', length=1, delay_cost=1)
	S += T4_50_mem1 >= 30
	T4_50_mem1 += INPUT_mem_r

	T4_60 = S.Task('T4_60', length=1, delay_cost=1)
	S += T4_60 >= 30
	T4_60 += ADD[0]

	T3_31_mem0 = S.Task('T3_31_mem0', length=1, delay_cost=1)
	S += T3_31_mem0 >= 31
	T3_31_mem0 += INPUT_mem_r

	T3_31_mem1 = S.Task('T3_31_mem1', length=1, delay_cost=1)
	S += T3_31_mem1 >= 31
	T3_31_mem1 += INPUT_mem_r

	T4_50 = S.Task('T4_50', length=1, delay_cost=1)
	S += T4_50 >= 31
	T4_50 += ADD[2]

	T2_1T2_mem0 = S.Task('T2_1T2_mem0', length=1, delay_cost=1)
	S += T2_1T2_mem0 >= 32
	T2_1T2_mem0 += INPUT_mem_r

	T2_1T2_mem1 = S.Task('T2_1T2_mem1', length=1, delay_cost=1)
	S += T2_1T2_mem1 >= 32
	T2_1T2_mem1 += INPUT_mem_r

	T3_31 = S.Task('T3_31', length=1, delay_cost=1)
	S += T3_31 >= 32
	T3_31 += ADD[2]

	T1_T3_mem0 = S.Task('T1_T3_mem0', length=1, delay_cost=1)
	S += T1_T3_mem0 >= 33
	T1_T3_mem0 += INPUT_mem_r

	T1_T3_mem1 = S.Task('T1_T3_mem1', length=1, delay_cost=1)
	S += T1_T3_mem1 >= 33
	T1_T3_mem1 += INPUT_mem_r

	T2_1T2 = S.Task('T2_1T2', length=1, delay_cost=1)
	S += T2_1T2 >= 33
	T2_1T2 += ADD[0]

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	S += T1T2_mem0 >= 34
	T1T2_mem0 += INPUT_mem_r

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	S += T1T2_mem1 >= 34
	T1T2_mem1 += INPUT_mem_r

	T1_T3 = S.Task('T1_T3', length=1, delay_cost=1)
	S += T1_T3 >= 34
	T1_T3 += ADD[1]

	T1T2 = S.Task('T1T2', length=1, delay_cost=1)
	S += T1T2 >= 35
	T1T2 += ADD[2]

	T3_30_mem0 = S.Task('T3_30_mem0', length=1, delay_cost=1)
	S += T3_30_mem0 >= 35
	T3_30_mem0 += INPUT_mem_r

	T3_30_mem1 = S.Task('T3_30_mem1', length=1, delay_cost=1)
	S += T3_30_mem1 >= 35
	T3_30_mem1 += INPUT_mem_r

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	S += T1_T2_mem0 >= 36
	T1_T2_mem0 += INPUT_mem_r

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	S += T1_T2_mem1 >= 36
	T1_T2_mem1 += INPUT_mem_r

	T3_30 = S.Task('T3_30', length=1, delay_cost=1)
	S += T3_30 >= 36
	T3_30 += ADD[0]

	T0_T3_mem0 = S.Task('T0_T3_mem0', length=1, delay_cost=1)
	S += T0_T3_mem0 >= 37
	T0_T3_mem0 += INPUT_mem_r

	T0_T3_mem1 = S.Task('T0_T3_mem1', length=1, delay_cost=1)
	S += T0_T3_mem1 >= 37
	T0_T3_mem1 += INPUT_mem_r

	T1_T2 = S.Task('T1_T2', length=1, delay_cost=1)
	S += T1_T2 >= 37
	T1_T2 += ADD[1]

	T0_T3 = S.Task('T0_T3', length=1, delay_cost=1)
	S += T0_T3 >= 38
	T0_T3 += ADD[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 38
	T31_mem0 += INPUT_mem_r

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 38
	T31_mem1 += INPUT_mem_r

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	S += T0_T2_mem0 >= 39
	T0_T2_mem0 += INPUT_mem_r

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	S += T0_T2_mem1 >= 39
	T0_T2_mem1 += INPUT_mem_r

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 39
	T31 += ADD[3]

	T0_T2 = S.Task('T0_T2', length=1, delay_cost=1)
	S += T0_T2 >= 40
	T0_T2 += ADD[1]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 40
	T61_mem0 += INPUT_mem_r

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 40
	T61_mem1 += INPUT_mem_r

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 41
	T60_mem0 += INPUT_mem_r

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 41
	T60_mem1 += INPUT_mem_r

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 41
	T61 += ADD[0]

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	S += T5_1_mem0 >= 42
	T5_1_mem0 += INPUT_mem_r

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	S += T5_1_mem1 >= 42
	T5_1_mem1 += INPUT_mem_r

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 42
	T60 += ADD[0]

	T0T3_mem0 = S.Task('T0T3_mem0', length=1, delay_cost=1)
	S += T0T3_mem0 >= 43
	T0T3_mem0 += INPUT_mem_r

	T0T3_mem1 = S.Task('T0T3_mem1', length=1, delay_cost=1)
	S += T0T3_mem1 >= 43
	T0T3_mem1 += INPUT_mem_r

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	S += T5_1 >= 43
	T5_1 += ADD[3]

	T0T3 = S.Task('T0T3', length=1, delay_cost=1)
	S += T0T3 >= 44
	T0T3 += ADD[0]

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	S += T5_0_mem0 >= 44
	T5_0_mem0 += INPUT_mem_r

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	S += T5_0_mem1 >= 44
	T5_0_mem1 += INPUT_mem_r

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 45
	T51_mem0 += INPUT_mem_r

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 45
	T51_mem1 += INPUT_mem_r

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	S += T5_0 >= 45
	T5_0 += ADD[0]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 46
	T50_mem0 += INPUT_mem_r

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 46
	T50_mem1 += INPUT_mem_r

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 46
	T51 += ADD[0]

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	S += T4_1_mem0 >= 47
	T4_1_mem0 += INPUT_mem_r

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	S += T4_1_mem1 >= 47
	T4_1_mem1 += INPUT_mem_r

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 47
	T50 += ADD[2]

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	S += T4_0_mem0 >= 48
	T4_0_mem0 += INPUT_mem_r

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	S += T4_0_mem1 >= 48
	T4_0_mem1 += INPUT_mem_r

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	S += T4_1 >= 48
	T4_1 += ADD[1]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 49
	T41_mem0 += INPUT_mem_r

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 49
	T41_mem1 += INPUT_mem_r

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	S += T4_0 >= 49
	T4_0 += ADD[3]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 50
	T180_mem0 += INPUT_mem_r

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 50
	T180_mem1 += INPUT_mem_r

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 50
	T41 += ADD[1]

	T180 = S.Task('T180', length=1, delay_cost=1)
	S += T180 >= 51
	T180 += ADD[2]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 51
	T181_mem0 += INPUT_mem_r

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 51
	T181_mem1 += INPUT_mem_r

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 52
	T140_mem0 += INPUT_mem_r

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 52
	T140_mem1 += INPUT_mem_r

	T181 = S.Task('T181', length=1, delay_cost=1)
	S += T181 >= 52
	T181 += ADD[0]

	T140 = S.Task('T140', length=1, delay_cost=1)
	S += T140 >= 53
	T140 += ADD[1]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 53
	T151_mem0 += INPUT_mem_r

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 53
	T151_mem1 += INPUT_mem_r

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 54
	T141_mem0 += INPUT_mem_r

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 54
	T141_mem1 += INPUT_mem_r

	T151 = S.Task('T151', length=1, delay_cost=1)
	S += T151 >= 54
	T151 += ADD[1]

	T141 = S.Task('T141', length=1, delay_cost=1)
	S += T141 >= 55
	T141 += ADD[1]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 55
	T150_mem0 += INPUT_mem_r

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 55
	T150_mem1 += INPUT_mem_r

	T150 = S.Task('T150', length=1, delay_cost=1)
	S += T150 >= 56
	T150 += ADD[1]

	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	S += T170_mem0 >= 56
	T170_mem0 += INPUT_mem_r

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	S += T170_mem1 >= 56
	T170_mem1 += INPUT_mem_r

	T170 = S.Task('T170', length=1, delay_cost=1)
	S += T170 >= 57
	T170 += ADD[1]

	T171_mem0 = S.Task('T171_mem0', length=1, delay_cost=1)
	S += T171_mem0 >= 57
	T171_mem0 += INPUT_mem_r

	T171_mem1 = S.Task('T171_mem1', length=1, delay_cost=1)
	S += T171_mem1 >= 57
	T171_mem1 += INPUT_mem_r

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	S += T160_mem0 >= 58
	T160_mem0 += INPUT_mem_r

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	S += T160_mem1 >= 58
	T160_mem1 += INPUT_mem_r

	T171 = S.Task('T171', length=1, delay_cost=1)
	S += T171 >= 58
	T171 += ADD[3]

	T160 = S.Task('T160', length=1, delay_cost=1)
	S += T160 >= 59
	T160 += ADD[2]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	S += T161_mem0 >= 59
	T161_mem0 += INPUT_mem_r

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	S += T161_mem1 >= 59
	T161_mem1 += INPUT_mem_r

	T161 = S.Task('T161', length=1, delay_cost=1)
	S += T161 >= 60
	T161 += ADD[3]


	# new tasks
	T0T4_in = S.Task('T0T4_in', length=1, delay_cost=1)
	T0T4_in += alt(MUL_in)
	T0T4 = S.Task('T0T4', length=7, delay_cost=1)
	T0T4 += alt(MUL)
	S+=T0T4>=T0T4_in

	T0T4_mem0 = S.Task('T0T4_mem0', length=1, delay_cost=1)
	T0T4_mem0 += ADD_mem[1]
	S += 25<T0T4_mem0
	S += T0T4_mem0<=T0T4

	T0T4_mem1 = S.Task('T0T4_mem1', length=1, delay_cost=1)
	T0T4_mem1 += ADD_mem[0]
	S += 44<T0T4_mem1
	S += T0T4_mem1<=T0T4

	T0T5 = S.Task('T0T5', length=1, delay_cost=1)
	T0T5 += alt(ADD)

	T0T5_mem0 = S.Task('T0T5_mem0', length=1, delay_cost=1)
	T0T5_mem0 += MUL_mem[0]
	S += 18<T0T5_mem0
	S += T0T5_mem0<=T0T5

	T0T5_mem1 = S.Task('T0T5_mem1', length=1, delay_cost=1)
	T0T5_mem1 += MUL_mem[0]
	S += 15<T0T5_mem1
	S += T0T5_mem1<=T0T5

	T00 = S.Task('T00', length=1, delay_cost=1)
	T00 += alt(ADD)

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	T00_mem0 += MUL_mem[0]
	S += 18<T00_mem0
	S += T00_mem0<=T00

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	T00_mem1 += MUL_mem[0]
	S += 15<T00_mem1
	S += T00_mem1<=T00

	T1T4_in = S.Task('T1T4_in', length=1, delay_cost=1)
	T1T4_in += alt(MUL_in)
	T1T4 = S.Task('T1T4', length=7, delay_cost=1)
	T1T4 += alt(MUL)
	S+=T1T4>=T1T4_in

	T1T4_mem0 = S.Task('T1T4_mem0', length=1, delay_cost=1)
	T1T4_mem0 += ADD_mem[2]
	S += 35<T1T4_mem0
	S += T1T4_mem0<=T1T4

	T1T4_mem1 = S.Task('T1T4_mem1', length=1, delay_cost=1)
	T1T4_mem1 += ADD_mem[2]
	S += 18<T1T4_mem1
	S += T1T4_mem1<=T1T4

	T1T5 = S.Task('T1T5', length=1, delay_cost=1)
	T1T5 += alt(ADD)

	T1T5_mem0 = S.Task('T1T5_mem0', length=1, delay_cost=1)
	T1T5_mem0 += MUL_mem[0]
	S += 12<T1T5_mem0
	S += T1T5_mem0<=T1T5

	T1T5_mem1 = S.Task('T1T5_mem1', length=1, delay_cost=1)
	T1T5_mem1 += MUL_mem[0]
	S += 11<T1T5_mem1
	S += T1T5_mem1<=T1T5

	T10 = S.Task('T10', length=1, delay_cost=1)
	T10 += alt(ADD)

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += MUL_mem[0]
	S += 12<T10_mem0
	S += T10_mem0<=T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += MUL_mem[0]
	S += 11<T10_mem1
	S += T10_mem1<=T10

	T2T4_in = S.Task('T2T4_in', length=1, delay_cost=1)
	T2T4_in += alt(MUL_in)
	T2T4 = S.Task('T2T4', length=7, delay_cost=1)
	T2T4 += alt(MUL)
	S+=T2T4>=T2T4_in

	T2T4_mem0 = S.Task('T2T4_mem0', length=1, delay_cost=1)
	T2T4_mem0 += ADD_mem[0]
	S += 13<T2T4_mem0
	S += T2T4_mem0<=T2T4

	T2T4_mem1 = S.Task('T2T4_mem1', length=1, delay_cost=1)
	T2T4_mem1 += ADD_mem[1]
	S += 14<T2T4_mem1
	S += T2T4_mem1<=T2T4

	T2T5 = S.Task('T2T5', length=1, delay_cost=1)
	T2T5 += alt(ADD)

	T2T5_mem0 = S.Task('T2T5_mem0', length=1, delay_cost=1)
	T2T5_mem0 += MUL_mem[0]
	S += 16<T2T5_mem0
	S += T2T5_mem0<=T2T5

	T2T5_mem1 = S.Task('T2T5_mem1', length=1, delay_cost=1)
	T2T5_mem1 += MUL_mem[0]
	S += 8<T2T5_mem1
	S += T2T5_mem1<=T2T5

	T20 = S.Task('T20', length=1, delay_cost=1)
	T20 += alt(ADD)

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += MUL_mem[0]
	S += 16<T20_mem0
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += MUL_mem[0]
	S += 8<T20_mem1
	S += T20_mem1<=T20

	T3_T0_in = S.Task('T3_T0_in', length=1, delay_cost=1)
	T3_T0_in += alt(MUL_in)
	T3_T0 = S.Task('T3_T0', length=7, delay_cost=1)
	T3_T0 += alt(MUL)
	S+=T3_T0>=T3_T0_in

	T3_T0_mem0 = S.Task('T3_T0_mem0', length=1, delay_cost=1)
	T3_T0_mem0 += ADD_mem[3]
	S += 20<T3_T0_mem0
	S += T3_T0_mem0<=T3_T0

	T3_T0_mem1 = S.Task('T3_T0_mem1', length=1, delay_cost=1)
	T3_T0_mem1 += ADD_mem[0]
	S += 21<T3_T0_mem1
	S += T3_T0_mem1<=T3_T0

	T3_T1_in = S.Task('T3_T1_in', length=1, delay_cost=1)
	T3_T1_in += alt(MUL_in)
	T3_T1 = S.Task('T3_T1', length=7, delay_cost=1)
	T3_T1 += alt(MUL)
	S+=T3_T1>=T3_T1_in

	T3_T1_mem0 = S.Task('T3_T1_mem0', length=1, delay_cost=1)
	T3_T1_mem0 += ADD_mem[3]
	S += 39<T3_T1_mem0
	S += T3_T1_mem0<=T3_T1

	T3_T1_mem1 = S.Task('T3_T1_mem1', length=1, delay_cost=1)
	T3_T1_mem1 += ADD_mem[1]
	S += 50<T3_T1_mem1
	S += T3_T1_mem1<=T3_T1

	T3_T2 = S.Task('T3_T2', length=1, delay_cost=1)
	T3_T2 += alt(ADD)

	T3_T2_mem0 = S.Task('T3_T2_mem0', length=1, delay_cost=1)
	T3_T2_mem0 += ADD_mem[3]
	S += 20<T3_T2_mem0
	S += T3_T2_mem0<=T3_T2

	T3_T2_mem1 = S.Task('T3_T2_mem1', length=1, delay_cost=1)
	T3_T2_mem1 += ADD_mem[3]
	S += 39<T3_T2_mem1
	S += T3_T2_mem1<=T3_T2

	T3_T3 = S.Task('T3_T3', length=1, delay_cost=1)
	T3_T3 += alt(ADD)

	T3_T3_mem0 = S.Task('T3_T3_mem0', length=1, delay_cost=1)
	T3_T3_mem0 += ADD_mem[0]
	S += 21<T3_T3_mem0
	S += T3_T3_mem0<=T3_T3

	T3_T3_mem1 = S.Task('T3_T3_mem1', length=1, delay_cost=1)
	T3_T3_mem1 += ADD_mem[1]
	S += 50<T3_T3_mem1
	S += T3_T3_mem1<=T3_T3

	T4_1T0_in = S.Task('T4_1T0_in', length=1, delay_cost=1)
	T4_1T0_in += alt(MUL_in)
	T4_1T0 = S.Task('T4_1T0', length=7, delay_cost=1)
	T4_1T0 += alt(MUL)
	S+=T4_1T0>=T4_1T0_in

	T4_1T0_mem0 = S.Task('T4_1T0_mem0', length=1, delay_cost=1)
	T4_1T0_mem0 += ADD_mem[3]
	S += 49<T4_1T0_mem0
	S += T4_1T0_mem0<=T4_1T0

	T4_1T0_mem1 = S.Task('T4_1T0_mem1', length=1, delay_cost=1)
	T4_1T0_mem1 += ADD_mem[2]
	S += 47<T4_1T0_mem1
	S += T4_1T0_mem1<=T4_1T0

	T4_1T1_in = S.Task('T4_1T1_in', length=1, delay_cost=1)
	T4_1T1_in += alt(MUL_in)
	T4_1T1 = S.Task('T4_1T1', length=7, delay_cost=1)
	T4_1T1 += alt(MUL)
	S+=T4_1T1>=T4_1T1_in

	T4_1T1_mem0 = S.Task('T4_1T1_mem0', length=1, delay_cost=1)
	T4_1T1_mem0 += ADD_mem[1]
	S += 48<T4_1T1_mem0
	S += T4_1T1_mem0<=T4_1T1

	T4_1T1_mem1 = S.Task('T4_1T1_mem1', length=1, delay_cost=1)
	T4_1T1_mem1 += ADD_mem[0]
	S += 46<T4_1T1_mem1
	S += T4_1T1_mem1<=T4_1T1

	T4_1T2 = S.Task('T4_1T2', length=1, delay_cost=1)
	T4_1T2 += alt(ADD)

	T4_1T2_mem0 = S.Task('T4_1T2_mem0', length=1, delay_cost=1)
	T4_1T2_mem0 += ADD_mem[3]
	S += 49<T4_1T2_mem0
	S += T4_1T2_mem0<=T4_1T2

	T4_1T2_mem1 = S.Task('T4_1T2_mem1', length=1, delay_cost=1)
	T4_1T2_mem1 += ADD_mem[1]
	S += 48<T4_1T2_mem1
	S += T4_1T2_mem1<=T4_1T2

	T4_1T3 = S.Task('T4_1T3', length=1, delay_cost=1)
	T4_1T3 += alt(ADD)

	T4_1T3_mem0 = S.Task('T4_1T3_mem0', length=1, delay_cost=1)
	T4_1T3_mem0 += ADD_mem[2]
	S += 47<T4_1T3_mem0
	S += T4_1T3_mem0<=T4_1T3

	T4_1T3_mem1 = S.Task('T4_1T3_mem1', length=1, delay_cost=1)
	T4_1T3_mem1 += ADD_mem[0]
	S += 46<T4_1T3_mem1
	S += T4_1T3_mem1<=T4_1T3

	T5_1T0_in = S.Task('T5_1T0_in', length=1, delay_cost=1)
	T5_1T0_in += alt(MUL_in)
	T5_1T0 = S.Task('T5_1T0', length=7, delay_cost=1)
	T5_1T0 += alt(MUL)
	S+=T5_1T0>=T5_1T0_in

	T5_1T0_mem0 = S.Task('T5_1T0_mem0', length=1, delay_cost=1)
	T5_1T0_mem0 += ADD_mem[0]
	S += 45<T5_1T0_mem0
	S += T5_1T0_mem0<=T5_1T0

	T5_1T0_mem1 = S.Task('T5_1T0_mem1', length=1, delay_cost=1)
	T5_1T0_mem1 += ADD_mem[0]
	S += 42<T5_1T0_mem1
	S += T5_1T0_mem1<=T5_1T0

	T5_1T1_in = S.Task('T5_1T1_in', length=1, delay_cost=1)
	T5_1T1_in += alt(MUL_in)
	T5_1T1 = S.Task('T5_1T1', length=7, delay_cost=1)
	T5_1T1 += alt(MUL)
	S+=T5_1T1>=T5_1T1_in

	T5_1T1_mem0 = S.Task('T5_1T1_mem0', length=1, delay_cost=1)
	T5_1T1_mem0 += ADD_mem[3]
	S += 43<T5_1T1_mem0
	S += T5_1T1_mem0<=T5_1T1

	T5_1T1_mem1 = S.Task('T5_1T1_mem1', length=1, delay_cost=1)
	T5_1T1_mem1 += ADD_mem[0]
	S += 41<T5_1T1_mem1
	S += T5_1T1_mem1<=T5_1T1

	T5_1T2 = S.Task('T5_1T2', length=1, delay_cost=1)
	T5_1T2 += alt(ADD)

	T5_1T2_mem0 = S.Task('T5_1T2_mem0', length=1, delay_cost=1)
	T5_1T2_mem0 += ADD_mem[0]
	S += 45<T5_1T2_mem0
	S += T5_1T2_mem0<=T5_1T2

	T5_1T2_mem1 = S.Task('T5_1T2_mem1', length=1, delay_cost=1)
	T5_1T2_mem1 += ADD_mem[3]
	S += 43<T5_1T2_mem1
	S += T5_1T2_mem1<=T5_1T2

	T5_1T3 = S.Task('T5_1T3', length=1, delay_cost=1)
	T5_1T3 += alt(ADD)

	T5_1T3_mem0 = S.Task('T5_1T3_mem0', length=1, delay_cost=1)
	T5_1T3_mem0 += ADD_mem[0]
	S += 42<T5_1T3_mem0
	S += T5_1T3_mem0<=T5_1T3

	T5_1T3_mem1 = S.Task('T5_1T3_mem1', length=1, delay_cost=1)
	T5_1T3_mem1 += ADD_mem[0]
	S += 41<T5_1T3_mem1
	S += T5_1T3_mem1<=T5_1T3

	T0_T4_in = S.Task('T0_T4_in', length=1, delay_cost=1)
	T0_T4_in += alt(MUL_in)
	T0_T4 = S.Task('T0_T4', length=7, delay_cost=1)
	T0_T4 += alt(MUL)
	S+=T0_T4>=T0_T4_in

	T0_T4_mem0 = S.Task('T0_T4_mem0', length=1, delay_cost=1)
	T0_T4_mem0 += ADD_mem[1]
	S += 40<T0_T4_mem0
	S += T0_T4_mem0<=T0_T4

	T0_T4_mem1 = S.Task('T0_T4_mem1', length=1, delay_cost=1)
	T0_T4_mem1 += ADD_mem[0]
	S += 38<T0_T4_mem1
	S += T0_T4_mem1<=T0_T4

	T0_T5 = S.Task('T0_T5', length=1, delay_cost=1)
	T0_T5 += alt(ADD)

	T0_T5_mem0 = S.Task('T0_T5_mem0', length=1, delay_cost=1)
	T0_T5_mem0 += MUL_mem[0]
	S += 14<T0_T5_mem0
	S += T0_T5_mem0<=T0_T5

	T0_T5_mem1 = S.Task('T0_T5_mem1', length=1, delay_cost=1)
	T0_T5_mem1 += MUL_mem[0]
	S += 13<T0_T5_mem1
	S += T0_T5_mem1<=T0_T5

	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	T0_0 += alt(ADD)

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	T0_0_mem0 += MUL_mem[0]
	S += 14<T0_0_mem0
	S += T0_0_mem0<=T0_0

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	T0_0_mem1 += MUL_mem[0]
	S += 13<T0_0_mem1
	S += T0_0_mem1<=T0_0

	T1_T4_in = S.Task('T1_T4_in', length=1, delay_cost=1)
	T1_T4_in += alt(MUL_in)
	T1_T4 = S.Task('T1_T4', length=7, delay_cost=1)
	T1_T4 += alt(MUL)
	S+=T1_T4>=T1_T4_in

	T1_T4_mem0 = S.Task('T1_T4_mem0', length=1, delay_cost=1)
	T1_T4_mem0 += ADD_mem[1]
	S += 37<T1_T4_mem0
	S += T1_T4_mem0<=T1_T4

	T1_T4_mem1 = S.Task('T1_T4_mem1', length=1, delay_cost=1)
	T1_T4_mem1 += ADD_mem[1]
	S += 34<T1_T4_mem1
	S += T1_T4_mem1<=T1_T4

	T1_T5 = S.Task('T1_T5', length=1, delay_cost=1)
	T1_T5 += alt(ADD)

	T1_T5_mem0 = S.Task('T1_T5_mem0', length=1, delay_cost=1)
	T1_T5_mem0 += MUL_mem[0]
	S += 17<T1_T5_mem0
	S += T1_T5_mem0<=T1_T5

	T1_T5_mem1 = S.Task('T1_T5_mem1', length=1, delay_cost=1)
	T1_T5_mem1 += MUL_mem[0]
	S += 10<T1_T5_mem1
	S += T1_T5_mem1<=T1_T5

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	T1_0 += alt(ADD)

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	T1_0_mem0 += MUL_mem[0]
	S += 17<T1_0_mem0
	S += T1_0_mem0<=T1_0

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	T1_0_mem1 += MUL_mem[0]
	S += 10<T1_0_mem1
	S += T1_0_mem1<=T1_0

	T2_1T4_in = S.Task('T2_1T4_in', length=1, delay_cost=1)
	T2_1T4_in += alt(MUL_in)
	T2_1T4 = S.Task('T2_1T4', length=7, delay_cost=1)
	T2_1T4 += alt(MUL)
	S+=T2_1T4>=T2_1T4_in

	T2_1T4_mem0 = S.Task('T2_1T4_mem0', length=1, delay_cost=1)
	T2_1T4_mem0 += ADD_mem[0]
	S += 33<T2_1T4_mem0
	S += T2_1T4_mem0<=T2_1T4

	T2_1T4_mem1 = S.Task('T2_1T4_mem1', length=1, delay_cost=1)
	T2_1T4_mem1 += ADD_mem[0]
	S += 29<T2_1T4_mem1
	S += T2_1T4_mem1<=T2_1T4

	T2_1T5 = S.Task('T2_1T5', length=1, delay_cost=1)
	T2_1T5 += alt(ADD)

	T2_1T5_mem0 = S.Task('T2_1T5_mem0', length=1, delay_cost=1)
	T2_1T5_mem0 += MUL_mem[0]
	S += 9<T2_1T5_mem0
	S += T2_1T5_mem0<=T2_1T5

	T2_1T5_mem1 = S.Task('T2_1T5_mem1', length=1, delay_cost=1)
	T2_1T5_mem1 += MUL_mem[0]
	S += 7<T2_1T5_mem1
	S += T2_1T5_mem1<=T2_1T5

	T2_10 = S.Task('T2_10', length=1, delay_cost=1)
	T2_10 += alt(ADD)

	T2_10_mem0 = S.Task('T2_10_mem0', length=1, delay_cost=1)
	T2_10_mem0 += MUL_mem[0]
	S += 9<T2_10_mem0
	S += T2_10_mem0<=T2_10

	T2_10_mem1 = S.Task('T2_10_mem1', length=1, delay_cost=1)
	T2_10_mem1 += MUL_mem[0]
	S += 7<T2_10_mem1
	S += T2_10_mem1<=T2_10

	T3_4T0_in = S.Task('T3_4T0_in', length=1, delay_cost=1)
	T3_4T0_in += alt(MUL_in)
	T3_4T0 = S.Task('T3_4T0', length=7, delay_cost=1)
	T3_4T0 += alt(MUL)
	S+=T3_4T0>=T3_4T0_in

	T3_4T0_mem0 = S.Task('T3_4T0_mem0', length=1, delay_cost=1)
	T3_4T0_mem0 += ADD_mem[0]
	S += 36<T3_4T0_mem0
	S += T3_4T0_mem0<=T3_4T0

	T3_4T0_mem1 = S.Task('T3_4T0_mem1', length=1, delay_cost=1)
	T3_4T0_mem1 += ADD_mem[2]
	S += 31<T3_4T0_mem1
	S += T3_4T0_mem1<=T3_4T0

	T3_4T1_in = S.Task('T3_4T1_in', length=1, delay_cost=1)
	T3_4T1_in += alt(MUL_in)
	T3_4T1 = S.Task('T3_4T1', length=7, delay_cost=1)
	T3_4T1 += alt(MUL)
	S+=T3_4T1>=T3_4T1_in

	T3_4T1_mem0 = S.Task('T3_4T1_mem0', length=1, delay_cost=1)
	T3_4T1_mem0 += ADD_mem[2]
	S += 32<T3_4T1_mem0
	S += T3_4T1_mem0<=T3_4T1

	T3_4T1_mem1 = S.Task('T3_4T1_mem1', length=1, delay_cost=1)
	T3_4T1_mem1 += ADD_mem[2]
	S += 28<T3_4T1_mem1
	S += T3_4T1_mem1<=T3_4T1

	T3_4T2 = S.Task('T3_4T2', length=1, delay_cost=1)
	T3_4T2 += alt(ADD)

	T3_4T2_mem0 = S.Task('T3_4T2_mem0', length=1, delay_cost=1)
	T3_4T2_mem0 += ADD_mem[0]
	S += 36<T3_4T2_mem0
	S += T3_4T2_mem0<=T3_4T2

	T3_4T2_mem1 = S.Task('T3_4T2_mem1', length=1, delay_cost=1)
	T3_4T2_mem1 += ADD_mem[2]
	S += 32<T3_4T2_mem1
	S += T3_4T2_mem1<=T3_4T2

	T3_4T3 = S.Task('T3_4T3', length=1, delay_cost=1)
	T3_4T3 += alt(ADD)

	T3_4T3_mem0 = S.Task('T3_4T3_mem0', length=1, delay_cost=1)
	T3_4T3_mem0 += ADD_mem[2]
	S += 31<T3_4T3_mem0
	S += T3_4T3_mem0<=T3_4T3

	T3_4T3_mem1 = S.Task('T3_4T3_mem1', length=1, delay_cost=1)
	T3_4T3_mem1 += ADD_mem[2]
	S += 28<T3_4T3_mem1
	S += T3_4T3_mem1<=T3_4T3

	T4_7T0_in = S.Task('T4_7T0_in', length=1, delay_cost=1)
	T4_7T0_in += alt(MUL_in)
	T4_7T0 = S.Task('T4_7T0', length=7, delay_cost=1)
	T4_7T0 += alt(MUL)
	S+=T4_7T0>=T4_7T0_in

	T4_7T0_mem0 = S.Task('T4_7T0_mem0', length=1, delay_cost=1)
	T4_7T0_mem0 += ADD_mem[0]
	S += 30<T4_7T0_mem0
	S += T4_7T0_mem0<=T4_7T0

	T4_7T0_mem1 = S.Task('T4_7T0_mem1', length=1, delay_cost=1)
	T4_7T0_mem1 += ADD_mem[3]
	S += 26<T4_7T0_mem1
	S += T4_7T0_mem1<=T4_7T0

	T4_7T1_in = S.Task('T4_7T1_in', length=1, delay_cost=1)
	T4_7T1_in += alt(MUL_in)
	T4_7T1 = S.Task('T4_7T1', length=7, delay_cost=1)
	T4_7T1 += alt(MUL)
	S+=T4_7T1>=T4_7T1_in

	T4_7T1_mem0 = S.Task('T4_7T1_mem0', length=1, delay_cost=1)
	T4_7T1_mem0 += ADD_mem[0]
	S += 27<T4_7T1_mem0
	S += T4_7T1_mem0<=T4_7T1

	T4_7T1_mem1 = S.Task('T4_7T1_mem1', length=1, delay_cost=1)
	T4_7T1_mem1 += ADD_mem[0]
	S += 24<T4_7T1_mem1
	S += T4_7T1_mem1<=T4_7T1

	T4_7T2 = S.Task('T4_7T2', length=1, delay_cost=1)
	T4_7T2 += alt(ADD)

	T4_7T2_mem0 = S.Task('T4_7T2_mem0', length=1, delay_cost=1)
	T4_7T2_mem0 += ADD_mem[0]
	S += 30<T4_7T2_mem0
	S += T4_7T2_mem0<=T4_7T2

	T4_7T2_mem1 = S.Task('T4_7T2_mem1', length=1, delay_cost=1)
	T4_7T2_mem1 += ADD_mem[0]
	S += 27<T4_7T2_mem1
	S += T4_7T2_mem1<=T4_7T2

	T4_7T3 = S.Task('T4_7T3', length=1, delay_cost=1)
	T4_7T3 += alt(ADD)

	T4_7T3_mem0 = S.Task('T4_7T3_mem0', length=1, delay_cost=1)
	T4_7T3_mem0 += ADD_mem[3]
	S += 26<T4_7T3_mem0
	S += T4_7T3_mem0<=T4_7T3

	T4_7T3_mem1 = S.Task('T4_7T3_mem1', length=1, delay_cost=1)
	T4_7T3_mem1 += ADD_mem[0]
	S += 24<T4_7T3_mem1
	S += T4_7T3_mem1<=T4_7T3

	T5_6T0_in = S.Task('T5_6T0_in', length=1, delay_cost=1)
	T5_6T0_in += alt(MUL_in)
	T5_6T0 = S.Task('T5_6T0', length=7, delay_cost=1)
	T5_6T0 += alt(MUL)
	S+=T5_6T0>=T5_6T0_in

	T5_6T0_mem0 = S.Task('T5_6T0_mem0', length=1, delay_cost=1)
	T5_6T0_mem0 += ADD_mem[0]
	S += 22<T5_6T0_mem0
	S += T5_6T0_mem0<=T5_6T0

	T5_6T0_mem1 = S.Task('T5_6T0_mem1', length=1, delay_cost=1)
	T5_6T0_mem1 += ADD_mem[1]
	S += 23<T5_6T0_mem1
	S += T5_6T0_mem1<=T5_6T0

	T5_6T1_in = S.Task('T5_6T1_in', length=1, delay_cost=1)
	T5_6T1_in += alt(MUL_in)
	T5_6T1 = S.Task('T5_6T1', length=7, delay_cost=1)
	T5_6T1 += alt(MUL)
	S+=T5_6T1>=T5_6T1_in

	T5_6T1_mem0 = S.Task('T5_6T1_mem0', length=1, delay_cost=1)
	T5_6T1_mem0 += ADD_mem[0]
	S += 19<T5_6T1_mem0
	S += T5_6T1_mem0<=T5_6T1

	T5_6T1_mem1 = S.Task('T5_6T1_mem1', length=1, delay_cost=1)
	T5_6T1_mem1 += ADD_mem[3]
	S += 17<T5_6T1_mem1
	S += T5_6T1_mem1<=T5_6T1

	T5_6T2 = S.Task('T5_6T2', length=1, delay_cost=1)
	T5_6T2 += alt(ADD)

	T5_6T2_mem0 = S.Task('T5_6T2_mem0', length=1, delay_cost=1)
	T5_6T2_mem0 += ADD_mem[0]
	S += 22<T5_6T2_mem0
	S += T5_6T2_mem0<=T5_6T2

	T5_6T2_mem1 = S.Task('T5_6T2_mem1', length=1, delay_cost=1)
	T5_6T2_mem1 += ADD_mem[0]
	S += 19<T5_6T2_mem1
	S += T5_6T2_mem1<=T5_6T2

	T5_6T3 = S.Task('T5_6T3', length=1, delay_cost=1)
	T5_6T3 += alt(ADD)

	T5_6T3_mem0 = S.Task('T5_6T3_mem0', length=1, delay_cost=1)
	T5_6T3_mem0 += ADD_mem[1]
	S += 23<T5_6T3_mem0
	S += T5_6T3_mem0<=T5_6T3

	T5_6T3_mem1 = S.Task('T5_6T3_mem1', length=1, delay_cost=1)
	T5_6T3_mem1 += ADD_mem[3]
	S += 17<T5_6T3_mem1
	S += T5_6T3_mem1<=T5_6T3

	T0_1T0_in = S.Task('T0_1T0_in', length=1, delay_cost=1)
	T0_1T0_in += alt(MUL_in)
	T0_1T0 = S.Task('T0_1T0', length=7, delay_cost=1)
	T0_1T0 += alt(MUL)
	S+=T0_1T0>=T0_1T0_in

	T0_1T0_mem0 = S.Task('T0_1T0_mem0', length=1, delay_cost=1)
	T0_1T0_mem0 += ADD_mem[1]
	S += 16<T0_1T0_mem0
	S += T0_1T0_mem0<=T0_1T0

	T0_1T0_mem1 = S.Task('T0_1T0_mem1', length=1, delay_cost=1)
	T0_1T0_mem1 += ADD_mem[2]
	S += 59<T0_1T0_mem1
	S += T0_1T0_mem1<=T0_1T0

	T0_1T1_in = S.Task('T0_1T1_in', length=1, delay_cost=1)
	T0_1T1_in += alt(MUL_in)
	T0_1T1 = S.Task('T0_1T1', length=7, delay_cost=1)
	T0_1T1 += alt(MUL)
	S+=T0_1T1>=T0_1T1_in

	T0_1T1_mem0 = S.Task('T0_1T1_mem0', length=1, delay_cost=1)
	T0_1T1_mem0 += ADD_mem[0]
	S += 15<T0_1T1_mem0
	S += T0_1T1_mem0<=T0_1T1

	T0_1T1_mem1 = S.Task('T0_1T1_mem1', length=1, delay_cost=1)
	T0_1T1_mem1 += ADD_mem[3]
	S += 60<T0_1T1_mem1
	S += T0_1T1_mem1<=T0_1T1

	T0_1T2 = S.Task('T0_1T2', length=1, delay_cost=1)
	T0_1T2 += alt(ADD)

	T0_1T2_mem0 = S.Task('T0_1T2_mem0', length=1, delay_cost=1)
	T0_1T2_mem0 += ADD_mem[1]
	S += 16<T0_1T2_mem0
	S += T0_1T2_mem0<=T0_1T2

	T0_1T2_mem1 = S.Task('T0_1T2_mem1', length=1, delay_cost=1)
	T0_1T2_mem1 += ADD_mem[0]
	S += 15<T0_1T2_mem1
	S += T0_1T2_mem1<=T0_1T2

	T0_1T3 = S.Task('T0_1T3', length=1, delay_cost=1)
	T0_1T3 += alt(ADD)

	T0_1T3_mem0 = S.Task('T0_1T3_mem0', length=1, delay_cost=1)
	T0_1T3_mem0 += ADD_mem[2]
	S += 59<T0_1T3_mem0
	S += T0_1T3_mem0<=T0_1T3

	T0_1T3_mem1 = S.Task('T0_1T3_mem1', length=1, delay_cost=1)
	T0_1T3_mem1 += ADD_mem[3]
	S += 60<T0_1T3_mem1
	S += T0_1T3_mem1<=T0_1T3

	T1_1T0_in = S.Task('T1_1T0_in', length=1, delay_cost=1)
	T1_1T0_in += alt(MUL_in)
	T1_1T0 = S.Task('T1_1T0', length=7, delay_cost=1)
	T1_1T0 += alt(MUL)
	S+=T1_1T0>=T1_1T0_in

	T1_1T0_mem0 = S.Task('T1_1T0_mem0', length=1, delay_cost=1)
	T1_1T0_mem0 += ADD_mem[1]
	S += 53<T1_1T0_mem0
	S += T1_1T0_mem0<=T1_1T0

	T1_1T0_mem1 = S.Task('T1_1T0_mem1', length=1, delay_cost=1)
	T1_1T0_mem1 += ADD_mem[1]
	S += 57<T1_1T0_mem1
	S += T1_1T0_mem1<=T1_1T0

	T1_1T1_in = S.Task('T1_1T1_in', length=1, delay_cost=1)
	T1_1T1_in += alt(MUL_in)
	T1_1T1 = S.Task('T1_1T1', length=7, delay_cost=1)
	T1_1T1 += alt(MUL)
	S+=T1_1T1>=T1_1T1_in

	T1_1T1_mem0 = S.Task('T1_1T1_mem0', length=1, delay_cost=1)
	T1_1T1_mem0 += ADD_mem[1]
	S += 55<T1_1T1_mem0
	S += T1_1T1_mem0<=T1_1T1

	T1_1T1_mem1 = S.Task('T1_1T1_mem1', length=1, delay_cost=1)
	T1_1T1_mem1 += ADD_mem[3]
	S += 58<T1_1T1_mem1
	S += T1_1T1_mem1<=T1_1T1

	T1_1T2 = S.Task('T1_1T2', length=1, delay_cost=1)
	T1_1T2 += alt(ADD)

	T1_1T2_mem0 = S.Task('T1_1T2_mem0', length=1, delay_cost=1)
	T1_1T2_mem0 += ADD_mem[1]
	S += 53<T1_1T2_mem0
	S += T1_1T2_mem0<=T1_1T2

	T1_1T2_mem1 = S.Task('T1_1T2_mem1', length=1, delay_cost=1)
	T1_1T2_mem1 += ADD_mem[1]
	S += 55<T1_1T2_mem1
	S += T1_1T2_mem1<=T1_1T2

	T1_1T3 = S.Task('T1_1T3', length=1, delay_cost=1)
	T1_1T3 += alt(ADD)

	T1_1T3_mem0 = S.Task('T1_1T3_mem0', length=1, delay_cost=1)
	T1_1T3_mem0 += ADD_mem[1]
	S += 57<T1_1T3_mem0
	S += T1_1T3_mem0<=T1_1T3

	T1_1T3_mem1 = S.Task('T1_1T3_mem1', length=1, delay_cost=1)
	T1_1T3_mem1 += ADD_mem[3]
	S += 58<T1_1T3_mem1
	S += T1_1T3_mem1<=T1_1T3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01, time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "mul_mul1_add4/mul_mul1_add4_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_mul_mul1_add4_2(0, 0)