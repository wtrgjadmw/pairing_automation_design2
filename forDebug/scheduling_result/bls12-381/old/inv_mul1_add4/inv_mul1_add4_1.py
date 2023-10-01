from pyschedule import Scenario, solvers, plotters, alt

def solve_inv_mul1_add4_1(ConstStep, ExpStep):
	horizon = 127
	S=Scenario("inv_mul1_add4_1",horizon = horizon)

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

	T1_3T2_mem0 = S.Task('T1_3T2_mem0', length=1, delay_cost=1)
	S += T1_3T2_mem0 >= 9
	T1_3T2_mem0 += INPUT_mem_r

	T1_3T2_mem1 = S.Task('T1_3T2_mem1', length=1, delay_cost=1)
	S += T1_3T2_mem1 >= 9
	T1_3T2_mem1 += INPUT_mem_r

	T1_4T2 = S.Task('T1_4T2', length=1, delay_cost=1)
	S += T1_4T2 >= 9
	T1_4T2 += ADD[0]

	NEW_A121_mem0 = S.Task('NEW_A121_mem0', length=1, delay_cost=1)
	S += NEW_A121_mem0 >= 10
	NEW_A121_mem0 += INPUT_mem_r

	NEW_A121_mem1 = S.Task('NEW_A121_mem1', length=1, delay_cost=1)
	S += NEW_A121_mem1 >= 10
	NEW_A121_mem1 += INPUT_mem_r

	T1_3T2 = S.Task('T1_3T2', length=1, delay_cost=1)
	S += T1_3T2 >= 10
	T1_3T2 += ADD[2]

	NEW_A010_mem0 = S.Task('NEW_A010_mem0', length=1, delay_cost=1)
	S += NEW_A010_mem0 >= 11
	NEW_A010_mem0 += INPUT_mem_r

	NEW_A010_mem1 = S.Task('NEW_A010_mem1', length=1, delay_cost=1)
	S += NEW_A010_mem1 >= 11
	NEW_A010_mem1 += INPUT_mem_r

	NEW_A121 = S.Task('NEW_A121', length=1, delay_cost=1)
	S += NEW_A121 >= 11
	NEW_A121 += ADD[1]

	NEW_A000_mem0 = S.Task('NEW_A000_mem0', length=1, delay_cost=1)
	S += NEW_A000_mem0 >= 12
	NEW_A000_mem0 += INPUT_mem_r

	NEW_A000_mem1 = S.Task('NEW_A000_mem1', length=1, delay_cost=1)
	S += NEW_A000_mem1 >= 12
	NEW_A000_mem1 += INPUT_mem_r

	NEW_A010 = S.Task('NEW_A010', length=1, delay_cost=1)
	S += NEW_A010 >= 12
	NEW_A010 += ADD[0]

	NEW_A000 = S.Task('NEW_A000', length=1, delay_cost=1)
	S += NEW_A000 >= 13
	NEW_A000 += ADD[0]

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	S += T2T0_mem0 >= 13
	T2T0_mem0 += INPUT_mem_r

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	S += T2T0_mem1 >= 13
	T2T0_mem1 += INPUT_mem_r

	NEW_A111_mem0 = S.Task('NEW_A111_mem0', length=1, delay_cost=1)
	S += NEW_A111_mem0 >= 14
	NEW_A111_mem0 += INPUT_mem_r

	NEW_A111_mem1 = S.Task('NEW_A111_mem1', length=1, delay_cost=1)
	S += NEW_A111_mem1 >= 14
	NEW_A111_mem1 += INPUT_mem_r

	T2T0 = S.Task('T2T0', length=1, delay_cost=1)
	S += T2T0 >= 14
	T2T0 += ADD[0]

	NEW_A110_mem0 = S.Task('NEW_A110_mem0', length=1, delay_cost=1)
	S += NEW_A110_mem0 >= 15
	NEW_A110_mem0 += INPUT_mem_r

	NEW_A110_mem1 = S.Task('NEW_A110_mem1', length=1, delay_cost=1)
	S += NEW_A110_mem1 >= 15
	NEW_A110_mem1 += INPUT_mem_r

	NEW_A111 = S.Task('NEW_A111', length=1, delay_cost=1)
	S += NEW_A111 >= 15
	NEW_A111 += ADD[2]

	NEW_A110 = S.Task('NEW_A110', length=1, delay_cost=1)
	S += NEW_A110 >= 16
	NEW_A110 += ADD[1]

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	S += T0T0_mem0 >= 16
	T0T0_mem0 += INPUT_mem_r

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	S += T0T0_mem1 >= 16
	T0T0_mem1 += INPUT_mem_r

	NEW_A101_mem0 = S.Task('NEW_A101_mem0', length=1, delay_cost=1)
	S += NEW_A101_mem0 >= 17
	NEW_A101_mem0 += INPUT_mem_r

	NEW_A101_mem1 = S.Task('NEW_A101_mem1', length=1, delay_cost=1)
	S += NEW_A101_mem1 >= 17
	NEW_A101_mem1 += INPUT_mem_r

	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	S += T0T0 >= 17
	T0T0 += ADD[1]

	NEW_A101 = S.Task('NEW_A101', length=1, delay_cost=1)
	S += NEW_A101 >= 18
	NEW_A101 += ADD[0]

	T0_3T2_mem0 = S.Task('T0_3T2_mem0', length=1, delay_cost=1)
	S += T0_3T2_mem0 >= 18
	T0_3T2_mem0 += INPUT_mem_r

	T0_3T2_mem1 = S.Task('T0_3T2_mem1', length=1, delay_cost=1)
	S += T0_3T2_mem1 >= 18
	T0_3T2_mem1 += INPUT_mem_r

	T0_3T2 = S.Task('T0_3T2', length=1, delay_cost=1)
	S += T0_3T2 >= 19
	T0_3T2 += ADD[0]

	T0_4T2_mem0 = S.Task('T0_4T2_mem0', length=1, delay_cost=1)
	S += T0_4T2_mem0 >= 19
	T0_4T2_mem0 += INPUT_mem_r

	T0_4T2_mem1 = S.Task('T0_4T2_mem1', length=1, delay_cost=1)
	S += T0_4T2_mem1 >= 19
	T0_4T2_mem1 += INPUT_mem_r

	T0_4T2 = S.Task('T0_4T2', length=1, delay_cost=1)
	S += T0_4T2 >= 20
	T0_4T2 += ADD[0]

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	S += T1T1_mem0 >= 20
	T1T1_mem0 += INPUT_mem_r

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	S += T1T1_mem1 >= 20
	T1T1_mem1 += INPUT_mem_r

	NEW_A100_mem0 = S.Task('NEW_A100_mem0', length=1, delay_cost=1)
	S += NEW_A100_mem0 >= 21
	NEW_A100_mem0 += INPUT_mem_r

	NEW_A100_mem1 = S.Task('NEW_A100_mem1', length=1, delay_cost=1)
	S += NEW_A100_mem1 >= 21
	NEW_A100_mem1 += INPUT_mem_r

	T1T1 = S.Task('T1T1', length=1, delay_cost=1)
	S += T1T1 >= 21
	T1T1 += ADD[0]

	NEW_A100 = S.Task('NEW_A100', length=1, delay_cost=1)
	S += NEW_A100 >= 22
	NEW_A100 += ADD[0]

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	S += T2T1_mem0 >= 22
	T2T1_mem0 += INPUT_mem_r

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	S += T2T1_mem1 >= 22
	T2T1_mem1 += INPUT_mem_r

	T2T1 = S.Task('T2T1', length=1, delay_cost=1)
	S += T2T1 >= 23
	T2T1 += ADD[0]

	T2_6T2_mem0 = S.Task('T2_6T2_mem0', length=1, delay_cost=1)
	S += T2_6T2_mem0 >= 23
	T2_6T2_mem0 += INPUT_mem_r

	T2_6T2_mem1 = S.Task('T2_6T2_mem1', length=1, delay_cost=1)
	S += T2_6T2_mem1 >= 23
	T2_6T2_mem1 += INPUT_mem_r

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	S += T1T0_mem0 >= 24
	T1T0_mem0 += INPUT_mem_r

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	S += T1T0_mem1 >= 24
	T1T0_mem1 += INPUT_mem_r

	T2_6T2 = S.Task('T2_6T2', length=1, delay_cost=1)
	S += T2_6T2 >= 24
	T2_6T2 += ADD[0]

	NEW_A001_mem0 = S.Task('NEW_A001_mem0', length=1, delay_cost=1)
	S += NEW_A001_mem0 >= 25
	NEW_A001_mem0 += INPUT_mem_r

	NEW_A001_mem1 = S.Task('NEW_A001_mem1', length=1, delay_cost=1)
	S += NEW_A001_mem1 >= 25
	NEW_A001_mem1 += INPUT_mem_r

	T1T0 = S.Task('T1T0', length=1, delay_cost=1)
	S += T1T0 >= 25
	T1T0 += ADD[1]

	NEW_A001 = S.Task('NEW_A001', length=1, delay_cost=1)
	S += NEW_A001 >= 26
	NEW_A001 += ADD[0]

	T2_1T1_mem0 = S.Task('T2_1T1_mem0', length=1, delay_cost=1)
	S += T2_1T1_mem0 >= 26
	T2_1T1_mem0 += INPUT_mem_r

	T2_1T1_mem1 = S.Task('T2_1T1_mem1', length=1, delay_cost=1)
	S += T2_1T1_mem1 >= 26
	T2_1T1_mem1 += INPUT_mem_r

	NEW_A120_mem0 = S.Task('NEW_A120_mem0', length=1, delay_cost=1)
	S += NEW_A120_mem0 >= 27
	NEW_A120_mem0 += INPUT_mem_r

	NEW_A120_mem1 = S.Task('NEW_A120_mem1', length=1, delay_cost=1)
	S += NEW_A120_mem1 >= 27
	NEW_A120_mem1 += INPUT_mem_r

	T2_1T1 = S.Task('T2_1T1', length=1, delay_cost=1)
	S += T2_1T1 >= 27
	T2_1T1 += ADD[2]

	NEW_A120 = S.Task('NEW_A120', length=1, delay_cost=1)
	S += NEW_A120 >= 28
	NEW_A120 += ADD[0]

	T2_1T0_mem0 = S.Task('T2_1T0_mem0', length=1, delay_cost=1)
	S += T2_1T0_mem0 >= 28
	T2_1T0_mem0 += INPUT_mem_r

	T2_1T0_mem1 = S.Task('T2_1T0_mem1', length=1, delay_cost=1)
	S += T2_1T0_mem1 >= 28
	T2_1T0_mem1 += INPUT_mem_r

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	S += T1_T1_mem0 >= 29
	T1_T1_mem0 += INPUT_mem_r

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	S += T1_T1_mem1 >= 29
	T1_T1_mem1 += INPUT_mem_r

	T2_1T0 = S.Task('T2_1T0', length=1, delay_cost=1)
	S += T2_1T0 >= 29
	T2_1T0 += ADD[0]

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	S += T1_T0_mem0 >= 30
	T1_T0_mem0 += INPUT_mem_r

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	S += T1_T0_mem1 >= 30
	T1_T0_mem1 += INPUT_mem_r

	T1_T1 = S.Task('T1_T1', length=1, delay_cost=1)
	S += T1_T1 >= 30
	T1_T1 += ADD[1]

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	S += T0T1_mem0 >= 31
	T0T1_mem0 += INPUT_mem_r

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	S += T0T1_mem1 >= 31
	T0T1_mem1 += INPUT_mem_r

	T1_T0 = S.Task('T1_T0', length=1, delay_cost=1)
	S += T1_T0 >= 31
	T1_T0 += ADD[2]

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	S += T0T1 >= 32
	T0T1 += ADD[2]

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	S += T0_T1_mem0 >= 32
	T0_T1_mem0 += INPUT_mem_r

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	S += T0_T1_mem1 >= 32
	T0_T1_mem1 += INPUT_mem_r

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	S += T0_T0_mem0 >= 33
	T0_T0_mem0 += INPUT_mem_r

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	S += T0_T0_mem1 >= 33
	T0_T0_mem1 += INPUT_mem_r

	T0_T1 = S.Task('T0_T1', length=1, delay_cost=1)
	S += T0_T1 >= 33
	T0_T1 += ADD[1]

	NEW_A021_mem0 = S.Task('NEW_A021_mem0', length=1, delay_cost=1)
	S += NEW_A021_mem0 >= 34
	NEW_A021_mem0 += INPUT_mem_r

	NEW_A021_mem1 = S.Task('NEW_A021_mem1', length=1, delay_cost=1)
	S += NEW_A021_mem1 >= 34
	NEW_A021_mem1 += INPUT_mem_r

	T0_T0 = S.Task('T0_T0', length=1, delay_cost=1)
	S += T0_T0 >= 34
	T0_T0 += ADD[2]

	NEW_A020_mem0 = S.Task('NEW_A020_mem0', length=1, delay_cost=1)
	S += NEW_A020_mem0 >= 35
	NEW_A020_mem0 += INPUT_mem_r

	NEW_A020_mem1 = S.Task('NEW_A020_mem1', length=1, delay_cost=1)
	S += NEW_A020_mem1 >= 35
	NEW_A020_mem1 += INPUT_mem_r

	NEW_A021 = S.Task('NEW_A021', length=1, delay_cost=1)
	S += NEW_A021 >= 35
	NEW_A021 += ADD[0]

	NEW_A020 = S.Task('NEW_A020', length=1, delay_cost=1)
	S += NEW_A020 >= 36
	NEW_A020 += ADD[2]


	# new tasks
	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	T00_in += alt(MUL_in)
	T00 = S.Task('T00', length=7, delay_cost=1)
	T00 += alt(MUL)
	S+=T00>=T00_in

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	T00_mem0 += ADD_mem[1]
	S += 17<T00_mem0
	S += T00_mem0<=T00

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	T00_mem1 += ADD_mem[2]
	S += 32<T00_mem1
	S += T00_mem1<=T00

	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += MUL_mem[0]
	S += 12<T01_mem0
	S += T01_mem0<=T01

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	T10_in += alt(MUL_in)
	T10 = S.Task('T10', length=7, delay_cost=1)
	T10 += alt(MUL)
	S+=T10>=T10_in

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += ADD_mem[1]
	S += 25<T10_mem0
	S += T10_mem0<=T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += ADD_mem[0]
	S += 21<T10_mem1
	S += T10_mem1<=T10

	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(ADD)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MUL_mem[0]
	S += 9<T11_mem0
	S += T11_mem0<=T11

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	T20_in += alt(MUL_in)
	T20 = S.Task('T20', length=7, delay_cost=1)
	T20 += alt(MUL)
	S+=T20>=T20_in

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += ADD_mem[0]
	S += 14<T20_mem0
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += ADD_mem[0]
	S += 23<T20_mem1
	S += T20_mem1<=T20

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(ADD)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += MUL_mem[0]
	S += 8<T21_mem0
	S += T21_mem0<=T21

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	T3T0 += alt(ADD)

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	T3T0_mem0 += ADD_mem[0]
	S += 13<T3T0_mem0
	S += T3T0_mem0<=T3T0

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	T3T0_mem1 += ADD_mem[0]
	S += 26<T3T0_mem1
	S += T3T0_mem1<=T3T0

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	T3T1 += alt(ADD)

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	T3T1_mem0 += ADD_mem[0]
	S += 13<T3T1_mem0
	S += T3T1_mem0<=T3T1

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	T3T1_mem1 += ADD_mem[0]
	S += 26<T3T1_mem1
	S += T3T1_mem1<=T3T1

	T3T2_in = S.Task('T3T2_in', length=1, delay_cost=1)
	T3T2_in += alt(MUL_in)
	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	T3T2 += alt(MUL)
	S+=T3T2>=T3T2_in

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	T3T2_mem0 += ADD_mem[0]
	S += 13<T3T2_mem0
	S += T3T2_mem0<=T3T2

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	T3T2_mem1 += ADD_mem[0]
	S += 26<T3T2_mem1
	S += T3T2_mem1<=T3T2

	T4_T0 = S.Task('T4_T0', length=1, delay_cost=1)
	T4_T0 += alt(ADD)

	T4_T0_mem0 = S.Task('T4_T0_mem0', length=1, delay_cost=1)
	T4_T0_mem0 += ADD_mem[0]
	S += 12<T4_T0_mem0
	S += T4_T0_mem0<=T4_T0

	T4_T0_mem1 = S.Task('T4_T0_mem1', length=1, delay_cost=1)
	T4_T0_mem1 += ADD_mem[0]
	S += 8<T4_T0_mem1
	S += T4_T0_mem1<=T4_T0

	T4_T1 = S.Task('T4_T1', length=1, delay_cost=1)
	T4_T1 += alt(ADD)

	T4_T1_mem0 = S.Task('T4_T1_mem0', length=1, delay_cost=1)
	T4_T1_mem0 += ADD_mem[0]
	S += 12<T4_T1_mem0
	S += T4_T1_mem0<=T4_T1

	T4_T1_mem1 = S.Task('T4_T1_mem1', length=1, delay_cost=1)
	T4_T1_mem1 += ADD_mem[0]
	S += 8<T4_T1_mem1
	S += T4_T1_mem1<=T4_T1

	T4_T2_in = S.Task('T4_T2_in', length=1, delay_cost=1)
	T4_T2_in += alt(MUL_in)
	T4_T2 = S.Task('T4_T2', length=7, delay_cost=1)
	T4_T2 += alt(MUL)
	S+=T4_T2>=T4_T2_in

	T4_T2_mem0 = S.Task('T4_T2_mem0', length=1, delay_cost=1)
	T4_T2_mem0 += ADD_mem[0]
	S += 12<T4_T2_mem0
	S += T4_T2_mem0<=T4_T2

	T4_T2_mem1 = S.Task('T4_T2_mem1', length=1, delay_cost=1)
	T4_T2_mem1 += ADD_mem[0]
	S += 8<T4_T2_mem1
	S += T4_T2_mem1<=T4_T2

	T5_T0 = S.Task('T5_T0', length=1, delay_cost=1)
	T5_T0 += alt(ADD)

	T5_T0_mem0 = S.Task('T5_T0_mem0', length=1, delay_cost=1)
	T5_T0_mem0 += ADD_mem[2]
	S += 36<T5_T0_mem0
	S += T5_T0_mem0<=T5_T0

	T5_T0_mem1 = S.Task('T5_T0_mem1', length=1, delay_cost=1)
	T5_T0_mem1 += ADD_mem[0]
	S += 35<T5_T0_mem1
	S += T5_T0_mem1<=T5_T0

	T5_T1 = S.Task('T5_T1', length=1, delay_cost=1)
	T5_T1 += alt(ADD)

	T5_T1_mem0 = S.Task('T5_T1_mem0', length=1, delay_cost=1)
	T5_T1_mem0 += ADD_mem[2]
	S += 36<T5_T1_mem0
	S += T5_T1_mem0<=T5_T1

	T5_T1_mem1 = S.Task('T5_T1_mem1', length=1, delay_cost=1)
	T5_T1_mem1 += ADD_mem[0]
	S += 35<T5_T1_mem1
	S += T5_T1_mem1<=T5_T1

	T5_T2_in = S.Task('T5_T2_in', length=1, delay_cost=1)
	T5_T2_in += alt(MUL_in)
	T5_T2 = S.Task('T5_T2', length=7, delay_cost=1)
	T5_T2 += alt(MUL)
	S+=T5_T2>=T5_T2_in

	T5_T2_mem0 = S.Task('T5_T2_mem0', length=1, delay_cost=1)
	T5_T2_mem0 += ADD_mem[2]
	S += 36<T5_T2_mem0
	S += T5_T2_mem0<=T5_T2

	T5_T2_mem1 = S.Task('T5_T2_mem1', length=1, delay_cost=1)
	T5_T2_mem1 += ADD_mem[0]
	S += 35<T5_T2_mem1
	S += T5_T2_mem1<=T5_T2

	T0_0_in = S.Task('T0_0_in', length=1, delay_cost=1)
	T0_0_in += alt(MUL_in)
	T0_0 = S.Task('T0_0', length=7, delay_cost=1)
	T0_0 += alt(MUL)
	S+=T0_0>=T0_0_in

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	T0_0_mem0 += ADD_mem[2]
	S += 34<T0_0_mem0
	S += T0_0_mem0<=T0_0

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	T0_0_mem1 += ADD_mem[1]
	S += 33<T0_0_mem1
	S += T0_0_mem1<=T0_0

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	T0_1 += alt(ADD)

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	T0_1_mem0 += MUL_mem[0]
	S += 11<T0_1_mem0
	S += T0_1_mem0<=T0_1

	T1_0_in = S.Task('T1_0_in', length=1, delay_cost=1)
	T1_0_in += alt(MUL_in)
	T1_0 = S.Task('T1_0', length=7, delay_cost=1)
	T1_0 += alt(MUL)
	S+=T1_0>=T1_0_in

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	T1_0_mem0 += ADD_mem[2]
	S += 31<T1_0_mem0
	S += T1_0_mem0<=T1_0

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	T1_0_mem1 += ADD_mem[1]
	S += 30<T1_0_mem1
	S += T1_0_mem1<=T1_0

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	T1_1 += alt(ADD)

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	T1_1_mem0 += MUL_mem[0]
	S += 10<T1_1_mem0
	S += T1_1_mem0<=T1_1

	T2_10_in = S.Task('T2_10_in', length=1, delay_cost=1)
	T2_10_in += alt(MUL_in)
	T2_10 = S.Task('T2_10', length=7, delay_cost=1)
	T2_10 += alt(MUL)
	S+=T2_10>=T2_10_in

	T2_10_mem0 = S.Task('T2_10_mem0', length=1, delay_cost=1)
	T2_10_mem0 += ADD_mem[0]
	S += 29<T2_10_mem0
	S += T2_10_mem0<=T2_10

	T2_10_mem1 = S.Task('T2_10_mem1', length=1, delay_cost=1)
	T2_10_mem1 += ADD_mem[2]
	S += 27<T2_10_mem1
	S += T2_10_mem1<=T2_10

	T2_11 = S.Task('T2_11', length=1, delay_cost=1)
	T2_11 += alt(ADD)

	T2_11_mem0 = S.Task('T2_11_mem0', length=1, delay_cost=1)
	T2_11_mem0 += MUL_mem[0]
	S += 7<T2_11_mem0
	S += T2_11_mem0<=T2_11

	T3_1T0 = S.Task('T3_1T0', length=1, delay_cost=1)
	T3_1T0 += alt(ADD)

	T3_1T0_mem0 = S.Task('T3_1T0_mem0', length=1, delay_cost=1)
	T3_1T0_mem0 += ADD_mem[0]
	S += 22<T3_1T0_mem0
	S += T3_1T0_mem0<=T3_1T0

	T3_1T0_mem1 = S.Task('T3_1T0_mem1', length=1, delay_cost=1)
	T3_1T0_mem1 += ADD_mem[0]
	S += 18<T3_1T0_mem1
	S += T3_1T0_mem1<=T3_1T0

	T3_1T1 = S.Task('T3_1T1', length=1, delay_cost=1)
	T3_1T1 += alt(ADD)

	T3_1T1_mem0 = S.Task('T3_1T1_mem0', length=1, delay_cost=1)
	T3_1T1_mem0 += ADD_mem[0]
	S += 22<T3_1T1_mem0
	S += T3_1T1_mem0<=T3_1T1

	T3_1T1_mem1 = S.Task('T3_1T1_mem1', length=1, delay_cost=1)
	T3_1T1_mem1 += ADD_mem[0]
	S += 18<T3_1T1_mem1
	S += T3_1T1_mem1<=T3_1T1

	T3_1T2_in = S.Task('T3_1T2_in', length=1, delay_cost=1)
	T3_1T2_in += alt(MUL_in)
	T3_1T2 = S.Task('T3_1T2', length=7, delay_cost=1)
	T3_1T2 += alt(MUL)
	S+=T3_1T2>=T3_1T2_in

	T3_1T2_mem0 = S.Task('T3_1T2_mem0', length=1, delay_cost=1)
	T3_1T2_mem0 += ADD_mem[0]
	S += 22<T3_1T2_mem0
	S += T3_1T2_mem0<=T3_1T2

	T3_1T2_mem1 = S.Task('T3_1T2_mem1', length=1, delay_cost=1)
	T3_1T2_mem1 += ADD_mem[0]
	S += 18<T3_1T2_mem1
	S += T3_1T2_mem1<=T3_1T2

	T4_4T0 = S.Task('T4_4T0', length=1, delay_cost=1)
	T4_4T0 += alt(ADD)

	T4_4T0_mem0 = S.Task('T4_4T0_mem0', length=1, delay_cost=1)
	T4_4T0_mem0 += ADD_mem[1]
	S += 16<T4_4T0_mem0
	S += T4_4T0_mem0<=T4_4T0

	T4_4T0_mem1 = S.Task('T4_4T0_mem1', length=1, delay_cost=1)
	T4_4T0_mem1 += ADD_mem[2]
	S += 15<T4_4T0_mem1
	S += T4_4T0_mem1<=T4_4T0

	T4_4T1 = S.Task('T4_4T1', length=1, delay_cost=1)
	T4_4T1 += alt(ADD)

	T4_4T1_mem0 = S.Task('T4_4T1_mem0', length=1, delay_cost=1)
	T4_4T1_mem0 += ADD_mem[1]
	S += 16<T4_4T1_mem0
	S += T4_4T1_mem0<=T4_4T1

	T4_4T1_mem1 = S.Task('T4_4T1_mem1', length=1, delay_cost=1)
	T4_4T1_mem1 += ADD_mem[2]
	S += 15<T4_4T1_mem1
	S += T4_4T1_mem1<=T4_4T1

	T4_4T2_in = S.Task('T4_4T2_in', length=1, delay_cost=1)
	T4_4T2_in += alt(MUL_in)
	T4_4T2 = S.Task('T4_4T2', length=7, delay_cost=1)
	T4_4T2 += alt(MUL)
	S+=T4_4T2>=T4_4T2_in

	T4_4T2_mem0 = S.Task('T4_4T2_mem0', length=1, delay_cost=1)
	T4_4T2_mem0 += ADD_mem[1]
	S += 16<T4_4T2_mem0
	S += T4_4T2_mem0<=T4_4T2

	T4_4T2_mem1 = S.Task('T4_4T2_mem1', length=1, delay_cost=1)
	T4_4T2_mem1 += ADD_mem[2]
	S += 15<T4_4T2_mem1
	S += T4_4T2_mem1<=T4_4T2

	T5_3T0 = S.Task('T5_3T0', length=1, delay_cost=1)
	T5_3T0 += alt(ADD)

	T5_3T0_mem0 = S.Task('T5_3T0_mem0', length=1, delay_cost=1)
	T5_3T0_mem0 += ADD_mem[0]
	S += 28<T5_3T0_mem0
	S += T5_3T0_mem0<=T5_3T0

	T5_3T0_mem1 = S.Task('T5_3T0_mem1', length=1, delay_cost=1)
	T5_3T0_mem1 += ADD_mem[1]
	S += 11<T5_3T0_mem1
	S += T5_3T0_mem1<=T5_3T0

	T5_3T1 = S.Task('T5_3T1', length=1, delay_cost=1)
	T5_3T1 += alt(ADD)

	T5_3T1_mem0 = S.Task('T5_3T1_mem0', length=1, delay_cost=1)
	T5_3T1_mem0 += ADD_mem[0]
	S += 28<T5_3T1_mem0
	S += T5_3T1_mem0<=T5_3T1

	T5_3T1_mem1 = S.Task('T5_3T1_mem1', length=1, delay_cost=1)
	T5_3T1_mem1 += ADD_mem[1]
	S += 11<T5_3T1_mem1
	S += T5_3T1_mem1<=T5_3T1

	T5_3T2_in = S.Task('T5_3T2_in', length=1, delay_cost=1)
	T5_3T2_in += alt(MUL_in)
	T5_3T2 = S.Task('T5_3T2', length=7, delay_cost=1)
	T5_3T2 += alt(MUL)
	S+=T5_3T2>=T5_3T2_in

	T5_3T2_mem0 = S.Task('T5_3T2_mem0', length=1, delay_cost=1)
	T5_3T2_mem0 += ADD_mem[0]
	S += 28<T5_3T2_mem0
	S += T5_3T2_mem0<=T5_3T2

	T5_3T2_mem1 = S.Task('T5_3T2_mem1', length=1, delay_cost=1)
	T5_3T2_mem1 += ADD_mem[1]
	S += 11<T5_3T2_mem1
	S += T5_3T2_mem1<=T5_3T2

	T3_5T2 = S.Task('T3_5T2', length=1, delay_cost=1)
	T3_5T2 += alt(ADD)

	T3_5T2_mem0 = S.Task('T3_5T2_mem0', length=1, delay_cost=1)
	T3_5T2_mem0 += ADD_mem[0]
	S += 13<T3_5T2_mem0
	S += T3_5T2_mem0<=T3_5T2

	T3_5T2_mem1 = S.Task('T3_5T2_mem1', length=1, delay_cost=1)
	T3_5T2_mem1 += ADD_mem[0]
	S += 26<T3_5T2_mem1
	S += T3_5T2_mem1<=T3_5T2

	T4_15T2 = S.Task('T4_15T2', length=1, delay_cost=1)
	T4_15T2 += alt(ADD)

	T4_15T2_mem0 = S.Task('T4_15T2_mem0', length=1, delay_cost=1)
	T4_15T2_mem0 += ADD_mem[0]
	S += 12<T4_15T2_mem0
	S += T4_15T2_mem0<=T4_15T2

	T4_15T2_mem1 = S.Task('T4_15T2_mem1', length=1, delay_cost=1)
	T4_15T2_mem1 += ADD_mem[0]
	S += 8<T4_15T2_mem1
	S += T4_15T2_mem1<=T4_15T2

	T5_8T2 = S.Task('T5_8T2', length=1, delay_cost=1)
	T5_8T2 += alt(ADD)

	T5_8T2_mem0 = S.Task('T5_8T2_mem0', length=1, delay_cost=1)
	T5_8T2_mem0 += ADD_mem[2]
	S += 36<T5_8T2_mem0
	S += T5_8T2_mem0<=T5_8T2

	T5_8T2_mem1 = S.Task('T5_8T2_mem1', length=1, delay_cost=1)
	T5_8T2_mem1 += ADD_mem[0]
	S += 35<T5_8T2_mem1
	S += T5_8T2_mem1<=T5_8T2

	T3_7T2 = S.Task('T3_7T2', length=1, delay_cost=1)
	T3_7T2 += alt(ADD)

	T3_7T2_mem0 = S.Task('T3_7T2_mem0', length=1, delay_cost=1)
	T3_7T2_mem0 += ADD_mem[0]
	S += 22<T3_7T2_mem0
	S += T3_7T2_mem0<=T3_7T2

	T3_7T2_mem1 = S.Task('T3_7T2_mem1', length=1, delay_cost=1)
	T3_7T2_mem1 += ADD_mem[0]
	S += 18<T3_7T2_mem1
	S += T3_7T2_mem1<=T3_7T2

	T4_19T2 = S.Task('T4_19T2', length=1, delay_cost=1)
	T4_19T2 += alt(ADD)

	T4_19T2_mem0 = S.Task('T4_19T2_mem0', length=1, delay_cost=1)
	T4_19T2_mem0 += ADD_mem[1]
	S += 16<T4_19T2_mem0
	S += T4_19T2_mem0<=T4_19T2

	T4_19T2_mem1 = S.Task('T4_19T2_mem1', length=1, delay_cost=1)
	T4_19T2_mem1 += ADD_mem[2]
	S += 15<T4_19T2_mem1
	S += T4_19T2_mem1<=T4_19T2

	T5_11T2 = S.Task('T5_11T2', length=1, delay_cost=1)
	T5_11T2 += alt(ADD)

	T5_11T2_mem0 = S.Task('T5_11T2_mem0', length=1, delay_cost=1)
	T5_11T2_mem0 += ADD_mem[0]
	S += 28<T5_11T2_mem0
	S += T5_11T2_mem0<=T5_11T2

	T5_11T2_mem1 = S.Task('T5_11T2_mem1', length=1, delay_cost=1)
	T5_11T2_mem1 += ADD_mem[1]
	S += 11<T5_11T2_mem1
	S += T5_11T2_mem1<=T5_11T2

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "inv_mul1_add4/inv_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_inv_mul1_add4_1(0, 0)