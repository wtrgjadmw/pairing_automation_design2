from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 194
	S = Scenario("MUL_1", horizon=horizon)

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
	c_t0_t2_t1_t1_in = S.Task('c_t0_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t2_t1_t1_in >= 0
	c_t0_t2_t1_t1_in += MUL_in[0]

	c_t0_t2_t1_t1_mem0 = S.Task('c_t0_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t1_t1_mem0 >= 0
	c_t0_t2_t1_t1_mem0 += INPUT_mem_r

	c_t0_t2_t1_t1_mem1 = S.Task('c_t0_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t1_t1_mem1 >= 0
	c_t0_t2_t1_t1_mem1 += INPUT_mem_r

	c_t0_t0_t0_t1_in = S.Task('c_t0_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_t1_in >= 1
	c_t0_t0_t0_t1_in += MUL_in[0]

	c_t0_t0_t0_t1_mem0 = S.Task('c_t0_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_t1_mem0 >= 1
	c_t0_t0_t0_t1_mem0 += INPUT_mem_r

	c_t0_t0_t0_t1_mem1 = S.Task('c_t0_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_t1_mem1 >= 1
	c_t0_t0_t0_t1_mem1 += INPUT_mem_r

	c_t0_t2_t1_t1 = S.Task('c_t0_t2_t1_t1', length=7, delay_cost=1)
	S += c_t0_t2_t1_t1 >= 1
	c_t0_t2_t1_t1 += MUL[0]

	c_t0_t0_t0_t1 = S.Task('c_t0_t0_t0_t1', length=7, delay_cost=1)
	S += c_t0_t0_t0_t1 >= 2
	c_t0_t0_t0_t1 += MUL[0]

	c_t0_t1_t0_t0_in = S.Task('c_t0_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_t0_in >= 2
	c_t0_t1_t0_t0_in += MUL_in[0]

	c_t0_t1_t0_t0_mem0 = S.Task('c_t0_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_t0_mem0 >= 2
	c_t0_t1_t0_t0_mem0 += INPUT_mem_r

	c_t0_t1_t0_t0_mem1 = S.Task('c_t0_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_t0_mem1 >= 2
	c_t0_t1_t0_t0_mem1 += INPUT_mem_r

	c_t0_t1_t0_t0 = S.Task('c_t0_t1_t0_t0', length=7, delay_cost=1)
	S += c_t0_t1_t0_t0 >= 3
	c_t0_t1_t0_t0 += MUL[0]

	c_t0_t2_t0_t0_in = S.Task('c_t0_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t2_t0_t0_in >= 3
	c_t0_t2_t0_t0_in += MUL_in[0]

	c_t0_t2_t0_t0_mem0 = S.Task('c_t0_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_t0_mem0 >= 3
	c_t0_t2_t0_t0_mem0 += INPUT_mem_r

	c_t0_t2_t0_t0_mem1 = S.Task('c_t0_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_t0_mem1 >= 3
	c_t0_t2_t0_t0_mem1 += INPUT_mem_r

	c_t0_t1_t1_t1_in = S.Task('c_t0_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_t1_in >= 4
	c_t0_t1_t1_t1_in += MUL_in[0]

	c_t0_t1_t1_t1_mem0 = S.Task('c_t0_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_t1_mem0 >= 4
	c_t0_t1_t1_t1_mem0 += INPUT_mem_r

	c_t0_t1_t1_t1_mem1 = S.Task('c_t0_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_t1_mem1 >= 4
	c_t0_t1_t1_t1_mem1 += INPUT_mem_r

	c_t0_t2_t0_t0 = S.Task('c_t0_t2_t0_t0', length=7, delay_cost=1)
	S += c_t0_t2_t0_t0 >= 4
	c_t0_t2_t0_t0 += MUL[0]

	c_t0_t1_t0_t1_in = S.Task('c_t0_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_t1_in >= 5
	c_t0_t1_t0_t1_in += MUL_in[0]

	c_t0_t1_t0_t1_mem0 = S.Task('c_t0_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_t1_mem0 >= 5
	c_t0_t1_t0_t1_mem0 += INPUT_mem_r

	c_t0_t1_t0_t1_mem1 = S.Task('c_t0_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_t1_mem1 >= 5
	c_t0_t1_t0_t1_mem1 += INPUT_mem_r

	c_t0_t1_t1_t1 = S.Task('c_t0_t1_t1_t1', length=7, delay_cost=1)
	S += c_t0_t1_t1_t1 >= 5
	c_t0_t1_t1_t1 += MUL[0]

	c_t0_t0_t1_t0_in = S.Task('c_t0_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_t0_in >= 6
	c_t0_t0_t1_t0_in += MUL_in[0]

	c_t0_t0_t1_t0_mem0 = S.Task('c_t0_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_t0_mem0 >= 6
	c_t0_t0_t1_t0_mem0 += INPUT_mem_r

	c_t0_t0_t1_t0_mem1 = S.Task('c_t0_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_t0_mem1 >= 6
	c_t0_t0_t1_t0_mem1 += INPUT_mem_r

	c_t0_t1_t0_t1 = S.Task('c_t0_t1_t0_t1', length=7, delay_cost=1)
	S += c_t0_t1_t0_t1 >= 6
	c_t0_t1_t0_t1 += MUL[0]

	c_t0_t0_t1_t0 = S.Task('c_t0_t0_t1_t0', length=7, delay_cost=1)
	S += c_t0_t0_t1_t0 >= 7
	c_t0_t0_t1_t0 += MUL[0]

	c_t0_t2_t0_t1_in = S.Task('c_t0_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t2_t0_t1_in >= 7
	c_t0_t2_t0_t1_in += MUL_in[0]

	c_t0_t2_t0_t1_mem0 = S.Task('c_t0_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_t1_mem0 >= 7
	c_t0_t2_t0_t1_mem0 += INPUT_mem_r

	c_t0_t2_t0_t1_mem1 = S.Task('c_t0_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_t1_mem1 >= 7
	c_t0_t2_t0_t1_mem1 += INPUT_mem_r

	c_t0_t1_t1_t0_in = S.Task('c_t0_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_t0_in >= 8
	c_t0_t1_t1_t0_in += MUL_in[0]

	c_t0_t1_t1_t0_mem0 = S.Task('c_t0_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_t0_mem0 >= 8
	c_t0_t1_t1_t0_mem0 += INPUT_mem_r

	c_t0_t1_t1_t0_mem1 = S.Task('c_t0_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_t0_mem1 >= 8
	c_t0_t1_t1_t0_mem1 += INPUT_mem_r

	c_t0_t2_t0_t1 = S.Task('c_t0_t2_t0_t1', length=7, delay_cost=1)
	S += c_t0_t2_t0_t1 >= 8
	c_t0_t2_t0_t1 += MUL[0]

	c_t0_t1_t1_t0 = S.Task('c_t0_t1_t1_t0', length=7, delay_cost=1)
	S += c_t0_t1_t1_t0 >= 9
	c_t0_t1_t1_t0 += MUL[0]

	c_t0_t2_t1_t0_in = S.Task('c_t0_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t2_t1_t0_in >= 9
	c_t0_t2_t1_t0_in += MUL_in[0]

	c_t0_t2_t1_t0_mem0 = S.Task('c_t0_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t1_t0_mem0 >= 9
	c_t0_t2_t1_t0_mem0 += INPUT_mem_r

	c_t0_t2_t1_t0_mem1 = S.Task('c_t0_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t1_t0_mem1 >= 9
	c_t0_t2_t1_t0_mem1 += INPUT_mem_r

	c_t0_t0_t1_t1_in = S.Task('c_t0_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_t1_in >= 10
	c_t0_t0_t1_t1_in += MUL_in[0]

	c_t0_t0_t1_t1_mem0 = S.Task('c_t0_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_t1_mem0 >= 10
	c_t0_t0_t1_t1_mem0 += INPUT_mem_r

	c_t0_t0_t1_t1_mem1 = S.Task('c_t0_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_t1_mem1 >= 10
	c_t0_t0_t1_t1_mem1 += INPUT_mem_r

	c_t0_t2_t1_t0 = S.Task('c_t0_t2_t1_t0', length=7, delay_cost=1)
	S += c_t0_t2_t1_t0 >= 10
	c_t0_t2_t1_t0 += MUL[0]

	c_t0_t0_t0_t0_in = S.Task('c_t0_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_t0_in >= 11
	c_t0_t0_t0_t0_in += MUL_in[0]

	c_t0_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_t0_mem0 >= 11
	c_t0_t0_t0_t0_mem0 += INPUT_mem_r

	c_t0_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_t0_mem1 >= 11
	c_t0_t0_t0_t0_mem1 += INPUT_mem_r

	c_t0_t0_t1_t1 = S.Task('c_t0_t0_t1_t1', length=7, delay_cost=1)
	S += c_t0_t0_t1_t1 >= 11
	c_t0_t0_t1_t1 += MUL[0]

	c_t0_t0_t0_t0 = S.Task('c_t0_t0_t0_t0', length=7, delay_cost=1)
	S += c_t0_t0_t0_t0 >= 12
	c_t0_t0_t0_t0 += MUL[0]

	c_t0_t2_t0_t2_mem0 = S.Task('c_t0_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_t2_mem0 >= 12
	c_t0_t2_t0_t2_mem0 += INPUT_mem_r

	c_t0_t2_t0_t2_mem1 = S.Task('c_t0_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_t2_mem1 >= 12
	c_t0_t2_t0_t2_mem1 += INPUT_mem_r

	c_t0_t1_t1_t3_mem0 = S.Task('c_t0_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_t3_mem0 >= 13
	c_t0_t1_t1_t3_mem0 += INPUT_mem_r

	c_t0_t1_t1_t3_mem1 = S.Task('c_t0_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_t3_mem1 >= 13
	c_t0_t1_t1_t3_mem1 += INPUT_mem_r

	c_t0_t2_t0_t2 = S.Task('c_t0_t2_t0_t2', length=1, delay_cost=1)
	S += c_t0_t2_t0_t2 >= 13
	c_t0_t2_t0_t2 += ADD[0]

	c_t0_t1_t1_t3 = S.Task('c_t0_t1_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t1_t3 >= 14
	c_t0_t1_t1_t3 += ADD[2]

	c_t0_t1_t20_mem0 = S.Task('c_t0_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t20_mem0 >= 14
	c_t0_t1_t20_mem0 += INPUT_mem_r

	c_t0_t1_t20_mem1 = S.Task('c_t0_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t20_mem1 >= 14
	c_t0_t1_t20_mem1 += INPUT_mem_r

	c_t0_t0_t20_mem0 = S.Task('c_t0_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t20_mem0 >= 15
	c_t0_t0_t20_mem0 += INPUT_mem_r

	c_t0_t0_t20_mem1 = S.Task('c_t0_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t20_mem1 >= 15
	c_t0_t0_t20_mem1 += INPUT_mem_r

	c_t0_t1_t20 = S.Task('c_t0_t1_t20', length=1, delay_cost=1)
	S += c_t0_t1_t20 >= 15
	c_t0_t1_t20 += ADD[2]

	c_t0_t0_t20 = S.Task('c_t0_t0_t20', length=1, delay_cost=1)
	S += c_t0_t0_t20 >= 16
	c_t0_t0_t20 += ADD[1]

	c_t0_t1_t1_t2_mem0 = S.Task('c_t0_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_t2_mem0 >= 16
	c_t0_t1_t1_t2_mem0 += INPUT_mem_r

	c_t0_t1_t1_t2_mem1 = S.Task('c_t0_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_t2_mem1 >= 16
	c_t0_t1_t1_t2_mem1 += INPUT_mem_r

	c_t0_t0_t1_t3_mem0 = S.Task('c_t0_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_t3_mem0 >= 17
	c_t0_t0_t1_t3_mem0 += INPUT_mem_r

	c_t0_t0_t1_t3_mem1 = S.Task('c_t0_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_t3_mem1 >= 17
	c_t0_t0_t1_t3_mem1 += INPUT_mem_r

	c_t0_t1_t1_t2 = S.Task('c_t0_t1_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t1_t2 >= 17
	c_t0_t1_t1_t2 += ADD[0]

	c_t0_t0_t1_t2_mem0 = S.Task('c_t0_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_t2_mem0 >= 18
	c_t0_t0_t1_t2_mem0 += INPUT_mem_r

	c_t0_t0_t1_t2_mem1 = S.Task('c_t0_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_t2_mem1 >= 18
	c_t0_t0_t1_t2_mem1 += INPUT_mem_r

	c_t0_t0_t1_t3 = S.Task('c_t0_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t0_t1_t3 >= 18
	c_t0_t0_t1_t3 += ADD[1]

	c_t0_t0_t1_t2 = S.Task('c_t0_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t0_t1_t2 >= 19
	c_t0_t0_t1_t2 += ADD[2]

	c_t0_t1_t21_mem0 = S.Task('c_t0_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t21_mem0 >= 19
	c_t0_t1_t21_mem0 += INPUT_mem_r

	c_t0_t1_t21_mem1 = S.Task('c_t0_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t21_mem1 >= 19
	c_t0_t1_t21_mem1 += INPUT_mem_r

	c_t0_t1_t21 = S.Task('c_t0_t1_t21', length=1, delay_cost=1)
	S += c_t0_t1_t21 >= 20
	c_t0_t1_t21 += ADD[0]

	c_t0_t1_t31_mem0 = S.Task('c_t0_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t31_mem0 >= 20
	c_t0_t1_t31_mem0 += INPUT_mem_r

	c_t0_t1_t31_mem1 = S.Task('c_t0_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t31_mem1 >= 20
	c_t0_t1_t31_mem1 += INPUT_mem_r

	c_t0_t0_t0_t3_mem0 = S.Task('c_t0_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_t3_mem0 >= 21
	c_t0_t0_t0_t3_mem0 += INPUT_mem_r

	c_t0_t0_t0_t3_mem1 = S.Task('c_t0_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_t3_mem1 >= 21
	c_t0_t0_t0_t3_mem1 += INPUT_mem_r

	c_t0_t1_t31 = S.Task('c_t0_t1_t31', length=1, delay_cost=1)
	S += c_t0_t1_t31 >= 21
	c_t0_t1_t31 += ADD[1]

	c_t0_t0_t0_t2_mem0 = S.Task('c_t0_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_t2_mem0 >= 22
	c_t0_t0_t0_t2_mem0 += INPUT_mem_r

	c_t0_t0_t0_t2_mem1 = S.Task('c_t0_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_t2_mem1 >= 22
	c_t0_t0_t0_t2_mem1 += INPUT_mem_r

	c_t0_t0_t0_t3 = S.Task('c_t0_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t0_t3 >= 22
	c_t0_t0_t0_t3 += ADD[1]

	c_t0_t0_t0_t2 = S.Task('c_t0_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t0_t2 >= 23
	c_t0_t0_t0_t2 += ADD[3]

	c_t0_t1_t0_t3_mem0 = S.Task('c_t0_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_t3_mem0 >= 23
	c_t0_t1_t0_t3_mem0 += INPUT_mem_r

	c_t0_t1_t0_t3_mem1 = S.Task('c_t0_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_t3_mem1 >= 23
	c_t0_t1_t0_t3_mem1 += INPUT_mem_r

	c_t0_t1_t0_t3 = S.Task('c_t0_t1_t0_t3', length=1, delay_cost=1)
	S += c_t0_t1_t0_t3 >= 24
	c_t0_t1_t0_t3 += ADD[1]

	c_t0_t1_t30_mem0 = S.Task('c_t0_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t30_mem0 >= 24
	c_t0_t1_t30_mem0 += INPUT_mem_r

	c_t0_t1_t30_mem1 = S.Task('c_t0_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t30_mem1 >= 24
	c_t0_t1_t30_mem1 += INPUT_mem_r

	c_t0_t1_t30 = S.Task('c_t0_t1_t30', length=1, delay_cost=1)
	S += c_t0_t1_t30 >= 25
	c_t0_t1_t30 += ADD[0]

	c_t0_t2_t0_t3_mem0 = S.Task('c_t0_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_t3_mem0 >= 25
	c_t0_t2_t0_t3_mem0 += INPUT_mem_r

	c_t0_t2_t0_t3_mem1 = S.Task('c_t0_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_t3_mem1 >= 25
	c_t0_t2_t0_t3_mem1 += INPUT_mem_r

	c_t0_t1_t0_t2_mem0 = S.Task('c_t0_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_t2_mem0 >= 26
	c_t0_t1_t0_t2_mem0 += INPUT_mem_r

	c_t0_t1_t0_t2_mem1 = S.Task('c_t0_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_t2_mem1 >= 26
	c_t0_t1_t0_t2_mem1 += INPUT_mem_r

	c_t0_t2_t0_t3 = S.Task('c_t0_t2_t0_t3', length=1, delay_cost=1)
	S += c_t0_t2_t0_t3 >= 26
	c_t0_t2_t0_t3 += ADD[0]

	c_t0_t0_t31_mem0 = S.Task('c_t0_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t31_mem0 >= 27
	c_t0_t0_t31_mem0 += INPUT_mem_r

	c_t0_t0_t31_mem1 = S.Task('c_t0_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t31_mem1 >= 27
	c_t0_t0_t31_mem1 += INPUT_mem_r

	c_t0_t1_t0_t2 = S.Task('c_t0_t1_t0_t2', length=1, delay_cost=1)
	S += c_t0_t1_t0_t2 >= 27
	c_t0_t1_t0_t2 += ADD[0]

	c_t0_t0_t30_mem0 = S.Task('c_t0_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t30_mem0 >= 28
	c_t0_t0_t30_mem0 += INPUT_mem_r

	c_t0_t0_t30_mem1 = S.Task('c_t0_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t30_mem1 >= 28
	c_t0_t0_t30_mem1 += INPUT_mem_r

	c_t0_t0_t31 = S.Task('c_t0_t0_t31', length=1, delay_cost=1)
	S += c_t0_t0_t31 >= 28
	c_t0_t0_t31 += ADD[0]

	c_t0_t0_t21_mem0 = S.Task('c_t0_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t21_mem0 >= 29
	c_t0_t0_t21_mem0 += INPUT_mem_r

	c_t0_t0_t21_mem1 = S.Task('c_t0_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t21_mem1 >= 29
	c_t0_t0_t21_mem1 += INPUT_mem_r

	c_t0_t0_t30 = S.Task('c_t0_t0_t30', length=1, delay_cost=1)
	S += c_t0_t0_t30 >= 29
	c_t0_t0_t30 += ADD[0]

	c_t0_t0_t21 = S.Task('c_t0_t0_t21', length=1, delay_cost=1)
	S += c_t0_t0_t21 >= 30
	c_t0_t0_t21 += ADD[0]


	# new tasks
	c_t0_t2_t1_t2 = S.Task('c_t0_t2_t1_t2', length=1, delay_cost=1)
	c_t0_t2_t1_t2 += alt(ADD)

	c_t0_t2_t1_t2_mem0 = S.Task('c_t0_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t0_t2_t1_t2_mem0 += INPUT_mem_r
	S += c_t0_t2_t1_t2_mem0 <= c_t0_t2_t1_t2

	c_t0_t2_t1_t2_mem1 = S.Task('c_t0_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t0_t2_t1_t2_mem1 += INPUT_mem_r
	S += c_t0_t2_t1_t2_mem1 <= c_t0_t2_t1_t2

	c_t0_t2_t1_t3 = S.Task('c_t0_t2_t1_t3', length=1, delay_cost=1)
	c_t0_t2_t1_t3 += alt(ADD)

	c_t0_t2_t1_t3_mem0 = S.Task('c_t0_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t0_t2_t1_t3_mem0 += INPUT_mem_r
	S += c_t0_t2_t1_t3_mem0 <= c_t0_t2_t1_t3

	c_t0_t2_t1_t3_mem1 = S.Task('c_t0_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t0_t2_t1_t3_mem1 += INPUT_mem_r
	S += c_t0_t2_t1_t3_mem1 <= c_t0_t2_t1_t3

	c_t0_t2_t20 = S.Task('c_t0_t2_t20', length=1, delay_cost=1)
	c_t0_t2_t20 += alt(ADD)

	c_t0_t2_t20_mem0 = S.Task('c_t0_t2_t20_mem0', length=1, delay_cost=1)
	c_t0_t2_t20_mem0 += INPUT_mem_r
	S += c_t0_t2_t20_mem0 <= c_t0_t2_t20

	c_t0_t2_t20_mem1 = S.Task('c_t0_t2_t20_mem1', length=1, delay_cost=1)
	c_t0_t2_t20_mem1 += INPUT_mem_r
	S += c_t0_t2_t20_mem1 <= c_t0_t2_t20

	c_t0_t2_t21 = S.Task('c_t0_t2_t21', length=1, delay_cost=1)
	c_t0_t2_t21 += alt(ADD)

	c_t0_t2_t21_mem0 = S.Task('c_t0_t2_t21_mem0', length=1, delay_cost=1)
	c_t0_t2_t21_mem0 += INPUT_mem_r
	S += c_t0_t2_t21_mem0 <= c_t0_t2_t21

	c_t0_t2_t21_mem1 = S.Task('c_t0_t2_t21_mem1', length=1, delay_cost=1)
	c_t0_t2_t21_mem1 += INPUT_mem_r
	S += c_t0_t2_t21_mem1 <= c_t0_t2_t21

	c_t0_t2_t30 = S.Task('c_t0_t2_t30', length=1, delay_cost=1)
	c_t0_t2_t30 += alt(ADD)

	c_t0_t2_t30_mem0 = S.Task('c_t0_t2_t30_mem0', length=1, delay_cost=1)
	c_t0_t2_t30_mem0 += INPUT_mem_r
	S += c_t0_t2_t30_mem0 <= c_t0_t2_t30

	c_t0_t2_t30_mem1 = S.Task('c_t0_t2_t30_mem1', length=1, delay_cost=1)
	c_t0_t2_t30_mem1 += INPUT_mem_r
	S += c_t0_t2_t30_mem1 <= c_t0_t2_t30

	c_t0_t2_t31 = S.Task('c_t0_t2_t31', length=1, delay_cost=1)
	c_t0_t2_t31 += alt(ADD)

	c_t0_t2_t31_mem0 = S.Task('c_t0_t2_t31_mem0', length=1, delay_cost=1)
	c_t0_t2_t31_mem0 += INPUT_mem_r
	S += c_t0_t2_t31_mem0 <= c_t0_t2_t31

	c_t0_t2_t31_mem1 = S.Task('c_t0_t2_t31_mem1', length=1, delay_cost=1)
	c_t0_t2_t31_mem1 += INPUT_mem_r
	S += c_t0_t2_t31_mem1 <= c_t0_t2_t31

	c_t0_t3000 = S.Task('c_t0_t3000', length=1, delay_cost=1)
	c_t0_t3000 += alt(ADD)

	c_t0_t3000_mem0 = S.Task('c_t0_t3000_mem0', length=1, delay_cost=1)
	c_t0_t3000_mem0 += INPUT_mem_r
	S += c_t0_t3000_mem0 <= c_t0_t3000

	c_t0_t3000_mem1 = S.Task('c_t0_t3000_mem1', length=1, delay_cost=1)
	c_t0_t3000_mem1 += INPUT_mem_r
	S += c_t0_t3000_mem1 <= c_t0_t3000

	c_t0_t3001 = S.Task('c_t0_t3001', length=1, delay_cost=1)
	c_t0_t3001 += alt(ADD)

	c_t0_t3001_mem0 = S.Task('c_t0_t3001_mem0', length=1, delay_cost=1)
	c_t0_t3001_mem0 += INPUT_mem_r
	S += c_t0_t3001_mem0 <= c_t0_t3001

	c_t0_t3001_mem1 = S.Task('c_t0_t3001_mem1', length=1, delay_cost=1)
	c_t0_t3001_mem1 += INPUT_mem_r
	S += c_t0_t3001_mem1 <= c_t0_t3001

	c_t0_t3010 = S.Task('c_t0_t3010', length=1, delay_cost=1)
	c_t0_t3010 += alt(ADD)

	c_t0_t3010_mem0 = S.Task('c_t0_t3010_mem0', length=1, delay_cost=1)
	c_t0_t3010_mem0 += INPUT_mem_r
	S += c_t0_t3010_mem0 <= c_t0_t3010

	c_t0_t3010_mem1 = S.Task('c_t0_t3010_mem1', length=1, delay_cost=1)
	c_t0_t3010_mem1 += INPUT_mem_r
	S += c_t0_t3010_mem1 <= c_t0_t3010

	c_t0_t3011 = S.Task('c_t0_t3011', length=1, delay_cost=1)
	c_t0_t3011 += alt(ADD)

	c_t0_t3011_mem0 = S.Task('c_t0_t3011_mem0', length=1, delay_cost=1)
	c_t0_t3011_mem0 += INPUT_mem_r
	S += c_t0_t3011_mem0 <= c_t0_t3011

	c_t0_t3011_mem1 = S.Task('c_t0_t3011_mem1', length=1, delay_cost=1)
	c_t0_t3011_mem1 += INPUT_mem_r
	S += c_t0_t3011_mem1 <= c_t0_t3011

	c_t0_t3100 = S.Task('c_t0_t3100', length=1, delay_cost=1)
	c_t0_t3100 += alt(ADD)

	c_t0_t3100_mem0 = S.Task('c_t0_t3100_mem0', length=1, delay_cost=1)
	c_t0_t3100_mem0 += INPUT_mem_r
	S += c_t0_t3100_mem0 <= c_t0_t3100

	c_t0_t3100_mem1 = S.Task('c_t0_t3100_mem1', length=1, delay_cost=1)
	c_t0_t3100_mem1 += INPUT_mem_r
	S += c_t0_t3100_mem1 <= c_t0_t3100

	c_t0_t3101 = S.Task('c_t0_t3101', length=1, delay_cost=1)
	c_t0_t3101 += alt(ADD)

	c_t0_t3101_mem0 = S.Task('c_t0_t3101_mem0', length=1, delay_cost=1)
	c_t0_t3101_mem0 += INPUT_mem_r
	S += c_t0_t3101_mem0 <= c_t0_t3101

	c_t0_t3101_mem1 = S.Task('c_t0_t3101_mem1', length=1, delay_cost=1)
	c_t0_t3101_mem1 += INPUT_mem_r
	S += c_t0_t3101_mem1 <= c_t0_t3101

	c_t0_t3110 = S.Task('c_t0_t3110', length=1, delay_cost=1)
	c_t0_t3110 += alt(ADD)

	c_t0_t3110_mem0 = S.Task('c_t0_t3110_mem0', length=1, delay_cost=1)
	c_t0_t3110_mem0 += INPUT_mem_r
	S += c_t0_t3110_mem0 <= c_t0_t3110

	c_t0_t3110_mem1 = S.Task('c_t0_t3110_mem1', length=1, delay_cost=1)
	c_t0_t3110_mem1 += INPUT_mem_r
	S += c_t0_t3110_mem1 <= c_t0_t3110

	c_t0_t3111 = S.Task('c_t0_t3111', length=1, delay_cost=1)
	c_t0_t3111 += alt(ADD)

	c_t0_t3111_mem0 = S.Task('c_t0_t3111_mem0', length=1, delay_cost=1)
	c_t0_t3111_mem0 += INPUT_mem_r
	S += c_t0_t3111_mem0 <= c_t0_t3111

	c_t0_t3111_mem1 = S.Task('c_t0_t3111_mem1', length=1, delay_cost=1)
	c_t0_t3111_mem1 += INPUT_mem_r
	S += c_t0_t3111_mem1 <= c_t0_t3111

	c_t0_t4000 = S.Task('c_t0_t4000', length=1, delay_cost=1)
	c_t0_t4000 += alt(ADD)

	c_t0_t4000_mem0 = S.Task('c_t0_t4000_mem0', length=1, delay_cost=1)
	c_t0_t4000_mem0 += INPUT_mem_r
	S += c_t0_t4000_mem0 <= c_t0_t4000

	c_t0_t4000_mem1 = S.Task('c_t0_t4000_mem1', length=1, delay_cost=1)
	c_t0_t4000_mem1 += INPUT_mem_r
	S += c_t0_t4000_mem1 <= c_t0_t4000

	c_t0_t4001 = S.Task('c_t0_t4001', length=1, delay_cost=1)
	c_t0_t4001 += alt(ADD)

	c_t0_t4001_mem0 = S.Task('c_t0_t4001_mem0', length=1, delay_cost=1)
	c_t0_t4001_mem0 += INPUT_mem_r
	S += c_t0_t4001_mem0 <= c_t0_t4001

	c_t0_t4001_mem1 = S.Task('c_t0_t4001_mem1', length=1, delay_cost=1)
	c_t0_t4001_mem1 += INPUT_mem_r
	S += c_t0_t4001_mem1 <= c_t0_t4001

	c_t0_t4010 = S.Task('c_t0_t4010', length=1, delay_cost=1)
	c_t0_t4010 += alt(ADD)

	c_t0_t4010_mem0 = S.Task('c_t0_t4010_mem0', length=1, delay_cost=1)
	c_t0_t4010_mem0 += INPUT_mem_r
	S += c_t0_t4010_mem0 <= c_t0_t4010

	c_t0_t4010_mem1 = S.Task('c_t0_t4010_mem1', length=1, delay_cost=1)
	c_t0_t4010_mem1 += INPUT_mem_r
	S += c_t0_t4010_mem1 <= c_t0_t4010

	c_t0_t4011 = S.Task('c_t0_t4011', length=1, delay_cost=1)
	c_t0_t4011 += alt(ADD)

	c_t0_t4011_mem0 = S.Task('c_t0_t4011_mem0', length=1, delay_cost=1)
	c_t0_t4011_mem0 += INPUT_mem_r
	S += c_t0_t4011_mem0 <= c_t0_t4011

	c_t0_t4011_mem1 = S.Task('c_t0_t4011_mem1', length=1, delay_cost=1)
	c_t0_t4011_mem1 += INPUT_mem_r
	S += c_t0_t4011_mem1 <= c_t0_t4011

	c_t0_t4100 = S.Task('c_t0_t4100', length=1, delay_cost=1)
	c_t0_t4100 += alt(ADD)

	c_t0_t4100_mem0 = S.Task('c_t0_t4100_mem0', length=1, delay_cost=1)
	c_t0_t4100_mem0 += INPUT_mem_r
	S += c_t0_t4100_mem0 <= c_t0_t4100

	c_t0_t4100_mem1 = S.Task('c_t0_t4100_mem1', length=1, delay_cost=1)
	c_t0_t4100_mem1 += INPUT_mem_r
	S += c_t0_t4100_mem1 <= c_t0_t4100

	c_t0_t4101 = S.Task('c_t0_t4101', length=1, delay_cost=1)
	c_t0_t4101 += alt(ADD)

	c_t0_t4101_mem0 = S.Task('c_t0_t4101_mem0', length=1, delay_cost=1)
	c_t0_t4101_mem0 += INPUT_mem_r
	S += c_t0_t4101_mem0 <= c_t0_t4101

	c_t0_t4101_mem1 = S.Task('c_t0_t4101_mem1', length=1, delay_cost=1)
	c_t0_t4101_mem1 += INPUT_mem_r
	S += c_t0_t4101_mem1 <= c_t0_t4101

	c_t0_t4110 = S.Task('c_t0_t4110', length=1, delay_cost=1)
	c_t0_t4110 += alt(ADD)

	c_t0_t4110_mem0 = S.Task('c_t0_t4110_mem0', length=1, delay_cost=1)
	c_t0_t4110_mem0 += INPUT_mem_r
	S += c_t0_t4110_mem0 <= c_t0_t4110

	c_t0_t4110_mem1 = S.Task('c_t0_t4110_mem1', length=1, delay_cost=1)
	c_t0_t4110_mem1 += INPUT_mem_r
	S += c_t0_t4110_mem1 <= c_t0_t4110

	c_t0_t4111 = S.Task('c_t0_t4111', length=1, delay_cost=1)
	c_t0_t4111 += alt(ADD)

	c_t0_t4111_mem0 = S.Task('c_t0_t4111_mem0', length=1, delay_cost=1)
	c_t0_t4111_mem0 += INPUT_mem_r
	S += c_t0_t4111_mem0 <= c_t0_t4111

	c_t0_t4111_mem1 = S.Task('c_t0_t4111_mem1', length=1, delay_cost=1)
	c_t0_t4111_mem1 += INPUT_mem_r
	S += c_t0_t4111_mem1 <= c_t0_t4111

	c_t0_t5000 = S.Task('c_t0_t5000', length=1, delay_cost=1)
	c_t0_t5000 += alt(ADD)

	c_t0_t5000_mem0 = S.Task('c_t0_t5000_mem0', length=1, delay_cost=1)
	c_t0_t5000_mem0 += INPUT_mem_r
	S += c_t0_t5000_mem0 <= c_t0_t5000

	c_t0_t5000_mem1 = S.Task('c_t0_t5000_mem1', length=1, delay_cost=1)
	c_t0_t5000_mem1 += INPUT_mem_r
	S += c_t0_t5000_mem1 <= c_t0_t5000

	c_t0_t5001 = S.Task('c_t0_t5001', length=1, delay_cost=1)
	c_t0_t5001 += alt(ADD)

	c_t0_t5001_mem0 = S.Task('c_t0_t5001_mem0', length=1, delay_cost=1)
	c_t0_t5001_mem0 += INPUT_mem_r
	S += c_t0_t5001_mem0 <= c_t0_t5001

	c_t0_t5001_mem1 = S.Task('c_t0_t5001_mem1', length=1, delay_cost=1)
	c_t0_t5001_mem1 += INPUT_mem_r
	S += c_t0_t5001_mem1 <= c_t0_t5001

	c_t0_t5010 = S.Task('c_t0_t5010', length=1, delay_cost=1)
	c_t0_t5010 += alt(ADD)

	c_t0_t5010_mem0 = S.Task('c_t0_t5010_mem0', length=1, delay_cost=1)
	c_t0_t5010_mem0 += INPUT_mem_r
	S += c_t0_t5010_mem0 <= c_t0_t5010

	c_t0_t5010_mem1 = S.Task('c_t0_t5010_mem1', length=1, delay_cost=1)
	c_t0_t5010_mem1 += INPUT_mem_r
	S += c_t0_t5010_mem1 <= c_t0_t5010

	c_t0_t5011 = S.Task('c_t0_t5011', length=1, delay_cost=1)
	c_t0_t5011 += alt(ADD)

	c_t0_t5011_mem0 = S.Task('c_t0_t5011_mem0', length=1, delay_cost=1)
	c_t0_t5011_mem0 += INPUT_mem_r
	S += c_t0_t5011_mem0 <= c_t0_t5011

	c_t0_t5011_mem1 = S.Task('c_t0_t5011_mem1', length=1, delay_cost=1)
	c_t0_t5011_mem1 += INPUT_mem_r
	S += c_t0_t5011_mem1 <= c_t0_t5011

	c_t0_t5100 = S.Task('c_t0_t5100', length=1, delay_cost=1)
	c_t0_t5100 += alt(ADD)

	c_t0_t5100_mem0 = S.Task('c_t0_t5100_mem0', length=1, delay_cost=1)
	c_t0_t5100_mem0 += INPUT_mem_r
	S += c_t0_t5100_mem0 <= c_t0_t5100

	c_t0_t5100_mem1 = S.Task('c_t0_t5100_mem1', length=1, delay_cost=1)
	c_t0_t5100_mem1 += INPUT_mem_r
	S += c_t0_t5100_mem1 <= c_t0_t5100

	c_t0_t5101 = S.Task('c_t0_t5101', length=1, delay_cost=1)
	c_t0_t5101 += alt(ADD)

	c_t0_t5101_mem0 = S.Task('c_t0_t5101_mem0', length=1, delay_cost=1)
	c_t0_t5101_mem0 += INPUT_mem_r
	S += c_t0_t5101_mem0 <= c_t0_t5101

	c_t0_t5101_mem1 = S.Task('c_t0_t5101_mem1', length=1, delay_cost=1)
	c_t0_t5101_mem1 += INPUT_mem_r
	S += c_t0_t5101_mem1 <= c_t0_t5101

	c_t0_t5110 = S.Task('c_t0_t5110', length=1, delay_cost=1)
	c_t0_t5110 += alt(ADD)

	c_t0_t5110_mem0 = S.Task('c_t0_t5110_mem0', length=1, delay_cost=1)
	c_t0_t5110_mem0 += INPUT_mem_r
	S += c_t0_t5110_mem0 <= c_t0_t5110

	c_t0_t5110_mem1 = S.Task('c_t0_t5110_mem1', length=1, delay_cost=1)
	c_t0_t5110_mem1 += INPUT_mem_r
	S += c_t0_t5110_mem1 <= c_t0_t5110

	c_t0_t5111 = S.Task('c_t0_t5111', length=1, delay_cost=1)
	c_t0_t5111 += alt(ADD)

	c_t0_t5111_mem0 = S.Task('c_t0_t5111_mem0', length=1, delay_cost=1)
	c_t0_t5111_mem0 += INPUT_mem_r
	S += c_t0_t5111_mem0 <= c_t0_t5111

	c_t0_t5111_mem1 = S.Task('c_t0_t5111_mem1', length=1, delay_cost=1)
	c_t0_t5111_mem1 += INPUT_mem_r
	S += c_t0_t5111_mem1 <= c_t0_t5111

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls24-559/scheduling/MUL_mul1_add4/MUL_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

