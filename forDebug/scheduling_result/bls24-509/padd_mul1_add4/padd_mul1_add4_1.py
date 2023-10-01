from pyschedule import Scenario, solvers, plotters, alt

def solve_padd_mul1_add4_1(ConstStep, ExpStep):
	horizon = 119
	S=Scenario("padd_mul1_add4_1",horizon = horizon)

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
	T1t0_a0b0_in = S.Task('T1t0_a0b0_in', length=1, delay_cost=1)
	S += T1t0_a0b0_in >= 0
	T1t0_a0b0_in += MUL_in[0]

	T1t0_a0b0_mem0 = S.Task('T1t0_a0b0_mem0', length=1, delay_cost=1)
	S += T1t0_a0b0_mem0 >= 0
	T1t0_a0b0_mem0 += INPUT_mem_r

	T1t0_a0b0_mem1 = S.Task('T1t0_a0b0_mem1', length=1, delay_cost=1)
	S += T1t0_a0b0_mem1 >= 0
	T1t0_a0b0_mem1 += INPUT_mem_r

	T1t0_a0b0 = S.Task('T1t0_a0b0', length=7, delay_cost=1)
	S += T1t0_a0b0 >= 1
	T1t0_a0b0 += MUL[0]

	T1t1_a0b0_in = S.Task('T1t1_a0b0_in', length=1, delay_cost=1)
	S += T1t1_a0b0_in >= 1
	T1t1_a0b0_in += MUL_in[0]

	T1t1_a0b0_mem0 = S.Task('T1t1_a0b0_mem0', length=1, delay_cost=1)
	S += T1t1_a0b0_mem0 >= 1
	T1t1_a0b0_mem0 += INPUT_mem_r

	T1t1_a0b0_mem1 = S.Task('T1t1_a0b0_mem1', length=1, delay_cost=1)
	S += T1t1_a0b0_mem1 >= 1
	T1t1_a0b0_mem1 += INPUT_mem_r

	T0t0_a1b1_in = S.Task('T0t0_a1b1_in', length=1, delay_cost=1)
	S += T0t0_a1b1_in >= 2
	T0t0_a1b1_in += MUL_in[0]

	T0t0_a1b1_mem0 = S.Task('T0t0_a1b1_mem0', length=1, delay_cost=1)
	S += T0t0_a1b1_mem0 >= 2
	T0t0_a1b1_mem0 += INPUT_mem_r

	T0t0_a1b1_mem1 = S.Task('T0t0_a1b1_mem1', length=1, delay_cost=1)
	S += T0t0_a1b1_mem1 >= 2
	T0t0_a1b1_mem1 += INPUT_mem_r

	T1t1_a0b0 = S.Task('T1t1_a0b0', length=7, delay_cost=1)
	S += T1t1_a0b0 >= 2
	T1t1_a0b0 += MUL[0]

	T0t0_a1b1 = S.Task('T0t0_a1b1', length=7, delay_cost=1)
	S += T0t0_a1b1 >= 3
	T0t0_a1b1 += MUL[0]

	T0t1_a1b1_in = S.Task('T0t1_a1b1_in', length=1, delay_cost=1)
	S += T0t1_a1b1_in >= 3
	T0t1_a1b1_in += MUL_in[0]

	T0t1_a1b1_mem0 = S.Task('T0t1_a1b1_mem0', length=1, delay_cost=1)
	S += T0t1_a1b1_mem0 >= 3
	T0t1_a1b1_mem0 += INPUT_mem_r

	T0t1_a1b1_mem1 = S.Task('T0t1_a1b1_mem1', length=1, delay_cost=1)
	S += T0t1_a1b1_mem1 >= 3
	T0t1_a1b1_mem1 += INPUT_mem_r

	T0t1_a0b0_in = S.Task('T0t1_a0b0_in', length=1, delay_cost=1)
	S += T0t1_a0b0_in >= 4
	T0t1_a0b0_in += MUL_in[0]

	T0t1_a0b0_mem0 = S.Task('T0t1_a0b0_mem0', length=1, delay_cost=1)
	S += T0t1_a0b0_mem0 >= 4
	T0t1_a0b0_mem0 += INPUT_mem_r

	T0t1_a0b0_mem1 = S.Task('T0t1_a0b0_mem1', length=1, delay_cost=1)
	S += T0t1_a0b0_mem1 >= 4
	T0t1_a0b0_mem1 += INPUT_mem_r

	T0t1_a1b1 = S.Task('T0t1_a1b1', length=7, delay_cost=1)
	S += T0t1_a1b1 >= 4
	T0t1_a1b1 += MUL[0]

	T0t0_a0b0_in = S.Task('T0t0_a0b0_in', length=1, delay_cost=1)
	S += T0t0_a0b0_in >= 5
	T0t0_a0b0_in += MUL_in[0]

	T0t0_a0b0_mem0 = S.Task('T0t0_a0b0_mem0', length=1, delay_cost=1)
	S += T0t0_a0b0_mem0 >= 5
	T0t0_a0b0_mem0 += INPUT_mem_r

	T0t0_a0b0_mem1 = S.Task('T0t0_a0b0_mem1', length=1, delay_cost=1)
	S += T0t0_a0b0_mem1 >= 5
	T0t0_a0b0_mem1 += INPUT_mem_r

	T0t1_a0b0 = S.Task('T0t1_a0b0', length=7, delay_cost=1)
	S += T0t1_a0b0 >= 5
	T0t1_a0b0 += MUL[0]

	T0t0_a0b0 = S.Task('T0t0_a0b0', length=7, delay_cost=1)
	S += T0t0_a0b0 >= 6
	T0t0_a0b0 += MUL[0]

	T1t1_a1b1_in = S.Task('T1t1_a1b1_in', length=1, delay_cost=1)
	S += T1t1_a1b1_in >= 6
	T1t1_a1b1_in += MUL_in[0]

	T1t1_a1b1_mem0 = S.Task('T1t1_a1b1_mem0', length=1, delay_cost=1)
	S += T1t1_a1b1_mem0 >= 6
	T1t1_a1b1_mem0 += INPUT_mem_r

	T1t1_a1b1_mem1 = S.Task('T1t1_a1b1_mem1', length=1, delay_cost=1)
	S += T1t1_a1b1_mem1 >= 6
	T1t1_a1b1_mem1 += INPUT_mem_r

	T1t0_a1b1_in = S.Task('T1t0_a1b1_in', length=1, delay_cost=1)
	S += T1t0_a1b1_in >= 7
	T1t0_a1b1_in += MUL_in[0]

	T1t0_a1b1_mem0 = S.Task('T1t0_a1b1_mem0', length=1, delay_cost=1)
	S += T1t0_a1b1_mem0 >= 7
	T1t0_a1b1_mem0 += INPUT_mem_r

	T1t0_a1b1_mem1 = S.Task('T1t0_a1b1_mem1', length=1, delay_cost=1)
	S += T1t0_a1b1_mem1 >= 7
	T1t0_a1b1_mem1 += INPUT_mem_r

	T1t1_a1b1 = S.Task('T1t1_a1b1', length=7, delay_cost=1)
	S += T1t1_a1b1 >= 7
	T1t1_a1b1 += MUL[0]

	T0t3_1_mem0 = S.Task('T0t3_1_mem0', length=1, delay_cost=1)
	S += T0t3_1_mem0 >= 8
	T0t3_1_mem0 += INPUT_mem_r

	T0t3_1_mem1 = S.Task('T0t3_1_mem1', length=1, delay_cost=1)
	S += T0t3_1_mem1 >= 8
	T0t3_1_mem1 += INPUT_mem_r

	T1c0_a0b0_mem0 = S.Task('T1c0_a0b0_mem0', length=1, delay_cost=1)
	S += T1c0_a0b0_mem0 >= 8
	T1c0_a0b0_mem0 += MUL_mem[0]

	T1c0_a0b0_mem1 = S.Task('T1c0_a0b0_mem1', length=1, delay_cost=1)
	S += T1c0_a0b0_mem1 >= 8
	T1c0_a0b0_mem1 += MUL_mem[0]

	T1t0_a1b1 = S.Task('T1t0_a1b1', length=7, delay_cost=1)
	S += T1t0_a1b1 >= 8
	T1t0_a1b1 += MUL[0]

	T0t2_1_mem0 = S.Task('T0t2_1_mem0', length=1, delay_cost=1)
	S += T0t2_1_mem0 >= 9
	T0t2_1_mem0 += INPUT_mem_r

	T0t2_1_mem1 = S.Task('T0t2_1_mem1', length=1, delay_cost=1)
	S += T0t2_1_mem1 >= 9
	T0t2_1_mem1 += INPUT_mem_r

	T0t3_1 = S.Task('T0t3_1', length=1, delay_cost=1)
	S += T0t3_1 >= 9
	T0t3_1 += ADD[3]

	T1c0_a0b0 = S.Task('T1c0_a0b0', length=1, delay_cost=1)
	S += T1c0_a0b0 >= 9
	T1c0_a0b0 += ADD[1]

	T1t6_a0b0_mem0 = S.Task('T1t6_a0b0_mem0', length=1, delay_cost=1)
	S += T1t6_a0b0_mem0 >= 9
	T1t6_a0b0_mem0 += MUL_mem[0]

	T1t6_a0b0_mem1 = S.Task('T1t6_a0b0_mem1', length=1, delay_cost=1)
	S += T1t6_a0b0_mem1 >= 9
	T1t6_a0b0_mem1 += MUL_mem[0]

	T0t1_t2t3_in = S.Task('T0t1_t2t3_in', length=1, delay_cost=1)
	S += T0t1_t2t3_in >= 10
	T0t1_t2t3_in += MUL_in[0]

	T0t1_t2t3_mem0 = S.Task('T0t1_t2t3_mem0', length=1, delay_cost=1)
	S += T0t1_t2t3_mem0 >= 10
	T0t1_t2t3_mem0 += ADD_mem[2]

	T0t1_t2t3_mem1 = S.Task('T0t1_t2t3_mem1', length=1, delay_cost=1)
	S += T0t1_t2t3_mem1 >= 10
	T0t1_t2t3_mem1 += ADD_mem[3]

	T0t2_0_mem0 = S.Task('T0t2_0_mem0', length=1, delay_cost=1)
	S += T0t2_0_mem0 >= 10
	T0t2_0_mem0 += INPUT_mem_r

	T0t2_0_mem1 = S.Task('T0t2_0_mem1', length=1, delay_cost=1)
	S += T0t2_0_mem1 >= 10
	T0t2_0_mem1 += INPUT_mem_r

	T0t2_1 = S.Task('T0t2_1', length=1, delay_cost=1)
	S += T0t2_1 >= 10
	T0t2_1 += ADD[2]

	T0t6_a1b1_mem0 = S.Task('T0t6_a1b1_mem0', length=1, delay_cost=1)
	S += T0t6_a1b1_mem0 >= 10
	T0t6_a1b1_mem0 += MUL_mem[0]

	T0t6_a1b1_mem1 = S.Task('T0t6_a1b1_mem1', length=1, delay_cost=1)
	S += T0t6_a1b1_mem1 >= 10
	T0t6_a1b1_mem1 += MUL_mem[0]

	T1t6_a0b0 = S.Task('T1t6_a0b0', length=1, delay_cost=1)
	S += T1t6_a0b0 >= 10
	T1t6_a0b0 += ADD[1]

	T0c0_a1b1_mem0 = S.Task('T0c0_a1b1_mem0', length=1, delay_cost=1)
	S += T0c0_a1b1_mem0 >= 11
	T0c0_a1b1_mem0 += MUL_mem[0]

	T0c0_a1b1_mem1 = S.Task('T0c0_a1b1_mem1', length=1, delay_cost=1)
	S += T0c0_a1b1_mem1 >= 11
	T0c0_a1b1_mem1 += MUL_mem[0]

	T0t1_t2t3 = S.Task('T0t1_t2t3', length=7, delay_cost=1)
	S += T0t1_t2t3 >= 11
	T0t1_t2t3 += MUL[0]

	T0t2_0 = S.Task('T0t2_0', length=1, delay_cost=1)
	S += T0t2_0 >= 11
	T0t2_0 += ADD[2]

	T0t2_t2t3_mem0 = S.Task('T0t2_t2t3_mem0', length=1, delay_cost=1)
	S += T0t2_t2t3_mem0 >= 11
	T0t2_t2t3_mem0 += ADD_mem[2]

	T0t2_t2t3_mem1 = S.Task('T0t2_t2t3_mem1', length=1, delay_cost=1)
	S += T0t2_t2t3_mem1 >= 11
	T0t2_t2t3_mem1 += ADD_mem[2]

	T0t3_0_mem0 = S.Task('T0t3_0_mem0', length=1, delay_cost=1)
	S += T0t3_0_mem0 >= 11
	T0t3_0_mem0 += INPUT_mem_r

	T0t3_0_mem1 = S.Task('T0t3_0_mem1', length=1, delay_cost=1)
	S += T0t3_0_mem1 >= 11
	T0t3_0_mem1 += INPUT_mem_r

	T0t6_a1b1 = S.Task('T0t6_a1b1', length=1, delay_cost=1)
	S += T0t6_a1b1 >= 11
	T0t6_a1b1 += ADD[1]

	T0c0_a1b1 = S.Task('T0c0_a1b1', length=1, delay_cost=1)
	S += T0c0_a1b1 >= 12
	T0c0_a1b1 += ADD[1]

	T0t0_t2t3_in = S.Task('T0t0_t2t3_in', length=1, delay_cost=1)
	S += T0t0_t2t3_in >= 12
	T0t0_t2t3_in += MUL_in[0]

	T0t0_t2t3_mem0 = S.Task('T0t0_t2t3_mem0', length=1, delay_cost=1)
	S += T0t0_t2t3_mem0 >= 12
	T0t0_t2t3_mem0 += ADD_mem[2]

	T0t0_t2t3_mem1 = S.Task('T0t0_t2t3_mem1', length=1, delay_cost=1)
	S += T0t0_t2t3_mem1 >= 12
	T0t0_t2t3_mem1 += ADD_mem[0]

	T0t2_t2t3 = S.Task('T0t2_t2t3', length=1, delay_cost=1)
	S += T0t2_t2t3 >= 12
	T0t2_t2t3 += ADD[3]

	T0t3_0 = S.Task('T0t3_0', length=1, delay_cost=1)
	S += T0t3_0 >= 12
	T0t3_0 += ADD[0]

	T0t3_t2t3_mem0 = S.Task('T0t3_t2t3_mem0', length=1, delay_cost=1)
	S += T0t3_t2t3_mem0 >= 12
	T0t3_t2t3_mem0 += ADD_mem[0]

	T0t3_t2t3_mem1 = S.Task('T0t3_t2t3_mem1', length=1, delay_cost=1)
	S += T0t3_t2t3_mem1 >= 12
	T0t3_t2t3_mem1 += ADD_mem[3]

	T0t6_a0b0_mem0 = S.Task('T0t6_a0b0_mem0', length=1, delay_cost=1)
	S += T0t6_a0b0_mem0 >= 12
	T0t6_a0b0_mem0 += MUL_mem[0]

	T0t6_a0b0_mem1 = S.Task('T0t6_a0b0_mem1', length=1, delay_cost=1)
	S += T0t6_a0b0_mem1 >= 12
	T0t6_a0b0_mem1 += MUL_mem[0]

	T1t3_0_mem0 = S.Task('T1t3_0_mem0', length=1, delay_cost=1)
	S += T1t3_0_mem0 >= 12
	T1t3_0_mem0 += INPUT_mem_r

	T1t3_0_mem1 = S.Task('T1t3_0_mem1', length=1, delay_cost=1)
	S += T1t3_0_mem1 >= 12
	T1t3_0_mem1 += INPUT_mem_r

	T0c0_a0b0_mem0 = S.Task('T0c0_a0b0_mem0', length=1, delay_cost=1)
	S += T0c0_a0b0_mem0 >= 13
	T0c0_a0b0_mem0 += MUL_mem[0]

	T0c0_a0b0_mem1 = S.Task('T0c0_a0b0_mem1', length=1, delay_cost=1)
	S += T0c0_a0b0_mem1 >= 13
	T0c0_a0b0_mem1 += MUL_mem[0]

	T0t0_t2t3 = S.Task('T0t0_t2t3', length=7, delay_cost=1)
	S += T0t0_t2t3 >= 13
	T0t0_t2t3 += MUL[0]

	T0t3_t2t3 = S.Task('T0t3_t2t3', length=1, delay_cost=1)
	S += T0t3_t2t3 >= 13
	T0t3_t2t3 += ADD[3]

	T0t6_a0b0 = S.Task('T0t6_a0b0', length=1, delay_cost=1)
	S += T0t6_a0b0 >= 13
	T0t6_a0b0 += ADD[1]

	T1t0_t2t3_in = S.Task('T1t0_t2t3_in', length=1, delay_cost=1)
	S += T1t0_t2t3_in >= 13
	T1t0_t2t3_in += MUL_in[0]

	T1t0_t2t3_mem0 = S.Task('T1t0_t2t3_mem0', length=1, delay_cost=1)
	S += T1t0_t2t3_mem0 >= 13
	T1t0_t2t3_mem0 += ADD_mem[2]

	T1t0_t2t3_mem1 = S.Task('T1t0_t2t3_mem1', length=1, delay_cost=1)
	S += T1t0_t2t3_mem1 >= 13
	T1t0_t2t3_mem1 += ADD_mem[0]

	T1t3_0 = S.Task('T1t3_0', length=1, delay_cost=1)
	S += T1t3_0 >= 13
	T1t3_0 += ADD[0]

	T1t3_1_mem0 = S.Task('T1t3_1_mem0', length=1, delay_cost=1)
	S += T1t3_1_mem0 >= 13
	T1t3_1_mem0 += INPUT_mem_r

	T1t3_1_mem1 = S.Task('T1t3_1_mem1', length=1, delay_cost=1)
	S += T1t3_1_mem1 >= 13
	T1t3_1_mem1 += INPUT_mem_r

	T0c0_a0b0 = S.Task('T0c0_a0b0', length=1, delay_cost=1)
	S += T0c0_a0b0 >= 14
	T0c0_a0b0 += ADD[1]

	T0t3_a0b0_mem0 = S.Task('T0t3_a0b0_mem0', length=1, delay_cost=1)
	S += T0t3_a0b0_mem0 >= 14
	T0t3_a0b0_mem0 += INPUT_mem_r

	T0t3_a0b0_mem1 = S.Task('T0t3_a0b0_mem1', length=1, delay_cost=1)
	S += T0t3_a0b0_mem1 >= 14
	T0t3_a0b0_mem1 += INPUT_mem_r

	T1c0_a1b1_mem0 = S.Task('T1c0_a1b1_mem0', length=1, delay_cost=1)
	S += T1c0_a1b1_mem0 >= 14
	T1c0_a1b1_mem0 += MUL_mem[0]

	T1c0_a1b1_mem1 = S.Task('T1c0_a1b1_mem1', length=1, delay_cost=1)
	S += T1c0_a1b1_mem1 >= 14
	T1c0_a1b1_mem1 += MUL_mem[0]

	T1t0_t2t3 = S.Task('T1t0_t2t3', length=7, delay_cost=1)
	S += T1t0_t2t3 >= 14
	T1t0_t2t3 += MUL[0]

	T1t1_t2t3_in = S.Task('T1t1_t2t3_in', length=1, delay_cost=1)
	S += T1t1_t2t3_in >= 14
	T1t1_t2t3_in += MUL_in[0]

	T1t1_t2t3_mem0 = S.Task('T1t1_t2t3_mem0', length=1, delay_cost=1)
	S += T1t1_t2t3_mem0 >= 14
	T1t1_t2t3_mem0 += ADD_mem[2]

	T1t1_t2t3_mem1 = S.Task('T1t1_t2t3_mem1', length=1, delay_cost=1)
	S += T1t1_t2t3_mem1 >= 14
	T1t1_t2t3_mem1 += ADD_mem[3]

	T1t3_1 = S.Task('T1t3_1', length=1, delay_cost=1)
	S += T1t3_1 >= 14
	T1t3_1 += ADD[3]

	T1t3_t2t3_mem0 = S.Task('T1t3_t2t3_mem0', length=1, delay_cost=1)
	S += T1t3_t2t3_mem0 >= 14
	T1t3_t2t3_mem0 += ADD_mem[0]

	T1t3_t2t3_mem1 = S.Task('T1t3_t2t3_mem1', length=1, delay_cost=1)
	S += T1t3_t2t3_mem1 >= 14
	T1t3_t2t3_mem1 += ADD_mem[3]

	T0t2_a0b0_mem0 = S.Task('T0t2_a0b0_mem0', length=1, delay_cost=1)
	S += T0t2_a0b0_mem0 >= 15
	T0t2_a0b0_mem0 += INPUT_mem_r

	T0t2_a0b0_mem1 = S.Task('T0t2_a0b0_mem1', length=1, delay_cost=1)
	S += T0t2_a0b0_mem1 >= 15
	T0t2_a0b0_mem1 += INPUT_mem_r

	T0t3_a0b0 = S.Task('T0t3_a0b0', length=1, delay_cost=1)
	S += T0t3_a0b0 >= 15
	T0t3_a0b0 += ADD[2]

	T1c0_a1b1 = S.Task('T1c0_a1b1', length=1, delay_cost=1)
	S += T1c0_a1b1 >= 15
	T1c0_a1b1 += ADD[0]

	T1t1_t2t3 = S.Task('T1t1_t2t3', length=7, delay_cost=1)
	S += T1t1_t2t3 >= 15
	T1t1_t2t3 += MUL[0]

	T1t3_t2t3 = S.Task('T1t3_t2t3', length=1, delay_cost=1)
	S += T1t3_t2t3 >= 15
	T1t3_t2t3 += ADD[3]

	T1t6_a1b1_mem0 = S.Task('T1t6_a1b1_mem0', length=1, delay_cost=1)
	S += T1t6_a1b1_mem0 >= 15
	T1t6_a1b1_mem0 += MUL_mem[0]

	T1t6_a1b1_mem1 = S.Task('T1t6_a1b1_mem1', length=1, delay_cost=1)
	S += T1t6_a1b1_mem1 >= 15
	T1t6_a1b1_mem1 += MUL_mem[0]

	T0t2_a0b0 = S.Task('T0t2_a0b0', length=1, delay_cost=1)
	S += T0t2_a0b0 >= 16
	T0t2_a0b0 += ADD[2]

	T0t4_a0b0_in = S.Task('T0t4_a0b0_in', length=1, delay_cost=1)
	S += T0t4_a0b0_in >= 16
	T0t4_a0b0_in += MUL_in[0]

	T0t4_a0b0_mem0 = S.Task('T0t4_a0b0_mem0', length=1, delay_cost=1)
	S += T0t4_a0b0_mem0 >= 16
	T0t4_a0b0_mem0 += ADD_mem[2]

	T0t4_a0b0_mem1 = S.Task('T0t4_a0b0_mem1', length=1, delay_cost=1)
	S += T0t4_a0b0_mem1 >= 16
	T0t4_a0b0_mem1 += ADD_mem[2]

	T1t3_a0b0_mem0 = S.Task('T1t3_a0b0_mem0', length=1, delay_cost=1)
	S += T1t3_a0b0_mem0 >= 16
	T1t3_a0b0_mem0 += INPUT_mem_r

	T1t3_a0b0_mem1 = S.Task('T1t3_a0b0_mem1', length=1, delay_cost=1)
	S += T1t3_a0b0_mem1 >= 16
	T1t3_a0b0_mem1 += INPUT_mem_r

	T1t6_a1b1 = S.Task('T1t6_a1b1', length=1, delay_cost=1)
	S += T1t6_a1b1 >= 16
	T1t6_a1b1 += ADD[0]

	T0t3_a1b1_mem0 = S.Task('T0t3_a1b1_mem0', length=1, delay_cost=1)
	S += T0t3_a1b1_mem0 >= 17
	T0t3_a1b1_mem0 += INPUT_mem_r

	T0t3_a1b1_mem1 = S.Task('T0t3_a1b1_mem1', length=1, delay_cost=1)
	S += T0t3_a1b1_mem1 >= 17
	T0t3_a1b1_mem1 += INPUT_mem_r

	T0t4_a0b0 = S.Task('T0t4_a0b0', length=7, delay_cost=1)
	S += T0t4_a0b0 >= 17
	T0t4_a0b0 += MUL[0]

	T1t3_a0b0 = S.Task('T1t3_a0b0', length=1, delay_cost=1)
	S += T1t3_a0b0 >= 17
	T1t3_a0b0 += ADD[3]

	T1t4_a0b0_in = S.Task('T1t4_a0b0_in', length=1, delay_cost=1)
	S += T1t4_a0b0_in >= 17
	T1t4_a0b0_in += MUL_in[0]

	T1t4_a0b0_mem0 = S.Task('T1t4_a0b0_mem0', length=1, delay_cost=1)
	S += T1t4_a0b0_mem0 >= 17
	T1t4_a0b0_mem0 += ADD_mem[2]

	T1t4_a0b0_mem1 = S.Task('T1t4_a0b0_mem1', length=1, delay_cost=1)
	S += T1t4_a0b0_mem1 >= 17
	T1t4_a0b0_mem1 += ADD_mem[3]

	T0t2_a1b1_mem0 = S.Task('T0t2_a1b1_mem0', length=1, delay_cost=1)
	S += T0t2_a1b1_mem0 >= 18
	T0t2_a1b1_mem0 += INPUT_mem_r

	T0t2_a1b1_mem1 = S.Task('T0t2_a1b1_mem1', length=1, delay_cost=1)
	S += T0t2_a1b1_mem1 >= 18
	T0t2_a1b1_mem1 += INPUT_mem_r

	T0t3_a1b1 = S.Task('T0t3_a1b1', length=1, delay_cost=1)
	S += T0t3_a1b1 >= 18
	T0t3_a1b1 += ADD[3]

	T1t4_a0b0 = S.Task('T1t4_a0b0', length=7, delay_cost=1)
	S += T1t4_a0b0 >= 18
	T1t4_a0b0 += MUL[0]

	T0t2_a1b1 = S.Task('T0t2_a1b1', length=1, delay_cost=1)
	S += T0t2_a1b1 >= 19
	T0t2_a1b1 += ADD[2]

	T0t4_a1b1_in = S.Task('T0t4_a1b1_in', length=1, delay_cost=1)
	S += T0t4_a1b1_in >= 19
	T0t4_a1b1_in += MUL_in[0]

	T0t4_a1b1_mem0 = S.Task('T0t4_a1b1_mem0', length=1, delay_cost=1)
	S += T0t4_a1b1_mem0 >= 19
	T0t4_a1b1_mem0 += ADD_mem[2]

	T0t4_a1b1_mem1 = S.Task('T0t4_a1b1_mem1', length=1, delay_cost=1)
	S += T0t4_a1b1_mem1 >= 19
	T0t4_a1b1_mem1 += ADD_mem[3]

	T1t3_a1b1_mem0 = S.Task('T1t3_a1b1_mem0', length=1, delay_cost=1)
	S += T1t3_a1b1_mem0 >= 19
	T1t3_a1b1_mem0 += INPUT_mem_r

	T1t3_a1b1_mem1 = S.Task('T1t3_a1b1_mem1', length=1, delay_cost=1)
	S += T1t3_a1b1_mem1 >= 19
	T1t3_a1b1_mem1 += INPUT_mem_r

	T0t4_a1b1 = S.Task('T0t4_a1b1', length=7, delay_cost=1)
	S += T0t4_a1b1 >= 20
	T0t4_a1b1 += MUL[0]

	T1t3_a1b1 = S.Task('T1t3_a1b1', length=1, delay_cost=1)
	S += T1t3_a1b1 >= 20
	T1t3_a1b1 += ADD[3]

	T1t4_a1b1_in = S.Task('T1t4_a1b1_in', length=1, delay_cost=1)
	S += T1t4_a1b1_in >= 20
	T1t4_a1b1_in += MUL_in[0]

	T1t4_a1b1_mem0 = S.Task('T1t4_a1b1_mem0', length=1, delay_cost=1)
	S += T1t4_a1b1_mem0 >= 20
	T1t4_a1b1_mem0 += ADD_mem[2]

	T1t4_a1b1_mem1 = S.Task('T1t4_a1b1_mem1', length=1, delay_cost=1)
	S += T1t4_a1b1_mem1 >= 20
	T1t4_a1b1_mem1 += ADD_mem[3]

	T5t2_1_mem0 = S.Task('T5t2_1_mem0', length=1, delay_cost=1)
	S += T5t2_1_mem0 >= 20
	T5t2_1_mem0 += INPUT_mem_r

	T5t2_1_mem1 = S.Task('T5t2_1_mem1', length=1, delay_cost=1)
	S += T5t2_1_mem1 >= 20
	T5t2_1_mem1 += INPUT_mem_r

	T1t4_a1b1 = S.Task('T1t4_a1b1', length=7, delay_cost=1)
	S += T1t4_a1b1 >= 21
	T1t4_a1b1 += MUL[0]

	T5t2_0_mem0 = S.Task('T5t2_0_mem0', length=1, delay_cost=1)
	S += T5t2_0_mem0 >= 21
	T5t2_0_mem0 += INPUT_mem_r

	T5t2_0_mem1 = S.Task('T5t2_0_mem1', length=1, delay_cost=1)
	S += T5t2_0_mem1 >= 21
	T5t2_0_mem1 += INPUT_mem_r

	T5t2_1 = S.Task('T5t2_1', length=1, delay_cost=1)
	S += T5t2_1 >= 21
	T5t2_1 += ADD[2]

	T5t2_0 = S.Task('T5t2_0', length=1, delay_cost=1)
	S += T5t2_0 >= 22
	T5t2_0 += ADD[3]

	T5t2_t2t3_mem0 = S.Task('T5t2_t2t3_mem0', length=1, delay_cost=1)
	S += T5t2_t2t3_mem0 >= 22
	T5t2_t2t3_mem0 += ADD_mem[3]

	T5t2_t2t3_mem1 = S.Task('T5t2_t2t3_mem1', length=1, delay_cost=1)
	S += T5t2_t2t3_mem1 >= 22
	T5t2_t2t3_mem1 += ADD_mem[2]

	T6t3_1_mem0 = S.Task('T6t3_1_mem0', length=1, delay_cost=1)
	S += T6t3_1_mem0 >= 22
	T6t3_1_mem0 += INPUT_mem_r

	T6t3_1_mem1 = S.Task('T6t3_1_mem1', length=1, delay_cost=1)
	S += T6t3_1_mem1 >= 22
	T6t3_1_mem1 += INPUT_mem_r

	T5t2_t2t3 = S.Task('T5t2_t2t3', length=1, delay_cost=1)
	S += T5t2_t2t3 >= 23
	T5t2_t2t3 += ADD[0]

	T6t3_0_mem0 = S.Task('T6t3_0_mem0', length=1, delay_cost=1)
	S += T6t3_0_mem0 >= 23
	T6t3_0_mem0 += INPUT_mem_r

	T6t3_0_mem1 = S.Task('T6t3_0_mem1', length=1, delay_cost=1)
	S += T6t3_0_mem1 >= 23
	T6t3_0_mem1 += INPUT_mem_r

	T6t3_1 = S.Task('T6t3_1', length=1, delay_cost=1)
	S += T6t3_1 >= 23
	T6t3_1 += ADD[2]

	T6t3_0 = S.Task('T6t3_0', length=1, delay_cost=1)
	S += T6t3_0 >= 24
	T6t3_0 += ADD[0]

	T6t3_a0b0_mem0 = S.Task('T6t3_a0b0_mem0', length=1, delay_cost=1)
	S += T6t3_a0b0_mem0 >= 24
	T6t3_a0b0_mem0 += INPUT_mem_r

	T6t3_a0b0_mem1 = S.Task('T6t3_a0b0_mem1', length=1, delay_cost=1)
	S += T6t3_a0b0_mem1 >= 24
	T6t3_a0b0_mem1 += INPUT_mem_r

	T6t3_t2t3_mem0 = S.Task('T6t3_t2t3_mem0', length=1, delay_cost=1)
	S += T6t3_t2t3_mem0 >= 24
	T6t3_t2t3_mem0 += ADD_mem[0]

	T6t3_t2t3_mem1 = S.Task('T6t3_t2t3_mem1', length=1, delay_cost=1)
	S += T6t3_t2t3_mem1 >= 24
	T6t3_t2t3_mem1 += ADD_mem[2]

	T5t2_a1b1_mem0 = S.Task('T5t2_a1b1_mem0', length=1, delay_cost=1)
	S += T5t2_a1b1_mem0 >= 25
	T5t2_a1b1_mem0 += INPUT_mem_r

	T5t2_a1b1_mem1 = S.Task('T5t2_a1b1_mem1', length=1, delay_cost=1)
	S += T5t2_a1b1_mem1 >= 25
	T5t2_a1b1_mem1 += INPUT_mem_r

	T6t3_a0b0 = S.Task('T6t3_a0b0', length=1, delay_cost=1)
	S += T6t3_a0b0 >= 25
	T6t3_a0b0 += ADD[0]

	T6t3_t2t3 = S.Task('T6t3_t2t3', length=1, delay_cost=1)
	S += T6t3_t2t3 >= 25
	T6t3_t2t3 += ADD[1]

	T5t2_a1b1 = S.Task('T5t2_a1b1', length=1, delay_cost=1)
	S += T5t2_a1b1 >= 26
	T5t2_a1b1 += ADD[3]

	T6t3_a1b1_mem0 = S.Task('T6t3_a1b1_mem0', length=1, delay_cost=1)
	S += T6t3_a1b1_mem0 >= 26
	T6t3_a1b1_mem0 += INPUT_mem_r

	T6t3_a1b1_mem1 = S.Task('T6t3_a1b1_mem1', length=1, delay_cost=1)
	S += T6t3_a1b1_mem1 >= 26
	T6t3_a1b1_mem1 += INPUT_mem_r

	T5t2_a0b0_mem0 = S.Task('T5t2_a0b0_mem0', length=1, delay_cost=1)
	S += T5t2_a0b0_mem0 >= 27
	T5t2_a0b0_mem0 += INPUT_mem_r

	T5t2_a0b0_mem1 = S.Task('T5t2_a0b0_mem1', length=1, delay_cost=1)
	S += T5t2_a0b0_mem1 >= 27
	T5t2_a0b0_mem1 += INPUT_mem_r

	T6t3_a1b1 = S.Task('T6t3_a1b1', length=1, delay_cost=1)
	S += T6t3_a1b1 >= 27
	T6t3_a1b1 += ADD[3]

	T5t2_a0b0 = S.Task('T5t2_a0b0', length=1, delay_cost=1)
	S += T5t2_a0b0 >= 28
	T5t2_a0b0 += ADD[0]


	# new tasks
	T0c1_a0b0 = S.Task('T0c1_a0b0', length=1, delay_cost=1)
	T0c1_a0b0 += alt(ADD)

	T0c1_a0b0_mem0 = S.Task('T0c1_a0b0_mem0', length=1, delay_cost=1)
	T0c1_a0b0_mem0 += MUL_mem[0]
	S += T0t4_a0b0<T0c1_a0b0_mem0
	S += T0c1_a0b0_mem0<=T0c1_a0b0

	T0c1_a0b0_mem1 = S.Task('T0c1_a0b0_mem1', length=1, delay_cost=1)
	T0c1_a0b0_mem1 += ADD_mem[1]
	S += T0t6_a0b0<T0c1_a0b0_mem1
	S += T0c1_a0b0_mem1<=T0c1_a0b0

	T0c1_a1b1 = S.Task('T0c1_a1b1', length=1, delay_cost=1)
	T0c1_a1b1 += alt(ADD)

	T0c1_a1b1_mem0 = S.Task('T0c1_a1b1_mem0', length=1, delay_cost=1)
	T0c1_a1b1_mem0 += MUL_mem[0]
	S += T0t4_a1b1<T0c1_a1b1_mem0
	S += T0c1_a1b1_mem0<=T0c1_a1b1

	T0c1_a1b1_mem1 = S.Task('T0c1_a1b1_mem1', length=1, delay_cost=1)
	T0c1_a1b1_mem1 += ADD_mem[1]
	S += T0t6_a1b1<T0c1_a1b1_mem1
	S += T0c1_a1b1_mem1<=T0c1_a1b1

	T0t4_t2t3_in = S.Task('T0t4_t2t3_in', length=1, delay_cost=1)
	T0t4_t2t3_in += alt(MUL_in)
	T0t4_t2t3 = S.Task('T0t4_t2t3', length=7, delay_cost=1)
	T0t4_t2t3 += alt(MUL)
	S+=T0t4_t2t3>=T0t4_t2t3_in

	T0t4_t2t3_mem0 = S.Task('T0t4_t2t3_mem0', length=1, delay_cost=1)
	T0t4_t2t3_mem0 += ADD_mem[3]
	S += T0t2_t2t3<T0t4_t2t3_mem0
	S += T0t4_t2t3_mem0<=T0t4_t2t3

	T0t4_t2t3_mem1 = S.Task('T0t4_t2t3_mem1', length=1, delay_cost=1)
	T0t4_t2t3_mem1 += ADD_mem[3]
	S += T0t3_t2t3<T0t4_t2t3_mem1
	S += T0t4_t2t3_mem1<=T0t4_t2t3

	T0c0_t2t3 = S.Task('T0c0_t2t3', length=1, delay_cost=1)
	T0c0_t2t3 += alt(ADD)

	T0c0_t2t3_mem0 = S.Task('T0c0_t2t3_mem0', length=1, delay_cost=1)
	T0c0_t2t3_mem0 += MUL_mem[0]
	S += T0t0_t2t3<T0c0_t2t3_mem0
	S += T0c0_t2t3_mem0<=T0c0_t2t3

	T0c0_t2t3_mem1 = S.Task('T0c0_t2t3_mem1', length=1, delay_cost=1)
	T0c0_t2t3_mem1 += MUL_mem[0]
	S += T0t1_t2t3<T0c0_t2t3_mem1
	S += T0c0_t2t3_mem1<=T0c0_t2t3

	T0t6_t2t3 = S.Task('T0t6_t2t3', length=1, delay_cost=1)
	T0t6_t2t3 += alt(ADD)

	T0t6_t2t3_mem0 = S.Task('T0t6_t2t3_mem0', length=1, delay_cost=1)
	T0t6_t2t3_mem0 += MUL_mem[0]
	S += T0t0_t2t3<T0t6_t2t3_mem0
	S += T0t6_t2t3_mem0<=T0t6_t2t3

	T0t6_t2t3_mem1 = S.Task('T0t6_t2t3_mem1', length=1, delay_cost=1)
	T0t6_t2t3_mem1 += MUL_mem[0]
	S += T0t1_t2t3<T0t6_t2t3_mem1
	S += T0t6_t2t3_mem1<=T0t6_t2t3

	T0t5_0 = S.Task('T0t5_0', length=1, delay_cost=1)
	T0t5_0 += alt(ADD)

	T0t5_0_mem0 = S.Task('T0t5_0_mem0', length=1, delay_cost=1)
	T0t5_0_mem0 += ADD_mem[1]
	S += T0c0_a0b0<T0t5_0_mem0
	S += T0t5_0_mem0<=T0t5_0

	T0t5_0_mem1 = S.Task('T0t5_0_mem1', length=1, delay_cost=1)
	T0t5_0_mem1 += ADD_mem[1]
	S += T0c0_a1b1<T0t5_0_mem1
	S += T0t5_0_mem1<=T0t5_0

	T1c1_a0b0 = S.Task('T1c1_a0b0', length=1, delay_cost=1)
	T1c1_a0b0 += alt(ADD)

	T1c1_a0b0_mem0 = S.Task('T1c1_a0b0_mem0', length=1, delay_cost=1)
	T1c1_a0b0_mem0 += MUL_mem[0]
	S += T1t4_a0b0<T1c1_a0b0_mem0
	S += T1c1_a0b0_mem0<=T1c1_a0b0

	T1c1_a0b0_mem1 = S.Task('T1c1_a0b0_mem1', length=1, delay_cost=1)
	T1c1_a0b0_mem1 += ADD_mem[1]
	S += T1t6_a0b0<T1c1_a0b0_mem1
	S += T1c1_a0b0_mem1<=T1c1_a0b0

	T1c1_a1b1 = S.Task('T1c1_a1b1', length=1, delay_cost=1)
	T1c1_a1b1 += alt(ADD)

	T1c1_a1b1_mem0 = S.Task('T1c1_a1b1_mem0', length=1, delay_cost=1)
	T1c1_a1b1_mem0 += MUL_mem[0]
	S += T1t4_a1b1<T1c1_a1b1_mem0
	S += T1c1_a1b1_mem0<=T1c1_a1b1

	T1c1_a1b1_mem1 = S.Task('T1c1_a1b1_mem1', length=1, delay_cost=1)
	T1c1_a1b1_mem1 += ADD_mem[0]
	S += T1t6_a1b1<T1c1_a1b1_mem1
	S += T1c1_a1b1_mem1<=T1c1_a1b1

	T1t4_t2t3_in = S.Task('T1t4_t2t3_in', length=1, delay_cost=1)
	T1t4_t2t3_in += alt(MUL_in)
	T1t4_t2t3 = S.Task('T1t4_t2t3', length=7, delay_cost=1)
	T1t4_t2t3 += alt(MUL)
	S+=T1t4_t2t3>=T1t4_t2t3_in

	T1t4_t2t3_mem0 = S.Task('T1t4_t2t3_mem0', length=1, delay_cost=1)
	T1t4_t2t3_mem0 += ADD_mem[3]
	S += T0t2_t2t3<T1t4_t2t3_mem0
	S += T1t4_t2t3_mem0<=T1t4_t2t3

	T1t4_t2t3_mem1 = S.Task('T1t4_t2t3_mem1', length=1, delay_cost=1)
	T1t4_t2t3_mem1 += ADD_mem[3]
	S += T1t3_t2t3<T1t4_t2t3_mem1
	S += T1t4_t2t3_mem1<=T1t4_t2t3

	T1c0_t2t3 = S.Task('T1c0_t2t3', length=1, delay_cost=1)
	T1c0_t2t3 += alt(ADD)

	T1c0_t2t3_mem0 = S.Task('T1c0_t2t3_mem0', length=1, delay_cost=1)
	T1c0_t2t3_mem0 += MUL_mem[0]
	S += T1t0_t2t3<T1c0_t2t3_mem0
	S += T1c0_t2t3_mem0<=T1c0_t2t3

	T1c0_t2t3_mem1 = S.Task('T1c0_t2t3_mem1', length=1, delay_cost=1)
	T1c0_t2t3_mem1 += MUL_mem[0]
	S += T1t1_t2t3<T1c0_t2t3_mem1
	S += T1c0_t2t3_mem1<=T1c0_t2t3

	T1t6_t2t3 = S.Task('T1t6_t2t3', length=1, delay_cost=1)
	T1t6_t2t3 += alt(ADD)

	T1t6_t2t3_mem0 = S.Task('T1t6_t2t3_mem0', length=1, delay_cost=1)
	T1t6_t2t3_mem0 += MUL_mem[0]
	S += T1t0_t2t3<T1t6_t2t3_mem0
	S += T1t6_t2t3_mem0<=T1t6_t2t3

	T1t6_t2t3_mem1 = S.Task('T1t6_t2t3_mem1', length=1, delay_cost=1)
	T1t6_t2t3_mem1 += MUL_mem[0]
	S += T1t1_t2t3<T1t6_t2t3_mem1
	S += T1t6_t2t3_mem1<=T1t6_t2t3

	T1t5_0 = S.Task('T1t5_0', length=1, delay_cost=1)
	T1t5_0 += alt(ADD)

	T1t5_0_mem0 = S.Task('T1t5_0_mem0', length=1, delay_cost=1)
	T1t5_0_mem0 += ADD_mem[1]
	S += T1c0_a0b0<T1t5_0_mem0
	S += T1t5_0_mem0<=T1t5_0

	T1t5_0_mem1 = S.Task('T1t5_0_mem1', length=1, delay_cost=1)
	T1t5_0_mem1 += ADD_mem[0]
	S += T1c0_a1b1<T1t5_0_mem1
	S += T1t5_0_mem1<=T1t5_0

	T0c1_t2t3 = S.Task('T0c1_t2t3', length=1, delay_cost=1)
	T0c1_t2t3 += alt(ADD)

	T0c1_t2t3_mem0 = S.Task('T0c1_t2t3_mem0', length=1, delay_cost=1)
	T0c1_t2t3_mem0 += alt(MUL_mem)
	S += (T0t4_t2t3*MUL[0])-1<T0c1_t2t3_mem0*MUL_mem[0]
	S += T0c1_t2t3_mem0<=T0c1_t2t3

	T0c1_t2t3_mem1 = S.Task('T0c1_t2t3_mem1', length=1, delay_cost=1)
	T0c1_t2t3_mem1 += alt(ADD_mem)
	S += (T0t6_t2t3*ADD[0])-1<T0c1_t2t3_mem1*ADD_mem[0]
	S += (T0t6_t2t3*ADD[1])-1<T0c1_t2t3_mem1*ADD_mem[1]
	S += (T0t6_t2t3*ADD[2])-1<T0c1_t2t3_mem1*ADD_mem[2]
	S += (T0t6_t2t3*ADD[3])-1<T0c1_t2t3_mem1*ADD_mem[3]
	S += T0c1_t2t3_mem1<=T0c1_t2t3

	T0s0_0 = S.Task('T0s0_0', length=1, delay_cost=1)
	T0s0_0 += alt(ADD)

	T0s0_0_mem0 = S.Task('T0s0_0_mem0', length=1, delay_cost=1)
	T0s0_0_mem0 += ADD_mem[1]
	S += T0c0_a1b1<T0s0_0_mem0
	S += T0s0_0_mem0<=T0s0_0

	T0s0_0_mem1 = S.Task('T0s0_0_mem1', length=1, delay_cost=1)
	T0s0_0_mem1 += alt(ADD_mem)
	S += (T0c1_a1b1*ADD[0])-1<T0s0_0_mem1*ADD_mem[0]
	S += (T0c1_a1b1*ADD[1])-1<T0s0_0_mem1*ADD_mem[1]
	S += (T0c1_a1b1*ADD[2])-1<T0s0_0_mem1*ADD_mem[2]
	S += (T0c1_a1b1*ADD[3])-1<T0s0_0_mem1*ADD_mem[3]
	S += T0s0_0_mem1<=T0s0_0

	T0s0_1 = S.Task('T0s0_1', length=1, delay_cost=1)
	T0s0_1 += alt(ADD)

	T0s0_1_mem0 = S.Task('T0s0_1_mem0', length=1, delay_cost=1)
	T0s0_1_mem0 += alt(ADD_mem)
	S += (T0c1_a1b1*ADD[0])-1<T0s0_1_mem0*ADD_mem[0]
	S += (T0c1_a1b1*ADD[1])-1<T0s0_1_mem0*ADD_mem[1]
	S += (T0c1_a1b1*ADD[2])-1<T0s0_1_mem0*ADD_mem[2]
	S += (T0c1_a1b1*ADD[3])-1<T0s0_1_mem0*ADD_mem[3]
	S += T0s0_1_mem0<=T0s0_1

	T0s0_1_mem1 = S.Task('T0s0_1_mem1', length=1, delay_cost=1)
	T0s0_1_mem1 += ADD_mem[1]
	S += T0c0_a1b1<T0s0_1_mem1
	S += T0s0_1_mem1<=T0s0_1

	T0t5_1 = S.Task('T0t5_1', length=1, delay_cost=1)
	T0t5_1 += alt(ADD)

	T0t5_1_mem0 = S.Task('T0t5_1_mem0', length=1, delay_cost=1)
	T0t5_1_mem0 += alt(ADD_mem)
	S += (T0c1_a0b0*ADD[0])-1<T0t5_1_mem0*ADD_mem[0]
	S += (T0c1_a0b0*ADD[1])-1<T0t5_1_mem0*ADD_mem[1]
	S += (T0c1_a0b0*ADD[2])-1<T0t5_1_mem0*ADD_mem[2]
	S += (T0c1_a0b0*ADD[3])-1<T0t5_1_mem0*ADD_mem[3]
	S += T0t5_1_mem0<=T0t5_1

	T0t5_1_mem1 = S.Task('T0t5_1_mem1', length=1, delay_cost=1)
	T0t5_1_mem1 += alt(ADD_mem)
	S += (T0c1_a1b1*ADD[0])-1<T0t5_1_mem1*ADD_mem[0]
	S += (T0c1_a1b1*ADD[1])-1<T0t5_1_mem1*ADD_mem[1]
	S += (T0c1_a1b1*ADD[2])-1<T0t5_1_mem1*ADD_mem[2]
	S += (T0c1_a1b1*ADD[3])-1<T0t5_1_mem1*ADD_mem[3]
	S += T0t5_1_mem1<=T0t5_1

	T010 = S.Task('T010', length=1, delay_cost=1)
	T010 += alt(ADD)

	T010_mem0 = S.Task('T010_mem0', length=1, delay_cost=1)
	T010_mem0 += alt(ADD_mem)
	S += (T0c0_t2t3*ADD[0])-1<T010_mem0*ADD_mem[0]
	S += (T0c0_t2t3*ADD[1])-1<T010_mem0*ADD_mem[1]
	S += (T0c0_t2t3*ADD[2])-1<T010_mem0*ADD_mem[2]
	S += (T0c0_t2t3*ADD[3])-1<T010_mem0*ADD_mem[3]
	S += T010_mem0<=T010

	T010_mem1 = S.Task('T010_mem1', length=1, delay_cost=1)
	T010_mem1 += alt(ADD_mem)
	S += (T0t5_0*ADD[0])-1<T010_mem1*ADD_mem[0]
	S += (T0t5_0*ADD[1])-1<T010_mem1*ADD_mem[1]
	S += (T0t5_0*ADD[2])-1<T010_mem1*ADD_mem[2]
	S += (T0t5_0*ADD[3])-1<T010_mem1*ADD_mem[3]
	S += T010_mem1<=T010

	T1c1_t2t3 = S.Task('T1c1_t2t3', length=1, delay_cost=1)
	T1c1_t2t3 += alt(ADD)

	T1c1_t2t3_mem0 = S.Task('T1c1_t2t3_mem0', length=1, delay_cost=1)
	T1c1_t2t3_mem0 += alt(MUL_mem)
	S += (T1t4_t2t3*MUL[0])-1<T1c1_t2t3_mem0*MUL_mem[0]
	S += T1c1_t2t3_mem0<=T1c1_t2t3

	T1c1_t2t3_mem1 = S.Task('T1c1_t2t3_mem1', length=1, delay_cost=1)
	T1c1_t2t3_mem1 += alt(ADD_mem)
	S += (T1t6_t2t3*ADD[0])-1<T1c1_t2t3_mem1*ADD_mem[0]
	S += (T1t6_t2t3*ADD[1])-1<T1c1_t2t3_mem1*ADD_mem[1]
	S += (T1t6_t2t3*ADD[2])-1<T1c1_t2t3_mem1*ADD_mem[2]
	S += (T1t6_t2t3*ADD[3])-1<T1c1_t2t3_mem1*ADD_mem[3]
	S += T1c1_t2t3_mem1<=T1c1_t2t3

	T1s0_0 = S.Task('T1s0_0', length=1, delay_cost=1)
	T1s0_0 += alt(ADD)

	T1s0_0_mem0 = S.Task('T1s0_0_mem0', length=1, delay_cost=1)
	T1s0_0_mem0 += ADD_mem[0]
	S += T1c0_a1b1<T1s0_0_mem0
	S += T1s0_0_mem0<=T1s0_0

	T1s0_0_mem1 = S.Task('T1s0_0_mem1', length=1, delay_cost=1)
	T1s0_0_mem1 += alt(ADD_mem)
	S += (T1c1_a1b1*ADD[0])-1<T1s0_0_mem1*ADD_mem[0]
	S += (T1c1_a1b1*ADD[1])-1<T1s0_0_mem1*ADD_mem[1]
	S += (T1c1_a1b1*ADD[2])-1<T1s0_0_mem1*ADD_mem[2]
	S += (T1c1_a1b1*ADD[3])-1<T1s0_0_mem1*ADD_mem[3]
	S += T1s0_0_mem1<=T1s0_0

	T1s0_1 = S.Task('T1s0_1', length=1, delay_cost=1)
	T1s0_1 += alt(ADD)

	T1s0_1_mem0 = S.Task('T1s0_1_mem0', length=1, delay_cost=1)
	T1s0_1_mem0 += alt(ADD_mem)
	S += (T1c1_a1b1*ADD[0])-1<T1s0_1_mem0*ADD_mem[0]
	S += (T1c1_a1b1*ADD[1])-1<T1s0_1_mem0*ADD_mem[1]
	S += (T1c1_a1b1*ADD[2])-1<T1s0_1_mem0*ADD_mem[2]
	S += (T1c1_a1b1*ADD[3])-1<T1s0_1_mem0*ADD_mem[3]
	S += T1s0_1_mem0<=T1s0_1

	T1s0_1_mem1 = S.Task('T1s0_1_mem1', length=1, delay_cost=1)
	T1s0_1_mem1 += ADD_mem[0]
	S += T1c0_a1b1<T1s0_1_mem1
	S += T1s0_1_mem1<=T1s0_1

	T1t5_1 = S.Task('T1t5_1', length=1, delay_cost=1)
	T1t5_1 += alt(ADD)

	T1t5_1_mem0 = S.Task('T1t5_1_mem0', length=1, delay_cost=1)
	T1t5_1_mem0 += alt(ADD_mem)
	S += (T1c1_a0b0*ADD[0])-1<T1t5_1_mem0*ADD_mem[0]
	S += (T1c1_a0b0*ADD[1])-1<T1t5_1_mem0*ADD_mem[1]
	S += (T1c1_a0b0*ADD[2])-1<T1t5_1_mem0*ADD_mem[2]
	S += (T1c1_a0b0*ADD[3])-1<T1t5_1_mem0*ADD_mem[3]
	S += T1t5_1_mem0<=T1t5_1

	T1t5_1_mem1 = S.Task('T1t5_1_mem1', length=1, delay_cost=1)
	T1t5_1_mem1 += alt(ADD_mem)
	S += (T1c1_a1b1*ADD[0])-1<T1t5_1_mem1*ADD_mem[0]
	S += (T1c1_a1b1*ADD[1])-1<T1t5_1_mem1*ADD_mem[1]
	S += (T1c1_a1b1*ADD[2])-1<T1t5_1_mem1*ADD_mem[2]
	S += (T1c1_a1b1*ADD[3])-1<T1t5_1_mem1*ADD_mem[3]
	S += T1t5_1_mem1<=T1t5_1

	T110 = S.Task('T110', length=1, delay_cost=1)
	T110 += alt(ADD)

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	T110_mem0 += alt(ADD_mem)
	S += (T1c0_t2t3*ADD[0])-1<T110_mem0*ADD_mem[0]
	S += (T1c0_t2t3*ADD[1])-1<T110_mem0*ADD_mem[1]
	S += (T1c0_t2t3*ADD[2])-1<T110_mem0*ADD_mem[2]
	S += (T1c0_t2t3*ADD[3])-1<T110_mem0*ADD_mem[3]
	S += T110_mem0<=T110

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	T110_mem1 += alt(ADD_mem)
	S += (T1t5_0*ADD[0])-1<T110_mem1*ADD_mem[0]
	S += (T1t5_0*ADD[1])-1<T110_mem1*ADD_mem[1]
	S += (T1t5_0*ADD[2])-1<T110_mem1*ADD_mem[2]
	S += (T1t5_0*ADD[3])-1<T110_mem1*ADD_mem[3]
	S += T110_mem1<=T110

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "padd_mul1_add4/padd_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_padd_mul1_add4_1(0, 0)