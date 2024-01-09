from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 133
	S = Scenario("SPARSE_M_mul1_add4_2", horizon=horizon)

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
	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 0
	t4_t2_t1_in += MUL_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 0
	t4_t2_t1_mem0 += INPUT_mem_r

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 0
	t4_t2_t1_mem1 += INPUT_mem_r

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 1
	t4_t1_t0_in += MUL_in[0]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 1
	t4_t1_t0_mem0 += INPUT_mem_r

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 1
	t4_t1_t0_mem1 += INPUT_mem_r

	t4_t2_t1 = S.Task('t4_t2_t1', length=7, delay_cost=1)
	S += t4_t2_t1 >= 1
	t4_t2_t1 += MUL[0]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 2
	t4_t0_t1_in += MUL_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 2
	t4_t0_t1_mem0 += INPUT_mem_r

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 2
	t4_t0_t1_mem1 += INPUT_mem_r

	t4_t1_t0 = S.Task('t4_t1_t0', length=7, delay_cost=1)
	S += t4_t1_t0 >= 2
	t4_t1_t0 += MUL[0]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 3
	t4_t0_t0_in += MUL_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 3
	t4_t0_t0_mem0 += INPUT_mem_r

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 3
	t4_t0_t0_mem1 += INPUT_mem_r

	t4_t0_t1 = S.Task('t4_t0_t1', length=7, delay_cost=1)
	S += t4_t0_t1 >= 3
	t4_t0_t1 += MUL[0]

	t4_t0_t0 = S.Task('t4_t0_t0', length=7, delay_cost=1)
	S += t4_t0_t0 >= 4
	t4_t0_t0 += MUL[0]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 4
	t4_t8_t0_in += MUL_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 4
	t4_t8_t0_mem0 += INPUT_mem_r

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 4
	t4_t8_t0_mem1 += INPUT_mem_r

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 5
	t2_t1_in += MUL_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 5
	t2_t1_mem0 += INPUT_mem_r

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 5
	t2_t1_mem1 += INPUT_mem_r

	t4_t8_t0 = S.Task('t4_t8_t0', length=7, delay_cost=1)
	S += t4_t8_t0 >= 5
	t4_t8_t0 += MUL[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 6
	t2_t0_in += MUL_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 6
	t2_t0_mem0 += INPUT_mem_r

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 6
	t2_t0_mem1 += INPUT_mem_r

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 6
	t2_t1 += MUL[0]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 7
	t1_t0_in += MUL_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 7
	t1_t0_mem0 += INPUT_mem_r

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 7
	t1_t0_mem1 += INPUT_mem_r

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 7
	t2_t0 += MUL[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 8
	t0_t1_in += MUL_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 8
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 8
	t0_t1_mem1 += INPUT_mem_r

	t1_t0 = S.Task('t1_t0', length=7, delay_cost=1)
	S += t1_t0 >= 8
	t1_t0 += MUL[0]

	t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
	S += t0_t1 >= 9
	t0_t1 += MUL[0]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 9
	t4_t8_t1_in += MUL_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 9
	t4_t8_t1_mem0 += INPUT_mem_r

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 9
	t4_t8_t1_mem1 += INPUT_mem_r

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 10
	t4_t2_t0_in += MUL_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 10
	t4_t2_t0_mem0 += INPUT_mem_r

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 10
	t4_t2_t0_mem1 += INPUT_mem_r

	t4_t8_t1 = S.Task('t4_t8_t1', length=7, delay_cost=1)
	S += t4_t8_t1 >= 10
	t4_t8_t1 += MUL[0]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 11
	t4_t1_t1_in += MUL_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 11
	t4_t1_t1_mem0 += INPUT_mem_r

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 11
	t4_t1_t1_mem1 += INPUT_mem_r

	t4_t2_t0 = S.Task('t4_t2_t0', length=7, delay_cost=1)
	S += t4_t2_t0 >= 11
	t4_t2_t0 += MUL[0]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 12
	t1_t1_in += MUL_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 12
	t1_t1_mem0 += INPUT_mem_r

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 12
	t1_t1_mem1 += INPUT_mem_r

	t4_t1_t1 = S.Task('t4_t1_t1', length=7, delay_cost=1)
	S += t4_t1_t1 >= 12
	t4_t1_t1 += MUL[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 13
	t0_t0_in += MUL_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 13
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 13
	t0_t0_mem1 += INPUT_mem_r

	t1_t1 = S.Task('t1_t1', length=7, delay_cost=1)
	S += t1_t1 >= 13
	t1_t1 += MUL[0]

	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	S += t0_t0 >= 14
	t0_t0 += MUL[0]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 14
	t4_t51_mem0 += INPUT_mem_r

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 14
	t4_t51_mem1 += INPUT_mem_r

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 15
	t4_t1_t2_mem0 += INPUT_mem_r

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 15
	t4_t1_t2_mem1 += INPUT_mem_r

	t4_t51 = S.Task('t4_t51', length=1, delay_cost=1)
	S += t4_t51 >= 15
	t4_t51 += ADD[3]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 16
	t2_t2_mem0 += INPUT_mem_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 16
	t2_t2_mem1 += INPUT_mem_r

	t4_t1_t2 = S.Task('t4_t1_t2', length=1, delay_cost=1)
	S += t4_t1_t2 >= 16
	t4_t1_t2 += ADD[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 17
	t0_t2_mem0 += INPUT_mem_r

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 17
	t0_t2_mem1 += INPUT_mem_r

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 17
	t2_t2 += ADD[0]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 18
	t0_t2 += ADD[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 18
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 18
	t0_t3_mem1 += INPUT_mem_r

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 19
	t0_t3 += ADD[3]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 19
	t4_t0_t2_mem0 += INPUT_mem_r

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 19
	t4_t0_t2_mem1 += INPUT_mem_r

	t4_t0_t2 = S.Task('t4_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t2 >= 20
	t4_t0_t2 += ADD[3]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 20
	t4_t0_t3_mem0 += INPUT_mem_r

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 20
	t4_t0_t3_mem1 += INPUT_mem_r

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 21
	t1_t2_mem0 += INPUT_mem_r

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 21
	t1_t2_mem1 += INPUT_mem_r

	t4_t0_t3 = S.Task('t4_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t3 >= 21
	t4_t0_t3 += ADD[2]

	t1_t2 = S.Task('t1_t2', length=1, delay_cost=1)
	S += t1_t2 >= 22
	t1_t2 += ADD[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 22
	t2_t3_mem0 += INPUT_mem_r

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 22
	t2_t3_mem1 += INPUT_mem_r

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 23
	t2_t3 += ADD[1]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 23
	t4_t1_t3_mem0 += INPUT_mem_r

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 23
	t4_t1_t3_mem1 += INPUT_mem_r

	t4_t1_t3 = S.Task('t4_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t3 >= 24
	t4_t1_t3 += ADD[0]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 24
	t4_t50_mem0 += INPUT_mem_r

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 24
	t4_t50_mem1 += INPUT_mem_r

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 25
	t4_t41_mem0 += INPUT_mem_r

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 25
	t4_t41_mem1 += INPUT_mem_r

	t4_t50 = S.Task('t4_t50', length=1, delay_cost=1)
	S += t4_t50 >= 25
	t4_t50 += ADD[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 26
	t1_t3_mem0 += INPUT_mem_r

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 26
	t1_t3_mem1 += INPUT_mem_r

	t4_t41 = S.Task('t4_t41', length=1, delay_cost=1)
	S += t4_t41 >= 26
	t4_t41 += ADD[3]

	t1_t3 = S.Task('t1_t3', length=1, delay_cost=1)
	S += t1_t3 >= 27
	t1_t3 += ADD[1]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 27
	t4_t40_mem0 += INPUT_mem_r

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 27
	t4_t40_mem1 += INPUT_mem_r

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 28
	t4_t2_t3_mem0 += INPUT_mem_r

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 28
	t4_t2_t3_mem1 += INPUT_mem_r

	t4_t40 = S.Task('t4_t40', length=1, delay_cost=1)
	S += t4_t40 >= 28
	t4_t40 += ADD[2]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 29
	t4_t2_t2_mem0 += INPUT_mem_r

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 29
	t4_t2_t2_mem1 += INPUT_mem_r

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 29
	t4_t2_t3 += ADD[0]

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	S += t4_t2_t2 >= 30
	t4_t2_t2 += ADD[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 30
	t91_mem0 += INPUT_mem_r

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 30
	t91_mem1 += INPUT_mem_r

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 31
	t100_mem0 += INPUT_mem_r

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 31
	t100_mem1 += INPUT_mem_r

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 31
	t91 += ADD[1]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 32
	t100 += ADD[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 32
	t101_mem0 += INPUT_mem_r

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 32
	t101_mem1 += INPUT_mem_r

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 33
	t101 += ADD[1]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 33
	t5_t0_t2_mem0 += INPUT_mem_r

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 33
	t5_t0_t2_mem1 += INPUT_mem_r

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 34
	t4_t8_t2_mem0 += INPUT_mem_r

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 34
	t4_t8_t2_mem1 += INPUT_mem_r

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 34
	t5_t0_t2 += ADD[0]

	t4_t8_t2 = S.Task('t4_t8_t2', length=1, delay_cost=1)
	S += t4_t8_t2 >= 35
	t4_t8_t2 += ADD[1]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 35
	t5_t8_t2_mem0 += INPUT_mem_r

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 35
	t5_t8_t2_mem1 += INPUT_mem_r

	t5_t8_t2 = S.Task('t5_t8_t2', length=1, delay_cost=1)
	S += t5_t8_t2 >= 36
	t5_t8_t2 += ADD[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 36
	t81_mem0 += INPUT_mem_r

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 36
	t81_mem1 += INPUT_mem_r

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 37
	t70_mem0 += INPUT_mem_r

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 37
	t70_mem1 += INPUT_mem_r

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 37
	t81 += ADD[0]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 38
	t4_t8_t3_mem0 += INPUT_mem_r

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 38
	t4_t8_t3_mem1 += INPUT_mem_r

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 38
	t70 += ADD[0]

	t4_t8_t3 = S.Task('t4_t8_t3', length=1, delay_cost=1)
	S += t4_t8_t3 >= 39
	t4_t8_t3 += ADD[2]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 39
	t71_mem0 += INPUT_mem_r

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 39
	t71_mem1 += INPUT_mem_r

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 40
	t71 += ADD[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 40
	t90_mem0 += INPUT_mem_r

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 40
	t90_mem1 += INPUT_mem_r

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 41
	t80_mem0 += INPUT_mem_r

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 41
	t80_mem1 += INPUT_mem_r

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 41
	t90 += ADD[0]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 42
	t80 += ADD[2]


	# new tasks
	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	t1_t4_in += alt(MUL_in)
	t1_t4 = S.Task('t1_t4', length=7, delay_cost=1)
	t1_t4 += alt(MUL)
	S += t1_t4>=t1_t4_in

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	t1_t4_mem0 += ADD_mem[1]
	S += 22<t1_t4_mem0
	S += t1_t4_mem0<=t1_t4

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	t1_t4_mem1 += ADD_mem[1]
	S += 27<t1_t4_mem1
	S += t1_t4_mem1<=t1_t4

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(ADD)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += MUL_mem[0]
	S += 14<t10_mem0
	S += t10_mem0<=t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += MUL_mem[0]
	S += 19<t10_mem1
	S += t10_mem1<=t10

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	t1_t5 += alt(ADD)

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	t1_t5_mem0 += MUL_mem[0]
	S += 14<t1_t5_mem0
	S += t1_t5_mem0<=t1_t5

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	t1_t5_mem1 += MUL_mem[0]
	S += 19<t1_t5_mem1
	S += t1_t5_mem1<=t1_t5

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MUL_in)
	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	t2_t4 += alt(MUL)
	S += t2_t4>=t2_t4_in

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += ADD_mem[0]
	S += 17<t2_t4_mem0
	S += t2_t4_mem0<=t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += ADD_mem[1]
	S += 23<t2_t4_mem1
	S += t2_t4_mem1<=t2_t4

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(ADD)

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MUL_mem[0]
	S += 13<t20_mem0
	S += t20_mem0<=t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MUL_mem[0]
	S += 12<t20_mem1
	S += t20_mem1<=t20

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	t2_t5 += alt(ADD)

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += MUL_mem[0]
	S += 13<t2_t5_mem0
	S += t2_t5_mem0<=t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += MUL_mem[0]
	S += 12<t2_t5_mem1
	S += t2_t5_mem1<=t2_t5

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	t0_t4_in += alt(MUL_in)
	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	t0_t4 += alt(MUL)
	S += t0_t4>=t0_t4_in

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	t0_t4_mem0 += ADD_mem[1]
	S += 18<t0_t4_mem0
	S += t0_t4_mem0<=t0_t4

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	t0_t4_mem1 += ADD_mem[3]
	S += 19<t0_t4_mem1
	S += t0_t4_mem1<=t0_t4

	t00 = S.Task('t00', length=1, delay_cost=1)
	t00 += alt(ADD)

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += MUL_mem[0]
	S += 20<t00_mem0
	S += t00_mem0<=t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += MUL_mem[0]
	S += 15<t00_mem1
	S += t00_mem1<=t00

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(ADD)

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MUL_mem[0]
	S += 20<t0_t5_mem0
	S += t0_t5_mem0<=t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MUL_mem[0]
	S += 15<t0_t5_mem1
	S += t0_t5_mem1<=t0_t5

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	t4_t0_t4_in += alt(MUL_in)
	t4_t0_t4 = S.Task('t4_t0_t4', length=7, delay_cost=1)
	t4_t0_t4 += alt(MUL)
	S += t4_t0_t4>=t4_t0_t4_in

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	t4_t0_t4_mem0 += ADD_mem[3]
	S += 20<t4_t0_t4_mem0
	S += t4_t0_t4_mem0<=t4_t0_t4

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	t4_t0_t4_mem1 += ADD_mem[2]
	S += 21<t4_t0_t4_mem1
	S += t4_t0_t4_mem1<=t4_t0_t4

	t4_t00 = S.Task('t4_t00', length=1, delay_cost=1)
	t4_t00 += alt(ADD)

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	t4_t00_mem0 += MUL_mem[0]
	S += 10<t4_t00_mem0
	S += t4_t00_mem0<=t4_t00

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	t4_t00_mem1 += MUL_mem[0]
	S += 9<t4_t00_mem1
	S += t4_t00_mem1<=t4_t00

	t4_t0_t5 = S.Task('t4_t0_t5', length=1, delay_cost=1)
	t4_t0_t5 += alt(ADD)

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	t4_t0_t5_mem0 += MUL_mem[0]
	S += 10<t4_t0_t5_mem0
	S += t4_t0_t5_mem0<=t4_t0_t5

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	t4_t0_t5_mem1 += MUL_mem[0]
	S += 9<t4_t0_t5_mem1
	S += t4_t0_t5_mem1<=t4_t0_t5

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	t4_t1_t4_in += alt(MUL_in)
	t4_t1_t4 = S.Task('t4_t1_t4', length=7, delay_cost=1)
	t4_t1_t4 += alt(MUL)
	S += t4_t1_t4>=t4_t1_t4_in

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	t4_t1_t4_mem0 += ADD_mem[0]
	S += 16<t4_t1_t4_mem0
	S += t4_t1_t4_mem0<=t4_t1_t4

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	t4_t1_t4_mem1 += ADD_mem[0]
	S += 24<t4_t1_t4_mem1
	S += t4_t1_t4_mem1<=t4_t1_t4

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	t4_t10 += alt(ADD)

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	t4_t10_mem0 += MUL_mem[0]
	S += 8<t4_t10_mem0
	S += t4_t10_mem0<=t4_t10

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	t4_t10_mem1 += MUL_mem[0]
	S += 18<t4_t10_mem1
	S += t4_t10_mem1<=t4_t10

	t4_t1_t5 = S.Task('t4_t1_t5', length=1, delay_cost=1)
	t4_t1_t5 += alt(ADD)

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	t4_t1_t5_mem0 += MUL_mem[0]
	S += 8<t4_t1_t5_mem0
	S += t4_t1_t5_mem0<=t4_t1_t5

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	t4_t1_t5_mem1 += MUL_mem[0]
	S += 18<t4_t1_t5_mem1
	S += t4_t1_t5_mem1<=t4_t1_t5

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	t4_t2_t4_in += alt(MUL_in)
	t4_t2_t4 = S.Task('t4_t2_t4', length=7, delay_cost=1)
	t4_t2_t4 += alt(MUL)
	S += t4_t2_t4>=t4_t2_t4_in

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	t4_t2_t4_mem0 += ADD_mem[3]
	S += 30<t4_t2_t4_mem0
	S += t4_t2_t4_mem0<=t4_t2_t4

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	t4_t2_t4_mem1 += ADD_mem[0]
	S += 29<t4_t2_t4_mem1
	S += t4_t2_t4_mem1<=t4_t2_t4

	t4_t20 = S.Task('t4_t20', length=1, delay_cost=1)
	t4_t20 += alt(ADD)

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	t4_t20_mem0 += MUL_mem[0]
	S += 17<t4_t20_mem0
	S += t4_t20_mem0<=t4_t20

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	t4_t20_mem1 += MUL_mem[0]
	S += 7<t4_t20_mem1
	S += t4_t20_mem1<=t4_t20

	t4_t2_t5 = S.Task('t4_t2_t5', length=1, delay_cost=1)
	t4_t2_t5 += alt(ADD)

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	t4_t2_t5_mem0 += MUL_mem[0]
	S += 17<t4_t2_t5_mem0
	S += t4_t2_t5_mem0<=t4_t2_t5

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	t4_t2_t5_mem1 += MUL_mem[0]
	S += 7<t4_t2_t5_mem1
	S += t4_t2_t5_mem1<=t4_t2_t5

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	t4_t6_t0_in += alt(MUL_in)
	t4_t6_t0 = S.Task('t4_t6_t0', length=7, delay_cost=1)
	t4_t6_t0 += alt(MUL)
	S += t4_t6_t0>=t4_t6_t0_in

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	t4_t6_t0_mem0 += ADD_mem[2]
	S += 28<t4_t6_t0_mem0
	S += t4_t6_t0_mem0<=t4_t6_t0

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	t4_t6_t0_mem1 += ADD_mem[0]
	S += 25<t4_t6_t0_mem1
	S += t4_t6_t0_mem1<=t4_t6_t0

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	t4_t6_t1_in += alt(MUL_in)
	t4_t6_t1 = S.Task('t4_t6_t1', length=7, delay_cost=1)
	t4_t6_t1 += alt(MUL)
	S += t4_t6_t1>=t4_t6_t1_in

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	t4_t6_t1_mem0 += ADD_mem[3]
	S += 26<t4_t6_t1_mem0
	S += t4_t6_t1_mem0<=t4_t6_t1

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	t4_t6_t1_mem1 += ADD_mem[3]
	S += 15<t4_t6_t1_mem1
	S += t4_t6_t1_mem1<=t4_t6_t1

	t4_t6_t2 = S.Task('t4_t6_t2', length=1, delay_cost=1)
	t4_t6_t2 += alt(ADD)

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	t4_t6_t2_mem0 += ADD_mem[2]
	S += 28<t4_t6_t2_mem0
	S += t4_t6_t2_mem0<=t4_t6_t2

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	t4_t6_t2_mem1 += ADD_mem[3]
	S += 26<t4_t6_t2_mem1
	S += t4_t6_t2_mem1<=t4_t6_t2

	t4_t6_t3 = S.Task('t4_t6_t3', length=1, delay_cost=1)
	t4_t6_t3 += alt(ADD)

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	t4_t6_t3_mem0 += ADD_mem[0]
	S += 25<t4_t6_t3_mem0
	S += t4_t6_t3_mem0<=t4_t6_t3

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	t4_t6_t3_mem1 += ADD_mem[3]
	S += 15<t4_t6_t3_mem1
	S += t4_t6_t3_mem1<=t4_t6_t3

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	t4_t8_t4_in += alt(MUL_in)
	t4_t8_t4 = S.Task('t4_t8_t4', length=7, delay_cost=1)
	t4_t8_t4 += alt(MUL)
	S += t4_t8_t4>=t4_t8_t4_in

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	t4_t8_t4_mem0 += ADD_mem[1]
	S += 35<t4_t8_t4_mem0
	S += t4_t8_t4_mem0<=t4_t8_t4

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	t4_t8_t4_mem1 += ADD_mem[2]
	S += 39<t4_t8_t4_mem1
	S += t4_t8_t4_mem1<=t4_t8_t4

	t4_t80 = S.Task('t4_t80', length=1, delay_cost=1)
	t4_t80 += alt(ADD)

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	t4_t80_mem0 += MUL_mem[0]
	S += 11<t4_t80_mem0
	S += t4_t80_mem0<=t4_t80

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	t4_t80_mem1 += MUL_mem[0]
	S += 16<t4_t80_mem1
	S += t4_t80_mem1<=t4_t80

	t4_t8_t5 = S.Task('t4_t8_t5', length=1, delay_cost=1)
	t4_t8_t5 += alt(ADD)

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	t4_t8_t5_mem0 += MUL_mem[0]
	S += 11<t4_t8_t5_mem0
	S += t4_t8_t5_mem0<=t4_t8_t5

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	t4_t8_t5_mem1 += MUL_mem[0]
	S += 16<t4_t8_t5_mem1
	S += t4_t8_t5_mem1<=t4_t8_t5

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	t5_t0_t0_in += alt(MUL_in)
	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	t5_t0_t0 += alt(MUL)
	S += t5_t0_t0>=t5_t0_t0_in

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	t5_t0_t0_mem0 += INPUT_mem_r
	S += t5_t0_t0_mem0<=t5_t0_t0

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	t5_t0_t0_mem1 += ADD_mem[2]
	S += 42<t5_t0_t0_mem1
	S += t5_t0_t0_mem1<=t5_t0_t0

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	t5_t0_t1_in += alt(MUL_in)
	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	t5_t0_t1 += alt(MUL)
	S += t5_t0_t1>=t5_t0_t1_in

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	t5_t0_t1_mem0 += INPUT_mem_r
	S += t5_t0_t1_mem0<=t5_t0_t1

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	t5_t0_t1_mem1 += ADD_mem[0]
	S += 37<t5_t0_t1_mem1
	S += t5_t0_t1_mem1<=t5_t0_t1

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	t5_t0_t3 += alt(ADD)

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	t5_t0_t3_mem0 += ADD_mem[2]
	S += 42<t5_t0_t3_mem0
	S += t5_t0_t3_mem0<=t5_t0_t3

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	t5_t0_t3_mem1 += ADD_mem[0]
	S += 37<t5_t0_t3_mem1
	S += t5_t0_t3_mem1<=t5_t0_t3

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	t5_t1_t0_in += alt(MUL_in)
	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	t5_t1_t0 += alt(MUL)
	S += t5_t1_t0>=t5_t1_t0_in

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	t5_t1_t0_mem0 += ADD_mem[0]
	S += 38<t5_t1_t0_mem0
	S += t5_t1_t0_mem0<=t5_t1_t0

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	t5_t1_t0_mem1 += ADD_mem[0]
	S += 41<t5_t1_t0_mem1
	S += t5_t1_t0_mem1<=t5_t1_t0

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	t5_t1_t1_in += alt(MUL_in)
	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	t5_t1_t1 += alt(MUL)
	S += t5_t1_t1>=t5_t1_t1_in

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	t5_t1_t1_mem0 += ADD_mem[0]
	S += 40<t5_t1_t1_mem0
	S += t5_t1_t1_mem0<=t5_t1_t1

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	t5_t1_t1_mem1 += ADD_mem[1]
	S += 31<t5_t1_t1_mem1
	S += t5_t1_t1_mem1<=t5_t1_t1

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	t5_t1_t2 += alt(ADD)

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	t5_t1_t2_mem0 += ADD_mem[0]
	S += 38<t5_t1_t2_mem0
	S += t5_t1_t2_mem0<=t5_t1_t2

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	t5_t1_t2_mem1 += ADD_mem[0]
	S += 40<t5_t1_t2_mem1
	S += t5_t1_t2_mem1<=t5_t1_t2

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	t5_t1_t3 += alt(ADD)

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	t5_t1_t3_mem0 += ADD_mem[0]
	S += 41<t5_t1_t3_mem0
	S += t5_t1_t3_mem0<=t5_t1_t3

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	t5_t1_t3_mem1 += ADD_mem[1]
	S += 31<t5_t1_t3_mem1
	S += t5_t1_t3_mem1<=t5_t1_t3

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	t5_t2_t0_in += alt(MUL_in)
	t5_t2_t0 = S.Task('t5_t2_t0', length=7, delay_cost=1)
	t5_t2_t0 += alt(MUL)
	S += t5_t2_t0>=t5_t2_t0_in

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	t5_t2_t0_mem0 += ADD_mem[0]
	S += 38<t5_t2_t0_mem0
	S += t5_t2_t0_mem0<=t5_t2_t0

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	t5_t2_t0_mem1 += ADD_mem[3]
	S += 32<t5_t2_t0_mem1
	S += t5_t2_t0_mem1<=t5_t2_t0

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	t5_t2_t1_in += alt(MUL_in)
	t5_t2_t1 = S.Task('t5_t2_t1', length=7, delay_cost=1)
	t5_t2_t1 += alt(MUL)
	S += t5_t2_t1>=t5_t2_t1_in

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	t5_t2_t1_mem0 += ADD_mem[0]
	S += 40<t5_t2_t1_mem0
	S += t5_t2_t1_mem0<=t5_t2_t1

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	t5_t2_t1_mem1 += ADD_mem[1]
	S += 33<t5_t2_t1_mem1
	S += t5_t2_t1_mem1<=t5_t2_t1

	t5_t2_t2 = S.Task('t5_t2_t2', length=1, delay_cost=1)
	t5_t2_t2 += alt(ADD)

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	t5_t2_t2_mem0 += ADD_mem[0]
	S += 38<t5_t2_t2_mem0
	S += t5_t2_t2_mem0<=t5_t2_t2

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	t5_t2_t2_mem1 += ADD_mem[0]
	S += 40<t5_t2_t2_mem1
	S += t5_t2_t2_mem1<=t5_t2_t2

	t5_t2_t3 = S.Task('t5_t2_t3', length=1, delay_cost=1)
	t5_t2_t3 += alt(ADD)

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	t5_t2_t3_mem0 += ADD_mem[3]
	S += 32<t5_t2_t3_mem0
	S += t5_t2_t3_mem0<=t5_t2_t3

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	t5_t2_t3_mem1 += ADD_mem[1]
	S += 33<t5_t2_t3_mem1
	S += t5_t2_t3_mem1<=t5_t2_t3

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	t5_t40 += alt(ADD)

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	t5_t40_mem0 += INPUT_mem_r
	S += t5_t40_mem0<=t5_t40

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	t5_t40_mem1 += ADD_mem[0]
	S += 38<t5_t40_mem1
	S += t5_t40_mem1<=t5_t40

	t5_t41 = S.Task('t5_t41', length=1, delay_cost=1)
	t5_t41 += alt(ADD)

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	t5_t41_mem0 += INPUT_mem_r
	S += t5_t41_mem0<=t5_t41

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	t5_t41_mem1 += ADD_mem[0]
	S += 40<t5_t41_mem1
	S += t5_t41_mem1<=t5_t41

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	t5_t50 += alt(ADD)

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	t5_t50_mem0 += ADD_mem[2]
	S += 42<t5_t50_mem0
	S += t5_t50_mem0<=t5_t50

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	t5_t50_mem1 += ADD_mem[0]
	S += 41<t5_t50_mem1
	S += t5_t50_mem1<=t5_t50

	t5_t51 = S.Task('t5_t51', length=1, delay_cost=1)
	t5_t51 += alt(ADD)

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	t5_t51_mem0 += ADD_mem[0]
	S += 37<t5_t51_mem0
	S += t5_t51_mem0<=t5_t51

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	t5_t51_mem1 += ADD_mem[1]
	S += 31<t5_t51_mem1
	S += t5_t51_mem1<=t5_t51

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	t5_t8_t0_in += alt(MUL_in)
	t5_t8_t0 = S.Task('t5_t8_t0', length=7, delay_cost=1)
	t5_t8_t0 += alt(MUL)
	S += t5_t8_t0>=t5_t8_t0_in

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	t5_t8_t0_mem0 += INPUT_mem_r
	S += t5_t8_t0_mem0<=t5_t8_t0

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	t5_t8_t0_mem1 += ADD_mem[3]
	S += 32<t5_t8_t0_mem1
	S += t5_t8_t0_mem1<=t5_t8_t0

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	t5_t8_t1_in += alt(MUL_in)
	t5_t8_t1 = S.Task('t5_t8_t1', length=7, delay_cost=1)
	t5_t8_t1 += alt(MUL)
	S += t5_t8_t1>=t5_t8_t1_in

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	t5_t8_t1_mem0 += INPUT_mem_r
	S += t5_t8_t1_mem0<=t5_t8_t1

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	t5_t8_t1_mem1 += ADD_mem[1]
	S += 33<t5_t8_t1_mem1
	S += t5_t8_t1_mem1<=t5_t8_t1

	t5_t8_t3 = S.Task('t5_t8_t3', length=1, delay_cost=1)
	t5_t8_t3 += alt(ADD)

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	t5_t8_t3_mem0 += ADD_mem[3]
	S += 32<t5_t8_t3_mem0
	S += t5_t8_t3_mem0<=t5_t8_t3

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	t5_t8_t3_mem1 += ADD_mem[1]
	S += 33<t5_t8_t3_mem1
	S += t5_t8_t3_mem1<=t5_t8_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "SPARSE_M_mul1_add4/SPARSE_M_mul1_add4_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

