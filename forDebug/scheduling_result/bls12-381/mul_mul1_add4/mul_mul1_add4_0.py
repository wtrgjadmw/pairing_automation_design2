from pyschedule import Scenario, solvers, plotters, alt

def solve_mul_mul1_add4_0(ConstStep, ExpStep):
	horizon = 110
	S=Scenario("mul_mul1_add4_0",horizon = horizon)

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

	# new tasks
	T0T0_in = S.Task('T0T0_in', length=1, delay_cost=1)
	T0T0_in += alt(MUL_in)
	T0T0 = S.Task('T0T0', length=7, delay_cost=1)
	T0T0 += alt(MUL)
	S+=T0T0>=T0T0_in

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	T0T0_mem0 += INPUT_mem_r
	S += T0T0_mem0<=T0T0

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	T0T0_mem1 += INPUT_mem_r
	S += T0T0_mem1<=T0T0

	T0T1_in = S.Task('T0T1_in', length=1, delay_cost=1)
	T0T1_in += alt(MUL_in)
	T0T1 = S.Task('T0T1', length=7, delay_cost=1)
	T0T1 += alt(MUL)
	S+=T0T1>=T0T1_in

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	T0T1_mem0 += INPUT_mem_r
	S += T0T1_mem0<=T0T1

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	T0T1_mem1 += INPUT_mem_r
	S += T0T1_mem1<=T0T1

	T0T2 = S.Task('T0T2', length=1, delay_cost=1)
	T0T2 += alt(ADD)

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	T0T2_mem0 += INPUT_mem_r
	S += T0T2_mem0<=T0T2

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	T0T2_mem1 += INPUT_mem_r
	S += T0T2_mem1<=T0T2

	T0T3 = S.Task('T0T3', length=1, delay_cost=1)
	T0T3 += alt(ADD)

	T0T3_mem0 = S.Task('T0T3_mem0', length=1, delay_cost=1)
	T0T3_mem0 += INPUT_mem_r
	S += T0T3_mem0<=T0T3

	T0T3_mem1 = S.Task('T0T3_mem1', length=1, delay_cost=1)
	T0T3_mem1 += INPUT_mem_r
	S += T0T3_mem1<=T0T3

	T1T0_in = S.Task('T1T0_in', length=1, delay_cost=1)
	T1T0_in += alt(MUL_in)
	T1T0 = S.Task('T1T0', length=7, delay_cost=1)
	T1T0 += alt(MUL)
	S+=T1T0>=T1T0_in

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	T1T0_mem0 += INPUT_mem_r
	S += T1T0_mem0<=T1T0

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	T1T0_mem1 += INPUT_mem_r
	S += T1T0_mem1<=T1T0

	T1T1_in = S.Task('T1T1_in', length=1, delay_cost=1)
	T1T1_in += alt(MUL_in)
	T1T1 = S.Task('T1T1', length=7, delay_cost=1)
	T1T1 += alt(MUL)
	S+=T1T1>=T1T1_in

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	T1T1_mem0 += INPUT_mem_r
	S += T1T1_mem0<=T1T1

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	T1T1_mem1 += INPUT_mem_r
	S += T1T1_mem1<=T1T1

	T1T2 = S.Task('T1T2', length=1, delay_cost=1)
	T1T2 += alt(ADD)

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	T1T2_mem0 += INPUT_mem_r
	S += T1T2_mem0<=T1T2

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	T1T2_mem1 += INPUT_mem_r
	S += T1T2_mem1<=T1T2

	T1T3 = S.Task('T1T3', length=1, delay_cost=1)
	T1T3 += alt(ADD)

	T1T3_mem0 = S.Task('T1T3_mem0', length=1, delay_cost=1)
	T1T3_mem0 += INPUT_mem_r
	S += T1T3_mem0<=T1T3

	T1T3_mem1 = S.Task('T1T3_mem1', length=1, delay_cost=1)
	T1T3_mem1 += INPUT_mem_r
	S += T1T3_mem1<=T1T3

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	T2T0_in += alt(MUL_in)
	T2T0 = S.Task('T2T0', length=7, delay_cost=1)
	T2T0 += alt(MUL)
	S+=T2T0>=T2T0_in

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	T2T0_mem0 += INPUT_mem_r
	S += T2T0_mem0<=T2T0

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	T2T0_mem1 += INPUT_mem_r
	S += T2T0_mem1<=T2T0

	T2T1_in = S.Task('T2T1_in', length=1, delay_cost=1)
	T2T1_in += alt(MUL_in)
	T2T1 = S.Task('T2T1', length=7, delay_cost=1)
	T2T1 += alt(MUL)
	S+=T2T1>=T2T1_in

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	T2T1_mem0 += INPUT_mem_r
	S += T2T1_mem0<=T2T1

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	T2T1_mem1 += INPUT_mem_r
	S += T2T1_mem1<=T2T1

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	T2T2 += alt(ADD)

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	T2T2_mem0 += INPUT_mem_r
	S += T2T2_mem0<=T2T2

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	T2T2_mem1 += INPUT_mem_r
	S += T2T2_mem1<=T2T2

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	T2T3 += alt(ADD)

	T2T3_mem0 = S.Task('T2T3_mem0', length=1, delay_cost=1)
	T2T3_mem0 += INPUT_mem_r
	S += T2T3_mem0<=T2T3

	T2T3_mem1 = S.Task('T2T3_mem1', length=1, delay_cost=1)
	T2T3_mem1 += INPUT_mem_r
	S += T2T3_mem1<=T2T3

	T30 = S.Task('T30', length=1, delay_cost=1)
	T30 += alt(ADD)

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += INPUT_mem_r
	S += T30_mem0<=T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += INPUT_mem_r
	S += T30_mem1<=T30

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += INPUT_mem_r
	S += T31_mem0<=T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += INPUT_mem_r
	S += T31_mem1<=T31

	T40 = S.Task('T40', length=1, delay_cost=1)
	T40 += alt(ADD)

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += INPUT_mem_r
	S += T40_mem0<=T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += INPUT_mem_r
	S += T40_mem1<=T40

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += INPUT_mem_r
	S += T41_mem0<=T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += INPUT_mem_r
	S += T41_mem1<=T41

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	T4_0 += alt(ADD)

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	T4_0_mem0 += INPUT_mem_r
	S += T4_0_mem0<=T4_0

	T4_0_mem1 = S.Task('T4_0_mem1', length=1, delay_cost=1)
	T4_0_mem1 += INPUT_mem_r
	S += T4_0_mem1<=T4_0

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	T4_1 += alt(ADD)

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	T4_1_mem0 += INPUT_mem_r
	S += T4_1_mem0<=T4_1

	T4_1_mem1 = S.Task('T4_1_mem1', length=1, delay_cost=1)
	T4_1_mem1 += INPUT_mem_r
	S += T4_1_mem1<=T4_1

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(ADD)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += INPUT_mem_r
	S += T50_mem0<=T50

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	T50_mem1 += INPUT_mem_r
	S += T50_mem1<=T50

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(ADD)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += INPUT_mem_r
	S += T51_mem0<=T51

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	T51_mem1 += INPUT_mem_r
	S += T51_mem1<=T51

	T5_0 = S.Task('T5_0', length=1, delay_cost=1)
	T5_0 += alt(ADD)

	T5_0_mem0 = S.Task('T5_0_mem0', length=1, delay_cost=1)
	T5_0_mem0 += INPUT_mem_r
	S += T5_0_mem0<=T5_0

	T5_0_mem1 = S.Task('T5_0_mem1', length=1, delay_cost=1)
	T5_0_mem1 += INPUT_mem_r
	S += T5_0_mem1<=T5_0

	T5_1 = S.Task('T5_1', length=1, delay_cost=1)
	T5_1 += alt(ADD)

	T5_1_mem0 = S.Task('T5_1_mem0', length=1, delay_cost=1)
	T5_1_mem0 += INPUT_mem_r
	S += T5_1_mem0<=T5_1

	T5_1_mem1 = S.Task('T5_1_mem1', length=1, delay_cost=1)
	T5_1_mem1 += INPUT_mem_r
	S += T5_1_mem1<=T5_1

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += INPUT_mem_r
	S += T60_mem0<=T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += INPUT_mem_r
	S += T60_mem1<=T60

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += INPUT_mem_r
	S += T61_mem0<=T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += INPUT_mem_r
	S += T61_mem1<=T61

	T0_T0_in = S.Task('T0_T0_in', length=1, delay_cost=1)
	T0_T0_in += alt(MUL_in)
	T0_T0 = S.Task('T0_T0', length=7, delay_cost=1)
	T0_T0 += alt(MUL)
	S+=T0_T0>=T0_T0_in

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	T0_T0_mem0 += INPUT_mem_r
	S += T0_T0_mem0<=T0_T0

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	T0_T0_mem1 += INPUT_mem_r
	S += T0_T0_mem1<=T0_T0

	T0_T1_in = S.Task('T0_T1_in', length=1, delay_cost=1)
	T0_T1_in += alt(MUL_in)
	T0_T1 = S.Task('T0_T1', length=7, delay_cost=1)
	T0_T1 += alt(MUL)
	S+=T0_T1>=T0_T1_in

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	T0_T1_mem0 += INPUT_mem_r
	S += T0_T1_mem0<=T0_T1

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	T0_T1_mem1 += INPUT_mem_r
	S += T0_T1_mem1<=T0_T1

	T0_T2 = S.Task('T0_T2', length=1, delay_cost=1)
	T0_T2 += alt(ADD)

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	T0_T2_mem0 += INPUT_mem_r
	S += T0_T2_mem0<=T0_T2

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	T0_T2_mem1 += INPUT_mem_r
	S += T0_T2_mem1<=T0_T2

	T0_T3 = S.Task('T0_T3', length=1, delay_cost=1)
	T0_T3 += alt(ADD)

	T0_T3_mem0 = S.Task('T0_T3_mem0', length=1, delay_cost=1)
	T0_T3_mem0 += INPUT_mem_r
	S += T0_T3_mem0<=T0_T3

	T0_T3_mem1 = S.Task('T0_T3_mem1', length=1, delay_cost=1)
	T0_T3_mem1 += INPUT_mem_r
	S += T0_T3_mem1<=T0_T3

	T1_T0_in = S.Task('T1_T0_in', length=1, delay_cost=1)
	T1_T0_in += alt(MUL_in)
	T1_T0 = S.Task('T1_T0', length=7, delay_cost=1)
	T1_T0 += alt(MUL)
	S+=T1_T0>=T1_T0_in

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	T1_T0_mem0 += INPUT_mem_r
	S += T1_T0_mem0<=T1_T0

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	T1_T0_mem1 += INPUT_mem_r
	S += T1_T0_mem1<=T1_T0

	T1_T1_in = S.Task('T1_T1_in', length=1, delay_cost=1)
	T1_T1_in += alt(MUL_in)
	T1_T1 = S.Task('T1_T1', length=7, delay_cost=1)
	T1_T1 += alt(MUL)
	S+=T1_T1>=T1_T1_in

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	T1_T1_mem0 += INPUT_mem_r
	S += T1_T1_mem0<=T1_T1

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	T1_T1_mem1 += INPUT_mem_r
	S += T1_T1_mem1<=T1_T1

	T1_T2 = S.Task('T1_T2', length=1, delay_cost=1)
	T1_T2 += alt(ADD)

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	T1_T2_mem0 += INPUT_mem_r
	S += T1_T2_mem0<=T1_T2

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	T1_T2_mem1 += INPUT_mem_r
	S += T1_T2_mem1<=T1_T2

	T1_T3 = S.Task('T1_T3', length=1, delay_cost=1)
	T1_T3 += alt(ADD)

	T1_T3_mem0 = S.Task('T1_T3_mem0', length=1, delay_cost=1)
	T1_T3_mem0 += INPUT_mem_r
	S += T1_T3_mem0<=T1_T3

	T1_T3_mem1 = S.Task('T1_T3_mem1', length=1, delay_cost=1)
	T1_T3_mem1 += INPUT_mem_r
	S += T1_T3_mem1<=T1_T3

	T2_1T0_in = S.Task('T2_1T0_in', length=1, delay_cost=1)
	T2_1T0_in += alt(MUL_in)
	T2_1T0 = S.Task('T2_1T0', length=7, delay_cost=1)
	T2_1T0 += alt(MUL)
	S+=T2_1T0>=T2_1T0_in

	T2_1T0_mem0 = S.Task('T2_1T0_mem0', length=1, delay_cost=1)
	T2_1T0_mem0 += INPUT_mem_r
	S += T2_1T0_mem0<=T2_1T0

	T2_1T0_mem1 = S.Task('T2_1T0_mem1', length=1, delay_cost=1)
	T2_1T0_mem1 += INPUT_mem_r
	S += T2_1T0_mem1<=T2_1T0

	T2_1T1_in = S.Task('T2_1T1_in', length=1, delay_cost=1)
	T2_1T1_in += alt(MUL_in)
	T2_1T1 = S.Task('T2_1T1', length=7, delay_cost=1)
	T2_1T1 += alt(MUL)
	S+=T2_1T1>=T2_1T1_in

	T2_1T1_mem0 = S.Task('T2_1T1_mem0', length=1, delay_cost=1)
	T2_1T1_mem0 += INPUT_mem_r
	S += T2_1T1_mem0<=T2_1T1

	T2_1T1_mem1 = S.Task('T2_1T1_mem1', length=1, delay_cost=1)
	T2_1T1_mem1 += INPUT_mem_r
	S += T2_1T1_mem1<=T2_1T1

	T2_1T2 = S.Task('T2_1T2', length=1, delay_cost=1)
	T2_1T2 += alt(ADD)

	T2_1T2_mem0 = S.Task('T2_1T2_mem0', length=1, delay_cost=1)
	T2_1T2_mem0 += INPUT_mem_r
	S += T2_1T2_mem0<=T2_1T2

	T2_1T2_mem1 = S.Task('T2_1T2_mem1', length=1, delay_cost=1)
	T2_1T2_mem1 += INPUT_mem_r
	S += T2_1T2_mem1<=T2_1T2

	T2_1T3 = S.Task('T2_1T3', length=1, delay_cost=1)
	T2_1T3 += alt(ADD)

	T2_1T3_mem0 = S.Task('T2_1T3_mem0', length=1, delay_cost=1)
	T2_1T3_mem0 += INPUT_mem_r
	S += T2_1T3_mem0<=T2_1T3

	T2_1T3_mem1 = S.Task('T2_1T3_mem1', length=1, delay_cost=1)
	T2_1T3_mem1 += INPUT_mem_r
	S += T2_1T3_mem1<=T2_1T3

	T3_30 = S.Task('T3_30', length=1, delay_cost=1)
	T3_30 += alt(ADD)

	T3_30_mem0 = S.Task('T3_30_mem0', length=1, delay_cost=1)
	T3_30_mem0 += INPUT_mem_r
	S += T3_30_mem0<=T3_30

	T3_30_mem1 = S.Task('T3_30_mem1', length=1, delay_cost=1)
	T3_30_mem1 += INPUT_mem_r
	S += T3_30_mem1<=T3_30

	T3_31 = S.Task('T3_31', length=1, delay_cost=1)
	T3_31 += alt(ADD)

	T3_31_mem0 = S.Task('T3_31_mem0', length=1, delay_cost=1)
	T3_31_mem0 += INPUT_mem_r
	S += T3_31_mem0<=T3_31

	T3_31_mem1 = S.Task('T3_31_mem1', length=1, delay_cost=1)
	T3_31_mem1 += INPUT_mem_r
	S += T3_31_mem1<=T3_31

	T4_50 = S.Task('T4_50', length=1, delay_cost=1)
	T4_50 += alt(ADD)

	T4_50_mem0 = S.Task('T4_50_mem0', length=1, delay_cost=1)
	T4_50_mem0 += INPUT_mem_r
	S += T4_50_mem0<=T4_50

	T4_50_mem1 = S.Task('T4_50_mem1', length=1, delay_cost=1)
	T4_50_mem1 += INPUT_mem_r
	S += T4_50_mem1<=T4_50

	T4_51 = S.Task('T4_51', length=1, delay_cost=1)
	T4_51 += alt(ADD)

	T4_51_mem0 = S.Task('T4_51_mem0', length=1, delay_cost=1)
	T4_51_mem0 += INPUT_mem_r
	S += T4_51_mem0<=T4_51

	T4_51_mem1 = S.Task('T4_51_mem1', length=1, delay_cost=1)
	T4_51_mem1 += INPUT_mem_r
	S += T4_51_mem1<=T4_51

	T4_60 = S.Task('T4_60', length=1, delay_cost=1)
	T4_60 += alt(ADD)

	T4_60_mem0 = S.Task('T4_60_mem0', length=1, delay_cost=1)
	T4_60_mem0 += INPUT_mem_r
	S += T4_60_mem0<=T4_60

	T4_60_mem1 = S.Task('T4_60_mem1', length=1, delay_cost=1)
	T4_60_mem1 += INPUT_mem_r
	S += T4_60_mem1<=T4_60

	T4_61 = S.Task('T4_61', length=1, delay_cost=1)
	T4_61 += alt(ADD)

	T4_61_mem0 = S.Task('T4_61_mem0', length=1, delay_cost=1)
	T4_61_mem0 += INPUT_mem_r
	S += T4_61_mem0<=T4_61

	T4_61_mem1 = S.Task('T4_61_mem1', length=1, delay_cost=1)
	T4_61_mem1 += INPUT_mem_r
	S += T4_61_mem1<=T4_61

	T5_40 = S.Task('T5_40', length=1, delay_cost=1)
	T5_40 += alt(ADD)

	T5_40_mem0 = S.Task('T5_40_mem0', length=1, delay_cost=1)
	T5_40_mem0 += INPUT_mem_r
	S += T5_40_mem0<=T5_40

	T5_40_mem1 = S.Task('T5_40_mem1', length=1, delay_cost=1)
	T5_40_mem1 += INPUT_mem_r
	S += T5_40_mem1<=T5_40

	T5_41 = S.Task('T5_41', length=1, delay_cost=1)
	T5_41 += alt(ADD)

	T5_41_mem0 = S.Task('T5_41_mem0', length=1, delay_cost=1)
	T5_41_mem0 += INPUT_mem_r
	S += T5_41_mem0<=T5_41

	T5_41_mem1 = S.Task('T5_41_mem1', length=1, delay_cost=1)
	T5_41_mem1 += INPUT_mem_r
	S += T5_41_mem1<=T5_41

	T5_50 = S.Task('T5_50', length=1, delay_cost=1)
	T5_50 += alt(ADD)

	T5_50_mem0 = S.Task('T5_50_mem0', length=1, delay_cost=1)
	T5_50_mem0 += INPUT_mem_r
	S += T5_50_mem0<=T5_50

	T5_50_mem1 = S.Task('T5_50_mem1', length=1, delay_cost=1)
	T5_50_mem1 += INPUT_mem_r
	S += T5_50_mem1<=T5_50

	T5_51 = S.Task('T5_51', length=1, delay_cost=1)
	T5_51 += alt(ADD)

	T5_51_mem0 = S.Task('T5_51_mem0', length=1, delay_cost=1)
	T5_51_mem0 += INPUT_mem_r
	S += T5_51_mem0<=T5_51

	T5_51_mem1 = S.Task('T5_51_mem1', length=1, delay_cost=1)
	T5_51_mem1 += INPUT_mem_r
	S += T5_51_mem1<=T5_51

	T6_0 = S.Task('T6_0', length=1, delay_cost=1)
	T6_0 += alt(ADD)

	T6_0_mem0 = S.Task('T6_0_mem0', length=1, delay_cost=1)
	T6_0_mem0 += INPUT_mem_r
	S += T6_0_mem0<=T6_0

	T6_0_mem1 = S.Task('T6_0_mem1', length=1, delay_cost=1)
	T6_0_mem1 += INPUT_mem_r
	S += T6_0_mem1<=T6_0

	T6_1 = S.Task('T6_1', length=1, delay_cost=1)
	T6_1 += alt(ADD)

	T6_1_mem0 = S.Task('T6_1_mem0', length=1, delay_cost=1)
	T6_1_mem0 += INPUT_mem_r
	S += T6_1_mem0<=T6_1

	T6_1_mem1 = S.Task('T6_1_mem1', length=1, delay_cost=1)
	T6_1_mem1 += INPUT_mem_r
	S += T6_1_mem1<=T6_1

	T130 = S.Task('T130', length=1, delay_cost=1)
	T130 += alt(ADD)

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	T130_mem0 += INPUT_mem_r
	S += T130_mem0<=T130

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	T130_mem1 += INPUT_mem_r
	S += T130_mem1<=T130

	T131 = S.Task('T131', length=1, delay_cost=1)
	T131 += alt(ADD)

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	T131_mem0 += INPUT_mem_r
	S += T131_mem0<=T131

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	T131_mem1 += INPUT_mem_r
	S += T131_mem1<=T131

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01, time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "mul_mul1_add4/mul_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_mul_mul1_add4_0(0, 0)