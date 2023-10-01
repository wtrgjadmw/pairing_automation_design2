from pyschedule import Scenario, solvers, plotters, alt

def solve_square_mul1_add4_1(ConstStep, ExpStep):
	horizon = 127
	S=Scenario("square_mul1_add4_1",horizon = horizon)

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
	T8_1T0_in = S.Task('T8_1T0_in', length=1, delay_cost=1)
	S += T8_1T0_in >= 0
	T8_1T0_in += MUL_in[0]

	T8_1T0_mem0 = S.Task('T8_1T0_mem0', length=1, delay_cost=1)
	S += T8_1T0_mem0 >= 0
	T8_1T0_mem0 += INPUT_mem_r

	T8_1T0_mem1 = S.Task('T8_1T0_mem1', length=1, delay_cost=1)
	S += T8_1T0_mem1 >= 0
	T8_1T0_mem1 += INPUT_mem_r

	T7_T1_in = S.Task('T7_T1_in', length=1, delay_cost=1)
	S += T7_T1_in >= 1
	T7_T1_in += MUL_in[0]

	T7_T1_mem0 = S.Task('T7_T1_mem0', length=1, delay_cost=1)
	S += T7_T1_mem0 >= 1
	T7_T1_mem0 += INPUT_mem_r

	T7_T1_mem1 = S.Task('T7_T1_mem1', length=1, delay_cost=1)
	S += T7_T1_mem1 >= 1
	T7_T1_mem1 += INPUT_mem_r

	T8_1T0 = S.Task('T8_1T0', length=7, delay_cost=1)
	S += T8_1T0 >= 1
	T8_1T0 += MUL[0]

	T7_T1 = S.Task('T7_T1', length=7, delay_cost=1)
	S += T7_T1 >= 2
	T7_T1 += MUL[0]

	T8_1T1_in = S.Task('T8_1T1_in', length=1, delay_cost=1)
	S += T8_1T1_in >= 2
	T8_1T1_in += MUL_in[0]

	T8_1T1_mem0 = S.Task('T8_1T1_mem0', length=1, delay_cost=1)
	S += T8_1T1_mem0 >= 2
	T8_1T1_mem0 += INPUT_mem_r

	T8_1T1_mem1 = S.Task('T8_1T1_mem1', length=1, delay_cost=1)
	S += T8_1T1_mem1 >= 2
	T8_1T1_mem1 += INPUT_mem_r

	T7_T0_in = S.Task('T7_T0_in', length=1, delay_cost=1)
	S += T7_T0_in >= 3
	T7_T0_in += MUL_in[0]

	T7_T0_mem0 = S.Task('T7_T0_mem0', length=1, delay_cost=1)
	S += T7_T0_mem0 >= 3
	T7_T0_mem0 += INPUT_mem_r

	T7_T0_mem1 = S.Task('T7_T0_mem1', length=1, delay_cost=1)
	S += T7_T0_mem1 >= 3
	T7_T0_mem1 += INPUT_mem_r

	T8_1T1 = S.Task('T8_1T1', length=7, delay_cost=1)
	S += T8_1T1 >= 3
	T8_1T1 += MUL[0]

	T6_T1_in = S.Task('T6_T1_in', length=1, delay_cost=1)
	S += T6_T1_in >= 4
	T6_T1_in += MUL_in[0]

	T6_T1_mem0 = S.Task('T6_T1_mem0', length=1, delay_cost=1)
	S += T6_T1_mem0 >= 4
	T6_T1_mem0 += INPUT_mem_r

	T6_T1_mem1 = S.Task('T6_T1_mem1', length=1, delay_cost=1)
	S += T6_T1_mem1 >= 4
	T6_T1_mem1 += INPUT_mem_r

	T7_T0 = S.Task('T7_T0', length=7, delay_cost=1)
	S += T7_T0 >= 4
	T7_T0 += MUL[0]

	T6_T0_in = S.Task('T6_T0_in', length=1, delay_cost=1)
	S += T6_T0_in >= 5
	T6_T0_in += MUL_in[0]

	T6_T0_mem0 = S.Task('T6_T0_mem0', length=1, delay_cost=1)
	S += T6_T0_mem0 >= 5
	T6_T0_mem0 += INPUT_mem_r

	T6_T0_mem1 = S.Task('T6_T0_mem1', length=1, delay_cost=1)
	S += T6_T0_mem1 >= 5
	T6_T0_mem1 += INPUT_mem_r

	T6_T1 = S.Task('T6_T1', length=7, delay_cost=1)
	S += T6_T1 >= 5
	T6_T1 += MUL[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 6
	T41_mem0 += INPUT_mem_r

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 6
	T41_mem1 += INPUT_mem_r

	T6_T0 = S.Task('T6_T0', length=7, delay_cost=1)
	S += T6_T0 >= 6
	T6_T0 += MUL[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 7
	T41 += ADD[1]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 7
	T50_mem0 += INPUT_mem_r

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 7
	T50_mem1 += INPUT_mem_r

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 8
	T21_mem0 += INPUT_mem_r

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 8
	T21_mem1 += INPUT_mem_r

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 8
	T50 += ADD[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 9
	T21 += ADD[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 9
	T40_mem0 += INPUT_mem_r

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 9
	T40_mem1 += INPUT_mem_r

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 10
	T40 += ADD[3]

	T4_10_mem0 = S.Task('T4_10_mem0', length=1, delay_cost=1)
	S += T4_10_mem0 >= 10
	T4_10_mem0 += INPUT_mem_r

	T4_10_mem1 = S.Task('T4_10_mem1', length=1, delay_cost=1)
	S += T4_10_mem1 >= 10
	T4_10_mem1 += INPUT_mem_r

	T4_10 = S.Task('T4_10', length=1, delay_cost=1)
	S += T4_10 >= 11
	T4_10 += ADD[0]

	T4_11_mem0 = S.Task('T4_11_mem0', length=1, delay_cost=1)
	S += T4_11_mem0 >= 11
	T4_11_mem0 += INPUT_mem_r

	T4_11_mem1 = S.Task('T4_11_mem1', length=1, delay_cost=1)
	S += T4_11_mem1 >= 11
	T4_11_mem1 += INPUT_mem_r

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 12
	T20_mem0 += INPUT_mem_r

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 12
	T20_mem1 += INPUT_mem_r

	T4_11 = S.Task('T4_11', length=1, delay_cost=1)
	S += T4_11 >= 12
	T4_11 += ADD[1]

	T10_0_mem0 = S.Task('T10_0_mem0', length=1, delay_cost=1)
	S += T10_0_mem0 >= 13
	T10_0_mem0 += INPUT_mem_r

	T10_0_mem1 = S.Task('T10_0_mem1', length=1, delay_cost=1)
	S += T10_0_mem1 >= 13
	T10_0_mem1 += INPUT_mem_r

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 13
	T20 += ADD[0]

	T10_0 = S.Task('T10_0', length=1, delay_cost=1)
	S += T10_0 >= 14
	T10_0 += ADD[0]

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	S += T5_11_mem0 >= 14
	T5_11_mem0 += INPUT_mem_r

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	S += T5_11_mem1 >= 14
	T5_11_mem1 += INPUT_mem_r

	T10_1_mem0 = S.Task('T10_1_mem0', length=1, delay_cost=1)
	S += T10_1_mem0 >= 15
	T10_1_mem0 += INPUT_mem_r

	T10_1_mem1 = S.Task('T10_1_mem1', length=1, delay_cost=1)
	S += T10_1_mem1 >= 15
	T10_1_mem1 += INPUT_mem_r

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	S += T5_11 >= 15
	T5_11 += ADD[2]

	T10_1 = S.Task('T10_1', length=1, delay_cost=1)
	S += T10_1 >= 16
	T10_1 += ADD[3]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 16
	T30_mem0 += INPUT_mem_r

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 16
	T30_mem1 += INPUT_mem_r

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 17
	T00_mem0 += INPUT_mem_r

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 17
	T00_mem1 += INPUT_mem_r

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 17
	T30 += ADD[0]

	T00 = S.Task('T00', length=1, delay_cost=1)
	S += T00 >= 18
	T00 += ADD[0]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 18
	T3_0_mem0 += INPUT_mem_r

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 18
	T3_0_mem1 += INPUT_mem_r

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 19
	T3_0 += ADD[0]

	T9_31_mem0 = S.Task('T9_31_mem0', length=1, delay_cost=1)
	S += T9_31_mem0 >= 19
	T9_31_mem0 += INPUT_mem_r

	T9_31_mem1 = S.Task('T9_31_mem1', length=1, delay_cost=1)
	S += T9_31_mem1 >= 19
	T9_31_mem1 += INPUT_mem_r

	T8_1T3_mem0 = S.Task('T8_1T3_mem0', length=1, delay_cost=1)
	S += T8_1T3_mem0 >= 20
	T8_1T3_mem0 += INPUT_mem_r

	T8_1T3_mem1 = S.Task('T8_1T3_mem1', length=1, delay_cost=1)
	S += T8_1T3_mem1 >= 20
	T8_1T3_mem1 += INPUT_mem_r

	T9_31 = S.Task('T9_31', length=1, delay_cost=1)
	S += T9_31 >= 20
	T9_31 += ADD[0]

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	S += T3_1_mem0 >= 21
	T3_1_mem0 += INPUT_mem_r

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	S += T3_1_mem1 >= 21
	T3_1_mem1 += INPUT_mem_r

	T8_1T3 = S.Task('T8_1T3', length=1, delay_cost=1)
	S += T8_1T3 >= 21
	T8_1T3 += ADD[2]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 22
	T31_mem0 += INPUT_mem_r

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 22
	T31_mem1 += INPUT_mem_r

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 22
	T3_1 += ADD[0]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 23
	T31 += ADD[1]

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	S += T5_10_mem0 >= 23
	T5_10_mem0 += INPUT_mem_r

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	S += T5_10_mem1 >= 23
	T5_10_mem1 += INPUT_mem_r

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 24
	T11_mem0 += INPUT_mem_r

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 24
	T11_mem1 += INPUT_mem_r

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	S += T5_10 >= 24
	T5_10 += ADD[1]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 25
	T10_mem0 += INPUT_mem_r

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 25
	T10_mem1 += INPUT_mem_r

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 25
	T11 += ADD[1]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 26
	T10 += ADD[0]

	T9_30_mem0 = S.Task('T9_30_mem0', length=1, delay_cost=1)
	S += T9_30_mem0 >= 26
	T9_30_mem0 += INPUT_mem_r

	T9_30_mem1 = S.Task('T9_30_mem1', length=1, delay_cost=1)
	S += T9_30_mem1 >= 26
	T9_30_mem1 += INPUT_mem_r

	T8_1T2_mem0 = S.Task('T8_1T2_mem0', length=1, delay_cost=1)
	S += T8_1T2_mem0 >= 27
	T8_1T2_mem0 += INPUT_mem_r

	T8_1T2_mem1 = S.Task('T8_1T2_mem1', length=1, delay_cost=1)
	S += T8_1T2_mem1 >= 27
	T8_1T2_mem1 += INPUT_mem_r

	T9_30 = S.Task('T9_30', length=1, delay_cost=1)
	S += T9_30 >= 27
	T9_30 += ADD[2]

	T4_20_mem0 = S.Task('T4_20_mem0', length=1, delay_cost=1)
	S += T4_20_mem0 >= 28
	T4_20_mem0 += INPUT_mem_r

	T4_20_mem1 = S.Task('T4_20_mem1', length=1, delay_cost=1)
	S += T4_20_mem1 >= 28
	T4_20_mem1 += INPUT_mem_r

	T8_1T2 = S.Task('T8_1T2', length=1, delay_cost=1)
	S += T8_1T2 >= 28
	T8_1T2 += ADD[1]

	T4_20 = S.Task('T4_20', length=1, delay_cost=1)
	S += T4_20 >= 29
	T4_20 += ADD[0]

	T4_21_mem0 = S.Task('T4_21_mem0', length=1, delay_cost=1)
	S += T4_21_mem0 >= 29
	T4_21_mem0 += INPUT_mem_r

	T4_21_mem1 = S.Task('T4_21_mem1', length=1, delay_cost=1)
	S += T4_21_mem1 >= 29
	T4_21_mem1 += INPUT_mem_r

	T4_21 = S.Task('T4_21', length=1, delay_cost=1)
	S += T4_21 >= 30
	T4_21 += ADD[0]

	T7_T3_mem0 = S.Task('T7_T3_mem0', length=1, delay_cost=1)
	S += T7_T3_mem0 >= 30
	T7_T3_mem0 += INPUT_mem_r

	T7_T3_mem1 = S.Task('T7_T3_mem1', length=1, delay_cost=1)
	S += T7_T3_mem1 >= 30
	T7_T3_mem1 += INPUT_mem_r

	T7_T2_mem0 = S.Task('T7_T2_mem0', length=1, delay_cost=1)
	S += T7_T2_mem0 >= 31
	T7_T2_mem0 += INPUT_mem_r

	T7_T2_mem1 = S.Task('T7_T2_mem1', length=1, delay_cost=1)
	S += T7_T2_mem1 >= 31
	T7_T2_mem1 += INPUT_mem_r

	T7_T3 = S.Task('T7_T3', length=1, delay_cost=1)
	S += T7_T3 >= 31
	T7_T3 += ADD[3]

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 32
	T01_mem0 += INPUT_mem_r

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	S += T01_mem1 >= 32
	T01_mem1 += INPUT_mem_r

	T7_T2 = S.Task('T7_T2', length=1, delay_cost=1)
	S += T7_T2 >= 32
	T7_T2 += ADD[1]

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 33
	T01 += ADD[2]

	T6_T3_mem0 = S.Task('T6_T3_mem0', length=1, delay_cost=1)
	S += T6_T3_mem0 >= 33
	T6_T3_mem0 += INPUT_mem_r

	T6_T3_mem1 = S.Task('T6_T3_mem1', length=1, delay_cost=1)
	S += T6_T3_mem1 >= 33
	T6_T3_mem1 += INPUT_mem_r

	T6_T2_mem0 = S.Task('T6_T2_mem0', length=1, delay_cost=1)
	S += T6_T2_mem0 >= 34
	T6_T2_mem0 += INPUT_mem_r

	T6_T2_mem1 = S.Task('T6_T2_mem1', length=1, delay_cost=1)
	S += T6_T2_mem1 >= 34
	T6_T2_mem1 += INPUT_mem_r

	T6_T3 = S.Task('T6_T3', length=1, delay_cost=1)
	S += T6_T3 >= 34
	T6_T3 += ADD[0]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 35
	T51_mem0 += INPUT_mem_r

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 35
	T51_mem1 += INPUT_mem_r

	T6_T2 = S.Task('T6_T2', length=1, delay_cost=1)
	S += T6_T2 >= 35
	T6_T2 += ADD[2]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 36
	T51 += ADD[0]


	# new tasks
	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	T0_0 += alt(ADD)

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	T0_0_mem0 += INPUT_mem_r
	S += T0_0_mem0<=T0_0

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	T0_0_mem1 += ADD_mem[0]
	S += 18<T0_0_mem1
	S += T0_0_mem1<=T0_0

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	T0_1 += alt(ADD)

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	T0_1_mem0 += INPUT_mem_r
	S += T0_1_mem0<=T0_1

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	T0_1_mem1 += ADD_mem[2]
	S += 33<T0_1_mem1
	S += T0_1_mem1<=T0_1

	T6T3 = S.Task('T6T3', length=1, delay_cost=1)
	T6T3 += alt(ADD)

	T6T3_mem0 = S.Task('T6T3_mem0', length=1, delay_cost=1)
	T6T3_mem0 += ADD_mem[0]
	S += 17<T6T3_mem0
	S += T6T3_mem0<=T6T3

	T6T3_mem1 = S.Task('T6T3_mem1', length=1, delay_cost=1)
	T6T3_mem1 += ADD_mem[1]
	S += 23<T6T3_mem1
	S += T6T3_mem1<=T6T3

	T7T0_in = S.Task('T7T0_in', length=1, delay_cost=1)
	T7T0_in += alt(MUL_in)
	T7T0 = S.Task('T7T0', length=7, delay_cost=1)
	T7T0 += alt(MUL)
	S+=T7T0>=T7T0_in

	T7T0_mem0 = S.Task('T7T0_mem0', length=1, delay_cost=1)
	T7T0_mem0 += ADD_mem[0]
	S += 26<T7T0_mem0
	S += T7T0_mem0<=T7T0

	T7T0_mem1 = S.Task('T7T0_mem1', length=1, delay_cost=1)
	T7T0_mem1 += ADD_mem[3]
	S += 10<T7T0_mem1
	S += T7T0_mem1<=T7T0

	T7T1_in = S.Task('T7T1_in', length=1, delay_cost=1)
	T7T1_in += alt(MUL_in)
	T7T1 = S.Task('T7T1', length=7, delay_cost=1)
	T7T1 += alt(MUL)
	S+=T7T1>=T7T1_in

	T7T1_mem0 = S.Task('T7T1_mem0', length=1, delay_cost=1)
	T7T1_mem0 += ADD_mem[1]
	S += 25<T7T1_mem0
	S += T7T1_mem0<=T7T1

	T7T1_mem1 = S.Task('T7T1_mem1', length=1, delay_cost=1)
	T7T1_mem1 += ADD_mem[1]
	S += 7<T7T1_mem1
	S += T7T1_mem1<=T7T1

	T7T2 = S.Task('T7T2', length=1, delay_cost=1)
	T7T2 += alt(ADD)

	T7T2_mem0 = S.Task('T7T2_mem0', length=1, delay_cost=1)
	T7T2_mem0 += ADD_mem[0]
	S += 26<T7T2_mem0
	S += T7T2_mem0<=T7T2

	T7T2_mem1 = S.Task('T7T2_mem1', length=1, delay_cost=1)
	T7T2_mem1 += ADD_mem[1]
	S += 25<T7T2_mem1
	S += T7T2_mem1<=T7T2

	T7T3 = S.Task('T7T3', length=1, delay_cost=1)
	T7T3 += alt(ADD)

	T7T3_mem0 = S.Task('T7T3_mem0', length=1, delay_cost=1)
	T7T3_mem0 += ADD_mem[3]
	S += 10<T7T3_mem0
	S += T7T3_mem0<=T7T3

	T7T3_mem1 = S.Task('T7T3_mem1', length=1, delay_cost=1)
	T7T3_mem1 += ADD_mem[1]
	S += 7<T7T3_mem1
	S += T7T3_mem1<=T7T3

	T8T0_in = S.Task('T8T0_in', length=1, delay_cost=1)
	T8T0_in += alt(MUL_in)
	T8T0 = S.Task('T8T0', length=7, delay_cost=1)
	T8T0 += alt(MUL)
	S+=T8T0>=T8T0_in

	T8T0_mem0 = S.Task('T8T0_mem0', length=1, delay_cost=1)
	T8T0_mem0 += ADD_mem[0]
	S += 13<T8T0_mem0
	S += T8T0_mem0<=T8T0

	T8T0_mem1 = S.Task('T8T0_mem1', length=1, delay_cost=1)
	T8T0_mem1 += ADD_mem[0]
	S += 8<T8T0_mem1
	S += T8T0_mem1<=T8T0

	T8T1_in = S.Task('T8T1_in', length=1, delay_cost=1)
	T8T1_in += alt(MUL_in)
	T8T1 = S.Task('T8T1', length=7, delay_cost=1)
	T8T1 += alt(MUL)
	S+=T8T1>=T8T1_in

	T8T1_mem0 = S.Task('T8T1_mem0', length=1, delay_cost=1)
	T8T1_mem0 += ADD_mem[0]
	S += 9<T8T1_mem0
	S += T8T1_mem0<=T8T1

	T8T1_mem1 = S.Task('T8T1_mem1', length=1, delay_cost=1)
	T8T1_mem1 += ADD_mem[0]
	S += 36<T8T1_mem1
	S += T8T1_mem1<=T8T1

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	T8T2 += alt(ADD)

	T8T2_mem0 = S.Task('T8T2_mem0', length=1, delay_cost=1)
	T8T2_mem0 += ADD_mem[0]
	S += 13<T8T2_mem0
	S += T8T2_mem0<=T8T2

	T8T2_mem1 = S.Task('T8T2_mem1', length=1, delay_cost=1)
	T8T2_mem1 += ADD_mem[0]
	S += 9<T8T2_mem1
	S += T8T2_mem1<=T8T2

	T8T3 = S.Task('T8T3', length=1, delay_cost=1)
	T8T3 += alt(ADD)

	T8T3_mem0 = S.Task('T8T3_mem0', length=1, delay_cost=1)
	T8T3_mem0 += ADD_mem[0]
	S += 8<T8T3_mem0
	S += T8T3_mem0<=T8T3

	T8T3_mem1 = S.Task('T8T3_mem1', length=1, delay_cost=1)
	T8T3_mem1 += ADD_mem[0]
	S += 36<T8T3_mem1
	S += T8T3_mem1<=T8T3

	T100 = S.Task('T100', length=1, delay_cost=1)
	T100 += alt(ADD)

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	T100_mem0 += ADD_mem[0]
	S += 17<T100_mem0
	S += T100_mem0<=T100

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	T100_mem1 += ADD_mem[3]
	S += 10<T100_mem1
	S += T100_mem1<=T100

	T101 = S.Task('T101', length=1, delay_cost=1)
	T101 += alt(ADD)

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	T101_mem0 += ADD_mem[1]
	S += 23<T101_mem0
	S += T101_mem0<=T101

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	T101_mem1 += ADD_mem[1]
	S += 7<T101_mem1
	S += T101_mem1<=T101

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	T1_0 += alt(ADD)

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	T1_0_mem0 += ADD_mem[0]
	S += 26<T1_0_mem0
	S += T1_0_mem0<=T1_0

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	T1_0_mem1 += ADD_mem[0]
	S += 13<T1_0_mem1
	S += T1_0_mem1<=T1_0

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	T1_1 += alt(ADD)

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	T1_1_mem0 += ADD_mem[1]
	S += 25<T1_1_mem0
	S += T1_1_mem0<=T1_1

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	T1_1_mem1 += ADD_mem[0]
	S += 9<T1_1_mem1
	S += T1_1_mem1<=T1_1

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	T4_0 += alt(ADD)

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	T4_0_mem0 += ADD_mem[3]
	S += 10<T4_0_mem0
	S += T4_0_mem0<=T4_0

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	T4_0_mem1 += ADD_mem[0]
	S += 8<T4_0_mem1
	S += T4_0_mem1<=T4_0

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	T4_1 += alt(ADD)

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	T4_1_mem0 += ADD_mem[1]
	S += 7<T4_1_mem0
	S += T4_1_mem0<=T4_1

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	T4_1_mem1 += ADD_mem[0]
	S += 36<T4_1_mem1
	S += T4_1_mem1<=T4_1

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	T5_0 += alt(ADD)

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	T5_0_mem0 += ADD_mem[0]
	S += 17<T5_0_mem0
	S += T5_0_mem0<=T5_0

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	T5_0_mem1 += ADD_mem[0]
	S += 8<T5_0_mem1
	S += T5_0_mem1<=T5_0

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	T5_1 += alt(ADD)

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	T5_1_mem0 += ADD_mem[1]
	S += 23<T5_1_mem0
	S += T5_1_mem0<=T5_1

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	T5_1_mem1 += ADD_mem[0]
	S += 36<T5_1_mem1
	S += T5_1_mem1<=T5_1

	T6_T4_in = S.Task('T6_T4_in', length=1, delay_cost=1)
	T6_T4_in += alt(MUL_in)
	T6_T4 = S.Task('T6_T4', length=7, delay_cost=1)
	T6_T4 += alt(MUL)
	S+=T6_T4>=T6_T4_in

	T6_T4_mem0 = S.Task('T6_T4_mem0', length=1, delay_cost=1)
	T6_T4_mem0 += ADD_mem[2]
	S += 35<T6_T4_mem0
	S += T6_T4_mem0<=T6_T4

	T6_T4_mem1 = S.Task('T6_T4_mem1', length=1, delay_cost=1)
	T6_T4_mem1 += ADD_mem[0]
	S += 34<T6_T4_mem1
	S += T6_T4_mem1<=T6_T4

	T6_T5 = S.Task('T6_T5', length=1, delay_cost=1)
	T6_T5 += alt(ADD)

	T6_T5_mem0 = S.Task('T6_T5_mem0', length=1, delay_cost=1)
	T6_T5_mem0 += MUL_mem[0]
	S += 12<T6_T5_mem0
	S += T6_T5_mem0<=T6_T5

	T6_T5_mem1 = S.Task('T6_T5_mem1', length=1, delay_cost=1)
	T6_T5_mem1 += MUL_mem[0]
	S += 11<T6_T5_mem1
	S += T6_T5_mem1<=T6_T5

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	T6_0 += alt(ADD)

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	T6_0_mem0 += MUL_mem[0]
	S += 12<T6_0_mem0
	S += T6_0_mem0<=T6_0

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	T6_0_mem1 += MUL_mem[0]
	S += 11<T6_0_mem1
	S += T6_0_mem1<=T6_0

	T7_T4_in = S.Task('T7_T4_in', length=1, delay_cost=1)
	T7_T4_in += alt(MUL_in)
	T7_T4 = S.Task('T7_T4', length=7, delay_cost=1)
	T7_T4 += alt(MUL)
	S+=T7_T4>=T7_T4_in

	T7_T4_mem0 = S.Task('T7_T4_mem0', length=1, delay_cost=1)
	T7_T4_mem0 += ADD_mem[1]
	S += 32<T7_T4_mem0
	S += T7_T4_mem0<=T7_T4

	T7_T4_mem1 = S.Task('T7_T4_mem1', length=1, delay_cost=1)
	T7_T4_mem1 += ADD_mem[3]
	S += 31<T7_T4_mem1
	S += T7_T4_mem1<=T7_T4

	T7_T5 = S.Task('T7_T5', length=1, delay_cost=1)
	T7_T5 += alt(ADD)

	T7_T5_mem0 = S.Task('T7_T5_mem0', length=1, delay_cost=1)
	T7_T5_mem0 += MUL_mem[0]
	S += 10<T7_T5_mem0
	S += T7_T5_mem0<=T7_T5

	T7_T5_mem1 = S.Task('T7_T5_mem1', length=1, delay_cost=1)
	T7_T5_mem1 += MUL_mem[0]
	S += 8<T7_T5_mem1
	S += T7_T5_mem1<=T7_T5

	T7_0 = S.Task('T7_0', length=1, delay_cost=1)
	T7_0 += alt(ADD)

	T7_0_mem0 = S.Task('T7_0_mem0', length=1, delay_cost=1)
	T7_0_mem0 += MUL_mem[0]
	S += 10<T7_0_mem0
	S += T7_0_mem0<=T7_0

	T7_0_mem1 = S.Task('T7_0_mem1', length=1, delay_cost=1)
	T7_0_mem1 += MUL_mem[0]
	S += 8<T7_0_mem1
	S += T7_0_mem1<=T7_0

	T8_1T4_in = S.Task('T8_1T4_in', length=1, delay_cost=1)
	T8_1T4_in += alt(MUL_in)
	T8_1T4 = S.Task('T8_1T4', length=7, delay_cost=1)
	T8_1T4 += alt(MUL)
	S+=T8_1T4>=T8_1T4_in

	T8_1T4_mem0 = S.Task('T8_1T4_mem0', length=1, delay_cost=1)
	T8_1T4_mem0 += ADD_mem[1]
	S += 28<T8_1T4_mem0
	S += T8_1T4_mem0<=T8_1T4

	T8_1T4_mem1 = S.Task('T8_1T4_mem1', length=1, delay_cost=1)
	T8_1T4_mem1 += ADD_mem[2]
	S += 21<T8_1T4_mem1
	S += T8_1T4_mem1<=T8_1T4

	T8_1T5 = S.Task('T8_1T5', length=1, delay_cost=1)
	T8_1T5 += alt(ADD)

	T8_1T5_mem0 = S.Task('T8_1T5_mem0', length=1, delay_cost=1)
	T8_1T5_mem0 += MUL_mem[0]
	S += 7<T8_1T5_mem0
	S += T8_1T5_mem0<=T8_1T5

	T8_1T5_mem1 = S.Task('T8_1T5_mem1', length=1, delay_cost=1)
	T8_1T5_mem1 += MUL_mem[0]
	S += 9<T8_1T5_mem1
	S += T8_1T5_mem1<=T8_1T5

	T8_10 = S.Task('T8_10', length=1, delay_cost=1)
	T8_10 += alt(ADD)

	T8_10_mem0 = S.Task('T8_10_mem0', length=1, delay_cost=1)
	T8_10_mem0 += MUL_mem[0]
	S += 7<T8_10_mem0
	S += T8_10_mem0<=T8_10

	T8_10_mem1 = S.Task('T8_10_mem1', length=1, delay_cost=1)
	T8_10_mem1 += MUL_mem[0]
	S += 9<T8_10_mem1
	S += T8_10_mem1<=T8_10

	T9_4T0_in = S.Task('T9_4T0_in', length=1, delay_cost=1)
	T9_4T0_in += alt(MUL_in)
	T9_4T0 = S.Task('T9_4T0', length=7, delay_cost=1)
	T9_4T0 += alt(MUL)
	S+=T9_4T0>=T9_4T0_in

	T9_4T0_mem0 = S.Task('T9_4T0_mem0', length=1, delay_cost=1)
	T9_4T0_mem0 += ADD_mem[2]
	S += 27<T9_4T0_mem0
	S += T9_4T0_mem0<=T9_4T0

	T9_4T0_mem1 = S.Task('T9_4T0_mem1', length=1, delay_cost=1)
	T9_4T0_mem1 += ADD_mem[0]
	S += 14<T9_4T0_mem1
	S += T9_4T0_mem1<=T9_4T0

	T9_4T1_in = S.Task('T9_4T1_in', length=1, delay_cost=1)
	T9_4T1_in += alt(MUL_in)
	T9_4T1 = S.Task('T9_4T1', length=7, delay_cost=1)
	T9_4T1 += alt(MUL)
	S+=T9_4T1>=T9_4T1_in

	T9_4T1_mem0 = S.Task('T9_4T1_mem0', length=1, delay_cost=1)
	T9_4T1_mem0 += ADD_mem[0]
	S += 20<T9_4T1_mem0
	S += T9_4T1_mem0<=T9_4T1

	T9_4T1_mem1 = S.Task('T9_4T1_mem1', length=1, delay_cost=1)
	T9_4T1_mem1 += ADD_mem[3]
	S += 16<T9_4T1_mem1
	S += T9_4T1_mem1<=T9_4T1

	T9_4T2 = S.Task('T9_4T2', length=1, delay_cost=1)
	T9_4T2 += alt(ADD)

	T9_4T2_mem0 = S.Task('T9_4T2_mem0', length=1, delay_cost=1)
	T9_4T2_mem0 += ADD_mem[2]
	S += 27<T9_4T2_mem0
	S += T9_4T2_mem0<=T9_4T2

	T9_4T2_mem1 = S.Task('T9_4T2_mem1', length=1, delay_cost=1)
	T9_4T2_mem1 += ADD_mem[0]
	S += 20<T9_4T2_mem1
	S += T9_4T2_mem1<=T9_4T2

	T9_4T3 = S.Task('T9_4T3', length=1, delay_cost=1)
	T9_4T3 += alt(ADD)

	T9_4T3_mem0 = S.Task('T9_4T3_mem0', length=1, delay_cost=1)
	T9_4T3_mem0 += ADD_mem[0]
	S += 14<T9_4T3_mem0
	S += T9_4T3_mem0<=T9_4T3

	T9_4T3_mem1 = S.Task('T9_4T3_mem1', length=1, delay_cost=1)
	T9_4T3_mem1 += ADD_mem[3]
	S += 16<T9_4T3_mem1
	S += T9_4T3_mem1<=T9_4T3

	T3_1T0_in = S.Task('T3_1T0_in', length=1, delay_cost=1)
	T3_1T0_in += alt(MUL_in)
	T3_1T0 = S.Task('T3_1T0', length=7, delay_cost=1)
	T3_1T0 += alt(MUL)
	S+=T3_1T0>=T3_1T0_in

	T3_1T0_mem0 = S.Task('T3_1T0_mem0', length=1, delay_cost=1)
	T3_1T0_mem0 += ADD_mem[0]
	S += 19<T3_1T0_mem0
	S += T3_1T0_mem0<=T3_1T0

	T3_1T0_mem1 = S.Task('T3_1T0_mem1', length=1, delay_cost=1)
	T3_1T0_mem1 += ADD_mem[0]
	S += 11<T3_1T0_mem1
	S += T3_1T0_mem1<=T3_1T0

	T3_1T1_in = S.Task('T3_1T1_in', length=1, delay_cost=1)
	T3_1T1_in += alt(MUL_in)
	T3_1T1 = S.Task('T3_1T1', length=7, delay_cost=1)
	T3_1T1 += alt(MUL)
	S+=T3_1T1>=T3_1T1_in

	T3_1T1_mem0 = S.Task('T3_1T1_mem0', length=1, delay_cost=1)
	T3_1T1_mem0 += ADD_mem[0]
	S += 22<T3_1T1_mem0
	S += T3_1T1_mem0<=T3_1T1

	T3_1T1_mem1 = S.Task('T3_1T1_mem1', length=1, delay_cost=1)
	T3_1T1_mem1 += ADD_mem[1]
	S += 12<T3_1T1_mem1
	S += T3_1T1_mem1<=T3_1T1

	T3_1T2 = S.Task('T3_1T2', length=1, delay_cost=1)
	T3_1T2 += alt(ADD)

	T3_1T2_mem0 = S.Task('T3_1T2_mem0', length=1, delay_cost=1)
	T3_1T2_mem0 += ADD_mem[0]
	S += 19<T3_1T2_mem0
	S += T3_1T2_mem0<=T3_1T2

	T3_1T2_mem1 = S.Task('T3_1T2_mem1', length=1, delay_cost=1)
	T3_1T2_mem1 += ADD_mem[0]
	S += 22<T3_1T2_mem1
	S += T3_1T2_mem1<=T3_1T2

	T3_1T3 = S.Task('T3_1T3', length=1, delay_cost=1)
	T3_1T3 += alt(ADD)

	T3_1T3_mem0 = S.Task('T3_1T3_mem0', length=1, delay_cost=1)
	T3_1T3_mem0 += ADD_mem[0]
	S += 11<T3_1T3_mem0
	S += T3_1T3_mem0<=T3_1T3

	T3_1T3_mem1 = S.Task('T3_1T3_mem1', length=1, delay_cost=1)
	T3_1T3_mem1 += ADD_mem[1]
	S += 12<T3_1T3_mem1
	S += T3_1T3_mem1<=T3_1T3

	T4_3T0_in = S.Task('T4_3T0_in', length=1, delay_cost=1)
	T4_3T0_in += alt(MUL_in)
	T4_3T0 = S.Task('T4_3T0', length=7, delay_cost=1)
	T4_3T0 += alt(MUL)
	S+=T4_3T0>=T4_3T0_in

	T4_3T0_mem0 = S.Task('T4_3T0_mem0', length=1, delay_cost=1)
	T4_3T0_mem0 += ADD_mem[0]
	S += 29<T4_3T0_mem0
	S += T4_3T0_mem0<=T4_3T0

	T4_3T0_mem1 = S.Task('T4_3T0_mem1', length=1, delay_cost=1)
	T4_3T0_mem1 += ADD_mem[1]
	S += 24<T4_3T0_mem1
	S += T4_3T0_mem1<=T4_3T0

	T4_3T1_in = S.Task('T4_3T1_in', length=1, delay_cost=1)
	T4_3T1_in += alt(MUL_in)
	T4_3T1 = S.Task('T4_3T1', length=7, delay_cost=1)
	T4_3T1 += alt(MUL)
	S+=T4_3T1>=T4_3T1_in

	T4_3T1_mem0 = S.Task('T4_3T1_mem0', length=1, delay_cost=1)
	T4_3T1_mem0 += ADD_mem[0]
	S += 30<T4_3T1_mem0
	S += T4_3T1_mem0<=T4_3T1

	T4_3T1_mem1 = S.Task('T4_3T1_mem1', length=1, delay_cost=1)
	T4_3T1_mem1 += ADD_mem[2]
	S += 15<T4_3T1_mem1
	S += T4_3T1_mem1<=T4_3T1

	T4_3T2 = S.Task('T4_3T2', length=1, delay_cost=1)
	T4_3T2 += alt(ADD)

	T4_3T2_mem0 = S.Task('T4_3T2_mem0', length=1, delay_cost=1)
	T4_3T2_mem0 += ADD_mem[0]
	S += 29<T4_3T2_mem0
	S += T4_3T2_mem0<=T4_3T2

	T4_3T2_mem1 = S.Task('T4_3T2_mem1', length=1, delay_cost=1)
	T4_3T2_mem1 += ADD_mem[0]
	S += 30<T4_3T2_mem1
	S += T4_3T2_mem1<=T4_3T2

	T4_3T3 = S.Task('T4_3T3', length=1, delay_cost=1)
	T4_3T3 += alt(ADD)

	T4_3T3_mem0 = S.Task('T4_3T3_mem0', length=1, delay_cost=1)
	T4_3T3_mem0 += ADD_mem[1]
	S += 24<T4_3T3_mem0
	S += T4_3T3_mem0<=T4_3T3

	T4_3T3_mem1 = S.Task('T4_3T3_mem1', length=1, delay_cost=1)
	T4_3T3_mem1 += ADD_mem[2]
	S += 15<T4_3T3_mem1
	S += T4_3T3_mem1<=T4_3T3

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "square_mul1_add4/square_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_square_mul1_add4_1(0, 0)