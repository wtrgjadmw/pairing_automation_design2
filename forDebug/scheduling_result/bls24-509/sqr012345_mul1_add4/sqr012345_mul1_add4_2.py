from pyschedule import Scenario, solvers, plotters, alt

def solve_sqr012345_mul1_add4_2(ConstStep, ExpStep):
	horizon = 151
	S=Scenario("sqr012345_mul1_add4_2",horizon = horizon)

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
	T7t1_a0b0_in = S.Task('T7t1_a0b0_in', length=1, delay_cost=1)
	S += T7t1_a0b0_in >= 0
	T7t1_a0b0_in += MUL_in[0]

	T7t1_a0b0_mem0 = S.Task('T7t1_a0b0_mem0', length=1, delay_cost=1)
	S += T7t1_a0b0_mem0 >= 0
	T7t1_a0b0_mem0 += INPUT_mem_r

	T7t1_a0b0_mem1 = S.Task('T7t1_a0b0_mem1', length=1, delay_cost=1)
	S += T7t1_a0b0_mem1 >= 0
	T7t1_a0b0_mem1 += INPUT_mem_r

	T7t1_a0b0 = S.Task('T7t1_a0b0', length=7, delay_cost=1)
	S += T7t1_a0b0 >= 1
	T7t1_a0b0 += MUL[0]

	T7t1_a1b1_in = S.Task('T7t1_a1b1_in', length=1, delay_cost=1)
	S += T7t1_a1b1_in >= 1
	T7t1_a1b1_in += MUL_in[0]

	T7t1_a1b1_mem0 = S.Task('T7t1_a1b1_mem0', length=1, delay_cost=1)
	S += T7t1_a1b1_mem0 >= 1
	T7t1_a1b1_mem0 += INPUT_mem_r

	T7t1_a1b1_mem1 = S.Task('T7t1_a1b1_mem1', length=1, delay_cost=1)
	S += T7t1_a1b1_mem1 >= 1
	T7t1_a1b1_mem1 += INPUT_mem_r

	T6t1_a0b0_in = S.Task('T6t1_a0b0_in', length=1, delay_cost=1)
	S += T6t1_a0b0_in >= 2
	T6t1_a0b0_in += MUL_in[0]

	T6t1_a0b0_mem0 = S.Task('T6t1_a0b0_mem0', length=1, delay_cost=1)
	S += T6t1_a0b0_mem0 >= 2
	T6t1_a0b0_mem0 += INPUT_mem_r

	T6t1_a0b0_mem1 = S.Task('T6t1_a0b0_mem1', length=1, delay_cost=1)
	S += T6t1_a0b0_mem1 >= 2
	T6t1_a0b0_mem1 += INPUT_mem_r

	T7t1_a1b1 = S.Task('T7t1_a1b1', length=7, delay_cost=1)
	S += T7t1_a1b1 >= 2
	T7t1_a1b1 += MUL[0]

	T6t1_a0b0 = S.Task('T6t1_a0b0', length=7, delay_cost=1)
	S += T6t1_a0b0 >= 3
	T6t1_a0b0 += MUL[0]

	T7t0_a1b1_in = S.Task('T7t0_a1b1_in', length=1, delay_cost=1)
	S += T7t0_a1b1_in >= 3
	T7t0_a1b1_in += MUL_in[0]

	T7t0_a1b1_mem0 = S.Task('T7t0_a1b1_mem0', length=1, delay_cost=1)
	S += T7t0_a1b1_mem0 >= 3
	T7t0_a1b1_mem0 += INPUT_mem_r

	T7t0_a1b1_mem1 = S.Task('T7t0_a1b1_mem1', length=1, delay_cost=1)
	S += T7t0_a1b1_mem1 >= 3
	T7t0_a1b1_mem1 += INPUT_mem_r

	T5t1_a0b0_in = S.Task('T5t1_a0b0_in', length=1, delay_cost=1)
	S += T5t1_a0b0_in >= 4
	T5t1_a0b0_in += MUL_in[0]

	T5t1_a0b0_mem0 = S.Task('T5t1_a0b0_mem0', length=1, delay_cost=1)
	S += T5t1_a0b0_mem0 >= 4
	T5t1_a0b0_mem0 += INPUT_mem_r

	T5t1_a0b0_mem1 = S.Task('T5t1_a0b0_mem1', length=1, delay_cost=1)
	S += T5t1_a0b0_mem1 >= 4
	T5t1_a0b0_mem1 += INPUT_mem_r

	T7t0_a1b1 = S.Task('T7t0_a1b1', length=7, delay_cost=1)
	S += T7t0_a1b1 >= 4
	T7t0_a1b1 += MUL[0]

	T5t0_a1b1_in = S.Task('T5t0_a1b1_in', length=1, delay_cost=1)
	S += T5t0_a1b1_in >= 5
	T5t0_a1b1_in += MUL_in[0]

	T5t0_a1b1_mem0 = S.Task('T5t0_a1b1_mem0', length=1, delay_cost=1)
	S += T5t0_a1b1_mem0 >= 5
	T5t0_a1b1_mem0 += INPUT_mem_r

	T5t0_a1b1_mem1 = S.Task('T5t0_a1b1_mem1', length=1, delay_cost=1)
	S += T5t0_a1b1_mem1 >= 5
	T5t0_a1b1_mem1 += INPUT_mem_r

	T5t1_a0b0 = S.Task('T5t1_a0b0', length=7, delay_cost=1)
	S += T5t1_a0b0 >= 5
	T5t1_a0b0 += MUL[0]

	T5t0_a0b0_in = S.Task('T5t0_a0b0_in', length=1, delay_cost=1)
	S += T5t0_a0b0_in >= 6
	T5t0_a0b0_in += MUL_in[0]

	T5t0_a0b0_mem0 = S.Task('T5t0_a0b0_mem0', length=1, delay_cost=1)
	S += T5t0_a0b0_mem0 >= 6
	T5t0_a0b0_mem0 += INPUT_mem_r

	T5t0_a0b0_mem1 = S.Task('T5t0_a0b0_mem1', length=1, delay_cost=1)
	S += T5t0_a0b0_mem1 >= 6
	T5t0_a0b0_mem1 += INPUT_mem_r

	T5t0_a1b1 = S.Task('T5t0_a1b1', length=7, delay_cost=1)
	S += T5t0_a1b1 >= 6
	T5t0_a1b1 += MUL[0]

	T4t0_a0a1_in = S.Task('T4t0_a0a1_in', length=1, delay_cost=1)
	S += T4t0_a0a1_in >= 7
	T4t0_a0a1_in += MUL_in[0]

	T4t0_a0a1_mem0 = S.Task('T4t0_a0a1_mem0', length=1, delay_cost=1)
	S += T4t0_a0a1_mem0 >= 7
	T4t0_a0a1_mem0 += INPUT_mem_r

	T4t0_a0a1_mem1 = S.Task('T4t0_a0a1_mem1', length=1, delay_cost=1)
	S += T4t0_a0a1_mem1 >= 7
	T4t0_a0a1_mem1 += INPUT_mem_r

	T5t0_a0b0 = S.Task('T5t0_a0b0', length=7, delay_cost=1)
	S += T5t0_a0b0 >= 7
	T5t0_a0b0 += MUL[0]

	T4t0_a0a1 = S.Task('T4t0_a0a1', length=7, delay_cost=1)
	S += T4t0_a0a1 >= 8
	T4t0_a0a1 += MUL[0]

	T6t1_a1b1_in = S.Task('T6t1_a1b1_in', length=1, delay_cost=1)
	S += T6t1_a1b1_in >= 8
	T6t1_a1b1_in += MUL_in[0]

	T6t1_a1b1_mem0 = S.Task('T6t1_a1b1_mem0', length=1, delay_cost=1)
	S += T6t1_a1b1_mem0 >= 8
	T6t1_a1b1_mem0 += INPUT_mem_r

	T6t1_a1b1_mem1 = S.Task('T6t1_a1b1_mem1', length=1, delay_cost=1)
	S += T6t1_a1b1_mem1 >= 8
	T6t1_a1b1_mem1 += INPUT_mem_r

	T6t1_a1b1 = S.Task('T6t1_a1b1', length=7, delay_cost=1)
	S += T6t1_a1b1 >= 9
	T6t1_a1b1 += MUL[0]

	T7t0_a0b0_in = S.Task('T7t0_a0b0_in', length=1, delay_cost=1)
	S += T7t0_a0b0_in >= 9
	T7t0_a0b0_in += MUL_in[0]

	T7t0_a0b0_mem0 = S.Task('T7t0_a0b0_mem0', length=1, delay_cost=1)
	S += T7t0_a0b0_mem0 >= 9
	T7t0_a0b0_mem0 += INPUT_mem_r

	T7t0_a0b0_mem1 = S.Task('T7t0_a0b0_mem1', length=1, delay_cost=1)
	S += T7t0_a0b0_mem1 >= 9
	T7t0_a0b0_mem1 += INPUT_mem_r

	T6t0_a1b1_in = S.Task('T6t0_a1b1_in', length=1, delay_cost=1)
	S += T6t0_a1b1_in >= 10
	T6t0_a1b1_in += MUL_in[0]

	T6t0_a1b1_mem0 = S.Task('T6t0_a1b1_mem0', length=1, delay_cost=1)
	S += T6t0_a1b1_mem0 >= 10
	T6t0_a1b1_mem0 += INPUT_mem_r

	T6t0_a1b1_mem1 = S.Task('T6t0_a1b1_mem1', length=1, delay_cost=1)
	S += T6t0_a1b1_mem1 >= 10
	T6t0_a1b1_mem1 += INPUT_mem_r

	T7c0_a1b1_mem0 = S.Task('T7c0_a1b1_mem0', length=1, delay_cost=1)
	S += T7c0_a1b1_mem0 >= 10
	T7c0_a1b1_mem0 += MUL_mem[0]

	T7c0_a1b1_mem1 = S.Task('T7c0_a1b1_mem1', length=1, delay_cost=1)
	S += T7c0_a1b1_mem1 >= 10
	T7c0_a1b1_mem1 += MUL_mem[0]

	T7t0_a0b0 = S.Task('T7t0_a0b0', length=7, delay_cost=1)
	S += T7t0_a0b0 >= 10
	T7t0_a0b0 += MUL[0]

	T6t0_a0b0_in = S.Task('T6t0_a0b0_in', length=1, delay_cost=1)
	S += T6t0_a0b0_in >= 11
	T6t0_a0b0_in += MUL_in[0]

	T6t0_a0b0_mem0 = S.Task('T6t0_a0b0_mem0', length=1, delay_cost=1)
	S += T6t0_a0b0_mem0 >= 11
	T6t0_a0b0_mem0 += INPUT_mem_r

	T6t0_a0b0_mem1 = S.Task('T6t0_a0b0_mem1', length=1, delay_cost=1)
	S += T6t0_a0b0_mem1 >= 11
	T6t0_a0b0_mem1 += INPUT_mem_r

	T6t0_a1b1 = S.Task('T6t0_a1b1', length=7, delay_cost=1)
	S += T6t0_a1b1 >= 11
	T6t0_a1b1 += MUL[0]

	T7c0_a1b1 = S.Task('T7c0_a1b1', length=1, delay_cost=1)
	S += T7c0_a1b1 >= 11
	T7c0_a1b1 += ADD[3]

	T7t6_a1b1_mem0 = S.Task('T7t6_a1b1_mem0', length=1, delay_cost=1)
	S += T7t6_a1b1_mem0 >= 11
	T7t6_a1b1_mem0 += MUL_mem[0]

	T7t6_a1b1_mem1 = S.Task('T7t6_a1b1_mem1', length=1, delay_cost=1)
	S += T7t6_a1b1_mem1 >= 11
	T7t6_a1b1_mem1 += MUL_mem[0]

	T5t1_a1b1_in = S.Task('T5t1_a1b1_in', length=1, delay_cost=1)
	S += T5t1_a1b1_in >= 12
	T5t1_a1b1_in += MUL_in[0]

	T5t1_a1b1_mem0 = S.Task('T5t1_a1b1_mem0', length=1, delay_cost=1)
	S += T5t1_a1b1_mem0 >= 12
	T5t1_a1b1_mem0 += INPUT_mem_r

	T5t1_a1b1_mem1 = S.Task('T5t1_a1b1_mem1', length=1, delay_cost=1)
	S += T5t1_a1b1_mem1 >= 12
	T5t1_a1b1_mem1 += INPUT_mem_r

	T6t0_a0b0 = S.Task('T6t0_a0b0', length=7, delay_cost=1)
	S += T6t0_a0b0 >= 12
	T6t0_a0b0 += MUL[0]

	T7t6_a1b1 = S.Task('T7t6_a1b1', length=1, delay_cost=1)
	S += T7t6_a1b1 >= 12
	T7t6_a1b1 += ADD[3]

	T4t1_a0a1_in = S.Task('T4t1_a0a1_in', length=1, delay_cost=1)
	S += T4t1_a0a1_in >= 13
	T4t1_a0a1_in += MUL_in[0]

	T4t1_a0a1_mem0 = S.Task('T4t1_a0a1_mem0', length=1, delay_cost=1)
	S += T4t1_a0a1_mem0 >= 13
	T4t1_a0a1_mem0 += INPUT_mem_r

	T4t1_a0a1_mem1 = S.Task('T4t1_a0a1_mem1', length=1, delay_cost=1)
	S += T4t1_a0a1_mem1 >= 13
	T4t1_a0a1_mem1 += INPUT_mem_r

	T5c0_a0b0_mem0 = S.Task('T5c0_a0b0_mem0', length=1, delay_cost=1)
	S += T5c0_a0b0_mem0 >= 13
	T5c0_a0b0_mem0 += MUL_mem[0]

	T5c0_a0b0_mem1 = S.Task('T5c0_a0b0_mem1', length=1, delay_cost=1)
	S += T5c0_a0b0_mem1 >= 13
	T5c0_a0b0_mem1 += MUL_mem[0]

	T5t1_a1b1 = S.Task('T5t1_a1b1', length=7, delay_cost=1)
	S += T5t1_a1b1 >= 13
	T5t1_a1b1 += MUL[0]

	T3t1_a1b1_in = S.Task('T3t1_a1b1_in', length=1, delay_cost=1)
	S += T3t1_a1b1_in >= 14
	T3t1_a1b1_in += MUL_in[0]

	T3t1_a1b1_mem0 = S.Task('T3t1_a1b1_mem0', length=1, delay_cost=1)
	S += T3t1_a1b1_mem0 >= 14
	T3t1_a1b1_mem0 += INPUT_mem_r

	T3t1_a1b1_mem1 = S.Task('T3t1_a1b1_mem1', length=1, delay_cost=1)
	S += T3t1_a1b1_mem1 >= 14
	T3t1_a1b1_mem1 += INPUT_mem_r

	T4t1_a0a1 = S.Task('T4t1_a0a1', length=7, delay_cost=1)
	S += T4t1_a0a1 >= 14
	T4t1_a0a1 += MUL[0]

	T5c0_a0b0 = S.Task('T5c0_a0b0', length=1, delay_cost=1)
	S += T5c0_a0b0 >= 14
	T5c0_a0b0 += ADD[0]

	T5t6_a0b0_mem0 = S.Task('T5t6_a0b0_mem0', length=1, delay_cost=1)
	S += T5t6_a0b0_mem0 >= 14
	T5t6_a0b0_mem0 += MUL_mem[0]

	T5t6_a0b0_mem1 = S.Task('T5t6_a0b0_mem1', length=1, delay_cost=1)
	S += T5t6_a0b0_mem1 >= 14
	T5t6_a0b0_mem1 += MUL_mem[0]

	T3t1_a0b0_in = S.Task('T3t1_a0b0_in', length=1, delay_cost=1)
	S += T3t1_a0b0_in >= 15
	T3t1_a0b0_in += MUL_in[0]

	T3t1_a0b0_mem0 = S.Task('T3t1_a0b0_mem0', length=1, delay_cost=1)
	S += T3t1_a0b0_mem0 >= 15
	T3t1_a0b0_mem0 += INPUT_mem_r

	T3t1_a0b0_mem1 = S.Task('T3t1_a0b0_mem1', length=1, delay_cost=1)
	S += T3t1_a0b0_mem1 >= 15
	T3t1_a0b0_mem1 += INPUT_mem_r

	T3t1_a1b1 = S.Task('T3t1_a1b1', length=7, delay_cost=1)
	S += T3t1_a1b1 >= 15
	T3t1_a1b1 += MUL[0]

	T5t6_a0b0 = S.Task('T5t6_a0b0', length=1, delay_cost=1)
	S += T5t6_a0b0 >= 15
	T5t6_a0b0 += ADD[1]

	T3t0_a1b1_in = S.Task('T3t0_a1b1_in', length=1, delay_cost=1)
	S += T3t0_a1b1_in >= 16
	T3t0_a1b1_in += MUL_in[0]

	T3t0_a1b1_mem0 = S.Task('T3t0_a1b1_mem0', length=1, delay_cost=1)
	S += T3t0_a1b1_mem0 >= 16
	T3t0_a1b1_mem0 += INPUT_mem_r

	T3t0_a1b1_mem1 = S.Task('T3t0_a1b1_mem1', length=1, delay_cost=1)
	S += T3t0_a1b1_mem1 >= 16
	T3t0_a1b1_mem1 += INPUT_mem_r

	T3t1_a0b0 = S.Task('T3t1_a0b0', length=7, delay_cost=1)
	S += T3t1_a0b0 >= 16
	T3t1_a0b0 += MUL[0]

	T7t6_a0b0_mem0 = S.Task('T7t6_a0b0_mem0', length=1, delay_cost=1)
	S += T7t6_a0b0_mem0 >= 16
	T7t6_a0b0_mem0 += MUL_mem[0]

	T7t6_a0b0_mem1 = S.Task('T7t6_a0b0_mem1', length=1, delay_cost=1)
	S += T7t6_a0b0_mem1 >= 16
	T7t6_a0b0_mem1 += MUL_mem[0]

	T3t0_a0b0_in = S.Task('T3t0_a0b0_in', length=1, delay_cost=1)
	S += T3t0_a0b0_in >= 17
	T3t0_a0b0_in += MUL_in[0]

	T3t0_a0b0_mem0 = S.Task('T3t0_a0b0_mem0', length=1, delay_cost=1)
	S += T3t0_a0b0_mem0 >= 17
	T3t0_a0b0_mem0 += INPUT_mem_r

	T3t0_a0b0_mem1 = S.Task('T3t0_a0b0_mem1', length=1, delay_cost=1)
	S += T3t0_a0b0_mem1 >= 17
	T3t0_a0b0_mem1 += INPUT_mem_r

	T3t0_a1b1 = S.Task('T3t0_a1b1', length=7, delay_cost=1)
	S += T3t0_a1b1 >= 17
	T3t0_a1b1 += MUL[0]

	T6c0_a1b1_mem0 = S.Task('T6c0_a1b1_mem0', length=1, delay_cost=1)
	S += T6c0_a1b1_mem0 >= 17
	T6c0_a1b1_mem0 += MUL_mem[0]

	T6c0_a1b1_mem1 = S.Task('T6c0_a1b1_mem1', length=1, delay_cost=1)
	S += T6c0_a1b1_mem1 >= 17
	T6c0_a1b1_mem1 += MUL_mem[0]

	T7t6_a0b0 = S.Task('T7t6_a0b0', length=1, delay_cost=1)
	S += T7t6_a0b0 >= 17
	T7t6_a0b0 += ADD[1]

	T0t1_a0a1_in = S.Task('T0t1_a0a1_in', length=1, delay_cost=1)
	S += T0t1_a0a1_in >= 18
	T0t1_a0a1_in += MUL_in[0]

	T0t1_a0a1_mem0 = S.Task('T0t1_a0a1_mem0', length=1, delay_cost=1)
	S += T0t1_a0a1_mem0 >= 18
	T0t1_a0a1_mem0 += INPUT_mem_r

	T0t1_a0a1_mem1 = S.Task('T0t1_a0a1_mem1', length=1, delay_cost=1)
	S += T0t1_a0a1_mem1 >= 18
	T0t1_a0a1_mem1 += INPUT_mem_r

	T3t0_a0b0 = S.Task('T3t0_a0b0', length=7, delay_cost=1)
	S += T3t0_a0b0 >= 18
	T3t0_a0b0 += MUL[0]

	T6c0_a1b1 = S.Task('T6c0_a1b1', length=1, delay_cost=1)
	S += T6c0_a1b1 >= 18
	T6c0_a1b1 += ADD[1]

	T7c0_a0b0_mem0 = S.Task('T7c0_a0b0_mem0', length=1, delay_cost=1)
	S += T7c0_a0b0_mem0 >= 18
	T7c0_a0b0_mem0 += MUL_mem[0]

	T7c0_a0b0_mem1 = S.Task('T7c0_a0b0_mem1', length=1, delay_cost=1)
	S += T7c0_a0b0_mem1 >= 18
	T7c0_a0b0_mem1 += MUL_mem[0]

	T0t0_a0a1_in = S.Task('T0t0_a0a1_in', length=1, delay_cost=1)
	S += T0t0_a0a1_in >= 19
	T0t0_a0a1_in += MUL_in[0]

	T0t0_a0a1_mem0 = S.Task('T0t0_a0a1_mem0', length=1, delay_cost=1)
	S += T0t0_a0a1_mem0 >= 19
	T0t0_a0a1_mem0 += INPUT_mem_r

	T0t0_a0a1_mem1 = S.Task('T0t0_a0a1_mem1', length=1, delay_cost=1)
	S += T0t0_a0a1_mem1 >= 19
	T0t0_a0a1_mem1 += INPUT_mem_r

	T0t1_a0a1 = S.Task('T0t1_a0a1', length=7, delay_cost=1)
	S += T0t1_a0a1 >= 19
	T0t1_a0a1 += MUL[0]

	T6t6_a0b0_mem0 = S.Task('T6t6_a0b0_mem0', length=1, delay_cost=1)
	S += T6t6_a0b0_mem0 >= 19
	T6t6_a0b0_mem0 += MUL_mem[0]

	T6t6_a0b0_mem1 = S.Task('T6t6_a0b0_mem1', length=1, delay_cost=1)
	S += T6t6_a0b0_mem1 >= 19
	T6t6_a0b0_mem1 += MUL_mem[0]

	T7c0_a0b0 = S.Task('T7c0_a0b0', length=1, delay_cost=1)
	S += T7c0_a0b0 >= 19
	T7c0_a0b0 += ADD[3]

	T0t0_a0a1 = S.Task('T0t0_a0a1', length=7, delay_cost=1)
	S += T0t0_a0a1 >= 20
	T0t0_a0a1 += MUL[0]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 20
	T110_mem0 += INPUT_mem_r

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 20
	T110_mem1 += INPUT_mem_r

	T4c0_a0a1_mem0 = S.Task('T4c0_a0a1_mem0', length=1, delay_cost=1)
	S += T4c0_a0a1_mem0 >= 20
	T4c0_a0a1_mem0 += MUL_mem[0]

	T4c0_a0a1_mem1 = S.Task('T4c0_a0a1_mem1', length=1, delay_cost=1)
	S += T4c0_a0a1_mem1 >= 20
	T4c0_a0a1_mem1 += MUL_mem[0]

	T6t6_a0b0 = S.Task('T6t6_a0b0', length=1, delay_cost=1)
	S += T6t6_a0b0 >= 20
	T6t6_a0b0 += ADD[2]

	T0t2_a0a1_mem0 = S.Task('T0t2_a0a1_mem0', length=1, delay_cost=1)
	S += T0t2_a0a1_mem0 >= 21
	T0t2_a0a1_mem0 += INPUT_mem_r

	T0t2_a0a1_mem1 = S.Task('T0t2_a0a1_mem1', length=1, delay_cost=1)
	S += T0t2_a0a1_mem1 >= 21
	T0t2_a0a1_mem1 += INPUT_mem_r

	T110 = S.Task('T110', length=1, delay_cost=1)
	S += T110 >= 21
	T110 += ADD[0]

	T4c0_a0a1 = S.Task('T4c0_a0a1', length=1, delay_cost=1)
	S += T4c0_a0a1 >= 21
	T4c0_a0a1 += ADD[2]

	T5t6_a1b1_mem0 = S.Task('T5t6_a1b1_mem0', length=1, delay_cost=1)
	S += T5t6_a1b1_mem0 >= 21
	T5t6_a1b1_mem0 += MUL_mem[0]

	T5t6_a1b1_mem1 = S.Task('T5t6_a1b1_mem1', length=1, delay_cost=1)
	S += T5t6_a1b1_mem1 >= 21
	T5t6_a1b1_mem1 += MUL_mem[0]

	T0a10_new_mem0 = S.Task('T0a10_new_mem0', length=1, delay_cost=1)
	S += T0a10_new_mem0 >= 22
	T0a10_new_mem0 += INPUT_mem_r

	T0a10_new_mem1 = S.Task('T0a10_new_mem1', length=1, delay_cost=1)
	S += T0a10_new_mem1 >= 22
	T0a10_new_mem1 += INPUT_mem_r

	T0t2_a0a1 = S.Task('T0t2_a0a1', length=1, delay_cost=1)
	S += T0t2_a0a1 >= 22
	T0t2_a0a1 += ADD[0]

	T5t6_a1b1 = S.Task('T5t6_a1b1', length=1, delay_cost=1)
	S += T5t6_a1b1 >= 22
	T5t6_a1b1 += ADD[3]

	T6t6_a1b1_mem0 = S.Task('T6t6_a1b1_mem0', length=1, delay_cost=1)
	S += T6t6_a1b1_mem0 >= 22
	T6t6_a1b1_mem0 += MUL_mem[0]

	T6t6_a1b1_mem1 = S.Task('T6t6_a1b1_mem1', length=1, delay_cost=1)
	S += T6t6_a1b1_mem1 >= 22
	T6t6_a1b1_mem1 += MUL_mem[0]

	T0a10_new = S.Task('T0a10_new', length=1, delay_cost=1)
	S += T0a10_new >= 23
	T0a10_new += ADD[0]

	T3t6_a1b1_mem0 = S.Task('T3t6_a1b1_mem0', length=1, delay_cost=1)
	S += T3t6_a1b1_mem0 >= 23
	T3t6_a1b1_mem0 += MUL_mem[0]

	T3t6_a1b1_mem1 = S.Task('T3t6_a1b1_mem1', length=1, delay_cost=1)
	S += T3t6_a1b1_mem1 >= 23
	T3t6_a1b1_mem1 += MUL_mem[0]

	T6t6_a1b1 = S.Task('T6t6_a1b1', length=1, delay_cost=1)
	S += T6t6_a1b1 >= 23
	T6t6_a1b1 += ADD[1]

	T7t2_1_mem0 = S.Task('T7t2_1_mem0', length=1, delay_cost=1)
	S += T7t2_1_mem0 >= 23
	T7t2_1_mem0 += INPUT_mem_r

	T7t2_1_mem1 = S.Task('T7t2_1_mem1', length=1, delay_cost=1)
	S += T7t2_1_mem1 >= 23
	T7t2_1_mem1 += INPUT_mem_r

	T3t6_a0b0_mem0 = S.Task('T3t6_a0b0_mem0', length=1, delay_cost=1)
	S += T3t6_a0b0_mem0 >= 24
	T3t6_a0b0_mem0 += MUL_mem[0]

	T3t6_a0b0_mem1 = S.Task('T3t6_a0b0_mem1', length=1, delay_cost=1)
	S += T3t6_a0b0_mem1 >= 24
	T3t6_a0b0_mem1 += MUL_mem[0]

	T3t6_a1b1 = S.Task('T3t6_a1b1', length=1, delay_cost=1)
	S += T3t6_a1b1 >= 24
	T3t6_a1b1 += ADD[1]

	T6t3_a0b0_mem0 = S.Task('T6t3_a0b0_mem0', length=1, delay_cost=1)
	S += T6t3_a0b0_mem0 >= 24
	T6t3_a0b0_mem0 += INPUT_mem_r

	T6t3_a0b0_mem1 = S.Task('T6t3_a0b0_mem1', length=1, delay_cost=1)
	S += T6t3_a0b0_mem1 >= 24
	T6t3_a0b0_mem1 += INPUT_mem_r

	T7t2_1 = S.Task('T7t2_1', length=1, delay_cost=1)
	S += T7t2_1 >= 24
	T7t2_1 += ADD[0]

	T3c0_a1b1_mem0 = S.Task('T3c0_a1b1_mem0', length=1, delay_cost=1)
	S += T3c0_a1b1_mem0 >= 25
	T3c0_a1b1_mem0 += MUL_mem[0]

	T3c0_a1b1_mem1 = S.Task('T3c0_a1b1_mem1', length=1, delay_cost=1)
	S += T3c0_a1b1_mem1 >= 25
	T3c0_a1b1_mem1 += MUL_mem[0]

	T3t2_1_mem0 = S.Task('T3t2_1_mem0', length=1, delay_cost=1)
	S += T3t2_1_mem0 >= 25
	T3t2_1_mem0 += INPUT_mem_r

	T3t2_1_mem1 = S.Task('T3t2_1_mem1', length=1, delay_cost=1)
	S += T3t2_1_mem1 >= 25
	T3t2_1_mem1 += INPUT_mem_r

	T3t6_a0b0 = S.Task('T3t6_a0b0', length=1, delay_cost=1)
	S += T3t6_a0b0 >= 25
	T3t6_a0b0 += ADD[1]

	T6t3_a0b0 = S.Task('T6t3_a0b0', length=1, delay_cost=1)
	S += T6t3_a0b0 >= 25
	T6t3_a0b0 += ADD[0]

	T0c0_a0a1_mem0 = S.Task('T0c0_a0a1_mem0', length=1, delay_cost=1)
	S += T0c0_a0a1_mem0 >= 26
	T0c0_a0a1_mem0 += MUL_mem[0]

	T0c0_a0a1_mem1 = S.Task('T0c0_a0a1_mem1', length=1, delay_cost=1)
	S += T0c0_a0a1_mem1 >= 26
	T0c0_a0a1_mem1 += MUL_mem[0]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 26
	T100_mem0 += INPUT_mem_r

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 26
	T100_mem1 += INPUT_mem_r

	T3c0_a1b1 = S.Task('T3c0_a1b1', length=1, delay_cost=1)
	S += T3c0_a1b1 >= 26
	T3c0_a1b1 += ADD[0]

	T3t2_1 = S.Task('T3t2_1', length=1, delay_cost=1)
	S += T3t2_1 >= 26
	T3t2_1 += ADD[3]

	T7t1_t2t3_in = S.Task('T7t1_t2t3_in', length=1, delay_cost=1)
	S += T7t1_t2t3_in >= 26
	T7t1_t2t3_in += MUL_in[0]

	T7t1_t2t3_mem0 = S.Task('T7t1_t2t3_mem0', length=1, delay_cost=1)
	S += T7t1_t2t3_mem0 >= 26
	T7t1_t2t3_mem0 += ADD_mem[0]

	T7t1_t2t3_mem1 = S.Task('T7t1_t2t3_mem1', length=1, delay_cost=1)
	S += T7t1_t2t3_mem1 >= 26
	T7t1_t2t3_mem1 += ADD_mem[3]

	T0c0_a0a1 = S.Task('T0c0_a0a1', length=1, delay_cost=1)
	S += T0c0_a0a1 >= 27
	T0c0_a0a1 += ADD[1]

	T0t11_mem0 = S.Task('T0t11_mem0', length=1, delay_cost=1)
	S += T0t11_mem0 >= 27
	T0t11_mem0 += INPUT_mem_r

	T0t11_mem1 = S.Task('T0t11_mem1', length=1, delay_cost=1)
	S += T0t11_mem1 >= 27
	T0t11_mem1 += INPUT_mem_r

	T0t6_a0a1_mem0 = S.Task('T0t6_a0a1_mem0', length=1, delay_cost=1)
	S += T0t6_a0a1_mem0 >= 27
	T0t6_a0a1_mem0 += MUL_mem[0]

	T0t6_a0a1_mem1 = S.Task('T0t6_a0a1_mem1', length=1, delay_cost=1)
	S += T0t6_a0a1_mem1 >= 27
	T0t6_a0a1_mem1 += MUL_mem[0]

	T100 = S.Task('T100', length=1, delay_cost=1)
	S += T100 >= 27
	T100 += ADD[0]

	T7t1_t2t3 = S.Task('T7t1_t2t3', length=7, delay_cost=1)
	S += T7t1_t2t3 >= 27
	T7t1_t2t3 += MUL[0]

	T0t11 = S.Task('T0t11', length=1, delay_cost=1)
	S += T0t11 >= 28
	T0t11 += ADD[0]

	T0t6_a0a1 = S.Task('T0t6_a0a1', length=1, delay_cost=1)
	S += T0t6_a0a1 >= 28
	T0t6_a0a1 += ADD[1]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 28
	T101_mem0 += INPUT_mem_r

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 28
	T101_mem1 += INPUT_mem_r

	T3c0_a0b0_mem0 = S.Task('T3c0_a0b0_mem0', length=1, delay_cost=1)
	S += T3c0_a0b0_mem0 >= 28
	T3c0_a0b0_mem0 += MUL_mem[0]

	T3c0_a0b0_mem1 = S.Task('T3c0_a0b0_mem1', length=1, delay_cost=1)
	S += T3c0_a0b0_mem1 >= 28
	T3c0_a0b0_mem1 += MUL_mem[0]

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 29
	T101 += ADD[0]

	T3c0_a0b0 = S.Task('T3c0_a0b0', length=1, delay_cost=1)
	S += T3c0_a0b0 >= 29
	T3c0_a0b0 += ADD[1]

	T6c0_a0b0_mem0 = S.Task('T6c0_a0b0_mem0', length=1, delay_cost=1)
	S += T6c0_a0b0_mem0 >= 29
	T6c0_a0b0_mem0 += MUL_mem[0]

	T6c0_a0b0_mem1 = S.Task('T6c0_a0b0_mem1', length=1, delay_cost=1)
	S += T6c0_a0b0_mem1 >= 29
	T6c0_a0b0_mem1 += MUL_mem[0]

	T6t3_a1b1_mem0 = S.Task('T6t3_a1b1_mem0', length=1, delay_cost=1)
	S += T6t3_a1b1_mem0 >= 29
	T6t3_a1b1_mem0 += INPUT_mem_r

	T6t3_a1b1_mem1 = S.Task('T6t3_a1b1_mem1', length=1, delay_cost=1)
	S += T6t3_a1b1_mem1 >= 29
	T6t3_a1b1_mem1 += INPUT_mem_r

	T0t10_mem0 = S.Task('T0t10_mem0', length=1, delay_cost=1)
	S += T0t10_mem0 >= 30
	T0t10_mem0 += INPUT_mem_r

	T0t10_mem1 = S.Task('T0t10_mem1', length=1, delay_cost=1)
	S += T0t10_mem1 >= 30
	T0t10_mem1 += INPUT_mem_r

	T4t6_a0a1_mem0 = S.Task('T4t6_a0a1_mem0', length=1, delay_cost=1)
	S += T4t6_a0a1_mem0 >= 30
	T4t6_a0a1_mem0 += MUL_mem[0]

	T4t6_a0a1_mem1 = S.Task('T4t6_a0a1_mem1', length=1, delay_cost=1)
	S += T4t6_a0a1_mem1 >= 30
	T4t6_a0a1_mem1 += MUL_mem[0]

	T6c0_a0b0 = S.Task('T6c0_a0b0', length=1, delay_cost=1)
	S += T6c0_a0b0 >= 30
	T6c0_a0b0 += ADD[1]

	T6t3_a1b1 = S.Task('T6t3_a1b1', length=1, delay_cost=1)
	S += T6t3_a1b1 >= 30
	T6t3_a1b1 += ADD[0]

	T0t10 = S.Task('T0t10', length=1, delay_cost=1)
	S += T0t10 >= 31
	T0t10 += ADD[0]

	T0t3_t0t1_mem0 = S.Task('T0t3_t0t1_mem0', length=1, delay_cost=1)
	S += T0t3_t0t1_mem0 >= 31
	T0t3_t0t1_mem0 += ADD_mem[0]

	T0t3_t0t1_mem1 = S.Task('T0t3_t0t1_mem1', length=1, delay_cost=1)
	S += T0t3_t0t1_mem1 >= 31
	T0t3_t0t1_mem1 += ADD_mem[0]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 31
	T111_mem0 += INPUT_mem_r

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 31
	T111_mem1 += INPUT_mem_r

	T4t6_a0a1 = S.Task('T4t6_a0a1', length=1, delay_cost=1)
	S += T4t6_a0a1 >= 31
	T4t6_a0a1 += ADD[1]

	T5c0_a1b1_mem0 = S.Task('T5c0_a1b1_mem0', length=1, delay_cost=1)
	S += T5c0_a1b1_mem0 >= 31
	T5c0_a1b1_mem0 += MUL_mem[0]

	T5c0_a1b1_mem1 = S.Task('T5c0_a1b1_mem1', length=1, delay_cost=1)
	S += T5c0_a1b1_mem1 >= 31
	T5c0_a1b1_mem1 += MUL_mem[0]

	T0t3_t0t1 = S.Task('T0t3_t0t1', length=1, delay_cost=1)
	S += T0t3_t0t1 >= 32
	T0t3_t0t1 += ADD[2]

	T111 = S.Task('T111', length=1, delay_cost=1)
	S += T111 >= 32
	T111 += ADD[0]

	T5c0_a1b1 = S.Task('T5c0_a1b1', length=1, delay_cost=1)
	S += T5c0_a1b1 >= 32
	T5c0_a1b1 += ADD[1]

	T7t2_a1b1_mem0 = S.Task('T7t2_a1b1_mem0', length=1, delay_cost=1)
	S += T7t2_a1b1_mem0 >= 32
	T7t2_a1b1_mem0 += INPUT_mem_r

	T7t2_a1b1_mem1 = S.Task('T7t2_a1b1_mem1', length=1, delay_cost=1)
	S += T7t2_a1b1_mem1 >= 32
	T7t2_a1b1_mem1 += INPUT_mem_r

	T7t2_0_mem0 = S.Task('T7t2_0_mem0', length=1, delay_cost=1)
	S += T7t2_0_mem0 >= 33
	T7t2_0_mem0 += INPUT_mem_r

	T7t2_0_mem1 = S.Task('T7t2_0_mem1', length=1, delay_cost=1)
	S += T7t2_0_mem1 >= 33
	T7t2_0_mem1 += INPUT_mem_r

	T7t2_a1b1 = S.Task('T7t2_a1b1', length=1, delay_cost=1)
	S += T7t2_a1b1 >= 33
	T7t2_a1b1 += ADD[2]

	T6t3_1_mem0 = S.Task('T6t3_1_mem0', length=1, delay_cost=1)
	S += T6t3_1_mem0 >= 34
	T6t3_1_mem0 += INPUT_mem_r

	T6t3_1_mem1 = S.Task('T6t3_1_mem1', length=1, delay_cost=1)
	S += T6t3_1_mem1 >= 34
	T6t3_1_mem1 += INPUT_mem_r

	T7t2_0 = S.Task('T7t2_0', length=1, delay_cost=1)
	S += T7t2_0 >= 34
	T7t2_0 += ADD[0]

	T7t2_t2t3_mem0 = S.Task('T7t2_t2t3_mem0', length=1, delay_cost=1)
	S += T7t2_t2t3_mem0 >= 34
	T7t2_t2t3_mem0 += ADD_mem[0]

	T7t2_t2t3_mem1 = S.Task('T7t2_t2t3_mem1', length=1, delay_cost=1)
	S += T7t2_t2t3_mem1 >= 34
	T7t2_t2t3_mem1 += ADD_mem[0]

	T3t2_0_mem0 = S.Task('T3t2_0_mem0', length=1, delay_cost=1)
	S += T3t2_0_mem0 >= 35
	T3t2_0_mem0 += INPUT_mem_r

	T3t2_0_mem1 = S.Task('T3t2_0_mem1', length=1, delay_cost=1)
	S += T3t2_0_mem1 >= 35
	T3t2_0_mem1 += INPUT_mem_r

	T6t3_1 = S.Task('T6t3_1', length=1, delay_cost=1)
	S += T6t3_1 >= 35
	T6t3_1 += ADD[1]

	T7t2_t2t3 = S.Task('T7t2_t2t3', length=1, delay_cost=1)
	S += T7t2_t2t3 >= 35
	T7t2_t2t3 += ADD[0]

	T3t2_0 = S.Task('T3t2_0', length=1, delay_cost=1)
	S += T3t2_0 >= 36
	T3t2_0 += ADD[3]

	T7t0_t2t3_in = S.Task('T7t0_t2t3_in', length=1, delay_cost=1)
	S += T7t0_t2t3_in >= 36
	T7t0_t2t3_in += MUL_in[0]

	T7t0_t2t3_mem0 = S.Task('T7t0_t2t3_mem0', length=1, delay_cost=1)
	S += T7t0_t2t3_mem0 >= 36
	T7t0_t2t3_mem0 += ADD_mem[0]

	T7t0_t2t3_mem1 = S.Task('T7t0_t2t3_mem1', length=1, delay_cost=1)
	S += T7t0_t2t3_mem1 >= 36
	T7t0_t2t3_mem1 += ADD_mem[3]

	T7t2_a0b0_mem0 = S.Task('T7t2_a0b0_mem0', length=1, delay_cost=1)
	S += T7t2_a0b0_mem0 >= 36
	T7t2_a0b0_mem0 += INPUT_mem_r

	T7t2_a0b0_mem1 = S.Task('T7t2_a0b0_mem1', length=1, delay_cost=1)
	S += T7t2_a0b0_mem1 >= 36
	T7t2_a0b0_mem1 += INPUT_mem_r

	T3t2_t2t3_mem0 = S.Task('T3t2_t2t3_mem0', length=1, delay_cost=1)
	S += T3t2_t2t3_mem0 >= 37
	T3t2_t2t3_mem0 += ADD_mem[3]

	T3t2_t2t3_mem1 = S.Task('T3t2_t2t3_mem1', length=1, delay_cost=1)
	S += T3t2_t2t3_mem1 >= 37
	T3t2_t2t3_mem1 += ADD_mem[3]

	T6t3_0_mem0 = S.Task('T6t3_0_mem0', length=1, delay_cost=1)
	S += T6t3_0_mem0 >= 37
	T6t3_0_mem0 += INPUT_mem_r

	T6t3_0_mem1 = S.Task('T6t3_0_mem1', length=1, delay_cost=1)
	S += T6t3_0_mem1 >= 37
	T6t3_0_mem1 += INPUT_mem_r

	T7t0_t2t3 = S.Task('T7t0_t2t3', length=7, delay_cost=1)
	S += T7t0_t2t3 >= 37
	T7t0_t2t3 += MUL[0]

	T7t2_a0b0 = S.Task('T7t2_a0b0', length=1, delay_cost=1)
	S += T7t2_a0b0 >= 37
	T7t2_a0b0 += ADD[0]

	T3t2_t2t3 = S.Task('T3t2_t2t3', length=1, delay_cost=1)
	S += T3t2_t2t3 >= 38
	T3t2_t2t3 += ADD[2]

	T5t3_a1b1_mem0 = S.Task('T5t3_a1b1_mem0', length=1, delay_cost=1)
	S += T5t3_a1b1_mem0 >= 38
	T5t3_a1b1_mem0 += INPUT_mem_r

	T5t3_a1b1_mem1 = S.Task('T5t3_a1b1_mem1', length=1, delay_cost=1)
	S += T5t3_a1b1_mem1 >= 38
	T5t3_a1b1_mem1 += INPUT_mem_r

	T6t3_0 = S.Task('T6t3_0', length=1, delay_cost=1)
	S += T6t3_0 >= 38
	T6t3_0 += ADD[0]

	T6t3_t2t3_mem0 = S.Task('T6t3_t2t3_mem0', length=1, delay_cost=1)
	S += T6t3_t2t3_mem0 >= 38
	T6t3_t2t3_mem0 += ADD_mem[0]

	T6t3_t2t3_mem1 = S.Task('T6t3_t2t3_mem1', length=1, delay_cost=1)
	S += T6t3_t2t3_mem1 >= 38
	T6t3_t2t3_mem1 += ADD_mem[1]

	T5t3_a0b0_mem0 = S.Task('T5t3_a0b0_mem0', length=1, delay_cost=1)
	S += T5t3_a0b0_mem0 >= 39
	T5t3_a0b0_mem0 += INPUT_mem_r

	T5t3_a0b0_mem1 = S.Task('T5t3_a0b0_mem1', length=1, delay_cost=1)
	S += T5t3_a0b0_mem1 >= 39
	T5t3_a0b0_mem1 += INPUT_mem_r

	T5t3_a1b1 = S.Task('T5t3_a1b1', length=1, delay_cost=1)
	S += T5t3_a1b1 >= 39
	T5t3_a1b1 += ADD[0]

	T6t3_t2t3 = S.Task('T6t3_t2t3', length=1, delay_cost=1)
	S += T6t3_t2t3 >= 39
	T6t3_t2t3 += ADD[1]

	T5t3_1_mem0 = S.Task('T5t3_1_mem0', length=1, delay_cost=1)
	S += T5t3_1_mem0 >= 40
	T5t3_1_mem0 += INPUT_mem_r

	T5t3_1_mem1 = S.Task('T5t3_1_mem1', length=1, delay_cost=1)
	S += T5t3_1_mem1 >= 40
	T5t3_1_mem1 += INPUT_mem_r

	T5t3_a0b0 = S.Task('T5t3_a0b0', length=1, delay_cost=1)
	S += T5t3_a0b0 >= 40
	T5t3_a0b0 += ADD[0]

	T5t4_a0b0_in = S.Task('T5t4_a0b0_in', length=1, delay_cost=1)
	S += T5t4_a0b0_in >= 40
	T5t4_a0b0_in += MUL_in[0]

	T5t4_a0b0_mem0 = S.Task('T5t4_a0b0_mem0', length=1, delay_cost=1)
	S += T5t4_a0b0_mem0 >= 40
	T5t4_a0b0_mem0 += ADD_mem[0]

	T5t4_a0b0_mem1 = S.Task('T5t4_a0b0_mem1', length=1, delay_cost=1)
	S += T5t4_a0b0_mem1 >= 40
	T5t4_a0b0_mem1 += ADD_mem[0]

	T5t1_t2t3_in = S.Task('T5t1_t2t3_in', length=1, delay_cost=1)
	S += T5t1_t2t3_in >= 41
	T5t1_t2t3_in += MUL_in[0]

	T5t1_t2t3_mem0 = S.Task('T5t1_t2t3_mem0', length=1, delay_cost=1)
	S += T5t1_t2t3_mem0 >= 41
	T5t1_t2t3_mem0 += ADD_mem[0]

	T5t1_t2t3_mem1 = S.Task('T5t1_t2t3_mem1', length=1, delay_cost=1)
	S += T5t1_t2t3_mem1 >= 41
	T5t1_t2t3_mem1 += ADD_mem[0]

	T5t3_0_mem0 = S.Task('T5t3_0_mem0', length=1, delay_cost=1)
	S += T5t3_0_mem0 >= 41
	T5t3_0_mem0 += INPUT_mem_r

	T5t3_0_mem1 = S.Task('T5t3_0_mem1', length=1, delay_cost=1)
	S += T5t3_0_mem1 >= 41
	T5t3_0_mem1 += INPUT_mem_r

	T5t3_1 = S.Task('T5t3_1', length=1, delay_cost=1)
	S += T5t3_1 >= 41
	T5t3_1 += ADD[0]

	T5t4_a0b0 = S.Task('T5t4_a0b0', length=7, delay_cost=1)
	S += T5t4_a0b0 >= 41
	T5t4_a0b0 += MUL[0]

	T4a10_new_mem0 = S.Task('T4a10_new_mem0', length=1, delay_cost=1)
	S += T4a10_new_mem0 >= 42
	T4a10_new_mem0 += INPUT_mem_r

	T4a10_new_mem1 = S.Task('T4a10_new_mem1', length=1, delay_cost=1)
	S += T4a10_new_mem1 >= 42
	T4a10_new_mem1 += INPUT_mem_r

	T5t0_t2t3_in = S.Task('T5t0_t2t3_in', length=1, delay_cost=1)
	S += T5t0_t2t3_in >= 42
	T5t0_t2t3_in += MUL_in[0]

	T5t0_t2t3_mem0 = S.Task('T5t0_t2t3_mem0', length=1, delay_cost=1)
	S += T5t0_t2t3_mem0 >= 42
	T5t0_t2t3_mem0 += ADD_mem[0]

	T5t0_t2t3_mem1 = S.Task('T5t0_t2t3_mem1', length=1, delay_cost=1)
	S += T5t0_t2t3_mem1 >= 42
	T5t0_t2t3_mem1 += ADD_mem[0]

	T5t1_t2t3 = S.Task('T5t1_t2t3', length=7, delay_cost=1)
	S += T5t1_t2t3 >= 42
	T5t1_t2t3 += MUL[0]

	T5t3_0 = S.Task('T5t3_0', length=1, delay_cost=1)
	S += T5t3_0 >= 42
	T5t3_0 += ADD[0]

	T3t3_a1b1_mem0 = S.Task('T3t3_a1b1_mem0', length=1, delay_cost=1)
	S += T3t3_a1b1_mem0 >= 43
	T3t3_a1b1_mem0 += INPUT_mem_r

	T3t3_a1b1_mem1 = S.Task('T3t3_a1b1_mem1', length=1, delay_cost=1)
	S += T3t3_a1b1_mem1 >= 43
	T3t3_a1b1_mem1 += INPUT_mem_r

	T4a10_new = S.Task('T4a10_new', length=1, delay_cost=1)
	S += T4a10_new >= 43
	T4a10_new += ADD[0]

	T5t0_t2t3 = S.Task('T5t0_t2t3', length=7, delay_cost=1)
	S += T5t0_t2t3 >= 43
	T5t0_t2t3 += MUL[0]

	T5t3_t2t3_mem0 = S.Task('T5t3_t2t3_mem0', length=1, delay_cost=1)
	S += T5t3_t2t3_mem0 >= 43
	T5t3_t2t3_mem0 += ADD_mem[0]

	T5t3_t2t3_mem1 = S.Task('T5t3_t2t3_mem1', length=1, delay_cost=1)
	S += T5t3_t2t3_mem1 >= 43
	T5t3_t2t3_mem1 += ADD_mem[0]

	T3t2_a1b1_mem0 = S.Task('T3t2_a1b1_mem0', length=1, delay_cost=1)
	S += T3t2_a1b1_mem0 >= 44
	T3t2_a1b1_mem0 += INPUT_mem_r

	T3t2_a1b1_mem1 = S.Task('T3t2_a1b1_mem1', length=1, delay_cost=1)
	S += T3t2_a1b1_mem1 >= 44
	T3t2_a1b1_mem1 += INPUT_mem_r

	T3t3_a1b1 = S.Task('T3t3_a1b1', length=1, delay_cost=1)
	S += T3t3_a1b1 >= 44
	T3t3_a1b1 += ADD[0]

	T5t3_t2t3 = S.Task('T5t3_t2t3', length=1, delay_cost=1)
	S += T5t3_t2t3 >= 44
	T5t3_t2t3 += ADD[2]

	T6t4_a1b1_in = S.Task('T6t4_a1b1_in', length=1, delay_cost=1)
	S += T6t4_a1b1_in >= 44
	T6t4_a1b1_in += MUL_in[0]

	T6t4_a1b1_mem0 = S.Task('T6t4_a1b1_mem0', length=1, delay_cost=1)
	S += T6t4_a1b1_mem0 >= 44
	T6t4_a1b1_mem0 += ADD_mem[0]

	T6t4_a1b1_mem1 = S.Task('T6t4_a1b1_mem1', length=1, delay_cost=1)
	S += T6t4_a1b1_mem1 >= 44
	T6t4_a1b1_mem1 += ADD_mem[0]

	T0a11_new_mem0 = S.Task('T0a11_new_mem0', length=1, delay_cost=1)
	S += T0a11_new_mem0 >= 45
	T0a11_new_mem0 += INPUT_mem_r

	T0a11_new_mem1 = S.Task('T0a11_new_mem1', length=1, delay_cost=1)
	S += T0a11_new_mem1 >= 45
	T0a11_new_mem1 += INPUT_mem_r

	T3t2_a1b1 = S.Task('T3t2_a1b1', length=1, delay_cost=1)
	S += T3t2_a1b1 >= 45
	T3t2_a1b1 += ADD[0]

	T3t4_a1b1_in = S.Task('T3t4_a1b1_in', length=1, delay_cost=1)
	S += T3t4_a1b1_in >= 45
	T3t4_a1b1_in += MUL_in[0]

	T3t4_a1b1_mem0 = S.Task('T3t4_a1b1_mem0', length=1, delay_cost=1)
	S += T3t4_a1b1_mem0 >= 45
	T3t4_a1b1_mem0 += ADD_mem[0]

	T3t4_a1b1_mem1 = S.Task('T3t4_a1b1_mem1', length=1, delay_cost=1)
	S += T3t4_a1b1_mem1 >= 45
	T3t4_a1b1_mem1 += ADD_mem[0]

	T6t4_a1b1 = S.Task('T6t4_a1b1', length=7, delay_cost=1)
	S += T6t4_a1b1 >= 45
	T6t4_a1b1 += MUL[0]

	T0a11_new = S.Task('T0a11_new', length=1, delay_cost=1)
	S += T0a11_new >= 46
	T0a11_new += ADD[0]

	T3t3_a0b0_mem0 = S.Task('T3t3_a0b0_mem0', length=1, delay_cost=1)
	S += T3t3_a0b0_mem0 >= 46
	T3t3_a0b0_mem0 += INPUT_mem_r

	T3t3_a0b0_mem1 = S.Task('T3t3_a0b0_mem1', length=1, delay_cost=1)
	S += T3t3_a0b0_mem1 >= 46
	T3t3_a0b0_mem1 += INPUT_mem_r

	T3t4_a1b1 = S.Task('T3t4_a1b1', length=7, delay_cost=1)
	S += T3t4_a1b1 >= 46
	T3t4_a1b1 += MUL[0]

	T5t4_a1b1_in = S.Task('T5t4_a1b1_in', length=1, delay_cost=1)
	S += T5t4_a1b1_in >= 46
	T5t4_a1b1_in += MUL_in[0]

	T5t4_a1b1_mem0 = S.Task('T5t4_a1b1_mem0', length=1, delay_cost=1)
	S += T5t4_a1b1_mem0 >= 46
	T5t4_a1b1_mem0 += ADD_mem[0]

	T5t4_a1b1_mem1 = S.Task('T5t4_a1b1_mem1', length=1, delay_cost=1)
	S += T5t4_a1b1_mem1 >= 46
	T5t4_a1b1_mem1 += ADD_mem[0]

	T0t4_a0a1_in = S.Task('T0t4_a0a1_in', length=1, delay_cost=1)
	S += T0t4_a0a1_in >= 47
	T0t4_a0a1_in += MUL_in[0]

	T0t4_a0a1_mem0 = S.Task('T0t4_a0a1_mem0', length=1, delay_cost=1)
	S += T0t4_a0a1_mem0 >= 47
	T0t4_a0a1_mem0 += ADD_mem[0]

	T0t4_a0a1_mem1 = S.Task('T0t4_a0a1_mem1', length=1, delay_cost=1)
	S += T0t4_a0a1_mem1 >= 47
	T0t4_a0a1_mem1 += ADD_mem[0]

	T3t2_a0b0_mem0 = S.Task('T3t2_a0b0_mem0', length=1, delay_cost=1)
	S += T3t2_a0b0_mem0 >= 47
	T3t2_a0b0_mem0 += INPUT_mem_r

	T3t2_a0b0_mem1 = S.Task('T3t2_a0b0_mem1', length=1, delay_cost=1)
	S += T3t2_a0b0_mem1 >= 47
	T3t2_a0b0_mem1 += INPUT_mem_r

	T3t3_a0b0 = S.Task('T3t3_a0b0', length=1, delay_cost=1)
	S += T3t3_a0b0 >= 47
	T3t3_a0b0 += ADD[3]

	T5t4_a1b1 = S.Task('T5t4_a1b1', length=7, delay_cost=1)
	S += T5t4_a1b1 >= 47
	T5t4_a1b1 += MUL[0]

	T0t4_a0a1 = S.Task('T0t4_a0a1', length=7, delay_cost=1)
	S += T0t4_a0a1 >= 48
	T0t4_a0a1 += MUL[0]

	T3t2_a0b0 = S.Task('T3t2_a0b0', length=1, delay_cost=1)
	S += T3t2_a0b0 >= 48
	T3t2_a0b0 += ADD[0]

	T3t3_1_mem0 = S.Task('T3t3_1_mem0', length=1, delay_cost=1)
	S += T3t3_1_mem0 >= 48
	T3t3_1_mem0 += INPUT_mem_r

	T3t3_1_mem1 = S.Task('T3t3_1_mem1', length=1, delay_cost=1)
	S += T3t3_1_mem1 >= 48
	T3t3_1_mem1 += INPUT_mem_r

	T4t4_a0a1_in = S.Task('T4t4_a0a1_in', length=1, delay_cost=1)
	S += T4t4_a0a1_in >= 48
	T4t4_a0a1_in += MUL_in[0]

	T4t4_a0a1_mem0 = S.Task('T4t4_a0a1_mem0', length=1, delay_cost=1)
	S += T4t4_a0a1_mem0 >= 48
	T4t4_a0a1_mem0 += ADD_mem[0]

	T4t4_a0a1_mem1 = S.Task('T4t4_a0a1_mem1', length=1, delay_cost=1)
	S += T4t4_a0a1_mem1 >= 48
	T4t4_a0a1_mem1 += ADD_mem[0]

	T3t3_0_mem0 = S.Task('T3t3_0_mem0', length=1, delay_cost=1)
	S += T3t3_0_mem0 >= 49
	T3t3_0_mem0 += INPUT_mem_r

	T3t3_0_mem1 = S.Task('T3t3_0_mem1', length=1, delay_cost=1)
	S += T3t3_0_mem1 >= 49
	T3t3_0_mem1 += INPUT_mem_r

	T3t3_1 = S.Task('T3t3_1', length=1, delay_cost=1)
	S += T3t3_1 >= 49
	T3t3_1 += ADD[0]

	T4t4_a0a1 = S.Task('T4t4_a0a1', length=7, delay_cost=1)
	S += T4t4_a0a1 >= 49
	T4t4_a0a1 += MUL[0]

	T7t4_a0b0_in = S.Task('T7t4_a0b0_in', length=1, delay_cost=1)
	S += T7t4_a0b0_in >= 49
	T7t4_a0b0_in += MUL_in[0]

	T7t4_a0b0_mem0 = S.Task('T7t4_a0b0_mem0', length=1, delay_cost=1)
	S += T7t4_a0b0_mem0 >= 49
	T7t4_a0b0_mem0 += ADD_mem[0]

	T7t4_a0b0_mem1 = S.Task('T7t4_a0b0_mem1', length=1, delay_cost=1)
	S += T7t4_a0b0_mem1 >= 49
	T7t4_a0b0_mem1 += ADD_mem[0]

	T0t01_mem0 = S.Task('T0t01_mem0', length=1, delay_cost=1)
	S += T0t01_mem0 >= 50
	T0t01_mem0 += ADD_mem[0]

	T0t01_mem1 = S.Task('T0t01_mem1', length=1, delay_cost=1)
	S += T0t01_mem1 >= 50
	T0t01_mem1 += INPUT_mem_r

	T1100_mem0 = S.Task('T1100_mem0', length=1, delay_cost=1)
	S += T1100_mem0 >= 50
	T1100_mem0 += ADD_mem[0]

	T1100_mem1 = S.Task('T1100_mem1', length=1, delay_cost=1)
	S += T1100_mem1 >= 50
	T1100_mem1 += INPUT_mem_r

	T3t0_t2t3_in = S.Task('T3t0_t2t3_in', length=1, delay_cost=1)
	S += T3t0_t2t3_in >= 50
	T3t0_t2t3_in += MUL_in[0]

	T3t0_t2t3_mem0 = S.Task('T3t0_t2t3_mem0', length=1, delay_cost=1)
	S += T3t0_t2t3_mem0 >= 50
	T3t0_t2t3_mem0 += ADD_mem[3]

	T3t0_t2t3_mem1 = S.Task('T3t0_t2t3_mem1', length=1, delay_cost=1)
	S += T3t0_t2t3_mem1 >= 50
	T3t0_t2t3_mem1 += ADD_mem[3]

	T3t3_0 = S.Task('T3t3_0', length=1, delay_cost=1)
	S += T3t3_0 >= 50
	T3t3_0 += ADD[3]

	T7t4_a0b0 = S.Task('T7t4_a0b0', length=7, delay_cost=1)
	S += T7t4_a0b0 >= 50
	T7t4_a0b0 += MUL[0]

	T0t01 = S.Task('T0t01', length=1, delay_cost=1)
	S += T0t01 >= 51
	T0t01 += ADD[0]

	T1100 = S.Task('T1100', length=1, delay_cost=1)
	S += T1100 >= 51
	T1100 += ADD[1]

	T3t0_t2t3 = S.Task('T3t0_t2t3', length=7, delay_cost=1)
	S += T3t0_t2t3 >= 51
	T3t0_t2t3 += MUL[0]

	T3t3_t2t3_mem0 = S.Task('T3t3_t2t3_mem0', length=1, delay_cost=1)
	S += T3t3_t2t3_mem0 >= 51
	T3t3_t2t3_mem0 += ADD_mem[3]

	T3t3_t2t3_mem1 = S.Task('T3t3_t2t3_mem1', length=1, delay_cost=1)
	S += T3t3_t2t3_mem1 >= 51
	T3t3_t2t3_mem1 += ADD_mem[0]

	T7t4_a1b1_in = S.Task('T7t4_a1b1_in', length=1, delay_cost=1)
	S += T7t4_a1b1_in >= 51
	T7t4_a1b1_in += MUL_in[0]

	T7t4_a1b1_mem0 = S.Task('T7t4_a1b1_mem0', length=1, delay_cost=1)
	S += T7t4_a1b1_mem0 >= 51
	T7t4_a1b1_mem0 += ADD_mem[2]

	T7t4_a1b1_mem1 = S.Task('T7t4_a1b1_mem1', length=1, delay_cost=1)
	S += T7t4_a1b1_mem1 >= 51
	T7t4_a1b1_mem1 += ADD_mem[0]

	T1111_mem0 = S.Task('T1111_mem0', length=1, delay_cost=1)
	S += T1111_mem0 >= 52
	T1111_mem0 += ADD_mem[0]

	T1111_mem1 = S.Task('T1111_mem1', length=1, delay_cost=1)
	S += T1111_mem1 >= 52
	T1111_mem1 += INPUT_mem_r

	T3t1_t2t3_in = S.Task('T3t1_t2t3_in', length=1, delay_cost=1)
	S += T3t1_t2t3_in >= 52
	T3t1_t2t3_in += MUL_in[0]

	T3t1_t2t3_mem0 = S.Task('T3t1_t2t3_mem0', length=1, delay_cost=1)
	S += T3t1_t2t3_mem0 >= 52
	T3t1_t2t3_mem0 += ADD_mem[3]

	T3t1_t2t3_mem1 = S.Task('T3t1_t2t3_mem1', length=1, delay_cost=1)
	S += T3t1_t2t3_mem1 >= 52
	T3t1_t2t3_mem1 += ADD_mem[0]

	T3t3_t2t3 = S.Task('T3t3_t2t3', length=1, delay_cost=1)
	S += T3t3_t2t3 >= 52
	T3t3_t2t3 += ADD[0]

	T7t4_a1b1 = S.Task('T7t4_a1b1', length=7, delay_cost=1)
	S += T7t4_a1b1 >= 52
	T7t4_a1b1 += MUL[0]

	T1111 = S.Task('T1111', length=1, delay_cost=1)
	S += T1111 >= 53
	T1111 += ADD[1]

	T3t1_t2t3 = S.Task('T3t1_t2t3', length=7, delay_cost=1)
	S += T3t1_t2t3 >= 53
	T3t1_t2t3 += MUL[0]

	T4t01_mem0 = S.Task('T4t01_mem0', length=1, delay_cost=1)
	S += T4t01_mem0 >= 53
	T4t01_mem0 += ADD_mem[0]

	T4t01_mem1 = S.Task('T4t01_mem1', length=1, delay_cost=1)
	S += T4t01_mem1 >= 53
	T4t01_mem1 += INPUT_mem_r

	T6t0_t2t3_in = S.Task('T6t0_t2t3_in', length=1, delay_cost=1)
	S += T6t0_t2t3_in >= 53
	T6t0_t2t3_in += MUL_in[0]

	T6t0_t2t3_mem0 = S.Task('T6t0_t2t3_mem0', length=1, delay_cost=1)
	S += T6t0_t2t3_mem0 >= 53
	T6t0_t2t3_mem0 += ADD_mem[3]

	T6t0_t2t3_mem1 = S.Task('T6t0_t2t3_mem1', length=1, delay_cost=1)
	S += T6t0_t2t3_mem1 >= 53
	T6t0_t2t3_mem1 += ADD_mem[0]

	T0t00_mem0 = S.Task('T0t00_mem0', length=1, delay_cost=1)
	S += T0t00_mem0 >= 54
	T0t00_mem0 += ADD_mem[0]

	T0t00_mem1 = S.Task('T0t00_mem1', length=1, delay_cost=1)
	S += T0t00_mem1 >= 54
	T0t00_mem1 += INPUT_mem_r

	T4t01 = S.Task('T4t01', length=1, delay_cost=1)
	S += T4t01 >= 54
	T4t01 += ADD[1]

	T6t0_t2t3 = S.Task('T6t0_t2t3', length=7, delay_cost=1)
	S += T6t0_t2t3 >= 54
	T6t0_t2t3 += MUL[0]

	T6t4_a0b0_in = S.Task('T6t4_a0b0_in', length=1, delay_cost=1)
	S += T6t4_a0b0_in >= 54
	T6t4_a0b0_in += MUL_in[0]

	T6t4_a0b0_mem0 = S.Task('T6t4_a0b0_mem0', length=1, delay_cost=1)
	S += T6t4_a0b0_mem0 >= 54
	T6t4_a0b0_mem0 += ADD_mem[3]

	T6t4_a0b0_mem1 = S.Task('T6t4_a0b0_mem1', length=1, delay_cost=1)
	S += T6t4_a0b0_mem1 >= 54
	T6t4_a0b0_mem1 += ADD_mem[0]

	T0t00 = S.Task('T0t00', length=1, delay_cost=1)
	S += T0t00 >= 55
	T0t00 += ADD[1]

	T3t4_a0b0_in = S.Task('T3t4_a0b0_in', length=1, delay_cost=1)
	S += T3t4_a0b0_in >= 55
	T3t4_a0b0_in += MUL_in[0]

	T3t4_a0b0_mem0 = S.Task('T3t4_a0b0_mem0', length=1, delay_cost=1)
	S += T3t4_a0b0_mem0 >= 55
	T3t4_a0b0_mem0 += ADD_mem[0]

	T3t4_a0b0_mem1 = S.Task('T3t4_a0b0_mem1', length=1, delay_cost=1)
	S += T3t4_a0b0_mem1 >= 55
	T3t4_a0b0_mem1 += ADD_mem[3]

	T4t00_mem0 = S.Task('T4t00_mem0', length=1, delay_cost=1)
	S += T4t00_mem0 >= 55
	T4t00_mem0 += ADD_mem[0]

	T4t00_mem1 = S.Task('T4t00_mem1', length=1, delay_cost=1)
	S += T4t00_mem1 >= 55
	T4t00_mem1 += INPUT_mem_r

	T6t4_a0b0 = S.Task('T6t4_a0b0', length=7, delay_cost=1)
	S += T6t4_a0b0 >= 55
	T6t4_a0b0 += MUL[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 56
	T210_mem0 += ADD_mem[0]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 56
	T210_mem1 += INPUT_mem_r

	T3t4_a0b0 = S.Task('T3t4_a0b0', length=7, delay_cost=1)
	S += T3t4_a0b0 >= 56
	T3t4_a0b0 += MUL[0]

	T4t00 = S.Task('T4t00', length=1, delay_cost=1)
	S += T4t00 >= 56
	T4t00 += ADD[1]

	T6t1_t2t3_in = S.Task('T6t1_t2t3_in', length=1, delay_cost=1)
	S += T6t1_t2t3_in >= 56
	T6t1_t2t3_in += MUL_in[0]

	T6t1_t2t3_mem0 = S.Task('T6t1_t2t3_mem0', length=1, delay_cost=1)
	S += T6t1_t2t3_mem0 >= 56
	T6t1_t2t3_mem0 += ADD_mem[0]

	T6t1_t2t3_mem1 = S.Task('T6t1_t2t3_mem1', length=1, delay_cost=1)
	S += T6t1_t2t3_mem1 >= 56
	T6t1_t2t3_mem1 += ADD_mem[1]

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	S += T201_mem0 >= 57
	T201_mem0 += ADD_mem[0]

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	S += T201_mem1 >= 57
	T201_mem1 += INPUT_mem_r

	T210 = S.Task('T210', length=1, delay_cost=1)
	S += T210 >= 57
	T210 += ADD[0]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 57
	T211_mem0 += ADD_mem[0]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 57
	T211_mem1 += INPUT_mem_r

	T6t1_t2t3 = S.Task('T6t1_t2t3', length=7, delay_cost=1)
	S += T6t1_t2t3 >= 57
	T6t1_t2t3 += MUL[0]

	T1101_mem0 = S.Task('T1101_mem0', length=1, delay_cost=1)
	S += T1101_mem0 >= 58
	T1101_mem0 += ADD_mem[0]

	T1101_mem1 = S.Task('T1101_mem1', length=1, delay_cost=1)
	S += T1101_mem1 >= 58
	T1101_mem1 += INPUT_mem_r

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	S += T200_mem0 >= 58
	T200_mem0 += ADD_mem[0]

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	S += T200_mem1 >= 58
	T200_mem1 += INPUT_mem_r

	T201 = S.Task('T201', length=1, delay_cost=1)
	S += T201 >= 58
	T201 += ADD[1]

	T211 = S.Task('T211', length=1, delay_cost=1)
	S += T211 >= 58
	T211 += ADD[3]

	T1101 = S.Task('T1101', length=1, delay_cost=1)
	S += T1101 >= 59
	T1101 += ADD[2]

	T1110_mem0 = S.Task('T1110_mem0', length=1, delay_cost=1)
	S += T1110_mem0 >= 59
	T1110_mem0 += ADD_mem[0]

	T1110_mem1 = S.Task('T1110_mem1', length=1, delay_cost=1)
	S += T1110_mem1 >= 59
	T1110_mem1 += INPUT_mem_r

	T200 = S.Task('T200', length=1, delay_cost=1)
	S += T200 >= 59
	T200 += ADD[0]

	T1110 = S.Task('T1110', length=1, delay_cost=1)
	S += T1110 >= 60
	T1110 += ADD[3]



	# new tasks
	T0t0_t0t1_in = S.Task('T0t0_t0t1_in', length=1, delay_cost=1)
	T0t0_t0t1_in += alt(MUL_in)
	T0t0_t0t1 = S.Task('T0t0_t0t1', length=7, delay_cost=1)
	T0t0_t0t1 += alt(MUL)
	S+=T0t0_t0t1>=T0t0_t0t1_in

	T0t1_t0t1_in = S.Task('T0t1_t0t1_in', length=1, delay_cost=1)
	T0t1_t0t1_in += alt(MUL_in)
	T0t1_t0t1 = S.Task('T0t1_t0t1', length=7, delay_cost=1)
	T0t1_t0t1 += alt(MUL)
	S+=T0t1_t0t1>=T0t1_t0t1_in

	T0t2_t0t1 = S.Task('T0t2_t0t1', length=1, delay_cost=1)
	T0t2_t0t1 += alt(ADD)

	T0c1_a0a1 = S.Task('T0c1_a0a1', length=1, delay_cost=1)
	T0c1_a0a1 += alt(ADD)

	T010 = S.Task('T010', length=1, delay_cost=1)
	T010 += alt(ADD)

	T12a10_new = S.Task('T12a10_new', length=1, delay_cost=1)
	T12a10_new += alt(ADD)

	T12a11_new = S.Task('T12a11_new', length=1, delay_cost=1)
	T12a11_new += alt(ADD)

	T12t10 = S.Task('T12t10', length=1, delay_cost=1)
	T12t10 += alt(ADD)

	T12t11 = S.Task('T12t11', length=1, delay_cost=1)
	T12t11 += alt(ADD)

	T12t0_a0a1_in = S.Task('T12t0_a0a1_in', length=1, delay_cost=1)
	T12t0_a0a1_in += alt(MUL_in)
	T12t0_a0a1 = S.Task('T12t0_a0a1', length=7, delay_cost=1)
	T12t0_a0a1 += alt(MUL)
	S+=T12t0_a0a1>=T12t0_a0a1_in

	T12t1_a0a1_in = S.Task('T12t1_a0a1_in', length=1, delay_cost=1)
	T12t1_a0a1_in += alt(MUL_in)
	T12t1_a0a1 = S.Task('T12t1_a0a1', length=7, delay_cost=1)
	T12t1_a0a1 += alt(MUL)
	S+=T12t1_a0a1>=T12t1_a0a1_in

	T12t2_a0a1 = S.Task('T12t2_a0a1', length=1, delay_cost=1)
	T12t2_a0a1 += alt(ADD)

	T21a10_new = S.Task('T21a10_new', length=1, delay_cost=1)
	T21a10_new += alt(ADD)

	T21a11_new = S.Task('T21a11_new', length=1, delay_cost=1)
	T21a11_new += alt(ADD)

	T21t10 = S.Task('T21t10', length=1, delay_cost=1)
	T21t10 += alt(ADD)

	T21t11 = S.Task('T21t11', length=1, delay_cost=1)
	T21t11 += alt(ADD)

	T21t0_a0a1_in = S.Task('T21t0_a0a1_in', length=1, delay_cost=1)
	T21t0_a0a1_in += alt(MUL_in)
	T21t0_a0a1 = S.Task('T21t0_a0a1', length=7, delay_cost=1)
	T21t0_a0a1 += alt(MUL)
	S+=T21t0_a0a1>=T21t0_a0a1_in

	T21t1_a0a1_in = S.Task('T21t1_a0a1_in', length=1, delay_cost=1)
	T21t1_a0a1_in += alt(MUL_in)
	T21t1_a0a1 = S.Task('T21t1_a0a1', length=7, delay_cost=1)
	T21t1_a0a1 += alt(MUL)
	S+=T21t1_a0a1>=T21t1_a0a1_in

	T21t2_a0a1 = S.Task('T21t2_a0a1', length=1, delay_cost=1)
	T21t2_a0a1 += alt(ADD)

	T3c1_a0b0 = S.Task('T3c1_a0b0', length=1, delay_cost=1)
	T3c1_a0b0 += alt(ADD)

	T3c1_a1b1 = S.Task('T3c1_a1b1', length=1, delay_cost=1)
	T3c1_a1b1 += alt(ADD)

	T3t4_t2t3_in = S.Task('T3t4_t2t3_in', length=1, delay_cost=1)
	T3t4_t2t3_in += alt(MUL_in)
	T3t4_t2t3 = S.Task('T3t4_t2t3', length=7, delay_cost=1)
	T3t4_t2t3 += alt(MUL)
	S+=T3t4_t2t3>=T3t4_t2t3_in

	T3c0_t2t3 = S.Task('T3c0_t2t3', length=1, delay_cost=1)
	T3c0_t2t3 += alt(ADD)

	T3t6_t2t3 = S.Task('T3t6_t2t3', length=1, delay_cost=1)
	T3t6_t2t3 += alt(ADD)

	T3t5_0 = S.Task('T3t5_0', length=1, delay_cost=1)
	T3t5_0 += alt(ADD)

	T4t0_t0t1_in = S.Task('T4t0_t0t1_in', length=1, delay_cost=1)
	T4t0_t0t1_in += alt(MUL_in)
	T4t0_t0t1 = S.Task('T4t0_t0t1', length=7, delay_cost=1)
	T4t0_t0t1 += alt(MUL)
	S+=T4t0_t0t1>=T4t0_t0t1_in

	T4t1_t0t1_in = S.Task('T4t1_t0t1_in', length=1, delay_cost=1)
	T4t1_t0t1_in += alt(MUL_in)
	T4t1_t0t1 = S.Task('T4t1_t0t1', length=7, delay_cost=1)
	T4t1_t0t1 += alt(MUL)
	S+=T4t1_t0t1>=T4t1_t0t1_in

	T4t2_t0t1 = S.Task('T4t2_t0t1', length=1, delay_cost=1)
	T4t2_t0t1 += alt(ADD)

	T4c1_a0a1 = S.Task('T4c1_a0a1', length=1, delay_cost=1)
	T4c1_a0a1 += alt(ADD)

	T410 = S.Task('T410', length=1, delay_cost=1)
	T410 += alt(ADD)

	T5c1_a0b0 = S.Task('T5c1_a0b0', length=1, delay_cost=1)
	T5c1_a0b0 += alt(ADD)

	T5c1_a1b1 = S.Task('T5c1_a1b1', length=1, delay_cost=1)
	T5c1_a1b1 += alt(ADD)

	T5t4_t2t3_in = S.Task('T5t4_t2t3_in', length=1, delay_cost=1)
	T5t4_t2t3_in += alt(MUL_in)
	T5t4_t2t3 = S.Task('T5t4_t2t3', length=7, delay_cost=1)
	T5t4_t2t3 += alt(MUL)
	S+=T5t4_t2t3>=T5t4_t2t3_in

	T5c0_t2t3 = S.Task('T5c0_t2t3', length=1, delay_cost=1)
	T5c0_t2t3 += alt(ADD)

	T5t6_t2t3 = S.Task('T5t6_t2t3', length=1, delay_cost=1)
	T5t6_t2t3 += alt(ADD)

	T5t5_0 = S.Task('T5t5_0', length=1, delay_cost=1)
	T5t5_0 += alt(ADD)

	T6c1_a0b0 = S.Task('T6c1_a0b0', length=1, delay_cost=1)
	T6c1_a0b0 += alt(ADD)

	T6c1_a1b1 = S.Task('T6c1_a1b1', length=1, delay_cost=1)
	T6c1_a1b1 += alt(ADD)

	T6t4_t2t3_in = S.Task('T6t4_t2t3_in', length=1, delay_cost=1)
	T6t4_t2t3_in += alt(MUL_in)
	T6t4_t2t3 = S.Task('T6t4_t2t3', length=7, delay_cost=1)
	T6t4_t2t3 += alt(MUL)
	S+=T6t4_t2t3>=T6t4_t2t3_in

	T6c0_t2t3 = S.Task('T6c0_t2t3', length=1, delay_cost=1)
	T6c0_t2t3 += alt(ADD)

	T6t6_t2t3 = S.Task('T6t6_t2t3', length=1, delay_cost=1)
	T6t6_t2t3 += alt(ADD)

	T6t5_0 = S.Task('T6t5_0', length=1, delay_cost=1)
	T6t5_0 += alt(ADD)

	T7c1_a0b0 = S.Task('T7c1_a0b0', length=1, delay_cost=1)
	T7c1_a0b0 += alt(ADD)

	T7c1_a1b1 = S.Task('T7c1_a1b1', length=1, delay_cost=1)
	T7c1_a1b1 += alt(ADD)

	T7t4_t2t3_in = S.Task('T7t4_t2t3_in', length=1, delay_cost=1)
	T7t4_t2t3_in += alt(MUL_in)
	T7t4_t2t3 = S.Task('T7t4_t2t3', length=7, delay_cost=1)
	T7t4_t2t3 += alt(MUL)
	S+=T7t4_t2t3>=T7t4_t2t3_in

	T7c0_t2t3 = S.Task('T7c0_t2t3', length=1, delay_cost=1)
	T7c0_t2t3 += alt(ADD)

	T7t6_t2t3 = S.Task('T7t6_t2t3', length=1, delay_cost=1)
	T7t6_t2t3 += alt(ADD)

	T7t5_0 = S.Task('T7t5_0', length=1, delay_cost=1)
	T7t5_0 += alt(ADD)

	T0t0_t0t1_mem0 = S.Task('T0t0_t0t1_mem0', length=1, delay_cost=1)
	T0t0_t0t1_mem0 += ADD_mem[1]
	S += 55<T0t0_t0t1_mem0
	S += T0t0_t0t1_mem0<=T0t0_t0t1

	T0t0_t0t1_mem1 = S.Task('T0t0_t0t1_mem1', length=1, delay_cost=1)
	T0t0_t0t1_mem1 += ADD_mem[0]
	S += 31<T0t0_t0t1_mem1
	S += T0t0_t0t1_mem1<=T0t0_t0t1

	T0t1_t0t1_mem0 = S.Task('T0t1_t0t1_mem0', length=1, delay_cost=1)
	T0t1_t0t1_mem0 += ADD_mem[0]
	S += 51<T0t1_t0t1_mem0
	S += T0t1_t0t1_mem0<=T0t1_t0t1

	T0t1_t0t1_mem1 = S.Task('T0t1_t0t1_mem1', length=1, delay_cost=1)
	T0t1_t0t1_mem1 += ADD_mem[0]
	S += 28<T0t1_t0t1_mem1
	S += T0t1_t0t1_mem1<=T0t1_t0t1

	T0t2_t0t1_mem0 = S.Task('T0t2_t0t1_mem0', length=1, delay_cost=1)
	T0t2_t0t1_mem0 += ADD_mem[1]
	S += 55<T0t2_t0t1_mem0
	S += T0t2_t0t1_mem0<=T0t2_t0t1

	T0t2_t0t1_mem1 = S.Task('T0t2_t0t1_mem1', length=1, delay_cost=1)
	T0t2_t0t1_mem1 += ADD_mem[0]
	S += 51<T0t2_t0t1_mem1
	S += T0t2_t0t1_mem1<=T0t2_t0t1

	T0c1_a0a1_mem0 = S.Task('T0c1_a0a1_mem0', length=1, delay_cost=1)
	T0c1_a0a1_mem0 += MUL_mem[0]
	S += 54<T0c1_a0a1_mem0
	S += T0c1_a0a1_mem0<=T0c1_a0a1

	T0c1_a0a1_mem1 = S.Task('T0c1_a0a1_mem1', length=1, delay_cost=1)
	T0c1_a0a1_mem1 += ADD_mem[1]
	S += 28<T0c1_a0a1_mem1
	S += T0c1_a0a1_mem1<=T0c1_a0a1

	T010_mem0 = S.Task('T010_mem0', length=1, delay_cost=1)
	T010_mem0 += ADD_mem[1]
	S += 27<T010_mem0
	S += T010_mem0<=T010

	T010_mem1 = S.Task('T010_mem1', length=1, delay_cost=1)
	T010_mem1 += ADD_mem[1]
	S += 27<T010_mem1
	S += T010_mem1<=T010

	T12a10_new_mem0 = S.Task('T12a10_new_mem0', length=1, delay_cost=1)
	T12a10_new_mem0 += ADD_mem[3]
	S += 60<T12a10_new_mem0
	S += T12a10_new_mem0<=T12a10_new

	T12a10_new_mem1 = S.Task('T12a10_new_mem1', length=1, delay_cost=1)
	T12a10_new_mem1 += ADD_mem[1]
	S += 53<T12a10_new_mem1
	S += T12a10_new_mem1<=T12a10_new

	T12a11_new_mem0 = S.Task('T12a11_new_mem0', length=1, delay_cost=1)
	T12a11_new_mem0 += ADD_mem[3]
	S += 60<T12a11_new_mem0
	S += T12a11_new_mem0<=T12a11_new

	T12a11_new_mem1 = S.Task('T12a11_new_mem1', length=1, delay_cost=1)
	T12a11_new_mem1 += ADD_mem[1]
	S += 53<T12a11_new_mem1
	S += T12a11_new_mem1<=T12a11_new

	T12t10_mem0 = S.Task('T12t10_mem0', length=1, delay_cost=1)
	T12t10_mem0 += ADD_mem[1]
	S += 51<T12t10_mem0
	S += T12t10_mem0<=T12t10

	T12t10_mem1 = S.Task('T12t10_mem1', length=1, delay_cost=1)
	T12t10_mem1 += ADD_mem[3]
	S += 60<T12t10_mem1
	S += T12t10_mem1<=T12t10

	T12t11_mem0 = S.Task('T12t11_mem0', length=1, delay_cost=1)
	T12t11_mem0 += ADD_mem[2]
	S += 59<T12t11_mem0
	S += T12t11_mem0<=T12t11

	T12t11_mem1 = S.Task('T12t11_mem1', length=1, delay_cost=1)
	T12t11_mem1 += ADD_mem[1]
	S += 53<T12t11_mem1
	S += T12t11_mem1<=T12t11

	T12t0_a0a1_mem0 = S.Task('T12t0_a0a1_mem0', length=1, delay_cost=1)
	T12t0_a0a1_mem0 += ADD_mem[1]
	S += 51<T12t0_a0a1_mem0
	S += T12t0_a0a1_mem0<=T12t0_a0a1

	T12t0_a0a1_mem1 = S.Task('T12t0_a0a1_mem1', length=1, delay_cost=1)
	T12t0_a0a1_mem1 += ADD_mem[3]
	S += 60<T12t0_a0a1_mem1
	S += T12t0_a0a1_mem1<=T12t0_a0a1

	T12t1_a0a1_mem0 = S.Task('T12t1_a0a1_mem0', length=1, delay_cost=1)
	T12t1_a0a1_mem0 += ADD_mem[2]
	S += 59<T12t1_a0a1_mem0
	S += T12t1_a0a1_mem0<=T12t1_a0a1

	T12t1_a0a1_mem1 = S.Task('T12t1_a0a1_mem1', length=1, delay_cost=1)
	T12t1_a0a1_mem1 += ADD_mem[1]
	S += 53<T12t1_a0a1_mem1
	S += T12t1_a0a1_mem1<=T12t1_a0a1

	T12t2_a0a1_mem0 = S.Task('T12t2_a0a1_mem0', length=1, delay_cost=1)
	T12t2_a0a1_mem0 += ADD_mem[1]
	S += 51<T12t2_a0a1_mem0
	S += T12t2_a0a1_mem0<=T12t2_a0a1

	T12t2_a0a1_mem1 = S.Task('T12t2_a0a1_mem1', length=1, delay_cost=1)
	T12t2_a0a1_mem1 += ADD_mem[2]
	S += 59<T12t2_a0a1_mem1
	S += T12t2_a0a1_mem1<=T12t2_a0a1

	T21a10_new_mem0 = S.Task('T21a10_new_mem0', length=1, delay_cost=1)
	T21a10_new_mem0 += ADD_mem[0]
	S += 57<T21a10_new_mem0
	S += T21a10_new_mem0<=T21a10_new

	T21a10_new_mem1 = S.Task('T21a10_new_mem1', length=1, delay_cost=1)
	T21a10_new_mem1 += ADD_mem[3]
	S += 58<T21a10_new_mem1
	S += T21a10_new_mem1<=T21a10_new

	T21a11_new_mem0 = S.Task('T21a11_new_mem0', length=1, delay_cost=1)
	T21a11_new_mem0 += ADD_mem[0]
	S += 57<T21a11_new_mem0
	S += T21a11_new_mem0<=T21a11_new

	T21a11_new_mem1 = S.Task('T21a11_new_mem1', length=1, delay_cost=1)
	T21a11_new_mem1 += ADD_mem[3]
	S += 58<T21a11_new_mem1
	S += T21a11_new_mem1<=T21a11_new

	T21t10_mem0 = S.Task('T21t10_mem0', length=1, delay_cost=1)
	T21t10_mem0 += ADD_mem[0]
	S += 59<T21t10_mem0
	S += T21t10_mem0<=T21t10

	T21t10_mem1 = S.Task('T21t10_mem1', length=1, delay_cost=1)
	T21t10_mem1 += ADD_mem[0]
	S += 57<T21t10_mem1
	S += T21t10_mem1<=T21t10

	T21t11_mem0 = S.Task('T21t11_mem0', length=1, delay_cost=1)
	T21t11_mem0 += ADD_mem[1]
	S += 58<T21t11_mem0
	S += T21t11_mem0<=T21t11

	T21t11_mem1 = S.Task('T21t11_mem1', length=1, delay_cost=1)
	T21t11_mem1 += ADD_mem[3]
	S += 58<T21t11_mem1
	S += T21t11_mem1<=T21t11

	T21t0_a0a1_mem0 = S.Task('T21t0_a0a1_mem0', length=1, delay_cost=1)
	T21t0_a0a1_mem0 += ADD_mem[0]
	S += 59<T21t0_a0a1_mem0
	S += T21t0_a0a1_mem0<=T21t0_a0a1

	T21t0_a0a1_mem1 = S.Task('T21t0_a0a1_mem1', length=1, delay_cost=1)
	T21t0_a0a1_mem1 += ADD_mem[0]
	S += 57<T21t0_a0a1_mem1
	S += T21t0_a0a1_mem1<=T21t0_a0a1

	T21t1_a0a1_mem0 = S.Task('T21t1_a0a1_mem0', length=1, delay_cost=1)
	T21t1_a0a1_mem0 += ADD_mem[1]
	S += 58<T21t1_a0a1_mem0
	S += T21t1_a0a1_mem0<=T21t1_a0a1

	T21t1_a0a1_mem1 = S.Task('T21t1_a0a1_mem1', length=1, delay_cost=1)
	T21t1_a0a1_mem1 += ADD_mem[3]
	S += 58<T21t1_a0a1_mem1
	S += T21t1_a0a1_mem1<=T21t1_a0a1

	T21t2_a0a1_mem0 = S.Task('T21t2_a0a1_mem0', length=1, delay_cost=1)
	T21t2_a0a1_mem0 += ADD_mem[0]
	S += 59<T21t2_a0a1_mem0
	S += T21t2_a0a1_mem0<=T21t2_a0a1

	T21t2_a0a1_mem1 = S.Task('T21t2_a0a1_mem1', length=1, delay_cost=1)
	T21t2_a0a1_mem1 += ADD_mem[1]
	S += 58<T21t2_a0a1_mem1
	S += T21t2_a0a1_mem1<=T21t2_a0a1

	T3c1_a0b0_mem0 = S.Task('T3c1_a0b0_mem0', length=1, delay_cost=1)
	T3c1_a0b0_mem0 += MUL_mem[0]
	S += 62<T3c1_a0b0_mem0
	S += T3c1_a0b0_mem0<=T3c1_a0b0

	T3c1_a0b0_mem1 = S.Task('T3c1_a0b0_mem1', length=1, delay_cost=1)
	T3c1_a0b0_mem1 += ADD_mem[1]
	S += 25<T3c1_a0b0_mem1
	S += T3c1_a0b0_mem1<=T3c1_a0b0

	T3c1_a1b1_mem0 = S.Task('T3c1_a1b1_mem0', length=1, delay_cost=1)
	T3c1_a1b1_mem0 += MUL_mem[0]
	S += 52<T3c1_a1b1_mem0
	S += T3c1_a1b1_mem0<=T3c1_a1b1

	T3c1_a1b1_mem1 = S.Task('T3c1_a1b1_mem1', length=1, delay_cost=1)
	T3c1_a1b1_mem1 += ADD_mem[1]
	S += 24<T3c1_a1b1_mem1
	S += T3c1_a1b1_mem1<=T3c1_a1b1

	T3t4_t2t3_mem0 = S.Task('T3t4_t2t3_mem0', length=1, delay_cost=1)
	T3t4_t2t3_mem0 += ADD_mem[2]
	S += 38<T3t4_t2t3_mem0
	S += T3t4_t2t3_mem0<=T3t4_t2t3

	T3t4_t2t3_mem1 = S.Task('T3t4_t2t3_mem1', length=1, delay_cost=1)
	T3t4_t2t3_mem1 += ADD_mem[0]
	S += 52<T3t4_t2t3_mem1
	S += T3t4_t2t3_mem1<=T3t4_t2t3

	T3c0_t2t3_mem0 = S.Task('T3c0_t2t3_mem0', length=1, delay_cost=1)
	T3c0_t2t3_mem0 += MUL_mem[0]
	S += 57<T3c0_t2t3_mem0
	S += T3c0_t2t3_mem0<=T3c0_t2t3

	T3c0_t2t3_mem1 = S.Task('T3c0_t2t3_mem1', length=1, delay_cost=1)
	T3c0_t2t3_mem1 += MUL_mem[0]
	S += 59<T3c0_t2t3_mem1
	S += T3c0_t2t3_mem1<=T3c0_t2t3

	T3t6_t2t3_mem0 = S.Task('T3t6_t2t3_mem0', length=1, delay_cost=1)
	T3t6_t2t3_mem0 += MUL_mem[0]
	S += 57<T3t6_t2t3_mem0
	S += T3t6_t2t3_mem0<=T3t6_t2t3

	T3t6_t2t3_mem1 = S.Task('T3t6_t2t3_mem1', length=1, delay_cost=1)
	T3t6_t2t3_mem1 += MUL_mem[0]
	S += 59<T3t6_t2t3_mem1
	S += T3t6_t2t3_mem1<=T3t6_t2t3

	T3t5_0_mem0 = S.Task('T3t5_0_mem0', length=1, delay_cost=1)
	T3t5_0_mem0 += ADD_mem[1]
	S += 29<T3t5_0_mem0
	S += T3t5_0_mem0<=T3t5_0

	T3t5_0_mem1 = S.Task('T3t5_0_mem1', length=1, delay_cost=1)
	T3t5_0_mem1 += ADD_mem[0]
	S += 26<T3t5_0_mem1
	S += T3t5_0_mem1<=T3t5_0

	T4t0_t0t1_mem0 = S.Task('T4t0_t0t1_mem0', length=1, delay_cost=1)
	T4t0_t0t1_mem0 += ADD_mem[1]
	S += 56<T4t0_t0t1_mem0
	S += T4t0_t0t1_mem0<=T4t0_t0t1

	T4t0_t0t1_mem1 = S.Task('T4t0_t0t1_mem1', length=1, delay_cost=1)
	T4t0_t0t1_mem1 += ADD_mem[3]
	S += 36<T4t0_t0t1_mem1
	S += T4t0_t0t1_mem1<=T4t0_t0t1

	T4t1_t0t1_mem0 = S.Task('T4t1_t0t1_mem0', length=1, delay_cost=1)
	T4t1_t0t1_mem0 += ADD_mem[1]
	S += 54<T4t1_t0t1_mem0
	S += T4t1_t0t1_mem0<=T4t1_t0t1

	T4t1_t0t1_mem1 = S.Task('T4t1_t0t1_mem1', length=1, delay_cost=1)
	T4t1_t0t1_mem1 += ADD_mem[3]
	S += 26<T4t1_t0t1_mem1
	S += T4t1_t0t1_mem1<=T4t1_t0t1

	T4t2_t0t1_mem0 = S.Task('T4t2_t0t1_mem0', length=1, delay_cost=1)
	T4t2_t0t1_mem0 += ADD_mem[1]
	S += 56<T4t2_t0t1_mem0
	S += T4t2_t0t1_mem0<=T4t2_t0t1

	T4t2_t0t1_mem1 = S.Task('T4t2_t0t1_mem1', length=1, delay_cost=1)
	T4t2_t0t1_mem1 += ADD_mem[1]
	S += 54<T4t2_t0t1_mem1
	S += T4t2_t0t1_mem1<=T4t2_t0t1

	T4c1_a0a1_mem0 = S.Task('T4c1_a0a1_mem0', length=1, delay_cost=1)
	T4c1_a0a1_mem0 += MUL_mem[0]
	S += 55<T4c1_a0a1_mem0
	S += T4c1_a0a1_mem0<=T4c1_a0a1

	T4c1_a0a1_mem1 = S.Task('T4c1_a0a1_mem1', length=1, delay_cost=1)
	T4c1_a0a1_mem1 += ADD_mem[1]
	S += 31<T4c1_a0a1_mem1
	S += T4c1_a0a1_mem1<=T4c1_a0a1

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	T410_mem0 += ADD_mem[2]
	S += 21<T410_mem0
	S += T410_mem0<=T410

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	T410_mem1 += ADD_mem[2]
	S += 21<T410_mem1
	S += T410_mem1<=T410

	T5c1_a0b0_mem0 = S.Task('T5c1_a0b0_mem0', length=1, delay_cost=1)
	T5c1_a0b0_mem0 += MUL_mem[0]
	S += 47<T5c1_a0b0_mem0
	S += T5c1_a0b0_mem0<=T5c1_a0b0

	T5c1_a0b0_mem1 = S.Task('T5c1_a0b0_mem1', length=1, delay_cost=1)
	T5c1_a0b0_mem1 += ADD_mem[1]
	S += 15<T5c1_a0b0_mem1
	S += T5c1_a0b0_mem1<=T5c1_a0b0

	T5c1_a1b1_mem0 = S.Task('T5c1_a1b1_mem0', length=1, delay_cost=1)
	T5c1_a1b1_mem0 += MUL_mem[0]
	S += 53<T5c1_a1b1_mem0
	S += T5c1_a1b1_mem0<=T5c1_a1b1

	T5c1_a1b1_mem1 = S.Task('T5c1_a1b1_mem1', length=1, delay_cost=1)
	T5c1_a1b1_mem1 += ADD_mem[3]
	S += 22<T5c1_a1b1_mem1
	S += T5c1_a1b1_mem1<=T5c1_a1b1

	T5t4_t2t3_mem0 = S.Task('T5t4_t2t3_mem0', length=1, delay_cost=1)
	T5t4_t2t3_mem0 += ADD_mem[2]
	S += 32<T5t4_t2t3_mem0
	S += T5t4_t2t3_mem0<=T5t4_t2t3

	T5t4_t2t3_mem1 = S.Task('T5t4_t2t3_mem1', length=1, delay_cost=1)
	T5t4_t2t3_mem1 += ADD_mem[2]
	S += 44<T5t4_t2t3_mem1
	S += T5t4_t2t3_mem1<=T5t4_t2t3

	T5c0_t2t3_mem0 = S.Task('T5c0_t2t3_mem0', length=1, delay_cost=1)
	T5c0_t2t3_mem0 += MUL_mem[0]
	S += 49<T5c0_t2t3_mem0
	S += T5c0_t2t3_mem0<=T5c0_t2t3

	T5c0_t2t3_mem1 = S.Task('T5c0_t2t3_mem1', length=1, delay_cost=1)
	T5c0_t2t3_mem1 += MUL_mem[0]
	S += 48<T5c0_t2t3_mem1
	S += T5c0_t2t3_mem1<=T5c0_t2t3

	T5t6_t2t3_mem0 = S.Task('T5t6_t2t3_mem0', length=1, delay_cost=1)
	T5t6_t2t3_mem0 += MUL_mem[0]
	S += 49<T5t6_t2t3_mem0
	S += T5t6_t2t3_mem0<=T5t6_t2t3

	T5t6_t2t3_mem1 = S.Task('T5t6_t2t3_mem1', length=1, delay_cost=1)
	T5t6_t2t3_mem1 += MUL_mem[0]
	S += 48<T5t6_t2t3_mem1
	S += T5t6_t2t3_mem1<=T5t6_t2t3

	T5t5_0_mem0 = S.Task('T5t5_0_mem0', length=1, delay_cost=1)
	T5t5_0_mem0 += ADD_mem[0]
	S += 14<T5t5_0_mem0
	S += T5t5_0_mem0<=T5t5_0

	T5t5_0_mem1 = S.Task('T5t5_0_mem1', length=1, delay_cost=1)
	T5t5_0_mem1 += ADD_mem[1]
	S += 32<T5t5_0_mem1
	S += T5t5_0_mem1<=T5t5_0

	T6c1_a0b0_mem0 = S.Task('T6c1_a0b0_mem0', length=1, delay_cost=1)
	T6c1_a0b0_mem0 += MUL_mem[0]
	S += 61<T6c1_a0b0_mem0
	S += T6c1_a0b0_mem0<=T6c1_a0b0

	T6c1_a0b0_mem1 = S.Task('T6c1_a0b0_mem1', length=1, delay_cost=1)
	T6c1_a0b0_mem1 += ADD_mem[2]
	S += 20<T6c1_a0b0_mem1
	S += T6c1_a0b0_mem1<=T6c1_a0b0

	T6c1_a1b1_mem0 = S.Task('T6c1_a1b1_mem0', length=1, delay_cost=1)
	T6c1_a1b1_mem0 += MUL_mem[0]
	S += 51<T6c1_a1b1_mem0
	S += T6c1_a1b1_mem0<=T6c1_a1b1

	T6c1_a1b1_mem1 = S.Task('T6c1_a1b1_mem1', length=1, delay_cost=1)
	T6c1_a1b1_mem1 += ADD_mem[1]
	S += 23<T6c1_a1b1_mem1
	S += T6c1_a1b1_mem1<=T6c1_a1b1

	T6t4_t2t3_mem0 = S.Task('T6t4_t2t3_mem0', length=1, delay_cost=1)
	T6t4_t2t3_mem0 += ADD_mem[0]
	S += 52<T6t4_t2t3_mem0
	S += T6t4_t2t3_mem0<=T6t4_t2t3

	T6t4_t2t3_mem1 = S.Task('T6t4_t2t3_mem1', length=1, delay_cost=1)
	T6t4_t2t3_mem1 += ADD_mem[1]
	S += 39<T6t4_t2t3_mem1
	S += T6t4_t2t3_mem1<=T6t4_t2t3

	T6c0_t2t3_mem0 = S.Task('T6c0_t2t3_mem0', length=1, delay_cost=1)
	T6c0_t2t3_mem0 += MUL_mem[0]
	S += 60<T6c0_t2t3_mem0
	S += T6c0_t2t3_mem0<=T6c0_t2t3

	T6c0_t2t3_mem1 = S.Task('T6c0_t2t3_mem1', length=1, delay_cost=1)
	T6c0_t2t3_mem1 += MUL_mem[0]
	S += 63<T6c0_t2t3_mem1
	S += T6c0_t2t3_mem1<=T6c0_t2t3

	T6t6_t2t3_mem0 = S.Task('T6t6_t2t3_mem0', length=1, delay_cost=1)
	T6t6_t2t3_mem0 += MUL_mem[0]
	S += 60<T6t6_t2t3_mem0
	S += T6t6_t2t3_mem0<=T6t6_t2t3

	T6t6_t2t3_mem1 = S.Task('T6t6_t2t3_mem1', length=1, delay_cost=1)
	T6t6_t2t3_mem1 += MUL_mem[0]
	S += 63<T6t6_t2t3_mem1
	S += T6t6_t2t3_mem1<=T6t6_t2t3

	T6t5_0_mem0 = S.Task('T6t5_0_mem0', length=1, delay_cost=1)
	T6t5_0_mem0 += ADD_mem[1]
	S += 30<T6t5_0_mem0
	S += T6t5_0_mem0<=T6t5_0

	T6t5_0_mem1 = S.Task('T6t5_0_mem1', length=1, delay_cost=1)
	T6t5_0_mem1 += ADD_mem[1]
	S += 18<T6t5_0_mem1
	S += T6t5_0_mem1<=T6t5_0

	T7c1_a0b0_mem0 = S.Task('T7c1_a0b0_mem0', length=1, delay_cost=1)
	T7c1_a0b0_mem0 += MUL_mem[0]
	S += 56<T7c1_a0b0_mem0
	S += T7c1_a0b0_mem0<=T7c1_a0b0

	T7c1_a0b0_mem1 = S.Task('T7c1_a0b0_mem1', length=1, delay_cost=1)
	T7c1_a0b0_mem1 += ADD_mem[1]
	S += 17<T7c1_a0b0_mem1
	S += T7c1_a0b0_mem1<=T7c1_a0b0

	T7c1_a1b1_mem0 = S.Task('T7c1_a1b1_mem0', length=1, delay_cost=1)
	T7c1_a1b1_mem0 += MUL_mem[0]
	S += 58<T7c1_a1b1_mem0
	S += T7c1_a1b1_mem0<=T7c1_a1b1

	T7c1_a1b1_mem1 = S.Task('T7c1_a1b1_mem1', length=1, delay_cost=1)
	T7c1_a1b1_mem1 += ADD_mem[3]
	S += 12<T7c1_a1b1_mem1
	S += T7c1_a1b1_mem1<=T7c1_a1b1

	T7t4_t2t3_mem0 = S.Task('T7t4_t2t3_mem0', length=1, delay_cost=1)
	T7t4_t2t3_mem0 += ADD_mem[0]
	S += 35<T7t4_t2t3_mem0
	S += T7t4_t2t3_mem0<=T7t4_t2t3

	T7t4_t2t3_mem1 = S.Task('T7t4_t2t3_mem1', length=1, delay_cost=1)
	T7t4_t2t3_mem1 += ADD_mem[2]
	S += 38<T7t4_t2t3_mem1
	S += T7t4_t2t3_mem1<=T7t4_t2t3

	T7c0_t2t3_mem0 = S.Task('T7c0_t2t3_mem0', length=1, delay_cost=1)
	T7c0_t2t3_mem0 += MUL_mem[0]
	S += 43<T7c0_t2t3_mem0
	S += T7c0_t2t3_mem0<=T7c0_t2t3

	T7c0_t2t3_mem1 = S.Task('T7c0_t2t3_mem1', length=1, delay_cost=1)
	T7c0_t2t3_mem1 += MUL_mem[0]
	S += 33<T7c0_t2t3_mem1
	S += T7c0_t2t3_mem1<=T7c0_t2t3

	T7t6_t2t3_mem0 = S.Task('T7t6_t2t3_mem0', length=1, delay_cost=1)
	T7t6_t2t3_mem0 += MUL_mem[0]
	S += 43<T7t6_t2t3_mem0
	S += T7t6_t2t3_mem0<=T7t6_t2t3

	T7t6_t2t3_mem1 = S.Task('T7t6_t2t3_mem1', length=1, delay_cost=1)
	T7t6_t2t3_mem1 += MUL_mem[0]
	S += 33<T7t6_t2t3_mem1
	S += T7t6_t2t3_mem1<=T7t6_t2t3

	T7t5_0_mem0 = S.Task('T7t5_0_mem0', length=1, delay_cost=1)
	T7t5_0_mem0 += ADD_mem[3]
	S += 19<T7t5_0_mem0
	S += T7t5_0_mem0<=T7t5_0

	T7t5_0_mem1 = S.Task('T7t5_0_mem1', length=1, delay_cost=1)
	T7t5_0_mem1 += ADD_mem[3]
	S += 11<T7t5_0_mem1
	S += T7t5_0_mem1<=T7t5_0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sqr012345_mul1_add4/sqr012345_mul1_add4_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sqr012345_mul1_add4_2(0, 0)