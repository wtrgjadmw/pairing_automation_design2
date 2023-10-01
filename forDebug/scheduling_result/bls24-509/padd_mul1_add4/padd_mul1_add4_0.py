from pyschedule import Scenario, solvers, plotters, alt

def solve_padd_mul1_add4_0(ConstStep, ExpStep):
	horizon = 98
	S=Scenario("padd_mul1_add4_0",horizon = horizon)

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

	T1t3_a1b1 = S.Task('T1t3_a1b1', length=1, delay_cost=1)
	T1t3_a1b1 += alt(ADD)

	T1t3_a1b1_mem0 = S.Task('T1t3_a1b1_mem0', length=1, delay_cost=1)
	T1t3_a1b1_mem0 += INPUT_mem_r
	S += T1t3_a1b1_mem0<=T1t3_a1b1

	T1t3_a1b1_mem1 = S.Task('T1t3_a1b1_mem1', length=1, delay_cost=1)
	T1t3_a1b1_mem1 += INPUT_mem_r
	S += T1t3_a1b1_mem1<=T1t3_a1b1

	T5t2_0 = S.Task('T5t2_0', length=1, delay_cost=1)
	T5t2_0 += alt(ADD)

	T5t2_0_mem0 = S.Task('T5t2_0_mem0', length=1, delay_cost=1)
	T5t2_0_mem0 += INPUT_mem_r
	S += T5t2_0_mem0<=T5t2_0

	T5t2_0_mem1 = S.Task('T5t2_0_mem1', length=1, delay_cost=1)
	T5t2_0_mem1 += INPUT_mem_r
	S += T5t2_0_mem1<=T5t2_0

	T5t2_1 = S.Task('T5t2_1', length=1, delay_cost=1)
	T5t2_1 += alt(ADD)

	T5t2_1_mem0 = S.Task('T5t2_1_mem0', length=1, delay_cost=1)
	T5t2_1_mem0 += INPUT_mem_r
	S += T5t2_1_mem0<=T5t2_1

	T5t2_1_mem1 = S.Task('T5t2_1_mem1', length=1, delay_cost=1)
	T5t2_1_mem1 += INPUT_mem_r
	S += T5t2_1_mem1<=T5t2_1

	T5t2_a0b0 = S.Task('T5t2_a0b0', length=1, delay_cost=1)
	T5t2_a0b0 += alt(ADD)

	T5t2_a0b0_mem0 = S.Task('T5t2_a0b0_mem0', length=1, delay_cost=1)
	T5t2_a0b0_mem0 += INPUT_mem_r
	S += T5t2_a0b0_mem0<=T5t2_a0b0

	T5t2_a0b0_mem1 = S.Task('T5t2_a0b0_mem1', length=1, delay_cost=1)
	T5t2_a0b0_mem1 += INPUT_mem_r
	S += T5t2_a0b0_mem1<=T5t2_a0b0

	T5t2_a1b1 = S.Task('T5t2_a1b1', length=1, delay_cost=1)
	T5t2_a1b1 += alt(ADD)

	T5t2_a1b1_mem0 = S.Task('T5t2_a1b1_mem0', length=1, delay_cost=1)
	T5t2_a1b1_mem0 += INPUT_mem_r
	S += T5t2_a1b1_mem0<=T5t2_a1b1

	T5t2_a1b1_mem1 = S.Task('T5t2_a1b1_mem1', length=1, delay_cost=1)
	T5t2_a1b1_mem1 += INPUT_mem_r
	S += T5t2_a1b1_mem1<=T5t2_a1b1

	T6t3_0 = S.Task('T6t3_0', length=1, delay_cost=1)
	T6t3_0 += alt(ADD)

	T6t3_0_mem0 = S.Task('T6t3_0_mem0', length=1, delay_cost=1)
	T6t3_0_mem0 += INPUT_mem_r
	S += T6t3_0_mem0<=T6t3_0

	T6t3_0_mem1 = S.Task('T6t3_0_mem1', length=1, delay_cost=1)
	T6t3_0_mem1 += INPUT_mem_r
	S += T6t3_0_mem1<=T6t3_0

	T6t3_1 = S.Task('T6t3_1', length=1, delay_cost=1)
	T6t3_1 += alt(ADD)

	T6t3_1_mem0 = S.Task('T6t3_1_mem0', length=1, delay_cost=1)
	T6t3_1_mem0 += INPUT_mem_r
	S += T6t3_1_mem0<=T6t3_1

	T6t3_1_mem1 = S.Task('T6t3_1_mem1', length=1, delay_cost=1)
	T6t3_1_mem1 += INPUT_mem_r
	S += T6t3_1_mem1<=T6t3_1

	T6t3_a0b0 = S.Task('T6t3_a0b0', length=1, delay_cost=1)
	T6t3_a0b0 += alt(ADD)

	T6t3_a0b0_mem0 = S.Task('T6t3_a0b0_mem0', length=1, delay_cost=1)
	T6t3_a0b0_mem0 += INPUT_mem_r
	S += T6t3_a0b0_mem0<=T6t3_a0b0

	T6t3_a0b0_mem1 = S.Task('T6t3_a0b0_mem1', length=1, delay_cost=1)
	T6t3_a0b0_mem1 += INPUT_mem_r
	S += T6t3_a0b0_mem1<=T6t3_a0b0

	T6t3_a1b1 = S.Task('T6t3_a1b1', length=1, delay_cost=1)
	T6t3_a1b1 += alt(ADD)

	T6t3_a1b1_mem0 = S.Task('T6t3_a1b1_mem0', length=1, delay_cost=1)
	T6t3_a1b1_mem0 += INPUT_mem_r
	S += T6t3_a1b1_mem0<=T6t3_a1b1

	T6t3_a1b1_mem1 = S.Task('T6t3_a1b1_mem1', length=1, delay_cost=1)
	T6t3_a1b1_mem1 += INPUT_mem_r
	S += T6t3_a1b1_mem1<=T6t3_a1b1

	T0t4_a0b0_in = S.Task('T0t4_a0b0_in', length=1, delay_cost=1)
	T0t4_a0b0_in += alt(MUL_in)
	T0t4_a0b0 = S.Task('T0t4_a0b0', length=7, delay_cost=1)
	T0t4_a0b0 += alt(MUL)
	S+=T0t4_a0b0>=T0t4_a0b0_in

	T0t4_a0b0_mem0 = S.Task('T0t4_a0b0_mem0', length=1, delay_cost=1)
	T0t4_a0b0_mem0 += alt(ADD_mem)
	S += (T0t2_a0b0*ADD[0])-1<T0t4_a0b0_mem0*ADD_mem[0]
	S += (T0t2_a0b0*ADD[1])-1<T0t4_a0b0_mem0*ADD_mem[1]
	S += (T0t2_a0b0*ADD[2])-1<T0t4_a0b0_mem0*ADD_mem[2]
	S += (T0t2_a0b0*ADD[3])-1<T0t4_a0b0_mem0*ADD_mem[3]
	S += T0t4_a0b0_mem0<=T0t4_a0b0

	T0t4_a0b0_mem1 = S.Task('T0t4_a0b0_mem1', length=1, delay_cost=1)
	T0t4_a0b0_mem1 += alt(ADD_mem)
	S += (T0t3_a0b0*ADD[0])-1<T0t4_a0b0_mem1*ADD_mem[0]
	S += (T0t3_a0b0*ADD[1])-1<T0t4_a0b0_mem1*ADD_mem[1]
	S += (T0t3_a0b0*ADD[2])-1<T0t4_a0b0_mem1*ADD_mem[2]
	S += (T0t3_a0b0*ADD[3])-1<T0t4_a0b0_mem1*ADD_mem[3]
	S += T0t4_a0b0_mem1<=T0t4_a0b0

	T0c0_a0b0 = S.Task('T0c0_a0b0', length=1, delay_cost=1)
	T0c0_a0b0 += alt(ADD)

	T0c0_a0b0_mem0 = S.Task('T0c0_a0b0_mem0', length=1, delay_cost=1)
	T0c0_a0b0_mem0 += alt(MUL_mem)
	S += (T0t0_a0b0*MUL[0])-1<T0c0_a0b0_mem0*MUL_mem[0]
	S += T0c0_a0b0_mem0<=T0c0_a0b0

	T0c0_a0b0_mem1 = S.Task('T0c0_a0b0_mem1', length=1, delay_cost=1)
	T0c0_a0b0_mem1 += alt(MUL_mem)
	S += (T0t1_a0b0*MUL[0])-1<T0c0_a0b0_mem1*MUL_mem[0]
	S += T0c0_a0b0_mem1<=T0c0_a0b0

	T0t6_a0b0 = S.Task('T0t6_a0b0', length=1, delay_cost=1)
	T0t6_a0b0 += alt(ADD)

	T0t6_a0b0_mem0 = S.Task('T0t6_a0b0_mem0', length=1, delay_cost=1)
	T0t6_a0b0_mem0 += alt(MUL_mem)
	S += (T0t0_a0b0*MUL[0])-1<T0t6_a0b0_mem0*MUL_mem[0]
	S += T0t6_a0b0_mem0<=T0t6_a0b0

	T0t6_a0b0_mem1 = S.Task('T0t6_a0b0_mem1', length=1, delay_cost=1)
	T0t6_a0b0_mem1 += alt(MUL_mem)
	S += (T0t1_a0b0*MUL[0])-1<T0t6_a0b0_mem1*MUL_mem[0]
	S += T0t6_a0b0_mem1<=T0t6_a0b0

	T0t4_a1b1_in = S.Task('T0t4_a1b1_in', length=1, delay_cost=1)
	T0t4_a1b1_in += alt(MUL_in)
	T0t4_a1b1 = S.Task('T0t4_a1b1', length=7, delay_cost=1)
	T0t4_a1b1 += alt(MUL)
	S+=T0t4_a1b1>=T0t4_a1b1_in

	T0t4_a1b1_mem0 = S.Task('T0t4_a1b1_mem0', length=1, delay_cost=1)
	T0t4_a1b1_mem0 += alt(ADD_mem)
	S += (T0t2_a1b1*ADD[0])-1<T0t4_a1b1_mem0*ADD_mem[0]
	S += (T0t2_a1b1*ADD[1])-1<T0t4_a1b1_mem0*ADD_mem[1]
	S += (T0t2_a1b1*ADD[2])-1<T0t4_a1b1_mem0*ADD_mem[2]
	S += (T0t2_a1b1*ADD[3])-1<T0t4_a1b1_mem0*ADD_mem[3]
	S += T0t4_a1b1_mem0<=T0t4_a1b1

	T0t4_a1b1_mem1 = S.Task('T0t4_a1b1_mem1', length=1, delay_cost=1)
	T0t4_a1b1_mem1 += alt(ADD_mem)
	S += (T0t3_a1b1*ADD[0])-1<T0t4_a1b1_mem1*ADD_mem[0]
	S += (T0t3_a1b1*ADD[1])-1<T0t4_a1b1_mem1*ADD_mem[1]
	S += (T0t3_a1b1*ADD[2])-1<T0t4_a1b1_mem1*ADD_mem[2]
	S += (T0t3_a1b1*ADD[3])-1<T0t4_a1b1_mem1*ADD_mem[3]
	S += T0t4_a1b1_mem1<=T0t4_a1b1

	T0c0_a1b1 = S.Task('T0c0_a1b1', length=1, delay_cost=1)
	T0c0_a1b1 += alt(ADD)

	T0c0_a1b1_mem0 = S.Task('T0c0_a1b1_mem0', length=1, delay_cost=1)
	T0c0_a1b1_mem0 += alt(MUL_mem)
	S += (T0t0_a1b1*MUL[0])-1<T0c0_a1b1_mem0*MUL_mem[0]
	S += T0c0_a1b1_mem0<=T0c0_a1b1

	T0c0_a1b1_mem1 = S.Task('T0c0_a1b1_mem1', length=1, delay_cost=1)
	T0c0_a1b1_mem1 += alt(MUL_mem)
	S += (T0t1_a1b1*MUL[0])-1<T0c0_a1b1_mem1*MUL_mem[0]
	S += T0c0_a1b1_mem1<=T0c0_a1b1

	T0t6_a1b1 = S.Task('T0t6_a1b1', length=1, delay_cost=1)
	T0t6_a1b1 += alt(ADD)

	T0t6_a1b1_mem0 = S.Task('T0t6_a1b1_mem0', length=1, delay_cost=1)
	T0t6_a1b1_mem0 += alt(MUL_mem)
	S += (T0t0_a1b1*MUL[0])-1<T0t6_a1b1_mem0*MUL_mem[0]
	S += T0t6_a1b1_mem0<=T0t6_a1b1

	T0t6_a1b1_mem1 = S.Task('T0t6_a1b1_mem1', length=1, delay_cost=1)
	T0t6_a1b1_mem1 += alt(MUL_mem)
	S += (T0t1_a1b1*MUL[0])-1<T0t6_a1b1_mem1*MUL_mem[0]
	S += T0t6_a1b1_mem1<=T0t6_a1b1

	T0t0_t2t3_in = S.Task('T0t0_t2t3_in', length=1, delay_cost=1)
	T0t0_t2t3_in += alt(MUL_in)
	T0t0_t2t3 = S.Task('T0t0_t2t3', length=7, delay_cost=1)
	T0t0_t2t3 += alt(MUL)
	S+=T0t0_t2t3>=T0t0_t2t3_in

	T0t0_t2t3_mem0 = S.Task('T0t0_t2t3_mem0', length=1, delay_cost=1)
	T0t0_t2t3_mem0 += alt(ADD_mem)
	S += (T0t2_0*ADD[0])-1<T0t0_t2t3_mem0*ADD_mem[0]
	S += (T0t2_0*ADD[1])-1<T0t0_t2t3_mem0*ADD_mem[1]
	S += (T0t2_0*ADD[2])-1<T0t0_t2t3_mem0*ADD_mem[2]
	S += (T0t2_0*ADD[3])-1<T0t0_t2t3_mem0*ADD_mem[3]
	S += T0t0_t2t3_mem0<=T0t0_t2t3

	T0t0_t2t3_mem1 = S.Task('T0t0_t2t3_mem1', length=1, delay_cost=1)
	T0t0_t2t3_mem1 += alt(ADD_mem)
	S += (T0t3_0*ADD[0])-1<T0t0_t2t3_mem1*ADD_mem[0]
	S += (T0t3_0*ADD[1])-1<T0t0_t2t3_mem1*ADD_mem[1]
	S += (T0t3_0*ADD[2])-1<T0t0_t2t3_mem1*ADD_mem[2]
	S += (T0t3_0*ADD[3])-1<T0t0_t2t3_mem1*ADD_mem[3]
	S += T0t0_t2t3_mem1<=T0t0_t2t3

	T0t1_t2t3_in = S.Task('T0t1_t2t3_in', length=1, delay_cost=1)
	T0t1_t2t3_in += alt(MUL_in)
	T0t1_t2t3 = S.Task('T0t1_t2t3', length=7, delay_cost=1)
	T0t1_t2t3 += alt(MUL)
	S+=T0t1_t2t3>=T0t1_t2t3_in

	T0t1_t2t3_mem0 = S.Task('T0t1_t2t3_mem0', length=1, delay_cost=1)
	T0t1_t2t3_mem0 += alt(ADD_mem)
	S += (T0t2_1*ADD[0])-1<T0t1_t2t3_mem0*ADD_mem[0]
	S += (T0t2_1*ADD[1])-1<T0t1_t2t3_mem0*ADD_mem[1]
	S += (T0t2_1*ADD[2])-1<T0t1_t2t3_mem0*ADD_mem[2]
	S += (T0t2_1*ADD[3])-1<T0t1_t2t3_mem0*ADD_mem[3]
	S += T0t1_t2t3_mem0<=T0t1_t2t3

	T0t1_t2t3_mem1 = S.Task('T0t1_t2t3_mem1', length=1, delay_cost=1)
	T0t1_t2t3_mem1 += alt(ADD_mem)
	S += (T0t3_1*ADD[0])-1<T0t1_t2t3_mem1*ADD_mem[0]
	S += (T0t3_1*ADD[1])-1<T0t1_t2t3_mem1*ADD_mem[1]
	S += (T0t3_1*ADD[2])-1<T0t1_t2t3_mem1*ADD_mem[2]
	S += (T0t3_1*ADD[3])-1<T0t1_t2t3_mem1*ADD_mem[3]
	S += T0t1_t2t3_mem1<=T0t1_t2t3

	T0t2_t2t3 = S.Task('T0t2_t2t3', length=1, delay_cost=1)
	T0t2_t2t3 += alt(ADD)

	T0t2_t2t3_mem0 = S.Task('T0t2_t2t3_mem0', length=1, delay_cost=1)
	T0t2_t2t3_mem0 += alt(ADD_mem)
	S += (T0t2_0*ADD[0])-1<T0t2_t2t3_mem0*ADD_mem[0]
	S += (T0t2_0*ADD[1])-1<T0t2_t2t3_mem0*ADD_mem[1]
	S += (T0t2_0*ADD[2])-1<T0t2_t2t3_mem0*ADD_mem[2]
	S += (T0t2_0*ADD[3])-1<T0t2_t2t3_mem0*ADD_mem[3]
	S += T0t2_t2t3_mem0<=T0t2_t2t3

	T0t2_t2t3_mem1 = S.Task('T0t2_t2t3_mem1', length=1, delay_cost=1)
	T0t2_t2t3_mem1 += alt(ADD_mem)
	S += (T0t2_1*ADD[0])-1<T0t2_t2t3_mem1*ADD_mem[0]
	S += (T0t2_1*ADD[1])-1<T0t2_t2t3_mem1*ADD_mem[1]
	S += (T0t2_1*ADD[2])-1<T0t2_t2t3_mem1*ADD_mem[2]
	S += (T0t2_1*ADD[3])-1<T0t2_t2t3_mem1*ADD_mem[3]
	S += T0t2_t2t3_mem1<=T0t2_t2t3

	T0t3_t2t3 = S.Task('T0t3_t2t3', length=1, delay_cost=1)
	T0t3_t2t3 += alt(ADD)

	T0t3_t2t3_mem0 = S.Task('T0t3_t2t3_mem0', length=1, delay_cost=1)
	T0t3_t2t3_mem0 += alt(ADD_mem)
	S += (T0t3_0*ADD[0])-1<T0t3_t2t3_mem0*ADD_mem[0]
	S += (T0t3_0*ADD[1])-1<T0t3_t2t3_mem0*ADD_mem[1]
	S += (T0t3_0*ADD[2])-1<T0t3_t2t3_mem0*ADD_mem[2]
	S += (T0t3_0*ADD[3])-1<T0t3_t2t3_mem0*ADD_mem[3]
	S += T0t3_t2t3_mem0<=T0t3_t2t3

	T0t3_t2t3_mem1 = S.Task('T0t3_t2t3_mem1', length=1, delay_cost=1)
	T0t3_t2t3_mem1 += alt(ADD_mem)
	S += (T0t3_1*ADD[0])-1<T0t3_t2t3_mem1*ADD_mem[0]
	S += (T0t3_1*ADD[1])-1<T0t3_t2t3_mem1*ADD_mem[1]
	S += (T0t3_1*ADD[2])-1<T0t3_t2t3_mem1*ADD_mem[2]
	S += (T0t3_1*ADD[3])-1<T0t3_t2t3_mem1*ADD_mem[3]
	S += T0t3_t2t3_mem1<=T0t3_t2t3

	T1t4_a0b0_in = S.Task('T1t4_a0b0_in', length=1, delay_cost=1)
	T1t4_a0b0_in += alt(MUL_in)
	T1t4_a0b0 = S.Task('T1t4_a0b0', length=7, delay_cost=1)
	T1t4_a0b0 += alt(MUL)
	S+=T1t4_a0b0>=T1t4_a0b0_in

	T1t4_a0b0_mem0 = S.Task('T1t4_a0b0_mem0', length=1, delay_cost=1)
	T1t4_a0b0_mem0 += alt(ADD_mem)
	S += (T0t2_a0b0*ADD[0])-1<T1t4_a0b0_mem0*ADD_mem[0]
	S += (T0t2_a0b0*ADD[1])-1<T1t4_a0b0_mem0*ADD_mem[1]
	S += (T0t2_a0b0*ADD[2])-1<T1t4_a0b0_mem0*ADD_mem[2]
	S += (T0t2_a0b0*ADD[3])-1<T1t4_a0b0_mem0*ADD_mem[3]
	S += T1t4_a0b0_mem0<=T1t4_a0b0

	T1t4_a0b0_mem1 = S.Task('T1t4_a0b0_mem1', length=1, delay_cost=1)
	T1t4_a0b0_mem1 += alt(ADD_mem)
	S += (T1t3_a0b0*ADD[0])-1<T1t4_a0b0_mem1*ADD_mem[0]
	S += (T1t3_a0b0*ADD[1])-1<T1t4_a0b0_mem1*ADD_mem[1]
	S += (T1t3_a0b0*ADD[2])-1<T1t4_a0b0_mem1*ADD_mem[2]
	S += (T1t3_a0b0*ADD[3])-1<T1t4_a0b0_mem1*ADD_mem[3]
	S += T1t4_a0b0_mem1<=T1t4_a0b0

	T1c0_a0b0 = S.Task('T1c0_a0b0', length=1, delay_cost=1)
	T1c0_a0b0 += alt(ADD)

	T1c0_a0b0_mem0 = S.Task('T1c0_a0b0_mem0', length=1, delay_cost=1)
	T1c0_a0b0_mem0 += alt(MUL_mem)
	S += (T1t0_a0b0*MUL[0])-1<T1c0_a0b0_mem0*MUL_mem[0]
	S += T1c0_a0b0_mem0<=T1c0_a0b0

	T1c0_a0b0_mem1 = S.Task('T1c0_a0b0_mem1', length=1, delay_cost=1)
	T1c0_a0b0_mem1 += alt(MUL_mem)
	S += (T1t1_a0b0*MUL[0])-1<T1c0_a0b0_mem1*MUL_mem[0]
	S += T1c0_a0b0_mem1<=T1c0_a0b0

	T1t6_a0b0 = S.Task('T1t6_a0b0', length=1, delay_cost=1)
	T1t6_a0b0 += alt(ADD)

	T1t6_a0b0_mem0 = S.Task('T1t6_a0b0_mem0', length=1, delay_cost=1)
	T1t6_a0b0_mem0 += alt(MUL_mem)
	S += (T1t0_a0b0*MUL[0])-1<T1t6_a0b0_mem0*MUL_mem[0]
	S += T1t6_a0b0_mem0<=T1t6_a0b0

	T1t6_a0b0_mem1 = S.Task('T1t6_a0b0_mem1', length=1, delay_cost=1)
	T1t6_a0b0_mem1 += alt(MUL_mem)
	S += (T1t1_a0b0*MUL[0])-1<T1t6_a0b0_mem1*MUL_mem[0]
	S += T1t6_a0b0_mem1<=T1t6_a0b0

	T1t4_a1b1_in = S.Task('T1t4_a1b1_in', length=1, delay_cost=1)
	T1t4_a1b1_in += alt(MUL_in)
	T1t4_a1b1 = S.Task('T1t4_a1b1', length=7, delay_cost=1)
	T1t4_a1b1 += alt(MUL)
	S+=T1t4_a1b1>=T1t4_a1b1_in

	T1t4_a1b1_mem0 = S.Task('T1t4_a1b1_mem0', length=1, delay_cost=1)
	T1t4_a1b1_mem0 += alt(ADD_mem)
	S += (T0t2_a1b1*ADD[0])-1<T1t4_a1b1_mem0*ADD_mem[0]
	S += (T0t2_a1b1*ADD[1])-1<T1t4_a1b1_mem0*ADD_mem[1]
	S += (T0t2_a1b1*ADD[2])-1<T1t4_a1b1_mem0*ADD_mem[2]
	S += (T0t2_a1b1*ADD[3])-1<T1t4_a1b1_mem0*ADD_mem[3]
	S += T1t4_a1b1_mem0<=T1t4_a1b1

	T1t4_a1b1_mem1 = S.Task('T1t4_a1b1_mem1', length=1, delay_cost=1)
	T1t4_a1b1_mem1 += alt(ADD_mem)
	S += (T1t3_a1b1*ADD[0])-1<T1t4_a1b1_mem1*ADD_mem[0]
	S += (T1t3_a1b1*ADD[1])-1<T1t4_a1b1_mem1*ADD_mem[1]
	S += (T1t3_a1b1*ADD[2])-1<T1t4_a1b1_mem1*ADD_mem[2]
	S += (T1t3_a1b1*ADD[3])-1<T1t4_a1b1_mem1*ADD_mem[3]
	S += T1t4_a1b1_mem1<=T1t4_a1b1

	T1c0_a1b1 = S.Task('T1c0_a1b1', length=1, delay_cost=1)
	T1c0_a1b1 += alt(ADD)

	T1c0_a1b1_mem0 = S.Task('T1c0_a1b1_mem0', length=1, delay_cost=1)
	T1c0_a1b1_mem0 += alt(MUL_mem)
	S += (T1t0_a1b1*MUL[0])-1<T1c0_a1b1_mem0*MUL_mem[0]
	S += T1c0_a1b1_mem0<=T1c0_a1b1

	T1c0_a1b1_mem1 = S.Task('T1c0_a1b1_mem1', length=1, delay_cost=1)
	T1c0_a1b1_mem1 += alt(MUL_mem)
	S += (T1t1_a1b1*MUL[0])-1<T1c0_a1b1_mem1*MUL_mem[0]
	S += T1c0_a1b1_mem1<=T1c0_a1b1

	T1t6_a1b1 = S.Task('T1t6_a1b1', length=1, delay_cost=1)
	T1t6_a1b1 += alt(ADD)

	T1t6_a1b1_mem0 = S.Task('T1t6_a1b1_mem0', length=1, delay_cost=1)
	T1t6_a1b1_mem0 += alt(MUL_mem)
	S += (T1t0_a1b1*MUL[0])-1<T1t6_a1b1_mem0*MUL_mem[0]
	S += T1t6_a1b1_mem0<=T1t6_a1b1

	T1t6_a1b1_mem1 = S.Task('T1t6_a1b1_mem1', length=1, delay_cost=1)
	T1t6_a1b1_mem1 += alt(MUL_mem)
	S += (T1t1_a1b1*MUL[0])-1<T1t6_a1b1_mem1*MUL_mem[0]
	S += T1t6_a1b1_mem1<=T1t6_a1b1

	T1t0_t2t3_in = S.Task('T1t0_t2t3_in', length=1, delay_cost=1)
	T1t0_t2t3_in += alt(MUL_in)
	T1t0_t2t3 = S.Task('T1t0_t2t3', length=7, delay_cost=1)
	T1t0_t2t3 += alt(MUL)
	S+=T1t0_t2t3>=T1t0_t2t3_in

	T1t0_t2t3_mem0 = S.Task('T1t0_t2t3_mem0', length=1, delay_cost=1)
	T1t0_t2t3_mem0 += alt(ADD_mem)
	S += (T0t2_0*ADD[0])-1<T1t0_t2t3_mem0*ADD_mem[0]
	S += (T0t2_0*ADD[1])-1<T1t0_t2t3_mem0*ADD_mem[1]
	S += (T0t2_0*ADD[2])-1<T1t0_t2t3_mem0*ADD_mem[2]
	S += (T0t2_0*ADD[3])-1<T1t0_t2t3_mem0*ADD_mem[3]
	S += T1t0_t2t3_mem0<=T1t0_t2t3

	T1t0_t2t3_mem1 = S.Task('T1t0_t2t3_mem1', length=1, delay_cost=1)
	T1t0_t2t3_mem1 += alt(ADD_mem)
	S += (T1t3_0*ADD[0])-1<T1t0_t2t3_mem1*ADD_mem[0]
	S += (T1t3_0*ADD[1])-1<T1t0_t2t3_mem1*ADD_mem[1]
	S += (T1t3_0*ADD[2])-1<T1t0_t2t3_mem1*ADD_mem[2]
	S += (T1t3_0*ADD[3])-1<T1t0_t2t3_mem1*ADD_mem[3]
	S += T1t0_t2t3_mem1<=T1t0_t2t3

	T1t1_t2t3_in = S.Task('T1t1_t2t3_in', length=1, delay_cost=1)
	T1t1_t2t3_in += alt(MUL_in)
	T1t1_t2t3 = S.Task('T1t1_t2t3', length=7, delay_cost=1)
	T1t1_t2t3 += alt(MUL)
	S+=T1t1_t2t3>=T1t1_t2t3_in

	T1t1_t2t3_mem0 = S.Task('T1t1_t2t3_mem0', length=1, delay_cost=1)
	T1t1_t2t3_mem0 += alt(ADD_mem)
	S += (T0t2_1*ADD[0])-1<T1t1_t2t3_mem0*ADD_mem[0]
	S += (T0t2_1*ADD[1])-1<T1t1_t2t3_mem0*ADD_mem[1]
	S += (T0t2_1*ADD[2])-1<T1t1_t2t3_mem0*ADD_mem[2]
	S += (T0t2_1*ADD[3])-1<T1t1_t2t3_mem0*ADD_mem[3]
	S += T1t1_t2t3_mem0<=T1t1_t2t3

	T1t1_t2t3_mem1 = S.Task('T1t1_t2t3_mem1', length=1, delay_cost=1)
	T1t1_t2t3_mem1 += alt(ADD_mem)
	S += (T1t3_1*ADD[0])-1<T1t1_t2t3_mem1*ADD_mem[0]
	S += (T1t3_1*ADD[1])-1<T1t1_t2t3_mem1*ADD_mem[1]
	S += (T1t3_1*ADD[2])-1<T1t1_t2t3_mem1*ADD_mem[2]
	S += (T1t3_1*ADD[3])-1<T1t1_t2t3_mem1*ADD_mem[3]
	S += T1t1_t2t3_mem1<=T1t1_t2t3

	T1t3_t2t3 = S.Task('T1t3_t2t3', length=1, delay_cost=1)
	T1t3_t2t3 += alt(ADD)

	T1t3_t2t3_mem0 = S.Task('T1t3_t2t3_mem0', length=1, delay_cost=1)
	T1t3_t2t3_mem0 += alt(ADD_mem)
	S += (T1t3_0*ADD[0])-1<T1t3_t2t3_mem0*ADD_mem[0]
	S += (T1t3_0*ADD[1])-1<T1t3_t2t3_mem0*ADD_mem[1]
	S += (T1t3_0*ADD[2])-1<T1t3_t2t3_mem0*ADD_mem[2]
	S += (T1t3_0*ADD[3])-1<T1t3_t2t3_mem0*ADD_mem[3]
	S += T1t3_t2t3_mem0<=T1t3_t2t3

	T1t3_t2t3_mem1 = S.Task('T1t3_t2t3_mem1', length=1, delay_cost=1)
	T1t3_t2t3_mem1 += alt(ADD_mem)
	S += (T1t3_1*ADD[0])-1<T1t3_t2t3_mem1*ADD_mem[0]
	S += (T1t3_1*ADD[1])-1<T1t3_t2t3_mem1*ADD_mem[1]
	S += (T1t3_1*ADD[2])-1<T1t3_t2t3_mem1*ADD_mem[2]
	S += (T1t3_1*ADD[3])-1<T1t3_t2t3_mem1*ADD_mem[3]
	S += T1t3_t2t3_mem1<=T1t3_t2t3

	T5t2_t2t3 = S.Task('T5t2_t2t3', length=1, delay_cost=1)
	T5t2_t2t3 += alt(ADD)

	T5t2_t2t3_mem0 = S.Task('T5t2_t2t3_mem0', length=1, delay_cost=1)
	T5t2_t2t3_mem0 += alt(ADD_mem)
	S += (T5t2_0*ADD[0])-1<T5t2_t2t3_mem0*ADD_mem[0]
	S += (T5t2_0*ADD[1])-1<T5t2_t2t3_mem0*ADD_mem[1]
	S += (T5t2_0*ADD[2])-1<T5t2_t2t3_mem0*ADD_mem[2]
	S += (T5t2_0*ADD[3])-1<T5t2_t2t3_mem0*ADD_mem[3]
	S += T5t2_t2t3_mem0<=T5t2_t2t3

	T5t2_t2t3_mem1 = S.Task('T5t2_t2t3_mem1', length=1, delay_cost=1)
	T5t2_t2t3_mem1 += alt(ADD_mem)
	S += (T5t2_1*ADD[0])-1<T5t2_t2t3_mem1*ADD_mem[0]
	S += (T5t2_1*ADD[1])-1<T5t2_t2t3_mem1*ADD_mem[1]
	S += (T5t2_1*ADD[2])-1<T5t2_t2t3_mem1*ADD_mem[2]
	S += (T5t2_1*ADD[3])-1<T5t2_t2t3_mem1*ADD_mem[3]
	S += T5t2_t2t3_mem1<=T5t2_t2t3

	T6t3_t2t3 = S.Task('T6t3_t2t3', length=1, delay_cost=1)
	T6t3_t2t3 += alt(ADD)

	T6t3_t2t3_mem0 = S.Task('T6t3_t2t3_mem0', length=1, delay_cost=1)
	T6t3_t2t3_mem0 += alt(ADD_mem)
	S += (T6t3_0*ADD[0])-1<T6t3_t2t3_mem0*ADD_mem[0]
	S += (T6t3_0*ADD[1])-1<T6t3_t2t3_mem0*ADD_mem[1]
	S += (T6t3_0*ADD[2])-1<T6t3_t2t3_mem0*ADD_mem[2]
	S += (T6t3_0*ADD[3])-1<T6t3_t2t3_mem0*ADD_mem[3]
	S += T6t3_t2t3_mem0<=T6t3_t2t3

	T6t3_t2t3_mem1 = S.Task('T6t3_t2t3_mem1', length=1, delay_cost=1)
	T6t3_t2t3_mem1 += alt(ADD_mem)
	S += (T6t3_1*ADD[0])-1<T6t3_t2t3_mem1*ADD_mem[0]
	S += (T6t3_1*ADD[1])-1<T6t3_t2t3_mem1*ADD_mem[1]
	S += (T6t3_1*ADD[2])-1<T6t3_t2t3_mem1*ADD_mem[2]
	S += (T6t3_1*ADD[3])-1<T6t3_t2t3_mem1*ADD_mem[3]
	S += T6t3_t2t3_mem1<=T6t3_t2t3

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "padd_mul1_add4/padd_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_padd_mul1_add4_0(0, 0)