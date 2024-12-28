from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 143
	S = Scenario("PDBL_2", horizon=horizon)

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
	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 0
	t5_t0_t1_in += MUL_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 0
	t5_t0_t1_mem0 += INPUT_mem_r

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 0
	t5_t0_t1_mem1 += INPUT_mem_r

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 1
	t5_t0_t0_in += MUL_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 1
	t5_t0_t0_mem0 += INPUT_mem_r

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 1
	t5_t0_t0_mem1 += INPUT_mem_r

	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	S += t5_t0_t1 >= 1
	t5_t0_t1 += MUL[0]

	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	S += t5_t0_t0 >= 2
	t5_t0_t0 += MUL[0]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 2
	t5_t1_t0_in += MUL_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 2
	t5_t1_t0_mem0 += INPUT_mem_r

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 2
	t5_t1_t0_mem1 += INPUT_mem_r

	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	S += t5_t1_t0 >= 3
	t5_t1_t0 += MUL[0]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 3
	t5_t1_t1_in += MUL_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 3
	t5_t1_t1_mem0 += INPUT_mem_r

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 3
	t5_t1_t1_mem1 += INPUT_mem_r

	t1_t3_t1_in = S.Task('t1_t3_t1_in', length=1, delay_cost=1)
	S += t1_t3_t1_in >= 4
	t1_t3_t1_in += MUL_in[0]

	t1_t3_t1_mem0 = S.Task('t1_t3_t1_mem0', length=1, delay_cost=1)
	S += t1_t3_t1_mem0 >= 4
	t1_t3_t1_mem0 += INPUT_mem_r

	t1_t3_t1_mem1 = S.Task('t1_t3_t1_mem1', length=1, delay_cost=1)
	S += t1_t3_t1_mem1 >= 4
	t1_t3_t1_mem1 += INPUT_mem_r

	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	S += t5_t1_t1 >= 4
	t5_t1_t1 += MUL[0]

	t1_t3_t0_in = S.Task('t1_t3_t0_in', length=1, delay_cost=1)
	S += t1_t3_t0_in >= 5
	t1_t3_t0_in += MUL_in[0]

	t1_t3_t0_mem0 = S.Task('t1_t3_t0_mem0', length=1, delay_cost=1)
	S += t1_t3_t0_mem0 >= 5
	t1_t3_t0_mem0 += INPUT_mem_r

	t1_t3_t0_mem1 = S.Task('t1_t3_t0_mem1', length=1, delay_cost=1)
	S += t1_t3_t0_mem1 >= 5
	t1_t3_t0_mem1 += INPUT_mem_r

	t1_t3_t1 = S.Task('t1_t3_t1', length=7, delay_cost=1)
	S += t1_t3_t1 >= 5
	t1_t3_t1 += MUL[0]

	t0_t3_t1_in = S.Task('t0_t3_t1_in', length=1, delay_cost=1)
	S += t0_t3_t1_in >= 6
	t0_t3_t1_in += MUL_in[0]

	t0_t3_t1_mem0 = S.Task('t0_t3_t1_mem0', length=1, delay_cost=1)
	S += t0_t3_t1_mem0 >= 6
	t0_t3_t1_mem0 += INPUT_mem_r

	t0_t3_t1_mem1 = S.Task('t0_t3_t1_mem1', length=1, delay_cost=1)
	S += t0_t3_t1_mem1 >= 6
	t0_t3_t1_mem1 += INPUT_mem_r

	t1_t3_t0 = S.Task('t1_t3_t0', length=7, delay_cost=1)
	S += t1_t3_t0 >= 6
	t1_t3_t0 += MUL[0]

	t0_t3_t0_in = S.Task('t0_t3_t0_in', length=1, delay_cost=1)
	S += t0_t3_t0_in >= 7
	t0_t3_t0_in += MUL_in[0]

	t0_t3_t0_mem0 = S.Task('t0_t3_t0_mem0', length=1, delay_cost=1)
	S += t0_t3_t0_mem0 >= 7
	t0_t3_t0_mem0 += INPUT_mem_r

	t0_t3_t0_mem1 = S.Task('t0_t3_t0_mem1', length=1, delay_cost=1)
	S += t0_t3_t0_mem1 >= 7
	t0_t3_t0_mem1 += INPUT_mem_r

	t0_t3_t1 = S.Task('t0_t3_t1', length=7, delay_cost=1)
	S += t0_t3_t1 >= 7
	t0_t3_t1 += MUL[0]

	t0_t3_t0 = S.Task('t0_t3_t0', length=7, delay_cost=1)
	S += t0_t3_t0 >= 8
	t0_t3_t0 += MUL[0]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 8
	t5_t1_t3_mem0 += INPUT_mem_r

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 8
	t5_t1_t3_mem1 += INPUT_mem_r

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	S += t5_t1_t3 >= 9
	t5_t1_t3 += ADD[0]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	S += t5_t20_mem0 >= 9
	t5_t20_mem0 += INPUT_mem_r

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	S += t5_t20_mem1 >= 9
	t5_t20_mem1 += INPUT_mem_r

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 10
	t5_t1_t2_mem0 += INPUT_mem_r

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 10
	t5_t1_t2_mem1 += INPUT_mem_r

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	S += t5_t20 >= 10
	t5_t20 += ADD[1]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 11
	t5_t0_t3_mem0 += INPUT_mem_r

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 11
	t5_t0_t3_mem1 += INPUT_mem_r

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	S += t5_t1_t2 >= 11
	t5_t1_t2 += ADD[0]

	t0_t3_t2_mem0 = S.Task('t0_t3_t2_mem0', length=1, delay_cost=1)
	S += t0_t3_t2_mem0 >= 12
	t0_t3_t2_mem0 += INPUT_mem_r

	t0_t3_t2_mem1 = S.Task('t0_t3_t2_mem1', length=1, delay_cost=1)
	S += t0_t3_t2_mem1 >= 12
	t0_t3_t2_mem1 += INPUT_mem_r

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	S += t5_t0_t3 >= 12
	t5_t0_t3 += ADD[0]

	t0_t3_t2 = S.Task('t0_t3_t2', length=1, delay_cost=1)
	S += t0_t3_t2 >= 13
	t0_t3_t2 += ADD[1]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 13
	t5_t0_t2_mem0 += INPUT_mem_r

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 13
	t5_t0_t2_mem1 += INPUT_mem_r

	t1_a1_0_mem0 = S.Task('t1_a1_0_mem0', length=1, delay_cost=1)
	S += t1_a1_0_mem0 >= 14
	t1_a1_0_mem0 += INPUT_mem_r

	t1_a1_0_mem1 = S.Task('t1_a1_0_mem1', length=1, delay_cost=1)
	S += t1_a1_0_mem1 >= 14
	t1_a1_0_mem1 += INPUT_mem_r

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 14
	t5_t0_t2 += ADD[0]

	t0_t11_mem0 = S.Task('t0_t11_mem0', length=1, delay_cost=1)
	S += t0_t11_mem0 >= 15
	t0_t11_mem0 += INPUT_mem_r

	t0_t11_mem1 = S.Task('t0_t11_mem1', length=1, delay_cost=1)
	S += t0_t11_mem1 >= 15
	t0_t11_mem1 += INPUT_mem_r

	t1_a1_0 = S.Task('t1_a1_0', length=1, delay_cost=1)
	S += t1_a1_0 >= 15
	t1_a1_0 += ADD[3]

	t0_t11 = S.Task('t0_t11', length=1, delay_cost=1)
	S += t0_t11 >= 16
	t0_t11 += ADD[1]

	t2_t20_mem0 = S.Task('t2_t20_mem0', length=1, delay_cost=1)
	S += t2_t20_mem0 >= 16
	t2_t20_mem0 += INPUT_mem_r

	t2_t20_mem1 = S.Task('t2_t20_mem1', length=1, delay_cost=1)
	S += t2_t20_mem1 >= 16
	t2_t20_mem1 += INPUT_mem_r

	t2_t20 = S.Task('t2_t20', length=1, delay_cost=1)
	S += t2_t20 >= 17
	t2_t20 += ADD[0]

	t2_t21_mem0 = S.Task('t2_t21_mem0', length=1, delay_cost=1)
	S += t2_t21_mem0 >= 17
	t2_t21_mem0 += INPUT_mem_r

	t2_t21_mem1 = S.Task('t2_t21_mem1', length=1, delay_cost=1)
	S += t2_t21_mem1 >= 17
	t2_t21_mem1 += INPUT_mem_r

	t0_t3_t3_mem0 = S.Task('t0_t3_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_t3_mem0 >= 18
	t0_t3_t3_mem0 += INPUT_mem_r

	t0_t3_t3_mem1 = S.Task('t0_t3_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_t3_mem1 >= 18
	t0_t3_t3_mem1 += INPUT_mem_r

	t2_t21 = S.Task('t2_t21', length=1, delay_cost=1)
	S += t2_t21 >= 18
	t2_t21 += ADD[2]

	t0_a1_0_mem0 = S.Task('t0_a1_0_mem0', length=1, delay_cost=1)
	S += t0_a1_0_mem0 >= 19
	t0_a1_0_mem0 += INPUT_mem_r

	t0_a1_0_mem1 = S.Task('t0_a1_0_mem1', length=1, delay_cost=1)
	S += t0_a1_0_mem1 >= 19
	t0_a1_0_mem1 += INPUT_mem_r

	t0_t3_t3 = S.Task('t0_t3_t3', length=1, delay_cost=1)
	S += t0_t3_t3 >= 19
	t0_t3_t3 += ADD[3]

	t0_a1_0 = S.Task('t0_a1_0', length=1, delay_cost=1)
	S += t0_a1_0 >= 20
	t0_a1_0 += ADD[0]

	t0_t10_mem0 = S.Task('t0_t10_mem0', length=1, delay_cost=1)
	S += t0_t10_mem0 >= 20
	t0_t10_mem0 += INPUT_mem_r

	t0_t10_mem1 = S.Task('t0_t10_mem1', length=1, delay_cost=1)
	S += t0_t10_mem1 >= 20
	t0_t10_mem1 += INPUT_mem_r

	t0_t10 = S.Task('t0_t10', length=1, delay_cost=1)
	S += t0_t10 >= 21
	t0_t10 += ADD[0]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	S += t5_t21_mem0 >= 21
	t5_t21_mem0 += INPUT_mem_r

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	S += t5_t21_mem1 >= 21
	t5_t21_mem1 += INPUT_mem_r

	t1_a1_1_mem0 = S.Task('t1_a1_1_mem0', length=1, delay_cost=1)
	S += t1_a1_1_mem0 >= 22
	t1_a1_1_mem0 += INPUT_mem_r

	t1_a1_1_mem1 = S.Task('t1_a1_1_mem1', length=1, delay_cost=1)
	S += t1_a1_1_mem1 >= 22
	t1_a1_1_mem1 += INPUT_mem_r

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	S += t5_t21 >= 22
	t5_t21 += ADD[0]

	t1_a1_1 = S.Task('t1_a1_1', length=1, delay_cost=1)
	S += t1_a1_1 >= 23
	t1_a1_1 += ADD[2]

	t1_t10_mem0 = S.Task('t1_t10_mem0', length=1, delay_cost=1)
	S += t1_t10_mem0 >= 23
	t1_t10_mem0 += INPUT_mem_r

	t1_t10_mem1 = S.Task('t1_t10_mem1', length=1, delay_cost=1)
	S += t1_t10_mem1 >= 23
	t1_t10_mem1 += INPUT_mem_r

	t1_t10 = S.Task('t1_t10', length=1, delay_cost=1)
	S += t1_t10 >= 24
	t1_t10 += ADD[0]

	t2_t1_t2_mem0 = S.Task('t2_t1_t2_mem0', length=1, delay_cost=1)
	S += t2_t1_t2_mem0 >= 24
	t2_t1_t2_mem0 += INPUT_mem_r

	t2_t1_t2_mem1 = S.Task('t2_t1_t2_mem1', length=1, delay_cost=1)
	S += t2_t1_t2_mem1 >= 24
	t2_t1_t2_mem1 += INPUT_mem_r

	t0_a1_1_mem0 = S.Task('t0_a1_1_mem0', length=1, delay_cost=1)
	S += t0_a1_1_mem0 >= 25
	t0_a1_1_mem0 += INPUT_mem_r

	t0_a1_1_mem1 = S.Task('t0_a1_1_mem1', length=1, delay_cost=1)
	S += t0_a1_1_mem1 >= 25
	t0_a1_1_mem1 += INPUT_mem_r

	t2_t1_t2 = S.Task('t2_t1_t2', length=1, delay_cost=1)
	S += t2_t1_t2 >= 25
	t2_t1_t2 += ADD[1]

	t0_a1_1 = S.Task('t0_a1_1', length=1, delay_cost=1)
	S += t0_a1_1 >= 26
	t0_a1_1 += ADD[2]

	t2_t0_t2_mem0 = S.Task('t2_t0_t2_mem0', length=1, delay_cost=1)
	S += t2_t0_t2_mem0 >= 26
	t2_t0_t2_mem0 += INPUT_mem_r

	t2_t0_t2_mem1 = S.Task('t2_t0_t2_mem1', length=1, delay_cost=1)
	S += t2_t0_t2_mem1 >= 26
	t2_t0_t2_mem1 += INPUT_mem_r

	t1_t3_t3_mem0 = S.Task('t1_t3_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_t3_mem0 >= 27
	t1_t3_t3_mem0 += INPUT_mem_r

	t1_t3_t3_mem1 = S.Task('t1_t3_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_t3_mem1 >= 27
	t1_t3_t3_mem1 += INPUT_mem_r

	t2_t0_t2 = S.Task('t2_t0_t2', length=1, delay_cost=1)
	S += t2_t0_t2 >= 27
	t2_t0_t2 += ADD[0]

	t1_t3_t2_mem0 = S.Task('t1_t3_t2_mem0', length=1, delay_cost=1)
	S += t1_t3_t2_mem0 >= 28
	t1_t3_t2_mem0 += INPUT_mem_r

	t1_t3_t2_mem1 = S.Task('t1_t3_t2_mem1', length=1, delay_cost=1)
	S += t1_t3_t2_mem1 >= 28
	t1_t3_t2_mem1 += INPUT_mem_r

	t1_t3_t3 = S.Task('t1_t3_t3', length=1, delay_cost=1)
	S += t1_t3_t3 >= 28
	t1_t3_t3 += ADD[0]

	t1_t11_mem0 = S.Task('t1_t11_mem0', length=1, delay_cost=1)
	S += t1_t11_mem0 >= 29
	t1_t11_mem0 += INPUT_mem_r

	t1_t11_mem1 = S.Task('t1_t11_mem1', length=1, delay_cost=1)
	S += t1_t11_mem1 >= 29
	t1_t11_mem1 += INPUT_mem_r

	t1_t3_t2 = S.Task('t1_t3_t2', length=1, delay_cost=1)
	S += t1_t3_t2 >= 29
	t1_t3_t2 += ADD[1]

	t1_t11 = S.Task('t1_t11', length=1, delay_cost=1)
	S += t1_t11 >= 30
	t1_t11 += ADD[0]

	t7_t3_t1_in = S.Task('t7_t3_t1_in', length=1, delay_cost=1)
	S += t7_t3_t1_in >= 30
	t7_t3_t1_in += MUL_in[0]

	t7_t3_t1_mem0 = S.Task('t7_t3_t1_mem0', length=1, delay_cost=1)
	S += t7_t3_t1_mem0 >= 30
	t7_t3_t1_mem0 += INPUT_mem_r

	t7_t3_t1_mem1 = S.Task('t7_t3_t1_mem1', length=1, delay_cost=1)
	S += t7_t3_t1_mem1 >= 30
	t7_t3_t1_mem1 += INPUT_mem_r

	t10_t1_t1_in = S.Task('t10_t1_t1_in', length=1, delay_cost=1)
	S += t10_t1_t1_in >= 31
	t10_t1_t1_in += MUL_in[0]

	t10_t1_t1_mem0 = S.Task('t10_t1_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_t1_mem0 >= 31
	t10_t1_t1_mem0 += INPUT_mem_r

	t10_t1_t1_mem1 = S.Task('t10_t1_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_t1_mem1 >= 31
	t10_t1_t1_mem1 += INPUT_mem_r

	t7_t3_t1 = S.Task('t7_t3_t1', length=7, delay_cost=1)
	S += t7_t3_t1 >= 31
	t7_t3_t1 += MUL[0]

	t10_t1_t1 = S.Task('t10_t1_t1', length=7, delay_cost=1)
	S += t10_t1_t1 >= 32
	t10_t1_t1 += MUL[0]

	t7_t3_t0_in = S.Task('t7_t3_t0_in', length=1, delay_cost=1)
	S += t7_t3_t0_in >= 32
	t7_t3_t0_in += MUL_in[0]

	t7_t3_t0_mem0 = S.Task('t7_t3_t0_mem0', length=1, delay_cost=1)
	S += t7_t3_t0_mem0 >= 32
	t7_t3_t0_mem0 += INPUT_mem_r

	t7_t3_t0_mem1 = S.Task('t7_t3_t0_mem1', length=1, delay_cost=1)
	S += t7_t3_t0_mem1 >= 32
	t7_t3_t0_mem1 += INPUT_mem_r

	t10_t1_t0_in = S.Task('t10_t1_t0_in', length=1, delay_cost=1)
	S += t10_t1_t0_in >= 33
	t10_t1_t0_in += MUL_in[0]

	t10_t1_t0_mem0 = S.Task('t10_t1_t0_mem0', length=1, delay_cost=1)
	S += t10_t1_t0_mem0 >= 33
	t10_t1_t0_mem0 += INPUT_mem_r

	t10_t1_t0_mem1 = S.Task('t10_t1_t0_mem1', length=1, delay_cost=1)
	S += t10_t1_t0_mem1 >= 33
	t10_t1_t0_mem1 += INPUT_mem_r

	t7_t3_t0 = S.Task('t7_t3_t0', length=7, delay_cost=1)
	S += t7_t3_t0 >= 33
	t7_t3_t0 += MUL[0]

	t10_t0_t1_in = S.Task('t10_t0_t1_in', length=1, delay_cost=1)
	S += t10_t0_t1_in >= 34
	t10_t0_t1_in += MUL_in[0]

	t10_t0_t1_mem0 = S.Task('t10_t0_t1_mem0', length=1, delay_cost=1)
	S += t10_t0_t1_mem0 >= 34
	t10_t0_t1_mem0 += INPUT_mem_r

	t10_t0_t1_mem1 = S.Task('t10_t0_t1_mem1', length=1, delay_cost=1)
	S += t10_t0_t1_mem1 >= 34
	t10_t0_t1_mem1 += INPUT_mem_r

	t10_t1_t0 = S.Task('t10_t1_t0', length=7, delay_cost=1)
	S += t10_t1_t0 >= 34
	t10_t1_t0 += MUL[0]

	t10_t0_t0_in = S.Task('t10_t0_t0_in', length=1, delay_cost=1)
	S += t10_t0_t0_in >= 35
	t10_t0_t0_in += MUL_in[0]

	t10_t0_t0_mem0 = S.Task('t10_t0_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_t0_mem0 >= 35
	t10_t0_t0_mem0 += INPUT_mem_r

	t10_t0_t0_mem1 = S.Task('t10_t0_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_t0_mem1 >= 35
	t10_t0_t0_mem1 += INPUT_mem_r

	t10_t0_t1 = S.Task('t10_t0_t1', length=7, delay_cost=1)
	S += t10_t0_t1 >= 35
	t10_t0_t1 += MUL[0]

	t10_t0_t0 = S.Task('t10_t0_t0', length=7, delay_cost=1)
	S += t10_t0_t0 >= 36
	t10_t0_t0 += MUL[0]

	t10_t31_mem0 = S.Task('t10_t31_mem0', length=1, delay_cost=1)
	S += t10_t31_mem0 >= 36
	t10_t31_mem0 += INPUT_mem_r

	t10_t31_mem1 = S.Task('t10_t31_mem1', length=1, delay_cost=1)
	S += t10_t31_mem1 >= 36
	t10_t31_mem1 += INPUT_mem_r

	t10_t30_mem0 = S.Task('t10_t30_mem0', length=1, delay_cost=1)
	S += t10_t30_mem0 >= 37
	t10_t30_mem0 += INPUT_mem_r

	t10_t30_mem1 = S.Task('t10_t30_mem1', length=1, delay_cost=1)
	S += t10_t30_mem1 >= 37
	t10_t30_mem1 += INPUT_mem_r

	t10_t31 = S.Task('t10_t31', length=1, delay_cost=1)
	S += t10_t31 >= 37
	t10_t31 += ADD[0]

	t10_t30 = S.Task('t10_t30', length=1, delay_cost=1)
	S += t10_t30 >= 38
	t10_t30 += ADD[2]

	t7_a1_0_mem0 = S.Task('t7_a1_0_mem0', length=1, delay_cost=1)
	S += t7_a1_0_mem0 >= 38
	t7_a1_0_mem0 += INPUT_mem_r

	t7_a1_0_mem1 = S.Task('t7_a1_0_mem1', length=1, delay_cost=1)
	S += t7_a1_0_mem1 >= 38
	t7_a1_0_mem1 += INPUT_mem_r

	t10_t21_mem0 = S.Task('t10_t21_mem0', length=1, delay_cost=1)
	S += t10_t21_mem0 >= 39
	t10_t21_mem0 += INPUT_mem_r

	t10_t21_mem1 = S.Task('t10_t21_mem1', length=1, delay_cost=1)
	S += t10_t21_mem1 >= 39
	t10_t21_mem1 += INPUT_mem_r

	t7_a1_0 = S.Task('t7_a1_0', length=1, delay_cost=1)
	S += t7_a1_0 >= 39
	t7_a1_0 += ADD[0]

	t10_t20_mem0 = S.Task('t10_t20_mem0', length=1, delay_cost=1)
	S += t10_t20_mem0 >= 40
	t10_t20_mem0 += INPUT_mem_r

	t10_t20_mem1 = S.Task('t10_t20_mem1', length=1, delay_cost=1)
	S += t10_t20_mem1 >= 40
	t10_t20_mem1 += INPUT_mem_r

	t10_t21 = S.Task('t10_t21', length=1, delay_cost=1)
	S += t10_t21 >= 40
	t10_t21 += ADD[3]

	t10_t20 = S.Task('t10_t20', length=1, delay_cost=1)
	S += t10_t20 >= 41
	t10_t20 += ADD[3]

	t5_t31_mem0 = S.Task('t5_t31_mem0', length=1, delay_cost=1)
	S += t5_t31_mem0 >= 41
	t5_t31_mem0 += INPUT_mem_r

	t5_t31_mem1 = S.Task('t5_t31_mem1', length=1, delay_cost=1)
	S += t5_t31_mem1 >= 41
	t5_t31_mem1 += INPUT_mem_r

	t5_t31 = S.Task('t5_t31', length=1, delay_cost=1)
	S += t5_t31 >= 42
	t5_t31 += ADD[2]

	t7_t10_mem0 = S.Task('t7_t10_mem0', length=1, delay_cost=1)
	S += t7_t10_mem0 >= 42
	t7_t10_mem0 += INPUT_mem_r

	t7_t10_mem1 = S.Task('t7_t10_mem1', length=1, delay_cost=1)
	S += t7_t10_mem1 >= 42
	t7_t10_mem1 += INPUT_mem_r

	t7_t10 = S.Task('t7_t10', length=1, delay_cost=1)
	S += t7_t10 >= 43
	t7_t10 += ADD[0]

	t7_t3_t2_mem0 = S.Task('t7_t3_t2_mem0', length=1, delay_cost=1)
	S += t7_t3_t2_mem0 >= 43
	t7_t3_t2_mem0 += INPUT_mem_r

	t7_t3_t2_mem1 = S.Task('t7_t3_t2_mem1', length=1, delay_cost=1)
	S += t7_t3_t2_mem1 >= 43
	t7_t3_t2_mem1 += INPUT_mem_r

	t7_t11_mem0 = S.Task('t7_t11_mem0', length=1, delay_cost=1)
	S += t7_t11_mem0 >= 44
	t7_t11_mem0 += INPUT_mem_r

	t7_t11_mem1 = S.Task('t7_t11_mem1', length=1, delay_cost=1)
	S += t7_t11_mem1 >= 44
	t7_t11_mem1 += INPUT_mem_r

	t7_t3_t2 = S.Task('t7_t3_t2', length=1, delay_cost=1)
	S += t7_t3_t2 >= 44
	t7_t3_t2 += ADD[1]

	t7_a1_1_mem0 = S.Task('t7_a1_1_mem0', length=1, delay_cost=1)
	S += t7_a1_1_mem0 >= 45
	t7_a1_1_mem0 += INPUT_mem_r

	t7_a1_1_mem1 = S.Task('t7_a1_1_mem1', length=1, delay_cost=1)
	S += t7_a1_1_mem1 >= 45
	t7_a1_1_mem1 += INPUT_mem_r

	t7_t11 = S.Task('t7_t11', length=1, delay_cost=1)
	S += t7_t11 >= 45
	t7_t11 += ADD[3]

	t10_t1_t3_mem0 = S.Task('t10_t1_t3_mem0', length=1, delay_cost=1)
	S += t10_t1_t3_mem0 >= 46
	t10_t1_t3_mem0 += INPUT_mem_r

	t10_t1_t3_mem1 = S.Task('t10_t1_t3_mem1', length=1, delay_cost=1)
	S += t10_t1_t3_mem1 >= 46
	t10_t1_t3_mem1 += INPUT_mem_r

	t7_a1_1 = S.Task('t7_a1_1', length=1, delay_cost=1)
	S += t7_a1_1 >= 46
	t7_a1_1 += ADD[1]

	t10_t1_t3 = S.Task('t10_t1_t3', length=1, delay_cost=1)
	S += t10_t1_t3 >= 47
	t10_t1_t3 += ADD[1]

	t5_t30_mem0 = S.Task('t5_t30_mem0', length=1, delay_cost=1)
	S += t5_t30_mem0 >= 47
	t5_t30_mem0 += INPUT_mem_r

	t5_t30_mem1 = S.Task('t5_t30_mem1', length=1, delay_cost=1)
	S += t5_t30_mem1 >= 47
	t5_t30_mem1 += INPUT_mem_r

	t10_t1_t2_mem0 = S.Task('t10_t1_t2_mem0', length=1, delay_cost=1)
	S += t10_t1_t2_mem0 >= 48
	t10_t1_t2_mem0 += INPUT_mem_r

	t10_t1_t2_mem1 = S.Task('t10_t1_t2_mem1', length=1, delay_cost=1)
	S += t10_t1_t2_mem1 >= 48
	t10_t1_t2_mem1 += INPUT_mem_r

	t5_t30 = S.Task('t5_t30', length=1, delay_cost=1)
	S += t5_t30 >= 48
	t5_t30 += ADD[0]

	t10_t0_t3_mem0 = S.Task('t10_t0_t3_mem0', length=1, delay_cost=1)
	S += t10_t0_t3_mem0 >= 49
	t10_t0_t3_mem0 += INPUT_mem_r

	t10_t0_t3_mem1 = S.Task('t10_t0_t3_mem1', length=1, delay_cost=1)
	S += t10_t0_t3_mem1 >= 49
	t10_t0_t3_mem1 += INPUT_mem_r

	t10_t1_t2 = S.Task('t10_t1_t2', length=1, delay_cost=1)
	S += t10_t1_t2 >= 49
	t10_t1_t2 += ADD[1]

	t10_t0_t2_mem0 = S.Task('t10_t0_t2_mem0', length=1, delay_cost=1)
	S += t10_t0_t2_mem0 >= 50
	t10_t0_t2_mem0 += INPUT_mem_r

	t10_t0_t2_mem1 = S.Task('t10_t0_t2_mem1', length=1, delay_cost=1)
	S += t10_t0_t2_mem1 >= 50
	t10_t0_t2_mem1 += INPUT_mem_r

	t10_t0_t3 = S.Task('t10_t0_t3', length=1, delay_cost=1)
	S += t10_t0_t3 >= 50
	t10_t0_t3 += ADD[0]

	t10_t0_t2 = S.Task('t10_t0_t2', length=1, delay_cost=1)
	S += t10_t0_t2 >= 51
	t10_t0_t2 += ADD[2]

	t7_t3_t3_mem0 = S.Task('t7_t3_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_t3_mem0 >= 51
	t7_t3_t3_mem0 += INPUT_mem_r

	t7_t3_t3_mem1 = S.Task('t7_t3_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_t3_mem1 >= 51
	t7_t3_t3_mem1 += INPUT_mem_r

	t7_t3_t3 = S.Task('t7_t3_t3', length=1, delay_cost=1)
	S += t7_t3_t3 >= 52
	t7_t3_t3 += ADD[0]


	# new tasks
	t0_t00 = S.Task('t0_t00', length=1, delay_cost=1)
	t0_t00 += alt(ADD)

	t0_t00_mem0 = S.Task('t0_t00_mem0', length=1, delay_cost=1)
	t0_t00_mem0 += INPUT_mem_r
	S += t0_t00_mem0 <= t0_t00

	t0_t00_mem1 = S.Task('t0_t00_mem1', length=1, delay_cost=1)
	t0_t00_mem1 += ADD_mem[0]
	S += 21 < t0_t00_mem1
	S += t0_t00_mem1 <= t0_t00

	t0_t01 = S.Task('t0_t01', length=1, delay_cost=1)
	t0_t01 += alt(ADD)

	t0_t01_mem0 = S.Task('t0_t01_mem0', length=1, delay_cost=1)
	t0_t01_mem0 += INPUT_mem_r
	S += t0_t01_mem0 <= t0_t01

	t0_t01_mem1 = S.Task('t0_t01_mem1', length=1, delay_cost=1)
	t0_t01_mem1 += ADD_mem[2]
	S += 27 < t0_t01_mem1
	S += t0_t01_mem1 <= t0_t01

	t0_t2_t3 = S.Task('t0_t2_t3', length=1, delay_cost=1)
	t0_t2_t3 += alt(ADD)

	t0_t2_t3_mem0 = S.Task('t0_t2_t3_mem0', length=1, delay_cost=1)
	t0_t2_t3_mem0 += ADD_mem[0]
	S += 22 < t0_t2_t3_mem0
	S += t0_t2_t3_mem0 <= t0_t2_t3

	t0_t2_t3_mem1 = S.Task('t0_t2_t3_mem1', length=1, delay_cost=1)
	t0_t2_t3_mem1 += ADD_mem[1]
	S += 17 < t0_t2_t3_mem1
	S += t0_t2_t3_mem1 <= t0_t2_t3

	t0_t3_t4_in = S.Task('t0_t3_t4_in', length=1, delay_cost=1)
	t0_t3_t4_in += alt(MUL_in)
	t0_t3_t4 = S.Task('t0_t3_t4', length=7, delay_cost=1)
	t0_t3_t4 += alt(MUL)
	S += t0_t3_t4>=t0_t3_t4_in

	t0_t3_t4_mem0 = S.Task('t0_t3_t4_mem0', length=1, delay_cost=1)
	t0_t3_t4_mem0 += ADD_mem[1]
	S += 14 < t0_t3_t4_mem0
	S += t0_t3_t4_mem0 <= t0_t3_t4

	t0_t3_t4_mem1 = S.Task('t0_t3_t4_mem1', length=1, delay_cost=1)
	t0_t3_t4_mem1 += ADD_mem[3]
	S += 20 < t0_t3_t4_mem1
	S += t0_t3_t4_mem1 <= t0_t3_t4

	t0_t30 = S.Task('t0_t30', length=1, delay_cost=1)
	t0_t30 += alt(ADD)

	t0_t30_mem0 = S.Task('t0_t30_mem0', length=1, delay_cost=1)
	t0_t30_mem0 += MUL_mem[0]
	S += 15 < t0_t30_mem0
	S += t0_t30_mem0 <= t0_t30

	t0_t30_mem1 = S.Task('t0_t30_mem1', length=1, delay_cost=1)
	t0_t30_mem1 += MUL_mem[0]
	S += 14 < t0_t30_mem1
	S += t0_t30_mem1 <= t0_t30

	t0_t3_t5 = S.Task('t0_t3_t5', length=1, delay_cost=1)
	t0_t3_t5 += alt(ADD)

	t0_t3_t5_mem0 = S.Task('t0_t3_t5_mem0', length=1, delay_cost=1)
	t0_t3_t5_mem0 += MUL_mem[0]
	S += 15 < t0_t3_t5_mem0
	S += t0_t3_t5_mem0 <= t0_t3_t5

	t0_t3_t5_mem1 = S.Task('t0_t3_t5_mem1', length=1, delay_cost=1)
	t0_t3_t5_mem1 += MUL_mem[0]
	S += 14 < t0_t3_t5_mem1
	S += t0_t3_t5_mem1 <= t0_t3_t5

	t1_t00 = S.Task('t1_t00', length=1, delay_cost=1)
	t1_t00 += alt(ADD)

	t1_t00_mem0 = S.Task('t1_t00_mem0', length=1, delay_cost=1)
	t1_t00_mem0 += INPUT_mem_r
	S += t1_t00_mem0 <= t1_t00

	t1_t00_mem1 = S.Task('t1_t00_mem1', length=1, delay_cost=1)
	t1_t00_mem1 += ADD_mem[3]
	S += 16 < t1_t00_mem1
	S += t1_t00_mem1 <= t1_t00

	t1_t01 = S.Task('t1_t01', length=1, delay_cost=1)
	t1_t01 += alt(ADD)

	t1_t01_mem0 = S.Task('t1_t01_mem0', length=1, delay_cost=1)
	t1_t01_mem0 += INPUT_mem_r
	S += t1_t01_mem0 <= t1_t01

	t1_t01_mem1 = S.Task('t1_t01_mem1', length=1, delay_cost=1)
	t1_t01_mem1 += ADD_mem[2]
	S += 24 < t1_t01_mem1
	S += t1_t01_mem1 <= t1_t01

	t1_t2_t3 = S.Task('t1_t2_t3', length=1, delay_cost=1)
	t1_t2_t3 += alt(ADD)

	t1_t2_t3_mem0 = S.Task('t1_t2_t3_mem0', length=1, delay_cost=1)
	t1_t2_t3_mem0 += ADD_mem[0]
	S += 25 < t1_t2_t3_mem0
	S += t1_t2_t3_mem0 <= t1_t2_t3

	t1_t2_t3_mem1 = S.Task('t1_t2_t3_mem1', length=1, delay_cost=1)
	t1_t2_t3_mem1 += ADD_mem[0]
	S += 31 < t1_t2_t3_mem1
	S += t1_t2_t3_mem1 <= t1_t2_t3

	t1_t3_t4_in = S.Task('t1_t3_t4_in', length=1, delay_cost=1)
	t1_t3_t4_in += alt(MUL_in)
	t1_t3_t4 = S.Task('t1_t3_t4', length=7, delay_cost=1)
	t1_t3_t4 += alt(MUL)
	S += t1_t3_t4>=t1_t3_t4_in

	t1_t3_t4_mem0 = S.Task('t1_t3_t4_mem0', length=1, delay_cost=1)
	t1_t3_t4_mem0 += ADD_mem[1]
	S += 30 < t1_t3_t4_mem0
	S += t1_t3_t4_mem0 <= t1_t3_t4

	t1_t3_t4_mem1 = S.Task('t1_t3_t4_mem1', length=1, delay_cost=1)
	t1_t3_t4_mem1 += ADD_mem[0]
	S += 29 < t1_t3_t4_mem1
	S += t1_t3_t4_mem1 <= t1_t3_t4

	t1_t30 = S.Task('t1_t30', length=1, delay_cost=1)
	t1_t30 += alt(ADD)

	t1_t30_mem0 = S.Task('t1_t30_mem0', length=1, delay_cost=1)
	t1_t30_mem0 += MUL_mem[0]
	S += 13 < t1_t30_mem0
	S += t1_t30_mem0 <= t1_t30

	t1_t30_mem1 = S.Task('t1_t30_mem1', length=1, delay_cost=1)
	t1_t30_mem1 += MUL_mem[0]
	S += 12 < t1_t30_mem1
	S += t1_t30_mem1 <= t1_t30

	t1_t3_t5 = S.Task('t1_t3_t5', length=1, delay_cost=1)
	t1_t3_t5 += alt(ADD)

	t1_t3_t5_mem0 = S.Task('t1_t3_t5_mem0', length=1, delay_cost=1)
	t1_t3_t5_mem0 += MUL_mem[0]
	S += 13 < t1_t3_t5_mem0
	S += t1_t3_t5_mem0 <= t1_t3_t5

	t1_t3_t5_mem1 = S.Task('t1_t3_t5_mem1', length=1, delay_cost=1)
	t1_t3_t5_mem1 += MUL_mem[0]
	S += 12 < t1_t3_t5_mem1
	S += t1_t3_t5_mem1 <= t1_t3_t5

	t2_t4_t2 = S.Task('t2_t4_t2', length=1, delay_cost=1)
	t2_t4_t2 += alt(ADD)

	t2_t4_t2_mem0 = S.Task('t2_t4_t2_mem0', length=1, delay_cost=1)
	t2_t4_t2_mem0 += ADD_mem[0]
	S += 18 < t2_t4_t2_mem0
	S += t2_t4_t2_mem0 <= t2_t4_t2

	t2_t4_t2_mem1 = S.Task('t2_t4_t2_mem1', length=1, delay_cost=1)
	t2_t4_t2_mem1 += ADD_mem[2]
	S += 19 < t2_t4_t2_mem1
	S += t2_t4_t2_mem1 <= t2_t4_t2

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	t5_t0_t4_in += alt(MUL_in)
	t5_t0_t4 = S.Task('t5_t0_t4', length=7, delay_cost=1)
	t5_t0_t4 += alt(MUL)
	S += t5_t0_t4>=t5_t0_t4_in

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	t5_t0_t4_mem0 += ADD_mem[0]
	S += 15 < t5_t0_t4_mem0
	S += t5_t0_t4_mem0 <= t5_t0_t4

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	t5_t0_t4_mem1 += ADD_mem[0]
	S += 13 < t5_t0_t4_mem1
	S += t5_t0_t4_mem1 <= t5_t0_t4

	t5_t00 = S.Task('t5_t00', length=1, delay_cost=1)
	t5_t00 += alt(ADD)

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	t5_t00_mem0 += MUL_mem[0]
	S += 9 < t5_t00_mem0
	S += t5_t00_mem0 <= t5_t00

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	t5_t00_mem1 += MUL_mem[0]
	S += 8 < t5_t00_mem1
	S += t5_t00_mem1 <= t5_t00

	t5_t0_t5 = S.Task('t5_t0_t5', length=1, delay_cost=1)
	t5_t0_t5 += alt(ADD)

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	t5_t0_t5_mem0 += MUL_mem[0]
	S += 9 < t5_t0_t5_mem0
	S += t5_t0_t5_mem0 <= t5_t0_t5

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	t5_t0_t5_mem1 += MUL_mem[0]
	S += 8 < t5_t0_t5_mem1
	S += t5_t0_t5_mem1 <= t5_t0_t5

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	t5_t1_t4_in += alt(MUL_in)
	t5_t1_t4 = S.Task('t5_t1_t4', length=7, delay_cost=1)
	t5_t1_t4 += alt(MUL)
	S += t5_t1_t4>=t5_t1_t4_in

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	t5_t1_t4_mem0 += ADD_mem[0]
	S += 12 < t5_t1_t4_mem0
	S += t5_t1_t4_mem0 <= t5_t1_t4

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	t5_t1_t4_mem1 += ADD_mem[0]
	S += 10 < t5_t1_t4_mem1
	S += t5_t1_t4_mem1 <= t5_t1_t4

	t5_t10 = S.Task('t5_t10', length=1, delay_cost=1)
	t5_t10 += alt(ADD)

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	t5_t10_mem0 += MUL_mem[0]
	S += 10 < t5_t10_mem0
	S += t5_t10_mem0 <= t5_t10

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	t5_t10_mem1 += MUL_mem[0]
	S += 11 < t5_t10_mem1
	S += t5_t10_mem1 <= t5_t10

	t5_t1_t5 = S.Task('t5_t1_t5', length=1, delay_cost=1)
	t5_t1_t5 += alt(ADD)

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	t5_t1_t5_mem0 += MUL_mem[0]
	S += 10 < t5_t1_t5_mem0
	S += t5_t1_t5_mem0 <= t5_t1_t5

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	t5_t1_t5_mem1 += MUL_mem[0]
	S += 11 < t5_t1_t5_mem1
	S += t5_t1_t5_mem1 <= t5_t1_t5

	t5_t4_t0_in = S.Task('t5_t4_t0_in', length=1, delay_cost=1)
	t5_t4_t0_in += alt(MUL_in)
	t5_t4_t0 = S.Task('t5_t4_t0', length=7, delay_cost=1)
	t5_t4_t0 += alt(MUL)
	S += t5_t4_t0>=t5_t4_t0_in

	t5_t4_t0_mem0 = S.Task('t5_t4_t0_mem0', length=1, delay_cost=1)
	t5_t4_t0_mem0 += ADD_mem[1]
	S += 11 < t5_t4_t0_mem0
	S += t5_t4_t0_mem0 <= t5_t4_t0

	t5_t4_t0_mem1 = S.Task('t5_t4_t0_mem1', length=1, delay_cost=1)
	t5_t4_t0_mem1 += ADD_mem[0]
	S += 49 < t5_t4_t0_mem1
	S += t5_t4_t0_mem1 <= t5_t4_t0

	t5_t4_t1_in = S.Task('t5_t4_t1_in', length=1, delay_cost=1)
	t5_t4_t1_in += alt(MUL_in)
	t5_t4_t1 = S.Task('t5_t4_t1', length=7, delay_cost=1)
	t5_t4_t1 += alt(MUL)
	S += t5_t4_t1>=t5_t4_t1_in

	t5_t4_t1_mem0 = S.Task('t5_t4_t1_mem0', length=1, delay_cost=1)
	t5_t4_t1_mem0 += ADD_mem[0]
	S += 23 < t5_t4_t1_mem0
	S += t5_t4_t1_mem0 <= t5_t4_t1

	t5_t4_t1_mem1 = S.Task('t5_t4_t1_mem1', length=1, delay_cost=1)
	t5_t4_t1_mem1 += ADD_mem[2]
	S += 43 < t5_t4_t1_mem1
	S += t5_t4_t1_mem1 <= t5_t4_t1

	t5_t4_t2 = S.Task('t5_t4_t2', length=1, delay_cost=1)
	t5_t4_t2 += alt(ADD)

	t5_t4_t2_mem0 = S.Task('t5_t4_t2_mem0', length=1, delay_cost=1)
	t5_t4_t2_mem0 += ADD_mem[1]
	S += 11 < t5_t4_t2_mem0
	S += t5_t4_t2_mem0 <= t5_t4_t2

	t5_t4_t2_mem1 = S.Task('t5_t4_t2_mem1', length=1, delay_cost=1)
	t5_t4_t2_mem1 += ADD_mem[0]
	S += 23 < t5_t4_t2_mem1
	S += t5_t4_t2_mem1 <= t5_t4_t2

	t5_t4_t3 = S.Task('t5_t4_t3', length=1, delay_cost=1)
	t5_t4_t3 += alt(ADD)

	t5_t4_t3_mem0 = S.Task('t5_t4_t3_mem0', length=1, delay_cost=1)
	t5_t4_t3_mem0 += ADD_mem[0]
	S += 49 < t5_t4_t3_mem0
	S += t5_t4_t3_mem0 <= t5_t4_t3

	t5_t4_t3_mem1 = S.Task('t5_t4_t3_mem1', length=1, delay_cost=1)
	t5_t4_t3_mem1 += ADD_mem[2]
	S += 43 < t5_t4_t3_mem1
	S += t5_t4_t3_mem1 <= t5_t4_t3

	t7_t00 = S.Task('t7_t00', length=1, delay_cost=1)
	t7_t00 += alt(ADD)

	t7_t00_mem0 = S.Task('t7_t00_mem0', length=1, delay_cost=1)
	t7_t00_mem0 += INPUT_mem_r
	S += t7_t00_mem0 <= t7_t00

	t7_t00_mem1 = S.Task('t7_t00_mem1', length=1, delay_cost=1)
	t7_t00_mem1 += ADD_mem[0]
	S += 40 < t7_t00_mem1
	S += t7_t00_mem1 <= t7_t00

	t7_t01 = S.Task('t7_t01', length=1, delay_cost=1)
	t7_t01 += alt(ADD)

	t7_t01_mem0 = S.Task('t7_t01_mem0', length=1, delay_cost=1)
	t7_t01_mem0 += INPUT_mem_r
	S += t7_t01_mem0 <= t7_t01

	t7_t01_mem1 = S.Task('t7_t01_mem1', length=1, delay_cost=1)
	t7_t01_mem1 += ADD_mem[1]
	S += 47 < t7_t01_mem1
	S += t7_t01_mem1 <= t7_t01

	t7_t2_t3 = S.Task('t7_t2_t3', length=1, delay_cost=1)
	t7_t2_t3 += alt(ADD)

	t7_t2_t3_mem0 = S.Task('t7_t2_t3_mem0', length=1, delay_cost=1)
	t7_t2_t3_mem0 += ADD_mem[0]
	S += 44 < t7_t2_t3_mem0
	S += t7_t2_t3_mem0 <= t7_t2_t3

	t7_t2_t3_mem1 = S.Task('t7_t2_t3_mem1', length=1, delay_cost=1)
	t7_t2_t3_mem1 += ADD_mem[3]
	S += 46 < t7_t2_t3_mem1
	S += t7_t2_t3_mem1 <= t7_t2_t3

	t7_t3_t4_in = S.Task('t7_t3_t4_in', length=1, delay_cost=1)
	t7_t3_t4_in += alt(MUL_in)
	t7_t3_t4 = S.Task('t7_t3_t4', length=7, delay_cost=1)
	t7_t3_t4 += alt(MUL)
	S += t7_t3_t4>=t7_t3_t4_in

	t7_t3_t4_mem0 = S.Task('t7_t3_t4_mem0', length=1, delay_cost=1)
	t7_t3_t4_mem0 += ADD_mem[1]
	S += 45 < t7_t3_t4_mem0
	S += t7_t3_t4_mem0 <= t7_t3_t4

	t7_t3_t4_mem1 = S.Task('t7_t3_t4_mem1', length=1, delay_cost=1)
	t7_t3_t4_mem1 += ADD_mem[0]
	S += 53 < t7_t3_t4_mem1
	S += t7_t3_t4_mem1 <= t7_t3_t4

	t7_t30 = S.Task('t7_t30', length=1, delay_cost=1)
	t7_t30 += alt(ADD)

	t7_t30_mem0 = S.Task('t7_t30_mem0', length=1, delay_cost=1)
	t7_t30_mem0 += MUL_mem[0]
	S += 40 < t7_t30_mem0
	S += t7_t30_mem0 <= t7_t30

	t7_t30_mem1 = S.Task('t7_t30_mem1', length=1, delay_cost=1)
	t7_t30_mem1 += MUL_mem[0]
	S += 38 < t7_t30_mem1
	S += t7_t30_mem1 <= t7_t30

	t7_t3_t5 = S.Task('t7_t3_t5', length=1, delay_cost=1)
	t7_t3_t5 += alt(ADD)

	t7_t3_t5_mem0 = S.Task('t7_t3_t5_mem0', length=1, delay_cost=1)
	t7_t3_t5_mem0 += MUL_mem[0]
	S += 40 < t7_t3_t5_mem0
	S += t7_t3_t5_mem0 <= t7_t3_t5

	t7_t3_t5_mem1 = S.Task('t7_t3_t5_mem1', length=1, delay_cost=1)
	t7_t3_t5_mem1 += MUL_mem[0]
	S += 38 < t7_t3_t5_mem1
	S += t7_t3_t5_mem1 <= t7_t3_t5

	t10_t0_t4_in = S.Task('t10_t0_t4_in', length=1, delay_cost=1)
	t10_t0_t4_in += alt(MUL_in)
	t10_t0_t4 = S.Task('t10_t0_t4', length=7, delay_cost=1)
	t10_t0_t4 += alt(MUL)
	S += t10_t0_t4>=t10_t0_t4_in

	t10_t0_t4_mem0 = S.Task('t10_t0_t4_mem0', length=1, delay_cost=1)
	t10_t0_t4_mem0 += ADD_mem[2]
	S += 52 < t10_t0_t4_mem0
	S += t10_t0_t4_mem0 <= t10_t0_t4

	t10_t0_t4_mem1 = S.Task('t10_t0_t4_mem1', length=1, delay_cost=1)
	t10_t0_t4_mem1 += ADD_mem[0]
	S += 51 < t10_t0_t4_mem1
	S += t10_t0_t4_mem1 <= t10_t0_t4

	t10_t00 = S.Task('t10_t00', length=1, delay_cost=1)
	t10_t00 += alt(ADD)

	t10_t00_mem0 = S.Task('t10_t00_mem0', length=1, delay_cost=1)
	t10_t00_mem0 += MUL_mem[0]
	S += 43 < t10_t00_mem0
	S += t10_t00_mem0 <= t10_t00

	t10_t00_mem1 = S.Task('t10_t00_mem1', length=1, delay_cost=1)
	t10_t00_mem1 += MUL_mem[0]
	S += 42 < t10_t00_mem1
	S += t10_t00_mem1 <= t10_t00

	t10_t0_t5 = S.Task('t10_t0_t5', length=1, delay_cost=1)
	t10_t0_t5 += alt(ADD)

	t10_t0_t5_mem0 = S.Task('t10_t0_t5_mem0', length=1, delay_cost=1)
	t10_t0_t5_mem0 += MUL_mem[0]
	S += 43 < t10_t0_t5_mem0
	S += t10_t0_t5_mem0 <= t10_t0_t5

	t10_t0_t5_mem1 = S.Task('t10_t0_t5_mem1', length=1, delay_cost=1)
	t10_t0_t5_mem1 += MUL_mem[0]
	S += 42 < t10_t0_t5_mem1
	S += t10_t0_t5_mem1 <= t10_t0_t5

	t10_t1_t4_in = S.Task('t10_t1_t4_in', length=1, delay_cost=1)
	t10_t1_t4_in += alt(MUL_in)
	t10_t1_t4 = S.Task('t10_t1_t4', length=7, delay_cost=1)
	t10_t1_t4 += alt(MUL)
	S += t10_t1_t4>=t10_t1_t4_in

	t10_t1_t4_mem0 = S.Task('t10_t1_t4_mem0', length=1, delay_cost=1)
	t10_t1_t4_mem0 += ADD_mem[1]
	S += 50 < t10_t1_t4_mem0
	S += t10_t1_t4_mem0 <= t10_t1_t4

	t10_t1_t4_mem1 = S.Task('t10_t1_t4_mem1', length=1, delay_cost=1)
	t10_t1_t4_mem1 += ADD_mem[1]
	S += 48 < t10_t1_t4_mem1
	S += t10_t1_t4_mem1 <= t10_t1_t4

	t10_t10 = S.Task('t10_t10', length=1, delay_cost=1)
	t10_t10 += alt(ADD)

	t10_t10_mem0 = S.Task('t10_t10_mem0', length=1, delay_cost=1)
	t10_t10_mem0 += MUL_mem[0]
	S += 41 < t10_t10_mem0
	S += t10_t10_mem0 <= t10_t10

	t10_t10_mem1 = S.Task('t10_t10_mem1', length=1, delay_cost=1)
	t10_t10_mem1 += MUL_mem[0]
	S += 39 < t10_t10_mem1
	S += t10_t10_mem1 <= t10_t10

	t10_t1_t5 = S.Task('t10_t1_t5', length=1, delay_cost=1)
	t10_t1_t5 += alt(ADD)

	t10_t1_t5_mem0 = S.Task('t10_t1_t5_mem0', length=1, delay_cost=1)
	t10_t1_t5_mem0 += MUL_mem[0]
	S += 41 < t10_t1_t5_mem0
	S += t10_t1_t5_mem0 <= t10_t1_t5

	t10_t1_t5_mem1 = S.Task('t10_t1_t5_mem1', length=1, delay_cost=1)
	t10_t1_t5_mem1 += MUL_mem[0]
	S += 39 < t10_t1_t5_mem1
	S += t10_t1_t5_mem1 <= t10_t1_t5

	t10_t4_t0_in = S.Task('t10_t4_t0_in', length=1, delay_cost=1)
	t10_t4_t0_in += alt(MUL_in)
	t10_t4_t0 = S.Task('t10_t4_t0', length=7, delay_cost=1)
	t10_t4_t0 += alt(MUL)
	S += t10_t4_t0>=t10_t4_t0_in

	t10_t4_t0_mem0 = S.Task('t10_t4_t0_mem0', length=1, delay_cost=1)
	t10_t4_t0_mem0 += ADD_mem[3]
	S += 42 < t10_t4_t0_mem0
	S += t10_t4_t0_mem0 <= t10_t4_t0

	t10_t4_t0_mem1 = S.Task('t10_t4_t0_mem1', length=1, delay_cost=1)
	t10_t4_t0_mem1 += ADD_mem[2]
	S += 39 < t10_t4_t0_mem1
	S += t10_t4_t0_mem1 <= t10_t4_t0

	t10_t4_t1_in = S.Task('t10_t4_t1_in', length=1, delay_cost=1)
	t10_t4_t1_in += alt(MUL_in)
	t10_t4_t1 = S.Task('t10_t4_t1', length=7, delay_cost=1)
	t10_t4_t1 += alt(MUL)
	S += t10_t4_t1>=t10_t4_t1_in

	t10_t4_t1_mem0 = S.Task('t10_t4_t1_mem0', length=1, delay_cost=1)
	t10_t4_t1_mem0 += ADD_mem[3]
	S += 41 < t10_t4_t1_mem0
	S += t10_t4_t1_mem0 <= t10_t4_t1

	t10_t4_t1_mem1 = S.Task('t10_t4_t1_mem1', length=1, delay_cost=1)
	t10_t4_t1_mem1 += ADD_mem[0]
	S += 38 < t10_t4_t1_mem1
	S += t10_t4_t1_mem1 <= t10_t4_t1

	t10_t4_t2 = S.Task('t10_t4_t2', length=1, delay_cost=1)
	t10_t4_t2 += alt(ADD)

	t10_t4_t2_mem0 = S.Task('t10_t4_t2_mem0', length=1, delay_cost=1)
	t10_t4_t2_mem0 += ADD_mem[3]
	S += 42 < t10_t4_t2_mem0
	S += t10_t4_t2_mem0 <= t10_t4_t2

	t10_t4_t2_mem1 = S.Task('t10_t4_t2_mem1', length=1, delay_cost=1)
	t10_t4_t2_mem1 += ADD_mem[3]
	S += 41 < t10_t4_t2_mem1
	S += t10_t4_t2_mem1 <= t10_t4_t2

	t10_t4_t3 = S.Task('t10_t4_t3', length=1, delay_cost=1)
	t10_t4_t3 += alt(ADD)

	t10_t4_t3_mem0 = S.Task('t10_t4_t3_mem0', length=1, delay_cost=1)
	t10_t4_t3_mem0 += ADD_mem[2]
	S += 39 < t10_t4_t3_mem0
	S += t10_t4_t3_mem0 <= t10_t4_t3

	t10_t4_t3_mem1 = S.Task('t10_t4_t3_mem1', length=1, delay_cost=1)
	t10_t4_t3_mem1 += ADD_mem[0]
	S += 38 < t10_t4_t3_mem1
	S += t10_t4_t3_mem1 <= t10_t4_t3

	t0_t2_t0_in = S.Task('t0_t2_t0_in', length=1, delay_cost=1)
	t0_t2_t0_in += alt(MUL_in)
	t0_t2_t0 = S.Task('t0_t2_t0', length=7, delay_cost=1)
	t0_t2_t0 += alt(MUL)
	S += t0_t2_t0>=t0_t2_t0_in

	t0_t2_t0_mem0 = S.Task('t0_t2_t0_mem0', length=1, delay_cost=1)
	t0_t2_t0_mem0 += alt(ADD_mem)
	S += (t0_t00*ADD[0]) < t0_t2_t0_mem0*ADD_mem[0]
	S += (t0_t00*ADD[1]) < t0_t2_t0_mem0*ADD_mem[1]
	S += (t0_t00*ADD[2]) < t0_t2_t0_mem0*ADD_mem[2]
	S += (t0_t00*ADD[3]) < t0_t2_t0_mem0*ADD_mem[3]
	S += t0_t2_t0_mem0 <= t0_t2_t0

	t0_t2_t0_mem1 = S.Task('t0_t2_t0_mem1', length=1, delay_cost=1)
	t0_t2_t0_mem1 += ADD_mem[0]
	S += 22 < t0_t2_t0_mem1
	S += t0_t2_t0_mem1 <= t0_t2_t0

	t0_t2_t1_in = S.Task('t0_t2_t1_in', length=1, delay_cost=1)
	t0_t2_t1_in += alt(MUL_in)
	t0_t2_t1 = S.Task('t0_t2_t1', length=7, delay_cost=1)
	t0_t2_t1 += alt(MUL)
	S += t0_t2_t1>=t0_t2_t1_in

	t0_t2_t1_mem0 = S.Task('t0_t2_t1_mem0', length=1, delay_cost=1)
	t0_t2_t1_mem0 += alt(ADD_mem)
	S += (t0_t01*ADD[0]) < t0_t2_t1_mem0*ADD_mem[0]
	S += (t0_t01*ADD[1]) < t0_t2_t1_mem0*ADD_mem[1]
	S += (t0_t01*ADD[2]) < t0_t2_t1_mem0*ADD_mem[2]
	S += (t0_t01*ADD[3]) < t0_t2_t1_mem0*ADD_mem[3]
	S += t0_t2_t1_mem0 <= t0_t2_t1

	t0_t2_t1_mem1 = S.Task('t0_t2_t1_mem1', length=1, delay_cost=1)
	t0_t2_t1_mem1 += ADD_mem[1]
	S += 17 < t0_t2_t1_mem1
	S += t0_t2_t1_mem1 <= t0_t2_t1

	t0_t2_t2 = S.Task('t0_t2_t2', length=1, delay_cost=1)
	t0_t2_t2 += alt(ADD)

	t0_t2_t2_mem0 = S.Task('t0_t2_t2_mem0', length=1, delay_cost=1)
	t0_t2_t2_mem0 += alt(ADD_mem)
	S += (t0_t00*ADD[0]) < t0_t2_t2_mem0*ADD_mem[0]
	S += (t0_t00*ADD[1]) < t0_t2_t2_mem0*ADD_mem[1]
	S += (t0_t00*ADD[2]) < t0_t2_t2_mem0*ADD_mem[2]
	S += (t0_t00*ADD[3]) < t0_t2_t2_mem0*ADD_mem[3]
	S += t0_t2_t2_mem0 <= t0_t2_t2

	t0_t2_t2_mem1 = S.Task('t0_t2_t2_mem1', length=1, delay_cost=1)
	t0_t2_t2_mem1 += alt(ADD_mem)
	S += (t0_t01*ADD[0]) < t0_t2_t2_mem1*ADD_mem[0]
	S += (t0_t01*ADD[1]) < t0_t2_t2_mem1*ADD_mem[1]
	S += (t0_t01*ADD[2]) < t0_t2_t2_mem1*ADD_mem[2]
	S += (t0_t01*ADD[3]) < t0_t2_t2_mem1*ADD_mem[3]
	S += t0_t2_t2_mem1 <= t0_t2_t2

	t0_t31 = S.Task('t0_t31', length=1, delay_cost=1)
	t0_t31 += alt(ADD)

	t0_t31_mem0 = S.Task('t0_t31_mem0', length=1, delay_cost=1)
	t0_t31_mem0 += alt(MUL_mem)
	S += (t0_t3_t4*MUL[0]) < t0_t31_mem0*MUL_mem[0]
	S += t0_t31_mem0 <= t0_t31

	t0_t31_mem1 = S.Task('t0_t31_mem1', length=1, delay_cost=1)
	t0_t31_mem1 += alt(ADD_mem)
	S += (t0_t3_t5*ADD[0]) < t0_t31_mem1*ADD_mem[0]
	S += (t0_t3_t5*ADD[1]) < t0_t31_mem1*ADD_mem[1]
	S += (t0_t3_t5*ADD[2]) < t0_t31_mem1*ADD_mem[2]
	S += (t0_t3_t5*ADD[3]) < t0_t31_mem1*ADD_mem[3]
	S += t0_t31_mem1 <= t0_t31

	t010 = S.Task('t010', length=1, delay_cost=1)
	t010 += alt(ADD)

	t010_mem0 = S.Task('t010_mem0', length=1, delay_cost=1)
	t010_mem0 += alt(ADD_mem)
	S += (t0_t30*ADD[0]) < t010_mem0*ADD_mem[0]
	S += (t0_t30*ADD[1]) < t010_mem0*ADD_mem[1]
	S += (t0_t30*ADD[2]) < t010_mem0*ADD_mem[2]
	S += (t0_t30*ADD[3]) < t010_mem0*ADD_mem[3]
	S += t010_mem0 <= t010

	t1_t2_t0_in = S.Task('t1_t2_t0_in', length=1, delay_cost=1)
	t1_t2_t0_in += alt(MUL_in)
	t1_t2_t0 = S.Task('t1_t2_t0', length=7, delay_cost=1)
	t1_t2_t0 += alt(MUL)
	S += t1_t2_t0>=t1_t2_t0_in

	t1_t2_t0_mem0 = S.Task('t1_t2_t0_mem0', length=1, delay_cost=1)
	t1_t2_t0_mem0 += alt(ADD_mem)
	S += (t1_t00*ADD[0]) < t1_t2_t0_mem0*ADD_mem[0]
	S += (t1_t00*ADD[1]) < t1_t2_t0_mem0*ADD_mem[1]
	S += (t1_t00*ADD[2]) < t1_t2_t0_mem0*ADD_mem[2]
	S += (t1_t00*ADD[3]) < t1_t2_t0_mem0*ADD_mem[3]
	S += t1_t2_t0_mem0 <= t1_t2_t0

	t1_t2_t0_mem1 = S.Task('t1_t2_t0_mem1', length=1, delay_cost=1)
	t1_t2_t0_mem1 += ADD_mem[0]
	S += 25 < t1_t2_t0_mem1
	S += t1_t2_t0_mem1 <= t1_t2_t0

	t1_t2_t1_in = S.Task('t1_t2_t1_in', length=1, delay_cost=1)
	t1_t2_t1_in += alt(MUL_in)
	t1_t2_t1 = S.Task('t1_t2_t1', length=7, delay_cost=1)
	t1_t2_t1 += alt(MUL)
	S += t1_t2_t1>=t1_t2_t1_in

	t1_t2_t1_mem0 = S.Task('t1_t2_t1_mem0', length=1, delay_cost=1)
	t1_t2_t1_mem0 += alt(ADD_mem)
	S += (t1_t01*ADD[0]) < t1_t2_t1_mem0*ADD_mem[0]
	S += (t1_t01*ADD[1]) < t1_t2_t1_mem0*ADD_mem[1]
	S += (t1_t01*ADD[2]) < t1_t2_t1_mem0*ADD_mem[2]
	S += (t1_t01*ADD[3]) < t1_t2_t1_mem0*ADD_mem[3]
	S += t1_t2_t1_mem0 <= t1_t2_t1

	t1_t2_t1_mem1 = S.Task('t1_t2_t1_mem1', length=1, delay_cost=1)
	t1_t2_t1_mem1 += ADD_mem[0]
	S += 31 < t1_t2_t1_mem1
	S += t1_t2_t1_mem1 <= t1_t2_t1

	t1_t2_t2 = S.Task('t1_t2_t2', length=1, delay_cost=1)
	t1_t2_t2 += alt(ADD)

	t1_t2_t2_mem0 = S.Task('t1_t2_t2_mem0', length=1, delay_cost=1)
	t1_t2_t2_mem0 += alt(ADD_mem)
	S += (t1_t00*ADD[0]) < t1_t2_t2_mem0*ADD_mem[0]
	S += (t1_t00*ADD[1]) < t1_t2_t2_mem0*ADD_mem[1]
	S += (t1_t00*ADD[2]) < t1_t2_t2_mem0*ADD_mem[2]
	S += (t1_t00*ADD[3]) < t1_t2_t2_mem0*ADD_mem[3]
	S += t1_t2_t2_mem0 <= t1_t2_t2

	t1_t2_t2_mem1 = S.Task('t1_t2_t2_mem1', length=1, delay_cost=1)
	t1_t2_t2_mem1 += alt(ADD_mem)
	S += (t1_t01*ADD[0]) < t1_t2_t2_mem1*ADD_mem[0]
	S += (t1_t01*ADD[1]) < t1_t2_t2_mem1*ADD_mem[1]
	S += (t1_t01*ADD[2]) < t1_t2_t2_mem1*ADD_mem[2]
	S += (t1_t01*ADD[3]) < t1_t2_t2_mem1*ADD_mem[3]
	S += t1_t2_t2_mem1 <= t1_t2_t2

	t1_t31 = S.Task('t1_t31', length=1, delay_cost=1)
	t1_t31 += alt(ADD)

	t1_t31_mem0 = S.Task('t1_t31_mem0', length=1, delay_cost=1)
	t1_t31_mem0 += alt(MUL_mem)
	S += (t1_t3_t4*MUL[0]) < t1_t31_mem0*MUL_mem[0]
	S += t1_t31_mem0 <= t1_t31

	t1_t31_mem1 = S.Task('t1_t31_mem1', length=1, delay_cost=1)
	t1_t31_mem1 += alt(ADD_mem)
	S += (t1_t3_t5*ADD[0]) < t1_t31_mem1*ADD_mem[0]
	S += (t1_t3_t5*ADD[1]) < t1_t31_mem1*ADD_mem[1]
	S += (t1_t3_t5*ADD[2]) < t1_t31_mem1*ADD_mem[2]
	S += (t1_t3_t5*ADD[3]) < t1_t31_mem1*ADD_mem[3]
	S += t1_t31_mem1 <= t1_t31

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(ADD)

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(ADD_mem)
	S += (t1_t30*ADD[0]) < t110_mem0*ADD_mem[0]
	S += (t1_t30*ADD[1]) < t110_mem0*ADD_mem[1]
	S += (t1_t30*ADD[2]) < t110_mem0*ADD_mem[2]
	S += (t1_t30*ADD[3]) < t110_mem0*ADD_mem[3]
	S += t110_mem0 <= t110

	t5_t01 = S.Task('t5_t01', length=1, delay_cost=1)
	t5_t01 += alt(ADD)

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	t5_t01_mem0 += alt(MUL_mem)
	S += (t5_t0_t4*MUL[0]) < t5_t01_mem0*MUL_mem[0]
	S += t5_t01_mem0 <= t5_t01

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	t5_t01_mem1 += alt(ADD_mem)
	S += (t5_t0_t5*ADD[0]) < t5_t01_mem1*ADD_mem[0]
	S += (t5_t0_t5*ADD[1]) < t5_t01_mem1*ADD_mem[1]
	S += (t5_t0_t5*ADD[2]) < t5_t01_mem1*ADD_mem[2]
	S += (t5_t0_t5*ADD[3]) < t5_t01_mem1*ADD_mem[3]
	S += t5_t01_mem1 <= t5_t01

	t5_t11 = S.Task('t5_t11', length=1, delay_cost=1)
	t5_t11 += alt(ADD)

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	t5_t11_mem0 += alt(MUL_mem)
	S += (t5_t1_t4*MUL[0]) < t5_t11_mem0*MUL_mem[0]
	S += t5_t11_mem0 <= t5_t11

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	t5_t11_mem1 += alt(ADD_mem)
	S += (t5_t1_t5*ADD[0]) < t5_t11_mem1*ADD_mem[0]
	S += (t5_t1_t5*ADD[1]) < t5_t11_mem1*ADD_mem[1]
	S += (t5_t1_t5*ADD[2]) < t5_t11_mem1*ADD_mem[2]
	S += (t5_t1_t5*ADD[3]) < t5_t11_mem1*ADD_mem[3]
	S += t5_t11_mem1 <= t5_t11

	t5_t4_t4_in = S.Task('t5_t4_t4_in', length=1, delay_cost=1)
	t5_t4_t4_in += alt(MUL_in)
	t5_t4_t4 = S.Task('t5_t4_t4', length=7, delay_cost=1)
	t5_t4_t4 += alt(MUL)
	S += t5_t4_t4>=t5_t4_t4_in

	t5_t4_t4_mem0 = S.Task('t5_t4_t4_mem0', length=1, delay_cost=1)
	t5_t4_t4_mem0 += alt(ADD_mem)
	S += (t5_t4_t2*ADD[0]) < t5_t4_t4_mem0*ADD_mem[0]
	S += (t5_t4_t2*ADD[1]) < t5_t4_t4_mem0*ADD_mem[1]
	S += (t5_t4_t2*ADD[2]) < t5_t4_t4_mem0*ADD_mem[2]
	S += (t5_t4_t2*ADD[3]) < t5_t4_t4_mem0*ADD_mem[3]
	S += t5_t4_t4_mem0 <= t5_t4_t4

	t5_t4_t4_mem1 = S.Task('t5_t4_t4_mem1', length=1, delay_cost=1)
	t5_t4_t4_mem1 += alt(ADD_mem)
	S += (t5_t4_t3*ADD[0]) < t5_t4_t4_mem1*ADD_mem[0]
	S += (t5_t4_t3*ADD[1]) < t5_t4_t4_mem1*ADD_mem[1]
	S += (t5_t4_t3*ADD[2]) < t5_t4_t4_mem1*ADD_mem[2]
	S += (t5_t4_t3*ADD[3]) < t5_t4_t4_mem1*ADD_mem[3]
	S += t5_t4_t4_mem1 <= t5_t4_t4

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	t5_t40 += alt(ADD)

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	t5_t40_mem0 += alt(MUL_mem)
	S += (t5_t4_t0*MUL[0]) < t5_t40_mem0*MUL_mem[0]
	S += t5_t40_mem0 <= t5_t40

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	t5_t40_mem1 += alt(MUL_mem)
	S += (t5_t4_t1*MUL[0]) < t5_t40_mem1*MUL_mem[0]
	S += t5_t40_mem1 <= t5_t40

	t5_t4_t5 = S.Task('t5_t4_t5', length=1, delay_cost=1)
	t5_t4_t5 += alt(ADD)

	t5_t4_t5_mem0 = S.Task('t5_t4_t5_mem0', length=1, delay_cost=1)
	t5_t4_t5_mem0 += alt(MUL_mem)
	S += (t5_t4_t0*MUL[0]) < t5_t4_t5_mem0*MUL_mem[0]
	S += t5_t4_t5_mem0 <= t5_t4_t5

	t5_t4_t5_mem1 = S.Task('t5_t4_t5_mem1', length=1, delay_cost=1)
	t5_t4_t5_mem1 += alt(MUL_mem)
	S += (t5_t4_t1*MUL[0]) < t5_t4_t5_mem1*MUL_mem[0]
	S += t5_t4_t5_mem1 <= t5_t4_t5

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	t5_t50 += alt(ADD)

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	t5_t50_mem0 += alt(ADD_mem)
	S += (t5_t00*ADD[0]) < t5_t50_mem0*ADD_mem[0]
	S += (t5_t00*ADD[1]) < t5_t50_mem0*ADD_mem[1]
	S += (t5_t00*ADD[2]) < t5_t50_mem0*ADD_mem[2]
	S += (t5_t00*ADD[3]) < t5_t50_mem0*ADD_mem[3]
	S += t5_t50_mem0 <= t5_t50

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	t5_t50_mem1 += alt(ADD_mem)
	S += (t5_t10*ADD[0]) < t5_t50_mem1*ADD_mem[0]
	S += (t5_t10*ADD[1]) < t5_t50_mem1*ADD_mem[1]
	S += (t5_t10*ADD[2]) < t5_t50_mem1*ADD_mem[2]
	S += (t5_t10*ADD[3]) < t5_t50_mem1*ADD_mem[3]
	S += t5_t50_mem1 <= t5_t50

	t7_t2_t0_in = S.Task('t7_t2_t0_in', length=1, delay_cost=1)
	t7_t2_t0_in += alt(MUL_in)
	t7_t2_t0 = S.Task('t7_t2_t0', length=7, delay_cost=1)
	t7_t2_t0 += alt(MUL)
	S += t7_t2_t0>=t7_t2_t0_in

	t7_t2_t0_mem0 = S.Task('t7_t2_t0_mem0', length=1, delay_cost=1)
	t7_t2_t0_mem0 += alt(ADD_mem)
	S += (t7_t00*ADD[0]) < t7_t2_t0_mem0*ADD_mem[0]
	S += (t7_t00*ADD[1]) < t7_t2_t0_mem0*ADD_mem[1]
	S += (t7_t00*ADD[2]) < t7_t2_t0_mem0*ADD_mem[2]
	S += (t7_t00*ADD[3]) < t7_t2_t0_mem0*ADD_mem[3]
	S += t7_t2_t0_mem0 <= t7_t2_t0

	t7_t2_t0_mem1 = S.Task('t7_t2_t0_mem1', length=1, delay_cost=1)
	t7_t2_t0_mem1 += ADD_mem[0]
	S += 44 < t7_t2_t0_mem1
	S += t7_t2_t0_mem1 <= t7_t2_t0

	t7_t2_t1_in = S.Task('t7_t2_t1_in', length=1, delay_cost=1)
	t7_t2_t1_in += alt(MUL_in)
	t7_t2_t1 = S.Task('t7_t2_t1', length=7, delay_cost=1)
	t7_t2_t1 += alt(MUL)
	S += t7_t2_t1>=t7_t2_t1_in

	t7_t2_t1_mem0 = S.Task('t7_t2_t1_mem0', length=1, delay_cost=1)
	t7_t2_t1_mem0 += alt(ADD_mem)
	S += (t7_t01*ADD[0]) < t7_t2_t1_mem0*ADD_mem[0]
	S += (t7_t01*ADD[1]) < t7_t2_t1_mem0*ADD_mem[1]
	S += (t7_t01*ADD[2]) < t7_t2_t1_mem0*ADD_mem[2]
	S += (t7_t01*ADD[3]) < t7_t2_t1_mem0*ADD_mem[3]
	S += t7_t2_t1_mem0 <= t7_t2_t1

	t7_t2_t1_mem1 = S.Task('t7_t2_t1_mem1', length=1, delay_cost=1)
	t7_t2_t1_mem1 += ADD_mem[3]
	S += 46 < t7_t2_t1_mem1
	S += t7_t2_t1_mem1 <= t7_t2_t1

	t7_t2_t2 = S.Task('t7_t2_t2', length=1, delay_cost=1)
	t7_t2_t2 += alt(ADD)

	t7_t2_t2_mem0 = S.Task('t7_t2_t2_mem0', length=1, delay_cost=1)
	t7_t2_t2_mem0 += alt(ADD_mem)
	S += (t7_t00*ADD[0]) < t7_t2_t2_mem0*ADD_mem[0]
	S += (t7_t00*ADD[1]) < t7_t2_t2_mem0*ADD_mem[1]
	S += (t7_t00*ADD[2]) < t7_t2_t2_mem0*ADD_mem[2]
	S += (t7_t00*ADD[3]) < t7_t2_t2_mem0*ADD_mem[3]
	S += t7_t2_t2_mem0 <= t7_t2_t2

	t7_t2_t2_mem1 = S.Task('t7_t2_t2_mem1', length=1, delay_cost=1)
	t7_t2_t2_mem1 += alt(ADD_mem)
	S += (t7_t01*ADD[0]) < t7_t2_t2_mem1*ADD_mem[0]
	S += (t7_t01*ADD[1]) < t7_t2_t2_mem1*ADD_mem[1]
	S += (t7_t01*ADD[2]) < t7_t2_t2_mem1*ADD_mem[2]
	S += (t7_t01*ADD[3]) < t7_t2_t2_mem1*ADD_mem[3]
	S += t7_t2_t2_mem1 <= t7_t2_t2

	t7_t31 = S.Task('t7_t31', length=1, delay_cost=1)
	t7_t31 += alt(ADD)

	t7_t31_mem0 = S.Task('t7_t31_mem0', length=1, delay_cost=1)
	t7_t31_mem0 += alt(MUL_mem)
	S += (t7_t3_t4*MUL[0]) < t7_t31_mem0*MUL_mem[0]
	S += t7_t31_mem0 <= t7_t31

	t7_t31_mem1 = S.Task('t7_t31_mem1', length=1, delay_cost=1)
	t7_t31_mem1 += alt(ADD_mem)
	S += (t7_t3_t5*ADD[0]) < t7_t31_mem1*ADD_mem[0]
	S += (t7_t3_t5*ADD[1]) < t7_t31_mem1*ADD_mem[1]
	S += (t7_t3_t5*ADD[2]) < t7_t31_mem1*ADD_mem[2]
	S += (t7_t3_t5*ADD[3]) < t7_t31_mem1*ADD_mem[3]
	S += t7_t31_mem1 <= t7_t31

	t710 = S.Task('t710', length=1, delay_cost=1)
	t710 += alt(ADD)

	t710_mem0 = S.Task('t710_mem0', length=1, delay_cost=1)
	t710_mem0 += alt(ADD_mem)
	S += (t7_t30*ADD[0]) < t710_mem0*ADD_mem[0]
	S += (t7_t30*ADD[1]) < t710_mem0*ADD_mem[1]
	S += (t7_t30*ADD[2]) < t710_mem0*ADD_mem[2]
	S += (t7_t30*ADD[3]) < t710_mem0*ADD_mem[3]
	S += t710_mem0 <= t710

	t10_t01 = S.Task('t10_t01', length=1, delay_cost=1)
	t10_t01 += alt(ADD)

	t10_t01_mem0 = S.Task('t10_t01_mem0', length=1, delay_cost=1)
	t10_t01_mem0 += alt(MUL_mem)
	S += (t10_t0_t4*MUL[0]) < t10_t01_mem0*MUL_mem[0]
	S += t10_t01_mem0 <= t10_t01

	t10_t01_mem1 = S.Task('t10_t01_mem1', length=1, delay_cost=1)
	t10_t01_mem1 += alt(ADD_mem)
	S += (t10_t0_t5*ADD[0]) < t10_t01_mem1*ADD_mem[0]
	S += (t10_t0_t5*ADD[1]) < t10_t01_mem1*ADD_mem[1]
	S += (t10_t0_t5*ADD[2]) < t10_t01_mem1*ADD_mem[2]
	S += (t10_t0_t5*ADD[3]) < t10_t01_mem1*ADD_mem[3]
	S += t10_t01_mem1 <= t10_t01

	t10_t11 = S.Task('t10_t11', length=1, delay_cost=1)
	t10_t11 += alt(ADD)

	t10_t11_mem0 = S.Task('t10_t11_mem0', length=1, delay_cost=1)
	t10_t11_mem0 += alt(MUL_mem)
	S += (t10_t1_t4*MUL[0]) < t10_t11_mem0*MUL_mem[0]
	S += t10_t11_mem0 <= t10_t11

	t10_t11_mem1 = S.Task('t10_t11_mem1', length=1, delay_cost=1)
	t10_t11_mem1 += alt(ADD_mem)
	S += (t10_t1_t5*ADD[0]) < t10_t11_mem1*ADD_mem[0]
	S += (t10_t1_t5*ADD[1]) < t10_t11_mem1*ADD_mem[1]
	S += (t10_t1_t5*ADD[2]) < t10_t11_mem1*ADD_mem[2]
	S += (t10_t1_t5*ADD[3]) < t10_t11_mem1*ADD_mem[3]
	S += t10_t11_mem1 <= t10_t11

	t10_t4_t4_in = S.Task('t10_t4_t4_in', length=1, delay_cost=1)
	t10_t4_t4_in += alt(MUL_in)
	t10_t4_t4 = S.Task('t10_t4_t4', length=7, delay_cost=1)
	t10_t4_t4 += alt(MUL)
	S += t10_t4_t4>=t10_t4_t4_in

	t10_t4_t4_mem0 = S.Task('t10_t4_t4_mem0', length=1, delay_cost=1)
	t10_t4_t4_mem0 += alt(ADD_mem)
	S += (t10_t4_t2*ADD[0]) < t10_t4_t4_mem0*ADD_mem[0]
	S += (t10_t4_t2*ADD[1]) < t10_t4_t4_mem0*ADD_mem[1]
	S += (t10_t4_t2*ADD[2]) < t10_t4_t4_mem0*ADD_mem[2]
	S += (t10_t4_t2*ADD[3]) < t10_t4_t4_mem0*ADD_mem[3]
	S += t10_t4_t4_mem0 <= t10_t4_t4

	t10_t4_t4_mem1 = S.Task('t10_t4_t4_mem1', length=1, delay_cost=1)
	t10_t4_t4_mem1 += alt(ADD_mem)
	S += (t10_t4_t3*ADD[0]) < t10_t4_t4_mem1*ADD_mem[0]
	S += (t10_t4_t3*ADD[1]) < t10_t4_t4_mem1*ADD_mem[1]
	S += (t10_t4_t3*ADD[2]) < t10_t4_t4_mem1*ADD_mem[2]
	S += (t10_t4_t3*ADD[3]) < t10_t4_t4_mem1*ADD_mem[3]
	S += t10_t4_t4_mem1 <= t10_t4_t4

	t10_t40 = S.Task('t10_t40', length=1, delay_cost=1)
	t10_t40 += alt(ADD)

	t10_t40_mem0 = S.Task('t10_t40_mem0', length=1, delay_cost=1)
	t10_t40_mem0 += alt(MUL_mem)
	S += (t10_t4_t0*MUL[0]) < t10_t40_mem0*MUL_mem[0]
	S += t10_t40_mem0 <= t10_t40

	t10_t40_mem1 = S.Task('t10_t40_mem1', length=1, delay_cost=1)
	t10_t40_mem1 += alt(MUL_mem)
	S += (t10_t4_t1*MUL[0]) < t10_t40_mem1*MUL_mem[0]
	S += t10_t40_mem1 <= t10_t40

	t10_t4_t5 = S.Task('t10_t4_t5', length=1, delay_cost=1)
	t10_t4_t5 += alt(ADD)

	t10_t4_t5_mem0 = S.Task('t10_t4_t5_mem0', length=1, delay_cost=1)
	t10_t4_t5_mem0 += alt(MUL_mem)
	S += (t10_t4_t0*MUL[0]) < t10_t4_t5_mem0*MUL_mem[0]
	S += t10_t4_t5_mem0 <= t10_t4_t5

	t10_t4_t5_mem1 = S.Task('t10_t4_t5_mem1', length=1, delay_cost=1)
	t10_t4_t5_mem1 += alt(MUL_mem)
	S += (t10_t4_t1*MUL[0]) < t10_t4_t5_mem1*MUL_mem[0]
	S += t10_t4_t5_mem1 <= t10_t4_t5

	t10_t50 = S.Task('t10_t50', length=1, delay_cost=1)
	t10_t50 += alt(ADD)

	t10_t50_mem0 = S.Task('t10_t50_mem0', length=1, delay_cost=1)
	t10_t50_mem0 += alt(ADD_mem)
	S += (t10_t00*ADD[0]) < t10_t50_mem0*ADD_mem[0]
	S += (t10_t00*ADD[1]) < t10_t50_mem0*ADD_mem[1]
	S += (t10_t00*ADD[2]) < t10_t50_mem0*ADD_mem[2]
	S += (t10_t00*ADD[3]) < t10_t50_mem0*ADD_mem[3]
	S += t10_t50_mem0 <= t10_t50

	t10_t50_mem1 = S.Task('t10_t50_mem1', length=1, delay_cost=1)
	t10_t50_mem1 += alt(ADD_mem)
	S += (t10_t10*ADD[0]) < t10_t50_mem1*ADD_mem[0]
	S += (t10_t10*ADD[1]) < t10_t50_mem1*ADD_mem[1]
	S += (t10_t10*ADD[2]) < t10_t50_mem1*ADD_mem[2]
	S += (t10_t10*ADD[3]) < t10_t50_mem1*ADD_mem[3]
	S += t10_t50_mem1 <= t10_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls24-559/scheduling/PDBL_mul1_add4/PDBL_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

