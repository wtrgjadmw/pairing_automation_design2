from pyschedule import Scenario, solvers, plotters, alt

def solve_frob_mul1_add4_1(ConstStep, ExpStep):
	horizon = 117
	S=Scenario("frob_mul1_add4_1",horizon = horizon)

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
	NEW_F01T0_in = S.Task('NEW_F01T0_in', length=1, delay_cost=1)
	S += NEW_F01T0_in >= 2
	NEW_F01T0_in += MUL_in[0]

	NEW_F01T0_mem0 = S.Task('NEW_F01T0_mem0', length=1, delay_cost=1)
	S += NEW_F01T0_mem0 >= 2
	NEW_F01T0_mem0 += INPUT_mem_r

	NEW_F01T0_mem1 = S.Task('NEW_F01T0_mem1', length=1, delay_cost=1)
	S += NEW_F01T0_mem1 >= 2
	NEW_F01T0_mem1 += INPUT_mem_r

	NEW_F01T0 = S.Task('NEW_F01T0', length=7, delay_cost=1)
	S += NEW_F01T0 >= 3
	NEW_F01T0 += MUL[0]

	NEW_F01T1_in = S.Task('NEW_F01T1_in', length=1, delay_cost=1)
	S += NEW_F01T1_in >= 3
	NEW_F01T1_in += MUL_in[0]

	NEW_F01T1_mem0 = S.Task('NEW_F01T1_mem0', length=1, delay_cost=1)
	S += NEW_F01T1_mem0 >= 3
	NEW_F01T1_mem0 += INPUT_mem_r

	NEW_F01T1_mem1 = S.Task('NEW_F01T1_mem1', length=1, delay_cost=1)
	S += NEW_F01T1_mem1 >= 3
	NEW_F01T1_mem1 += INPUT_mem_r

	NEW_F01T1 = S.Task('NEW_F01T1', length=7, delay_cost=1)
	S += NEW_F01T1 >= 4
	NEW_F01T1 += MUL[0]

	NEW_F11T0_in = S.Task('NEW_F11T0_in', length=1, delay_cost=1)
	S += NEW_F11T0_in >= 5
	NEW_F11T0_in += MUL_in[0]

	NEW_F11T0_mem0 = S.Task('NEW_F11T0_mem0', length=1, delay_cost=1)
	S += NEW_F11T0_mem0 >= 5
	NEW_F11T0_mem0 += INPUT_mem_r

	NEW_F11T0_mem1 = S.Task('NEW_F11T0_mem1', length=1, delay_cost=1)
	S += NEW_F11T0_mem1 >= 5
	NEW_F11T0_mem1 += INPUT_mem_r

	NEW_F11T0 = S.Task('NEW_F11T0', length=7, delay_cost=1)
	S += NEW_F11T0 >= 6
	NEW_F11T0 += MUL[0]

	NEW_F21T0_in = S.Task('NEW_F21T0_in', length=1, delay_cost=1)
	S += NEW_F21T0_in >= 7
	NEW_F21T0_in += MUL_in[0]

	NEW_F21T0_mem0 = S.Task('NEW_F21T0_mem0', length=1, delay_cost=1)
	S += NEW_F21T0_mem0 >= 7
	NEW_F21T0_mem0 += INPUT_mem_r

	NEW_F21T0_mem1 = S.Task('NEW_F21T0_mem1', length=1, delay_cost=1)
	S += NEW_F21T0_mem1 >= 7
	NEW_F21T0_mem1 += INPUT_mem_r

	NEW_F20T1_in = S.Task('NEW_F20T1_in', length=1, delay_cost=1)
	S += NEW_F20T1_in >= 8
	NEW_F20T1_in += MUL_in[0]

	NEW_F20T1_mem0 = S.Task('NEW_F20T1_mem0', length=1, delay_cost=1)
	S += NEW_F20T1_mem0 >= 8
	NEW_F20T1_mem0 += INPUT_mem_r

	NEW_F20T1_mem1 = S.Task('NEW_F20T1_mem1', length=1, delay_cost=1)
	S += NEW_F20T1_mem1 >= 8
	NEW_F20T1_mem1 += INPUT_mem_r

	NEW_F21T0 = S.Task('NEW_F21T0', length=7, delay_cost=1)
	S += NEW_F21T0 >= 8
	NEW_F21T0 += MUL[0]

	NEW_F20T0_in = S.Task('NEW_F20T0_in', length=1, delay_cost=1)
	S += NEW_F20T0_in >= 9
	NEW_F20T0_in += MUL_in[0]

	NEW_F20T0_mem0 = S.Task('NEW_F20T0_mem0', length=1, delay_cost=1)
	S += NEW_F20T0_mem0 >= 9
	NEW_F20T0_mem0 += INPUT_mem_r

	NEW_F20T0_mem1 = S.Task('NEW_F20T0_mem1', length=1, delay_cost=1)
	S += NEW_F20T0_mem1 >= 9
	NEW_F20T0_mem1 += INPUT_mem_r

	NEW_F20T1 = S.Task('NEW_F20T1', length=7, delay_cost=1)
	S += NEW_F20T1 >= 9
	NEW_F20T1 += MUL[0]

	NEW_F010_mem0 = S.Task('NEW_F010_mem0', length=1, delay_cost=1)
	S += NEW_F010_mem0 >= 10
	NEW_F010_mem0 += MUL_mem[0]

	NEW_F010_mem1 = S.Task('NEW_F010_mem1', length=1, delay_cost=1)
	S += NEW_F010_mem1 >= 10
	NEW_F010_mem1 += MUL_mem[0]

	NEW_F20T0 = S.Task('NEW_F20T0', length=7, delay_cost=1)
	S += NEW_F20T0 >= 10
	NEW_F20T0 += MUL[0]

	NEW_F010 = S.Task('NEW_F010', length=1, delay_cost=1)
	S += NEW_F010 >= 11
	NEW_F010 += ADD[2]

	NEW_F010_w = S.Task('NEW_F010_w', length=1, delay_cost=1)
	S += NEW_F010_w >= 11
	NEW_F010_w += INPUT_mem_w

	NEW_F01T5_mem0 = S.Task('NEW_F01T5_mem0', length=1, delay_cost=1)
	S += NEW_F01T5_mem0 >= 11
	NEW_F01T5_mem0 += MUL_mem[0]

	NEW_F01T5_mem1 = S.Task('NEW_F01T5_mem1', length=1, delay_cost=1)
	S += NEW_F01T5_mem1 >= 11
	NEW_F01T5_mem1 += MUL_mem[0]

	NEW_F20T3_mem0 = S.Task('NEW_F20T3_mem0', length=1, delay_cost=1)
	S += NEW_F20T3_mem0 >= 11
	NEW_F20T3_mem0 += INPUT_mem_r

	NEW_F20T3_mem1 = S.Task('NEW_F20T3_mem1', length=1, delay_cost=1)
	S += NEW_F20T3_mem1 >= 11
	NEW_F20T3_mem1 += INPUT_mem_r

	NEW_F01T5 = S.Task('NEW_F01T5', length=1, delay_cost=1)
	S += NEW_F01T5 >= 12
	NEW_F01T5 += ADD[0]

	NEW_F110_mem0 = S.Task('NEW_F110_mem0', length=1, delay_cost=1)
	S += NEW_F110_mem0 >= 12
	NEW_F110_mem0 += MUL_mem[0]

	NEW_F110_mem1 = S.Task('NEW_F110_mem1', length=1, delay_cost=1)
	S += NEW_F110_mem1 >= 12
	NEW_F110_mem1 += MUL_mem[0]

	NEW_F20T3 = S.Task('NEW_F20T3', length=1, delay_cost=1)
	S += NEW_F20T3 >= 12
	NEW_F20T3 += ADD[1]

	NEW_F20T4_in = S.Task('NEW_F20T4_in', length=1, delay_cost=1)
	S += NEW_F20T4_in >= 12
	NEW_F20T4_in += MUL_in[0]

	NEW_F20T4_mem0 = S.Task('NEW_F20T4_mem0', length=1, delay_cost=1)
	S += NEW_F20T4_mem0 >= 12
	NEW_F20T4_mem0 += ADD_mem[1]

	NEW_F20T4_mem1 = S.Task('NEW_F20T4_mem1', length=1, delay_cost=1)
	S += NEW_F20T4_mem1 >= 12
	NEW_F20T4_mem1 += ADD_mem[1]

	NEW_F21T2_mem0 = S.Task('NEW_F21T2_mem0', length=1, delay_cost=1)
	S += NEW_F21T2_mem0 >= 12
	NEW_F21T2_mem0 += INPUT_mem_r

	NEW_F21T2_mem1 = S.Task('NEW_F21T2_mem1', length=1, delay_cost=1)
	S += NEW_F21T2_mem1 >= 12
	NEW_F21T2_mem1 += INPUT_mem_r

	NEW_F110 = S.Task('NEW_F110', length=1, delay_cost=1)
	S += NEW_F110 >= 13
	NEW_F110 += ADD[0]

	NEW_F110_w = S.Task('NEW_F110_w', length=1, delay_cost=1)
	S += NEW_F110_w >= 13
	NEW_F110_w += INPUT_mem_w

	NEW_F11T5_mem0 = S.Task('NEW_F11T5_mem0', length=1, delay_cost=1)
	S += NEW_F11T5_mem0 >= 13
	NEW_F11T5_mem0 += MUL_mem[0]

	NEW_F11T5_mem1 = S.Task('NEW_F11T5_mem1', length=1, delay_cost=1)
	S += NEW_F11T5_mem1 >= 13
	NEW_F11T5_mem1 += MUL_mem[0]

	NEW_F20T4 = S.Task('NEW_F20T4', length=7, delay_cost=1)
	S += NEW_F20T4 >= 13
	NEW_F20T4 += MUL[0]

	NEW_F21T2 = S.Task('NEW_F21T2', length=1, delay_cost=1)
	S += NEW_F21T2 >= 13
	NEW_F21T2 += ADD[2]

	NEW_F21T3_mem0 = S.Task('NEW_F21T3_mem0', length=1, delay_cost=1)
	S += NEW_F21T3_mem0 >= 13
	NEW_F21T3_mem0 += INPUT_mem_r

	NEW_F21T3_mem1 = S.Task('NEW_F21T3_mem1', length=1, delay_cost=1)
	S += NEW_F21T3_mem1 >= 13
	NEW_F21T3_mem1 += INPUT_mem_r

	NEW_F11T3_mem0 = S.Task('NEW_F11T3_mem0', length=1, delay_cost=1)
	S += NEW_F11T3_mem0 >= 14
	NEW_F11T3_mem0 += INPUT_mem_r

	NEW_F11T3_mem1 = S.Task('NEW_F11T3_mem1', length=1, delay_cost=1)
	S += NEW_F11T3_mem1 >= 14
	NEW_F11T3_mem1 += INPUT_mem_r

	NEW_F11T5 = S.Task('NEW_F11T5', length=1, delay_cost=1)
	S += NEW_F11T5 >= 14
	NEW_F11T5 += ADD[2]

	NEW_F210_mem0 = S.Task('NEW_F210_mem0', length=1, delay_cost=1)
	S += NEW_F210_mem0 >= 14
	NEW_F210_mem0 += MUL_mem[0]

	NEW_F210_mem1 = S.Task('NEW_F210_mem1', length=1, delay_cost=1)
	S += NEW_F210_mem1 >= 14
	NEW_F210_mem1 += MUL_mem[0]

	NEW_F21T3 = S.Task('NEW_F21T3', length=1, delay_cost=1)
	S += NEW_F21T3 >= 14
	NEW_F21T3 += ADD[0]

	NEW_F21T4_in = S.Task('NEW_F21T4_in', length=1, delay_cost=1)
	S += NEW_F21T4_in >= 14
	NEW_F21T4_in += MUL_in[0]

	NEW_F21T4_mem0 = S.Task('NEW_F21T4_mem0', length=1, delay_cost=1)
	S += NEW_F21T4_mem0 >= 14
	NEW_F21T4_mem0 += ADD_mem[2]

	NEW_F21T4_mem1 = S.Task('NEW_F21T4_mem1', length=1, delay_cost=1)
	S += NEW_F21T4_mem1 >= 14
	NEW_F21T4_mem1 += ADD_mem[0]

	NEW_F11T2_mem0 = S.Task('NEW_F11T2_mem0', length=1, delay_cost=1)
	S += NEW_F11T2_mem0 >= 15
	NEW_F11T2_mem0 += INPUT_mem_r

	NEW_F11T2_mem1 = S.Task('NEW_F11T2_mem1', length=1, delay_cost=1)
	S += NEW_F11T2_mem1 >= 15
	NEW_F11T2_mem1 += INPUT_mem_r

	NEW_F11T3 = S.Task('NEW_F11T3', length=1, delay_cost=1)
	S += NEW_F11T3 >= 15
	NEW_F11T3 += ADD[2]

	NEW_F210 = S.Task('NEW_F210', length=1, delay_cost=1)
	S += NEW_F210 >= 15
	NEW_F210 += ADD[0]

	NEW_F210_w = S.Task('NEW_F210_w', length=1, delay_cost=1)
	S += NEW_F210_w >= 15
	NEW_F210_w += INPUT_mem_w

	NEW_F21T4 = S.Task('NEW_F21T4', length=7, delay_cost=1)
	S += NEW_F21T4 >= 15
	NEW_F21T4 += MUL[0]

	NEW_F21T5_mem0 = S.Task('NEW_F21T5_mem0', length=1, delay_cost=1)
	S += NEW_F21T5_mem0 >= 15
	NEW_F21T5_mem0 += MUL_mem[0]

	NEW_F21T5_mem1 = S.Task('NEW_F21T5_mem1', length=1, delay_cost=1)
	S += NEW_F21T5_mem1 >= 15
	NEW_F21T5_mem1 += MUL_mem[0]

	NEW_F10T3_mem0 = S.Task('NEW_F10T3_mem0', length=1, delay_cost=1)
	S += NEW_F10T3_mem0 >= 16
	NEW_F10T3_mem0 += INPUT_mem_r

	NEW_F10T3_mem1 = S.Task('NEW_F10T3_mem1', length=1, delay_cost=1)
	S += NEW_F10T3_mem1 >= 16
	NEW_F10T3_mem1 += INPUT_mem_r

	NEW_F11T2 = S.Task('NEW_F11T2', length=1, delay_cost=1)
	S += NEW_F11T2 >= 16
	NEW_F11T2 += ADD[3]

	NEW_F11T4_in = S.Task('NEW_F11T4_in', length=1, delay_cost=1)
	S += NEW_F11T4_in >= 16
	NEW_F11T4_in += MUL_in[0]

	NEW_F11T4_mem0 = S.Task('NEW_F11T4_mem0', length=1, delay_cost=1)
	S += NEW_F11T4_mem0 >= 16
	NEW_F11T4_mem0 += ADD_mem[3]

	NEW_F11T4_mem1 = S.Task('NEW_F11T4_mem1', length=1, delay_cost=1)
	S += NEW_F11T4_mem1 >= 16
	NEW_F11T4_mem1 += ADD_mem[2]

	NEW_F200_mem0 = S.Task('NEW_F200_mem0', length=1, delay_cost=1)
	S += NEW_F200_mem0 >= 16
	NEW_F200_mem0 += MUL_mem[0]

	NEW_F200_mem1 = S.Task('NEW_F200_mem1', length=1, delay_cost=1)
	S += NEW_F200_mem1 >= 16
	NEW_F200_mem1 += MUL_mem[0]

	NEW_F21T5 = S.Task('NEW_F21T5', length=1, delay_cost=1)
	S += NEW_F21T5 >= 16
	NEW_F21T5 += ADD[0]

	NEW_F10T2_mem0 = S.Task('NEW_F10T2_mem0', length=1, delay_cost=1)
	S += NEW_F10T2_mem0 >= 17
	NEW_F10T2_mem0 += INPUT_mem_r

	NEW_F10T2_mem1 = S.Task('NEW_F10T2_mem1', length=1, delay_cost=1)
	S += NEW_F10T2_mem1 >= 17
	NEW_F10T2_mem1 += INPUT_mem_r

	NEW_F10T3 = S.Task('NEW_F10T3', length=1, delay_cost=1)
	S += NEW_F10T3 >= 17
	NEW_F10T3 += ADD[0]

	NEW_F11T4 = S.Task('NEW_F11T4', length=7, delay_cost=1)
	S += NEW_F11T4 >= 17
	NEW_F11T4 += MUL[0]

	NEW_F200 = S.Task('NEW_F200', length=1, delay_cost=1)
	S += NEW_F200 >= 17
	NEW_F200 += ADD[2]

	NEW_F200_w = S.Task('NEW_F200_w', length=1, delay_cost=1)
	S += NEW_F200_w >= 17
	NEW_F200_w += INPUT_mem_w

	NEW_F20T5_mem0 = S.Task('NEW_F20T5_mem0', length=1, delay_cost=1)
	S += NEW_F20T5_mem0 >= 17
	NEW_F20T5_mem0 += MUL_mem[0]

	NEW_F20T5_mem1 = S.Task('NEW_F20T5_mem1', length=1, delay_cost=1)
	S += NEW_F20T5_mem1 >= 17
	NEW_F20T5_mem1 += MUL_mem[0]

	NEW_F10T2 = S.Task('NEW_F10T2', length=1, delay_cost=1)
	S += NEW_F10T2 >= 18
	NEW_F10T2 += ADD[2]

	NEW_F10T4_in = S.Task('NEW_F10T4_in', length=1, delay_cost=1)
	S += NEW_F10T4_in >= 18
	NEW_F10T4_in += MUL_in[0]

	NEW_F10T4_mem0 = S.Task('NEW_F10T4_mem0', length=1, delay_cost=1)
	S += NEW_F10T4_mem0 >= 18
	NEW_F10T4_mem0 += ADD_mem[2]

	NEW_F10T4_mem1 = S.Task('NEW_F10T4_mem1', length=1, delay_cost=1)
	S += NEW_F10T4_mem1 >= 18
	NEW_F10T4_mem1 += ADD_mem[0]

	NEW_F20T5 = S.Task('NEW_F20T5', length=1, delay_cost=1)
	S += NEW_F20T5 >= 18
	NEW_F20T5 += ADD[3]

	NEW_F01T3_mem0 = S.Task('NEW_F01T3_mem0', length=1, delay_cost=1)
	S += NEW_F01T3_mem0 >= 19
	NEW_F01T3_mem0 += INPUT_mem_r

	NEW_F01T3_mem1 = S.Task('NEW_F01T3_mem1', length=1, delay_cost=1)
	S += NEW_F01T3_mem1 >= 19
	NEW_F01T3_mem1 += INPUT_mem_r

	NEW_F10T4 = S.Task('NEW_F10T4', length=7, delay_cost=1)
	S += NEW_F10T4 >= 19
	NEW_F10T4 += MUL[0]

	NEW_F201_mem0 = S.Task('NEW_F201_mem0', length=1, delay_cost=1)
	S += NEW_F201_mem0 >= 19
	NEW_F201_mem0 += MUL_mem[0]

	NEW_F201_mem1 = S.Task('NEW_F201_mem1', length=1, delay_cost=1)
	S += NEW_F201_mem1 >= 19
	NEW_F201_mem1 += ADD_mem[3]

	NEW_F001_mem0 = S.Task('NEW_F001_mem0', length=1, delay_cost=1)
	S += NEW_F001_mem0 >= 20
	NEW_F001_mem0 += INPUT_mem_r

	NEW_F001_mem1 = S.Task('NEW_F001_mem1', length=1, delay_cost=1)
	S += NEW_F001_mem1 >= 20
	NEW_F001_mem1 += INPUT_mem_r

	NEW_F01T3 = S.Task('NEW_F01T3', length=1, delay_cost=1)
	S += NEW_F01T3 >= 20
	NEW_F01T3 += ADD[1]

	NEW_F201 = S.Task('NEW_F201', length=1, delay_cost=1)
	S += NEW_F201 >= 20
	NEW_F201 += ADD[0]

	NEW_F201_w = S.Task('NEW_F201_w', length=1, delay_cost=1)
	S += NEW_F201_w >= 20
	NEW_F201_w += INPUT_mem_w

	NEW_F000_mem0 = S.Task('NEW_F000_mem0', length=1, delay_cost=1)
	S += NEW_F000_mem0 >= 21
	NEW_F000_mem0 += INPUT_mem_r

	NEW_F000_mem1 = S.Task('NEW_F000_mem1', length=1, delay_cost=1)
	S += NEW_F000_mem1 >= 21
	NEW_F000_mem1 += INPUT_mem_r

	NEW_F001 = S.Task('NEW_F001', length=1, delay_cost=1)
	S += NEW_F001 >= 21
	NEW_F001 += ADD[3]

	NEW_F001_w = S.Task('NEW_F001_w', length=1, delay_cost=1)
	S += NEW_F001_w >= 21
	NEW_F001_w += INPUT_mem_w

	NEW_F211_mem0 = S.Task('NEW_F211_mem0', length=1, delay_cost=1)
	S += NEW_F211_mem0 >= 21
	NEW_F211_mem0 += MUL_mem[0]

	NEW_F211_mem1 = S.Task('NEW_F211_mem1', length=1, delay_cost=1)
	S += NEW_F211_mem1 >= 21
	NEW_F211_mem1 += ADD_mem[0]

	NEW_F000 = S.Task('NEW_F000', length=1, delay_cost=1)
	S += NEW_F000 >= 22
	NEW_F000 += ADD[0]

	NEW_F000_w = S.Task('NEW_F000_w', length=1, delay_cost=1)
	S += NEW_F000_w >= 22
	NEW_F000_w += INPUT_mem_w

	NEW_F211 = S.Task('NEW_F211', length=1, delay_cost=1)
	S += NEW_F211 >= 22
	NEW_F211 += ADD[3]

	NEW_F211_w = S.Task('NEW_F211_w', length=1, delay_cost=1)
	S += NEW_F211_w >= 22
	NEW_F211_w += INPUT_mem_w

	NEW_F111_mem0 = S.Task('NEW_F111_mem0', length=1, delay_cost=1)
	S += NEW_F111_mem0 >= 23
	NEW_F111_mem0 += MUL_mem[0]

	NEW_F111_mem1 = S.Task('NEW_F111_mem1', length=1, delay_cost=1)
	S += NEW_F111_mem1 >= 23
	NEW_F111_mem1 += ADD_mem[2]

	NEW_F111 = S.Task('NEW_F111', length=1, delay_cost=1)
	S += NEW_F111 >= 24
	NEW_F111 += ADD[3]

	NEW_F111_w = S.Task('NEW_F111_w', length=1, delay_cost=1)
	S += NEW_F111_w >= 24
	NEW_F111_w += INPUT_mem_w

	NEW_F101_mem0 = S.Task('NEW_F101_mem0', length=1, delay_cost=1)
	S += NEW_F101_mem0 >= 25
	NEW_F101_mem0 += MUL_mem[0]

	NEW_F101_mem1 = S.Task('NEW_F101_mem1', length=1, delay_cost=1)
	S += NEW_F101_mem1 >= 25
	NEW_F101_mem1 += ADD_mem[1]

	NEW_F101 = S.Task('NEW_F101', length=1, delay_cost=1)
	S += NEW_F101 >= 26
	NEW_F101 += ADD[2]

	NEW_F101_w = S.Task('NEW_F101_w', length=1, delay_cost=1)
	S += NEW_F101_w >= 26
	NEW_F101_w += INPUT_mem_w


	# new tasks
	NEW_F10T0_in = S.Task('NEW_F10T0_in', length=1, delay_cost=1)
	NEW_F10T0_in += alt(MUL_in)
	NEW_F10T0 = S.Task('NEW_F10T0', length=7, delay_cost=1)
	NEW_F10T0 += alt(MUL)
	S+=NEW_F10T0>=NEW_F10T0_in

	NEW_F10T0_mem0 = S.Task('NEW_F10T0_mem0', length=1, delay_cost=1)
	NEW_F10T0_mem0 += INPUT_mem_r
	S += NEW_F10T0_mem0<=NEW_F10T0

	NEW_F10T0_mem1 = S.Task('NEW_F10T0_mem1', length=1, delay_cost=1)
	NEW_F10T0_mem1 += INPUT_mem_r
	S += NEW_F10T0_mem1<=NEW_F10T0

	NEW_F10T1_in = S.Task('NEW_F10T1_in', length=1, delay_cost=1)
	NEW_F10T1_in += alt(MUL_in)
	NEW_F10T1 = S.Task('NEW_F10T1', length=7, delay_cost=1)
	NEW_F10T1 += alt(MUL)
	S+=NEW_F10T1>=NEW_F10T1_in

	NEW_F10T1_mem0 = S.Task('NEW_F10T1_mem0', length=1, delay_cost=1)
	NEW_F10T1_mem0 += INPUT_mem_r
	S += NEW_F10T1_mem0<=NEW_F10T1

	NEW_F10T1_mem1 = S.Task('NEW_F10T1_mem1', length=1, delay_cost=1)
	NEW_F10T1_mem1 += INPUT_mem_r
	S += NEW_F10T1_mem1<=NEW_F10T1

	NEW_F20T2 = S.Task('NEW_F20T2', length=1, delay_cost=1)
	NEW_F20T2 += alt(ADD)

	NEW_F20T2_mem0 = S.Task('NEW_F20T2_mem0', length=1, delay_cost=1)
	NEW_F20T2_mem0 += INPUT_mem_r
	S += NEW_F20T2_mem0<=NEW_F20T2

	NEW_F20T2_mem1 = S.Task('NEW_F20T2_mem1', length=1, delay_cost=1)
	NEW_F20T2_mem1 += INPUT_mem_r
	S += NEW_F20T2_mem1<=NEW_F20T2

	NEW_F01T2 = S.Task('NEW_F01T2', length=1, delay_cost=1)
	NEW_F01T2 += alt(ADD)

	NEW_F01T2_mem0 = S.Task('NEW_F01T2_mem0', length=1, delay_cost=1)
	NEW_F01T2_mem0 += INPUT_mem_r
	S += NEW_F01T2_mem0<=NEW_F01T2

	NEW_F01T2_mem1 = S.Task('NEW_F01T2_mem1', length=1, delay_cost=1)
	NEW_F01T2_mem1 += INPUT_mem_r
	S += NEW_F01T2_mem1<=NEW_F01T2

	NEW_F11T1_in = S.Task('NEW_F11T1_in', length=1, delay_cost=1)
	NEW_F11T1_in += alt(MUL_in)
	NEW_F11T1 = S.Task('NEW_F11T1', length=7, delay_cost=1)
	NEW_F11T1 += alt(MUL)
	S+=NEW_F11T1>=NEW_F11T1_in

	NEW_F11T1_mem0 = S.Task('NEW_F11T1_mem0', length=1, delay_cost=1)
	NEW_F11T1_mem0 += INPUT_mem_r
	S += NEW_F11T1_mem0<=NEW_F11T1

	NEW_F11T1_mem1 = S.Task('NEW_F11T1_mem1', length=1, delay_cost=1)
	NEW_F11T1_mem1 += INPUT_mem_r
	S += NEW_F11T1_mem1<=NEW_F11T1

	NEW_F21T1_in = S.Task('NEW_F21T1_in', length=1, delay_cost=1)
	NEW_F21T1_in += alt(MUL_in)
	NEW_F21T1 = S.Task('NEW_F21T1', length=7, delay_cost=1)
	NEW_F21T1 += alt(MUL)
	S+=NEW_F21T1>=NEW_F21T1_in

	NEW_F21T1_mem0 = S.Task('NEW_F21T1_mem0', length=1, delay_cost=1)
	NEW_F21T1_mem0 += INPUT_mem_r
	S += NEW_F21T1_mem0<=NEW_F21T1

	NEW_F21T1_mem1 = S.Task('NEW_F21T1_mem1', length=1, delay_cost=1)
	NEW_F21T1_mem1 += INPUT_mem_r
	S += NEW_F21T1_mem1<=NEW_F21T1

	NEW_F10T5 = S.Task('NEW_F10T5', length=1, delay_cost=1)
	NEW_F10T5 += alt(ADD)

	NEW_F10T5_mem0 = S.Task('NEW_F10T5_mem0', length=1, delay_cost=1)
	NEW_F10T5_mem0 += alt(MUL_mem)
	S += (NEW_F10T0*MUL[0])-1<NEW_F10T5_mem0*MUL_mem[0]
	S += NEW_F10T5_mem0<=NEW_F10T5

	NEW_F10T5_mem1 = S.Task('NEW_F10T5_mem1', length=1, delay_cost=1)
	NEW_F10T5_mem1 += alt(MUL_mem)
	S += (NEW_F10T1*MUL[0])-1<NEW_F10T5_mem1*MUL_mem[0]
	S += NEW_F10T5_mem1<=NEW_F10T5

	NEW_F01T4_in = S.Task('NEW_F01T4_in', length=1, delay_cost=1)
	NEW_F01T4_in += alt(MUL_in)
	NEW_F01T4 = S.Task('NEW_F01T4', length=7, delay_cost=1)
	NEW_F01T4 += alt(MUL)
	S+=NEW_F01T4>=NEW_F01T4_in

	NEW_F01T4_mem0 = S.Task('NEW_F01T4_mem0', length=1, delay_cost=1)
	NEW_F01T4_mem0 += alt(ADD_mem)
	S += (NEW_F01T2*ADD[0])-1<NEW_F01T4_mem0*ADD_mem[0]
	S += (NEW_F01T2*ADD[1])-1<NEW_F01T4_mem0*ADD_mem[1]
	S += (NEW_F01T2*ADD[2])-1<NEW_F01T4_mem0*ADD_mem[2]
	S += (NEW_F01T2*ADD[3])-1<NEW_F01T4_mem0*ADD_mem[3]
	S += NEW_F01T4_mem0<=NEW_F01T4

	NEW_F01T4_mem1 = S.Task('NEW_F01T4_mem1', length=1, delay_cost=1)
	NEW_F01T4_mem1 += ADD_mem[1]
	S += NEW_F01T3<NEW_F01T4_mem1
	S += NEW_F01T4_mem1<=NEW_F01T4

	NEW_F100 = S.Task('NEW_F100', length=1, delay_cost=1)
	NEW_F100 += alt(ADD)

	NEW_F100_mem0 = S.Task('NEW_F100_mem0', length=1, delay_cost=1)
	NEW_F100_mem0 += alt(MUL_mem)
	S += (NEW_F10T0*MUL[0])-1<NEW_F100_mem0*MUL_mem[0]
	S += NEW_F100_mem0<=NEW_F100

	NEW_F100_mem1 = S.Task('NEW_F100_mem1', length=1, delay_cost=1)
	NEW_F100_mem1 += alt(MUL_mem)
	S += (NEW_F10T1*MUL[0])-1<NEW_F100_mem1*MUL_mem[0]
	S += NEW_F100_mem1<=NEW_F100

	NEW_F100_w = S.Task('NEW_F100_w', length=1, delay_cost=1)
	NEW_F100_w += alt(INPUT_mem_w)
	S += 22 < NEW_F100_w
	S += NEW_F100-1 <= NEW_F100_w

	NEW_F011 = S.Task('NEW_F011', length=1, delay_cost=1)
	NEW_F011 += alt(ADD)

	NEW_F011_mem0 = S.Task('NEW_F011_mem0', length=1, delay_cost=1)
	NEW_F011_mem0 += alt(MUL_mem)
	S += (NEW_F01T4*MUL[0])-1<NEW_F011_mem0*MUL_mem[0]
	S += NEW_F011_mem0<=NEW_F011

	NEW_F011_mem1 = S.Task('NEW_F011_mem1', length=1, delay_cost=1)
	NEW_F011_mem1 += ADD_mem[0]
	S += NEW_F01T5<NEW_F011_mem1
	S += NEW_F011_mem1<=NEW_F011

	NEW_F011_w = S.Task('NEW_F011_w', length=1, delay_cost=1)
	NEW_F011_w += alt(INPUT_mem_w)
	S += 22 < NEW_F011_w
	S += NEW_F011-1 <= NEW_F011_w

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "frob_mul1_add4/frob_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_frob_mul1_add4_1(0, 0)