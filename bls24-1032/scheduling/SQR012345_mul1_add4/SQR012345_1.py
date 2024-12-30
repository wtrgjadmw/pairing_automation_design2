from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 130
	S = Scenario("SQR012345_1", horizon=horizon)

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
	t3_t1_t1_in = S.Task('t3_t1_t1_in', length=1, delay_cost=1)
	S += t3_t1_t1_in >= 0
	t3_t1_t1_in += MUL_in[0]

	t3_t1_t1_mem0 = S.Task('t3_t1_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_t1_mem0 >= 0
	t3_t1_t1_mem0 += INPUT_mem_r

	t3_t1_t1_mem1 = S.Task('t3_t1_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_t1_mem1 >= 0
	t3_t1_t1_mem1 += INPUT_mem_r

	t3_t1_t1 = S.Task('t3_t1_t1', length=7, delay_cost=1)
	S += t3_t1_t1 >= 1
	t3_t1_t1 += MUL[0]

	t4_t3_t1_in = S.Task('t4_t3_t1_in', length=1, delay_cost=1)
	S += t4_t3_t1_in >= 1
	t4_t3_t1_in += MUL_in[0]

	t4_t3_t1_mem0 = S.Task('t4_t3_t1_mem0', length=1, delay_cost=1)
	S += t4_t3_t1_mem0 >= 1
	t4_t3_t1_mem0 += INPUT_mem_r

	t4_t3_t1_mem1 = S.Task('t4_t3_t1_mem1', length=1, delay_cost=1)
	S += t4_t3_t1_mem1 >= 1
	t4_t3_t1_mem1 += INPUT_mem_r

	t3_t1_t0_in = S.Task('t3_t1_t0_in', length=1, delay_cost=1)
	S += t3_t1_t0_in >= 2
	t3_t1_t0_in += MUL_in[0]

	t3_t1_t0_mem0 = S.Task('t3_t1_t0_mem0', length=1, delay_cost=1)
	S += t3_t1_t0_mem0 >= 2
	t3_t1_t0_mem0 += INPUT_mem_r

	t3_t1_t0_mem1 = S.Task('t3_t1_t0_mem1', length=1, delay_cost=1)
	S += t3_t1_t0_mem1 >= 2
	t3_t1_t0_mem1 += INPUT_mem_r

	t4_t3_t1 = S.Task('t4_t3_t1', length=7, delay_cost=1)
	S += t4_t3_t1 >= 2
	t4_t3_t1 += MUL[0]

	t3_t1_t0 = S.Task('t3_t1_t0', length=7, delay_cost=1)
	S += t3_t1_t0 >= 3
	t3_t1_t0 += MUL[0]

	t4_t3_t0_in = S.Task('t4_t3_t0_in', length=1, delay_cost=1)
	S += t4_t3_t0_in >= 3
	t4_t3_t0_in += MUL_in[0]

	t4_t3_t0_mem0 = S.Task('t4_t3_t0_mem0', length=1, delay_cost=1)
	S += t4_t3_t0_mem0 >= 3
	t4_t3_t0_mem0 += INPUT_mem_r

	t4_t3_t0_mem1 = S.Task('t4_t3_t0_mem1', length=1, delay_cost=1)
	S += t4_t3_t0_mem1 >= 3
	t4_t3_t0_mem1 += INPUT_mem_r

	t3_t0_t1_in = S.Task('t3_t0_t1_in', length=1, delay_cost=1)
	S += t3_t0_t1_in >= 4
	t3_t0_t1_in += MUL_in[0]

	t3_t0_t1_mem0 = S.Task('t3_t0_t1_mem0', length=1, delay_cost=1)
	S += t3_t0_t1_mem0 >= 4
	t3_t0_t1_mem0 += INPUT_mem_r

	t3_t0_t1_mem1 = S.Task('t3_t0_t1_mem1', length=1, delay_cost=1)
	S += t3_t0_t1_mem1 >= 4
	t3_t0_t1_mem1 += INPUT_mem_r

	t4_t3_t0 = S.Task('t4_t3_t0', length=7, delay_cost=1)
	S += t4_t3_t0 >= 4
	t4_t3_t0 += MUL[0]

	t3_t0_t0_in = S.Task('t3_t0_t0_in', length=1, delay_cost=1)
	S += t3_t0_t0_in >= 5
	t3_t0_t0_in += MUL_in[0]

	t3_t0_t0_mem0 = S.Task('t3_t0_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_t0_mem0 >= 5
	t3_t0_t0_mem0 += INPUT_mem_r

	t3_t0_t0_mem1 = S.Task('t3_t0_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_t0_mem1 >= 5
	t3_t0_t0_mem1 += INPUT_mem_r

	t3_t0_t1 = S.Task('t3_t0_t1', length=7, delay_cost=1)
	S += t3_t0_t1 >= 5
	t3_t0_t1 += MUL[0]

	t0_t3_t1_in = S.Task('t0_t3_t1_in', length=1, delay_cost=1)
	S += t0_t3_t1_in >= 6
	t0_t3_t1_in += MUL_in[0]

	t0_t3_t1_mem0 = S.Task('t0_t3_t1_mem0', length=1, delay_cost=1)
	S += t0_t3_t1_mem0 >= 6
	t0_t3_t1_mem0 += INPUT_mem_r

	t0_t3_t1_mem1 = S.Task('t0_t3_t1_mem1', length=1, delay_cost=1)
	S += t0_t3_t1_mem1 >= 6
	t0_t3_t1_mem1 += INPUT_mem_r

	t3_t0_t0 = S.Task('t3_t0_t0', length=7, delay_cost=1)
	S += t3_t0_t0 >= 6
	t3_t0_t0 += MUL[0]

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

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	S += t4_t11_mem0 >= 8
	t4_t11_mem0 += INPUT_mem_r

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	S += t4_t11_mem1 >= 8
	t4_t11_mem1 += INPUT_mem_r

	t0_t11_mem0 = S.Task('t0_t11_mem0', length=1, delay_cost=1)
	S += t0_t11_mem0 >= 9
	t0_t11_mem0 += INPUT_mem_r

	t0_t11_mem1 = S.Task('t0_t11_mem1', length=1, delay_cost=1)
	S += t0_t11_mem1 >= 9
	t0_t11_mem1 += INPUT_mem_r

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	S += t4_t11 >= 9
	t4_t11 += ADD[0]

	t0_t11 = S.Task('t0_t11', length=1, delay_cost=1)
	S += t0_t11 >= 10
	t0_t11 += ADD[2]

	t0_t3_t3_mem0 = S.Task('t0_t3_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_t3_mem0 >= 10
	t0_t3_t3_mem0 += INPUT_mem_r

	t0_t3_t3_mem1 = S.Task('t0_t3_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_t3_mem1 >= 10
	t0_t3_t3_mem1 += INPUT_mem_r

	t0_t10_mem0 = S.Task('t0_t10_mem0', length=1, delay_cost=1)
	S += t0_t10_mem0 >= 11
	t0_t10_mem0 += INPUT_mem_r

	t0_t10_mem1 = S.Task('t0_t10_mem1', length=1, delay_cost=1)
	S += t0_t10_mem1 >= 11
	t0_t10_mem1 += INPUT_mem_r

	t0_t3_t3 = S.Task('t0_t3_t3', length=1, delay_cost=1)
	S += t0_t3_t3 >= 11
	t0_t3_t3 += ADD[0]

	t0_t10 = S.Task('t0_t10', length=1, delay_cost=1)
	S += t0_t10 >= 12
	t0_t10 += ADD[3]

	t3_t30_mem0 = S.Task('t3_t30_mem0', length=1, delay_cost=1)
	S += t3_t30_mem0 >= 12
	t3_t30_mem0 += INPUT_mem_r

	t3_t30_mem1 = S.Task('t3_t30_mem1', length=1, delay_cost=1)
	S += t3_t30_mem1 >= 12
	t3_t30_mem1 += INPUT_mem_r

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 13
	t100_mem0 += INPUT_mem_r

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 13
	t100_mem1 += INPUT_mem_r

	t3_t30 = S.Task('t3_t30', length=1, delay_cost=1)
	S += t3_t30 >= 13
	t3_t30 += ADD[0]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 14
	t100 += ADD[2]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 14
	t101_mem0 += INPUT_mem_r

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 14
	t101_mem1 += INPUT_mem_r

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 15
	t101 += ADD[3]

	t3_t20_mem0 = S.Task('t3_t20_mem0', length=1, delay_cost=1)
	S += t3_t20_mem0 >= 15
	t3_t20_mem0 += INPUT_mem_r

	t3_t20_mem1 = S.Task('t3_t20_mem1', length=1, delay_cost=1)
	S += t3_t20_mem1 >= 15
	t3_t20_mem1 += INPUT_mem_r

	t0_a1_0_mem0 = S.Task('t0_a1_0_mem0', length=1, delay_cost=1)
	S += t0_a1_0_mem0 >= 16
	t0_a1_0_mem0 += INPUT_mem_r

	t0_a1_0_mem1 = S.Task('t0_a1_0_mem1', length=1, delay_cost=1)
	S += t0_a1_0_mem1 >= 16
	t0_a1_0_mem1 += INPUT_mem_r

	t3_t20 = S.Task('t3_t20', length=1, delay_cost=1)
	S += t3_t20 >= 16
	t3_t20 += ADD[3]

	t0_a1_0 = S.Task('t0_a1_0', length=1, delay_cost=1)
	S += t0_a1_0 >= 17
	t0_a1_0 += ADD[1]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 17
	t4_t10_mem0 += INPUT_mem_r

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 17
	t4_t10_mem1 += INPUT_mem_r

	t3_t21_mem0 = S.Task('t3_t21_mem0', length=1, delay_cost=1)
	S += t3_t21_mem0 >= 18
	t3_t21_mem0 += INPUT_mem_r

	t3_t21_mem1 = S.Task('t3_t21_mem1', length=1, delay_cost=1)
	S += t3_t21_mem1 >= 18
	t3_t21_mem1 += INPUT_mem_r

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	S += t4_t10 >= 18
	t4_t10 += ADD[0]

	t3_t21 = S.Task('t3_t21', length=1, delay_cost=1)
	S += t3_t21 >= 19
	t3_t21 += ADD[0]

	t4_a1_0_mem0 = S.Task('t4_a1_0_mem0', length=1, delay_cost=1)
	S += t4_a1_0_mem0 >= 19
	t4_a1_0_mem0 += INPUT_mem_r

	t4_a1_0_mem1 = S.Task('t4_a1_0_mem1', length=1, delay_cost=1)
	S += t4_a1_0_mem1 >= 19
	t4_a1_0_mem1 += INPUT_mem_r

	t3_t31_mem0 = S.Task('t3_t31_mem0', length=1, delay_cost=1)
	S += t3_t31_mem0 >= 20
	t3_t31_mem0 += INPUT_mem_r

	t3_t31_mem1 = S.Task('t3_t31_mem1', length=1, delay_cost=1)
	S += t3_t31_mem1 >= 20
	t3_t31_mem1 += INPUT_mem_r

	t4_a1_0 = S.Task('t4_a1_0', length=1, delay_cost=1)
	S += t4_a1_0 >= 20
	t4_a1_0 += ADD[3]

	t3_t31 = S.Task('t3_t31', length=1, delay_cost=1)
	S += t3_t31 >= 21
	t3_t31 += ADD[1]

	t4_a1_1_mem0 = S.Task('t4_a1_1_mem0', length=1, delay_cost=1)
	S += t4_a1_1_mem0 >= 21
	t4_a1_1_mem0 += INPUT_mem_r

	t4_a1_1_mem1 = S.Task('t4_a1_1_mem1', length=1, delay_cost=1)
	S += t4_a1_1_mem1 >= 21
	t4_a1_1_mem1 += INPUT_mem_r

	t0_t3_t2_mem0 = S.Task('t0_t3_t2_mem0', length=1, delay_cost=1)
	S += t0_t3_t2_mem0 >= 22
	t0_t3_t2_mem0 += INPUT_mem_r

	t0_t3_t2_mem1 = S.Task('t0_t3_t2_mem1', length=1, delay_cost=1)
	S += t0_t3_t2_mem1 >= 22
	t0_t3_t2_mem1 += INPUT_mem_r

	t4_a1_1 = S.Task('t4_a1_1', length=1, delay_cost=1)
	S += t4_a1_1 >= 22
	t4_a1_1 += ADD[0]

	t0_t3_t2 = S.Task('t0_t3_t2', length=1, delay_cost=1)
	S += t0_t3_t2 >= 23
	t0_t3_t2 += ADD[2]

	t3_t1_t3_mem0 = S.Task('t3_t1_t3_mem0', length=1, delay_cost=1)
	S += t3_t1_t3_mem0 >= 23
	t3_t1_t3_mem0 += INPUT_mem_r

	t3_t1_t3_mem1 = S.Task('t3_t1_t3_mem1', length=1, delay_cost=1)
	S += t3_t1_t3_mem1 >= 23
	t3_t1_t3_mem1 += INPUT_mem_r

	t3_t1_t2_mem0 = S.Task('t3_t1_t2_mem0', length=1, delay_cost=1)
	S += t3_t1_t2_mem0 >= 24
	t3_t1_t2_mem0 += INPUT_mem_r

	t3_t1_t2_mem1 = S.Task('t3_t1_t2_mem1', length=1, delay_cost=1)
	S += t3_t1_t2_mem1 >= 24
	t3_t1_t2_mem1 += INPUT_mem_r

	t3_t1_t3 = S.Task('t3_t1_t3', length=1, delay_cost=1)
	S += t3_t1_t3 >= 24
	t3_t1_t3 += ADD[1]

	t0_a1_1_mem0 = S.Task('t0_a1_1_mem0', length=1, delay_cost=1)
	S += t0_a1_1_mem0 >= 25
	t0_a1_1_mem0 += INPUT_mem_r

	t0_a1_1_mem1 = S.Task('t0_a1_1_mem1', length=1, delay_cost=1)
	S += t0_a1_1_mem1 >= 25
	t0_a1_1_mem1 += INPUT_mem_r

	t3_t1_t2 = S.Task('t3_t1_t2', length=1, delay_cost=1)
	S += t3_t1_t2 >= 25
	t3_t1_t2 += ADD[3]

	t0_a1_1 = S.Task('t0_a1_1', length=1, delay_cost=1)
	S += t0_a1_1 >= 26
	t0_a1_1 += ADD[3]

	t3_t0_t3_mem0 = S.Task('t3_t0_t3_mem0', length=1, delay_cost=1)
	S += t3_t0_t3_mem0 >= 26
	t3_t0_t3_mem0 += INPUT_mem_r

	t3_t0_t3_mem1 = S.Task('t3_t0_t3_mem1', length=1, delay_cost=1)
	S += t3_t0_t3_mem1 >= 26
	t3_t0_t3_mem1 += INPUT_mem_r

	t3_t0_t2_mem0 = S.Task('t3_t0_t2_mem0', length=1, delay_cost=1)
	S += t3_t0_t2_mem0 >= 27
	t3_t0_t2_mem0 += INPUT_mem_r

	t3_t0_t2_mem1 = S.Task('t3_t0_t2_mem1', length=1, delay_cost=1)
	S += t3_t0_t2_mem1 >= 27
	t3_t0_t2_mem1 += INPUT_mem_r

	t3_t0_t3 = S.Task('t3_t0_t3', length=1, delay_cost=1)
	S += t3_t0_t3 >= 27
	t3_t0_t3 += ADD[2]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 28
	t111_mem0 += INPUT_mem_r

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 28
	t111_mem1 += INPUT_mem_r

	t3_t0_t2 = S.Task('t3_t0_t2', length=1, delay_cost=1)
	S += t3_t0_t2 >= 28
	t3_t0_t2 += ADD[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 29
	t110_mem0 += INPUT_mem_r

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 29
	t110_mem1 += INPUT_mem_r

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 29
	t111 += ADD[3]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 30
	t110 += ADD[2]


	# new tasks
	t4_t3_t2 = S.Task('t4_t3_t2', length=1, delay_cost=1)
	t4_t3_t2 += alt(ADD)

	t4_t3_t2_mem0 = S.Task('t4_t3_t2_mem0', length=1, delay_cost=1)
	t4_t3_t2_mem0 += INPUT_mem_r
	S += t4_t3_t2_mem0 <= t4_t3_t2

	t4_t3_t2_mem1 = S.Task('t4_t3_t2_mem1', length=1, delay_cost=1)
	t4_t3_t2_mem1 += INPUT_mem_r
	S += t4_t3_t2_mem1 <= t4_t3_t2

	t4_t3_t3 = S.Task('t4_t3_t3', length=1, delay_cost=1)
	t4_t3_t3 += alt(ADD)

	t4_t3_t3_mem0 = S.Task('t4_t3_t3_mem0', length=1, delay_cost=1)
	t4_t3_t3_mem0 += INPUT_mem_r
	S += t4_t3_t3_mem0 <= t4_t3_t3

	t4_t3_t3_mem1 = S.Task('t4_t3_t3_mem1', length=1, delay_cost=1)
	t4_t3_t3_mem1 += INPUT_mem_r
	S += t4_t3_t3_mem1 <= t4_t3_t3

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	t5_t0_t0_in += alt(MUL_in)
	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	t5_t0_t0 += alt(MUL)
	S += t5_t0_t0>=t5_t0_t0_in

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	t5_t0_t0_mem0 += INPUT_mem_r
	S += t5_t0_t0_mem0 <= t5_t0_t0

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	t5_t0_t0_mem1 += INPUT_mem_r
	S += t5_t0_t0_mem1 <= t5_t0_t0

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	t5_t0_t1_in += alt(MUL_in)
	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	t5_t0_t1 += alt(MUL)
	S += t5_t0_t1>=t5_t0_t1_in

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	t5_t0_t1_mem0 += INPUT_mem_r
	S += t5_t0_t1_mem0 <= t5_t0_t1

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	t5_t0_t1_mem1 += INPUT_mem_r
	S += t5_t0_t1_mem1 <= t5_t0_t1

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	t5_t0_t2 += alt(ADD)

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	t5_t0_t2_mem0 += INPUT_mem_r
	S += t5_t0_t2_mem0 <= t5_t0_t2

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	t5_t0_t2_mem1 += INPUT_mem_r
	S += t5_t0_t2_mem1 <= t5_t0_t2

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	t5_t0_t3 += alt(ADD)

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	t5_t0_t3_mem0 += INPUT_mem_r
	S += t5_t0_t3_mem0 <= t5_t0_t3

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	t5_t0_t3_mem1 += INPUT_mem_r
	S += t5_t0_t3_mem1 <= t5_t0_t3

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	t5_t1_t0_in += alt(MUL_in)
	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	t5_t1_t0 += alt(MUL)
	S += t5_t1_t0>=t5_t1_t0_in

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	t5_t1_t0_mem0 += INPUT_mem_r
	S += t5_t1_t0_mem0 <= t5_t1_t0

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	t5_t1_t0_mem1 += INPUT_mem_r
	S += t5_t1_t0_mem1 <= t5_t1_t0

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	t5_t1_t1_in += alt(MUL_in)
	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	t5_t1_t1 += alt(MUL)
	S += t5_t1_t1>=t5_t1_t1_in

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	t5_t1_t1_mem0 += INPUT_mem_r
	S += t5_t1_t1_mem0 <= t5_t1_t1

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	t5_t1_t1_mem1 += INPUT_mem_r
	S += t5_t1_t1_mem1 <= t5_t1_t1

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	t5_t1_t2 += alt(ADD)

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	t5_t1_t2_mem0 += INPUT_mem_r
	S += t5_t1_t2_mem0 <= t5_t1_t2

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	t5_t1_t2_mem1 += INPUT_mem_r
	S += t5_t1_t2_mem1 <= t5_t1_t2

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	t5_t1_t3 += alt(ADD)

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	t5_t1_t3_mem0 += INPUT_mem_r
	S += t5_t1_t3_mem0 <= t5_t1_t3

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	t5_t1_t3_mem1 += INPUT_mem_r
	S += t5_t1_t3_mem1 <= t5_t1_t3

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	t5_t20 += alt(ADD)

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	t5_t20_mem0 += INPUT_mem_r
	S += t5_t20_mem0 <= t5_t20

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	t5_t20_mem1 += INPUT_mem_r
	S += t5_t20_mem1 <= t5_t20

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	t5_t21 += alt(ADD)

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	t5_t21_mem0 += INPUT_mem_r
	S += t5_t21_mem0 <= t5_t21

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	t5_t21_mem1 += INPUT_mem_r
	S += t5_t21_mem1 <= t5_t21

	t5_t30 = S.Task('t5_t30', length=1, delay_cost=1)
	t5_t30 += alt(ADD)

	t5_t30_mem0 = S.Task('t5_t30_mem0', length=1, delay_cost=1)
	t5_t30_mem0 += INPUT_mem_r
	S += t5_t30_mem0 <= t5_t30

	t5_t30_mem1 = S.Task('t5_t30_mem1', length=1, delay_cost=1)
	t5_t30_mem1 += INPUT_mem_r
	S += t5_t30_mem1 <= t5_t30

	t5_t31 = S.Task('t5_t31', length=1, delay_cost=1)
	t5_t31 += alt(ADD)

	t5_t31_mem0 = S.Task('t5_t31_mem0', length=1, delay_cost=1)
	t5_t31_mem0 += INPUT_mem_r
	S += t5_t31_mem0 <= t5_t31

	t5_t31_mem1 = S.Task('t5_t31_mem1', length=1, delay_cost=1)
	t5_t31_mem1 += INPUT_mem_r
	S += t5_t31_mem1 <= t5_t31

	t6_t0_t0_in = S.Task('t6_t0_t0_in', length=1, delay_cost=1)
	t6_t0_t0_in += alt(MUL_in)
	t6_t0_t0 = S.Task('t6_t0_t0', length=7, delay_cost=1)
	t6_t0_t0 += alt(MUL)
	S += t6_t0_t0>=t6_t0_t0_in

	t6_t0_t0_mem0 = S.Task('t6_t0_t0_mem0', length=1, delay_cost=1)
	t6_t0_t0_mem0 += INPUT_mem_r
	S += t6_t0_t0_mem0 <= t6_t0_t0

	t6_t0_t0_mem1 = S.Task('t6_t0_t0_mem1', length=1, delay_cost=1)
	t6_t0_t0_mem1 += INPUT_mem_r
	S += t6_t0_t0_mem1 <= t6_t0_t0

	t6_t0_t1_in = S.Task('t6_t0_t1_in', length=1, delay_cost=1)
	t6_t0_t1_in += alt(MUL_in)
	t6_t0_t1 = S.Task('t6_t0_t1', length=7, delay_cost=1)
	t6_t0_t1 += alt(MUL)
	S += t6_t0_t1>=t6_t0_t1_in

	t6_t0_t1_mem0 = S.Task('t6_t0_t1_mem0', length=1, delay_cost=1)
	t6_t0_t1_mem0 += INPUT_mem_r
	S += t6_t0_t1_mem0 <= t6_t0_t1

	t6_t0_t1_mem1 = S.Task('t6_t0_t1_mem1', length=1, delay_cost=1)
	t6_t0_t1_mem1 += INPUT_mem_r
	S += t6_t0_t1_mem1 <= t6_t0_t1

	t6_t0_t2 = S.Task('t6_t0_t2', length=1, delay_cost=1)
	t6_t0_t2 += alt(ADD)

	t6_t0_t2_mem0 = S.Task('t6_t0_t2_mem0', length=1, delay_cost=1)
	t6_t0_t2_mem0 += INPUT_mem_r
	S += t6_t0_t2_mem0 <= t6_t0_t2

	t6_t0_t2_mem1 = S.Task('t6_t0_t2_mem1', length=1, delay_cost=1)
	t6_t0_t2_mem1 += INPUT_mem_r
	S += t6_t0_t2_mem1 <= t6_t0_t2

	t6_t0_t3 = S.Task('t6_t0_t3', length=1, delay_cost=1)
	t6_t0_t3 += alt(ADD)

	t6_t0_t3_mem0 = S.Task('t6_t0_t3_mem0', length=1, delay_cost=1)
	t6_t0_t3_mem0 += INPUT_mem_r
	S += t6_t0_t3_mem0 <= t6_t0_t3

	t6_t0_t3_mem1 = S.Task('t6_t0_t3_mem1', length=1, delay_cost=1)
	t6_t0_t3_mem1 += INPUT_mem_r
	S += t6_t0_t3_mem1 <= t6_t0_t3

	t6_t1_t0_in = S.Task('t6_t1_t0_in', length=1, delay_cost=1)
	t6_t1_t0_in += alt(MUL_in)
	t6_t1_t0 = S.Task('t6_t1_t0', length=7, delay_cost=1)
	t6_t1_t0 += alt(MUL)
	S += t6_t1_t0>=t6_t1_t0_in

	t6_t1_t0_mem0 = S.Task('t6_t1_t0_mem0', length=1, delay_cost=1)
	t6_t1_t0_mem0 += INPUT_mem_r
	S += t6_t1_t0_mem0 <= t6_t1_t0

	t6_t1_t0_mem1 = S.Task('t6_t1_t0_mem1', length=1, delay_cost=1)
	t6_t1_t0_mem1 += INPUT_mem_r
	S += t6_t1_t0_mem1 <= t6_t1_t0

	t6_t1_t1_in = S.Task('t6_t1_t1_in', length=1, delay_cost=1)
	t6_t1_t1_in += alt(MUL_in)
	t6_t1_t1 = S.Task('t6_t1_t1', length=7, delay_cost=1)
	t6_t1_t1 += alt(MUL)
	S += t6_t1_t1>=t6_t1_t1_in

	t6_t1_t1_mem0 = S.Task('t6_t1_t1_mem0', length=1, delay_cost=1)
	t6_t1_t1_mem0 += INPUT_mem_r
	S += t6_t1_t1_mem0 <= t6_t1_t1

	t6_t1_t1_mem1 = S.Task('t6_t1_t1_mem1', length=1, delay_cost=1)
	t6_t1_t1_mem1 += INPUT_mem_r
	S += t6_t1_t1_mem1 <= t6_t1_t1

	t6_t1_t2 = S.Task('t6_t1_t2', length=1, delay_cost=1)
	t6_t1_t2 += alt(ADD)

	t6_t1_t2_mem0 = S.Task('t6_t1_t2_mem0', length=1, delay_cost=1)
	t6_t1_t2_mem0 += INPUT_mem_r
	S += t6_t1_t2_mem0 <= t6_t1_t2

	t6_t1_t2_mem1 = S.Task('t6_t1_t2_mem1', length=1, delay_cost=1)
	t6_t1_t2_mem1 += INPUT_mem_r
	S += t6_t1_t2_mem1 <= t6_t1_t2

	t6_t1_t3 = S.Task('t6_t1_t3', length=1, delay_cost=1)
	t6_t1_t3 += alt(ADD)

	t6_t1_t3_mem0 = S.Task('t6_t1_t3_mem0', length=1, delay_cost=1)
	t6_t1_t3_mem0 += INPUT_mem_r
	S += t6_t1_t3_mem0 <= t6_t1_t3

	t6_t1_t3_mem1 = S.Task('t6_t1_t3_mem1', length=1, delay_cost=1)
	t6_t1_t3_mem1 += INPUT_mem_r
	S += t6_t1_t3_mem1 <= t6_t1_t3

	t6_t20 = S.Task('t6_t20', length=1, delay_cost=1)
	t6_t20 += alt(ADD)

	t6_t20_mem0 = S.Task('t6_t20_mem0', length=1, delay_cost=1)
	t6_t20_mem0 += INPUT_mem_r
	S += t6_t20_mem0 <= t6_t20

	t6_t20_mem1 = S.Task('t6_t20_mem1', length=1, delay_cost=1)
	t6_t20_mem1 += INPUT_mem_r
	S += t6_t20_mem1 <= t6_t20

	t6_t21 = S.Task('t6_t21', length=1, delay_cost=1)
	t6_t21 += alt(ADD)

	t6_t21_mem0 = S.Task('t6_t21_mem0', length=1, delay_cost=1)
	t6_t21_mem0 += INPUT_mem_r
	S += t6_t21_mem0 <= t6_t21

	t6_t21_mem1 = S.Task('t6_t21_mem1', length=1, delay_cost=1)
	t6_t21_mem1 += INPUT_mem_r
	S += t6_t21_mem1 <= t6_t21

	t6_t30 = S.Task('t6_t30', length=1, delay_cost=1)
	t6_t30 += alt(ADD)

	t6_t30_mem0 = S.Task('t6_t30_mem0', length=1, delay_cost=1)
	t6_t30_mem0 += INPUT_mem_r
	S += t6_t30_mem0 <= t6_t30

	t6_t30_mem1 = S.Task('t6_t30_mem1', length=1, delay_cost=1)
	t6_t30_mem1 += INPUT_mem_r
	S += t6_t30_mem1 <= t6_t30

	t6_t31 = S.Task('t6_t31', length=1, delay_cost=1)
	t6_t31 += alt(ADD)

	t6_t31_mem0 = S.Task('t6_t31_mem0', length=1, delay_cost=1)
	t6_t31_mem0 += INPUT_mem_r
	S += t6_t31_mem0 <= t6_t31

	t6_t31_mem1 = S.Task('t6_t31_mem1', length=1, delay_cost=1)
	t6_t31_mem1 += INPUT_mem_r
	S += t6_t31_mem1 <= t6_t31

	t7_t0_t0_in = S.Task('t7_t0_t0_in', length=1, delay_cost=1)
	t7_t0_t0_in += alt(MUL_in)
	t7_t0_t0 = S.Task('t7_t0_t0', length=7, delay_cost=1)
	t7_t0_t0 += alt(MUL)
	S += t7_t0_t0>=t7_t0_t0_in

	t7_t0_t0_mem0 = S.Task('t7_t0_t0_mem0', length=1, delay_cost=1)
	t7_t0_t0_mem0 += INPUT_mem_r
	S += t7_t0_t0_mem0 <= t7_t0_t0

	t7_t0_t0_mem1 = S.Task('t7_t0_t0_mem1', length=1, delay_cost=1)
	t7_t0_t0_mem1 += INPUT_mem_r
	S += t7_t0_t0_mem1 <= t7_t0_t0

	t7_t0_t1_in = S.Task('t7_t0_t1_in', length=1, delay_cost=1)
	t7_t0_t1_in += alt(MUL_in)
	t7_t0_t1 = S.Task('t7_t0_t1', length=7, delay_cost=1)
	t7_t0_t1 += alt(MUL)
	S += t7_t0_t1>=t7_t0_t1_in

	t7_t0_t1_mem0 = S.Task('t7_t0_t1_mem0', length=1, delay_cost=1)
	t7_t0_t1_mem0 += INPUT_mem_r
	S += t7_t0_t1_mem0 <= t7_t0_t1

	t7_t0_t1_mem1 = S.Task('t7_t0_t1_mem1', length=1, delay_cost=1)
	t7_t0_t1_mem1 += INPUT_mem_r
	S += t7_t0_t1_mem1 <= t7_t0_t1

	t7_t0_t2 = S.Task('t7_t0_t2', length=1, delay_cost=1)
	t7_t0_t2 += alt(ADD)

	t7_t0_t2_mem0 = S.Task('t7_t0_t2_mem0', length=1, delay_cost=1)
	t7_t0_t2_mem0 += INPUT_mem_r
	S += t7_t0_t2_mem0 <= t7_t0_t2

	t7_t0_t2_mem1 = S.Task('t7_t0_t2_mem1', length=1, delay_cost=1)
	t7_t0_t2_mem1 += INPUT_mem_r
	S += t7_t0_t2_mem1 <= t7_t0_t2

	t7_t0_t3 = S.Task('t7_t0_t3', length=1, delay_cost=1)
	t7_t0_t3 += alt(ADD)

	t7_t0_t3_mem0 = S.Task('t7_t0_t3_mem0', length=1, delay_cost=1)
	t7_t0_t3_mem0 += INPUT_mem_r
	S += t7_t0_t3_mem0 <= t7_t0_t3

	t7_t0_t3_mem1 = S.Task('t7_t0_t3_mem1', length=1, delay_cost=1)
	t7_t0_t3_mem1 += INPUT_mem_r
	S += t7_t0_t3_mem1 <= t7_t0_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls24-1032/scheduling/SQR012345_mul1_add4/SQR012345_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

