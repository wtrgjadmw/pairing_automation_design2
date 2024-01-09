from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 139
	S = Scenario("SPARSE_M_mul1_add4_3", horizon=horizon)

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

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	S += t4_t0_t5_mem0 >= 10
	t4_t0_t5_mem0 += MUL_mem[0]

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	S += t4_t0_t5_mem1 >= 10
	t4_t0_t5_mem1 += MUL_mem[0]

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

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 11
	t4_t00_mem0 += MUL_mem[0]

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 11
	t4_t00_mem1 += MUL_mem[0]

	t4_t0_t5 = S.Task('t4_t0_t5', length=1, delay_cost=1)
	S += t4_t0_t5 >= 11
	t4_t0_t5 += ADD[0]

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

	t4_t00 = S.Task('t4_t00', length=1, delay_cost=1)
	S += t4_t00 >= 12
	t4_t00 += ADD[3]

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

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 13
	t20_mem0 += MUL_mem[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 13
	t20_mem1 += MUL_mem[0]

	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	S += t0_t0 >= 14
	t0_t0 += MUL[0]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 14
	t20 += ADD[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 14
	t2_t5_mem0 += MUL_mem[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 14
	t2_t5_mem1 += MUL_mem[0]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 14
	t4_t51_mem0 += INPUT_mem_r

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 14
	t4_t51_mem1 += INPUT_mem_r

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 15
	t2_t5 += ADD[1]

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

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	S += t4_t8_t5_mem0 >= 16
	t4_t8_t5_mem0 += MUL_mem[0]

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	S += t4_t8_t5_mem1 >= 16
	t4_t8_t5_mem1 += MUL_mem[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 17
	t0_t2_mem0 += INPUT_mem_r

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 17
	t0_t2_mem1 += INPUT_mem_r

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 17
	t2_t2 += ADD[0]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	S += t4_t2_t5_mem0 >= 17
	t4_t2_t5_mem0 += MUL_mem[0]

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	S += t4_t2_t5_mem1 >= 17
	t4_t2_t5_mem1 += MUL_mem[0]

	t4_t8_t5 = S.Task('t4_t8_t5', length=1, delay_cost=1)
	S += t4_t8_t5 >= 17
	t4_t8_t5 += ADD[3]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 18
	t0_t2 += ADD[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 18
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 18
	t0_t3_mem1 += INPUT_mem_r

	t4_t2_t5 = S.Task('t4_t2_t5', length=1, delay_cost=1)
	S += t4_t2_t5 >= 18
	t4_t2_t5 += ADD[3]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	S += t4_t80_mem0 >= 18
	t4_t80_mem0 += MUL_mem[0]

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	S += t4_t80_mem1 >= 18
	t4_t80_mem1 += MUL_mem[0]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 19
	t0_t3 += ADD[3]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 19
	t0_t4_in += MUL_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 19
	t0_t4_mem0 += ADD_mem[1]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 19
	t0_t4_mem1 += ADD_mem[3]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 19
	t1_t5_mem0 += MUL_mem[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 19
	t1_t5_mem1 += MUL_mem[0]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 19
	t4_t0_t2_mem0 += INPUT_mem_r

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 19
	t4_t0_t2_mem1 += INPUT_mem_r

	t4_t80 = S.Task('t4_t80', length=1, delay_cost=1)
	S += t4_t80 >= 19
	t4_t80 += ADD[2]

	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	S += t0_t4 >= 20
	t0_t4 += MUL[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 20
	t0_t5_mem0 += MUL_mem[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 20
	t0_t5_mem1 += MUL_mem[0]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 20
	t1_t5 += ADD[0]

	t4_t0_t2 = S.Task('t4_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t2 >= 20
	t4_t0_t2 += ADD[3]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 20
	t4_t0_t3_mem0 += INPUT_mem_r

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 20
	t4_t0_t3_mem1 += INPUT_mem_r

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 21
	t0_t5 += ADD[3]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 21
	t10_mem0 += MUL_mem[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 21
	t10_mem1 += MUL_mem[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 21
	t1_t2_mem0 += INPUT_mem_r

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 21
	t1_t2_mem1 += INPUT_mem_r

	t4_t0_t3 = S.Task('t4_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t3 >= 21
	t4_t0_t3 += ADD[2]

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	S += t4_t0_t4_in >= 21
	t4_t0_t4_in += MUL_in[0]

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	S += t4_t0_t4_mem0 >= 21
	t4_t0_t4_mem0 += ADD_mem[3]

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	S += t4_t0_t4_mem1 >= 21
	t4_t0_t4_mem1 += ADD_mem[2]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 22
	t10 += ADD[0]

	t1_t2 = S.Task('t1_t2', length=1, delay_cost=1)
	S += t1_t2 >= 22
	t1_t2 += ADD[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 22
	t2_t3_mem0 += INPUT_mem_r

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 22
	t2_t3_mem1 += INPUT_mem_r

	t4_t0_t4 = S.Task('t4_t0_t4', length=7, delay_cost=1)
	S += t4_t0_t4 >= 22
	t4_t0_t4 += MUL[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 22
	t4_t10_mem0 += MUL_mem[0]

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 22
	t4_t10_mem1 += MUL_mem[0]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 23
	t2_t3 += ADD[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 23
	t2_t4_in += MUL_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 23
	t2_t4_mem0 += ADD_mem[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 23
	t2_t4_mem1 += ADD_mem[1]

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	S += t4_t10 >= 23
	t4_t10 += ADD[2]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 23
	t4_t1_t3_mem0 += INPUT_mem_r

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 23
	t4_t1_t3_mem1 += INPUT_mem_r

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	S += t4_t1_t5_mem0 >= 23
	t4_t1_t5_mem0 += MUL_mem[0]

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	S += t4_t1_t5_mem1 >= 23
	t4_t1_t5_mem1 += MUL_mem[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 24
	t00_mem0 += MUL_mem[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 24
	t00_mem1 += MUL_mem[0]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 24
	t2_t4 += MUL[0]

	t4_t1_t3 = S.Task('t4_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t3 >= 24
	t4_t1_t3 += ADD[0]

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	S += t4_t1_t4_in >= 24
	t4_t1_t4_in += MUL_in[0]

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	S += t4_t1_t4_mem0 >= 24
	t4_t1_t4_mem0 += ADD_mem[0]

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	S += t4_t1_t4_mem1 >= 24
	t4_t1_t4_mem1 += ADD_mem[0]

	t4_t1_t5 = S.Task('t4_t1_t5', length=1, delay_cost=1)
	S += t4_t1_t5 >= 24
	t4_t1_t5 += ADD[1]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 24
	t4_t50_mem0 += INPUT_mem_r

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 24
	t4_t50_mem1 += INPUT_mem_r

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 25
	t00 += ADD[1]

	t4_t1_t4 = S.Task('t4_t1_t4', length=7, delay_cost=1)
	S += t4_t1_t4 >= 25
	t4_t1_t4 += MUL[0]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	S += t4_t20_mem0 >= 25
	t4_t20_mem0 += MUL_mem[0]

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	S += t4_t20_mem1 >= 25
	t4_t20_mem1 += MUL_mem[0]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 25
	t4_t41_mem0 += INPUT_mem_r

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 25
	t4_t41_mem1 += INPUT_mem_r

	t4_t50 = S.Task('t4_t50', length=1, delay_cost=1)
	S += t4_t50 >= 25
	t4_t50 += ADD[0]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	S += t4_t6_t3_mem0 >= 25
	t4_t6_t3_mem0 += ADD_mem[0]

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	S += t4_t6_t3_mem1 >= 25
	t4_t6_t3_mem1 += ADD_mem[3]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 26
	t1_t3_mem0 += INPUT_mem_r

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 26
	t1_t3_mem1 += INPUT_mem_r

	t4_t20 = S.Task('t4_t20', length=1, delay_cost=1)
	S += t4_t20 >= 26
	t4_t20 += ADD[1]

	t4_t41 = S.Task('t4_t41', length=1, delay_cost=1)
	S += t4_t41 >= 26
	t4_t41 += ADD[3]

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	S += t4_t6_t1_in >= 26
	t4_t6_t1_in += MUL_in[0]

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	S += t4_t6_t1_mem0 >= 26
	t4_t6_t1_mem0 += ADD_mem[3]

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	S += t4_t6_t1_mem1 >= 26
	t4_t6_t1_mem1 += ADD_mem[3]

	t4_t6_t3 = S.Task('t4_t6_t3', length=1, delay_cost=1)
	S += t4_t6_t3 >= 26
	t4_t6_t3 += ADD[0]

	t1_t3 = S.Task('t1_t3', length=1, delay_cost=1)
	S += t1_t3 >= 27
	t1_t3 += ADD[1]

	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	S += t1_t4_in >= 27
	t1_t4_in += MUL_in[0]

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	S += t1_t4_mem0 >= 27
	t1_t4_mem0 += ADD_mem[1]

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	S += t1_t4_mem1 >= 27
	t1_t4_mem1 += ADD_mem[1]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 27
	t4_t40_mem0 += INPUT_mem_r

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 27
	t4_t40_mem1 += INPUT_mem_r

	t4_t6_t1 = S.Task('t4_t6_t1', length=7, delay_cost=1)
	S += t4_t6_t1 >= 27
	t4_t6_t1 += MUL[0]

	t1_t4 = S.Task('t1_t4', length=7, delay_cost=1)
	S += t1_t4 >= 28
	t1_t4 += MUL[0]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 28
	t4_t2_t3_mem0 += INPUT_mem_r

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 28
	t4_t2_t3_mem1 += INPUT_mem_r

	t4_t40 = S.Task('t4_t40', length=1, delay_cost=1)
	S += t4_t40 >= 28
	t4_t40 += ADD[2]

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	S += t4_t6_t0_in >= 28
	t4_t6_t0_in += MUL_in[0]

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	S += t4_t6_t0_mem0 >= 28
	t4_t6_t0_mem0 += ADD_mem[2]

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	S += t4_t6_t0_mem1 >= 28
	t4_t6_t0_mem1 += ADD_mem[0]

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	S += t4_t6_t2_mem0 >= 28
	t4_t6_t2_mem0 += ADD_mem[2]

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	S += t4_t6_t2_mem1 >= 28
	t4_t6_t2_mem1 += ADD_mem[3]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 29
	t4_t2_t2_mem0 += INPUT_mem_r

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 29
	t4_t2_t2_mem1 += INPUT_mem_r

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 29
	t4_t2_t3 += ADD[0]

	t4_t6_t0 = S.Task('t4_t6_t0', length=7, delay_cost=1)
	S += t4_t6_t0 >= 29
	t4_t6_t0 += MUL[0]

	t4_t6_t2 = S.Task('t4_t6_t2', length=1, delay_cost=1)
	S += t4_t6_t2 >= 29
	t4_t6_t2 += ADD[1]

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	S += t4_t2_t2 >= 30
	t4_t2_t2 += ADD[3]

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	S += t4_t2_t4_in >= 30
	t4_t2_t4_in += MUL_in[0]

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	S += t4_t2_t4_mem0 >= 30
	t4_t2_t4_mem0 += ADD_mem[3]

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	S += t4_t2_t4_mem1 >= 30
	t4_t2_t4_mem1 += ADD_mem[0]

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

	t4_t2_t4 = S.Task('t4_t2_t4', length=7, delay_cost=1)
	S += t4_t2_t4 >= 31
	t4_t2_t4 += MUL[0]

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

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	S += t5_t2_t3_mem0 >= 33
	t5_t2_t3_mem0 += ADD_mem[3]

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	S += t5_t2_t3_mem1 >= 33
	t5_t2_t3_mem1 += ADD_mem[1]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	S += t5_t8_t3_mem0 >= 33
	t5_t8_t3_mem0 += ADD_mem[3]

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	S += t5_t8_t3_mem1 >= 33
	t5_t8_t3_mem1 += ADD_mem[1]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 34
	t4_t8_t2_mem0 += INPUT_mem_r

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 34
	t4_t8_t2_mem1 += INPUT_mem_r

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 34
	t5_t0_t2 += ADD[0]

	t5_t2_t3 = S.Task('t5_t2_t3', length=1, delay_cost=1)
	S += t5_t2_t3 >= 34
	t5_t2_t3 += ADD[2]

	t5_t8_t3 = S.Task('t5_t8_t3', length=1, delay_cost=1)
	S += t5_t8_t3 >= 34
	t5_t8_t3 += ADD[1]

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

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	S += t5_t51_mem0 >= 37
	t5_t51_mem0 += ADD_mem[0]

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	S += t5_t51_mem1 >= 37
	t5_t51_mem1 += ADD_mem[1]

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

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	S += t5_t2_t0_in >= 38
	t5_t2_t0_in += MUL_in[0]

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	S += t5_t2_t0_mem0 >= 38
	t5_t2_t0_mem0 += ADD_mem[0]

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	S += t5_t2_t0_mem1 >= 38
	t5_t2_t0_mem1 += ADD_mem[3]

	t5_t51 = S.Task('t5_t51', length=1, delay_cost=1)
	S += t5_t51 >= 38
	t5_t51 += ADD[2]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 38
	t70 += ADD[0]

	t4_t8_t3 = S.Task('t4_t8_t3', length=1, delay_cost=1)
	S += t4_t8_t3 >= 39
	t4_t8_t3 += ADD[2]

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	S += t4_t8_t4_in >= 39
	t4_t8_t4_in += MUL_in[0]

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	S += t4_t8_t4_mem0 >= 39
	t4_t8_t4_mem0 += ADD_mem[1]

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	S += t4_t8_t4_mem1 >= 39
	t4_t8_t4_mem1 += ADD_mem[2]

	t5_t2_t0 = S.Task('t5_t2_t0', length=7, delay_cost=1)
	S += t5_t2_t0 >= 39
	t5_t2_t0 += MUL[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 39
	t71_mem0 += INPUT_mem_r

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 39
	t71_mem1 += INPUT_mem_r

	t4_t8_t4 = S.Task('t4_t8_t4', length=7, delay_cost=1)
	S += t4_t8_t4 >= 40
	t4_t8_t4 += MUL[0]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 40
	t5_t1_t1_in += MUL_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 40
	t5_t1_t1_mem0 += ADD_mem[0]

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 40
	t5_t1_t1_mem1 += ADD_mem[1]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 40
	t71 += ADD[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 40
	t90_mem0 += INPUT_mem_r

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 40
	t90_mem1 += INPUT_mem_r

	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	S += t5_t1_t1 >= 41
	t5_t1_t1 += MUL[0]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 41
	t5_t1_t3_mem0 += ADD_mem[0]

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 41
	t5_t1_t3_mem1 += ADD_mem[1]

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	S += t5_t2_t1_in >= 41
	t5_t2_t1_in += MUL_in[0]

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	S += t5_t2_t1_mem0 >= 41
	t5_t2_t1_mem0 += ADD_mem[0]

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	S += t5_t2_t1_mem1 >= 41
	t5_t2_t1_mem1 += ADD_mem[1]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 41
	t80_mem0 += INPUT_mem_r

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 41
	t80_mem1 += INPUT_mem_r

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 41
	t90 += ADD[0]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 42
	t5_t0_t0_in += MUL_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 42
	t5_t0_t0_mem0 += INPUT_mem_r

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 42
	t5_t0_t0_mem1 += ADD_mem[2]

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	S += t5_t1_t3 >= 42
	t5_t1_t3 += ADD[0]

	t5_t2_t1 = S.Task('t5_t2_t1', length=7, delay_cost=1)
	S += t5_t2_t1 >= 42
	t5_t2_t1 += MUL[0]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	S += t5_t41_mem0 >= 42
	t5_t41_mem0 += INPUT_mem_r

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	S += t5_t41_mem1 >= 42
	t5_t41_mem1 += ADD_mem[0]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	S += t5_t50_mem0 >= 42
	t5_t50_mem0 += ADD_mem[2]

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	S += t5_t50_mem1 >= 42
	t5_t50_mem1 += ADD_mem[0]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 42
	t80 += ADD[2]

	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	S += t5_t0_t0 >= 43
	t5_t0_t0 += MUL[0]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 43
	t5_t0_t3_mem0 += ADD_mem[2]

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 43
	t5_t0_t3_mem1 += ADD_mem[0]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	S += t5_t40_mem0 >= 43
	t5_t40_mem0 += INPUT_mem_r

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	S += t5_t40_mem1 >= 43
	t5_t40_mem1 += ADD_mem[0]

	t5_t41 = S.Task('t5_t41', length=1, delay_cost=1)
	S += t5_t41 >= 43
	t5_t41 += ADD[0]

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	S += t5_t50 >= 43
	t5_t50 += ADD[1]

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	S += t5_t8_t0_in >= 43
	t5_t8_t0_in += MUL_in[0]

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	S += t5_t8_t0_mem0 >= 43
	t5_t8_t0_mem0 += INPUT_mem_r

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	S += t5_t8_t0_mem1 >= 43
	t5_t8_t0_mem1 += ADD_mem[3]

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	S += t5_t0_t3 >= 44
	t5_t0_t3 += ADD[0]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_t2_mem0 >= 44
	t5_t2_t2_mem0 += ADD_mem[0]

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_t2_mem1 >= 44
	t5_t2_t2_mem1 += ADD_mem[0]

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	S += t5_t40 >= 44
	t5_t40 += ADD[2]

	t5_t8_t0 = S.Task('t5_t8_t0', length=7, delay_cost=1)
	S += t5_t8_t0 >= 44
	t5_t8_t0 += MUL[0]

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	S += t5_t8_t1_in >= 44
	t5_t8_t1_in += MUL_in[0]

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	S += t5_t8_t1_mem0 >= 44
	t5_t8_t1_mem0 += INPUT_mem_r

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	S += t5_t8_t1_mem1 >= 44
	t5_t8_t1_mem1 += ADD_mem[1]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 45
	t5_t1_t0_in += MUL_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 45
	t5_t1_t0_mem0 += ADD_mem[0]

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 45
	t5_t1_t0_mem1 += ADD_mem[0]

	t5_t2_t2 = S.Task('t5_t2_t2', length=1, delay_cost=1)
	S += t5_t2_t2 >= 45
	t5_t2_t2 += ADD[3]

	t5_t8_t1 = S.Task('t5_t8_t1', length=7, delay_cost=1)
	S += t5_t8_t1 >= 45
	t5_t8_t1 += MUL[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 46
	t5_t0_t1_in += MUL_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 46
	t5_t0_t1_mem0 += INPUT_mem_r

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 46
	t5_t0_t1_mem1 += ADD_mem[0]

	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	S += t5_t1_t0 >= 46
	t5_t1_t0 += MUL[0]

	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	S += t5_t0_t1 >= 47
	t5_t0_t1 += MUL[0]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 47
	t5_t1_t2_mem0 += ADD_mem[0]

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 47
	t5_t1_t2_mem1 += ADD_mem[0]

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	S += t5_t1_t2 >= 48
	t5_t1_t2 += ADD[0]


	# new tasks
	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(ADD)

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MUL_mem[0]
	S += 34<t11_mem0
	S += t11_mem0<=t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += ADD_mem[0]
	S += 20<t11_mem1
	S += t11_mem1<=t11

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(ADD)

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MUL_mem[0]
	S += 30<t21_mem0
	S += t21_mem0<=t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += ADD_mem[1]
	S += 15<t21_mem1
	S += t21_mem1<=t21

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(ADD)

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MUL_mem[0]
	S += 26<t01_mem0
	S += t01_mem0<=t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += ADD_mem[3]
	S += 21<t01_mem1
	S += t01_mem1<=t01

	t4_t01 = S.Task('t4_t01', length=1, delay_cost=1)
	t4_t01 += alt(ADD)

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	t4_t01_mem0 += MUL_mem[0]
	S += 28<t4_t01_mem0
	S += t4_t01_mem0<=t4_t01

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	t4_t01_mem1 += ADD_mem[0]
	S += 11<t4_t01_mem1
	S += t4_t01_mem1<=t4_t01

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	t4_t11 += alt(ADD)

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	t4_t11_mem0 += MUL_mem[0]
	S += 31<t4_t11_mem0
	S += t4_t11_mem0<=t4_t11

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	t4_t11_mem1 += ADD_mem[1]
	S += 24<t4_t11_mem1
	S += t4_t11_mem1<=t4_t11

	t4_t21 = S.Task('t4_t21', length=1, delay_cost=1)
	t4_t21 += alt(ADD)

	t4_t21_mem0 = S.Task('t4_t21_mem0', length=1, delay_cost=1)
	t4_t21_mem0 += MUL_mem[0]
	S += 37<t4_t21_mem0
	S += t4_t21_mem0<=t4_t21

	t4_t21_mem1 = S.Task('t4_t21_mem1', length=1, delay_cost=1)
	t4_t21_mem1 += ADD_mem[3]
	S += 18<t4_t21_mem1
	S += t4_t21_mem1<=t4_t21

	t4_t6_t4_in = S.Task('t4_t6_t4_in', length=1, delay_cost=1)
	t4_t6_t4_in += alt(MUL_in)
	t4_t6_t4 = S.Task('t4_t6_t4', length=7, delay_cost=1)
	t4_t6_t4 += alt(MUL)
	S += t4_t6_t4>=t4_t6_t4_in

	t4_t6_t4_mem0 = S.Task('t4_t6_t4_mem0', length=1, delay_cost=1)
	t4_t6_t4_mem0 += ADD_mem[1]
	S += 29<t4_t6_t4_mem0
	S += t4_t6_t4_mem0<=t4_t6_t4

	t4_t6_t4_mem1 = S.Task('t4_t6_t4_mem1', length=1, delay_cost=1)
	t4_t6_t4_mem1 += ADD_mem[0]
	S += 26<t4_t6_t4_mem1
	S += t4_t6_t4_mem1<=t4_t6_t4

	t4_t60 = S.Task('t4_t60', length=1, delay_cost=1)
	t4_t60 += alt(ADD)

	t4_t60_mem0 = S.Task('t4_t60_mem0', length=1, delay_cost=1)
	t4_t60_mem0 += MUL_mem[0]
	S += 35<t4_t60_mem0
	S += t4_t60_mem0<=t4_t60

	t4_t60_mem1 = S.Task('t4_t60_mem1', length=1, delay_cost=1)
	t4_t60_mem1 += MUL_mem[0]
	S += 33<t4_t60_mem1
	S += t4_t60_mem1<=t4_t60

	t4_t6_t5 = S.Task('t4_t6_t5', length=1, delay_cost=1)
	t4_t6_t5 += alt(ADD)

	t4_t6_t5_mem0 = S.Task('t4_t6_t5_mem0', length=1, delay_cost=1)
	t4_t6_t5_mem0 += MUL_mem[0]
	S += 35<t4_t6_t5_mem0
	S += t4_t6_t5_mem0<=t4_t6_t5

	t4_t6_t5_mem1 = S.Task('t4_t6_t5_mem1', length=1, delay_cost=1)
	t4_t6_t5_mem1 += MUL_mem[0]
	S += 33<t4_t6_t5_mem1
	S += t4_t6_t5_mem1<=t4_t6_t5

	t4_t70 = S.Task('t4_t70', length=1, delay_cost=1)
	t4_t70 += alt(ADD)

	t4_t70_mem0 = S.Task('t4_t70_mem0', length=1, delay_cost=1)
	t4_t70_mem0 += ADD_mem[3]
	S += 12<t4_t70_mem0
	S += t4_t70_mem0<=t4_t70

	t4_t70_mem1 = S.Task('t4_t70_mem1', length=1, delay_cost=1)
	t4_t70_mem1 += ADD_mem[2]
	S += 23<t4_t70_mem1
	S += t4_t70_mem1<=t4_t70

	t4_t81 = S.Task('t4_t81', length=1, delay_cost=1)
	t4_t81 += alt(ADD)

	t4_t81_mem0 = S.Task('t4_t81_mem0', length=1, delay_cost=1)
	t4_t81_mem0 += MUL_mem[0]
	S += 46<t4_t81_mem0
	S += t4_t81_mem0<=t4_t81

	t4_t81_mem1 = S.Task('t4_t81_mem1', length=1, delay_cost=1)
	t4_t81_mem1 += ADD_mem[3]
	S += 17<t4_t81_mem1
	S += t4_t81_mem1<=t4_t81

	t420 = S.Task('t420', length=1, delay_cost=1)
	t420 += alt(ADD)

	t420_mem0 = S.Task('t420_mem0', length=1, delay_cost=1)
	t420_mem0 += ADD_mem[2]
	S += 19<t420_mem0
	S += t420_mem0<=t420

	t420_mem1 = S.Task('t420_mem1', length=1, delay_cost=1)
	t420_mem1 += ADD_mem[2]
	S += 23<t420_mem1
	S += t420_mem1<=t420

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	t5_t0_t4_in += alt(MUL_in)
	t5_t0_t4 = S.Task('t5_t0_t4', length=7, delay_cost=1)
	t5_t0_t4 += alt(MUL)
	S += t5_t0_t4>=t5_t0_t4_in

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	t5_t0_t4_mem0 += ADD_mem[0]
	S += 34<t5_t0_t4_mem0
	S += t5_t0_t4_mem0<=t5_t0_t4

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	t5_t0_t4_mem1 += ADD_mem[0]
	S += 44<t5_t0_t4_mem1
	S += t5_t0_t4_mem1<=t5_t0_t4

	t5_t00 = S.Task('t5_t00', length=1, delay_cost=1)
	t5_t00 += alt(ADD)

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	t5_t00_mem0 += MUL_mem[0]
	S += 49<t5_t00_mem0
	S += t5_t00_mem0<=t5_t00

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	t5_t00_mem1 += MUL_mem[0]
	S += 53<t5_t00_mem1
	S += t5_t00_mem1<=t5_t00

	t5_t0_t5 = S.Task('t5_t0_t5', length=1, delay_cost=1)
	t5_t0_t5 += alt(ADD)

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	t5_t0_t5_mem0 += MUL_mem[0]
	S += 49<t5_t0_t5_mem0
	S += t5_t0_t5_mem0<=t5_t0_t5

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	t5_t0_t5_mem1 += MUL_mem[0]
	S += 53<t5_t0_t5_mem1
	S += t5_t0_t5_mem1<=t5_t0_t5

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	t5_t1_t4_in += alt(MUL_in)
	t5_t1_t4 = S.Task('t5_t1_t4', length=7, delay_cost=1)
	t5_t1_t4 += alt(MUL)
	S += t5_t1_t4>=t5_t1_t4_in

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	t5_t1_t4_mem0 += ADD_mem[0]
	S += 48<t5_t1_t4_mem0
	S += t5_t1_t4_mem0<=t5_t1_t4

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	t5_t1_t4_mem1 += ADD_mem[0]
	S += 42<t5_t1_t4_mem1
	S += t5_t1_t4_mem1<=t5_t1_t4

	t5_t10 = S.Task('t5_t10', length=1, delay_cost=1)
	t5_t10 += alt(ADD)

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	t5_t10_mem0 += MUL_mem[0]
	S += 52<t5_t10_mem0
	S += t5_t10_mem0<=t5_t10

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	t5_t10_mem1 += MUL_mem[0]
	S += 47<t5_t10_mem1
	S += t5_t10_mem1<=t5_t10

	t5_t1_t5 = S.Task('t5_t1_t5', length=1, delay_cost=1)
	t5_t1_t5 += alt(ADD)

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	t5_t1_t5_mem0 += MUL_mem[0]
	S += 52<t5_t1_t5_mem0
	S += t5_t1_t5_mem0<=t5_t1_t5

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	t5_t1_t5_mem1 += MUL_mem[0]
	S += 47<t5_t1_t5_mem1
	S += t5_t1_t5_mem1<=t5_t1_t5

	t5_t2_t4_in = S.Task('t5_t2_t4_in', length=1, delay_cost=1)
	t5_t2_t4_in += alt(MUL_in)
	t5_t2_t4 = S.Task('t5_t2_t4', length=7, delay_cost=1)
	t5_t2_t4 += alt(MUL)
	S += t5_t2_t4>=t5_t2_t4_in

	t5_t2_t4_mem0 = S.Task('t5_t2_t4_mem0', length=1, delay_cost=1)
	t5_t2_t4_mem0 += ADD_mem[3]
	S += 45<t5_t2_t4_mem0
	S += t5_t2_t4_mem0<=t5_t2_t4

	t5_t2_t4_mem1 = S.Task('t5_t2_t4_mem1', length=1, delay_cost=1)
	t5_t2_t4_mem1 += ADD_mem[2]
	S += 34<t5_t2_t4_mem1
	S += t5_t2_t4_mem1<=t5_t2_t4

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	t5_t20 += alt(ADD)

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	t5_t20_mem0 += MUL_mem[0]
	S += 45<t5_t20_mem0
	S += t5_t20_mem0<=t5_t20

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	t5_t20_mem1 += MUL_mem[0]
	S += 48<t5_t20_mem1
	S += t5_t20_mem1<=t5_t20

	t5_t2_t5 = S.Task('t5_t2_t5', length=1, delay_cost=1)
	t5_t2_t5 += alt(ADD)

	t5_t2_t5_mem0 = S.Task('t5_t2_t5_mem0', length=1, delay_cost=1)
	t5_t2_t5_mem0 += MUL_mem[0]
	S += 45<t5_t2_t5_mem0
	S += t5_t2_t5_mem0<=t5_t2_t5

	t5_t2_t5_mem1 = S.Task('t5_t2_t5_mem1', length=1, delay_cost=1)
	t5_t2_t5_mem1 += MUL_mem[0]
	S += 48<t5_t2_t5_mem1
	S += t5_t2_t5_mem1<=t5_t2_t5

	t5_t6_t0_in = S.Task('t5_t6_t0_in', length=1, delay_cost=1)
	t5_t6_t0_in += alt(MUL_in)
	t5_t6_t0 = S.Task('t5_t6_t0', length=7, delay_cost=1)
	t5_t6_t0 += alt(MUL)
	S += t5_t6_t0>=t5_t6_t0_in

	t5_t6_t0_mem0 = S.Task('t5_t6_t0_mem0', length=1, delay_cost=1)
	t5_t6_t0_mem0 += ADD_mem[2]
	S += 44<t5_t6_t0_mem0
	S += t5_t6_t0_mem0<=t5_t6_t0

	t5_t6_t0_mem1 = S.Task('t5_t6_t0_mem1', length=1, delay_cost=1)
	t5_t6_t0_mem1 += ADD_mem[1]
	S += 43<t5_t6_t0_mem1
	S += t5_t6_t0_mem1<=t5_t6_t0

	t5_t6_t1_in = S.Task('t5_t6_t1_in', length=1, delay_cost=1)
	t5_t6_t1_in += alt(MUL_in)
	t5_t6_t1 = S.Task('t5_t6_t1', length=7, delay_cost=1)
	t5_t6_t1 += alt(MUL)
	S += t5_t6_t1>=t5_t6_t1_in

	t5_t6_t1_mem0 = S.Task('t5_t6_t1_mem0', length=1, delay_cost=1)
	t5_t6_t1_mem0 += ADD_mem[0]
	S += 43<t5_t6_t1_mem0
	S += t5_t6_t1_mem0<=t5_t6_t1

	t5_t6_t1_mem1 = S.Task('t5_t6_t1_mem1', length=1, delay_cost=1)
	t5_t6_t1_mem1 += ADD_mem[2]
	S += 38<t5_t6_t1_mem1
	S += t5_t6_t1_mem1<=t5_t6_t1

	t5_t6_t2 = S.Task('t5_t6_t2', length=1, delay_cost=1)
	t5_t6_t2 += alt(ADD)

	t5_t6_t2_mem0 = S.Task('t5_t6_t2_mem0', length=1, delay_cost=1)
	t5_t6_t2_mem0 += ADD_mem[2]
	S += 44<t5_t6_t2_mem0
	S += t5_t6_t2_mem0<=t5_t6_t2

	t5_t6_t2_mem1 = S.Task('t5_t6_t2_mem1', length=1, delay_cost=1)
	t5_t6_t2_mem1 += ADD_mem[0]
	S += 43<t5_t6_t2_mem1
	S += t5_t6_t2_mem1<=t5_t6_t2

	t5_t6_t3 = S.Task('t5_t6_t3', length=1, delay_cost=1)
	t5_t6_t3 += alt(ADD)

	t5_t6_t3_mem0 = S.Task('t5_t6_t3_mem0', length=1, delay_cost=1)
	t5_t6_t3_mem0 += ADD_mem[1]
	S += 43<t5_t6_t3_mem0
	S += t5_t6_t3_mem0<=t5_t6_t3

	t5_t6_t3_mem1 = S.Task('t5_t6_t3_mem1', length=1, delay_cost=1)
	t5_t6_t3_mem1 += ADD_mem[2]
	S += 38<t5_t6_t3_mem1
	S += t5_t6_t3_mem1<=t5_t6_t3

	t5_t8_t4_in = S.Task('t5_t8_t4_in', length=1, delay_cost=1)
	t5_t8_t4_in += alt(MUL_in)
	t5_t8_t4 = S.Task('t5_t8_t4', length=7, delay_cost=1)
	t5_t8_t4 += alt(MUL)
	S += t5_t8_t4>=t5_t8_t4_in

	t5_t8_t4_mem0 = S.Task('t5_t8_t4_mem0', length=1, delay_cost=1)
	t5_t8_t4_mem0 += ADD_mem[0]
	S += 36<t5_t8_t4_mem0
	S += t5_t8_t4_mem0<=t5_t8_t4

	t5_t8_t4_mem1 = S.Task('t5_t8_t4_mem1', length=1, delay_cost=1)
	t5_t8_t4_mem1 += ADD_mem[1]
	S += 34<t5_t8_t4_mem1
	S += t5_t8_t4_mem1<=t5_t8_t4

	t5_t80 = S.Task('t5_t80', length=1, delay_cost=1)
	t5_t80 += alt(ADD)

	t5_t80_mem0 = S.Task('t5_t80_mem0', length=1, delay_cost=1)
	t5_t80_mem0 += MUL_mem[0]
	S += 50<t5_t80_mem0
	S += t5_t80_mem0<=t5_t80

	t5_t80_mem1 = S.Task('t5_t80_mem1', length=1, delay_cost=1)
	t5_t80_mem1 += MUL_mem[0]
	S += 51<t5_t80_mem1
	S += t5_t80_mem1<=t5_t80

	t5_t8_t5 = S.Task('t5_t8_t5', length=1, delay_cost=1)
	t5_t8_t5 += alt(ADD)

	t5_t8_t5_mem0 = S.Task('t5_t8_t5_mem0', length=1, delay_cost=1)
	t5_t8_t5_mem0 += MUL_mem[0]
	S += 50<t5_t8_t5_mem0
	S += t5_t8_t5_mem0<=t5_t8_t5

	t5_t8_t5_mem1 = S.Task('t5_t8_t5_mem1', length=1, delay_cost=1)
	t5_t8_t5_mem1 += MUL_mem[0]
	S += 51<t5_t8_t5_mem1
	S += t5_t8_t5_mem1<=t5_t8_t5

	t30 = S.Task('t30', length=1, delay_cost=1)
	t30 += alt(ADD)

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += ADD_mem[1]
	S += 25<t30_mem0
	S += t30_mem0<=t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += alt(ADD_mem)
	S += (t01*ADD[0])-1<t30_mem1*ADD_mem[0]
	S += (t01*ADD[1])-1<t30_mem1*ADD_mem[1]
	S += (t01*ADD[2])-1<t30_mem1*ADD_mem[2]
	S += (t01*ADD[3])-1<t30_mem1*ADD_mem[3]
	S += t30_mem1<=t30

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(ADD)

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(ADD_mem)
	S += (t01*ADD[0])-1<t31_mem0*ADD_mem[0]
	S += (t01*ADD[1])-1<t31_mem0*ADD_mem[1]
	S += (t01*ADD[2])-1<t31_mem0*ADD_mem[2]
	S += (t01*ADD[3])-1<t31_mem0*ADD_mem[3]
	S += t31_mem0<=t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += ADD_mem[1]
	S += 25<t31_mem1
	S += t31_mem1<=t31

	t4_t100 = S.Task('t4_t100', length=1, delay_cost=1)
	t4_t100 += alt(ADD)

	t4_t100_mem0 = S.Task('t4_t100_mem0', length=1, delay_cost=1)
	t4_t100_mem0 += ADD_mem[1]
	S += 26<t4_t100_mem0
	S += t4_t100_mem0<=t4_t100

	t4_t100_mem1 = S.Task('t4_t100_mem1', length=1, delay_cost=1)
	t4_t100_mem1 += alt(ADD_mem)
	S += (t4_t21*ADD[0])-1<t4_t100_mem1*ADD_mem[0]
	S += (t4_t21*ADD[1])-1<t4_t100_mem1*ADD_mem[1]
	S += (t4_t21*ADD[2])-1<t4_t100_mem1*ADD_mem[2]
	S += (t4_t21*ADD[3])-1<t4_t100_mem1*ADD_mem[3]
	S += t4_t100_mem1<=t4_t100

	t4_t101 = S.Task('t4_t101', length=1, delay_cost=1)
	t4_t101 += alt(ADD)

	t4_t101_mem0 = S.Task('t4_t101_mem0', length=1, delay_cost=1)
	t4_t101_mem0 += alt(ADD_mem)
	S += (t4_t21*ADD[0])-1<t4_t101_mem0*ADD_mem[0]
	S += (t4_t21*ADD[1])-1<t4_t101_mem0*ADD_mem[1]
	S += (t4_t21*ADD[2])-1<t4_t101_mem0*ADD_mem[2]
	S += (t4_t21*ADD[3])-1<t4_t101_mem0*ADD_mem[3]
	S += t4_t101_mem0<=t4_t101

	t4_t101_mem1 = S.Task('t4_t101_mem1', length=1, delay_cost=1)
	t4_t101_mem1 += ADD_mem[1]
	S += 26<t4_t101_mem1
	S += t4_t101_mem1<=t4_t101

	t4_t61 = S.Task('t4_t61', length=1, delay_cost=1)
	t4_t61 += alt(ADD)

	t4_t61_mem0 = S.Task('t4_t61_mem0', length=1, delay_cost=1)
	t4_t61_mem0 += alt(MUL_mem)
	S += (t4_t6_t4*MUL[0])-1<t4_t61_mem0*MUL_mem[0]
	S += t4_t61_mem0<=t4_t61

	t4_t61_mem1 = S.Task('t4_t61_mem1', length=1, delay_cost=1)
	t4_t61_mem1 += alt(ADD_mem)
	S += (t4_t6_t5*ADD[0])-1<t4_t61_mem1*ADD_mem[0]
	S += (t4_t6_t5*ADD[1])-1<t4_t61_mem1*ADD_mem[1]
	S += (t4_t6_t5*ADD[2])-1<t4_t61_mem1*ADD_mem[2]
	S += (t4_t6_t5*ADD[3])-1<t4_t61_mem1*ADD_mem[3]
	S += t4_t61_mem1<=t4_t61

	t4_t71 = S.Task('t4_t71', length=1, delay_cost=1)
	t4_t71 += alt(ADD)

	t4_t71_mem0 = S.Task('t4_t71_mem0', length=1, delay_cost=1)
	t4_t71_mem0 += alt(ADD_mem)
	S += (t4_t01*ADD[0])-1<t4_t71_mem0*ADD_mem[0]
	S += (t4_t01*ADD[1])-1<t4_t71_mem0*ADD_mem[1]
	S += (t4_t01*ADD[2])-1<t4_t71_mem0*ADD_mem[2]
	S += (t4_t01*ADD[3])-1<t4_t71_mem0*ADD_mem[3]
	S += t4_t71_mem0<=t4_t71

	t4_t71_mem1 = S.Task('t4_t71_mem1', length=1, delay_cost=1)
	t4_t71_mem1 += alt(ADD_mem)
	S += (t4_t11*ADD[0])-1<t4_t71_mem1*ADD_mem[0]
	S += (t4_t11*ADD[1])-1<t4_t71_mem1*ADD_mem[1]
	S += (t4_t11*ADD[2])-1<t4_t71_mem1*ADD_mem[2]
	S += (t4_t11*ADD[3])-1<t4_t71_mem1*ADD_mem[3]
	S += t4_t71_mem1<=t4_t71

	t410 = S.Task('t410', length=1, delay_cost=1)
	t410 += alt(ADD)

	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	t410_mem0 += alt(ADD_mem)
	S += (t4_t60*ADD[0])-1<t410_mem0*ADD_mem[0]
	S += (t4_t60*ADD[1])-1<t410_mem0*ADD_mem[1]
	S += (t4_t60*ADD[2])-1<t410_mem0*ADD_mem[2]
	S += (t4_t60*ADD[3])-1<t410_mem0*ADD_mem[3]
	S += t410_mem0<=t410

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	t410_mem1 += alt(ADD_mem)
	S += (t4_t70*ADD[0])-1<t410_mem1*ADD_mem[0]
	S += (t4_t70*ADD[1])-1<t410_mem1*ADD_mem[1]
	S += (t4_t70*ADD[2])-1<t410_mem1*ADD_mem[2]
	S += (t4_t70*ADD[3])-1<t410_mem1*ADD_mem[3]
	S += t410_mem1<=t410

	t421 = S.Task('t421', length=1, delay_cost=1)
	t421 += alt(ADD)

	t421_mem0 = S.Task('t421_mem0', length=1, delay_cost=1)
	t421_mem0 += alt(ADD_mem)
	S += (t4_t81*ADD[0])-1<t421_mem0*ADD_mem[0]
	S += (t4_t81*ADD[1])-1<t421_mem0*ADD_mem[1]
	S += (t4_t81*ADD[2])-1<t421_mem0*ADD_mem[2]
	S += (t4_t81*ADD[3])-1<t421_mem0*ADD_mem[3]
	S += t421_mem0<=t421

	t421_mem1 = S.Task('t421_mem1', length=1, delay_cost=1)
	t421_mem1 += alt(ADD_mem)
	S += (t4_t11*ADD[0])-1<t421_mem1*ADD_mem[0]
	S += (t4_t11*ADD[1])-1<t421_mem1*ADD_mem[1]
	S += (t4_t11*ADD[2])-1<t421_mem1*ADD_mem[2]
	S += (t4_t11*ADD[3])-1<t421_mem1*ADD_mem[3]
	S += t421_mem1<=t421

	t5_t01 = S.Task('t5_t01', length=1, delay_cost=1)
	t5_t01 += alt(ADD)

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	t5_t01_mem0 += alt(MUL_mem)
	S += (t5_t0_t4*MUL[0])-1<t5_t01_mem0*MUL_mem[0]
	S += t5_t01_mem0<=t5_t01

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	t5_t01_mem1 += alt(ADD_mem)
	S += (t5_t0_t5*ADD[0])-1<t5_t01_mem1*ADD_mem[0]
	S += (t5_t0_t5*ADD[1])-1<t5_t01_mem1*ADD_mem[1]
	S += (t5_t0_t5*ADD[2])-1<t5_t01_mem1*ADD_mem[2]
	S += (t5_t0_t5*ADD[3])-1<t5_t01_mem1*ADD_mem[3]
	S += t5_t01_mem1<=t5_t01

	t5_t11 = S.Task('t5_t11', length=1, delay_cost=1)
	t5_t11 += alt(ADD)

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	t5_t11_mem0 += alt(MUL_mem)
	S += (t5_t1_t4*MUL[0])-1<t5_t11_mem0*MUL_mem[0]
	S += t5_t11_mem0<=t5_t11

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	t5_t11_mem1 += alt(ADD_mem)
	S += (t5_t1_t5*ADD[0])-1<t5_t11_mem1*ADD_mem[0]
	S += (t5_t1_t5*ADD[1])-1<t5_t11_mem1*ADD_mem[1]
	S += (t5_t1_t5*ADD[2])-1<t5_t11_mem1*ADD_mem[2]
	S += (t5_t1_t5*ADD[3])-1<t5_t11_mem1*ADD_mem[3]
	S += t5_t11_mem1<=t5_t11

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	t5_t21 += alt(ADD)

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	t5_t21_mem0 += alt(MUL_mem)
	S += (t5_t2_t4*MUL[0])-1<t5_t21_mem0*MUL_mem[0]
	S += t5_t21_mem0<=t5_t21

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	t5_t21_mem1 += alt(ADD_mem)
	S += (t5_t2_t5*ADD[0])-1<t5_t21_mem1*ADD_mem[0]
	S += (t5_t2_t5*ADD[1])-1<t5_t21_mem1*ADD_mem[1]
	S += (t5_t2_t5*ADD[2])-1<t5_t21_mem1*ADD_mem[2]
	S += (t5_t2_t5*ADD[3])-1<t5_t21_mem1*ADD_mem[3]
	S += t5_t21_mem1<=t5_t21

	t5_t6_t4_in = S.Task('t5_t6_t4_in', length=1, delay_cost=1)
	t5_t6_t4_in += alt(MUL_in)
	t5_t6_t4 = S.Task('t5_t6_t4', length=7, delay_cost=1)
	t5_t6_t4 += alt(MUL)
	S += t5_t6_t4>=t5_t6_t4_in

	t5_t6_t4_mem0 = S.Task('t5_t6_t4_mem0', length=1, delay_cost=1)
	t5_t6_t4_mem0 += alt(ADD_mem)
	S += (t5_t6_t2*ADD[0])-1<t5_t6_t4_mem0*ADD_mem[0]
	S += (t5_t6_t2*ADD[1])-1<t5_t6_t4_mem0*ADD_mem[1]
	S += (t5_t6_t2*ADD[2])-1<t5_t6_t4_mem0*ADD_mem[2]
	S += (t5_t6_t2*ADD[3])-1<t5_t6_t4_mem0*ADD_mem[3]
	S += t5_t6_t4_mem0<=t5_t6_t4

	t5_t6_t4_mem1 = S.Task('t5_t6_t4_mem1', length=1, delay_cost=1)
	t5_t6_t4_mem1 += alt(ADD_mem)
	S += (t5_t6_t3*ADD[0])-1<t5_t6_t4_mem1*ADD_mem[0]
	S += (t5_t6_t3*ADD[1])-1<t5_t6_t4_mem1*ADD_mem[1]
	S += (t5_t6_t3*ADD[2])-1<t5_t6_t4_mem1*ADD_mem[2]
	S += (t5_t6_t3*ADD[3])-1<t5_t6_t4_mem1*ADD_mem[3]
	S += t5_t6_t4_mem1<=t5_t6_t4

	t5_t60 = S.Task('t5_t60', length=1, delay_cost=1)
	t5_t60 += alt(ADD)

	t5_t60_mem0 = S.Task('t5_t60_mem0', length=1, delay_cost=1)
	t5_t60_mem0 += alt(MUL_mem)
	S += (t5_t6_t0*MUL[0])-1<t5_t60_mem0*MUL_mem[0]
	S += t5_t60_mem0<=t5_t60

	t5_t60_mem1 = S.Task('t5_t60_mem1', length=1, delay_cost=1)
	t5_t60_mem1 += alt(MUL_mem)
	S += (t5_t6_t1*MUL[0])-1<t5_t60_mem1*MUL_mem[0]
	S += t5_t60_mem1<=t5_t60

	t5_t6_t5 = S.Task('t5_t6_t5', length=1, delay_cost=1)
	t5_t6_t5 += alt(ADD)

	t5_t6_t5_mem0 = S.Task('t5_t6_t5_mem0', length=1, delay_cost=1)
	t5_t6_t5_mem0 += alt(MUL_mem)
	S += (t5_t6_t0*MUL[0])-1<t5_t6_t5_mem0*MUL_mem[0]
	S += t5_t6_t5_mem0<=t5_t6_t5

	t5_t6_t5_mem1 = S.Task('t5_t6_t5_mem1', length=1, delay_cost=1)
	t5_t6_t5_mem1 += alt(MUL_mem)
	S += (t5_t6_t1*MUL[0])-1<t5_t6_t5_mem1*MUL_mem[0]
	S += t5_t6_t5_mem1<=t5_t6_t5

	t5_t70 = S.Task('t5_t70', length=1, delay_cost=1)
	t5_t70 += alt(ADD)

	t5_t70_mem0 = S.Task('t5_t70_mem0', length=1, delay_cost=1)
	t5_t70_mem0 += alt(ADD_mem)
	S += (t5_t00*ADD[0])-1<t5_t70_mem0*ADD_mem[0]
	S += (t5_t00*ADD[1])-1<t5_t70_mem0*ADD_mem[1]
	S += (t5_t00*ADD[2])-1<t5_t70_mem0*ADD_mem[2]
	S += (t5_t00*ADD[3])-1<t5_t70_mem0*ADD_mem[3]
	S += t5_t70_mem0<=t5_t70

	t5_t70_mem1 = S.Task('t5_t70_mem1', length=1, delay_cost=1)
	t5_t70_mem1 += alt(ADD_mem)
	S += (t5_t10*ADD[0])-1<t5_t70_mem1*ADD_mem[0]
	S += (t5_t10*ADD[1])-1<t5_t70_mem1*ADD_mem[1]
	S += (t5_t10*ADD[2])-1<t5_t70_mem1*ADD_mem[2]
	S += (t5_t10*ADD[3])-1<t5_t70_mem1*ADD_mem[3]
	S += t5_t70_mem1<=t5_t70

	t5_t81 = S.Task('t5_t81', length=1, delay_cost=1)
	t5_t81 += alt(ADD)

	t5_t81_mem0 = S.Task('t5_t81_mem0', length=1, delay_cost=1)
	t5_t81_mem0 += alt(MUL_mem)
	S += (t5_t8_t4*MUL[0])-1<t5_t81_mem0*MUL_mem[0]
	S += t5_t81_mem0<=t5_t81

	t5_t81_mem1 = S.Task('t5_t81_mem1', length=1, delay_cost=1)
	t5_t81_mem1 += alt(ADD_mem)
	S += (t5_t8_t5*ADD[0])-1<t5_t81_mem1*ADD_mem[0]
	S += (t5_t8_t5*ADD[1])-1<t5_t81_mem1*ADD_mem[1]
	S += (t5_t8_t5*ADD[2])-1<t5_t81_mem1*ADD_mem[2]
	S += (t5_t8_t5*ADD[3])-1<t5_t81_mem1*ADD_mem[3]
	S += t5_t81_mem1<=t5_t81

	t520 = S.Task('t520', length=1, delay_cost=1)
	t520 += alt(ADD)

	t520_mem0 = S.Task('t520_mem0', length=1, delay_cost=1)
	t520_mem0 += alt(ADD_mem)
	S += (t5_t80*ADD[0])-1<t520_mem0*ADD_mem[0]
	S += (t5_t80*ADD[1])-1<t520_mem0*ADD_mem[1]
	S += (t5_t80*ADD[2])-1<t520_mem0*ADD_mem[2]
	S += (t5_t80*ADD[3])-1<t520_mem0*ADD_mem[3]
	S += t520_mem0<=t520

	t520_mem1 = S.Task('t520_mem1', length=1, delay_cost=1)
	t520_mem1 += alt(ADD_mem)
	S += (t5_t10*ADD[0])-1<t520_mem1*ADD_mem[0]
	S += (t5_t10*ADD[1])-1<t520_mem1*ADD_mem[1]
	S += (t5_t10*ADD[2])-1<t520_mem1*ADD_mem[2]
	S += (t5_t10*ADD[3])-1<t520_mem1*ADD_mem[3]
	S += t520_mem1<=t520

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(ADD)

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += ADD_mem[0]
	S += 14<t160_mem0
	S += t160_mem0<=t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(ADD_mem)
	S += (t420*ADD[0])-1<t160_mem1*ADD_mem[0]
	S += (t420*ADD[1])-1<t160_mem1*ADD_mem[1]
	S += (t420*ADD[2])-1<t160_mem1*ADD_mem[2]
	S += (t420*ADD[3])-1<t160_mem1*ADD_mem[3]
	S += t160_mem1<=t160

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(ADD)

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += ADD_mem[0]
	S += 14<t170_mem0
	S += t170_mem0<=t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(ADD_mem)
	S += (t21*ADD[0])-1<t170_mem1*ADD_mem[0]
	S += (t21*ADD[1])-1<t170_mem1*ADD_mem[1]
	S += (t21*ADD[2])-1<t170_mem1*ADD_mem[2]
	S += (t21*ADD[3])-1<t170_mem1*ADD_mem[3]
	S += t170_mem1<=t170

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(ADD)

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(ADD_mem)
	S += (t21*ADD[0])-1<t171_mem0*ADD_mem[0]
	S += (t21*ADD[1])-1<t171_mem0*ADD_mem[1]
	S += (t21*ADD[2])-1<t171_mem0*ADD_mem[2]
	S += (t21*ADD[3])-1<t171_mem0*ADD_mem[3]
	S += t171_mem0<=t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += ADD_mem[0]
	S += 14<t171_mem1
	S += t171_mem1<=t171

	t400 = S.Task('t400', length=1, delay_cost=1)
	t400 += alt(ADD)

	t400_mem0 = S.Task('t400_mem0', length=1, delay_cost=1)
	t400_mem0 += ADD_mem[3]
	S += 12<t400_mem0
	S += t400_mem0<=t400

	t400_mem1 = S.Task('t400_mem1', length=1, delay_cost=1)
	t400_mem1 += alt(ADD_mem)
	S += (t4_t100*ADD[0])-1<t400_mem1*ADD_mem[0]
	S += (t4_t100*ADD[1])-1<t400_mem1*ADD_mem[1]
	S += (t4_t100*ADD[2])-1<t400_mem1*ADD_mem[2]
	S += (t4_t100*ADD[3])-1<t400_mem1*ADD_mem[3]
	S += t400_mem1<=t400

	t401 = S.Task('t401', length=1, delay_cost=1)
	t401 += alt(ADD)

	t401_mem0 = S.Task('t401_mem0', length=1, delay_cost=1)
	t401_mem0 += alt(ADD_mem)
	S += (t4_t01*ADD[0])-1<t401_mem0*ADD_mem[0]
	S += (t4_t01*ADD[1])-1<t401_mem0*ADD_mem[1]
	S += (t4_t01*ADD[2])-1<t401_mem0*ADD_mem[2]
	S += (t4_t01*ADD[3])-1<t401_mem0*ADD_mem[3]
	S += t401_mem0<=t401

	t401_mem1 = S.Task('t401_mem1', length=1, delay_cost=1)
	t401_mem1 += alt(ADD_mem)
	S += (t4_t101*ADD[0])-1<t401_mem1*ADD_mem[0]
	S += (t4_t101*ADD[1])-1<t401_mem1*ADD_mem[1]
	S += (t4_t101*ADD[2])-1<t401_mem1*ADD_mem[2]
	S += (t4_t101*ADD[3])-1<t401_mem1*ADD_mem[3]
	S += t401_mem1<=t401

	t411 = S.Task('t411', length=1, delay_cost=1)
	t411 += alt(ADD)

	t411_mem0 = S.Task('t411_mem0', length=1, delay_cost=1)
	t411_mem0 += alt(ADD_mem)
	S += (t4_t61*ADD[0])-1<t411_mem0*ADD_mem[0]
	S += (t4_t61*ADD[1])-1<t411_mem0*ADD_mem[1]
	S += (t4_t61*ADD[2])-1<t411_mem0*ADD_mem[2]
	S += (t4_t61*ADD[3])-1<t411_mem0*ADD_mem[3]
	S += t411_mem0<=t411

	t411_mem1 = S.Task('t411_mem1', length=1, delay_cost=1)
	t411_mem1 += alt(ADD_mem)
	S += (t4_t71*ADD[0])-1<t411_mem1*ADD_mem[0]
	S += (t4_t71*ADD[1])-1<t411_mem1*ADD_mem[1]
	S += (t4_t71*ADD[2])-1<t411_mem1*ADD_mem[2]
	S += (t4_t71*ADD[3])-1<t411_mem1*ADD_mem[3]
	S += t411_mem1<=t411

	t5_t100 = S.Task('t5_t100', length=1, delay_cost=1)
	t5_t100 += alt(ADD)

	t5_t100_mem0 = S.Task('t5_t100_mem0', length=1, delay_cost=1)
	t5_t100_mem0 += alt(ADD_mem)
	S += (t5_t20*ADD[0])-1<t5_t100_mem0*ADD_mem[0]
	S += (t5_t20*ADD[1])-1<t5_t100_mem0*ADD_mem[1]
	S += (t5_t20*ADD[2])-1<t5_t100_mem0*ADD_mem[2]
	S += (t5_t20*ADD[3])-1<t5_t100_mem0*ADD_mem[3]
	S += t5_t100_mem0<=t5_t100

	t5_t100_mem1 = S.Task('t5_t100_mem1', length=1, delay_cost=1)
	t5_t100_mem1 += alt(ADD_mem)
	S += (t5_t21*ADD[0])-1<t5_t100_mem1*ADD_mem[0]
	S += (t5_t21*ADD[1])-1<t5_t100_mem1*ADD_mem[1]
	S += (t5_t21*ADD[2])-1<t5_t100_mem1*ADD_mem[2]
	S += (t5_t21*ADD[3])-1<t5_t100_mem1*ADD_mem[3]
	S += t5_t100_mem1<=t5_t100

	t5_t101 = S.Task('t5_t101', length=1, delay_cost=1)
	t5_t101 += alt(ADD)

	t5_t101_mem0 = S.Task('t5_t101_mem0', length=1, delay_cost=1)
	t5_t101_mem0 += alt(ADD_mem)
	S += (t5_t21*ADD[0])-1<t5_t101_mem0*ADD_mem[0]
	S += (t5_t21*ADD[1])-1<t5_t101_mem0*ADD_mem[1]
	S += (t5_t21*ADD[2])-1<t5_t101_mem0*ADD_mem[2]
	S += (t5_t21*ADD[3])-1<t5_t101_mem0*ADD_mem[3]
	S += t5_t101_mem0<=t5_t101

	t5_t101_mem1 = S.Task('t5_t101_mem1', length=1, delay_cost=1)
	t5_t101_mem1 += alt(ADD_mem)
	S += (t5_t20*ADD[0])-1<t5_t101_mem1*ADD_mem[0]
	S += (t5_t20*ADD[1])-1<t5_t101_mem1*ADD_mem[1]
	S += (t5_t20*ADD[2])-1<t5_t101_mem1*ADD_mem[2]
	S += (t5_t20*ADD[3])-1<t5_t101_mem1*ADD_mem[3]
	S += t5_t101_mem1<=t5_t101

	t5_t61 = S.Task('t5_t61', length=1, delay_cost=1)
	t5_t61 += alt(ADD)

	t5_t61_mem0 = S.Task('t5_t61_mem0', length=1, delay_cost=1)
	t5_t61_mem0 += alt(MUL_mem)
	S += (t5_t6_t4*MUL[0])-1<t5_t61_mem0*MUL_mem[0]
	S += t5_t61_mem0<=t5_t61

	t5_t61_mem1 = S.Task('t5_t61_mem1', length=1, delay_cost=1)
	t5_t61_mem1 += alt(ADD_mem)
	S += (t5_t6_t5*ADD[0])-1<t5_t61_mem1*ADD_mem[0]
	S += (t5_t6_t5*ADD[1])-1<t5_t61_mem1*ADD_mem[1]
	S += (t5_t6_t5*ADD[2])-1<t5_t61_mem1*ADD_mem[2]
	S += (t5_t6_t5*ADD[3])-1<t5_t61_mem1*ADD_mem[3]
	S += t5_t61_mem1<=t5_t61

	t5_t71 = S.Task('t5_t71', length=1, delay_cost=1)
	t5_t71 += alt(ADD)

	t5_t71_mem0 = S.Task('t5_t71_mem0', length=1, delay_cost=1)
	t5_t71_mem0 += alt(ADD_mem)
	S += (t5_t01*ADD[0])-1<t5_t71_mem0*ADD_mem[0]
	S += (t5_t01*ADD[1])-1<t5_t71_mem0*ADD_mem[1]
	S += (t5_t01*ADD[2])-1<t5_t71_mem0*ADD_mem[2]
	S += (t5_t01*ADD[3])-1<t5_t71_mem0*ADD_mem[3]
	S += t5_t71_mem0<=t5_t71

	t5_t71_mem1 = S.Task('t5_t71_mem1', length=1, delay_cost=1)
	t5_t71_mem1 += alt(ADD_mem)
	S += (t5_t11*ADD[0])-1<t5_t71_mem1*ADD_mem[0]
	S += (t5_t11*ADD[1])-1<t5_t71_mem1*ADD_mem[1]
	S += (t5_t11*ADD[2])-1<t5_t71_mem1*ADD_mem[2]
	S += (t5_t11*ADD[3])-1<t5_t71_mem1*ADD_mem[3]
	S += t5_t71_mem1<=t5_t71

	t510 = S.Task('t510', length=1, delay_cost=1)
	t510 += alt(ADD)

	t510_mem0 = S.Task('t510_mem0', length=1, delay_cost=1)
	t510_mem0 += alt(ADD_mem)
	S += (t5_t60*ADD[0])-1<t510_mem0*ADD_mem[0]
	S += (t5_t60*ADD[1])-1<t510_mem0*ADD_mem[1]
	S += (t5_t60*ADD[2])-1<t510_mem0*ADD_mem[2]
	S += (t5_t60*ADD[3])-1<t510_mem0*ADD_mem[3]
	S += t510_mem0<=t510

	t510_mem1 = S.Task('t510_mem1', length=1, delay_cost=1)
	t510_mem1 += alt(ADD_mem)
	S += (t5_t70*ADD[0])-1<t510_mem1*ADD_mem[0]
	S += (t5_t70*ADD[1])-1<t510_mem1*ADD_mem[1]
	S += (t5_t70*ADD[2])-1<t510_mem1*ADD_mem[2]
	S += (t5_t70*ADD[3])-1<t510_mem1*ADD_mem[3]
	S += t510_mem1<=t510

	t521 = S.Task('t521', length=1, delay_cost=1)
	t521 += alt(ADD)

	t521_mem0 = S.Task('t521_mem0', length=1, delay_cost=1)
	t521_mem0 += alt(ADD_mem)
	S += (t5_t81*ADD[0])-1<t521_mem0*ADD_mem[0]
	S += (t5_t81*ADD[1])-1<t521_mem0*ADD_mem[1]
	S += (t5_t81*ADD[2])-1<t521_mem0*ADD_mem[2]
	S += (t5_t81*ADD[3])-1<t521_mem0*ADD_mem[3]
	S += t521_mem0<=t521

	t521_mem1 = S.Task('t521_mem1', length=1, delay_cost=1)
	t521_mem1 += alt(ADD_mem)
	S += (t5_t11*ADD[0])-1<t521_mem1*ADD_mem[0]
	S += (t5_t11*ADD[1])-1<t521_mem1*ADD_mem[1]
	S += (t5_t11*ADD[2])-1<t521_mem1*ADD_mem[2]
	S += (t5_t11*ADD[3])-1<t521_mem1*ADD_mem[3]
	S += t521_mem1<=t521

	t150 = S.Task('t150', length=1, delay_cost=1)
	t150 += alt(ADD)

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += ADD_mem[0]
	S += 22<t150_mem0
	S += t150_mem0<=t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(ADD_mem)
	S += (t410*ADD[0])-1<t150_mem1*ADD_mem[0]
	S += (t410*ADD[1])-1<t150_mem1*ADD_mem[1]
	S += (t410*ADD[2])-1<t150_mem1*ADD_mem[2]
	S += (t410*ADD[3])-1<t150_mem1*ADD_mem[3]
	S += t150_mem1<=t150

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(ADD)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += alt(ADD_mem)
	S += (t21*ADD[0])-1<t161_mem0*ADD_mem[0]
	S += (t21*ADD[1])-1<t161_mem0*ADD_mem[1]
	S += (t21*ADD[2])-1<t161_mem0*ADD_mem[2]
	S += (t21*ADD[3])-1<t161_mem0*ADD_mem[3]
	S += t161_mem0<=t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += alt(ADD_mem)
	S += (t421*ADD[0])-1<t161_mem1*ADD_mem[0]
	S += (t421*ADD[1])-1<t161_mem1*ADD_mem[1]
	S += (t421*ADD[2])-1<t161_mem1*ADD_mem[2]
	S += (t421*ADD[3])-1<t161_mem1*ADD_mem[3]
	S += t161_mem1<=t161

	t500 = S.Task('t500', length=1, delay_cost=1)
	t500 += alt(ADD)

	t500_mem0 = S.Task('t500_mem0', length=1, delay_cost=1)
	t500_mem0 += alt(ADD_mem)
	S += (t5_t00*ADD[0])-1<t500_mem0*ADD_mem[0]
	S += (t5_t00*ADD[1])-1<t500_mem0*ADD_mem[1]
	S += (t5_t00*ADD[2])-1<t500_mem0*ADD_mem[2]
	S += (t5_t00*ADD[3])-1<t500_mem0*ADD_mem[3]
	S += t500_mem0<=t500

	t500_mem1 = S.Task('t500_mem1', length=1, delay_cost=1)
	t500_mem1 += alt(ADD_mem)
	S += (t5_t100*ADD[0])-1<t500_mem1*ADD_mem[0]
	S += (t5_t100*ADD[1])-1<t500_mem1*ADD_mem[1]
	S += (t5_t100*ADD[2])-1<t500_mem1*ADD_mem[2]
	S += (t5_t100*ADD[3])-1<t500_mem1*ADD_mem[3]
	S += t500_mem1<=t500

	t501 = S.Task('t501', length=1, delay_cost=1)
	t501 += alt(ADD)

	t501_mem0 = S.Task('t501_mem0', length=1, delay_cost=1)
	t501_mem0 += alt(ADD_mem)
	S += (t5_t01*ADD[0])-1<t501_mem0*ADD_mem[0]
	S += (t5_t01*ADD[1])-1<t501_mem0*ADD_mem[1]
	S += (t5_t01*ADD[2])-1<t501_mem0*ADD_mem[2]
	S += (t5_t01*ADD[3])-1<t501_mem0*ADD_mem[3]
	S += t501_mem0<=t501

	t501_mem1 = S.Task('t501_mem1', length=1, delay_cost=1)
	t501_mem1 += alt(ADD_mem)
	S += (t5_t101*ADD[0])-1<t501_mem1*ADD_mem[0]
	S += (t5_t101*ADD[1])-1<t501_mem1*ADD_mem[1]
	S += (t5_t101*ADD[2])-1<t501_mem1*ADD_mem[2]
	S += (t5_t101*ADD[3])-1<t501_mem1*ADD_mem[3]
	S += t501_mem1<=t501

	t511 = S.Task('t511', length=1, delay_cost=1)
	t511 += alt(ADD)

	t511_mem0 = S.Task('t511_mem0', length=1, delay_cost=1)
	t511_mem0 += alt(ADD_mem)
	S += (t5_t61*ADD[0])-1<t511_mem0*ADD_mem[0]
	S += (t5_t61*ADD[1])-1<t511_mem0*ADD_mem[1]
	S += (t5_t61*ADD[2])-1<t511_mem0*ADD_mem[2]
	S += (t5_t61*ADD[3])-1<t511_mem0*ADD_mem[3]
	S += t511_mem0<=t511

	t511_mem1 = S.Task('t511_mem1', length=1, delay_cost=1)
	t511_mem1 += alt(ADD_mem)
	S += (t5_t71*ADD[0])-1<t511_mem1*ADD_mem[0]
	S += (t5_t71*ADD[1])-1<t511_mem1*ADD_mem[1]
	S += (t5_t71*ADD[2])-1<t511_mem1*ADD_mem[2]
	S += (t5_t71*ADD[3])-1<t511_mem1*ADD_mem[3]
	S += t511_mem1<=t511

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(ADD)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(ADD_mem)
	S += (t30*ADD[0])-1<t140_mem0*ADD_mem[0]
	S += (t30*ADD[1])-1<t140_mem0*ADD_mem[1]
	S += (t30*ADD[2])-1<t140_mem0*ADD_mem[2]
	S += (t30*ADD[3])-1<t140_mem0*ADD_mem[3]
	S += t140_mem0<=t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(ADD_mem)
	S += (t400*ADD[0])-1<t140_mem1*ADD_mem[0]
	S += (t400*ADD[1])-1<t140_mem1*ADD_mem[1]
	S += (t400*ADD[2])-1<t140_mem1*ADD_mem[2]
	S += (t400*ADD[3])-1<t140_mem1*ADD_mem[3]
	S += t140_mem1<=t140

	t141 = S.Task('t141', length=1, delay_cost=1)
	t141 += alt(ADD)

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += alt(ADD_mem)
	S += (t31*ADD[0])-1<t141_mem0*ADD_mem[0]
	S += (t31*ADD[1])-1<t141_mem0*ADD_mem[1]
	S += (t31*ADD[2])-1<t141_mem0*ADD_mem[2]
	S += (t31*ADD[3])-1<t141_mem0*ADD_mem[3]
	S += t141_mem0<=t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(ADD_mem)
	S += (t401*ADD[0])-1<t141_mem1*ADD_mem[0]
	S += (t401*ADD[1])-1<t141_mem1*ADD_mem[1]
	S += (t401*ADD[2])-1<t141_mem1*ADD_mem[2]
	S += (t401*ADD[3])-1<t141_mem1*ADD_mem[3]
	S += t141_mem1<=t141

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(ADD)

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(ADD_mem)
	S += (t11*ADD[0])-1<t151_mem0*ADD_mem[0]
	S += (t11*ADD[1])-1<t151_mem0*ADD_mem[1]
	S += (t11*ADD[2])-1<t151_mem0*ADD_mem[2]
	S += (t11*ADD[3])-1<t151_mem0*ADD_mem[3]
	S += t151_mem0<=t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(ADD_mem)
	S += (t411*ADD[0])-1<t151_mem1*ADD_mem[0]
	S += (t411*ADD[1])-1<t151_mem1*ADD_mem[1]
	S += (t411*ADD[2])-1<t151_mem1*ADD_mem[2]
	S += (t411*ADD[3])-1<t151_mem1*ADD_mem[3]
	S += t151_mem1<=t151

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(ADD)

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += ADD_mem[0]
	S += 22<c110_mem0
	S += c110_mem0<=c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += alt(ADD_mem)
	S += (t420*ADD[0])-1<c110_mem1*ADD_mem[0]
	S += (t420*ADD[1])-1<c110_mem1*ADD_mem[1]
	S += (t420*ADD[2])-1<c110_mem1*ADD_mem[2]
	S += (t420*ADD[3])-1<c110_mem1*ADD_mem[3]
	S += c110_mem1<=c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(INPUT_mem_w)
	S += c110-1 <= c110_w

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(ADD)

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += alt(ADD_mem)
	S += (t520*ADD[0])-1<c210_mem0*ADD_mem[0]
	S += (t520*ADD[1])-1<c210_mem0*ADD_mem[1]
	S += (t520*ADD[2])-1<c210_mem0*ADD_mem[2]
	S += (t520*ADD[3])-1<c210_mem0*ADD_mem[3]
	S += c210_mem0<=c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += alt(ADD_mem)
	S += (t160*ADD[0])-1<c210_mem1*ADD_mem[0]
	S += (t160*ADD[1])-1<c210_mem1*ADD_mem[1]
	S += (t160*ADD[2])-1<c210_mem1*ADD_mem[2]
	S += (t160*ADD[3])-1<c210_mem1*ADD_mem[3]
	S += c210_mem1<=c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(INPUT_mem_w)
	S += c210-1 <= c210_w

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(ADD)

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(ADD_mem)
	S += (t30*ADD[0])-1<c200_mem0*ADD_mem[0]
	S += (t30*ADD[1])-1<c200_mem0*ADD_mem[1]
	S += (t30*ADD[2])-1<c200_mem0*ADD_mem[2]
	S += (t30*ADD[3])-1<c200_mem0*ADD_mem[3]
	S += c200_mem0<=c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += alt(ADD_mem)
	S += (t410*ADD[0])-1<c200_mem1*ADD_mem[0]
	S += (t410*ADD[1])-1<c200_mem1*ADD_mem[1]
	S += (t410*ADD[2])-1<c200_mem1*ADD_mem[2]
	S += (t410*ADD[3])-1<c200_mem1*ADD_mem[3]
	S += c200_mem1<=c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200-1 <= c200_w

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(ADD)

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(ADD_mem)
	S += (t11*ADD[0])-1<c111_mem0*ADD_mem[0]
	S += (t11*ADD[1])-1<c111_mem0*ADD_mem[1]
	S += (t11*ADD[2])-1<c111_mem0*ADD_mem[2]
	S += (t11*ADD[3])-1<c111_mem0*ADD_mem[3]
	S += c111_mem0<=c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += alt(ADD_mem)
	S += (t421*ADD[0])-1<c111_mem1*ADD_mem[0]
	S += (t421*ADD[1])-1<c111_mem1*ADD_mem[1]
	S += (t421*ADD[2])-1<c111_mem1*ADD_mem[2]
	S += (t421*ADD[3])-1<c111_mem1*ADD_mem[3]
	S += c111_mem1<=c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(INPUT_mem_w)
	S += c111-1 <= c111_w

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(ADD)

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(ADD_mem)
	S += (t510*ADD[0])-1<c010_mem0*ADD_mem[0]
	S += (t510*ADD[1])-1<c010_mem0*ADD_mem[1]
	S += (t510*ADD[2])-1<c010_mem0*ADD_mem[2]
	S += (t510*ADD[3])-1<c010_mem0*ADD_mem[3]
	S += c010_mem0<=c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(ADD_mem)
	S += (t150*ADD[0])-1<c010_mem1*ADD_mem[0]
	S += (t150*ADD[1])-1<c010_mem1*ADD_mem[1]
	S += (t150*ADD[2])-1<c010_mem1*ADD_mem[2]
	S += (t150*ADD[3])-1<c010_mem1*ADD_mem[3]
	S += c010_mem1<=c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010-1 <= c010_w

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(ADD)

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(ADD_mem)
	S += (t521*ADD[0])-1<c211_mem0*ADD_mem[0]
	S += (t521*ADD[1])-1<c211_mem0*ADD_mem[1]
	S += (t521*ADD[2])-1<c211_mem0*ADD_mem[2]
	S += (t521*ADD[3])-1<c211_mem0*ADD_mem[3]
	S += c211_mem0<=c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(ADD_mem)
	S += (t161*ADD[0])-1<c211_mem1*ADD_mem[0]
	S += (t161*ADD[1])-1<c211_mem1*ADD_mem[1]
	S += (t161*ADD[2])-1<c211_mem1*ADD_mem[2]
	S += (t161*ADD[3])-1<c211_mem1*ADD_mem[3]
	S += c211_mem1<=c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(INPUT_mem_w)
	S += c211-1 <= c211_w

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(ADD)

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(ADD_mem)
	S += (t170*ADD[0])-1<c000_mem0*ADD_mem[0]
	S += (t170*ADD[1])-1<c000_mem0*ADD_mem[1]
	S += (t170*ADD[2])-1<c000_mem0*ADD_mem[2]
	S += (t170*ADD[3])-1<c000_mem0*ADD_mem[3]
	S += c000_mem0<=c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(ADD_mem)
	S += (t400*ADD[0])-1<c000_mem1*ADD_mem[0]
	S += (t400*ADD[1])-1<c000_mem1*ADD_mem[1]
	S += (t400*ADD[2])-1<c000_mem1*ADD_mem[2]
	S += (t400*ADD[3])-1<c000_mem1*ADD_mem[3]
	S += c000_mem1<=c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(INPUT_mem_w)
	S += c000-1 <= c000_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(ADD)

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(ADD_mem)
	S += (t171*ADD[0])-1<c001_mem0*ADD_mem[0]
	S += (t171*ADD[1])-1<c001_mem0*ADD_mem[1]
	S += (t171*ADD[2])-1<c001_mem0*ADD_mem[2]
	S += (t171*ADD[3])-1<c001_mem0*ADD_mem[3]
	S += c001_mem0<=c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(ADD_mem)
	S += (t401*ADD[0])-1<c001_mem1*ADD_mem[0]
	S += (t401*ADD[1])-1<c001_mem1*ADD_mem[1]
	S += (t401*ADD[2])-1<c001_mem1*ADD_mem[2]
	S += (t401*ADD[3])-1<c001_mem1*ADD_mem[3]
	S += c001_mem1<=c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(INPUT_mem_w)
	S += c001-1 <= c001_w

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(ADD)

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(ADD_mem)
	S += (t31*ADD[0])-1<c201_mem0*ADD_mem[0]
	S += (t31*ADD[1])-1<c201_mem0*ADD_mem[1]
	S += (t31*ADD[2])-1<c201_mem0*ADD_mem[2]
	S += (t31*ADD[3])-1<c201_mem0*ADD_mem[3]
	S += c201_mem0<=c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(ADD_mem)
	S += (t411*ADD[0])-1<c201_mem1*ADD_mem[0]
	S += (t411*ADD[1])-1<c201_mem1*ADD_mem[1]
	S += (t411*ADD[2])-1<c201_mem1*ADD_mem[2]
	S += (t411*ADD[3])-1<c201_mem1*ADD_mem[3]
	S += c201_mem1<=c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201-1 <= c201_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(ADD)

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(ADD_mem)
	S += (t500*ADD[0])-1<c100_mem0*ADD_mem[0]
	S += (t500*ADD[1])-1<c100_mem0*ADD_mem[1]
	S += (t500*ADD[2])-1<c100_mem0*ADD_mem[2]
	S += (t500*ADD[3])-1<c100_mem0*ADD_mem[3]
	S += c100_mem0<=c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += alt(ADD_mem)
	S += (t140*ADD[0])-1<c100_mem1*ADD_mem[0]
	S += (t140*ADD[1])-1<c100_mem1*ADD_mem[1]
	S += (t140*ADD[2])-1<c100_mem1*ADD_mem[2]
	S += (t140*ADD[3])-1<c100_mem1*ADD_mem[3]
	S += c100_mem1<=c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(INPUT_mem_w)
	S += c100-1 <= c100_w

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(ADD)

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(ADD_mem)
	S += (t501*ADD[0])-1<c101_mem0*ADD_mem[0]
	S += (t501*ADD[1])-1<c101_mem0*ADD_mem[1]
	S += (t501*ADD[2])-1<c101_mem0*ADD_mem[2]
	S += (t501*ADD[3])-1<c101_mem0*ADD_mem[3]
	S += c101_mem0<=c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(ADD_mem)
	S += (t141*ADD[0])-1<c101_mem1*ADD_mem[0]
	S += (t141*ADD[1])-1<c101_mem1*ADD_mem[1]
	S += (t141*ADD[2])-1<c101_mem1*ADD_mem[2]
	S += (t141*ADD[3])-1<c101_mem1*ADD_mem[3]
	S += c101_mem1<=c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(INPUT_mem_w)
	S += c101-1 <= c101_w

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(ADD)

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(ADD_mem)
	S += (t511*ADD[0])-1<c011_mem0*ADD_mem[0]
	S += (t511*ADD[1])-1<c011_mem0*ADD_mem[1]
	S += (t511*ADD[2])-1<c011_mem0*ADD_mem[2]
	S += (t511*ADD[3])-1<c011_mem0*ADD_mem[3]
	S += c011_mem0<=c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(ADD_mem)
	S += (t151*ADD[0])-1<c011_mem1*ADD_mem[0]
	S += (t151*ADD[1])-1<c011_mem1*ADD_mem[1]
	S += (t151*ADD[2])-1<c011_mem1*ADD_mem[2]
	S += (t151*ADD[3])-1<c011_mem1*ADD_mem[3]
	S += c011_mem1<=c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(INPUT_mem_w)
	S += c011-1 <= c011_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "SPARSE_M_mul1_add4/SPARSE_M_mul1_add4_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

