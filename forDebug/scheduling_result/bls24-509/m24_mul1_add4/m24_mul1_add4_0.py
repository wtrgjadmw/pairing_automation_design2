from pyschedule import Scenario, solvers, plotters, alt

def solve_m24_mul1_add4_0(ConstStep, ExpStep):
	horizon = 194
	S=Scenario("m24_mul1_add4_0",horizon = horizon)

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
	T0t2_0 = S.Task('T0t2_0', length=1, delay_cost=1)
	T0t2_0 += alt(ADD)

	T0t2_0_mem0 = S.Task('T0t2_0_mem0', length=1, delay_cost=1)
	T0t2_0_mem0 += INPUT_mem_r
	S += T0t2_0_mem0<=T0t2_0

	T0t2_0_mem1 = S.Task('T0t2_0_mem1', length=1, delay_cost=1)
	T0t2_0_mem1 += INPUT_mem_r
	S += T0t2_0_mem1<=T0t2_0

	T0t2_1 = S.Task('T0t2_1', length=1, delay_cost=1)
	T0t2_1 += alt(ADD)

	T0t2_1_mem0 = S.Task('T0t2_1_mem0', length=1, delay_cost=1)
	T0t2_1_mem0 += INPUT_mem_r
	S += T0t2_1_mem0<=T0t2_1

	T0t2_1_mem1 = S.Task('T0t2_1_mem1', length=1, delay_cost=1)
	T0t2_1_mem1 += INPUT_mem_r
	S += T0t2_1_mem1<=T0t2_1

	T0t3_0 = S.Task('T0t3_0', length=1, delay_cost=1)
	T0t3_0 += alt(ADD)

	T0t3_0_mem0 = S.Task('T0t3_0_mem0', length=1, delay_cost=1)
	T0t3_0_mem0 += INPUT_mem_r
	S += T0t3_0_mem0<=T0t3_0

	T0t3_0_mem1 = S.Task('T0t3_0_mem1', length=1, delay_cost=1)
	T0t3_0_mem1 += INPUT_mem_r
	S += T0t3_0_mem1<=T0t3_0

	T0t3_1 = S.Task('T0t3_1', length=1, delay_cost=1)
	T0t3_1 += alt(ADD)

	T0t3_1_mem0 = S.Task('T0t3_1_mem0', length=1, delay_cost=1)
	T0t3_1_mem0 += INPUT_mem_r
	S += T0t3_1_mem0<=T0t3_1

	T0t3_1_mem1 = S.Task('T0t3_1_mem1', length=1, delay_cost=1)
	T0t3_1_mem1 += INPUT_mem_r
	S += T0t3_1_mem1<=T0t3_1

	T0t0_a0b0_in = S.Task('T0t0_a0b0_in', length=1, delay_cost=1)
	T0t0_a0b0_in += alt(MUL_in)
	T0t0_a0b0 = S.Task('T0t0_a0b0', length=7, delay_cost=1)
	T0t0_a0b0 += alt(MUL)
	S+=T0t0_a0b0>=T0t0_a0b0_in

	T0t0_a0b0_mem0 = S.Task('T0t0_a0b0_mem0', length=1, delay_cost=1)
	T0t0_a0b0_mem0 += INPUT_mem_r
	S += T0t0_a0b0_mem0<=T0t0_a0b0

	T0t0_a0b0_mem1 = S.Task('T0t0_a0b0_mem1', length=1, delay_cost=1)
	T0t0_a0b0_mem1 += INPUT_mem_r
	S += T0t0_a0b0_mem1<=T0t0_a0b0

	T0t1_a0b0_in = S.Task('T0t1_a0b0_in', length=1, delay_cost=1)
	T0t1_a0b0_in += alt(MUL_in)
	T0t1_a0b0 = S.Task('T0t1_a0b0', length=7, delay_cost=1)
	T0t1_a0b0 += alt(MUL)
	S+=T0t1_a0b0>=T0t1_a0b0_in

	T0t1_a0b0_mem0 = S.Task('T0t1_a0b0_mem0', length=1, delay_cost=1)
	T0t1_a0b0_mem0 += INPUT_mem_r
	S += T0t1_a0b0_mem0<=T0t1_a0b0

	T0t1_a0b0_mem1 = S.Task('T0t1_a0b0_mem1', length=1, delay_cost=1)
	T0t1_a0b0_mem1 += INPUT_mem_r
	S += T0t1_a0b0_mem1<=T0t1_a0b0

	T0t2_a0b0 = S.Task('T0t2_a0b0', length=1, delay_cost=1)
	T0t2_a0b0 += alt(ADD)

	T0t2_a0b0_mem0 = S.Task('T0t2_a0b0_mem0', length=1, delay_cost=1)
	T0t2_a0b0_mem0 += INPUT_mem_r
	S += T0t2_a0b0_mem0<=T0t2_a0b0

	T0t2_a0b0_mem1 = S.Task('T0t2_a0b0_mem1', length=1, delay_cost=1)
	T0t2_a0b0_mem1 += INPUT_mem_r
	S += T0t2_a0b0_mem1<=T0t2_a0b0

	T0t3_a0b0 = S.Task('T0t3_a0b0', length=1, delay_cost=1)
	T0t3_a0b0 += alt(ADD)

	T0t3_a0b0_mem0 = S.Task('T0t3_a0b0_mem0', length=1, delay_cost=1)
	T0t3_a0b0_mem0 += INPUT_mem_r
	S += T0t3_a0b0_mem0<=T0t3_a0b0

	T0t3_a0b0_mem1 = S.Task('T0t3_a0b0_mem1', length=1, delay_cost=1)
	T0t3_a0b0_mem1 += INPUT_mem_r
	S += T0t3_a0b0_mem1<=T0t3_a0b0

	T0t0_a1b1_in = S.Task('T0t0_a1b1_in', length=1, delay_cost=1)
	T0t0_a1b1_in += alt(MUL_in)
	T0t0_a1b1 = S.Task('T0t0_a1b1', length=7, delay_cost=1)
	T0t0_a1b1 += alt(MUL)
	S+=T0t0_a1b1>=T0t0_a1b1_in

	T0t0_a1b1_mem0 = S.Task('T0t0_a1b1_mem0', length=1, delay_cost=1)
	T0t0_a1b1_mem0 += INPUT_mem_r
	S += T0t0_a1b1_mem0<=T0t0_a1b1

	T0t0_a1b1_mem1 = S.Task('T0t0_a1b1_mem1', length=1, delay_cost=1)
	T0t0_a1b1_mem1 += INPUT_mem_r
	S += T0t0_a1b1_mem1<=T0t0_a1b1

	T0t1_a1b1_in = S.Task('T0t1_a1b1_in', length=1, delay_cost=1)
	T0t1_a1b1_in += alt(MUL_in)
	T0t1_a1b1 = S.Task('T0t1_a1b1', length=7, delay_cost=1)
	T0t1_a1b1 += alt(MUL)
	S+=T0t1_a1b1>=T0t1_a1b1_in

	T0t1_a1b1_mem0 = S.Task('T0t1_a1b1_mem0', length=1, delay_cost=1)
	T0t1_a1b1_mem0 += INPUT_mem_r
	S += T0t1_a1b1_mem0<=T0t1_a1b1

	T0t1_a1b1_mem1 = S.Task('T0t1_a1b1_mem1', length=1, delay_cost=1)
	T0t1_a1b1_mem1 += INPUT_mem_r
	S += T0t1_a1b1_mem1<=T0t1_a1b1

	T0t2_a1b1 = S.Task('T0t2_a1b1', length=1, delay_cost=1)
	T0t2_a1b1 += alt(ADD)

	T0t2_a1b1_mem0 = S.Task('T0t2_a1b1_mem0', length=1, delay_cost=1)
	T0t2_a1b1_mem0 += INPUT_mem_r
	S += T0t2_a1b1_mem0<=T0t2_a1b1

	T0t2_a1b1_mem1 = S.Task('T0t2_a1b1_mem1', length=1, delay_cost=1)
	T0t2_a1b1_mem1 += INPUT_mem_r
	S += T0t2_a1b1_mem1<=T0t2_a1b1

	T0t3_a1b1 = S.Task('T0t3_a1b1', length=1, delay_cost=1)
	T0t3_a1b1 += alt(ADD)

	T0t3_a1b1_mem0 = S.Task('T0t3_a1b1_mem0', length=1, delay_cost=1)
	T0t3_a1b1_mem0 += INPUT_mem_r
	S += T0t3_a1b1_mem0<=T0t3_a1b1

	T0t3_a1b1_mem1 = S.Task('T0t3_a1b1_mem1', length=1, delay_cost=1)
	T0t3_a1b1_mem1 += INPUT_mem_r
	S += T0t3_a1b1_mem1<=T0t3_a1b1

	T1t2_0 = S.Task('T1t2_0', length=1, delay_cost=1)
	T1t2_0 += alt(ADD)

	T1t2_0_mem0 = S.Task('T1t2_0_mem0', length=1, delay_cost=1)
	T1t2_0_mem0 += INPUT_mem_r
	S += T1t2_0_mem0<=T1t2_0

	T1t2_0_mem1 = S.Task('T1t2_0_mem1', length=1, delay_cost=1)
	T1t2_0_mem1 += INPUT_mem_r
	S += T1t2_0_mem1<=T1t2_0

	T1t2_1 = S.Task('T1t2_1', length=1, delay_cost=1)
	T1t2_1 += alt(ADD)

	T1t2_1_mem0 = S.Task('T1t2_1_mem0', length=1, delay_cost=1)
	T1t2_1_mem0 += INPUT_mem_r
	S += T1t2_1_mem0<=T1t2_1

	T1t2_1_mem1 = S.Task('T1t2_1_mem1', length=1, delay_cost=1)
	T1t2_1_mem1 += INPUT_mem_r
	S += T1t2_1_mem1<=T1t2_1

	T1t3_0 = S.Task('T1t3_0', length=1, delay_cost=1)
	T1t3_0 += alt(ADD)

	T1t3_0_mem0 = S.Task('T1t3_0_mem0', length=1, delay_cost=1)
	T1t3_0_mem0 += INPUT_mem_r
	S += T1t3_0_mem0<=T1t3_0

	T1t3_0_mem1 = S.Task('T1t3_0_mem1', length=1, delay_cost=1)
	T1t3_0_mem1 += INPUT_mem_r
	S += T1t3_0_mem1<=T1t3_0

	T1t3_1 = S.Task('T1t3_1', length=1, delay_cost=1)
	T1t3_1 += alt(ADD)

	T1t3_1_mem0 = S.Task('T1t3_1_mem0', length=1, delay_cost=1)
	T1t3_1_mem0 += INPUT_mem_r
	S += T1t3_1_mem0<=T1t3_1

	T1t3_1_mem1 = S.Task('T1t3_1_mem1', length=1, delay_cost=1)
	T1t3_1_mem1 += INPUT_mem_r
	S += T1t3_1_mem1<=T1t3_1

	T1t0_a0b0_in = S.Task('T1t0_a0b0_in', length=1, delay_cost=1)
	T1t0_a0b0_in += alt(MUL_in)
	T1t0_a0b0 = S.Task('T1t0_a0b0', length=7, delay_cost=1)
	T1t0_a0b0 += alt(MUL)
	S+=T1t0_a0b0>=T1t0_a0b0_in

	T1t0_a0b0_mem0 = S.Task('T1t0_a0b0_mem0', length=1, delay_cost=1)
	T1t0_a0b0_mem0 += INPUT_mem_r
	S += T1t0_a0b0_mem0<=T1t0_a0b0

	T1t0_a0b0_mem1 = S.Task('T1t0_a0b0_mem1', length=1, delay_cost=1)
	T1t0_a0b0_mem1 += INPUT_mem_r
	S += T1t0_a0b0_mem1<=T1t0_a0b0

	T1t1_a0b0_in = S.Task('T1t1_a0b0_in', length=1, delay_cost=1)
	T1t1_a0b0_in += alt(MUL_in)
	T1t1_a0b0 = S.Task('T1t1_a0b0', length=7, delay_cost=1)
	T1t1_a0b0 += alt(MUL)
	S+=T1t1_a0b0>=T1t1_a0b0_in

	T1t1_a0b0_mem0 = S.Task('T1t1_a0b0_mem0', length=1, delay_cost=1)
	T1t1_a0b0_mem0 += INPUT_mem_r
	S += T1t1_a0b0_mem0<=T1t1_a0b0

	T1t1_a0b0_mem1 = S.Task('T1t1_a0b0_mem1', length=1, delay_cost=1)
	T1t1_a0b0_mem1 += INPUT_mem_r
	S += T1t1_a0b0_mem1<=T1t1_a0b0

	T1t2_a0b0 = S.Task('T1t2_a0b0', length=1, delay_cost=1)
	T1t2_a0b0 += alt(ADD)

	T1t2_a0b0_mem0 = S.Task('T1t2_a0b0_mem0', length=1, delay_cost=1)
	T1t2_a0b0_mem0 += INPUT_mem_r
	S += T1t2_a0b0_mem0<=T1t2_a0b0

	T1t2_a0b0_mem1 = S.Task('T1t2_a0b0_mem1', length=1, delay_cost=1)
	T1t2_a0b0_mem1 += INPUT_mem_r
	S += T1t2_a0b0_mem1<=T1t2_a0b0

	T1t3_a0b0 = S.Task('T1t3_a0b0', length=1, delay_cost=1)
	T1t3_a0b0 += alt(ADD)

	T1t3_a0b0_mem0 = S.Task('T1t3_a0b0_mem0', length=1, delay_cost=1)
	T1t3_a0b0_mem0 += INPUT_mem_r
	S += T1t3_a0b0_mem0<=T1t3_a0b0

	T1t3_a0b0_mem1 = S.Task('T1t3_a0b0_mem1', length=1, delay_cost=1)
	T1t3_a0b0_mem1 += INPUT_mem_r
	S += T1t3_a0b0_mem1<=T1t3_a0b0

	T1t0_a1b1_in = S.Task('T1t0_a1b1_in', length=1, delay_cost=1)
	T1t0_a1b1_in += alt(MUL_in)
	T1t0_a1b1 = S.Task('T1t0_a1b1', length=7, delay_cost=1)
	T1t0_a1b1 += alt(MUL)
	S+=T1t0_a1b1>=T1t0_a1b1_in

	T1t0_a1b1_mem0 = S.Task('T1t0_a1b1_mem0', length=1, delay_cost=1)
	T1t0_a1b1_mem0 += INPUT_mem_r
	S += T1t0_a1b1_mem0<=T1t0_a1b1

	T1t0_a1b1_mem1 = S.Task('T1t0_a1b1_mem1', length=1, delay_cost=1)
	T1t0_a1b1_mem1 += INPUT_mem_r
	S += T1t0_a1b1_mem1<=T1t0_a1b1

	T1t1_a1b1_in = S.Task('T1t1_a1b1_in', length=1, delay_cost=1)
	T1t1_a1b1_in += alt(MUL_in)
	T1t1_a1b1 = S.Task('T1t1_a1b1', length=7, delay_cost=1)
	T1t1_a1b1 += alt(MUL)
	S+=T1t1_a1b1>=T1t1_a1b1_in

	T1t1_a1b1_mem0 = S.Task('T1t1_a1b1_mem0', length=1, delay_cost=1)
	T1t1_a1b1_mem0 += INPUT_mem_r
	S += T1t1_a1b1_mem0<=T1t1_a1b1

	T1t1_a1b1_mem1 = S.Task('T1t1_a1b1_mem1', length=1, delay_cost=1)
	T1t1_a1b1_mem1 += INPUT_mem_r
	S += T1t1_a1b1_mem1<=T1t1_a1b1

	T1t2_a1b1 = S.Task('T1t2_a1b1', length=1, delay_cost=1)
	T1t2_a1b1 += alt(ADD)

	T1t2_a1b1_mem0 = S.Task('T1t2_a1b1_mem0', length=1, delay_cost=1)
	T1t2_a1b1_mem0 += INPUT_mem_r
	S += T1t2_a1b1_mem0<=T1t2_a1b1

	T1t2_a1b1_mem1 = S.Task('T1t2_a1b1_mem1', length=1, delay_cost=1)
	T1t2_a1b1_mem1 += INPUT_mem_r
	S += T1t2_a1b1_mem1<=T1t2_a1b1

	T1t3_a1b1 = S.Task('T1t3_a1b1', length=1, delay_cost=1)
	T1t3_a1b1 += alt(ADD)

	T1t3_a1b1_mem0 = S.Task('T1t3_a1b1_mem0', length=1, delay_cost=1)
	T1t3_a1b1_mem0 += INPUT_mem_r
	S += T1t3_a1b1_mem0<=T1t3_a1b1

	T1t3_a1b1_mem1 = S.Task('T1t3_a1b1_mem1', length=1, delay_cost=1)
	T1t3_a1b1_mem1 += INPUT_mem_r
	S += T1t3_a1b1_mem1<=T1t3_a1b1

	T2t2_0 = S.Task('T2t2_0', length=1, delay_cost=1)
	T2t2_0 += alt(ADD)

	T2t2_0_mem0 = S.Task('T2t2_0_mem0', length=1, delay_cost=1)
	T2t2_0_mem0 += INPUT_mem_r
	S += T2t2_0_mem0<=T2t2_0

	T2t2_0_mem1 = S.Task('T2t2_0_mem1', length=1, delay_cost=1)
	T2t2_0_mem1 += INPUT_mem_r
	S += T2t2_0_mem1<=T2t2_0

	T2t2_1 = S.Task('T2t2_1', length=1, delay_cost=1)
	T2t2_1 += alt(ADD)

	T2t2_1_mem0 = S.Task('T2t2_1_mem0', length=1, delay_cost=1)
	T2t2_1_mem0 += INPUT_mem_r
	S += T2t2_1_mem0<=T2t2_1

	T2t2_1_mem1 = S.Task('T2t2_1_mem1', length=1, delay_cost=1)
	T2t2_1_mem1 += INPUT_mem_r
	S += T2t2_1_mem1<=T2t2_1

	T2t3_0 = S.Task('T2t3_0', length=1, delay_cost=1)
	T2t3_0 += alt(ADD)

	T2t3_0_mem0 = S.Task('T2t3_0_mem0', length=1, delay_cost=1)
	T2t3_0_mem0 += INPUT_mem_r
	S += T2t3_0_mem0<=T2t3_0

	T2t3_0_mem1 = S.Task('T2t3_0_mem1', length=1, delay_cost=1)
	T2t3_0_mem1 += INPUT_mem_r
	S += T2t3_0_mem1<=T2t3_0

	T2t3_1 = S.Task('T2t3_1', length=1, delay_cost=1)
	T2t3_1 += alt(ADD)

	T2t3_1_mem0 = S.Task('T2t3_1_mem0', length=1, delay_cost=1)
	T2t3_1_mem0 += INPUT_mem_r
	S += T2t3_1_mem0<=T2t3_1

	T2t3_1_mem1 = S.Task('T2t3_1_mem1', length=1, delay_cost=1)
	T2t3_1_mem1 += INPUT_mem_r
	S += T2t3_1_mem1<=T2t3_1

	T2t0_a0b0_in = S.Task('T2t0_a0b0_in', length=1, delay_cost=1)
	T2t0_a0b0_in += alt(MUL_in)
	T2t0_a0b0 = S.Task('T2t0_a0b0', length=7, delay_cost=1)
	T2t0_a0b0 += alt(MUL)
	S+=T2t0_a0b0>=T2t0_a0b0_in

	T2t0_a0b0_mem0 = S.Task('T2t0_a0b0_mem0', length=1, delay_cost=1)
	T2t0_a0b0_mem0 += INPUT_mem_r
	S += T2t0_a0b0_mem0<=T2t0_a0b0

	T2t0_a0b0_mem1 = S.Task('T2t0_a0b0_mem1', length=1, delay_cost=1)
	T2t0_a0b0_mem1 += INPUT_mem_r
	S += T2t0_a0b0_mem1<=T2t0_a0b0

	T2t1_a0b0_in = S.Task('T2t1_a0b0_in', length=1, delay_cost=1)
	T2t1_a0b0_in += alt(MUL_in)
	T2t1_a0b0 = S.Task('T2t1_a0b0', length=7, delay_cost=1)
	T2t1_a0b0 += alt(MUL)
	S+=T2t1_a0b0>=T2t1_a0b0_in

	T2t1_a0b0_mem0 = S.Task('T2t1_a0b0_mem0', length=1, delay_cost=1)
	T2t1_a0b0_mem0 += INPUT_mem_r
	S += T2t1_a0b0_mem0<=T2t1_a0b0

	T2t1_a0b0_mem1 = S.Task('T2t1_a0b0_mem1', length=1, delay_cost=1)
	T2t1_a0b0_mem1 += INPUT_mem_r
	S += T2t1_a0b0_mem1<=T2t1_a0b0

	T2t2_a0b0 = S.Task('T2t2_a0b0', length=1, delay_cost=1)
	T2t2_a0b0 += alt(ADD)

	T2t2_a0b0_mem0 = S.Task('T2t2_a0b0_mem0', length=1, delay_cost=1)
	T2t2_a0b0_mem0 += INPUT_mem_r
	S += T2t2_a0b0_mem0<=T2t2_a0b0

	T2t2_a0b0_mem1 = S.Task('T2t2_a0b0_mem1', length=1, delay_cost=1)
	T2t2_a0b0_mem1 += INPUT_mem_r
	S += T2t2_a0b0_mem1<=T2t2_a0b0

	T2t3_a0b0 = S.Task('T2t3_a0b0', length=1, delay_cost=1)
	T2t3_a0b0 += alt(ADD)

	T2t3_a0b0_mem0 = S.Task('T2t3_a0b0_mem0', length=1, delay_cost=1)
	T2t3_a0b0_mem0 += INPUT_mem_r
	S += T2t3_a0b0_mem0<=T2t3_a0b0

	T2t3_a0b0_mem1 = S.Task('T2t3_a0b0_mem1', length=1, delay_cost=1)
	T2t3_a0b0_mem1 += INPUT_mem_r
	S += T2t3_a0b0_mem1<=T2t3_a0b0

	T2t0_a1b1_in = S.Task('T2t0_a1b1_in', length=1, delay_cost=1)
	T2t0_a1b1_in += alt(MUL_in)
	T2t0_a1b1 = S.Task('T2t0_a1b1', length=7, delay_cost=1)
	T2t0_a1b1 += alt(MUL)
	S+=T2t0_a1b1>=T2t0_a1b1_in

	T2t0_a1b1_mem0 = S.Task('T2t0_a1b1_mem0', length=1, delay_cost=1)
	T2t0_a1b1_mem0 += INPUT_mem_r
	S += T2t0_a1b1_mem0<=T2t0_a1b1

	T2t0_a1b1_mem1 = S.Task('T2t0_a1b1_mem1', length=1, delay_cost=1)
	T2t0_a1b1_mem1 += INPUT_mem_r
	S += T2t0_a1b1_mem1<=T2t0_a1b1

	T2t1_a1b1_in = S.Task('T2t1_a1b1_in', length=1, delay_cost=1)
	T2t1_a1b1_in += alt(MUL_in)
	T2t1_a1b1 = S.Task('T2t1_a1b1', length=7, delay_cost=1)
	T2t1_a1b1 += alt(MUL)
	S+=T2t1_a1b1>=T2t1_a1b1_in

	T2t1_a1b1_mem0 = S.Task('T2t1_a1b1_mem0', length=1, delay_cost=1)
	T2t1_a1b1_mem0 += INPUT_mem_r
	S += T2t1_a1b1_mem0<=T2t1_a1b1

	T2t1_a1b1_mem1 = S.Task('T2t1_a1b1_mem1', length=1, delay_cost=1)
	T2t1_a1b1_mem1 += INPUT_mem_r
	S += T2t1_a1b1_mem1<=T2t1_a1b1

	T2t2_a1b1 = S.Task('T2t2_a1b1', length=1, delay_cost=1)
	T2t2_a1b1 += alt(ADD)

	T2t2_a1b1_mem0 = S.Task('T2t2_a1b1_mem0', length=1, delay_cost=1)
	T2t2_a1b1_mem0 += INPUT_mem_r
	S += T2t2_a1b1_mem0<=T2t2_a1b1

	T2t2_a1b1_mem1 = S.Task('T2t2_a1b1_mem1', length=1, delay_cost=1)
	T2t2_a1b1_mem1 += INPUT_mem_r
	S += T2t2_a1b1_mem1<=T2t2_a1b1

	T2t3_a1b1 = S.Task('T2t3_a1b1', length=1, delay_cost=1)
	T2t3_a1b1 += alt(ADD)

	T2t3_a1b1_mem0 = S.Task('T2t3_a1b1_mem0', length=1, delay_cost=1)
	T2t3_a1b1_mem0 += INPUT_mem_r
	S += T2t3_a1b1_mem0<=T2t3_a1b1

	T2t3_a1b1_mem1 = S.Task('T2t3_a1b1_mem1', length=1, delay_cost=1)
	T2t3_a1b1_mem1 += INPUT_mem_r
	S += T2t3_a1b1_mem1<=T2t3_a1b1

	T300 = S.Task('T300', length=1, delay_cost=1)
	T300 += alt(ADD)

	T300_mem0 = S.Task('T300_mem0', length=1, delay_cost=1)
	T300_mem0 += INPUT_mem_r
	S += T300_mem0<=T300

	T300_mem1 = S.Task('T300_mem1', length=1, delay_cost=1)
	T300_mem1 += INPUT_mem_r
	S += T300_mem1<=T300

	T301 = S.Task('T301', length=1, delay_cost=1)
	T301 += alt(ADD)

	T301_mem0 = S.Task('T301_mem0', length=1, delay_cost=1)
	T301_mem0 += INPUT_mem_r
	S += T301_mem0<=T301

	T301_mem1 = S.Task('T301_mem1', length=1, delay_cost=1)
	T301_mem1 += INPUT_mem_r
	S += T301_mem1<=T301

	T310 = S.Task('T310', length=1, delay_cost=1)
	T310 += alt(ADD)

	T310_mem0 = S.Task('T310_mem0', length=1, delay_cost=1)
	T310_mem0 += INPUT_mem_r
	S += T310_mem0<=T310

	T310_mem1 = S.Task('T310_mem1', length=1, delay_cost=1)
	T310_mem1 += INPUT_mem_r
	S += T310_mem1<=T310

	T311 = S.Task('T311', length=1, delay_cost=1)
	T311 += alt(ADD)

	T311_mem0 = S.Task('T311_mem0', length=1, delay_cost=1)
	T311_mem0 += INPUT_mem_r
	S += T311_mem0<=T311

	T311_mem1 = S.Task('T311_mem1', length=1, delay_cost=1)
	T311_mem1 += INPUT_mem_r
	S += T311_mem1<=T311

	T400 = S.Task('T400', length=1, delay_cost=1)
	T400 += alt(ADD)

	T400_mem0 = S.Task('T400_mem0', length=1, delay_cost=1)
	T400_mem0 += INPUT_mem_r
	S += T400_mem0<=T400

	T400_mem1 = S.Task('T400_mem1', length=1, delay_cost=1)
	T400_mem1 += INPUT_mem_r
	S += T400_mem1<=T400

	T401 = S.Task('T401', length=1, delay_cost=1)
	T401 += alt(ADD)

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	T401_mem0 += INPUT_mem_r
	S += T401_mem0<=T401

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	T401_mem1 += INPUT_mem_r
	S += T401_mem1<=T401

	T410 = S.Task('T410', length=1, delay_cost=1)
	T410 += alt(ADD)

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	T410_mem0 += INPUT_mem_r
	S += T410_mem0<=T410

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	T410_mem1 += INPUT_mem_r
	S += T410_mem1<=T410

	T411 = S.Task('T411', length=1, delay_cost=1)
	T411 += alt(ADD)

	T411_mem0 = S.Task('T411_mem0', length=1, delay_cost=1)
	T411_mem0 += INPUT_mem_r
	S += T411_mem0<=T411

	T411_mem1 = S.Task('T411_mem1', length=1, delay_cost=1)
	T411_mem1 += INPUT_mem_r
	S += T411_mem1<=T411

	T4_100 = S.Task('T4_100', length=1, delay_cost=1)
	T4_100 += alt(ADD)

	T4_100_mem0 = S.Task('T4_100_mem0', length=1, delay_cost=1)
	T4_100_mem0 += INPUT_mem_r
	S += T4_100_mem0<=T4_100

	T4_100_mem1 = S.Task('T4_100_mem1', length=1, delay_cost=1)
	T4_100_mem1 += INPUT_mem_r
	S += T4_100_mem1<=T4_100

	T4_101 = S.Task('T4_101', length=1, delay_cost=1)
	T4_101 += alt(ADD)

	T4_101_mem0 = S.Task('T4_101_mem0', length=1, delay_cost=1)
	T4_101_mem0 += INPUT_mem_r
	S += T4_101_mem0<=T4_101

	T4_101_mem1 = S.Task('T4_101_mem1', length=1, delay_cost=1)
	T4_101_mem1 += INPUT_mem_r
	S += T4_101_mem1<=T4_101

	T4_110 = S.Task('T4_110', length=1, delay_cost=1)
	T4_110 += alt(ADD)

	T4_110_mem0 = S.Task('T4_110_mem0', length=1, delay_cost=1)
	T4_110_mem0 += INPUT_mem_r
	S += T4_110_mem0<=T4_110

	T4_110_mem1 = S.Task('T4_110_mem1', length=1, delay_cost=1)
	T4_110_mem1 += INPUT_mem_r
	S += T4_110_mem1<=T4_110

	T4_111 = S.Task('T4_111', length=1, delay_cost=1)
	T4_111 += alt(ADD)

	T4_111_mem0 = S.Task('T4_111_mem0', length=1, delay_cost=1)
	T4_111_mem0 += INPUT_mem_r
	S += T4_111_mem0<=T4_111

	T4_111_mem1 = S.Task('T4_111_mem1', length=1, delay_cost=1)
	T4_111_mem1 += INPUT_mem_r
	S += T4_111_mem1<=T4_111

	T500 = S.Task('T500', length=1, delay_cost=1)
	T500 += alt(ADD)

	T500_mem0 = S.Task('T500_mem0', length=1, delay_cost=1)
	T500_mem0 += INPUT_mem_r
	S += T500_mem0<=T500

	T500_mem1 = S.Task('T500_mem1', length=1, delay_cost=1)
	T500_mem1 += INPUT_mem_r
	S += T500_mem1<=T500

	T501 = S.Task('T501', length=1, delay_cost=1)
	T501 += alt(ADD)

	T501_mem0 = S.Task('T501_mem0', length=1, delay_cost=1)
	T501_mem0 += INPUT_mem_r
	S += T501_mem0<=T501

	T501_mem1 = S.Task('T501_mem1', length=1, delay_cost=1)
	T501_mem1 += INPUT_mem_r
	S += T501_mem1<=T501

	T510 = S.Task('T510', length=1, delay_cost=1)
	T510 += alt(ADD)

	T510_mem0 = S.Task('T510_mem0', length=1, delay_cost=1)
	T510_mem0 += INPUT_mem_r
	S += T510_mem0<=T510

	T510_mem1 = S.Task('T510_mem1', length=1, delay_cost=1)
	T510_mem1 += INPUT_mem_r
	S += T510_mem1<=T510

	T511 = S.Task('T511', length=1, delay_cost=1)
	T511 += alt(ADD)

	T511_mem0 = S.Task('T511_mem0', length=1, delay_cost=1)
	T511_mem0 += INPUT_mem_r
	S += T511_mem0<=T511

	T511_mem1 = S.Task('T511_mem1', length=1, delay_cost=1)
	T511_mem1 += INPUT_mem_r
	S += T511_mem1<=T511

	T5_100 = S.Task('T5_100', length=1, delay_cost=1)
	T5_100 += alt(ADD)

	T5_100_mem0 = S.Task('T5_100_mem0', length=1, delay_cost=1)
	T5_100_mem0 += INPUT_mem_r
	S += T5_100_mem0<=T5_100

	T5_100_mem1 = S.Task('T5_100_mem1', length=1, delay_cost=1)
	T5_100_mem1 += INPUT_mem_r
	S += T5_100_mem1<=T5_100

	T5_101 = S.Task('T5_101', length=1, delay_cost=1)
	T5_101 += alt(ADD)

	T5_101_mem0 = S.Task('T5_101_mem0', length=1, delay_cost=1)
	T5_101_mem0 += INPUT_mem_r
	S += T5_101_mem0<=T5_101

	T5_101_mem1 = S.Task('T5_101_mem1', length=1, delay_cost=1)
	T5_101_mem1 += INPUT_mem_r
	S += T5_101_mem1<=T5_101

	T5_110 = S.Task('T5_110', length=1, delay_cost=1)
	T5_110 += alt(ADD)

	T5_110_mem0 = S.Task('T5_110_mem0', length=1, delay_cost=1)
	T5_110_mem0 += INPUT_mem_r
	S += T5_110_mem0<=T5_110

	T5_110_mem1 = S.Task('T5_110_mem1', length=1, delay_cost=1)
	T5_110_mem1 += INPUT_mem_r
	S += T5_110_mem1<=T5_110

	T5_111 = S.Task('T5_111', length=1, delay_cost=1)
	T5_111 += alt(ADD)

	T5_111_mem0 = S.Task('T5_111_mem0', length=1, delay_cost=1)
	T5_111_mem0 += INPUT_mem_r
	S += T5_111_mem0<=T5_111

	T5_111_mem1 = S.Task('T5_111_mem1', length=1, delay_cost=1)
	T5_111_mem1 += INPUT_mem_r
	S += T5_111_mem1<=T5_111

	T600 = S.Task('T600', length=1, delay_cost=1)
	T600 += alt(ADD)

	T600_mem0 = S.Task('T600_mem0', length=1, delay_cost=1)
	T600_mem0 += INPUT_mem_r
	S += T600_mem0<=T600

	T600_mem1 = S.Task('T600_mem1', length=1, delay_cost=1)
	T600_mem1 += INPUT_mem_r
	S += T600_mem1<=T600

	T601 = S.Task('T601', length=1, delay_cost=1)
	T601 += alt(ADD)

	T601_mem0 = S.Task('T601_mem0', length=1, delay_cost=1)
	T601_mem0 += INPUT_mem_r
	S += T601_mem0<=T601

	T601_mem1 = S.Task('T601_mem1', length=1, delay_cost=1)
	T601_mem1 += INPUT_mem_r
	S += T601_mem1<=T601

	T610 = S.Task('T610', length=1, delay_cost=1)
	T610 += alt(ADD)

	T610_mem0 = S.Task('T610_mem0', length=1, delay_cost=1)
	T610_mem0 += INPUT_mem_r
	S += T610_mem0<=T610

	T610_mem1 = S.Task('T610_mem1', length=1, delay_cost=1)
	T610_mem1 += INPUT_mem_r
	S += T610_mem1<=T610

	T611 = S.Task('T611', length=1, delay_cost=1)
	T611 += alt(ADD)

	T611_mem0 = S.Task('T611_mem0', length=1, delay_cost=1)
	T611_mem0 += INPUT_mem_r
	S += T611_mem0<=T611

	T611_mem1 = S.Task('T611_mem1', length=1, delay_cost=1)
	T611_mem1 += INPUT_mem_r
	S += T611_mem1<=T611

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "m24_mul1_add4/m24_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_m24_mul1_add4_0(0, 0)