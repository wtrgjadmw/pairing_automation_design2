from pyschedule import Scenario, solvers, plotters, alt

def solve_inv_mul1_add4_3(ConstStep, ExpStep):
	horizon = 138
	S=Scenario("inv_mul1_add4_3",horizon = horizon)

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
	T2_1T2_in = S.Task('T2_1T2_in', length=1, delay_cost=1)
	S += T2_1T2_in >= 0
	T2_1T2_in += MUL_in[0]

	T2_1T2_mem0 = S.Task('T2_1T2_mem0', length=1, delay_cost=1)
	S += T2_1T2_mem0 >= 0
	T2_1T2_mem0 += INPUT_mem_r

	T2_1T2_mem1 = S.Task('T2_1T2_mem1', length=1, delay_cost=1)
	S += T2_1T2_mem1 >= 0
	T2_1T2_mem1 += INPUT_mem_r

	T2T2_in = S.Task('T2T2_in', length=1, delay_cost=1)
	S += T2T2_in >= 1
	T2T2_in += MUL_in[0]

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	S += T2T2_mem0 >= 1
	T2T2_mem0 += INPUT_mem_r

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	S += T2T2_mem1 >= 1
	T2T2_mem1 += INPUT_mem_r

	T2_1T2 = S.Task('T2_1T2', length=7, delay_cost=1)
	S += T2_1T2 >= 1
	T2_1T2 += MUL[0]

	T1T2_in = S.Task('T1T2_in', length=1, delay_cost=1)
	S += T1T2_in >= 2
	T1T2_in += MUL_in[0]

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	S += T1T2_mem0 >= 2
	T1T2_mem0 += INPUT_mem_r

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	S += T1T2_mem1 >= 2
	T1T2_mem1 += INPUT_mem_r

	T2T2 = S.Task('T2T2', length=7, delay_cost=1)
	S += T2T2 >= 2
	T2T2 += MUL[0]

	T1T2 = S.Task('T1T2', length=7, delay_cost=1)
	S += T1T2 >= 3
	T1T2 += MUL[0]

	T1_T2_in = S.Task('T1_T2_in', length=1, delay_cost=1)
	S += T1_T2_in >= 3
	T1_T2_in += MUL_in[0]

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	S += T1_T2_mem0 >= 3
	T1_T2_mem0 += INPUT_mem_r

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	S += T1_T2_mem1 >= 3
	T1_T2_mem1 += INPUT_mem_r

	T0_T2_in = S.Task('T0_T2_in', length=1, delay_cost=1)
	S += T0_T2_in >= 4
	T0_T2_in += MUL_in[0]

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	S += T0_T2_mem0 >= 4
	T0_T2_mem0 += INPUT_mem_r

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	S += T0_T2_mem1 >= 4
	T0_T2_mem1 += INPUT_mem_r

	T1_T2 = S.Task('T1_T2', length=7, delay_cost=1)
	S += T1_T2 >= 4
	T1_T2 += MUL[0]

	T0T2_in = S.Task('T0T2_in', length=1, delay_cost=1)
	S += T0T2_in >= 5
	T0T2_in += MUL_in[0]

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	S += T0T2_mem0 >= 5
	T0T2_mem0 += INPUT_mem_r

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	S += T0T2_mem1 >= 5
	T0T2_mem1 += INPUT_mem_r

	T0_T2 = S.Task('T0_T2', length=7, delay_cost=1)
	S += T0_T2 >= 5
	T0_T2 += MUL[0]

	T0T2 = S.Task('T0T2', length=7, delay_cost=1)
	S += T0T2 >= 6
	T0T2 += MUL[0]

	T2_8T2_mem0 = S.Task('T2_8T2_mem0', length=1, delay_cost=1)
	S += T2_8T2_mem0 >= 6
	T2_8T2_mem0 += INPUT_mem_r

	T2_8T2_mem1 = S.Task('T2_8T2_mem1', length=1, delay_cost=1)
	S += T2_8T2_mem1 >= 6
	T2_8T2_mem1 += INPUT_mem_r

	NEW_A011_mem0 = S.Task('NEW_A011_mem0', length=1, delay_cost=1)
	S += NEW_A011_mem0 >= 7
	NEW_A011_mem0 += INPUT_mem_r

	NEW_A011_mem1 = S.Task('NEW_A011_mem1', length=1, delay_cost=1)
	S += NEW_A011_mem1 >= 7
	NEW_A011_mem1 += INPUT_mem_r

	T2_11_mem0 = S.Task('T2_11_mem0', length=1, delay_cost=1)
	S += T2_11_mem0 >= 7
	T2_11_mem0 += MUL_mem[0]

	T2_8T2 = S.Task('T2_8T2', length=1, delay_cost=1)
	S += T2_8T2 >= 7
	T2_8T2 += ADD[0]

	NEW_A011 = S.Task('NEW_A011', length=1, delay_cost=1)
	S += NEW_A011 >= 8
	NEW_A011 += ADD[0]

	T1_4T2_mem0 = S.Task('T1_4T2_mem0', length=1, delay_cost=1)
	S += T1_4T2_mem0 >= 8
	T1_4T2_mem0 += INPUT_mem_r

	T1_4T2_mem1 = S.Task('T1_4T2_mem1', length=1, delay_cost=1)
	S += T1_4T2_mem1 >= 8
	T1_4T2_mem1 += INPUT_mem_r

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 8
	T21_mem0 += MUL_mem[0]

	T2_11 = S.Task('T2_11', length=1, delay_cost=1)
	S += T2_11 >= 8
	T2_11 += ADD[3]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 9
	T11_mem0 += MUL_mem[0]

	T1_3T2_mem0 = S.Task('T1_3T2_mem0', length=1, delay_cost=1)
	S += T1_3T2_mem0 >= 9
	T1_3T2_mem0 += INPUT_mem_r

	T1_3T2_mem1 = S.Task('T1_3T2_mem1', length=1, delay_cost=1)
	S += T1_3T2_mem1 >= 9
	T1_3T2_mem1 += INPUT_mem_r

	T1_4T2 = S.Task('T1_4T2', length=1, delay_cost=1)
	S += T1_4T2 >= 9
	T1_4T2 += ADD[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 9
	T21 += ADD[1]

	NEW_A121_mem0 = S.Task('NEW_A121_mem0', length=1, delay_cost=1)
	S += NEW_A121_mem0 >= 10
	NEW_A121_mem0 += INPUT_mem_r

	NEW_A121_mem1 = S.Task('NEW_A121_mem1', length=1, delay_cost=1)
	S += NEW_A121_mem1 >= 10
	NEW_A121_mem1 += INPUT_mem_r

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 10
	T11 += ADD[0]

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	S += T1_1_mem0 >= 10
	T1_1_mem0 += MUL_mem[0]

	T1_3T2 = S.Task('T1_3T2', length=1, delay_cost=1)
	S += T1_3T2 >= 10
	T1_3T2 += ADD[2]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 10
	T51_mem0 += ADD_mem[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 10
	T51_mem1 += ADD_mem[1]

	NEW_A010_mem0 = S.Task('NEW_A010_mem0', length=1, delay_cost=1)
	S += NEW_A010_mem0 >= 11
	NEW_A010_mem0 += INPUT_mem_r

	NEW_A010_mem1 = S.Task('NEW_A010_mem1', length=1, delay_cost=1)
	S += NEW_A010_mem1 >= 11
	NEW_A010_mem1 += INPUT_mem_r

	NEW_A121 = S.Task('NEW_A121', length=1, delay_cost=1)
	S += NEW_A121 >= 11
	NEW_A121 += ADD[1]

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	S += T0_1_mem0 >= 11
	T0_1_mem0 += MUL_mem[0]

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	S += T1_1 >= 11
	T1_1 += ADD[0]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 11
	T51 += ADD[2]

	T5_21_mem0 = S.Task('T5_21_mem0', length=1, delay_cost=1)
	S += T5_21_mem0 >= 11
	T5_21_mem0 += ADD_mem[0]

	T5_21_mem1 = S.Task('T5_21_mem1', length=1, delay_cost=1)
	S += T5_21_mem1 >= 11
	T5_21_mem1 += ADD_mem[3]

	NEW_A000_mem0 = S.Task('NEW_A000_mem0', length=1, delay_cost=1)
	S += NEW_A000_mem0 >= 12
	NEW_A000_mem0 += INPUT_mem_r

	NEW_A000_mem1 = S.Task('NEW_A000_mem1', length=1, delay_cost=1)
	S += NEW_A000_mem1 >= 12
	NEW_A000_mem1 += INPUT_mem_r

	NEW_A010 = S.Task('NEW_A010', length=1, delay_cost=1)
	S += NEW_A010 >= 12
	NEW_A010 += ADD[0]

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	S += T01_mem0 >= 12
	T01_mem0 += MUL_mem[0]

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	S += T0_1 >= 12
	T0_1 += ADD[1]

	T4_T2_in = S.Task('T4_T2_in', length=1, delay_cost=1)
	S += T4_T2_in >= 12
	T4_T2_in += MUL_in[0]

	T4_T2_mem0 = S.Task('T4_T2_mem0', length=1, delay_cost=1)
	S += T4_T2_mem0 >= 12
	T4_T2_mem0 += ADD_mem[0]

	T4_T2_mem1 = S.Task('T4_T2_mem1', length=1, delay_cost=1)
	S += T4_T2_mem1 >= 12
	T4_T2_mem1 += ADD_mem[0]

	T5_21 = S.Task('T5_21', length=1, delay_cost=1)
	S += T5_21 >= 12
	T5_21 += ADD[2]

	T6_1_mem0 = S.Task('T6_1_mem0', length=1, delay_cost=1)
	S += T6_1_mem0 >= 12
	T6_1_mem0 += ADD_mem[3]

	T6_1_mem1 = S.Task('T6_1_mem1', length=1, delay_cost=1)
	S += T6_1_mem1 >= 12
	T6_1_mem1 += ADD_mem[1]

	NEW_A000 = S.Task('NEW_A000', length=1, delay_cost=1)
	S += NEW_A000 >= 13
	NEW_A000 += ADD[0]

	T01 = S.Task('T01', length=1, delay_cost=1)
	S += T01 >= 13
	T01 += ADD[3]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 13
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 13
	T2T0_mem1 += INPUT_mem_r

	T4_T1_mem0 = S.Task('T4_T1_mem0', length=1, delay_cost=1)
	S += T4_T1_mem0 >= 13
	T4_T1_mem0 += ADD_mem[0]

	T4_T1_mem1 = S.Task('T4_T1_mem1', length=1, delay_cost=1)
	S += T4_T1_mem1 >= 13
	T4_T1_mem1 += ADD_mem[0]

	T4_T2 = S.Task('T4_T2', length=7, delay_cost=1)
	S += T4_T2 >= 13
	T4_T2 += MUL[0]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 13
	T61_mem0 += ADD_mem[1]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 13
	T61_mem1 += ADD_mem[3]

	T6_1 = S.Task('T6_1', length=1, delay_cost=1)
	S += T6_1 >= 13
	T6_1 += ADD[1]

	NEW_A111_mem0 = S.Task('NEW_A111_mem0', length=1, delay_cost=1)
	S += NEW_A111_mem0 >= 14
	NEW_A111_mem0 += INPUT_mem_r

	NEW_A111_mem1 = S.Task('NEW_A111_mem1', length=1, delay_cost=1)
	S += NEW_A111_mem1 >= 14
	NEW_A111_mem1 += INPUT_mem_r

	T2T0 = S.Task('T2T0', length=1, delay_cost=1)
	S += T2T0 >= 14
	T2T0 += ADD[0]

	T4_15T2_mem0 = S.Task('T4_15T2_mem0', length=1, delay_cost=1)
	S += T4_15T2_mem0 >= 14
	T4_15T2_mem0 += ADD_mem[0]

	T4_15T2_mem1 = S.Task('T4_15T2_mem1', length=1, delay_cost=1)
	S += T4_15T2_mem1 >= 14
	T4_15T2_mem1 += ADD_mem[0]

	T4_T1 = S.Task('T4_T1', length=1, delay_cost=1)
	S += T4_T1 >= 14
	T4_T1 += ADD[1]

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 14
	T61 += ADD[3]

	NEW_A110_mem0 = S.Task('NEW_A110_mem0', length=1, delay_cost=1)
	S += NEW_A110_mem0 >= 15
	NEW_A110_mem0 += INPUT_mem_r

	NEW_A110_mem1 = S.Task('NEW_A110_mem1', length=1, delay_cost=1)
	S += NEW_A110_mem1 >= 15
	NEW_A110_mem1 += INPUT_mem_r

	NEW_A111 = S.Task('NEW_A111', length=1, delay_cost=1)
	S += NEW_A111 >= 15
	NEW_A111 += ADD[2]

	T4_15T2 = S.Task('T4_15T2', length=1, delay_cost=1)
	S += T4_15T2 >= 15
	T4_15T2 += ADD[3]

	T4_T0_mem0 = S.Task('T4_T0_mem0', length=1, delay_cost=1)
	S += T4_T0_mem0 >= 15
	T4_T0_mem0 += ADD_mem[0]

	T4_T0_mem1 = S.Task('T4_T0_mem1', length=1, delay_cost=1)
	S += T4_T0_mem1 >= 15
	T4_T0_mem1 += ADD_mem[0]

	NEW_A110 = S.Task('NEW_A110', length=1, delay_cost=1)
	S += NEW_A110 >= 16
	NEW_A110 += ADD[1]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 16
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 16
	T0T0_mem1 += INPUT_mem_r

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 16
	T41_mem0 += ADD_mem[3]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 16
	T41_mem1 += ADD_mem[0]

	T4_4T0_mem0 = S.Task('T4_4T0_mem0', length=1, delay_cost=1)
	S += T4_4T0_mem0 >= 16
	T4_4T0_mem0 += ADD_mem[1]

	T4_4T0_mem1 = S.Task('T4_4T0_mem1', length=1, delay_cost=1)
	S += T4_4T0_mem1 >= 16
	T4_4T0_mem1 += ADD_mem[2]

	T4_4T2_in = S.Task('T4_4T2_in', length=1, delay_cost=1)
	S += T4_4T2_in >= 16
	T4_4T2_in += MUL_in[0]

	T4_4T2_mem0 = S.Task('T4_4T2_mem0', length=1, delay_cost=1)
	S += T4_4T2_mem0 >= 16
	T4_4T2_mem0 += ADD_mem[1]

	T4_4T2_mem1 = S.Task('T4_4T2_mem1', length=1, delay_cost=1)
	S += T4_4T2_mem1 >= 16
	T4_4T2_mem1 += ADD_mem[2]

	T4_T0 = S.Task('T4_T0', length=1, delay_cost=1)
	S += T4_T0 >= 16
	T4_T0 += ADD[0]

	NEW_A101_mem0 = S.Task('NEW_A101_mem0', length=1, delay_cost=1)
	S += NEW_A101_mem0 >= 17
	NEW_A101_mem0 += INPUT_mem_r

	NEW_A101_mem1 = S.Task('NEW_A101_mem1', length=1, delay_cost=1)
	S += NEW_A101_mem1 >= 17
	NEW_A101_mem1 += INPUT_mem_r

	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	S += T0T0 >= 17
	T0T0 += ADD[1]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 17
	T41 += ADD[2]

	T4_19T2_mem0 = S.Task('T4_19T2_mem0', length=1, delay_cost=1)
	S += T4_19T2_mem0 >= 17
	T4_19T2_mem0 += ADD_mem[1]

	T4_19T2_mem1 = S.Task('T4_19T2_mem1', length=1, delay_cost=1)
	S += T4_19T2_mem1 >= 17
	T4_19T2_mem1 += ADD_mem[2]

	T4_4T0 = S.Task('T4_4T0', length=1, delay_cost=1)
	S += T4_4T0 >= 17
	T4_4T0 += ADD[0]

	T4_4T1_mem0 = S.Task('T4_4T1_mem0', length=1, delay_cost=1)
	S += T4_4T1_mem0 >= 17
	T4_4T1_mem0 += ADD_mem[1]

	T4_4T1_mem1 = S.Task('T4_4T1_mem1', length=1, delay_cost=1)
	S += T4_4T1_mem1 >= 17
	T4_4T1_mem1 += ADD_mem[2]

	T4_4T2 = S.Task('T4_4T2', length=7, delay_cost=1)
	S += T4_4T2 >= 17
	T4_4T2 += MUL[0]

	NEW_A101 = S.Task('NEW_A101', length=1, delay_cost=1)
	S += NEW_A101 >= 18
	NEW_A101 += ADD[0]

	T0_3T2_mem0 = S.Task('T0_3T2_mem0', length=1, delay_cost=1)
	S += T0_3T2_mem0 >= 18
	T0_3T2_mem0 += INPUT_mem_r

	T0_3T2_mem1 = S.Task('T0_3T2_mem1', length=1, delay_cost=1)
	S += T0_3T2_mem1 >= 18
	T0_3T2_mem1 += INPUT_mem_r

	T4_0_in = S.Task('T4_0_in', length=1, delay_cost=1)
	S += T4_0_in >= 18
	T4_0_in += MUL_in[0]

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	S += T4_0_mem0 >= 18
	T4_0_mem0 += ADD_mem[0]

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	S += T4_0_mem1 >= 18
	T4_0_mem1 += ADD_mem[1]

	T4_19T2 = S.Task('T4_19T2', length=1, delay_cost=1)
	S += T4_19T2 >= 18
	T4_19T2 += ADD[1]

	T4_31_mem0 = S.Task('T4_31_mem0', length=1, delay_cost=1)
	S += T4_31_mem0 >= 18
	T4_31_mem0 += ADD_mem[1]

	T4_31_mem1 = S.Task('T4_31_mem1', length=1, delay_cost=1)
	S += T4_31_mem1 >= 18
	T4_31_mem1 += ADD_mem[0]

	T4_4T1 = S.Task('T4_4T1', length=1, delay_cost=1)
	S += T4_4T1 >= 18
	T4_4T1 += ADD[3]

	T0_3T2 = S.Task('T0_3T2', length=1, delay_cost=1)
	S += T0_3T2 >= 19
	T0_3T2 += ADD[0]

	T0_4T2_mem0 = S.Task('T0_4T2_mem0', length=1, delay_cost=1)
	S += T0_4T2_mem0 >= 19
	T0_4T2_mem0 += INPUT_mem_r

	T0_4T2_mem1 = S.Task('T0_4T2_mem1', length=1, delay_cost=1)
	S += T0_4T2_mem1 >= 19
	T0_4T2_mem1 += INPUT_mem_r

	T4_0 = S.Task('T4_0', length=7, delay_cost=1)
	S += T4_0 >= 19
	T4_0 += MUL[0]

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	S += T4_1_mem0 >= 19
	T4_1_mem0 += MUL_mem[0]

	T4_31 = S.Task('T4_31', length=1, delay_cost=1)
	S += T4_31 >= 19
	T4_31 += ADD[3]

	T4_40_in = S.Task('T4_40_in', length=1, delay_cost=1)
	S += T4_40_in >= 19
	T4_40_in += MUL_in[0]

	T4_40_mem0 = S.Task('T4_40_mem0', length=1, delay_cost=1)
	S += T4_40_mem0 >= 19
	T4_40_mem0 += ADD_mem[0]

	T4_40_mem1 = S.Task('T4_40_mem1', length=1, delay_cost=1)
	S += T4_40_mem1 >= 19
	T4_40_mem1 += ADD_mem[3]

	T0_4T2 = S.Task('T0_4T2', length=1, delay_cost=1)
	S += T0_4T2 >= 20
	T0_4T2 += ADD[0]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 20
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 20
	T1T1_mem1 += INPUT_mem_r

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	S += T4_1 >= 20
	T4_1 += ADD[2]

	T4_11_mem0 = S.Task('T4_11_mem0', length=1, delay_cost=1)
	S += T4_11_mem0 >= 20
	T4_11_mem0 += ADD_mem[2]

	T4_11_mem1 = S.Task('T4_11_mem1', length=1, delay_cost=1)
	S += T4_11_mem1 >= 20
	T4_11_mem1 += ADD_mem[2]

	T4_40 = S.Task('T4_40', length=7, delay_cost=1)
	S += T4_40 >= 20
	T4_40 += MUL[0]

	NEW_A100_mem0 = S.Task('NEW_A100_mem0', length=1, delay_cost=1)
	S += NEW_A100_mem0 >= 21
	NEW_A100_mem0 += INPUT_mem_r

	NEW_A100_mem1 = S.Task('NEW_A100_mem1', length=1, delay_cost=1)
	S += NEW_A100_mem1 >= 21
	NEW_A100_mem1 += INPUT_mem_r

	T1T1 = S.Task('T1T1', length=1, delay_cost=1)
	S += T1T1 >= 21
	T1T1 += ADD[0]

	T4_11 = S.Task('T4_11', length=1, delay_cost=1)
	S += T4_11 >= 21
	T4_11 += ADD[1]

	NEW_A100 = S.Task('NEW_A100', length=1, delay_cost=1)
	S += NEW_A100 >= 22
	NEW_A100 += ADD[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 22
	T2T1_mem0 += INPUT_mem_r

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 22
	T2T1_mem1 += INPUT_mem_r

	T3_1T2_in = S.Task('T3_1T2_in', length=1, delay_cost=1)
	S += T3_1T2_in >= 22
	T3_1T2_in += MUL_in[0]

	T3_1T2_mem0 = S.Task('T3_1T2_mem0', length=1, delay_cost=1)
	S += T3_1T2_mem0 >= 22
	T3_1T2_mem0 += ADD_mem[0]

	T3_1T2_mem1 = S.Task('T3_1T2_mem1', length=1, delay_cost=1)
	S += T3_1T2_mem1 >= 22
	T3_1T2_mem1 += ADD_mem[0]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 23
	T20_in += MUL_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 23
	T20_mem0 += ADD_mem[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 23
	T20_mem1 += ADD_mem[0]

	T2T1 = S.Task('T2T1', length=1, delay_cost=1)
	S += T2T1 >= 23
	T2T1 += ADD[0]

	T2_6T2_mem0 = S.Task('T2_6T2_mem0', length=1, delay_cost=1)
	S += T2_6T2_mem0 >= 23
	T2_6T2_mem0 += INPUT_mem_r

	T2_6T2_mem1 = S.Task('T2_6T2_mem1', length=1, delay_cost=1)
	S += T2_6T2_mem1 >= 23
	T2_6T2_mem1 += INPUT_mem_r

	T3_1T2 = S.Task('T3_1T2', length=7, delay_cost=1)
	S += T3_1T2 >= 23
	T3_1T2 += MUL[0]

	T4_41_mem0 = S.Task('T4_41_mem0', length=1, delay_cost=1)
	S += T4_41_mem0 >= 23
	T4_41_mem0 += MUL_mem[0]

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 24
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 24
	T1T0_mem1 += INPUT_mem_r

	T20 = S.Task('T20', length=7, delay_cost=1)
	S += T20 >= 24
	T20 += MUL[0]

	T2_6T2 = S.Task('T2_6T2', length=1, delay_cost=1)
	S += T2_6T2 >= 24
	T2_6T2 += ADD[0]

	T3_1T0_mem0 = S.Task('T3_1T0_mem0', length=1, delay_cost=1)
	S += T3_1T0_mem0 >= 24
	T3_1T0_mem0 += ADD_mem[0]

	T3_1T0_mem1 = S.Task('T3_1T0_mem1', length=1, delay_cost=1)
	S += T3_1T0_mem1 >= 24
	T3_1T0_mem1 += ADD_mem[0]

	T4_41 = S.Task('T4_41', length=1, delay_cost=1)
	S += T4_41 >= 24
	T4_41 += ADD[2]

	T4_51_mem0 = S.Task('T4_51_mem0', length=1, delay_cost=1)
	S += T4_51_mem0 >= 24
	T4_51_mem0 += ADD_mem[2]

	T4_51_mem1 = S.Task('T4_51_mem1', length=1, delay_cost=1)
	S += T4_51_mem1 >= 24
	T4_51_mem1 += ADD_mem[2]

	NEW_A001_mem0 = S.Task('NEW_A001_mem0', length=1, delay_cost=1)
	S += NEW_A001_mem0 >= 25
	NEW_A001_mem0 += INPUT_mem_r

	NEW_A001_mem1 = S.Task('NEW_A001_mem1', length=1, delay_cost=1)
	S += NEW_A001_mem1 >= 25
	NEW_A001_mem1 += INPUT_mem_r

	T1T0 = S.Task('T1T0', length=1, delay_cost=1)
	S += T1T0 >= 25
	T1T0 += ADD[1]

	T3_1T0 = S.Task('T3_1T0', length=1, delay_cost=1)
	S += T3_1T0 >= 25
	T3_1T0 += ADD[3]

	T3_7T2_mem0 = S.Task('T3_7T2_mem0', length=1, delay_cost=1)
	S += T3_7T2_mem0 >= 25
	T3_7T2_mem0 += ADD_mem[0]

	T3_7T2_mem1 = S.Task('T3_7T2_mem1', length=1, delay_cost=1)
	S += T3_7T2_mem1 >= 25
	T3_7T2_mem1 += ADD_mem[0]

	T4_51 = S.Task('T4_51', length=1, delay_cost=1)
	S += T4_51 >= 25
	T4_51 += ADD[0]

	NEW_A001 = S.Task('NEW_A001', length=1, delay_cost=1)
	S += NEW_A001 >= 26
	NEW_A001 += ADD[0]

	T2_1T1_mem0 = S.Task('T2_1T1_mem0', length=1, delay_cost=1)
	S += T2_1T1_mem0 >= 26
	T2_1T1_mem0 += INPUT_mem_r

	T2_1T1_mem1 = S.Task('T2_1T1_mem1', length=1, delay_cost=1)
	S += T2_1T1_mem1 >= 26
	T2_1T1_mem1 += INPUT_mem_r

	T3T2_in = S.Task('T3T2_in', length=1, delay_cost=1)
	S += T3T2_in >= 26
	T3T2_in += MUL_in[0]

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	S += T3T2_mem0 >= 26
	T3T2_mem0 += ADD_mem[0]

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	S += T3T2_mem1 >= 26
	T3T2_mem1 += ADD_mem[0]

	T3_7T2 = S.Task('T3_7T2', length=1, delay_cost=1)
	S += T3_7T2 >= 26
	T3_7T2 += ADD[3]

	NEW_A120_mem0 = S.Task('NEW_A120_mem0', length=1, delay_cost=1)
	S += NEW_A120_mem0 >= 27
	NEW_A120_mem0 += INPUT_mem_r

	NEW_A120_mem1 = S.Task('NEW_A120_mem1', length=1, delay_cost=1)
	S += NEW_A120_mem1 >= 27
	NEW_A120_mem1 += INPUT_mem_r

	T2_1T1 = S.Task('T2_1T1', length=1, delay_cost=1)
	S += T2_1T1 >= 27
	T2_1T1 += ADD[2]

	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	S += T3T2 >= 27
	T3T2 += MUL[0]

	T3_1T1_mem0 = S.Task('T3_1T1_mem0', length=1, delay_cost=1)
	S += T3_1T1_mem0 >= 27
	T3_1T1_mem0 += ADD_mem[0]

	T3_1T1_mem1 = S.Task('T3_1T1_mem1', length=1, delay_cost=1)
	S += T3_1T1_mem1 >= 27
	T3_1T1_mem1 += ADD_mem[0]

	NEW_A120 = S.Task('NEW_A120', length=1, delay_cost=1)
	S += NEW_A120 >= 28
	NEW_A120 += ADD[0]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 28
	T10_in += MUL_in[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 28
	T10_mem0 += ADD_mem[1]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 28
	T10_mem1 += ADD_mem[0]

	T2_1T0_mem0 = S.Task('T2_1T0_mem0', length=1, delay_cost=1)
	S += T2_1T0_mem0 >= 28
	T2_1T0_mem0 += INPUT_mem_r

	T2_1T0_mem1 = S.Task('T2_1T0_mem1', length=1, delay_cost=1)
	S += T2_1T0_mem1 >= 28
	T2_1T0_mem1 += INPUT_mem_r

	T3_1T1 = S.Task('T3_1T1', length=1, delay_cost=1)
	S += T3_1T1 >= 28
	T3_1T1 += ADD[1]

	T5_11T2_mem0 = S.Task('T5_11T2_mem0', length=1, delay_cost=1)
	S += T5_11T2_mem0 >= 28
	T5_11T2_mem0 += ADD_mem[0]

	T5_11T2_mem1 = S.Task('T5_11T2_mem1', length=1, delay_cost=1)
	S += T5_11T2_mem1 >= 28
	T5_11T2_mem1 += ADD_mem[1]

	T10 = S.Task('T10', length=7, delay_cost=1)
	S += T10 >= 29
	T10 += MUL[0]

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	S += T1_T1_mem0 >= 29
	T1_T1_mem0 += INPUT_mem_r

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	S += T1_T1_mem1 >= 29
	T1_T1_mem1 += INPUT_mem_r

	T2_1T0 = S.Task('T2_1T0', length=1, delay_cost=1)
	S += T2_1T0 >= 29
	T2_1T0 += ADD[0]

	T3_11_mem0 = S.Task('T3_11_mem0', length=1, delay_cost=1)
	S += T3_11_mem0 >= 29
	T3_11_mem0 += MUL_mem[0]

	T5_11T2 = S.Task('T5_11T2', length=1, delay_cost=1)
	S += T5_11T2 >= 29
	T5_11T2 += ADD[3]

	T5_3T1_mem0 = S.Task('T5_3T1_mem0', length=1, delay_cost=1)
	S += T5_3T1_mem0 >= 29
	T5_3T1_mem0 += ADD_mem[0]

	T5_3T1_mem1 = S.Task('T5_3T1_mem1', length=1, delay_cost=1)
	S += T5_3T1_mem1 >= 29
	T5_3T1_mem1 += ADD_mem[1]

	T5_3T2_in = S.Task('T5_3T2_in', length=1, delay_cost=1)
	S += T5_3T2_in >= 29
	T5_3T2_in += MUL_in[0]

	T5_3T2_mem0 = S.Task('T5_3T2_mem0', length=1, delay_cost=1)
	S += T5_3T2_mem0 >= 29
	T5_3T2_mem0 += ADD_mem[0]

	T5_3T2_mem1 = S.Task('T5_3T2_mem1', length=1, delay_cost=1)
	S += T5_3T2_mem1 >= 29
	T5_3T2_mem1 += ADD_mem[1]

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	S += T1_T0_mem0 >= 30
	T1_T0_mem0 += INPUT_mem_r

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	S += T1_T0_mem1 >= 30
	T1_T0_mem1 += INPUT_mem_r

	T1_T1 = S.Task('T1_T1', length=1, delay_cost=1)
	S += T1_T1 >= 30
	T1_T1 += ADD[1]

	T2_10_in = S.Task('T2_10_in', length=1, delay_cost=1)
	S += T2_10_in >= 30
	T2_10_in += MUL_in[0]

	T2_10_mem0 = S.Task('T2_10_mem0', length=1, delay_cost=1)
	S += T2_10_mem0 >= 30
	T2_10_mem0 += ADD_mem[0]

	T2_10_mem1 = S.Task('T2_10_mem1', length=1, delay_cost=1)
	S += T2_10_mem1 >= 30
	T2_10_mem1 += ADD_mem[2]

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	S += T2_1_mem0 >= 30
	T2_1_mem0 += MUL_mem[0]

	T2_1_mem1 = S.Task('T2_1_mem1', length=1, delay_cost=1)
	S += T2_1_mem1 >= 30
	T2_1_mem1 += ADD_mem[1]

	T3_11 = S.Task('T3_11', length=1, delay_cost=1)
	S += T3_11 >= 30
	T3_11 += ADD[2]

	T3_21_mem0 = S.Task('T3_21_mem0', length=1, delay_cost=1)
	S += T3_21_mem0 >= 30
	T3_21_mem0 += ADD_mem[2]

	T3_21_mem1 = S.Task('T3_21_mem1', length=1, delay_cost=1)
	S += T3_21_mem1 >= 30
	T3_21_mem1 += ADD_mem[3]

	T5_3T0_mem0 = S.Task('T5_3T0_mem0', length=1, delay_cost=1)
	S += T5_3T0_mem0 >= 30
	T5_3T0_mem0 += ADD_mem[0]

	T5_3T0_mem1 = S.Task('T5_3T0_mem1', length=1, delay_cost=1)
	S += T5_3T0_mem1 >= 30
	T5_3T0_mem1 += ADD_mem[1]

	T5_3T1 = S.Task('T5_3T1', length=1, delay_cost=1)
	S += T5_3T1 >= 30
	T5_3T1 += ADD[3]

	T5_3T2 = S.Task('T5_3T2', length=7, delay_cost=1)
	S += T5_3T2 >= 30
	T5_3T2 += MUL[0]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 31
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 31
	T0T1_mem1 += INPUT_mem_r

	T1_0_in = S.Task('T1_0_in', length=1, delay_cost=1)
	S += T1_0_in >= 31
	T1_0_in += MUL_in[0]

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	S += T1_0_mem0 >= 31
	T1_0_mem0 += ADD_mem[2]

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	S += T1_0_mem1 >= 31
	T1_0_mem1 += ADD_mem[1]

	T1_T0 = S.Task('T1_T0', length=1, delay_cost=1)
	S += T1_T0 >= 31
	T1_T0 += ADD[2]

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	S += T2_0_mem0 >= 31
	T2_0_mem0 += MUL_mem[0]

	T2_0_mem1 = S.Task('T2_0_mem1', length=1, delay_cost=1)
	S += T2_0_mem1 >= 31
	T2_0_mem1 += ADD_mem[1]

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	S += T2_1 >= 31
	T2_1 += ADD[1]

	T2_10 = S.Task('T2_10', length=7, delay_cost=1)
	S += T2_10 >= 31
	T2_10 += MUL[0]

	T3_21 = S.Task('T3_21', length=1, delay_cost=1)
	S += T3_21 >= 31
	T3_21 += ADD[3]

	T3_5T2_mem0 = S.Task('T3_5T2_mem0', length=1, delay_cost=1)
	S += T3_5T2_mem0 >= 31
	T3_5T2_mem0 += ADD_mem[0]

	T3_5T2_mem1 = S.Task('T3_5T2_mem1', length=1, delay_cost=1)
	S += T3_5T2_mem1 >= 31
	T3_5T2_mem1 += ADD_mem[0]

	T5_3T0 = S.Task('T5_3T0', length=1, delay_cost=1)
	S += T5_3T0 >= 31
	T5_3T0 += ADD[0]

	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	S += T00_in >= 32
	T00_in += MUL_in[0]

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	S += T00_mem0 >= 32
	T00_mem0 += ADD_mem[1]

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	S += T00_mem1 >= 32
	T00_mem1 += ADD_mem[2]

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	S += T0T1 >= 32
	T0T1 += ADD[2]

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	S += T0_T1_mem0 >= 32
	T0_T1_mem0 += INPUT_mem_r

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	S += T0_T1_mem1 >= 32
	T0_T1_mem1 += INPUT_mem_r

	T1_0 = S.Task('T1_0', length=7, delay_cost=1)
	S += T1_0 >= 32
	T1_0 += MUL[0]

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	S += T2_0 >= 32
	T2_0 += ADD[1]

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	S += T3T0_mem0 >= 32
	T3T0_mem0 += ADD_mem[0]

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	S += T3T0_mem1 >= 32
	T3T0_mem1 += ADD_mem[0]

	T3_5T2 = S.Task('T3_5T2', length=1, delay_cost=1)
	S += T3_5T2 >= 32
	T3_5T2 += ADD[0]

	T00 = S.Task('T00', length=7, delay_cost=1)
	S += T00 >= 33
	T00 += MUL[0]

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	S += T0_T0_mem0 >= 33
	T0_T0_mem0 += INPUT_mem_r

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	S += T0_T0_mem1 >= 33
	T0_T0_mem1 += INPUT_mem_r

	T0_T1 = S.Task('T0_T1', length=1, delay_cost=1)
	S += T0_T1 >= 33
	T0_T1 += ADD[1]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 33
	T31_mem0 += MUL_mem[0]

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	S += T3T0 >= 33
	T3T0 += ADD[2]

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	S += T3T1_mem0 >= 33
	T3T1_mem0 += ADD_mem[0]

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	S += T3T1_mem1 >= 33
	T3T1_mem1 += ADD_mem[0]

	T3_10_in = S.Task('T3_10_in', length=1, delay_cost=1)
	S += T3_10_in >= 33
	T3_10_in += MUL_in[0]

	T3_10_mem0 = S.Task('T3_10_mem0', length=1, delay_cost=1)
	S += T3_10_mem0 >= 33
	T3_10_mem0 += ADD_mem[3]

	T3_10_mem1 = S.Task('T3_10_mem1', length=1, delay_cost=1)
	S += T3_10_mem1 >= 33
	T3_10_mem1 += ADD_mem[1]

	NEW_A021_mem0 = S.Task('NEW_A021_mem0', length=1, delay_cost=1)
	S += NEW_A021_mem0 >= 34
	NEW_A021_mem0 += INPUT_mem_r

	NEW_A021_mem1 = S.Task('NEW_A021_mem1', length=1, delay_cost=1)
	S += NEW_A021_mem1 >= 34
	NEW_A021_mem1 += INPUT_mem_r

	T0_0_in = S.Task('T0_0_in', length=1, delay_cost=1)
	S += T0_0_in >= 34
	T0_0_in += MUL_in[0]

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	S += T0_0_mem0 >= 34
	T0_0_mem0 += ADD_mem[2]

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	S += T0_0_mem1 >= 34
	T0_0_mem1 += ADD_mem[1]

	T0_T0 = S.Task('T0_T0', length=1, delay_cost=1)
	S += T0_T0 >= 34
	T0_T0 += ADD[2]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 34
	T31 += ADD[0]

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	S += T3T1 >= 34
	T3T1 += ADD[3]

	T3_10 = S.Task('T3_10', length=7, delay_cost=1)
	S += T3_10 >= 34
	T3_10 += MUL[0]

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	S += T3_1_mem0 >= 34
	T3_1_mem0 += ADD_mem[0]

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	S += T3_1_mem1 >= 34
	T3_1_mem1 += ADD_mem[2]

	NEW_A020_mem0 = S.Task('NEW_A020_mem0', length=1, delay_cost=1)
	S += NEW_A020_mem0 >= 35
	NEW_A020_mem0 += INPUT_mem_r

	NEW_A020_mem1 = S.Task('NEW_A020_mem1', length=1, delay_cost=1)
	S += NEW_A020_mem1 >= 35
	NEW_A020_mem1 += INPUT_mem_r

	NEW_A021 = S.Task('NEW_A021', length=1, delay_cost=1)
	S += NEW_A021 >= 35
	NEW_A021 += ADD[0]

	T0_0 = S.Task('T0_0', length=7, delay_cost=1)
	S += T0_0 >= 35
	T0_0 += MUL[0]

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 35
	T30_in += MUL_in[0]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 35
	T30_mem0 += ADD_mem[2]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 35
	T30_mem1 += ADD_mem[3]

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	S += T3_1 >= 35
	T3_1 += ADD[1]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 35
	T50_mem0 += MUL_mem[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 35
	T50_mem1 += MUL_mem[0]

	NEW_A020 = S.Task('NEW_A020', length=1, delay_cost=1)
	S += NEW_A020 >= 36
	NEW_A020 += ADD[2]

	T30 = S.Task('T30', length=7, delay_cost=1)
	S += T30 >= 36
	T30 += MUL[0]

	T4_10_mem0 = S.Task('T4_10_mem0', length=1, delay_cost=1)
	S += T4_10_mem0 >= 36
	T4_10_mem0 += MUL_mem[0]

	T4_10_mem1 = S.Task('T4_10_mem1', length=1, delay_cost=1)
	S += T4_10_mem1 >= 36
	T4_10_mem1 += ADD_mem[1]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 36
	T50 += ADD[1]

	T5_31_mem0 = S.Task('T5_31_mem0', length=1, delay_cost=1)
	S += T5_31_mem0 >= 36
	T5_31_mem0 += MUL_mem[0]

	T5_8T2_mem0 = S.Task('T5_8T2_mem0', length=1, delay_cost=1)
	S += T5_8T2_mem0 >= 36
	T5_8T2_mem0 += ADD_mem[2]

	T5_8T2_mem1 = S.Task('T5_8T2_mem1', length=1, delay_cost=1)
	S += T5_8T2_mem1 >= 36
	T5_8T2_mem1 += ADD_mem[0]

	T5_T2_in = S.Task('T5_T2_in', length=1, delay_cost=1)
	S += T5_T2_in >= 36
	T5_T2_in += MUL_in[0]

	T5_T2_mem0 = S.Task('T5_T2_mem0', length=1, delay_cost=1)
	S += T5_T2_mem0 >= 36
	T5_T2_mem0 += ADD_mem[2]

	T5_T2_mem1 = S.Task('T5_T2_mem1', length=1, delay_cost=1)
	S += T5_T2_mem1 >= 36
	T5_T2_mem1 += ADD_mem[0]

	T2_20_mem0 = S.Task('T2_20_mem0', length=1, delay_cost=1)
	S += T2_20_mem0 >= 37
	T2_20_mem0 += MUL_mem[0]

	T2_20_mem1 = S.Task('T2_20_mem1', length=1, delay_cost=1)
	S += T2_20_mem1 >= 37
	T2_20_mem1 += ADD_mem[3]

	T2_21_mem0 = S.Task('T2_21_mem0', length=1, delay_cost=1)
	S += T2_21_mem0 >= 37
	T2_21_mem0 += MUL_mem[0]

	T2_21_mem1 = S.Task('T2_21_mem1', length=1, delay_cost=1)
	S += T2_21_mem1 >= 37
	T2_21_mem1 += ADD_mem[3]

	T4_10 = S.Task('T4_10', length=1, delay_cost=1)
	S += T4_10 >= 37
	T4_10 += ADD[0]

	T5_31 = S.Task('T5_31', length=1, delay_cost=1)
	S += T5_31 >= 37
	T5_31 += ADD[1]

	T5_8T2 = S.Task('T5_8T2', length=1, delay_cost=1)
	S += T5_8T2 >= 37
	T5_8T2 += ADD[2]

	T5_T0_mem0 = S.Task('T5_T0_mem0', length=1, delay_cost=1)
	S += T5_T0_mem0 >= 37
	T5_T0_mem0 += ADD_mem[2]

	T5_T0_mem1 = S.Task('T5_T0_mem1', length=1, delay_cost=1)
	S += T5_T0_mem1 >= 37
	T5_T0_mem1 += ADD_mem[0]

	T5_T1_mem0 = S.Task('T5_T1_mem0', length=1, delay_cost=1)
	S += T5_T1_mem0 >= 37
	T5_T1_mem0 += ADD_mem[2]

	T5_T1_mem1 = S.Task('T5_T1_mem1', length=1, delay_cost=1)
	S += T5_T1_mem1 >= 37
	T5_T1_mem1 += ADD_mem[0]

	T5_T2 = S.Task('T5_T2', length=7, delay_cost=1)
	S += T5_T2 >= 37
	T5_T2 += MUL[0]

	T2_20 = S.Task('T2_20', length=1, delay_cost=1)
	S += T2_20 >= 38
	T2_20 += ADD[2]

	T2_21 = S.Task('T2_21', length=1, delay_cost=1)
	S += T2_21 >= 38
	T2_21 += ADD[3]

	T5_20_mem0 = S.Task('T5_20_mem0', length=1, delay_cost=1)
	S += T5_20_mem0 >= 38
	T5_20_mem0 += MUL_mem[0]

	T5_20_mem1 = S.Task('T5_20_mem1', length=1, delay_cost=1)
	S += T5_20_mem1 >= 38
	T5_20_mem1 += MUL_mem[0]

	T5_30_in = S.Task('T5_30_in', length=1, delay_cost=1)
	S += T5_30_in >= 38
	T5_30_in += MUL_in[0]

	T5_30_mem0 = S.Task('T5_30_mem0', length=1, delay_cost=1)
	S += T5_30_mem0 >= 38
	T5_30_mem0 += ADD_mem[0]

	T5_30_mem1 = S.Task('T5_30_mem1', length=1, delay_cost=1)
	S += T5_30_mem1 >= 38
	T5_30_mem1 += ADD_mem[3]

	T5_41_mem0 = S.Task('T5_41_mem0', length=1, delay_cost=1)
	S += T5_41_mem0 >= 38
	T5_41_mem0 += ADD_mem[1]

	T5_41_mem1 = S.Task('T5_41_mem1', length=1, delay_cost=1)
	S += T5_41_mem1 >= 38
	T5_41_mem1 += ADD_mem[1]

	T5_T0 = S.Task('T5_T0', length=1, delay_cost=1)
	S += T5_T0 >= 38
	T5_T0 += ADD[1]

	T5_T1 = S.Task('T5_T1', length=1, delay_cost=1)
	S += T5_T1 >= 38
	T5_T1 += ADD[0]

	T5_0_in = S.Task('T5_0_in', length=1, delay_cost=1)
	S += T5_0_in >= 39
	T5_0_in += MUL_in[0]

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	S += T5_0_mem0 >= 39
	T5_0_mem0 += ADD_mem[1]

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	S += T5_0_mem1 >= 39
	T5_0_mem1 += ADD_mem[0]

	T5_20 = S.Task('T5_20', length=1, delay_cost=1)
	S += T5_20 >= 39
	T5_20 += ADD[0]

	T5_30 = S.Task('T5_30', length=7, delay_cost=1)
	S += T5_30 >= 39
	T5_30 += MUL[0]

	T5_41 = S.Task('T5_41', length=1, delay_cost=1)
	S += T5_41 >= 39
	T5_41 += ADD[1]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 39
	T60_mem0 += MUL_mem[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 39
	T60_mem1 += MUL_mem[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 40
	T40_mem0 += MUL_mem[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 40
	T40_mem1 += MUL_mem[0]

	T5_0 = S.Task('T5_0', length=7, delay_cost=1)
	S += T5_0 >= 40
	T5_0 += MUL[0]

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 40
	T60 += ADD[3]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 41
	T40 += ADD[1]

	T4_30_mem0 = S.Task('T4_30_mem0', length=1, delay_cost=1)
	S += T4_30_mem0 >= 41
	T4_30_mem0 += MUL_mem[0]

	T4_30_mem1 = S.Task('T4_30_mem1', length=1, delay_cost=1)
	S += T4_30_mem1 >= 41
	T4_30_mem1 += MUL_mem[0]

	T3_20_mem0 = S.Task('T3_20_mem0', length=1, delay_cost=1)
	S += T3_20_mem0 >= 42
	T3_20_mem0 += MUL_mem[0]

	T3_20_mem1 = S.Task('T3_20_mem1', length=1, delay_cost=1)
	S += T3_20_mem1 >= 42
	T3_20_mem1 += ADD_mem[2]

	T4_30 = S.Task('T4_30', length=1, delay_cost=1)
	S += T4_30 >= 42
	T4_30 += ADD[2]

	T4_50_mem0 = S.Task('T4_50_mem0', length=1, delay_cost=1)
	S += T4_50_mem0 >= 42
	T4_50_mem0 += MUL_mem[0]

	T4_50_mem1 = S.Task('T4_50_mem1', length=1, delay_cost=1)
	S += T4_50_mem1 >= 42
	T4_50_mem1 += ADD_mem[0]

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	S += T3_0_mem0 >= 43
	T3_0_mem0 += MUL_mem[0]

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	S += T3_0_mem1 >= 43
	T3_0_mem1 += ADD_mem[1]

	T3_20 = S.Task('T3_20', length=1, delay_cost=1)
	S += T3_20 >= 43
	T3_20 += ADD[1]

	T4_50 = S.Task('T4_50', length=1, delay_cost=1)
	S += T4_50 >= 43
	T4_50 += ADD[3]

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	S += T5_1_mem0 >= 43
	T5_1_mem0 += MUL_mem[0]

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	S += T3_0 >= 44
	T3_0 += ADD[1]

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	S += T5_1 >= 44
	T5_1 += ADD[2]

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	S += T5_11_mem0 >= 44
	T5_11_mem0 += ADD_mem[2]

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	S += T5_11_mem1 >= 44
	T5_11_mem1 += ADD_mem[3]

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	S += T6_0_mem0 >= 44
	T6_0_mem0 += MUL_mem[0]

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	S += T6_0_mem1 >= 44
	T6_0_mem1 += MUL_mem[0]

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	S += T5_11 >= 45
	T5_11 += ADD[1]

	T5_40_mem0 = S.Task('T5_40_mem0', length=1, delay_cost=1)
	S += T5_40_mem0 >= 45
	T5_40_mem0 += MUL_mem[0]

	T5_40_mem1 = S.Task('T5_40_mem1', length=1, delay_cost=1)
	S += T5_40_mem1 >= 45
	T5_40_mem1 += ADD_mem[3]

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	S += T6_0 >= 45
	T6_0 += ADD[3]

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	S += T5_10_mem0 >= 46
	T5_10_mem0 += MUL_mem[0]

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	S += T5_10_mem1 >= 46
	T5_10_mem1 += ADD_mem[3]

	T5_40 = S.Task('T5_40', length=1, delay_cost=1)
	S += T5_40 >= 46
	T5_40 += ADD[2]

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	S += T5_10 >= 47
	T5_10 += ADD[1]


	# new tasks
	T4_20 = S.Task('T4_20', length=1, delay_cost=1)
	T4_20 += alt(ADD)

	T4_20_mem0 = S.Task('T4_20_mem0', length=1, delay_cost=1)
	T4_20_mem0 += ADD_mem[0]
	S += 37<T4_20_mem0
	S += T4_20_mem0<=T4_20

	T4_20_mem1 = S.Task('T4_20_mem1', length=1, delay_cost=1)
	T4_20_mem1 += ADD_mem[1]
	S += 21<T4_20_mem1
	S += T4_20_mem1<=T4_20

	T4_21 = S.Task('T4_21', length=1, delay_cost=1)
	T4_21 += alt(ADD)

	T4_21_mem0 = S.Task('T4_21_mem0', length=1, delay_cost=1)
	T4_21_mem0 += ADD_mem[0]
	S += 37<T4_21_mem0
	S += T4_21_mem0<=T4_21

	T4_21_mem1 = S.Task('T4_21_mem1', length=1, delay_cost=1)
	T4_21_mem1 += ADD_mem[1]
	S += 21<T4_21_mem1
	S += T4_21_mem1<=T4_21

	C10 = S.Task('C10', length=1, delay_cost=1)
	C10 += alt(ADD)

	C10_mem0 = S.Task('C10_mem0', length=1, delay_cost=1)
	C10_mem0 += ADD_mem[1]
	S += 44<C10_mem0
	S += C10_mem0<=C10

	C10_mem1 = S.Task('C10_mem1', length=1, delay_cost=1)
	C10_mem1 += ADD_mem[1]
	S += 32<C10_mem1
	S += C10_mem1<=C10

	C11 = S.Task('C11', length=1, delay_cost=1)
	C11 += alt(ADD)

	C11_mem0 = S.Task('C11_mem0', length=1, delay_cost=1)
	C11_mem0 += ADD_mem[1]
	S += 35<C11_mem0
	S += C11_mem0<=C11

	C11_mem1 = S.Task('C11_mem1', length=1, delay_cost=1)
	C11_mem1 += ADD_mem[1]
	S += 31<C11_mem1
	S += C11_mem1<=C11

	C20 = S.Task('C20', length=1, delay_cost=1)
	C20 += alt(ADD)

	C20_mem0 = S.Task('C20_mem0', length=1, delay_cost=1)
	C20_mem0 += MUL_mem[0]
	S += 35<C20_mem0
	S += C20_mem0<=C20

	C20_mem1 = S.Task('C20_mem1', length=1, delay_cost=1)
	C20_mem1 += ADD_mem[1]
	S += 47<C20_mem1
	S += C20_mem1<=C20

	C21 = S.Task('C21', length=1, delay_cost=1)
	C21 += alt(ADD)

	C21_mem0 = S.Task('C21_mem0', length=1, delay_cost=1)
	C21_mem0 += ADD_mem[0]
	S += 10<C21_mem0
	S += C21_mem0<=C21

	C21_mem1 = S.Task('C21_mem1', length=1, delay_cost=1)
	C21_mem1 += ADD_mem[1]
	S += 45<C21_mem1
	S += C21_mem1<=C21

	T4_60 = S.Task('T4_60', length=1, delay_cost=1)
	T4_60 += alt(ADD)

	T4_60_mem0 = S.Task('T4_60_mem0', length=1, delay_cost=1)
	T4_60_mem0 += ADD_mem[3]
	S += 43<T4_60_mem0
	S += T4_60_mem0<=T4_60

	T4_60_mem1 = S.Task('T4_60_mem1', length=1, delay_cost=1)
	T4_60_mem1 += ADD_mem[0]
	S += 25<T4_60_mem1
	S += T4_60_mem1<=T4_60

	T4_61 = S.Task('T4_61', length=1, delay_cost=1)
	T4_61 += alt(ADD)

	T4_61_mem0 = S.Task('T4_61_mem0', length=1, delay_cost=1)
	T4_61_mem0 += ADD_mem[3]
	S += 43<T4_61_mem0
	S += T4_61_mem0<=T4_61

	T4_61_mem1 = S.Task('T4_61_mem1', length=1, delay_cost=1)
	T4_61_mem1 += ADD_mem[0]
	S += 25<T4_61_mem1
	S += T4_61_mem1<=T4_61

	C40 = S.Task('C40', length=1, delay_cost=1)
	C40 += alt(ADD)

	C40_mem0 = S.Task('C40_mem0', length=1, delay_cost=1)
	C40_mem0 += ADD_mem[1]
	S += 43<C40_mem0
	S += C40_mem0<=C40

	C40_mem1 = S.Task('C40_mem1', length=1, delay_cost=1)
	C40_mem1 += ADD_mem[2]
	S += 38<C40_mem1
	S += C40_mem1<=C40

	C41 = S.Task('C41', length=1, delay_cost=1)
	C41 += alt(ADD)

	C41_mem0 = S.Task('C41_mem0', length=1, delay_cost=1)
	C41_mem0 += ADD_mem[3]
	S += 31<C41_mem0
	S += C41_mem0<=C41

	C41_mem1 = S.Task('C41_mem1', length=1, delay_cost=1)
	C41_mem1 += ADD_mem[3]
	S += 38<C41_mem1
	S += C41_mem1<=C41

	C50 = S.Task('C50', length=1, delay_cost=1)
	C50 += alt(ADD)

	C50_mem0 = S.Task('C50_mem0', length=1, delay_cost=1)
	C50_mem0 += MUL_mem[0]
	S += 38<C50_mem0
	S += C50_mem0<=C50

	C50_mem1 = S.Task('C50_mem1', length=1, delay_cost=1)
	C50_mem1 += ADD_mem[2]
	S += 46<C50_mem1
	S += C50_mem1<=C50

	C51 = S.Task('C51', length=1, delay_cost=1)
	C51 += alt(ADD)

	C51_mem0 = S.Task('C51_mem0', length=1, delay_cost=1)
	C51_mem0 += ADD_mem[0]
	S += 11<C51_mem0
	S += C51_mem0<=C51

	C51_mem1 = S.Task('C51_mem1', length=1, delay_cost=1)
	C51_mem1 += ADD_mem[1]
	S += 39<C51_mem1
	S += C51_mem1<=C51

	C00 = S.Task('C00', length=1, delay_cost=1)
	C00 += alt(ADD)

	C00_mem0 = S.Task('C00_mem0', length=1, delay_cost=1)
	C00_mem0 += MUL_mem[0]
	S += 39<C00_mem0
	S += C00_mem0<=C00

	C00_mem1 = S.Task('C00_mem1', length=1, delay_cost=1)
	C00_mem1 += alt(ADD_mem)
	S += (T4_20*ADD[0])-1<C00_mem1*ADD_mem[0]
	S += (T4_20*ADD[1])-1<C00_mem1*ADD_mem[1]
	S += (T4_20*ADD[2])-1<C00_mem1*ADD_mem[2]
	S += (T4_20*ADD[3])-1<C00_mem1*ADD_mem[3]
	S += C00_mem1<=C00

	C01 = S.Task('C01', length=1, delay_cost=1)
	C01 += alt(ADD)

	C01_mem0 = S.Task('C01_mem0', length=1, delay_cost=1)
	C01_mem0 += ADD_mem[3]
	S += 13<C01_mem0
	S += C01_mem0<=C01

	C01_mem1 = S.Task('C01_mem1', length=1, delay_cost=1)
	C01_mem1 += alt(ADD_mem)
	S += (T4_21*ADD[0])-1<C01_mem1*ADD_mem[0]
	S += (T4_21*ADD[1])-1<C01_mem1*ADD_mem[1]
	S += (T4_21*ADD[2])-1<C01_mem1*ADD_mem[2]
	S += (T4_21*ADD[3])-1<C01_mem1*ADD_mem[3]
	S += C01_mem1<=C01

	C30 = S.Task('C30', length=1, delay_cost=1)
	C30 += alt(ADD)

	C30_mem0 = S.Task('C30_mem0', length=1, delay_cost=1)
	C30_mem0 += MUL_mem[0]
	S += 41<C30_mem0
	S += C30_mem0<=C30

	C30_mem1 = S.Task('C30_mem1', length=1, delay_cost=1)
	C30_mem1 += alt(ADD_mem)
	S += (T4_60*ADD[0])-1<C30_mem1*ADD_mem[0]
	S += (T4_60*ADD[1])-1<C30_mem1*ADD_mem[1]
	S += (T4_60*ADD[2])-1<C30_mem1*ADD_mem[2]
	S += (T4_60*ADD[3])-1<C30_mem1*ADD_mem[3]
	S += C30_mem1<=C30

	C31 = S.Task('C31', length=1, delay_cost=1)
	C31 += alt(ADD)

	C31_mem0 = S.Task('C31_mem0', length=1, delay_cost=1)
	C31_mem0 += ADD_mem[1]
	S += 12<C31_mem0
	S += C31_mem0<=C31

	C31_mem1 = S.Task('C31_mem1', length=1, delay_cost=1)
	C31_mem1 += alt(ADD_mem)
	S += (T4_61*ADD[0])-1<C31_mem1*ADD_mem[0]
	S += (T4_61*ADD[1])-1<C31_mem1*ADD_mem[1]
	S += (T4_61*ADD[2])-1<C31_mem1*ADD_mem[2]
	S += (T4_61*ADD[3])-1<C31_mem1*ADD_mem[3]
	S += C31_mem1<=C31

	C5_0 = S.Task('C5_0', length=1, delay_cost=1)
	C5_0 += alt(ADD)

	C5_0_mem0 = S.Task('C5_0_mem0', length=1, delay_cost=1)
	C5_0_mem0 += alt(ADD_mem)
	S += (C50*ADD[0])-1<C5_0_mem0*ADD_mem[0]
	S += (C50*ADD[1])-1<C5_0_mem0*ADD_mem[1]
	S += (C50*ADD[2])-1<C5_0_mem0*ADD_mem[2]
	S += (C50*ADD[3])-1<C5_0_mem0*ADD_mem[3]
	S += C5_0_mem0<=C5_0

	C5_0_mem1 = S.Task('C5_0_mem1', length=1, delay_cost=1)
	C5_0_mem1 += alt(ADD_mem)
	S += (C51*ADD[0])-1<C5_0_mem1*ADD_mem[0]
	S += (C51*ADD[1])-1<C5_0_mem1*ADD_mem[1]
	S += (C51*ADD[2])-1<C5_0_mem1*ADD_mem[2]
	S += (C51*ADD[3])-1<C5_0_mem1*ADD_mem[3]
	S += C5_0_mem1<=C5_0

	C5_1 = S.Task('C5_1', length=1, delay_cost=1)
	C5_1 += alt(ADD)

	C5_1_mem0 = S.Task('C5_1_mem0', length=1, delay_cost=1)
	C5_1_mem0 += alt(ADD_mem)
	S += (C50*ADD[0])-1<C5_1_mem0*ADD_mem[0]
	S += (C50*ADD[1])-1<C5_1_mem0*ADD_mem[1]
	S += (C50*ADD[2])-1<C5_1_mem0*ADD_mem[2]
	S += (C50*ADD[3])-1<C5_1_mem0*ADD_mem[3]
	S += C5_1_mem0<=C5_1

	C5_1_mem1 = S.Task('C5_1_mem1', length=1, delay_cost=1)
	C5_1_mem1 += alt(ADD_mem)
	S += (C51*ADD[0])-1<C5_1_mem1*ADD_mem[0]
	S += (C51*ADD[1])-1<C5_1_mem1*ADD_mem[1]
	S += (C51*ADD[2])-1<C5_1_mem1*ADD_mem[2]
	S += (C51*ADD[3])-1<C5_1_mem1*ADD_mem[3]
	S += C5_1_mem1<=C5_1

	C2_0 = S.Task('C2_0', length=1, delay_cost=1)
	C2_0 += alt(ADD)

	C2_0_mem0 = S.Task('C2_0_mem0', length=1, delay_cost=1)
	C2_0_mem0 += alt(ADD_mem)
	S += (C20*ADD[0])-1<C2_0_mem0*ADD_mem[0]
	S += (C20*ADD[1])-1<C2_0_mem0*ADD_mem[1]
	S += (C20*ADD[2])-1<C2_0_mem0*ADD_mem[2]
	S += (C20*ADD[3])-1<C2_0_mem0*ADD_mem[3]
	S += C2_0_mem0<=C2_0

	C2_0_mem1 = S.Task('C2_0_mem1', length=1, delay_cost=1)
	C2_0_mem1 += alt(ADD_mem)
	S += (C40*ADD[0])-1<C2_0_mem1*ADD_mem[0]
	S += (C40*ADD[1])-1<C2_0_mem1*ADD_mem[1]
	S += (C40*ADD[2])-1<C2_0_mem1*ADD_mem[2]
	S += (C40*ADD[3])-1<C2_0_mem1*ADD_mem[3]
	S += C2_0_mem1<=C2_0

	C2_1 = S.Task('C2_1', length=1, delay_cost=1)
	C2_1 += alt(ADD)

	C2_1_mem0 = S.Task('C2_1_mem0', length=1, delay_cost=1)
	C2_1_mem0 += alt(ADD_mem)
	S += (C21*ADD[0])-1<C2_1_mem0*ADD_mem[0]
	S += (C21*ADD[1])-1<C2_1_mem0*ADD_mem[1]
	S += (C21*ADD[2])-1<C2_1_mem0*ADD_mem[2]
	S += (C21*ADD[3])-1<C2_1_mem0*ADD_mem[3]
	S += C2_1_mem0<=C2_1

	C2_1_mem1 = S.Task('C2_1_mem1', length=1, delay_cost=1)
	C2_1_mem1 += alt(ADD_mem)
	S += (C41*ADD[0])-1<C2_1_mem1*ADD_mem[0]
	S += (C41*ADD[1])-1<C2_1_mem1*ADD_mem[1]
	S += (C41*ADD[2])-1<C2_1_mem1*ADD_mem[2]
	S += (C41*ADD[3])-1<C2_1_mem1*ADD_mem[3]
	S += C2_1_mem1<=C2_1

	C0_0 = S.Task('C0_0', length=1, delay_cost=1)
	C0_0 += alt(ADD)

	C0_0_mem0 = S.Task('C0_0_mem0', length=1, delay_cost=1)
	C0_0_mem0 += alt(ADD_mem)
	S += (C00*ADD[0])-1<C0_0_mem0*ADD_mem[0]
	S += (C00*ADD[1])-1<C0_0_mem0*ADD_mem[1]
	S += (C00*ADD[2])-1<C0_0_mem0*ADD_mem[2]
	S += (C00*ADD[3])-1<C0_0_mem0*ADD_mem[3]
	S += C0_0_mem0<=C0_0

	C0_0_mem1 = S.Task('C0_0_mem1', length=1, delay_cost=1)
	C0_0_mem1 += alt(ADD_mem)
	S += (C5_0*ADD[0])-1<C0_0_mem1*ADD_mem[0]
	S += (C5_0*ADD[1])-1<C0_0_mem1*ADD_mem[1]
	S += (C5_0*ADD[2])-1<C0_0_mem1*ADD_mem[2]
	S += (C5_0*ADD[3])-1<C0_0_mem1*ADD_mem[3]
	S += C0_0_mem1<=C0_0

	C0_1 = S.Task('C0_1', length=1, delay_cost=1)
	C0_1 += alt(ADD)

	C0_1_mem0 = S.Task('C0_1_mem0', length=1, delay_cost=1)
	C0_1_mem0 += alt(ADD_mem)
	S += (C01*ADD[0])-1<C0_1_mem0*ADD_mem[0]
	S += (C01*ADD[1])-1<C0_1_mem0*ADD_mem[1]
	S += (C01*ADD[2])-1<C0_1_mem0*ADD_mem[2]
	S += (C01*ADD[3])-1<C0_1_mem0*ADD_mem[3]
	S += C0_1_mem0<=C0_1

	C0_1_mem1 = S.Task('C0_1_mem1', length=1, delay_cost=1)
	C0_1_mem1 += alt(ADD_mem)
	S += (C5_1*ADD[0])-1<C0_1_mem1*ADD_mem[0]
	S += (C5_1*ADD[1])-1<C0_1_mem1*ADD_mem[1]
	S += (C5_1*ADD[2])-1<C0_1_mem1*ADD_mem[2]
	S += (C5_1*ADD[3])-1<C0_1_mem1*ADD_mem[3]
	S += C0_1_mem1<=C0_1

	C1_0 = S.Task('C1_0', length=1, delay_cost=1)
	C1_0 += alt(ADD)

	C1_0_mem0 = S.Task('C1_0_mem0', length=1, delay_cost=1)
	C1_0_mem0 += alt(ADD_mem)
	S += (C10*ADD[0])-1<C1_0_mem0*ADD_mem[0]
	S += (C10*ADD[1])-1<C1_0_mem0*ADD_mem[1]
	S += (C10*ADD[2])-1<C1_0_mem0*ADD_mem[2]
	S += (C10*ADD[3])-1<C1_0_mem0*ADD_mem[3]
	S += C1_0_mem0<=C1_0

	C1_0_mem1 = S.Task('C1_0_mem1', length=1, delay_cost=1)
	C1_0_mem1 += alt(ADD_mem)
	S += (C30*ADD[0])-1<C1_0_mem1*ADD_mem[0]
	S += (C30*ADD[1])-1<C1_0_mem1*ADD_mem[1]
	S += (C30*ADD[2])-1<C1_0_mem1*ADD_mem[2]
	S += (C30*ADD[3])-1<C1_0_mem1*ADD_mem[3]
	S += C1_0_mem1<=C1_0

	C1_1 = S.Task('C1_1', length=1, delay_cost=1)
	C1_1 += alt(ADD)

	C1_1_mem0 = S.Task('C1_1_mem0', length=1, delay_cost=1)
	C1_1_mem0 += alt(ADD_mem)
	S += (C11*ADD[0])-1<C1_1_mem0*ADD_mem[0]
	S += (C11*ADD[1])-1<C1_1_mem0*ADD_mem[1]
	S += (C11*ADD[2])-1<C1_1_mem0*ADD_mem[2]
	S += (C11*ADD[3])-1<C1_1_mem0*ADD_mem[3]
	S += C1_1_mem0<=C1_1

	C1_1_mem1 = S.Task('C1_1_mem1', length=1, delay_cost=1)
	C1_1_mem1 += alt(ADD_mem)
	S += (C31*ADD[0])-1<C1_1_mem1*ADD_mem[0]
	S += (C31*ADD[1])-1<C1_1_mem1*ADD_mem[1]
	S += (C31*ADD[2])-1<C1_1_mem1*ADD_mem[2]
	S += (C31*ADD[3])-1<C1_1_mem1*ADD_mem[3]
	S += C1_1_mem1<=C1_1

	T2_3T0 = S.Task('T2_3T0', length=1, delay_cost=1)
	T2_3T0 += alt(ADD)

	T2_3T0_mem0 = S.Task('T2_3T0_mem0', length=1, delay_cost=1)
	T2_3T0_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T2_3T0_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T2_3T0_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T2_3T0_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T2_3T0_mem0*ADD_mem[3]
	S += T2_3T0_mem0<=T2_3T0

	T2_3T0_mem1 = S.Task('T2_3T0_mem1', length=1, delay_cost=1)
	T2_3T0_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T2_3T0_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T2_3T0_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T2_3T0_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T2_3T0_mem1*ADD_mem[3]
	S += T2_3T0_mem1<=T2_3T0

	T2_3T1 = S.Task('T2_3T1', length=1, delay_cost=1)
	T2_3T1 += alt(ADD)

	T2_3T1_mem0 = S.Task('T2_3T1_mem0', length=1, delay_cost=1)
	T2_3T1_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T2_3T1_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T2_3T1_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T2_3T1_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T2_3T1_mem0*ADD_mem[3]
	S += T2_3T1_mem0<=T2_3T1

	T2_3T1_mem1 = S.Task('T2_3T1_mem1', length=1, delay_cost=1)
	T2_3T1_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T2_3T1_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T2_3T1_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T2_3T1_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T2_3T1_mem1*ADD_mem[3]
	S += T2_3T1_mem1<=T2_3T1

	T2_3T2_in = S.Task('T2_3T2_in', length=1, delay_cost=1)
	T2_3T2_in += alt(MUL_in)
	T2_3T2 = S.Task('T2_3T2', length=7, delay_cost=1)
	T2_3T2 += alt(MUL)
	S+=T2_3T2>=T2_3T2_in

	T2_3T2_mem0 = S.Task('T2_3T2_mem0', length=1, delay_cost=1)
	T2_3T2_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T2_3T2_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T2_3T2_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T2_3T2_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T2_3T2_mem0*ADD_mem[3]
	S += T2_3T2_mem0<=T2_3T2

	T2_3T2_mem1 = S.Task('T2_3T2_mem1', length=1, delay_cost=1)
	T2_3T2_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T2_3T2_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T2_3T2_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T2_3T2_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T2_3T2_mem1*ADD_mem[3]
	S += T2_3T2_mem1<=T2_3T2

	T4_7T3 = S.Task('T4_7T3', length=1, delay_cost=1)
	T4_7T3 += alt(ADD)

	T4_7T3_mem0 = S.Task('T4_7T3_mem0', length=1, delay_cost=1)
	T4_7T3_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T4_7T3_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T4_7T3_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T4_7T3_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T4_7T3_mem0*ADD_mem[3]
	S += T4_7T3_mem0<=T4_7T3

	T4_7T3_mem1 = S.Task('T4_7T3_mem1', length=1, delay_cost=1)
	T4_7T3_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T4_7T3_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T4_7T3_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T4_7T3_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T4_7T3_mem1*ADD_mem[3]
	S += T4_7T3_mem1<=T4_7T3

	T5_5T2 = S.Task('T5_5T2', length=1, delay_cost=1)
	T5_5T2 += alt(ADD)

	T5_5T2_mem0 = S.Task('T5_5T2_mem0', length=1, delay_cost=1)
	T5_5T2_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T5_5T2_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T5_5T2_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T5_5T2_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T5_5T2_mem0*ADD_mem[3]
	S += T5_5T2_mem0<=T5_5T2

	T5_5T2_mem1 = S.Task('T5_5T2_mem1', length=1, delay_cost=1)
	T5_5T2_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T5_5T2_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T5_5T2_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T5_5T2_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T5_5T2_mem1*ADD_mem[3]
	S += T5_5T2_mem1<=T5_5T2

	T3_4T3 = S.Task('T3_4T3', length=1, delay_cost=1)
	T3_4T3 += alt(ADD)

	T3_4T3_mem0 = S.Task('T3_4T3_mem0', length=1, delay_cost=1)
	T3_4T3_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T3_4T3_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T3_4T3_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T3_4T3_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T3_4T3_mem0*ADD_mem[3]
	S += T3_4T3_mem0<=T3_4T3

	T3_4T3_mem1 = S.Task('T3_4T3_mem1', length=1, delay_cost=1)
	T3_4T3_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T3_4T3_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T3_4T3_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T3_4T3_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T3_4T3_mem1*ADD_mem[3]
	S += T3_4T3_mem1<=T3_4T3

	T0_1T0 = S.Task('T0_1T0', length=1, delay_cost=1)
	T0_1T0 += alt(ADD)

	T0_1T0_mem0 = S.Task('T0_1T0_mem0', length=1, delay_cost=1)
	T0_1T0_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T0_1T0_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T0_1T0_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T0_1T0_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T0_1T0_mem0*ADD_mem[3]
	S += T0_1T0_mem0<=T0_1T0

	T0_1T0_mem1 = S.Task('T0_1T0_mem1', length=1, delay_cost=1)
	T0_1T0_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T0_1T0_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T0_1T0_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T0_1T0_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T0_1T0_mem1*ADD_mem[3]
	S += T0_1T0_mem1<=T0_1T0

	T0_1T1 = S.Task('T0_1T1', length=1, delay_cost=1)
	T0_1T1 += alt(ADD)

	T0_1T1_mem0 = S.Task('T0_1T1_mem0', length=1, delay_cost=1)
	T0_1T1_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T0_1T1_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T0_1T1_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T0_1T1_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T0_1T1_mem0*ADD_mem[3]
	S += T0_1T1_mem0<=T0_1T1

	T0_1T1_mem1 = S.Task('T0_1T1_mem1', length=1, delay_cost=1)
	T0_1T1_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T0_1T1_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T0_1T1_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T0_1T1_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T0_1T1_mem1*ADD_mem[3]
	S += T0_1T1_mem1<=T0_1T1

	T0_1T2_in = S.Task('T0_1T2_in', length=1, delay_cost=1)
	T0_1T2_in += alt(MUL_in)
	T0_1T2 = S.Task('T0_1T2', length=7, delay_cost=1)
	T0_1T2 += alt(MUL)
	S+=T0_1T2>=T0_1T2_in

	T0_1T2_mem0 = S.Task('T0_1T2_mem0', length=1, delay_cost=1)
	T0_1T2_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T0_1T2_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T0_1T2_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T0_1T2_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T0_1T2_mem0*ADD_mem[3]
	S += T0_1T2_mem0<=T0_1T2

	T0_1T2_mem1 = S.Task('T0_1T2_mem1', length=1, delay_cost=1)
	T0_1T2_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T0_1T2_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T0_1T2_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T0_1T2_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T0_1T2_mem1*ADD_mem[3]
	S += T0_1T2_mem1<=T0_1T2

	T1_1T0 = S.Task('T1_1T0', length=1, delay_cost=1)
	T1_1T0 += alt(ADD)

	T1_1T0_mem0 = S.Task('T1_1T0_mem0', length=1, delay_cost=1)
	T1_1T0_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T1_1T0_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T1_1T0_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T1_1T0_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T1_1T0_mem0*ADD_mem[3]
	S += T1_1T0_mem0<=T1_1T0

	T1_1T0_mem1 = S.Task('T1_1T0_mem1', length=1, delay_cost=1)
	T1_1T0_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T1_1T0_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T1_1T0_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T1_1T0_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T1_1T0_mem1*ADD_mem[3]
	S += T1_1T0_mem1<=T1_1T0

	T1_1T1 = S.Task('T1_1T1', length=1, delay_cost=1)
	T1_1T1 += alt(ADD)

	T1_1T1_mem0 = S.Task('T1_1T1_mem0', length=1, delay_cost=1)
	T1_1T1_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T1_1T1_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T1_1T1_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T1_1T1_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T1_1T1_mem0*ADD_mem[3]
	S += T1_1T1_mem0<=T1_1T1

	T1_1T1_mem1 = S.Task('T1_1T1_mem1', length=1, delay_cost=1)
	T1_1T1_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T1_1T1_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T1_1T1_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T1_1T1_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T1_1T1_mem1*ADD_mem[3]
	S += T1_1T1_mem1<=T1_1T1

	T1_1T2_in = S.Task('T1_1T2_in', length=1, delay_cost=1)
	T1_1T2_in += alt(MUL_in)
	T1_1T2 = S.Task('T1_1T2', length=7, delay_cost=1)
	T1_1T2 += alt(MUL)
	S+=T1_1T2>=T1_1T2_in

	T1_1T2_mem0 = S.Task('T1_1T2_mem0', length=1, delay_cost=1)
	T1_1T2_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T1_1T2_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T1_1T2_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T1_1T2_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T1_1T2_mem0*ADD_mem[3]
	S += T1_1T2_mem0<=T1_1T2

	T1_1T2_mem1 = S.Task('T1_1T2_mem1', length=1, delay_cost=1)
	T1_1T2_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T1_1T2_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T1_1T2_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T1_1T2_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T1_1T2_mem1*ADD_mem[3]
	S += T1_1T2_mem1<=T1_1T2

	T2_30_in = S.Task('T2_30_in', length=1, delay_cost=1)
	T2_30_in += alt(MUL_in)
	T2_30 = S.Task('T2_30', length=7, delay_cost=1)
	T2_30 += alt(MUL)
	S+=T2_30>=T2_30_in

	T2_30_mem0 = S.Task('T2_30_mem0', length=1, delay_cost=1)
	T2_30_mem0 += alt(ADD_mem)
	S += (T2_3T0*ADD[0])-1<T2_30_mem0*ADD_mem[0]
	S += (T2_3T0*ADD[1])-1<T2_30_mem0*ADD_mem[1]
	S += (T2_3T0*ADD[2])-1<T2_30_mem0*ADD_mem[2]
	S += (T2_3T0*ADD[3])-1<T2_30_mem0*ADD_mem[3]
	S += T2_30_mem0<=T2_30

	T2_30_mem1 = S.Task('T2_30_mem1', length=1, delay_cost=1)
	T2_30_mem1 += alt(ADD_mem)
	S += (T2_3T1*ADD[0])-1<T2_30_mem1*ADD_mem[0]
	S += (T2_3T1*ADD[1])-1<T2_30_mem1*ADD_mem[1]
	S += (T2_3T1*ADD[2])-1<T2_30_mem1*ADD_mem[2]
	S += (T2_3T1*ADD[3])-1<T2_30_mem1*ADD_mem[3]
	S += T2_30_mem1<=T2_30

	T2_31 = S.Task('T2_31', length=1, delay_cost=1)
	T2_31 += alt(ADD)

	T2_31_mem0 = S.Task('T2_31_mem0', length=1, delay_cost=1)
	T2_31_mem0 += alt(MUL_mem)
	S += (T2_3T2*MUL[0])-1<T2_31_mem0*MUL_mem[0]
	S += T2_31_mem0<=T2_31

	T3_3T0_in = S.Task('T3_3T0_in', length=1, delay_cost=1)
	T3_3T0_in += alt(MUL_in)
	T3_3T0 = S.Task('T3_3T0', length=7, delay_cost=1)
	T3_3T0 += alt(MUL)
	S+=T3_3T0>=T3_3T0_in

	T3_3T0_mem0 = S.Task('T3_3T0_mem0', length=1, delay_cost=1)
	T3_3T0_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T3_3T0_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T3_3T0_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T3_3T0_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T3_3T0_mem0*ADD_mem[3]
	S += T3_3T0_mem0<=T3_3T0

	T3_3T0_mem1 = S.Task('T3_3T0_mem1', length=1, delay_cost=1)
	T3_3T0_mem1 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T3_3T0_mem1*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T3_3T0_mem1*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T3_3T0_mem1*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T3_3T0_mem1*ADD_mem[3]
	S += T3_3T0_mem1<=T3_3T0

	T3_3T1_in = S.Task('T3_3T1_in', length=1, delay_cost=1)
	T3_3T1_in += alt(MUL_in)
	T3_3T1 = S.Task('T3_3T1', length=7, delay_cost=1)
	T3_3T1 += alt(MUL)
	S+=T3_3T1>=T3_3T1_in

	T3_3T1_mem0 = S.Task('T3_3T1_mem0', length=1, delay_cost=1)
	T3_3T1_mem0 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T3_3T1_mem0*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T3_3T1_mem0*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T3_3T1_mem0*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T3_3T1_mem0*ADD_mem[3]
	S += T3_3T1_mem0<=T3_3T1

	T3_3T1_mem1 = S.Task('T3_3T1_mem1', length=1, delay_cost=1)
	T3_3T1_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T3_3T1_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T3_3T1_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T3_3T1_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T3_3T1_mem1*ADD_mem[3]
	S += T3_3T1_mem1<=T3_3T1

	T3_3T2 = S.Task('T3_3T2', length=1, delay_cost=1)
	T3_3T2 += alt(ADD)

	T3_3T2_mem0 = S.Task('T3_3T2_mem0', length=1, delay_cost=1)
	T3_3T2_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T3_3T2_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T3_3T2_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T3_3T2_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T3_3T2_mem0*ADD_mem[3]
	S += T3_3T2_mem0<=T3_3T2

	T3_3T2_mem1 = S.Task('T3_3T2_mem1', length=1, delay_cost=1)
	T3_3T2_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T3_3T2_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T3_3T2_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T3_3T2_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T3_3T2_mem1*ADD_mem[3]
	S += T3_3T2_mem1<=T3_3T2

	T3_3T3 = S.Task('T3_3T3', length=1, delay_cost=1)
	T3_3T3 += alt(ADD)

	T3_3T3_mem0 = S.Task('T3_3T3_mem0', length=1, delay_cost=1)
	T3_3T3_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T3_3T3_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T3_3T3_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T3_3T3_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T3_3T3_mem0*ADD_mem[3]
	S += T3_3T3_mem0<=T3_3T3

	T3_3T3_mem1 = S.Task('T3_3T3_mem1', length=1, delay_cost=1)
	T3_3T3_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T3_3T3_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T3_3T3_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T3_3T3_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T3_3T3_mem1*ADD_mem[3]
	S += T3_3T3_mem1<=T3_3T3

	T4_7T0_in = S.Task('T4_7T0_in', length=1, delay_cost=1)
	T4_7T0_in += alt(MUL_in)
	T4_7T0 = S.Task('T4_7T0', length=7, delay_cost=1)
	T4_7T0 += alt(MUL)
	S+=T4_7T0>=T4_7T0_in

	T4_7T0_mem0 = S.Task('T4_7T0_mem0', length=1, delay_cost=1)
	T4_7T0_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T4_7T0_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T4_7T0_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T4_7T0_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T4_7T0_mem0*ADD_mem[3]
	S += T4_7T0_mem0<=T4_7T0

	T4_7T0_mem1 = S.Task('T4_7T0_mem1', length=1, delay_cost=1)
	T4_7T0_mem1 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T4_7T0_mem1*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T4_7T0_mem1*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T4_7T0_mem1*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T4_7T0_mem1*ADD_mem[3]
	S += T4_7T0_mem1<=T4_7T0

	T4_7T1_in = S.Task('T4_7T1_in', length=1, delay_cost=1)
	T4_7T1_in += alt(MUL_in)
	T4_7T1 = S.Task('T4_7T1', length=7, delay_cost=1)
	T4_7T1 += alt(MUL)
	S+=T4_7T1>=T4_7T1_in

	T4_7T1_mem0 = S.Task('T4_7T1_mem0', length=1, delay_cost=1)
	T4_7T1_mem0 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T4_7T1_mem0*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T4_7T1_mem0*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T4_7T1_mem0*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T4_7T1_mem0*ADD_mem[3]
	S += T4_7T1_mem0<=T4_7T1

	T4_7T1_mem1 = S.Task('T4_7T1_mem1', length=1, delay_cost=1)
	T4_7T1_mem1 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T4_7T1_mem1*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T4_7T1_mem1*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T4_7T1_mem1*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T4_7T1_mem1*ADD_mem[3]
	S += T4_7T1_mem1<=T4_7T1

	T4_7T2 = S.Task('T4_7T2', length=1, delay_cost=1)
	T4_7T2 += alt(ADD)

	T4_7T2_mem0 = S.Task('T4_7T2_mem0', length=1, delay_cost=1)
	T4_7T2_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T4_7T2_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T4_7T2_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T4_7T2_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T4_7T2_mem0*ADD_mem[3]
	S += T4_7T2_mem0<=T4_7T2

	T4_7T2_mem1 = S.Task('T4_7T2_mem1', length=1, delay_cost=1)
	T4_7T2_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T4_7T2_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T4_7T2_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T4_7T2_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T4_7T2_mem1*ADD_mem[3]
	S += T4_7T2_mem1<=T4_7T2

	T5_5T0_in = S.Task('T5_5T0_in', length=1, delay_cost=1)
	T5_5T0_in += alt(MUL_in)
	T5_5T0 = S.Task('T5_5T0', length=7, delay_cost=1)
	T5_5T0 += alt(MUL)
	S+=T5_5T0>=T5_5T0_in

	T5_5T0_mem0 = S.Task('T5_5T0_mem0', length=1, delay_cost=1)
	T5_5T0_mem0 += alt(ADD_mem)
	S += (C2_0*ADD[0])-1<T5_5T0_mem0*ADD_mem[0]
	S += (C2_0*ADD[1])-1<T5_5T0_mem0*ADD_mem[1]
	S += (C2_0*ADD[2])-1<T5_5T0_mem0*ADD_mem[2]
	S += (C2_0*ADD[3])-1<T5_5T0_mem0*ADD_mem[3]
	S += T5_5T0_mem0<=T5_5T0

	T5_5T0_mem1 = S.Task('T5_5T0_mem1', length=1, delay_cost=1)
	T5_5T0_mem1 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T5_5T0_mem1*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T5_5T0_mem1*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T5_5T0_mem1*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T5_5T0_mem1*ADD_mem[3]
	S += T5_5T0_mem1<=T5_5T0

	T5_5T1_in = S.Task('T5_5T1_in', length=1, delay_cost=1)
	T5_5T1_in += alt(MUL_in)
	T5_5T1 = S.Task('T5_5T1', length=7, delay_cost=1)
	T5_5T1 += alt(MUL)
	S+=T5_5T1>=T5_5T1_in

	T5_5T1_mem0 = S.Task('T5_5T1_mem0', length=1, delay_cost=1)
	T5_5T1_mem0 += alt(ADD_mem)
	S += (C2_1*ADD[0])-1<T5_5T1_mem0*ADD_mem[0]
	S += (C2_1*ADD[1])-1<T5_5T1_mem0*ADD_mem[1]
	S += (C2_1*ADD[2])-1<T5_5T1_mem0*ADD_mem[2]
	S += (C2_1*ADD[3])-1<T5_5T1_mem0*ADD_mem[3]
	S += T5_5T1_mem0<=T5_5T1

	T5_5T1_mem1 = S.Task('T5_5T1_mem1', length=1, delay_cost=1)
	T5_5T1_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T5_5T1_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T5_5T1_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T5_5T1_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T5_5T1_mem1*ADD_mem[3]
	S += T5_5T1_mem1<=T5_5T1

	T5_5T3 = S.Task('T5_5T3', length=1, delay_cost=1)
	T5_5T3 += alt(ADD)

	T5_5T3_mem0 = S.Task('T5_5T3_mem0', length=1, delay_cost=1)
	T5_5T3_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T5_5T3_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T5_5T3_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T5_5T3_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T5_5T3_mem0*ADD_mem[3]
	S += T5_5T3_mem0<=T5_5T3

	T5_5T3_mem1 = S.Task('T5_5T3_mem1', length=1, delay_cost=1)
	T5_5T3_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T5_5T3_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T5_5T3_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T5_5T3_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T5_5T3_mem1*ADD_mem[3]
	S += T5_5T3_mem1<=T5_5T3

	T4_9T3 = S.Task('T4_9T3', length=1, delay_cost=1)
	T4_9T3 += alt(ADD)

	T4_9T3_mem0 = S.Task('T4_9T3_mem0', length=1, delay_cost=1)
	T4_9T3_mem0 += alt(ADD_mem)
	S += (C1_0*ADD[0])-1<T4_9T3_mem0*ADD_mem[0]
	S += (C1_0*ADD[1])-1<T4_9T3_mem0*ADD_mem[1]
	S += (C1_0*ADD[2])-1<T4_9T3_mem0*ADD_mem[2]
	S += (C1_0*ADD[3])-1<T4_9T3_mem0*ADD_mem[3]
	S += T4_9T3_mem0<=T4_9T3

	T4_9T3_mem1 = S.Task('T4_9T3_mem1', length=1, delay_cost=1)
	T4_9T3_mem1 += alt(ADD_mem)
	S += (C1_1*ADD[0])-1<T4_9T3_mem1*ADD_mem[0]
	S += (C1_1*ADD[1])-1<T4_9T3_mem1*ADD_mem[1]
	S += (C1_1*ADD[2])-1<T4_9T3_mem1*ADD_mem[2]
	S += (C1_1*ADD[3])-1<T4_9T3_mem1*ADD_mem[3]
	S += T4_9T3_mem1<=T4_9T3

	T5_6T3 = S.Task('T5_6T3', length=1, delay_cost=1)
	T5_6T3 += alt(ADD)

	T5_6T3_mem0 = S.Task('T5_6T3_mem0', length=1, delay_cost=1)
	T5_6T3_mem0 += alt(ADD_mem)
	S += (C0_0*ADD[0])-1<T5_6T3_mem0*ADD_mem[0]
	S += (C0_0*ADD[1])-1<T5_6T3_mem0*ADD_mem[1]
	S += (C0_0*ADD[2])-1<T5_6T3_mem0*ADD_mem[2]
	S += (C0_0*ADD[3])-1<T5_6T3_mem0*ADD_mem[3]
	S += T5_6T3_mem0<=T5_6T3

	T5_6T3_mem1 = S.Task('T5_6T3_mem1', length=1, delay_cost=1)
	T5_6T3_mem1 += alt(ADD_mem)
	S += (C0_1*ADD[0])-1<T5_6T3_mem1*ADD_mem[0]
	S += (C0_1*ADD[1])-1<T5_6T3_mem1*ADD_mem[1]
	S += (C0_1*ADD[2])-1<T5_6T3_mem1*ADD_mem[2]
	S += (C0_1*ADD[3])-1<T5_6T3_mem1*ADD_mem[3]
	S += T5_6T3_mem1<=T5_6T3

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "inv_mul1_add4/inv_mul1_add4_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_inv_mul1_add4_3(0, 0)