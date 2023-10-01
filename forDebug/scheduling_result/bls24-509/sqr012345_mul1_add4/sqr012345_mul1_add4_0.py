from pyschedule import Scenario, solvers, plotters, alt

def solve_sqr012345_mul1_add4_0(ConstStep, ExpStep):
	horizon = 90
	S=Scenario("sqr012345_mul1_add4_0",horizon = horizon)

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
	T0a10_new = S.Task('T0a10_new', length=1, delay_cost=1)
	T0a10_new += alt(ADD)

	T0a11_new = S.Task('T0a11_new', length=1, delay_cost=1)
	T0a11_new += alt(ADD)

	T0t10 = S.Task('T0t10', length=1, delay_cost=1)
	T0t10 += alt(ADD)

	T0t11 = S.Task('T0t11', length=1, delay_cost=1)
	T0t11 += alt(ADD)

	T0t0_a0a1_in = S.Task('T0t0_a0a1_in', length=1, delay_cost=1)
	T0t0_a0a1_in += alt(MUL_in)
	T0t0_a0a1 = S.Task('T0t0_a0a1', length=7, delay_cost=1)
	T0t0_a0a1 += alt(MUL)
	S+=T0t0_a0a1>=T0t0_a0a1_in

	T0t1_a0a1_in = S.Task('T0t1_a0a1_in', length=1, delay_cost=1)
	T0t1_a0a1_in += alt(MUL_in)
	T0t1_a0a1 = S.Task('T0t1_a0a1', length=7, delay_cost=1)
	T0t1_a0a1 += alt(MUL)
	S+=T0t1_a0a1>=T0t1_a0a1_in

	T0t2_a0a1 = S.Task('T0t2_a0a1', length=1, delay_cost=1)
	T0t2_a0a1 += alt(ADD)

	T100 = S.Task('T100', length=1, delay_cost=1)
	T100 += alt(ADD)

	T101 = S.Task('T101', length=1, delay_cost=1)
	T101 += alt(ADD)

	T110 = S.Task('T110', length=1, delay_cost=1)
	T110 += alt(ADD)

	T111 = S.Task('T111', length=1, delay_cost=1)
	T111 += alt(ADD)

	T3t2_0 = S.Task('T3t2_0', length=1, delay_cost=1)
	T3t2_0 += alt(ADD)

	T3t2_1 = S.Task('T3t2_1', length=1, delay_cost=1)
	T3t2_1 += alt(ADD)

	T3t3_0 = S.Task('T3t3_0', length=1, delay_cost=1)
	T3t3_0 += alt(ADD)

	T3t3_1 = S.Task('T3t3_1', length=1, delay_cost=1)
	T3t3_1 += alt(ADD)

	T3t0_a0b0_in = S.Task('T3t0_a0b0_in', length=1, delay_cost=1)
	T3t0_a0b0_in += alt(MUL_in)
	T3t0_a0b0 = S.Task('T3t0_a0b0', length=7, delay_cost=1)
	T3t0_a0b0 += alt(MUL)
	S+=T3t0_a0b0>=T3t0_a0b0_in

	T3t1_a0b0_in = S.Task('T3t1_a0b0_in', length=1, delay_cost=1)
	T3t1_a0b0_in += alt(MUL_in)
	T3t1_a0b0 = S.Task('T3t1_a0b0', length=7, delay_cost=1)
	T3t1_a0b0 += alt(MUL)
	S+=T3t1_a0b0>=T3t1_a0b0_in

	T3t2_a0b0 = S.Task('T3t2_a0b0', length=1, delay_cost=1)
	T3t2_a0b0 += alt(ADD)

	T3t3_a0b0 = S.Task('T3t3_a0b0', length=1, delay_cost=1)
	T3t3_a0b0 += alt(ADD)

	T3t0_a1b1_in = S.Task('T3t0_a1b1_in', length=1, delay_cost=1)
	T3t0_a1b1_in += alt(MUL_in)
	T3t0_a1b1 = S.Task('T3t0_a1b1', length=7, delay_cost=1)
	T3t0_a1b1 += alt(MUL)
	S+=T3t0_a1b1>=T3t0_a1b1_in

	T3t1_a1b1_in = S.Task('T3t1_a1b1_in', length=1, delay_cost=1)
	T3t1_a1b1_in += alt(MUL_in)
	T3t1_a1b1 = S.Task('T3t1_a1b1', length=7, delay_cost=1)
	T3t1_a1b1 += alt(MUL)
	S+=T3t1_a1b1>=T3t1_a1b1_in

	T3t2_a1b1 = S.Task('T3t2_a1b1', length=1, delay_cost=1)
	T3t2_a1b1 += alt(ADD)

	T3t3_a1b1 = S.Task('T3t3_a1b1', length=1, delay_cost=1)
	T3t3_a1b1 += alt(ADD)

	T4a10_new = S.Task('T4a10_new', length=1, delay_cost=1)
	T4a10_new += alt(ADD)

	T4t0_a0a1_in = S.Task('T4t0_a0a1_in', length=1, delay_cost=1)
	T4t0_a0a1_in += alt(MUL_in)
	T4t0_a0a1 = S.Task('T4t0_a0a1', length=7, delay_cost=1)
	T4t0_a0a1 += alt(MUL)
	S+=T4t0_a0a1>=T4t0_a0a1_in

	T4t1_a0a1_in = S.Task('T4t1_a0a1_in', length=1, delay_cost=1)
	T4t1_a0a1_in += alt(MUL_in)
	T4t1_a0a1 = S.Task('T4t1_a0a1', length=7, delay_cost=1)
	T4t1_a0a1 += alt(MUL)
	S+=T4t1_a0a1>=T4t1_a0a1_in

	T5t3_0 = S.Task('T5t3_0', length=1, delay_cost=1)
	T5t3_0 += alt(ADD)

	T5t3_1 = S.Task('T5t3_1', length=1, delay_cost=1)
	T5t3_1 += alt(ADD)

	T5t0_a0b0_in = S.Task('T5t0_a0b0_in', length=1, delay_cost=1)
	T5t0_a0b0_in += alt(MUL_in)
	T5t0_a0b0 = S.Task('T5t0_a0b0', length=7, delay_cost=1)
	T5t0_a0b0 += alt(MUL)
	S+=T5t0_a0b0>=T5t0_a0b0_in

	T5t1_a0b0_in = S.Task('T5t1_a0b0_in', length=1, delay_cost=1)
	T5t1_a0b0_in += alt(MUL_in)
	T5t1_a0b0 = S.Task('T5t1_a0b0', length=7, delay_cost=1)
	T5t1_a0b0 += alt(MUL)
	S+=T5t1_a0b0>=T5t1_a0b0_in

	T5t3_a0b0 = S.Task('T5t3_a0b0', length=1, delay_cost=1)
	T5t3_a0b0 += alt(ADD)

	T5t0_a1b1_in = S.Task('T5t0_a1b1_in', length=1, delay_cost=1)
	T5t0_a1b1_in += alt(MUL_in)
	T5t0_a1b1 = S.Task('T5t0_a1b1', length=7, delay_cost=1)
	T5t0_a1b1 += alt(MUL)
	S+=T5t0_a1b1>=T5t0_a1b1_in

	T5t1_a1b1_in = S.Task('T5t1_a1b1_in', length=1, delay_cost=1)
	T5t1_a1b1_in += alt(MUL_in)
	T5t1_a1b1 = S.Task('T5t1_a1b1', length=7, delay_cost=1)
	T5t1_a1b1 += alt(MUL)
	S+=T5t1_a1b1>=T5t1_a1b1_in

	T5t3_a1b1 = S.Task('T5t3_a1b1', length=1, delay_cost=1)
	T5t3_a1b1 += alt(ADD)

	T6t3_0 = S.Task('T6t3_0', length=1, delay_cost=1)
	T6t3_0 += alt(ADD)

	T6t3_1 = S.Task('T6t3_1', length=1, delay_cost=1)
	T6t3_1 += alt(ADD)

	T6t0_a0b0_in = S.Task('T6t0_a0b0_in', length=1, delay_cost=1)
	T6t0_a0b0_in += alt(MUL_in)
	T6t0_a0b0 = S.Task('T6t0_a0b0', length=7, delay_cost=1)
	T6t0_a0b0 += alt(MUL)
	S+=T6t0_a0b0>=T6t0_a0b0_in

	T6t1_a0b0_in = S.Task('T6t1_a0b0_in', length=1, delay_cost=1)
	T6t1_a0b0_in += alt(MUL_in)
	T6t1_a0b0 = S.Task('T6t1_a0b0', length=7, delay_cost=1)
	T6t1_a0b0 += alt(MUL)
	S+=T6t1_a0b0>=T6t1_a0b0_in

	T6t3_a0b0 = S.Task('T6t3_a0b0', length=1, delay_cost=1)
	T6t3_a0b0 += alt(ADD)

	T6t0_a1b1_in = S.Task('T6t0_a1b1_in', length=1, delay_cost=1)
	T6t0_a1b1_in += alt(MUL_in)
	T6t0_a1b1 = S.Task('T6t0_a1b1', length=7, delay_cost=1)
	T6t0_a1b1 += alt(MUL)
	S+=T6t0_a1b1>=T6t0_a1b1_in

	T6t1_a1b1_in = S.Task('T6t1_a1b1_in', length=1, delay_cost=1)
	T6t1_a1b1_in += alt(MUL_in)
	T6t1_a1b1 = S.Task('T6t1_a1b1', length=7, delay_cost=1)
	T6t1_a1b1 += alt(MUL)
	S+=T6t1_a1b1>=T6t1_a1b1_in

	T6t3_a1b1 = S.Task('T6t3_a1b1', length=1, delay_cost=1)
	T6t3_a1b1 += alt(ADD)

	T7t2_0 = S.Task('T7t2_0', length=1, delay_cost=1)
	T7t2_0 += alt(ADD)

	T7t2_1 = S.Task('T7t2_1', length=1, delay_cost=1)
	T7t2_1 += alt(ADD)

	T7t0_a0b0_in = S.Task('T7t0_a0b0_in', length=1, delay_cost=1)
	T7t0_a0b0_in += alt(MUL_in)
	T7t0_a0b0 = S.Task('T7t0_a0b0', length=7, delay_cost=1)
	T7t0_a0b0 += alt(MUL)
	S+=T7t0_a0b0>=T7t0_a0b0_in

	T7t1_a0b0_in = S.Task('T7t1_a0b0_in', length=1, delay_cost=1)
	T7t1_a0b0_in += alt(MUL_in)
	T7t1_a0b0 = S.Task('T7t1_a0b0', length=7, delay_cost=1)
	T7t1_a0b0 += alt(MUL)
	S+=T7t1_a0b0>=T7t1_a0b0_in

	T7t2_a0b0 = S.Task('T7t2_a0b0', length=1, delay_cost=1)
	T7t2_a0b0 += alt(ADD)

	T7t0_a1b1_in = S.Task('T7t0_a1b1_in', length=1, delay_cost=1)
	T7t0_a1b1_in += alt(MUL_in)
	T7t0_a1b1 = S.Task('T7t0_a1b1', length=7, delay_cost=1)
	T7t0_a1b1 += alt(MUL)
	S+=T7t0_a1b1>=T7t0_a1b1_in

	T7t1_a1b1_in = S.Task('T7t1_a1b1_in', length=1, delay_cost=1)
	T7t1_a1b1_in += alt(MUL_in)
	T7t1_a1b1 = S.Task('T7t1_a1b1', length=7, delay_cost=1)
	T7t1_a1b1 += alt(MUL)
	S+=T7t1_a1b1>=T7t1_a1b1_in

	T7t2_a1b1 = S.Task('T7t2_a1b1', length=1, delay_cost=1)
	T7t2_a1b1 += alt(ADD)

	T0a10_new_mem0 = S.Task('T0a10_new_mem0', length=1, delay_cost=1)
	T0a10_new_mem0 += INPUT_mem_r
	S += T0a10_new_mem0<=T0a10_new

	T0a10_new_mem1 = S.Task('T0a10_new_mem1', length=1, delay_cost=1)
	T0a10_new_mem1 += INPUT_mem_r
	S += T0a10_new_mem1<=T0a10_new

	T0a11_new_mem0 = S.Task('T0a11_new_mem0', length=1, delay_cost=1)
	T0a11_new_mem0 += INPUT_mem_r
	S += T0a11_new_mem0<=T0a11_new

	T0a11_new_mem1 = S.Task('T0a11_new_mem1', length=1, delay_cost=1)
	T0a11_new_mem1 += INPUT_mem_r
	S += T0a11_new_mem1<=T0a11_new

	T0t10_mem0 = S.Task('T0t10_mem0', length=1, delay_cost=1)
	T0t10_mem0 += INPUT_mem_r
	S += T0t10_mem0<=T0t10

	T0t10_mem1 = S.Task('T0t10_mem1', length=1, delay_cost=1)
	T0t10_mem1 += INPUT_mem_r
	S += T0t10_mem1<=T0t10

	T0t11_mem0 = S.Task('T0t11_mem0', length=1, delay_cost=1)
	T0t11_mem0 += INPUT_mem_r
	S += T0t11_mem0<=T0t11

	T0t11_mem1 = S.Task('T0t11_mem1', length=1, delay_cost=1)
	T0t11_mem1 += INPUT_mem_r
	S += T0t11_mem1<=T0t11

	T0t0_a0a1_mem0 = S.Task('T0t0_a0a1_mem0', length=1, delay_cost=1)
	T0t0_a0a1_mem0 += INPUT_mem_r
	S += T0t0_a0a1_mem0<=T0t0_a0a1

	T0t0_a0a1_mem1 = S.Task('T0t0_a0a1_mem1', length=1, delay_cost=1)
	T0t0_a0a1_mem1 += INPUT_mem_r
	S += T0t0_a0a1_mem1<=T0t0_a0a1

	T0t1_a0a1_mem0 = S.Task('T0t1_a0a1_mem0', length=1, delay_cost=1)
	T0t1_a0a1_mem0 += INPUT_mem_r
	S += T0t1_a0a1_mem0<=T0t1_a0a1

	T0t1_a0a1_mem1 = S.Task('T0t1_a0a1_mem1', length=1, delay_cost=1)
	T0t1_a0a1_mem1 += INPUT_mem_r
	S += T0t1_a0a1_mem1<=T0t1_a0a1

	T0t2_a0a1_mem0 = S.Task('T0t2_a0a1_mem0', length=1, delay_cost=1)
	T0t2_a0a1_mem0 += INPUT_mem_r
	S += T0t2_a0a1_mem0<=T0t2_a0a1

	T0t2_a0a1_mem1 = S.Task('T0t2_a0a1_mem1', length=1, delay_cost=1)
	T0t2_a0a1_mem1 += INPUT_mem_r
	S += T0t2_a0a1_mem1<=T0t2_a0a1

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	T100_mem0 += INPUT_mem_r
	S += T100_mem0<=T100

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	T100_mem1 += INPUT_mem_r
	S += T100_mem1<=T100

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	T101_mem0 += INPUT_mem_r
	S += T101_mem0<=T101

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	T101_mem1 += INPUT_mem_r
	S += T101_mem1<=T101

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	T110_mem0 += INPUT_mem_r
	S += T110_mem0<=T110

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	T110_mem1 += INPUT_mem_r
	S += T110_mem1<=T110

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	T111_mem0 += INPUT_mem_r
	S += T111_mem0<=T111

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	T111_mem1 += INPUT_mem_r
	S += T111_mem1<=T111

	T3t2_0_mem0 = S.Task('T3t2_0_mem0', length=1, delay_cost=1)
	T3t2_0_mem0 += INPUT_mem_r
	S += T3t2_0_mem0<=T3t2_0

	T3t2_0_mem1 = S.Task('T3t2_0_mem1', length=1, delay_cost=1)
	T3t2_0_mem1 += INPUT_mem_r
	S += T3t2_0_mem1<=T3t2_0

	T3t2_1_mem0 = S.Task('T3t2_1_mem0', length=1, delay_cost=1)
	T3t2_1_mem0 += INPUT_mem_r
	S += T3t2_1_mem0<=T3t2_1

	T3t2_1_mem1 = S.Task('T3t2_1_mem1', length=1, delay_cost=1)
	T3t2_1_mem1 += INPUT_mem_r
	S += T3t2_1_mem1<=T3t2_1

	T3t3_0_mem0 = S.Task('T3t3_0_mem0', length=1, delay_cost=1)
	T3t3_0_mem0 += INPUT_mem_r
	S += T3t3_0_mem0<=T3t3_0

	T3t3_0_mem1 = S.Task('T3t3_0_mem1', length=1, delay_cost=1)
	T3t3_0_mem1 += INPUT_mem_r
	S += T3t3_0_mem1<=T3t3_0

	T3t3_1_mem0 = S.Task('T3t3_1_mem0', length=1, delay_cost=1)
	T3t3_1_mem0 += INPUT_mem_r
	S += T3t3_1_mem0<=T3t3_1

	T3t3_1_mem1 = S.Task('T3t3_1_mem1', length=1, delay_cost=1)
	T3t3_1_mem1 += INPUT_mem_r
	S += T3t3_1_mem1<=T3t3_1

	T3t0_a0b0_mem0 = S.Task('T3t0_a0b0_mem0', length=1, delay_cost=1)
	T3t0_a0b0_mem0 += INPUT_mem_r
	S += T3t0_a0b0_mem0<=T3t0_a0b0

	T3t0_a0b0_mem1 = S.Task('T3t0_a0b0_mem1', length=1, delay_cost=1)
	T3t0_a0b0_mem1 += INPUT_mem_r
	S += T3t0_a0b0_mem1<=T3t0_a0b0

	T3t1_a0b0_mem0 = S.Task('T3t1_a0b0_mem0', length=1, delay_cost=1)
	T3t1_a0b0_mem0 += INPUT_mem_r
	S += T3t1_a0b0_mem0<=T3t1_a0b0

	T3t1_a0b0_mem1 = S.Task('T3t1_a0b0_mem1', length=1, delay_cost=1)
	T3t1_a0b0_mem1 += INPUT_mem_r
	S += T3t1_a0b0_mem1<=T3t1_a0b0

	T3t2_a0b0_mem0 = S.Task('T3t2_a0b0_mem0', length=1, delay_cost=1)
	T3t2_a0b0_mem0 += INPUT_mem_r
	S += T3t2_a0b0_mem0<=T3t2_a0b0

	T3t2_a0b0_mem1 = S.Task('T3t2_a0b0_mem1', length=1, delay_cost=1)
	T3t2_a0b0_mem1 += INPUT_mem_r
	S += T3t2_a0b0_mem1<=T3t2_a0b0

	T3t3_a0b0_mem0 = S.Task('T3t3_a0b0_mem0', length=1, delay_cost=1)
	T3t3_a0b0_mem0 += INPUT_mem_r
	S += T3t3_a0b0_mem0<=T3t3_a0b0

	T3t3_a0b0_mem1 = S.Task('T3t3_a0b0_mem1', length=1, delay_cost=1)
	T3t3_a0b0_mem1 += INPUT_mem_r
	S += T3t3_a0b0_mem1<=T3t3_a0b0

	T3t0_a1b1_mem0 = S.Task('T3t0_a1b1_mem0', length=1, delay_cost=1)
	T3t0_a1b1_mem0 += INPUT_mem_r
	S += T3t0_a1b1_mem0<=T3t0_a1b1

	T3t0_a1b1_mem1 = S.Task('T3t0_a1b1_mem1', length=1, delay_cost=1)
	T3t0_a1b1_mem1 += INPUT_mem_r
	S += T3t0_a1b1_mem1<=T3t0_a1b1

	T3t1_a1b1_mem0 = S.Task('T3t1_a1b1_mem0', length=1, delay_cost=1)
	T3t1_a1b1_mem0 += INPUT_mem_r
	S += T3t1_a1b1_mem0<=T3t1_a1b1

	T3t1_a1b1_mem1 = S.Task('T3t1_a1b1_mem1', length=1, delay_cost=1)
	T3t1_a1b1_mem1 += INPUT_mem_r
	S += T3t1_a1b1_mem1<=T3t1_a1b1

	T3t2_a1b1_mem0 = S.Task('T3t2_a1b1_mem0', length=1, delay_cost=1)
	T3t2_a1b1_mem0 += INPUT_mem_r
	S += T3t2_a1b1_mem0<=T3t2_a1b1

	T3t2_a1b1_mem1 = S.Task('T3t2_a1b1_mem1', length=1, delay_cost=1)
	T3t2_a1b1_mem1 += INPUT_mem_r
	S += T3t2_a1b1_mem1<=T3t2_a1b1

	T3t3_a1b1_mem0 = S.Task('T3t3_a1b1_mem0', length=1, delay_cost=1)
	T3t3_a1b1_mem0 += INPUT_mem_r
	S += T3t3_a1b1_mem0<=T3t3_a1b1

	T3t3_a1b1_mem1 = S.Task('T3t3_a1b1_mem1', length=1, delay_cost=1)
	T3t3_a1b1_mem1 += INPUT_mem_r
	S += T3t3_a1b1_mem1<=T3t3_a1b1

	T4a10_new_mem0 = S.Task('T4a10_new_mem0', length=1, delay_cost=1)
	T4a10_new_mem0 += INPUT_mem_r
	S += T4a10_new_mem0<=T4a10_new

	T4a10_new_mem1 = S.Task('T4a10_new_mem1', length=1, delay_cost=1)
	T4a10_new_mem1 += INPUT_mem_r
	S += T4a10_new_mem1<=T4a10_new

	T4t0_a0a1_mem0 = S.Task('T4t0_a0a1_mem0', length=1, delay_cost=1)
	T4t0_a0a1_mem0 += INPUT_mem_r
	S += T4t0_a0a1_mem0<=T4t0_a0a1

	T4t0_a0a1_mem1 = S.Task('T4t0_a0a1_mem1', length=1, delay_cost=1)
	T4t0_a0a1_mem1 += INPUT_mem_r
	S += T4t0_a0a1_mem1<=T4t0_a0a1

	T4t1_a0a1_mem0 = S.Task('T4t1_a0a1_mem0', length=1, delay_cost=1)
	T4t1_a0a1_mem0 += INPUT_mem_r
	S += T4t1_a0a1_mem0<=T4t1_a0a1

	T4t1_a0a1_mem1 = S.Task('T4t1_a0a1_mem1', length=1, delay_cost=1)
	T4t1_a0a1_mem1 += INPUT_mem_r
	S += T4t1_a0a1_mem1<=T4t1_a0a1

	T5t3_0_mem0 = S.Task('T5t3_0_mem0', length=1, delay_cost=1)
	T5t3_0_mem0 += INPUT_mem_r
	S += T5t3_0_mem0<=T5t3_0

	T5t3_0_mem1 = S.Task('T5t3_0_mem1', length=1, delay_cost=1)
	T5t3_0_mem1 += INPUT_mem_r
	S += T5t3_0_mem1<=T5t3_0

	T5t3_1_mem0 = S.Task('T5t3_1_mem0', length=1, delay_cost=1)
	T5t3_1_mem0 += INPUT_mem_r
	S += T5t3_1_mem0<=T5t3_1

	T5t3_1_mem1 = S.Task('T5t3_1_mem1', length=1, delay_cost=1)
	T5t3_1_mem1 += INPUT_mem_r
	S += T5t3_1_mem1<=T5t3_1

	T5t0_a0b0_mem0 = S.Task('T5t0_a0b0_mem0', length=1, delay_cost=1)
	T5t0_a0b0_mem0 += INPUT_mem_r
	S += T5t0_a0b0_mem0<=T5t0_a0b0

	T5t0_a0b0_mem1 = S.Task('T5t0_a0b0_mem1', length=1, delay_cost=1)
	T5t0_a0b0_mem1 += INPUT_mem_r
	S += T5t0_a0b0_mem1<=T5t0_a0b0

	T5t1_a0b0_mem0 = S.Task('T5t1_a0b0_mem0', length=1, delay_cost=1)
	T5t1_a0b0_mem0 += INPUT_mem_r
	S += T5t1_a0b0_mem0<=T5t1_a0b0

	T5t1_a0b0_mem1 = S.Task('T5t1_a0b0_mem1', length=1, delay_cost=1)
	T5t1_a0b0_mem1 += INPUT_mem_r
	S += T5t1_a0b0_mem1<=T5t1_a0b0

	T5t3_a0b0_mem0 = S.Task('T5t3_a0b0_mem0', length=1, delay_cost=1)
	T5t3_a0b0_mem0 += INPUT_mem_r
	S += T5t3_a0b0_mem0<=T5t3_a0b0

	T5t3_a0b0_mem1 = S.Task('T5t3_a0b0_mem1', length=1, delay_cost=1)
	T5t3_a0b0_mem1 += INPUT_mem_r
	S += T5t3_a0b0_mem1<=T5t3_a0b0

	T5t0_a1b1_mem0 = S.Task('T5t0_a1b1_mem0', length=1, delay_cost=1)
	T5t0_a1b1_mem0 += INPUT_mem_r
	S += T5t0_a1b1_mem0<=T5t0_a1b1

	T5t0_a1b1_mem1 = S.Task('T5t0_a1b1_mem1', length=1, delay_cost=1)
	T5t0_a1b1_mem1 += INPUT_mem_r
	S += T5t0_a1b1_mem1<=T5t0_a1b1

	T5t1_a1b1_mem0 = S.Task('T5t1_a1b1_mem0', length=1, delay_cost=1)
	T5t1_a1b1_mem0 += INPUT_mem_r
	S += T5t1_a1b1_mem0<=T5t1_a1b1

	T5t1_a1b1_mem1 = S.Task('T5t1_a1b1_mem1', length=1, delay_cost=1)
	T5t1_a1b1_mem1 += INPUT_mem_r
	S += T5t1_a1b1_mem1<=T5t1_a1b1

	T5t3_a1b1_mem0 = S.Task('T5t3_a1b1_mem0', length=1, delay_cost=1)
	T5t3_a1b1_mem0 += INPUT_mem_r
	S += T5t3_a1b1_mem0<=T5t3_a1b1

	T5t3_a1b1_mem1 = S.Task('T5t3_a1b1_mem1', length=1, delay_cost=1)
	T5t3_a1b1_mem1 += INPUT_mem_r
	S += T5t3_a1b1_mem1<=T5t3_a1b1

	T6t3_0_mem0 = S.Task('T6t3_0_mem0', length=1, delay_cost=1)
	T6t3_0_mem0 += INPUT_mem_r
	S += T6t3_0_mem0<=T6t3_0

	T6t3_0_mem1 = S.Task('T6t3_0_mem1', length=1, delay_cost=1)
	T6t3_0_mem1 += INPUT_mem_r
	S += T6t3_0_mem1<=T6t3_0

	T6t3_1_mem0 = S.Task('T6t3_1_mem0', length=1, delay_cost=1)
	T6t3_1_mem0 += INPUT_mem_r
	S += T6t3_1_mem0<=T6t3_1

	T6t3_1_mem1 = S.Task('T6t3_1_mem1', length=1, delay_cost=1)
	T6t3_1_mem1 += INPUT_mem_r
	S += T6t3_1_mem1<=T6t3_1

	T6t0_a0b0_mem0 = S.Task('T6t0_a0b0_mem0', length=1, delay_cost=1)
	T6t0_a0b0_mem0 += INPUT_mem_r
	S += T6t0_a0b0_mem0<=T6t0_a0b0

	T6t0_a0b0_mem1 = S.Task('T6t0_a0b0_mem1', length=1, delay_cost=1)
	T6t0_a0b0_mem1 += INPUT_mem_r
	S += T6t0_a0b0_mem1<=T6t0_a0b0

	T6t1_a0b0_mem0 = S.Task('T6t1_a0b0_mem0', length=1, delay_cost=1)
	T6t1_a0b0_mem0 += INPUT_mem_r
	S += T6t1_a0b0_mem0<=T6t1_a0b0

	T6t1_a0b0_mem1 = S.Task('T6t1_a0b0_mem1', length=1, delay_cost=1)
	T6t1_a0b0_mem1 += INPUT_mem_r
	S += T6t1_a0b0_mem1<=T6t1_a0b0

	T6t3_a0b0_mem0 = S.Task('T6t3_a0b0_mem0', length=1, delay_cost=1)
	T6t3_a0b0_mem0 += INPUT_mem_r
	S += T6t3_a0b0_mem0<=T6t3_a0b0

	T6t3_a0b0_mem1 = S.Task('T6t3_a0b0_mem1', length=1, delay_cost=1)
	T6t3_a0b0_mem1 += INPUT_mem_r
	S += T6t3_a0b0_mem1<=T6t3_a0b0

	T6t0_a1b1_mem0 = S.Task('T6t0_a1b1_mem0', length=1, delay_cost=1)
	T6t0_a1b1_mem0 += INPUT_mem_r
	S += T6t0_a1b1_mem0<=T6t0_a1b1

	T6t0_a1b1_mem1 = S.Task('T6t0_a1b1_mem1', length=1, delay_cost=1)
	T6t0_a1b1_mem1 += INPUT_mem_r
	S += T6t0_a1b1_mem1<=T6t0_a1b1

	T6t1_a1b1_mem0 = S.Task('T6t1_a1b1_mem0', length=1, delay_cost=1)
	T6t1_a1b1_mem0 += INPUT_mem_r
	S += T6t1_a1b1_mem0<=T6t1_a1b1

	T6t1_a1b1_mem1 = S.Task('T6t1_a1b1_mem1', length=1, delay_cost=1)
	T6t1_a1b1_mem1 += INPUT_mem_r
	S += T6t1_a1b1_mem1<=T6t1_a1b1

	T6t3_a1b1_mem0 = S.Task('T6t3_a1b1_mem0', length=1, delay_cost=1)
	T6t3_a1b1_mem0 += INPUT_mem_r
	S += T6t3_a1b1_mem0<=T6t3_a1b1

	T6t3_a1b1_mem1 = S.Task('T6t3_a1b1_mem1', length=1, delay_cost=1)
	T6t3_a1b1_mem1 += INPUT_mem_r
	S += T6t3_a1b1_mem1<=T6t3_a1b1

	T7t2_0_mem0 = S.Task('T7t2_0_mem0', length=1, delay_cost=1)
	T7t2_0_mem0 += INPUT_mem_r
	S += T7t2_0_mem0<=T7t2_0

	T7t2_0_mem1 = S.Task('T7t2_0_mem1', length=1, delay_cost=1)
	T7t2_0_mem1 += INPUT_mem_r
	S += T7t2_0_mem1<=T7t2_0

	T7t2_1_mem0 = S.Task('T7t2_1_mem0', length=1, delay_cost=1)
	T7t2_1_mem0 += INPUT_mem_r
	S += T7t2_1_mem0<=T7t2_1

	T7t2_1_mem1 = S.Task('T7t2_1_mem1', length=1, delay_cost=1)
	T7t2_1_mem1 += INPUT_mem_r
	S += T7t2_1_mem1<=T7t2_1

	T7t0_a0b0_mem0 = S.Task('T7t0_a0b0_mem0', length=1, delay_cost=1)
	T7t0_a0b0_mem0 += INPUT_mem_r
	S += T7t0_a0b0_mem0<=T7t0_a0b0

	T7t0_a0b0_mem1 = S.Task('T7t0_a0b0_mem1', length=1, delay_cost=1)
	T7t0_a0b0_mem1 += INPUT_mem_r
	S += T7t0_a0b0_mem1<=T7t0_a0b0

	T7t1_a0b0_mem0 = S.Task('T7t1_a0b0_mem0', length=1, delay_cost=1)
	T7t1_a0b0_mem0 += INPUT_mem_r
	S += T7t1_a0b0_mem0<=T7t1_a0b0

	T7t1_a0b0_mem1 = S.Task('T7t1_a0b0_mem1', length=1, delay_cost=1)
	T7t1_a0b0_mem1 += INPUT_mem_r
	S += T7t1_a0b0_mem1<=T7t1_a0b0

	T7t2_a0b0_mem0 = S.Task('T7t2_a0b0_mem0', length=1, delay_cost=1)
	T7t2_a0b0_mem0 += INPUT_mem_r
	S += T7t2_a0b0_mem0<=T7t2_a0b0

	T7t2_a0b0_mem1 = S.Task('T7t2_a0b0_mem1', length=1, delay_cost=1)
	T7t2_a0b0_mem1 += INPUT_mem_r
	S += T7t2_a0b0_mem1<=T7t2_a0b0

	T7t0_a1b1_mem0 = S.Task('T7t0_a1b1_mem0', length=1, delay_cost=1)
	T7t0_a1b1_mem0 += INPUT_mem_r
	S += T7t0_a1b1_mem0<=T7t0_a1b1

	T7t0_a1b1_mem1 = S.Task('T7t0_a1b1_mem1', length=1, delay_cost=1)
	T7t0_a1b1_mem1 += INPUT_mem_r
	S += T7t0_a1b1_mem1<=T7t0_a1b1

	T7t1_a1b1_mem0 = S.Task('T7t1_a1b1_mem0', length=1, delay_cost=1)
	T7t1_a1b1_mem0 += INPUT_mem_r
	S += T7t1_a1b1_mem0<=T7t1_a1b1

	T7t1_a1b1_mem1 = S.Task('T7t1_a1b1_mem1', length=1, delay_cost=1)
	T7t1_a1b1_mem1 += INPUT_mem_r
	S += T7t1_a1b1_mem1<=T7t1_a1b1

	T7t2_a1b1_mem0 = S.Task('T7t2_a1b1_mem0', length=1, delay_cost=1)
	T7t2_a1b1_mem0 += INPUT_mem_r
	S += T7t2_a1b1_mem0<=T7t2_a1b1

	T7t2_a1b1_mem1 = S.Task('T7t2_a1b1_mem1', length=1, delay_cost=1)
	T7t2_a1b1_mem1 += INPUT_mem_r
	S += T7t2_a1b1_mem1<=T7t2_a1b1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sqr012345_mul1_add4/sqr012345_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sqr012345_mul1_add4_0(0, 0)