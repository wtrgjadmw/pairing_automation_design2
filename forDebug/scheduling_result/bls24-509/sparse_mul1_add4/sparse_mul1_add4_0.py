from pyschedule import Scenario, solvers, plotters, alt

def solve_sparse_mul1_add4_0(ConstStep, ExpStep):
	horizon = 144
	S=Scenario("sparse_mul1_add4_0",horizon = horizon)

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

	T0t2_1 = S.Task('T0t2_1', length=1, delay_cost=1)
	T0t2_1 += alt(ADD)

	T0t3_0 = S.Task('T0t3_0', length=1, delay_cost=1)
	T0t3_0 += alt(ADD)

	T0t3_1 = S.Task('T0t3_1', length=1, delay_cost=1)
	T0t3_1 += alt(ADD)

	T0t0_a0b0_in = S.Task('T0t0_a0b0_in', length=1, delay_cost=1)
	T0t0_a0b0_in += alt(MUL_in)
	T0t0_a0b0 = S.Task('T0t0_a0b0', length=7, delay_cost=1)
	T0t0_a0b0 += alt(MUL)
	S+=T0t0_a0b0>=T0t0_a0b0_in

	T0t1_a0b0_in = S.Task('T0t1_a0b0_in', length=1, delay_cost=1)
	T0t1_a0b0_in += alt(MUL_in)
	T0t1_a0b0 = S.Task('T0t1_a0b0', length=7, delay_cost=1)
	T0t1_a0b0 += alt(MUL)
	S+=T0t1_a0b0>=T0t1_a0b0_in

	T0t2_a0b0 = S.Task('T0t2_a0b0', length=1, delay_cost=1)
	T0t2_a0b0 += alt(ADD)

	T0t3_a0b0 = S.Task('T0t3_a0b0', length=1, delay_cost=1)
	T0t3_a0b0 += alt(ADD)

	T0t0_a1b1_in = S.Task('T0t0_a1b1_in', length=1, delay_cost=1)
	T0t0_a1b1_in += alt(MUL_in)
	T0t0_a1b1 = S.Task('T0t0_a1b1', length=7, delay_cost=1)
	T0t0_a1b1 += alt(MUL)
	S+=T0t0_a1b1>=T0t0_a1b1_in

	T0t1_a1b1_in = S.Task('T0t1_a1b1_in', length=1, delay_cost=1)
	T0t1_a1b1_in += alt(MUL_in)
	T0t1_a1b1 = S.Task('T0t1_a1b1', length=7, delay_cost=1)
	T0t1_a1b1 += alt(MUL)
	S+=T0t1_a1b1>=T0t1_a1b1_in

	T0t2_a1b1 = S.Task('T0t2_a1b1', length=1, delay_cost=1)
	T0t2_a1b1 += alt(ADD)

	T0t3_a1b1 = S.Task('T0t3_a1b1', length=1, delay_cost=1)
	T0t3_a1b1 += alt(ADD)

	T1t3_0 = S.Task('T1t3_0', length=1, delay_cost=1)
	T1t3_0 += alt(ADD)

	T1t3_1 = S.Task('T1t3_1', length=1, delay_cost=1)
	T1t3_1 += alt(ADD)

	T1t0_a0b0_in = S.Task('T1t0_a0b0_in', length=1, delay_cost=1)
	T1t0_a0b0_in += alt(MUL_in)
	T1t0_a0b0 = S.Task('T1t0_a0b0', length=7, delay_cost=1)
	T1t0_a0b0 += alt(MUL)
	S+=T1t0_a0b0>=T1t0_a0b0_in

	T1t1_a0b0_in = S.Task('T1t1_a0b0_in', length=1, delay_cost=1)
	T1t1_a0b0_in += alt(MUL_in)
	T1t1_a0b0 = S.Task('T1t1_a0b0', length=7, delay_cost=1)
	T1t1_a0b0 += alt(MUL)
	S+=T1t1_a0b0>=T1t1_a0b0_in

	T1t3_a0b0 = S.Task('T1t3_a0b0', length=1, delay_cost=1)
	T1t3_a0b0 += alt(ADD)

	T1t0_a1b1_in = S.Task('T1t0_a1b1_in', length=1, delay_cost=1)
	T1t0_a1b1_in += alt(MUL_in)
	T1t0_a1b1 = S.Task('T1t0_a1b1', length=7, delay_cost=1)
	T1t0_a1b1 += alt(MUL)
	S+=T1t0_a1b1>=T1t0_a1b1_in

	T1t1_a1b1_in = S.Task('T1t1_a1b1_in', length=1, delay_cost=1)
	T1t1_a1b1_in += alt(MUL_in)
	T1t1_a1b1 = S.Task('T1t1_a1b1', length=7, delay_cost=1)
	T1t1_a1b1 += alt(MUL)
	S+=T1t1_a1b1>=T1t1_a1b1_in

	T1t3_a1b1 = S.Task('T1t3_a1b1', length=1, delay_cost=1)
	T1t3_a1b1 += alt(ADD)

	T2t3_0 = S.Task('T2t3_0', length=1, delay_cost=1)
	T2t3_0 += alt(ADD)

	T2t3_1 = S.Task('T2t3_1', length=1, delay_cost=1)
	T2t3_1 += alt(ADD)

	T2t0_a0b0_in = S.Task('T2t0_a0b0_in', length=1, delay_cost=1)
	T2t0_a0b0_in += alt(MUL_in)
	T2t0_a0b0 = S.Task('T2t0_a0b0', length=7, delay_cost=1)
	T2t0_a0b0 += alt(MUL)
	S+=T2t0_a0b0>=T2t0_a0b0_in

	T2t1_a0b0_in = S.Task('T2t1_a0b0_in', length=1, delay_cost=1)
	T2t1_a0b0_in += alt(MUL_in)
	T2t1_a0b0 = S.Task('T2t1_a0b0', length=7, delay_cost=1)
	T2t1_a0b0 += alt(MUL)
	S+=T2t1_a0b0>=T2t1_a0b0_in

	T2t3_a0b0 = S.Task('T2t3_a0b0', length=1, delay_cost=1)
	T2t3_a0b0 += alt(ADD)

	T2t0_a1b1_in = S.Task('T2t0_a1b1_in', length=1, delay_cost=1)
	T2t0_a1b1_in += alt(MUL_in)
	T2t0_a1b1 = S.Task('T2t0_a1b1', length=7, delay_cost=1)
	T2t0_a1b1 += alt(MUL)
	S+=T2t0_a1b1>=T2t0_a1b1_in

	T2t1_a1b1_in = S.Task('T2t1_a1b1_in', length=1, delay_cost=1)
	T2t1_a1b1_in += alt(MUL_in)
	T2t1_a1b1 = S.Task('T2t1_a1b1', length=7, delay_cost=1)
	T2t1_a1b1 += alt(MUL)
	S+=T2t1_a1b1>=T2t1_a1b1_in

	T2t3_a1b1 = S.Task('T2t3_a1b1', length=1, delay_cost=1)
	T2t3_a1b1 += alt(ADD)

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

	T4t2_0 = S.Task('T4t2_0', length=1, delay_cost=1)
	T4t2_0 += alt(ADD)

	T4t2_1 = S.Task('T4t2_1', length=1, delay_cost=1)
	T4t2_1 += alt(ADD)

	T4t3_0 = S.Task('T4t3_0', length=1, delay_cost=1)
	T4t3_0 += alt(ADD)

	T4t3_1 = S.Task('T4t3_1', length=1, delay_cost=1)
	T4t3_1 += alt(ADD)

	T4t0_a0b0_in = S.Task('T4t0_a0b0_in', length=1, delay_cost=1)
	T4t0_a0b0_in += alt(MUL_in)
	T4t0_a0b0 = S.Task('T4t0_a0b0', length=7, delay_cost=1)
	T4t0_a0b0 += alt(MUL)
	S+=T4t0_a0b0>=T4t0_a0b0_in

	T4t1_a0b0_in = S.Task('T4t1_a0b0_in', length=1, delay_cost=1)
	T4t1_a0b0_in += alt(MUL_in)
	T4t1_a0b0 = S.Task('T4t1_a0b0', length=7, delay_cost=1)
	T4t1_a0b0 += alt(MUL)
	S+=T4t1_a0b0>=T4t1_a0b0_in

	T4t2_a0b0 = S.Task('T4t2_a0b0', length=1, delay_cost=1)
	T4t2_a0b0 += alt(ADD)

	T4t3_a0b0 = S.Task('T4t3_a0b0', length=1, delay_cost=1)
	T4t3_a0b0 += alt(ADD)

	T4t0_a1b1_in = S.Task('T4t0_a1b1_in', length=1, delay_cost=1)
	T4t0_a1b1_in += alt(MUL_in)
	T4t0_a1b1 = S.Task('T4t0_a1b1', length=7, delay_cost=1)
	T4t0_a1b1 += alt(MUL)
	S+=T4t0_a1b1>=T4t0_a1b1_in

	T4t1_a1b1_in = S.Task('T4t1_a1b1_in', length=1, delay_cost=1)
	T4t1_a1b1_in += alt(MUL_in)
	T4t1_a1b1 = S.Task('T4t1_a1b1', length=7, delay_cost=1)
	T4t1_a1b1 += alt(MUL)
	S+=T4t1_a1b1>=T4t1_a1b1_in

	T4t2_a1b1 = S.Task('T4t2_a1b1', length=1, delay_cost=1)
	T4t2_a1b1 += alt(ADD)

	T4t3_a1b1 = S.Task('T4t3_a1b1', length=1, delay_cost=1)
	T4t3_a1b1 += alt(ADD)

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

	T600 = S.Task('T600', length=1, delay_cost=1)
	T600 += alt(ADD)

	T601 = S.Task('T601', length=1, delay_cost=1)
	T601 += alt(ADD)

	T610 = S.Task('T610', length=1, delay_cost=1)
	T610 += alt(ADD)

	T611 = S.Task('T611', length=1, delay_cost=1)
	T611 += alt(ADD)

	T700 = S.Task('T700', length=1, delay_cost=1)
	T700 += alt(ADD)

	T701 = S.Task('T701', length=1, delay_cost=1)
	T701 += alt(ADD)

	T710 = S.Task('T710', length=1, delay_cost=1)
	T710 += alt(ADD)

	T711 = S.Task('T711', length=1, delay_cost=1)
	T711 += alt(ADD)

	T6_2t0_a0b0_in = S.Task('T6_2t0_a0b0_in', length=1, delay_cost=1)
	T6_2t0_a0b0_in += alt(MUL_in)
	T6_2t0_a0b0 = S.Task('T6_2t0_a0b0', length=7, delay_cost=1)
	T6_2t0_a0b0 += alt(MUL)
	S+=T6_2t0_a0b0>=T6_2t0_a0b0_in

	T6_2t1_a0b0_in = S.Task('T6_2t1_a0b0_in', length=1, delay_cost=1)
	T6_2t1_a0b0_in += alt(MUL_in)
	T6_2t1_a0b0 = S.Task('T6_2t1_a0b0', length=7, delay_cost=1)
	T6_2t1_a0b0 += alt(MUL)
	S+=T6_2t1_a0b0>=T6_2t1_a0b0_in

	T6_2t0_a1b1_in = S.Task('T6_2t0_a1b1_in', length=1, delay_cost=1)
	T6_2t0_a1b1_in += alt(MUL_in)
	T6_2t0_a1b1 = S.Task('T6_2t0_a1b1', length=7, delay_cost=1)
	T6_2t0_a1b1 += alt(MUL)
	S+=T6_2t0_a1b1>=T6_2t0_a1b1_in

	T6_2t1_a1b1_in = S.Task('T6_2t1_a1b1_in', length=1, delay_cost=1)
	T6_2t1_a1b1_in += alt(MUL_in)
	T6_2t1_a1b1 = S.Task('T6_2t1_a1b1', length=7, delay_cost=1)
	T6_2t1_a1b1 += alt(MUL)
	S+=T6_2t1_a1b1>=T6_2t1_a1b1_in

	T1100 = S.Task('T1100', length=1, delay_cost=1)
	T1100 += alt(ADD)

	T1101 = S.Task('T1101', length=1, delay_cost=1)
	T1101 += alt(ADD)

	T1110 = S.Task('T1110', length=1, delay_cost=1)
	T1110 += alt(ADD)

	T1111 = S.Task('T1111', length=1, delay_cost=1)
	T1111 += alt(ADD)

	T1200 = S.Task('T1200', length=1, delay_cost=1)
	T1200 += alt(ADD)

	T1201 = S.Task('T1201', length=1, delay_cost=1)
	T1201 += alt(ADD)

	T1210 = S.Task('T1210', length=1, delay_cost=1)
	T1210 += alt(ADD)

	T1211 = S.Task('T1211', length=1, delay_cost=1)
	T1211 += alt(ADD)

	T1300 = S.Task('T1300', length=1, delay_cost=1)
	T1300 += alt(ADD)

	T1301 = S.Task('T1301', length=1, delay_cost=1)
	T1301 += alt(ADD)

	T1310 = S.Task('T1310', length=1, delay_cost=1)
	T1310 += alt(ADD)

	T1311 = S.Task('T1311', length=1, delay_cost=1)
	T1311 += alt(ADD)

	T1400 = S.Task('T1400', length=1, delay_cost=1)
	T1400 += alt(ADD)

	T1401 = S.Task('T1401', length=1, delay_cost=1)
	T1401 += alt(ADD)

	T1410 = S.Task('T1410', length=1, delay_cost=1)
	T1410 += alt(ADD)

	T1411 = S.Task('T1411', length=1, delay_cost=1)
	T1411 += alt(ADD)

	T0t2_0_mem0 = S.Task('T0t2_0_mem0', length=1, delay_cost=1)
	T0t2_0_mem0 += INPUT_mem_r
	S += T0t2_0_mem0<=T0t2_0

	T0t2_0_mem1 = S.Task('T0t2_0_mem1', length=1, delay_cost=1)
	T0t2_0_mem1 += INPUT_mem_r
	S += T0t2_0_mem1<=T0t2_0

	T0t2_1_mem0 = S.Task('T0t2_1_mem0', length=1, delay_cost=1)
	T0t2_1_mem0 += INPUT_mem_r
	S += T0t2_1_mem0<=T0t2_1

	T0t2_1_mem1 = S.Task('T0t2_1_mem1', length=1, delay_cost=1)
	T0t2_1_mem1 += INPUT_mem_r
	S += T0t2_1_mem1<=T0t2_1

	T0t3_0_mem0 = S.Task('T0t3_0_mem0', length=1, delay_cost=1)
	T0t3_0_mem0 += INPUT_mem_r
	S += T0t3_0_mem0<=T0t3_0

	T0t3_0_mem1 = S.Task('T0t3_0_mem1', length=1, delay_cost=1)
	T0t3_0_mem1 += INPUT_mem_r
	S += T0t3_0_mem1<=T0t3_0

	T0t3_1_mem0 = S.Task('T0t3_1_mem0', length=1, delay_cost=1)
	T0t3_1_mem0 += INPUT_mem_r
	S += T0t3_1_mem0<=T0t3_1

	T0t3_1_mem1 = S.Task('T0t3_1_mem1', length=1, delay_cost=1)
	T0t3_1_mem1 += INPUT_mem_r
	S += T0t3_1_mem1<=T0t3_1

	T0t0_a0b0_mem0 = S.Task('T0t0_a0b0_mem0', length=1, delay_cost=1)
	T0t0_a0b0_mem0 += INPUT_mem_r
	S += T0t0_a0b0_mem0<=T0t0_a0b0

	T0t0_a0b0_mem1 = S.Task('T0t0_a0b0_mem1', length=1, delay_cost=1)
	T0t0_a0b0_mem1 += INPUT_mem_r
	S += T0t0_a0b0_mem1<=T0t0_a0b0

	T0t1_a0b0_mem0 = S.Task('T0t1_a0b0_mem0', length=1, delay_cost=1)
	T0t1_a0b0_mem0 += INPUT_mem_r
	S += T0t1_a0b0_mem0<=T0t1_a0b0

	T0t1_a0b0_mem1 = S.Task('T0t1_a0b0_mem1', length=1, delay_cost=1)
	T0t1_a0b0_mem1 += INPUT_mem_r
	S += T0t1_a0b0_mem1<=T0t1_a0b0

	T0t2_a0b0_mem0 = S.Task('T0t2_a0b0_mem0', length=1, delay_cost=1)
	T0t2_a0b0_mem0 += INPUT_mem_r
	S += T0t2_a0b0_mem0<=T0t2_a0b0

	T0t2_a0b0_mem1 = S.Task('T0t2_a0b0_mem1', length=1, delay_cost=1)
	T0t2_a0b0_mem1 += INPUT_mem_r
	S += T0t2_a0b0_mem1<=T0t2_a0b0

	T0t3_a0b0_mem0 = S.Task('T0t3_a0b0_mem0', length=1, delay_cost=1)
	T0t3_a0b0_mem0 += INPUT_mem_r
	S += T0t3_a0b0_mem0<=T0t3_a0b0

	T0t3_a0b0_mem1 = S.Task('T0t3_a0b0_mem1', length=1, delay_cost=1)
	T0t3_a0b0_mem1 += INPUT_mem_r
	S += T0t3_a0b0_mem1<=T0t3_a0b0

	T0t0_a1b1_mem0 = S.Task('T0t0_a1b1_mem0', length=1, delay_cost=1)
	T0t0_a1b1_mem0 += INPUT_mem_r
	S += T0t0_a1b1_mem0<=T0t0_a1b1

	T0t0_a1b1_mem1 = S.Task('T0t0_a1b1_mem1', length=1, delay_cost=1)
	T0t0_a1b1_mem1 += INPUT_mem_r
	S += T0t0_a1b1_mem1<=T0t0_a1b1

	T0t1_a1b1_mem0 = S.Task('T0t1_a1b1_mem0', length=1, delay_cost=1)
	T0t1_a1b1_mem0 += INPUT_mem_r
	S += T0t1_a1b1_mem0<=T0t1_a1b1

	T0t1_a1b1_mem1 = S.Task('T0t1_a1b1_mem1', length=1, delay_cost=1)
	T0t1_a1b1_mem1 += INPUT_mem_r
	S += T0t1_a1b1_mem1<=T0t1_a1b1

	T0t2_a1b1_mem0 = S.Task('T0t2_a1b1_mem0', length=1, delay_cost=1)
	T0t2_a1b1_mem0 += INPUT_mem_r
	S += T0t2_a1b1_mem0<=T0t2_a1b1

	T0t2_a1b1_mem1 = S.Task('T0t2_a1b1_mem1', length=1, delay_cost=1)
	T0t2_a1b1_mem1 += INPUT_mem_r
	S += T0t2_a1b1_mem1<=T0t2_a1b1

	T0t3_a1b1_mem0 = S.Task('T0t3_a1b1_mem0', length=1, delay_cost=1)
	T0t3_a1b1_mem0 += INPUT_mem_r
	S += T0t3_a1b1_mem0<=T0t3_a1b1

	T0t3_a1b1_mem1 = S.Task('T0t3_a1b1_mem1', length=1, delay_cost=1)
	T0t3_a1b1_mem1 += INPUT_mem_r
	S += T0t3_a1b1_mem1<=T0t3_a1b1

	T1t3_0_mem0 = S.Task('T1t3_0_mem0', length=1, delay_cost=1)
	T1t3_0_mem0 += INPUT_mem_r
	S += T1t3_0_mem0<=T1t3_0

	T1t3_0_mem1 = S.Task('T1t3_0_mem1', length=1, delay_cost=1)
	T1t3_0_mem1 += INPUT_mem_r
	S += T1t3_0_mem1<=T1t3_0

	T1t3_1_mem0 = S.Task('T1t3_1_mem0', length=1, delay_cost=1)
	T1t3_1_mem0 += INPUT_mem_r
	S += T1t3_1_mem0<=T1t3_1

	T1t3_1_mem1 = S.Task('T1t3_1_mem1', length=1, delay_cost=1)
	T1t3_1_mem1 += INPUT_mem_r
	S += T1t3_1_mem1<=T1t3_1

	T1t0_a0b0_mem0 = S.Task('T1t0_a0b0_mem0', length=1, delay_cost=1)
	T1t0_a0b0_mem0 += INPUT_mem_r
	S += T1t0_a0b0_mem0<=T1t0_a0b0

	T1t0_a0b0_mem1 = S.Task('T1t0_a0b0_mem1', length=1, delay_cost=1)
	T1t0_a0b0_mem1 += INPUT_mem_r
	S += T1t0_a0b0_mem1<=T1t0_a0b0

	T1t1_a0b0_mem0 = S.Task('T1t1_a0b0_mem0', length=1, delay_cost=1)
	T1t1_a0b0_mem0 += INPUT_mem_r
	S += T1t1_a0b0_mem0<=T1t1_a0b0

	T1t1_a0b0_mem1 = S.Task('T1t1_a0b0_mem1', length=1, delay_cost=1)
	T1t1_a0b0_mem1 += INPUT_mem_r
	S += T1t1_a0b0_mem1<=T1t1_a0b0

	T1t3_a0b0_mem0 = S.Task('T1t3_a0b0_mem0', length=1, delay_cost=1)
	T1t3_a0b0_mem0 += INPUT_mem_r
	S += T1t3_a0b0_mem0<=T1t3_a0b0

	T1t3_a0b0_mem1 = S.Task('T1t3_a0b0_mem1', length=1, delay_cost=1)
	T1t3_a0b0_mem1 += INPUT_mem_r
	S += T1t3_a0b0_mem1<=T1t3_a0b0

	T1t0_a1b1_mem0 = S.Task('T1t0_a1b1_mem0', length=1, delay_cost=1)
	T1t0_a1b1_mem0 += INPUT_mem_r
	S += T1t0_a1b1_mem0<=T1t0_a1b1

	T1t0_a1b1_mem1 = S.Task('T1t0_a1b1_mem1', length=1, delay_cost=1)
	T1t0_a1b1_mem1 += INPUT_mem_r
	S += T1t0_a1b1_mem1<=T1t0_a1b1

	T1t1_a1b1_mem0 = S.Task('T1t1_a1b1_mem0', length=1, delay_cost=1)
	T1t1_a1b1_mem0 += INPUT_mem_r
	S += T1t1_a1b1_mem0<=T1t1_a1b1

	T1t1_a1b1_mem1 = S.Task('T1t1_a1b1_mem1', length=1, delay_cost=1)
	T1t1_a1b1_mem1 += INPUT_mem_r
	S += T1t1_a1b1_mem1<=T1t1_a1b1

	T1t3_a1b1_mem0 = S.Task('T1t3_a1b1_mem0', length=1, delay_cost=1)
	T1t3_a1b1_mem0 += INPUT_mem_r
	S += T1t3_a1b1_mem0<=T1t3_a1b1

	T1t3_a1b1_mem1 = S.Task('T1t3_a1b1_mem1', length=1, delay_cost=1)
	T1t3_a1b1_mem1 += INPUT_mem_r
	S += T1t3_a1b1_mem1<=T1t3_a1b1

	T2t3_0_mem0 = S.Task('T2t3_0_mem0', length=1, delay_cost=1)
	T2t3_0_mem0 += INPUT_mem_r
	S += T2t3_0_mem0<=T2t3_0

	T2t3_0_mem1 = S.Task('T2t3_0_mem1', length=1, delay_cost=1)
	T2t3_0_mem1 += INPUT_mem_r
	S += T2t3_0_mem1<=T2t3_0

	T2t3_1_mem0 = S.Task('T2t3_1_mem0', length=1, delay_cost=1)
	T2t3_1_mem0 += INPUT_mem_r
	S += T2t3_1_mem0<=T2t3_1

	T2t3_1_mem1 = S.Task('T2t3_1_mem1', length=1, delay_cost=1)
	T2t3_1_mem1 += INPUT_mem_r
	S += T2t3_1_mem1<=T2t3_1

	T2t0_a0b0_mem0 = S.Task('T2t0_a0b0_mem0', length=1, delay_cost=1)
	T2t0_a0b0_mem0 += INPUT_mem_r
	S += T2t0_a0b0_mem0<=T2t0_a0b0

	T2t0_a0b0_mem1 = S.Task('T2t0_a0b0_mem1', length=1, delay_cost=1)
	T2t0_a0b0_mem1 += INPUT_mem_r
	S += T2t0_a0b0_mem1<=T2t0_a0b0

	T2t1_a0b0_mem0 = S.Task('T2t1_a0b0_mem0', length=1, delay_cost=1)
	T2t1_a0b0_mem0 += INPUT_mem_r
	S += T2t1_a0b0_mem0<=T2t1_a0b0

	T2t1_a0b0_mem1 = S.Task('T2t1_a0b0_mem1', length=1, delay_cost=1)
	T2t1_a0b0_mem1 += INPUT_mem_r
	S += T2t1_a0b0_mem1<=T2t1_a0b0

	T2t3_a0b0_mem0 = S.Task('T2t3_a0b0_mem0', length=1, delay_cost=1)
	T2t3_a0b0_mem0 += INPUT_mem_r
	S += T2t3_a0b0_mem0<=T2t3_a0b0

	T2t3_a0b0_mem1 = S.Task('T2t3_a0b0_mem1', length=1, delay_cost=1)
	T2t3_a0b0_mem1 += INPUT_mem_r
	S += T2t3_a0b0_mem1<=T2t3_a0b0

	T2t0_a1b1_mem0 = S.Task('T2t0_a1b1_mem0', length=1, delay_cost=1)
	T2t0_a1b1_mem0 += INPUT_mem_r
	S += T2t0_a1b1_mem0<=T2t0_a1b1

	T2t0_a1b1_mem1 = S.Task('T2t0_a1b1_mem1', length=1, delay_cost=1)
	T2t0_a1b1_mem1 += INPUT_mem_r
	S += T2t0_a1b1_mem1<=T2t0_a1b1

	T2t1_a1b1_mem0 = S.Task('T2t1_a1b1_mem0', length=1, delay_cost=1)
	T2t1_a1b1_mem0 += INPUT_mem_r
	S += T2t1_a1b1_mem0<=T2t1_a1b1

	T2t1_a1b1_mem1 = S.Task('T2t1_a1b1_mem1', length=1, delay_cost=1)
	T2t1_a1b1_mem1 += INPUT_mem_r
	S += T2t1_a1b1_mem1<=T2t1_a1b1

	T2t3_a1b1_mem0 = S.Task('T2t3_a1b1_mem0', length=1, delay_cost=1)
	T2t3_a1b1_mem0 += INPUT_mem_r
	S += T2t3_a1b1_mem0<=T2t3_a1b1

	T2t3_a1b1_mem1 = S.Task('T2t3_a1b1_mem1', length=1, delay_cost=1)
	T2t3_a1b1_mem1 += INPUT_mem_r
	S += T2t3_a1b1_mem1<=T2t3_a1b1

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

	T4t2_0_mem0 = S.Task('T4t2_0_mem0', length=1, delay_cost=1)
	T4t2_0_mem0 += INPUT_mem_r
	S += T4t2_0_mem0<=T4t2_0

	T4t2_0_mem1 = S.Task('T4t2_0_mem1', length=1, delay_cost=1)
	T4t2_0_mem1 += INPUT_mem_r
	S += T4t2_0_mem1<=T4t2_0

	T4t2_1_mem0 = S.Task('T4t2_1_mem0', length=1, delay_cost=1)
	T4t2_1_mem0 += INPUT_mem_r
	S += T4t2_1_mem0<=T4t2_1

	T4t2_1_mem1 = S.Task('T4t2_1_mem1', length=1, delay_cost=1)
	T4t2_1_mem1 += INPUT_mem_r
	S += T4t2_1_mem1<=T4t2_1

	T4t3_0_mem0 = S.Task('T4t3_0_mem0', length=1, delay_cost=1)
	T4t3_0_mem0 += INPUT_mem_r
	S += T4t3_0_mem0<=T4t3_0

	T4t3_0_mem1 = S.Task('T4t3_0_mem1', length=1, delay_cost=1)
	T4t3_0_mem1 += INPUT_mem_r
	S += T4t3_0_mem1<=T4t3_0

	T4t3_1_mem0 = S.Task('T4t3_1_mem0', length=1, delay_cost=1)
	T4t3_1_mem0 += INPUT_mem_r
	S += T4t3_1_mem0<=T4t3_1

	T4t3_1_mem1 = S.Task('T4t3_1_mem1', length=1, delay_cost=1)
	T4t3_1_mem1 += INPUT_mem_r
	S += T4t3_1_mem1<=T4t3_1

	T4t0_a0b0_mem0 = S.Task('T4t0_a0b0_mem0', length=1, delay_cost=1)
	T4t0_a0b0_mem0 += INPUT_mem_r
	S += T4t0_a0b0_mem0<=T4t0_a0b0

	T4t0_a0b0_mem1 = S.Task('T4t0_a0b0_mem1', length=1, delay_cost=1)
	T4t0_a0b0_mem1 += INPUT_mem_r
	S += T4t0_a0b0_mem1<=T4t0_a0b0

	T4t1_a0b0_mem0 = S.Task('T4t1_a0b0_mem0', length=1, delay_cost=1)
	T4t1_a0b0_mem0 += INPUT_mem_r
	S += T4t1_a0b0_mem0<=T4t1_a0b0

	T4t1_a0b0_mem1 = S.Task('T4t1_a0b0_mem1', length=1, delay_cost=1)
	T4t1_a0b0_mem1 += INPUT_mem_r
	S += T4t1_a0b0_mem1<=T4t1_a0b0

	T4t2_a0b0_mem0 = S.Task('T4t2_a0b0_mem0', length=1, delay_cost=1)
	T4t2_a0b0_mem0 += INPUT_mem_r
	S += T4t2_a0b0_mem0<=T4t2_a0b0

	T4t2_a0b0_mem1 = S.Task('T4t2_a0b0_mem1', length=1, delay_cost=1)
	T4t2_a0b0_mem1 += INPUT_mem_r
	S += T4t2_a0b0_mem1<=T4t2_a0b0

	T4t3_a0b0_mem0 = S.Task('T4t3_a0b0_mem0', length=1, delay_cost=1)
	T4t3_a0b0_mem0 += INPUT_mem_r
	S += T4t3_a0b0_mem0<=T4t3_a0b0

	T4t3_a0b0_mem1 = S.Task('T4t3_a0b0_mem1', length=1, delay_cost=1)
	T4t3_a0b0_mem1 += INPUT_mem_r
	S += T4t3_a0b0_mem1<=T4t3_a0b0

	T4t0_a1b1_mem0 = S.Task('T4t0_a1b1_mem0', length=1, delay_cost=1)
	T4t0_a1b1_mem0 += INPUT_mem_r
	S += T4t0_a1b1_mem0<=T4t0_a1b1

	T4t0_a1b1_mem1 = S.Task('T4t0_a1b1_mem1', length=1, delay_cost=1)
	T4t0_a1b1_mem1 += INPUT_mem_r
	S += T4t0_a1b1_mem1<=T4t0_a1b1

	T4t1_a1b1_mem0 = S.Task('T4t1_a1b1_mem0', length=1, delay_cost=1)
	T4t1_a1b1_mem0 += INPUT_mem_r
	S += T4t1_a1b1_mem0<=T4t1_a1b1

	T4t1_a1b1_mem1 = S.Task('T4t1_a1b1_mem1', length=1, delay_cost=1)
	T4t1_a1b1_mem1 += INPUT_mem_r
	S += T4t1_a1b1_mem1<=T4t1_a1b1

	T4t2_a1b1_mem0 = S.Task('T4t2_a1b1_mem0', length=1, delay_cost=1)
	T4t2_a1b1_mem0 += INPUT_mem_r
	S += T4t2_a1b1_mem0<=T4t2_a1b1

	T4t2_a1b1_mem1 = S.Task('T4t2_a1b1_mem1', length=1, delay_cost=1)
	T4t2_a1b1_mem1 += INPUT_mem_r
	S += T4t2_a1b1_mem1<=T4t2_a1b1

	T4t3_a1b1_mem0 = S.Task('T4t3_a1b1_mem0', length=1, delay_cost=1)
	T4t3_a1b1_mem0 += INPUT_mem_r
	S += T4t3_a1b1_mem0<=T4t3_a1b1

	T4t3_a1b1_mem1 = S.Task('T4t3_a1b1_mem1', length=1, delay_cost=1)
	T4t3_a1b1_mem1 += INPUT_mem_r
	S += T4t3_a1b1_mem1<=T4t3_a1b1

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

	T600_mem0 = S.Task('T600_mem0', length=1, delay_cost=1)
	T600_mem0 += INPUT_mem_r
	S += T600_mem0<=T600

	T600_mem1 = S.Task('T600_mem1', length=1, delay_cost=1)
	T600_mem1 += INPUT_mem_r
	S += T600_mem1<=T600

	T601_mem0 = S.Task('T601_mem0', length=1, delay_cost=1)
	T601_mem0 += INPUT_mem_r
	S += T601_mem0<=T601

	T601_mem1 = S.Task('T601_mem1', length=1, delay_cost=1)
	T601_mem1 += INPUT_mem_r
	S += T601_mem1<=T601

	T610_mem0 = S.Task('T610_mem0', length=1, delay_cost=1)
	T610_mem0 += INPUT_mem_r
	S += T610_mem0<=T610

	T610_mem1 = S.Task('T610_mem1', length=1, delay_cost=1)
	T610_mem1 += INPUT_mem_r
	S += T610_mem1<=T610

	T611_mem0 = S.Task('T611_mem0', length=1, delay_cost=1)
	T611_mem0 += INPUT_mem_r
	S += T611_mem0<=T611

	T611_mem1 = S.Task('T611_mem1', length=1, delay_cost=1)
	T611_mem1 += INPUT_mem_r
	S += T611_mem1<=T611

	T700_mem0 = S.Task('T700_mem0', length=1, delay_cost=1)
	T700_mem0 += INPUT_mem_r
	S += T700_mem0<=T700

	T700_mem1 = S.Task('T700_mem1', length=1, delay_cost=1)
	T700_mem1 += INPUT_mem_r
	S += T700_mem1<=T700

	T701_mem0 = S.Task('T701_mem0', length=1, delay_cost=1)
	T701_mem0 += INPUT_mem_r
	S += T701_mem0<=T701

	T701_mem1 = S.Task('T701_mem1', length=1, delay_cost=1)
	T701_mem1 += INPUT_mem_r
	S += T701_mem1<=T701

	T710_mem0 = S.Task('T710_mem0', length=1, delay_cost=1)
	T710_mem0 += INPUT_mem_r
	S += T710_mem0<=T710

	T710_mem1 = S.Task('T710_mem1', length=1, delay_cost=1)
	T710_mem1 += INPUT_mem_r
	S += T710_mem1<=T710

	T711_mem0 = S.Task('T711_mem0', length=1, delay_cost=1)
	T711_mem0 += INPUT_mem_r
	S += T711_mem0<=T711

	T711_mem1 = S.Task('T711_mem1', length=1, delay_cost=1)
	T711_mem1 += INPUT_mem_r
	S += T711_mem1<=T711

	T6_2t0_a0b0_mem0 = S.Task('T6_2t0_a0b0_mem0', length=1, delay_cost=1)
	T6_2t0_a0b0_mem0 += INPUT_mem_r
	S += T6_2t0_a0b0_mem0<=T6_2t0_a0b0

	T6_2t0_a0b0_mem1 = S.Task('T6_2t0_a0b0_mem1', length=1, delay_cost=1)
	T6_2t0_a0b0_mem1 += INPUT_mem_r
	S += T6_2t0_a0b0_mem1<=T6_2t0_a0b0

	T6_2t1_a0b0_mem0 = S.Task('T6_2t1_a0b0_mem0', length=1, delay_cost=1)
	T6_2t1_a0b0_mem0 += INPUT_mem_r
	S += T6_2t1_a0b0_mem0<=T6_2t1_a0b0

	T6_2t1_a0b0_mem1 = S.Task('T6_2t1_a0b0_mem1', length=1, delay_cost=1)
	T6_2t1_a0b0_mem1 += INPUT_mem_r
	S += T6_2t1_a0b0_mem1<=T6_2t1_a0b0

	T6_2t0_a1b1_mem0 = S.Task('T6_2t0_a1b1_mem0', length=1, delay_cost=1)
	T6_2t0_a1b1_mem0 += INPUT_mem_r
	S += T6_2t0_a1b1_mem0<=T6_2t0_a1b1

	T6_2t0_a1b1_mem1 = S.Task('T6_2t0_a1b1_mem1', length=1, delay_cost=1)
	T6_2t0_a1b1_mem1 += INPUT_mem_r
	S += T6_2t0_a1b1_mem1<=T6_2t0_a1b1

	T6_2t1_a1b1_mem0 = S.Task('T6_2t1_a1b1_mem0', length=1, delay_cost=1)
	T6_2t1_a1b1_mem0 += INPUT_mem_r
	S += T6_2t1_a1b1_mem0<=T6_2t1_a1b1

	T6_2t1_a1b1_mem1 = S.Task('T6_2t1_a1b1_mem1', length=1, delay_cost=1)
	T6_2t1_a1b1_mem1 += INPUT_mem_r
	S += T6_2t1_a1b1_mem1<=T6_2t1_a1b1

	T1100_mem0 = S.Task('T1100_mem0', length=1, delay_cost=1)
	T1100_mem0 += INPUT_mem_r
	S += T1100_mem0<=T1100

	T1100_mem1 = S.Task('T1100_mem1', length=1, delay_cost=1)
	T1100_mem1 += INPUT_mem_r
	S += T1100_mem1<=T1100

	T1101_mem0 = S.Task('T1101_mem0', length=1, delay_cost=1)
	T1101_mem0 += INPUT_mem_r
	S += T1101_mem0<=T1101

	T1101_mem1 = S.Task('T1101_mem1', length=1, delay_cost=1)
	T1101_mem1 += INPUT_mem_r
	S += T1101_mem1<=T1101

	T1110_mem0 = S.Task('T1110_mem0', length=1, delay_cost=1)
	T1110_mem0 += INPUT_mem_r
	S += T1110_mem0<=T1110

	T1110_mem1 = S.Task('T1110_mem1', length=1, delay_cost=1)
	T1110_mem1 += INPUT_mem_r
	S += T1110_mem1<=T1110

	T1111_mem0 = S.Task('T1111_mem0', length=1, delay_cost=1)
	T1111_mem0 += INPUT_mem_r
	S += T1111_mem0<=T1111

	T1111_mem1 = S.Task('T1111_mem1', length=1, delay_cost=1)
	T1111_mem1 += INPUT_mem_r
	S += T1111_mem1<=T1111

	T1200_mem0 = S.Task('T1200_mem0', length=1, delay_cost=1)
	T1200_mem0 += INPUT_mem_r
	S += T1200_mem0<=T1200

	T1200_mem1 = S.Task('T1200_mem1', length=1, delay_cost=1)
	T1200_mem1 += INPUT_mem_r
	S += T1200_mem1<=T1200

	T1201_mem0 = S.Task('T1201_mem0', length=1, delay_cost=1)
	T1201_mem0 += INPUT_mem_r
	S += T1201_mem0<=T1201

	T1201_mem1 = S.Task('T1201_mem1', length=1, delay_cost=1)
	T1201_mem1 += INPUT_mem_r
	S += T1201_mem1<=T1201

	T1210_mem0 = S.Task('T1210_mem0', length=1, delay_cost=1)
	T1210_mem0 += INPUT_mem_r
	S += T1210_mem0<=T1210

	T1210_mem1 = S.Task('T1210_mem1', length=1, delay_cost=1)
	T1210_mem1 += INPUT_mem_r
	S += T1210_mem1<=T1210

	T1211_mem0 = S.Task('T1211_mem0', length=1, delay_cost=1)
	T1211_mem0 += INPUT_mem_r
	S += T1211_mem0<=T1211

	T1211_mem1 = S.Task('T1211_mem1', length=1, delay_cost=1)
	T1211_mem1 += INPUT_mem_r
	S += T1211_mem1<=T1211

	T1300_mem0 = S.Task('T1300_mem0', length=1, delay_cost=1)
	T1300_mem0 += INPUT_mem_r
	S += T1300_mem0<=T1300

	T1300_mem1 = S.Task('T1300_mem1', length=1, delay_cost=1)
	T1300_mem1 += INPUT_mem_r
	S += T1300_mem1<=T1300

	T1301_mem0 = S.Task('T1301_mem0', length=1, delay_cost=1)
	T1301_mem0 += INPUT_mem_r
	S += T1301_mem0<=T1301

	T1301_mem1 = S.Task('T1301_mem1', length=1, delay_cost=1)
	T1301_mem1 += INPUT_mem_r
	S += T1301_mem1<=T1301

	T1310_mem0 = S.Task('T1310_mem0', length=1, delay_cost=1)
	T1310_mem0 += INPUT_mem_r
	S += T1310_mem0<=T1310

	T1310_mem1 = S.Task('T1310_mem1', length=1, delay_cost=1)
	T1310_mem1 += INPUT_mem_r
	S += T1310_mem1<=T1310

	T1311_mem0 = S.Task('T1311_mem0', length=1, delay_cost=1)
	T1311_mem0 += INPUT_mem_r
	S += T1311_mem0<=T1311

	T1311_mem1 = S.Task('T1311_mem1', length=1, delay_cost=1)
	T1311_mem1 += INPUT_mem_r
	S += T1311_mem1<=T1311

	T1400_mem0 = S.Task('T1400_mem0', length=1, delay_cost=1)
	T1400_mem0 += INPUT_mem_r
	S += T1400_mem0<=T1400

	T1400_mem1 = S.Task('T1400_mem1', length=1, delay_cost=1)
	T1400_mem1 += INPUT_mem_r
	S += T1400_mem1<=T1400

	T1401_mem0 = S.Task('T1401_mem0', length=1, delay_cost=1)
	T1401_mem0 += INPUT_mem_r
	S += T1401_mem0<=T1401

	T1401_mem1 = S.Task('T1401_mem1', length=1, delay_cost=1)
	T1401_mem1 += INPUT_mem_r
	S += T1401_mem1<=T1401

	T1410_mem0 = S.Task('T1410_mem0', length=1, delay_cost=1)
	T1410_mem0 += INPUT_mem_r
	S += T1410_mem0<=T1410

	T1410_mem1 = S.Task('T1410_mem1', length=1, delay_cost=1)
	T1410_mem1 += INPUT_mem_r
	S += T1410_mem1<=T1410

	T1411_mem0 = S.Task('T1411_mem0', length=1, delay_cost=1)
	T1411_mem0 += INPUT_mem_r
	S += T1411_mem0<=T1411

	T1411_mem1 = S.Task('T1411_mem1', length=1, delay_cost=1)
	T1411_mem1 += INPUT_mem_r
	S += T1411_mem1<=T1411

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sparse_mul1_add4/sparse_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sparse_mul1_add4_0(0, 0)