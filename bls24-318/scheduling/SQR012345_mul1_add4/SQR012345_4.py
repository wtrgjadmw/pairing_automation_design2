from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 165
	S = Scenario("SQR012345_4", horizon=horizon)

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

	t3_t10_mem0 = S.Task('t3_t10_mem0', length=1, delay_cost=1)
	S += t3_t10_mem0 >= 9
	t3_t10_mem0 += MUL_mem[0]

	t3_t10_mem1 = S.Task('t3_t10_mem1', length=1, delay_cost=1)
	S += t3_t10_mem1 >= 9
	t3_t10_mem1 += MUL_mem[0]

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

	t3_t10 = S.Task('t3_t10', length=1, delay_cost=1)
	S += t3_t10 >= 10
	t3_t10 += ADD[0]

	t4_t3_t5_mem0 = S.Task('t4_t3_t5_mem0', length=1, delay_cost=1)
	S += t4_t3_t5_mem0 >= 10
	t4_t3_t5_mem0 += MUL_mem[0]

	t4_t3_t5_mem1 = S.Task('t4_t3_t5_mem1', length=1, delay_cost=1)
	S += t4_t3_t5_mem1 >= 10
	t4_t3_t5_mem1 += MUL_mem[0]

	t0_t10_mem0 = S.Task('t0_t10_mem0', length=1, delay_cost=1)
	S += t0_t10_mem0 >= 11
	t0_t10_mem0 += INPUT_mem_r

	t0_t10_mem1 = S.Task('t0_t10_mem1', length=1, delay_cost=1)
	S += t0_t10_mem1 >= 11
	t0_t10_mem1 += INPUT_mem_r

	t0_t3_t3 = S.Task('t0_t3_t3', length=1, delay_cost=1)
	S += t0_t3_t3 >= 11
	t0_t3_t3 += ADD[0]

	t3_t1_t5_mem0 = S.Task('t3_t1_t5_mem0', length=1, delay_cost=1)
	S += t3_t1_t5_mem0 >= 11
	t3_t1_t5_mem0 += MUL_mem[0]

	t3_t1_t5_mem1 = S.Task('t3_t1_t5_mem1', length=1, delay_cost=1)
	S += t3_t1_t5_mem1 >= 11
	t3_t1_t5_mem1 += MUL_mem[0]

	t4_t3_t5 = S.Task('t4_t3_t5', length=1, delay_cost=1)
	S += t4_t3_t5 >= 11
	t4_t3_t5 += ADD[3]

	t0_t10 = S.Task('t0_t10', length=1, delay_cost=1)
	S += t0_t10 >= 12
	t0_t10 += ADD[3]

	t0_t2_t3_mem0 = S.Task('t0_t2_t3_mem0', length=1, delay_cost=1)
	S += t0_t2_t3_mem0 >= 12
	t0_t2_t3_mem0 += ADD_mem[3]

	t0_t2_t3_mem1 = S.Task('t0_t2_t3_mem1', length=1, delay_cost=1)
	S += t0_t2_t3_mem1 >= 12
	t0_t2_t3_mem1 += ADD_mem[2]

	t3_t00_mem0 = S.Task('t3_t00_mem0', length=1, delay_cost=1)
	S += t3_t00_mem0 >= 12
	t3_t00_mem0 += MUL_mem[0]

	t3_t00_mem1 = S.Task('t3_t00_mem1', length=1, delay_cost=1)
	S += t3_t00_mem1 >= 12
	t3_t00_mem1 += MUL_mem[0]

	t3_t1_t5 = S.Task('t3_t1_t5', length=1, delay_cost=1)
	S += t3_t1_t5 >= 12
	t3_t1_t5 += ADD[0]

	t3_t30_mem0 = S.Task('t3_t30_mem0', length=1, delay_cost=1)
	S += t3_t30_mem0 >= 12
	t3_t30_mem0 += INPUT_mem_r

	t3_t30_mem1 = S.Task('t3_t30_mem1', length=1, delay_cost=1)
	S += t3_t30_mem1 >= 12
	t3_t30_mem1 += INPUT_mem_r

	t0_t2_t3 = S.Task('t0_t2_t3', length=1, delay_cost=1)
	S += t0_t2_t3 >= 13
	t0_t2_t3 += ADD[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 13
	t100_mem0 += INPUT_mem_r

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 13
	t100_mem1 += INPUT_mem_r

	t3_t00 = S.Task('t3_t00', length=1, delay_cost=1)
	S += t3_t00 >= 13
	t3_t00 += ADD[1]

	t3_t0_t5_mem0 = S.Task('t3_t0_t5_mem0', length=1, delay_cost=1)
	S += t3_t0_t5_mem0 >= 13
	t3_t0_t5_mem0 += MUL_mem[0]

	t3_t0_t5_mem1 = S.Task('t3_t0_t5_mem1', length=1, delay_cost=1)
	S += t3_t0_t5_mem1 >= 13
	t3_t0_t5_mem1 += MUL_mem[0]

	t3_t30 = S.Task('t3_t30', length=1, delay_cost=1)
	S += t3_t30 >= 13
	t3_t30 += ADD[0]

	t0_t30_mem0 = S.Task('t0_t30_mem0', length=1, delay_cost=1)
	S += t0_t30_mem0 >= 14
	t0_t30_mem0 += MUL_mem[0]

	t0_t30_mem1 = S.Task('t0_t30_mem1', length=1, delay_cost=1)
	S += t0_t30_mem1 >= 14
	t0_t30_mem1 += MUL_mem[0]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 14
	t100 += ADD[2]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 14
	t101_mem0 += INPUT_mem_r

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 14
	t101_mem1 += INPUT_mem_r

	t3_t0_t5 = S.Task('t3_t0_t5', length=1, delay_cost=1)
	S += t3_t0_t5 >= 14
	t3_t0_t5 += ADD[1]

	t0_t30 = S.Task('t0_t30', length=1, delay_cost=1)
	S += t0_t30 >= 15
	t0_t30 += ADD[0]

	t0_t3_t5_mem0 = S.Task('t0_t3_t5_mem0', length=1, delay_cost=1)
	S += t0_t3_t5_mem0 >= 15
	t0_t3_t5_mem0 += MUL_mem[0]

	t0_t3_t5_mem1 = S.Task('t0_t3_t5_mem1', length=1, delay_cost=1)
	S += t0_t3_t5_mem1 >= 15
	t0_t3_t5_mem1 += MUL_mem[0]

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

	t0_t3_t5 = S.Task('t0_t3_t5', length=1, delay_cost=1)
	S += t0_t3_t5 >= 16
	t0_t3_t5 += ADD[1]

	t3_t20 = S.Task('t3_t20', length=1, delay_cost=1)
	S += t3_t20 >= 16
	t3_t20 += ADD[3]

	t3_t4_t0_in = S.Task('t3_t4_t0_in', length=1, delay_cost=1)
	S += t3_t4_t0_in >= 16
	t3_t4_t0_in += MUL_in[0]

	t3_t4_t0_mem0 = S.Task('t3_t4_t0_mem0', length=1, delay_cost=1)
	S += t3_t4_t0_mem0 >= 16
	t3_t4_t0_mem0 += ADD_mem[3]

	t3_t4_t0_mem1 = S.Task('t3_t4_t0_mem1', length=1, delay_cost=1)
	S += t3_t4_t0_mem1 >= 16
	t3_t4_t0_mem1 += ADD_mem[0]

	t4_t30_mem0 = S.Task('t4_t30_mem0', length=1, delay_cost=1)
	S += t4_t30_mem0 >= 16
	t4_t30_mem0 += MUL_mem[0]

	t4_t30_mem1 = S.Task('t4_t30_mem1', length=1, delay_cost=1)
	S += t4_t30_mem1 >= 16
	t4_t30_mem1 += MUL_mem[0]

	t0_a1_0 = S.Task('t0_a1_0', length=1, delay_cost=1)
	S += t0_a1_0 >= 17
	t0_a1_0 += ADD[1]

	t3_t4_t0 = S.Task('t3_t4_t0', length=7, delay_cost=1)
	S += t3_t4_t0 >= 17
	t3_t4_t0 += MUL[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 17
	t4_t10_mem0 += INPUT_mem_r

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 17
	t4_t10_mem1 += INPUT_mem_r

	t4_t30 = S.Task('t4_t30', length=1, delay_cost=1)
	S += t4_t30 >= 17
	t4_t30 += ADD[0]

	t3_t21_mem0 = S.Task('t3_t21_mem0', length=1, delay_cost=1)
	S += t3_t21_mem0 >= 18
	t3_t21_mem0 += INPUT_mem_r

	t3_t21_mem1 = S.Task('t3_t21_mem1', length=1, delay_cost=1)
	S += t3_t21_mem1 >= 18
	t3_t21_mem1 += INPUT_mem_r

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	S += t4_t10 >= 18
	t4_t10 += ADD[0]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 18
	t4_t2_t3_mem0 += ADD_mem[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 18
	t4_t2_t3_mem1 += ADD_mem[0]

	t3_t21 = S.Task('t3_t21', length=1, delay_cost=1)
	S += t3_t21 >= 19
	t3_t21 += ADD[0]

	t3_t4_t2_mem0 = S.Task('t3_t4_t2_mem0', length=1, delay_cost=1)
	S += t3_t4_t2_mem0 >= 19
	t3_t4_t2_mem0 += ADD_mem[3]

	t3_t4_t2_mem1 = S.Task('t3_t4_t2_mem1', length=1, delay_cost=1)
	S += t3_t4_t2_mem1 >= 19
	t3_t4_t2_mem1 += ADD_mem[0]

	t4_a1_0_mem0 = S.Task('t4_a1_0_mem0', length=1, delay_cost=1)
	S += t4_a1_0_mem0 >= 19
	t4_a1_0_mem0 += INPUT_mem_r

	t4_a1_0_mem1 = S.Task('t4_a1_0_mem1', length=1, delay_cost=1)
	S += t4_a1_0_mem1 >= 19
	t4_a1_0_mem1 += INPUT_mem_r

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 19
	t4_t2_t3 += ADD[1]

	t3_t31_mem0 = S.Task('t3_t31_mem0', length=1, delay_cost=1)
	S += t3_t31_mem0 >= 20
	t3_t31_mem0 += INPUT_mem_r

	t3_t31_mem1 = S.Task('t3_t31_mem1', length=1, delay_cost=1)
	S += t3_t31_mem1 >= 20
	t3_t31_mem1 += INPUT_mem_r

	t3_t4_t2 = S.Task('t3_t4_t2', length=1, delay_cost=1)
	S += t3_t4_t2 >= 20
	t3_t4_t2 += ADD[0]

	t4_a1_0 = S.Task('t4_a1_0', length=1, delay_cost=1)
	S += t4_a1_0 >= 20
	t4_a1_0 += ADD[3]

	t3_t31 = S.Task('t3_t31', length=1, delay_cost=1)
	S += t3_t31 >= 21
	t3_t31 += ADD[1]

	t3_t4_t1_in = S.Task('t3_t4_t1_in', length=1, delay_cost=1)
	S += t3_t4_t1_in >= 21
	t3_t4_t1_in += MUL_in[0]

	t3_t4_t1_mem0 = S.Task('t3_t4_t1_mem0', length=1, delay_cost=1)
	S += t3_t4_t1_mem0 >= 21
	t3_t4_t1_mem0 += ADD_mem[0]

	t3_t4_t1_mem1 = S.Task('t3_t4_t1_mem1', length=1, delay_cost=1)
	S += t3_t4_t1_mem1 >= 21
	t3_t4_t1_mem1 += ADD_mem[1]

	t3_t4_t3_mem0 = S.Task('t3_t4_t3_mem0', length=1, delay_cost=1)
	S += t3_t4_t3_mem0 >= 21
	t3_t4_t3_mem0 += ADD_mem[0]

	t3_t4_t3_mem1 = S.Task('t3_t4_t3_mem1', length=1, delay_cost=1)
	S += t3_t4_t3_mem1 >= 21
	t3_t4_t3_mem1 += ADD_mem[1]

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

	t3_t4_t1 = S.Task('t3_t4_t1', length=7, delay_cost=1)
	S += t3_t4_t1 >= 22
	t3_t4_t1 += MUL[0]

	t3_t4_t3 = S.Task('t3_t4_t3', length=1, delay_cost=1)
	S += t3_t4_t3 >= 22
	t3_t4_t3 += ADD[1]

	t4_a1_1 = S.Task('t4_a1_1', length=1, delay_cost=1)
	S += t4_a1_1 >= 22
	t4_a1_1 += ADD[0]

	t0_t3_t2 = S.Task('t0_t3_t2', length=1, delay_cost=1)
	S += t0_t3_t2 >= 23
	t0_t3_t2 += ADD[2]

	t0_t3_t4_in = S.Task('t0_t3_t4_in', length=1, delay_cost=1)
	S += t0_t3_t4_in >= 23
	t0_t3_t4_in += MUL_in[0]

	t0_t3_t4_mem0 = S.Task('t0_t3_t4_mem0', length=1, delay_cost=1)
	S += t0_t3_t4_mem0 >= 23
	t0_t3_t4_mem0 += ADD_mem[2]

	t0_t3_t4_mem1 = S.Task('t0_t3_t4_mem1', length=1, delay_cost=1)
	S += t0_t3_t4_mem1 >= 23
	t0_t3_t4_mem1 += ADD_mem[0]

	t3_t1_t3_mem0 = S.Task('t3_t1_t3_mem0', length=1, delay_cost=1)
	S += t3_t1_t3_mem0 >= 23
	t3_t1_t3_mem0 += INPUT_mem_r

	t3_t1_t3_mem1 = S.Task('t3_t1_t3_mem1', length=1, delay_cost=1)
	S += t3_t1_t3_mem1 >= 23
	t3_t1_t3_mem1 += INPUT_mem_r

	t0_t3_t4 = S.Task('t0_t3_t4', length=7, delay_cost=1)
	S += t0_t3_t4 >= 24
	t0_t3_t4 += MUL[0]

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

	t3_t1_t4_in = S.Task('t3_t1_t4_in', length=1, delay_cost=1)
	S += t3_t1_t4_in >= 25
	t3_t1_t4_in += MUL_in[0]

	t3_t1_t4_mem0 = S.Task('t3_t1_t4_mem0', length=1, delay_cost=1)
	S += t3_t1_t4_mem0 >= 25
	t3_t1_t4_mem0 += ADD_mem[3]

	t3_t1_t4_mem1 = S.Task('t3_t1_t4_mem1', length=1, delay_cost=1)
	S += t3_t1_t4_mem1 >= 25
	t3_t1_t4_mem1 += ADD_mem[1]

	t0_a1_1 = S.Task('t0_a1_1', length=1, delay_cost=1)
	S += t0_a1_1 >= 26
	t0_a1_1 += ADD[3]

	t3_t0_t3_mem0 = S.Task('t3_t0_t3_mem0', length=1, delay_cost=1)
	S += t3_t0_t3_mem0 >= 26
	t3_t0_t3_mem0 += INPUT_mem_r

	t3_t0_t3_mem1 = S.Task('t3_t0_t3_mem1', length=1, delay_cost=1)
	S += t3_t0_t3_mem1 >= 26
	t3_t0_t3_mem1 += INPUT_mem_r

	t3_t1_t4 = S.Task('t3_t1_t4', length=7, delay_cost=1)
	S += t3_t1_t4 >= 26
	t3_t1_t4 += MUL[0]

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

	t3_t0_t4_in = S.Task('t3_t0_t4_in', length=1, delay_cost=1)
	S += t3_t0_t4_in >= 28
	t3_t0_t4_in += MUL_in[0]

	t3_t0_t4_mem0 = S.Task('t3_t0_t4_mem0', length=1, delay_cost=1)
	S += t3_t0_t4_mem0 >= 28
	t3_t0_t4_mem0 += ADD_mem[0]

	t3_t0_t4_mem1 = S.Task('t3_t0_t4_mem1', length=1, delay_cost=1)
	S += t3_t0_t4_mem1 >= 28
	t3_t0_t4_mem1 += ADD_mem[2]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 29
	t110_mem0 += INPUT_mem_r

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 29
	t110_mem1 += INPUT_mem_r

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 29
	t111 += ADD[3]

	t3_t0_t4 = S.Task('t3_t0_t4', length=7, delay_cost=1)
	S += t3_t0_t4 >= 29
	t3_t0_t4 += MUL[0]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 30
	t110 += ADD[2]

	t7_t0_t0_in = S.Task('t7_t0_t0_in', length=1, delay_cost=1)
	S += t7_t0_t0_in >= 30
	t7_t0_t0_in += MUL_in[0]

	t7_t0_t0_mem0 = S.Task('t7_t0_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_t0_mem0 >= 30
	t7_t0_t0_mem0 += INPUT_mem_r

	t7_t0_t0_mem1 = S.Task('t7_t0_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_t0_mem1 >= 30
	t7_t0_t0_mem1 += INPUT_mem_r

	t6_t1_t1_in = S.Task('t6_t1_t1_in', length=1, delay_cost=1)
	S += t6_t1_t1_in >= 31
	t6_t1_t1_in += MUL_in[0]

	t6_t1_t1_mem0 = S.Task('t6_t1_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_t1_mem0 >= 31
	t6_t1_t1_mem0 += INPUT_mem_r

	t6_t1_t1_mem1 = S.Task('t6_t1_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_t1_mem1 >= 31
	t6_t1_t1_mem1 += INPUT_mem_r

	t7_t0_t0 = S.Task('t7_t0_t0', length=7, delay_cost=1)
	S += t7_t0_t0 >= 31
	t7_t0_t0 += MUL[0]

	t6_t1_t0_in = S.Task('t6_t1_t0_in', length=1, delay_cost=1)
	S += t6_t1_t0_in >= 32
	t6_t1_t0_in += MUL_in[0]

	t6_t1_t0_mem0 = S.Task('t6_t1_t0_mem0', length=1, delay_cost=1)
	S += t6_t1_t0_mem0 >= 32
	t6_t1_t0_mem0 += INPUT_mem_r

	t6_t1_t0_mem1 = S.Task('t6_t1_t0_mem1', length=1, delay_cost=1)
	S += t6_t1_t0_mem1 >= 32
	t6_t1_t0_mem1 += INPUT_mem_r

	t6_t1_t1 = S.Task('t6_t1_t1', length=7, delay_cost=1)
	S += t6_t1_t1 >= 32
	t6_t1_t1 += MUL[0]

	t6_t1_t0 = S.Task('t6_t1_t0', length=7, delay_cost=1)
	S += t6_t1_t0 >= 33
	t6_t1_t0 += MUL[0]

	t7_t0_t1_in = S.Task('t7_t0_t1_in', length=1, delay_cost=1)
	S += t7_t0_t1_in >= 33
	t7_t0_t1_in += MUL_in[0]

	t7_t0_t1_mem0 = S.Task('t7_t0_t1_mem0', length=1, delay_cost=1)
	S += t7_t0_t1_mem0 >= 33
	t7_t0_t1_mem0 += INPUT_mem_r

	t7_t0_t1_mem1 = S.Task('t7_t0_t1_mem1', length=1, delay_cost=1)
	S += t7_t0_t1_mem1 >= 33
	t7_t0_t1_mem1 += INPUT_mem_r

	t6_t0_t1_in = S.Task('t6_t0_t1_in', length=1, delay_cost=1)
	S += t6_t0_t1_in >= 34
	t6_t0_t1_in += MUL_in[0]

	t6_t0_t1_mem0 = S.Task('t6_t0_t1_mem0', length=1, delay_cost=1)
	S += t6_t0_t1_mem0 >= 34
	t6_t0_t1_mem0 += INPUT_mem_r

	t6_t0_t1_mem1 = S.Task('t6_t0_t1_mem1', length=1, delay_cost=1)
	S += t6_t0_t1_mem1 >= 34
	t6_t0_t1_mem1 += INPUT_mem_r

	t7_t0_t1 = S.Task('t7_t0_t1', length=7, delay_cost=1)
	S += t7_t0_t1 >= 34
	t7_t0_t1 += MUL[0]

	t6_t0_t0_in = S.Task('t6_t0_t0_in', length=1, delay_cost=1)
	S += t6_t0_t0_in >= 35
	t6_t0_t0_in += MUL_in[0]

	t6_t0_t0_mem0 = S.Task('t6_t0_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_t0_mem0 >= 35
	t6_t0_t0_mem0 += INPUT_mem_r

	t6_t0_t0_mem1 = S.Task('t6_t0_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_t0_mem1 >= 35
	t6_t0_t0_mem1 += INPUT_mem_r

	t6_t0_t1 = S.Task('t6_t0_t1', length=7, delay_cost=1)
	S += t6_t0_t1 >= 35
	t6_t0_t1 += MUL[0]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 36
	t5_t1_t1_in += MUL_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 36
	t5_t1_t1_mem0 += INPUT_mem_r

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 36
	t5_t1_t1_mem1 += INPUT_mem_r

	t6_t0_t0 = S.Task('t6_t0_t0', length=7, delay_cost=1)
	S += t6_t0_t0 >= 36
	t6_t0_t0 += MUL[0]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 37
	t5_t1_t0_in += MUL_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 37
	t5_t1_t0_mem0 += INPUT_mem_r

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 37
	t5_t1_t0_mem1 += INPUT_mem_r

	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	S += t5_t1_t1 >= 37
	t5_t1_t1 += MUL[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 38
	t5_t0_t1_in += MUL_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 38
	t5_t0_t1_mem0 += INPUT_mem_r

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 38
	t5_t0_t1_mem1 += INPUT_mem_r

	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	S += t5_t1_t0 >= 38
	t5_t1_t0 += MUL[0]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 39
	t5_t0_t0_in += MUL_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 39
	t5_t0_t0_mem0 += INPUT_mem_r

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 39
	t5_t0_t0_mem1 += INPUT_mem_r

	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	S += t5_t0_t1 >= 39
	t5_t0_t1 += MUL[0]

	t6_t1_t5_mem0 = S.Task('t6_t1_t5_mem0', length=1, delay_cost=1)
	S += t6_t1_t5_mem0 >= 39
	t6_t1_t5_mem0 += MUL_mem[0]

	t6_t1_t5_mem1 = S.Task('t6_t1_t5_mem1', length=1, delay_cost=1)
	S += t6_t1_t5_mem1 >= 39
	t6_t1_t5_mem1 += MUL_mem[0]

	t4_t3_t3_mem0 = S.Task('t4_t3_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_t3_mem0 >= 40
	t4_t3_t3_mem0 += INPUT_mem_r

	t4_t3_t3_mem1 = S.Task('t4_t3_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_t3_mem1 >= 40
	t4_t3_t3_mem1 += INPUT_mem_r

	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	S += t5_t0_t0 >= 40
	t5_t0_t0 += MUL[0]

	t6_t1_t5 = S.Task('t6_t1_t5', length=1, delay_cost=1)
	S += t6_t1_t5 >= 40
	t6_t1_t5 += ADD[0]

	t7_t0_t5_mem0 = S.Task('t7_t0_t5_mem0', length=1, delay_cost=1)
	S += t7_t0_t5_mem0 >= 40
	t7_t0_t5_mem0 += MUL_mem[0]

	t7_t0_t5_mem1 = S.Task('t7_t0_t5_mem1', length=1, delay_cost=1)
	S += t7_t0_t5_mem1 >= 40
	t7_t0_t5_mem1 += MUL_mem[0]

	t4_t3_t3 = S.Task('t4_t3_t3', length=1, delay_cost=1)
	S += t4_t3_t3 >= 41
	t4_t3_t3 += ADD[1]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 41
	t5_t1_t2_mem0 += INPUT_mem_r

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 41
	t5_t1_t2_mem1 += INPUT_mem_r

	t6_t10_mem0 = S.Task('t6_t10_mem0', length=1, delay_cost=1)
	S += t6_t10_mem0 >= 41
	t6_t10_mem0 += MUL_mem[0]

	t6_t10_mem1 = S.Task('t6_t10_mem1', length=1, delay_cost=1)
	S += t6_t10_mem1 >= 41
	t6_t10_mem1 += MUL_mem[0]

	t7_t0_t5 = S.Task('t7_t0_t5', length=1, delay_cost=1)
	S += t7_t0_t5 >= 41
	t7_t0_t5 += ADD[0]

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	S += t5_t1_t2 >= 42
	t5_t1_t2 += ADD[0]

	t6_t0_t5_mem0 = S.Task('t6_t0_t5_mem0', length=1, delay_cost=1)
	S += t6_t0_t5_mem0 >= 42
	t6_t0_t5_mem0 += MUL_mem[0]

	t6_t0_t5_mem1 = S.Task('t6_t0_t5_mem1', length=1, delay_cost=1)
	S += t6_t0_t5_mem1 >= 42
	t6_t0_t5_mem1 += MUL_mem[0]

	t6_t10 = S.Task('t6_t10', length=1, delay_cost=1)
	S += t6_t10 >= 42
	t6_t10 += ADD[1]

	t7_t0_t3_mem0 = S.Task('t7_t0_t3_mem0', length=1, delay_cost=1)
	S += t7_t0_t3_mem0 >= 42
	t7_t0_t3_mem0 += INPUT_mem_r

	t7_t0_t3_mem1 = S.Task('t7_t0_t3_mem1', length=1, delay_cost=1)
	S += t7_t0_t3_mem1 >= 42
	t7_t0_t3_mem1 += INPUT_mem_r

	t6_t0_t5 = S.Task('t6_t0_t5', length=1, delay_cost=1)
	S += t6_t0_t5 >= 43
	t6_t0_t5 += ADD[0]

	t7_t00_mem0 = S.Task('t7_t00_mem0', length=1, delay_cost=1)
	S += t7_t00_mem0 >= 43
	t7_t00_mem0 += MUL_mem[0]

	t7_t00_mem1 = S.Task('t7_t00_mem1', length=1, delay_cost=1)
	S += t7_t00_mem1 >= 43
	t7_t00_mem1 += MUL_mem[0]

	t7_t0_t2_mem0 = S.Task('t7_t0_t2_mem0', length=1, delay_cost=1)
	S += t7_t0_t2_mem0 >= 43
	t7_t0_t2_mem0 += INPUT_mem_r

	t7_t0_t2_mem1 = S.Task('t7_t0_t2_mem1', length=1, delay_cost=1)
	S += t7_t0_t2_mem1 >= 43
	t7_t0_t2_mem1 += INPUT_mem_r

	t7_t0_t3 = S.Task('t7_t0_t3', length=1, delay_cost=1)
	S += t7_t0_t3 >= 43
	t7_t0_t3 += ADD[1]

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	S += t5_t10_mem0 >= 44
	t5_t10_mem0 += MUL_mem[0]

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	S += t5_t10_mem1 >= 44
	t5_t10_mem1 += MUL_mem[0]

	t6_t31_mem0 = S.Task('t6_t31_mem0', length=1, delay_cost=1)
	S += t6_t31_mem0 >= 44
	t6_t31_mem0 += INPUT_mem_r

	t6_t31_mem1 = S.Task('t6_t31_mem1', length=1, delay_cost=1)
	S += t6_t31_mem1 >= 44
	t6_t31_mem1 += INPUT_mem_r

	t7_t00 = S.Task('t7_t00', length=1, delay_cost=1)
	S += t7_t00 >= 44
	t7_t00 += ADD[3]

	t7_t0_t2 = S.Task('t7_t0_t2', length=1, delay_cost=1)
	S += t7_t0_t2 >= 44
	t7_t0_t2 += ADD[0]

	t7_t0_t4_in = S.Task('t7_t0_t4_in', length=1, delay_cost=1)
	S += t7_t0_t4_in >= 44
	t7_t0_t4_in += MUL_in[0]

	t7_t0_t4_mem0 = S.Task('t7_t0_t4_mem0', length=1, delay_cost=1)
	S += t7_t0_t4_mem0 >= 44
	t7_t0_t4_mem0 += ADD_mem[0]

	t7_t0_t4_mem1 = S.Task('t7_t0_t4_mem1', length=1, delay_cost=1)
	S += t7_t0_t4_mem1 >= 44
	t7_t0_t4_mem1 += ADD_mem[1]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 45
	t5_t0_t2_mem0 += INPUT_mem_r

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 45
	t5_t0_t2_mem1 += INPUT_mem_r

	t5_t10 = S.Task('t5_t10', length=1, delay_cost=1)
	S += t5_t10 >= 45
	t5_t10 += ADD[1]

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	S += t5_t1_t5_mem0 >= 45
	t5_t1_t5_mem0 += MUL_mem[0]

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	S += t5_t1_t5_mem1 >= 45
	t5_t1_t5_mem1 += MUL_mem[0]

	t6_t31 = S.Task('t6_t31', length=1, delay_cost=1)
	S += t6_t31 >= 45
	t6_t31 += ADD[0]

	t7_t0_t4 = S.Task('t7_t0_t4', length=7, delay_cost=1)
	S += t7_t0_t4 >= 45
	t7_t0_t4 += MUL[0]

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	S += t5_t00_mem0 >= 46
	t5_t00_mem0 += MUL_mem[0]

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	S += t5_t00_mem1 >= 46
	t5_t00_mem1 += MUL_mem[0]

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 46
	t5_t0_t2 += ADD[0]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 46
	t5_t0_t3_mem0 += INPUT_mem_r

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 46
	t5_t0_t3_mem1 += INPUT_mem_r

	t5_t1_t5 = S.Task('t5_t1_t5', length=1, delay_cost=1)
	S += t5_t1_t5 >= 46
	t5_t1_t5 += ADD[2]

	t5_t00 = S.Task('t5_t00', length=1, delay_cost=1)
	S += t5_t00 >= 47
	t5_t00 += ADD[0]

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	S += t5_t0_t3 >= 47
	t5_t0_t3 += ADD[3]

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	S += t5_t0_t4_in >= 47
	t5_t0_t4_in += MUL_in[0]

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	S += t5_t0_t4_mem0 >= 47
	t5_t0_t4_mem0 += ADD_mem[0]

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	S += t5_t0_t4_mem1 >= 47
	t5_t0_t4_mem1 += ADD_mem[3]

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	S += t5_t0_t5_mem0 >= 47
	t5_t0_t5_mem0 += MUL_mem[0]

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	S += t5_t0_t5_mem1 >= 47
	t5_t0_t5_mem1 += MUL_mem[0]

	t6_t30_mem0 = S.Task('t6_t30_mem0', length=1, delay_cost=1)
	S += t6_t30_mem0 >= 47
	t6_t30_mem0 += INPUT_mem_r

	t6_t30_mem1 = S.Task('t6_t30_mem1', length=1, delay_cost=1)
	S += t6_t30_mem1 >= 47
	t6_t30_mem1 += INPUT_mem_r

	t5_t0_t4 = S.Task('t5_t0_t4', length=7, delay_cost=1)
	S += t5_t0_t4 >= 48
	t5_t0_t4 += MUL[0]

	t5_t0_t5 = S.Task('t5_t0_t5', length=1, delay_cost=1)
	S += t5_t0_t5 >= 48
	t5_t0_t5 += ADD[2]

	t6_t00_mem0 = S.Task('t6_t00_mem0', length=1, delay_cost=1)
	S += t6_t00_mem0 >= 48
	t6_t00_mem0 += MUL_mem[0]

	t6_t00_mem1 = S.Task('t6_t00_mem1', length=1, delay_cost=1)
	S += t6_t00_mem1 >= 48
	t6_t00_mem1 += MUL_mem[0]

	t6_t21_mem0 = S.Task('t6_t21_mem0', length=1, delay_cost=1)
	S += t6_t21_mem0 >= 48
	t6_t21_mem0 += INPUT_mem_r

	t6_t21_mem1 = S.Task('t6_t21_mem1', length=1, delay_cost=1)
	S += t6_t21_mem1 >= 48
	t6_t21_mem1 += INPUT_mem_r

	t6_t30 = S.Task('t6_t30', length=1, delay_cost=1)
	S += t6_t30 >= 48
	t6_t30 += ADD[1]

	t6_t4_t3_mem0 = S.Task('t6_t4_t3_mem0', length=1, delay_cost=1)
	S += t6_t4_t3_mem0 >= 48
	t6_t4_t3_mem0 += ADD_mem[1]

	t6_t4_t3_mem1 = S.Task('t6_t4_t3_mem1', length=1, delay_cost=1)
	S += t6_t4_t3_mem1 >= 48
	t6_t4_t3_mem1 += ADD_mem[0]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 49
	t5_t1_t3_mem0 += INPUT_mem_r

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 49
	t5_t1_t3_mem1 += INPUT_mem_r

	t6_t00 = S.Task('t6_t00', length=1, delay_cost=1)
	S += t6_t00 >= 49
	t6_t00 += ADD[0]

	t6_t21 = S.Task('t6_t21', length=1, delay_cost=1)
	S += t6_t21 >= 49
	t6_t21 += ADD[3]

	t6_t4_t1_in = S.Task('t6_t4_t1_in', length=1, delay_cost=1)
	S += t6_t4_t1_in >= 49
	t6_t4_t1_in += MUL_in[0]

	t6_t4_t1_mem0 = S.Task('t6_t4_t1_mem0', length=1, delay_cost=1)
	S += t6_t4_t1_mem0 >= 49
	t6_t4_t1_mem0 += ADD_mem[3]

	t6_t4_t1_mem1 = S.Task('t6_t4_t1_mem1', length=1, delay_cost=1)
	S += t6_t4_t1_mem1 >= 49
	t6_t4_t1_mem1 += ADD_mem[0]

	t6_t4_t3 = S.Task('t6_t4_t3', length=1, delay_cost=1)
	S += t6_t4_t3 >= 49
	t6_t4_t3 += ADD[1]

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	S += t5_t1_t3 >= 50
	t5_t1_t3 += ADD[1]

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	S += t5_t1_t4_in >= 50
	t5_t1_t4_in += MUL_in[0]

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	S += t5_t1_t4_mem0 >= 50
	t5_t1_t4_mem0 += ADD_mem[0]

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	S += t5_t1_t4_mem1 >= 50
	t5_t1_t4_mem1 += ADD_mem[1]

	t6_t20_mem0 = S.Task('t6_t20_mem0', length=1, delay_cost=1)
	S += t6_t20_mem0 >= 50
	t6_t20_mem0 += INPUT_mem_r

	t6_t20_mem1 = S.Task('t6_t20_mem1', length=1, delay_cost=1)
	S += t6_t20_mem1 >= 50
	t6_t20_mem1 += INPUT_mem_r

	t6_t4_t1 = S.Task('t6_t4_t1', length=7, delay_cost=1)
	S += t6_t4_t1 >= 50
	t6_t4_t1 += MUL[0]

	t5_t1_t4 = S.Task('t5_t1_t4', length=7, delay_cost=1)
	S += t5_t1_t4 >= 51
	t5_t1_t4 += MUL[0]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	S += t5_t20_mem0 >= 51
	t5_t20_mem0 += INPUT_mem_r

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	S += t5_t20_mem1 >= 51
	t5_t20_mem1 += INPUT_mem_r

	t6_t20 = S.Task('t6_t20', length=1, delay_cost=1)
	S += t6_t20 >= 51
	t6_t20 += ADD[0]

	t6_t4_t0_in = S.Task('t6_t4_t0_in', length=1, delay_cost=1)
	S += t6_t4_t0_in >= 51
	t6_t4_t0_in += MUL_in[0]

	t6_t4_t0_mem0 = S.Task('t6_t4_t0_mem0', length=1, delay_cost=1)
	S += t6_t4_t0_mem0 >= 51
	t6_t4_t0_mem0 += ADD_mem[0]

	t6_t4_t0_mem1 = S.Task('t6_t4_t0_mem1', length=1, delay_cost=1)
	S += t6_t4_t0_mem1 >= 51
	t6_t4_t0_mem1 += ADD_mem[1]

	t6_t4_t2_mem0 = S.Task('t6_t4_t2_mem0', length=1, delay_cost=1)
	S += t6_t4_t2_mem0 >= 51
	t6_t4_t2_mem0 += ADD_mem[0]

	t6_t4_t2_mem1 = S.Task('t6_t4_t2_mem1', length=1, delay_cost=1)
	S += t6_t4_t2_mem1 >= 51
	t6_t4_t2_mem1 += ADD_mem[3]

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	S += t5_t20 >= 52
	t5_t20 += ADD[3]

	t6_t1_t3_mem0 = S.Task('t6_t1_t3_mem0', length=1, delay_cost=1)
	S += t6_t1_t3_mem0 >= 52
	t6_t1_t3_mem0 += INPUT_mem_r

	t6_t1_t3_mem1 = S.Task('t6_t1_t3_mem1', length=1, delay_cost=1)
	S += t6_t1_t3_mem1 >= 52
	t6_t1_t3_mem1 += INPUT_mem_r

	t6_t4_t0 = S.Task('t6_t4_t0', length=7, delay_cost=1)
	S += t6_t4_t0 >= 52
	t6_t4_t0 += MUL[0]

	t6_t4_t2 = S.Task('t6_t4_t2', length=1, delay_cost=1)
	S += t6_t4_t2 >= 52
	t6_t4_t2 += ADD[2]

	t6_t1_t2_mem0 = S.Task('t6_t1_t2_mem0', length=1, delay_cost=1)
	S += t6_t1_t2_mem0 >= 53
	t6_t1_t2_mem0 += INPUT_mem_r

	t6_t1_t2_mem1 = S.Task('t6_t1_t2_mem1', length=1, delay_cost=1)
	S += t6_t1_t2_mem1 >= 53
	t6_t1_t2_mem1 += INPUT_mem_r

	t6_t1_t3 = S.Task('t6_t1_t3', length=1, delay_cost=1)
	S += t6_t1_t3 >= 53
	t6_t1_t3 += ADD[0]

	t6_t0_t3_mem0 = S.Task('t6_t0_t3_mem0', length=1, delay_cost=1)
	S += t6_t0_t3_mem0 >= 54
	t6_t0_t3_mem0 += INPUT_mem_r

	t6_t0_t3_mem1 = S.Task('t6_t0_t3_mem1', length=1, delay_cost=1)
	S += t6_t0_t3_mem1 >= 54
	t6_t0_t3_mem1 += INPUT_mem_r

	t6_t1_t2 = S.Task('t6_t1_t2', length=1, delay_cost=1)
	S += t6_t1_t2 >= 54
	t6_t1_t2 += ADD[0]

	t6_t1_t4_in = S.Task('t6_t1_t4_in', length=1, delay_cost=1)
	S += t6_t1_t4_in >= 54
	t6_t1_t4_in += MUL_in[0]

	t6_t1_t4_mem0 = S.Task('t6_t1_t4_mem0', length=1, delay_cost=1)
	S += t6_t1_t4_mem0 >= 54
	t6_t1_t4_mem0 += ADD_mem[0]

	t6_t1_t4_mem1 = S.Task('t6_t1_t4_mem1', length=1, delay_cost=1)
	S += t6_t1_t4_mem1 >= 54
	t6_t1_t4_mem1 += ADD_mem[0]

	t4_t3_t2_mem0 = S.Task('t4_t3_t2_mem0', length=1, delay_cost=1)
	S += t4_t3_t2_mem0 >= 55
	t4_t3_t2_mem0 += INPUT_mem_r

	t4_t3_t2_mem1 = S.Task('t4_t3_t2_mem1', length=1, delay_cost=1)
	S += t4_t3_t2_mem1 >= 55
	t4_t3_t2_mem1 += INPUT_mem_r

	t6_t0_t3 = S.Task('t6_t0_t3', length=1, delay_cost=1)
	S += t6_t0_t3 >= 55
	t6_t0_t3 += ADD[2]

	t6_t1_t4 = S.Task('t6_t1_t4', length=7, delay_cost=1)
	S += t6_t1_t4 >= 55
	t6_t1_t4 += MUL[0]

	t4_t3_t2 = S.Task('t4_t3_t2', length=1, delay_cost=1)
	S += t4_t3_t2 >= 56
	t4_t3_t2 += ADD[2]

	t4_t3_t4_in = S.Task('t4_t3_t4_in', length=1, delay_cost=1)
	S += t4_t3_t4_in >= 56
	t4_t3_t4_in += MUL_in[0]

	t4_t3_t4_mem0 = S.Task('t4_t3_t4_mem0', length=1, delay_cost=1)
	S += t4_t3_t4_mem0 >= 56
	t4_t3_t4_mem0 += ADD_mem[2]

	t4_t3_t4_mem1 = S.Task('t4_t3_t4_mem1', length=1, delay_cost=1)
	S += t4_t3_t4_mem1 >= 56
	t4_t3_t4_mem1 += ADD_mem[1]

	t6_t0_t2_mem0 = S.Task('t6_t0_t2_mem0', length=1, delay_cost=1)
	S += t6_t0_t2_mem0 >= 56
	t6_t0_t2_mem0 += INPUT_mem_r

	t6_t0_t2_mem1 = S.Task('t6_t0_t2_mem1', length=1, delay_cost=1)
	S += t6_t0_t2_mem1 >= 56
	t6_t0_t2_mem1 += INPUT_mem_r

	t4_t3_t4 = S.Task('t4_t3_t4', length=7, delay_cost=1)
	S += t4_t3_t4 >= 57
	t4_t3_t4 += MUL[0]

	t5_t31_mem0 = S.Task('t5_t31_mem0', length=1, delay_cost=1)
	S += t5_t31_mem0 >= 57
	t5_t31_mem0 += INPUT_mem_r

	t5_t31_mem1 = S.Task('t5_t31_mem1', length=1, delay_cost=1)
	S += t5_t31_mem1 >= 57
	t5_t31_mem1 += INPUT_mem_r

	t6_t0_t2 = S.Task('t6_t0_t2', length=1, delay_cost=1)
	S += t6_t0_t2 >= 57
	t6_t0_t2 += ADD[0]

	t6_t0_t4_in = S.Task('t6_t0_t4_in', length=1, delay_cost=1)
	S += t6_t0_t4_in >= 57
	t6_t0_t4_in += MUL_in[0]

	t6_t0_t4_mem0 = S.Task('t6_t0_t4_mem0', length=1, delay_cost=1)
	S += t6_t0_t4_mem0 >= 57
	t6_t0_t4_mem0 += ADD_mem[0]

	t6_t0_t4_mem1 = S.Task('t6_t0_t4_mem1', length=1, delay_cost=1)
	S += t6_t0_t4_mem1 >= 57
	t6_t0_t4_mem1 += ADD_mem[2]

	t5_t30_mem0 = S.Task('t5_t30_mem0', length=1, delay_cost=1)
	S += t5_t30_mem0 >= 58
	t5_t30_mem0 += INPUT_mem_r

	t5_t30_mem1 = S.Task('t5_t30_mem1', length=1, delay_cost=1)
	S += t5_t30_mem1 >= 58
	t5_t30_mem1 += INPUT_mem_r

	t5_t31 = S.Task('t5_t31', length=1, delay_cost=1)
	S += t5_t31 >= 58
	t5_t31 += ADD[0]

	t6_t0_t4 = S.Task('t6_t0_t4', length=7, delay_cost=1)
	S += t6_t0_t4 >= 58
	t6_t0_t4 += MUL[0]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	S += t5_t21_mem0 >= 59
	t5_t21_mem0 += INPUT_mem_r

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	S += t5_t21_mem1 >= 59
	t5_t21_mem1 += INPUT_mem_r

	t5_t30 = S.Task('t5_t30', length=1, delay_cost=1)
	S += t5_t30 >= 59
	t5_t30 += ADD[0]

	t5_t4_t0_in = S.Task('t5_t4_t0_in', length=1, delay_cost=1)
	S += t5_t4_t0_in >= 59
	t5_t4_t0_in += MUL_in[0]

	t5_t4_t0_mem0 = S.Task('t5_t4_t0_mem0', length=1, delay_cost=1)
	S += t5_t4_t0_mem0 >= 59
	t5_t4_t0_mem0 += ADD_mem[3]

	t5_t4_t0_mem1 = S.Task('t5_t4_t0_mem1', length=1, delay_cost=1)
	S += t5_t4_t0_mem1 >= 59
	t5_t4_t0_mem1 += ADD_mem[0]

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	S += t5_t21 >= 60
	t5_t21 += ADD[0]

	t5_t4_t0 = S.Task('t5_t4_t0', length=7, delay_cost=1)
	S += t5_t4_t0 >= 60
	t5_t4_t0 += MUL[0]

	t5_t4_t2_mem0 = S.Task('t5_t4_t2_mem0', length=1, delay_cost=1)
	S += t5_t4_t2_mem0 >= 60
	t5_t4_t2_mem0 += ADD_mem[3]

	t5_t4_t2_mem1 = S.Task('t5_t4_t2_mem1', length=1, delay_cost=1)
	S += t5_t4_t2_mem1 >= 60
	t5_t4_t2_mem1 += ADD_mem[0]

	t7_t1_t0_in = S.Task('t7_t1_t0_in', length=1, delay_cost=1)
	S += t7_t1_t0_in >= 60
	t7_t1_t0_in += MUL_in[0]

	t7_t1_t0_mem0 = S.Task('t7_t1_t0_mem0', length=1, delay_cost=1)
	S += t7_t1_t0_mem0 >= 60
	t7_t1_t0_mem0 += INPUT_mem_r

	t7_t1_t0_mem1 = S.Task('t7_t1_t0_mem1', length=1, delay_cost=1)
	S += t7_t1_t0_mem1 >= 60
	t7_t1_t0_mem1 += INPUT_mem_r

	t5_t4_t2 = S.Task('t5_t4_t2', length=1, delay_cost=1)
	S += t5_t4_t2 >= 61
	t5_t4_t2 += ADD[0]

	t5_t4_t3_mem0 = S.Task('t5_t4_t3_mem0', length=1, delay_cost=1)
	S += t5_t4_t3_mem0 >= 61
	t5_t4_t3_mem0 += ADD_mem[0]

	t5_t4_t3_mem1 = S.Task('t5_t4_t3_mem1', length=1, delay_cost=1)
	S += t5_t4_t3_mem1 >= 61
	t5_t4_t3_mem1 += ADD_mem[0]

	t7_t1_t0 = S.Task('t7_t1_t0', length=7, delay_cost=1)
	S += t7_t1_t0 >= 61
	t7_t1_t0 += MUL[0]

	t7_t1_t1_in = S.Task('t7_t1_t1_in', length=1, delay_cost=1)
	S += t7_t1_t1_in >= 61
	t7_t1_t1_in += MUL_in[0]

	t7_t1_t1_mem0 = S.Task('t7_t1_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_t1_mem0 >= 61
	t7_t1_t1_mem0 += INPUT_mem_r

	t7_t1_t1_mem1 = S.Task('t7_t1_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_t1_mem1 >= 61
	t7_t1_t1_mem1 += INPUT_mem_r

	t5_t4_t1_in = S.Task('t5_t4_t1_in', length=1, delay_cost=1)
	S += t5_t4_t1_in >= 62
	t5_t4_t1_in += MUL_in[0]

	t5_t4_t1_mem0 = S.Task('t5_t4_t1_mem0', length=1, delay_cost=1)
	S += t5_t4_t1_mem0 >= 62
	t5_t4_t1_mem0 += ADD_mem[0]

	t5_t4_t1_mem1 = S.Task('t5_t4_t1_mem1', length=1, delay_cost=1)
	S += t5_t4_t1_mem1 >= 62
	t5_t4_t1_mem1 += ADD_mem[0]

	t5_t4_t3 = S.Task('t5_t4_t3', length=1, delay_cost=1)
	S += t5_t4_t3 >= 62
	t5_t4_t3 += ADD[0]

	t7_t1_t1 = S.Task('t7_t1_t1', length=7, delay_cost=1)
	S += t7_t1_t1 >= 62
	t7_t1_t1 += MUL[0]

	t7_t20_mem0 = S.Task('t7_t20_mem0', length=1, delay_cost=1)
	S += t7_t20_mem0 >= 62
	t7_t20_mem0 += INPUT_mem_r

	t7_t20_mem1 = S.Task('t7_t20_mem1', length=1, delay_cost=1)
	S += t7_t20_mem1 >= 62
	t7_t20_mem1 += INPUT_mem_r

	t5_t4_t1 = S.Task('t5_t4_t1', length=7, delay_cost=1)
	S += t5_t4_t1 >= 63
	t5_t4_t1 += MUL[0]

	t7_t20 = S.Task('t7_t20', length=1, delay_cost=1)
	S += t7_t20 >= 63
	t7_t20 += ADD[0]

	t7_t21_mem0 = S.Task('t7_t21_mem0', length=1, delay_cost=1)
	S += t7_t21_mem0 >= 63
	t7_t21_mem0 += INPUT_mem_r

	t7_t21_mem1 = S.Task('t7_t21_mem1', length=1, delay_cost=1)
	S += t7_t21_mem1 >= 63
	t7_t21_mem1 += INPUT_mem_r

	t7_t21 = S.Task('t7_t21', length=1, delay_cost=1)
	S += t7_t21 >= 64
	t7_t21 += ADD[0]

	t7_t31_mem0 = S.Task('t7_t31_mem0', length=1, delay_cost=1)
	S += t7_t31_mem0 >= 64
	t7_t31_mem0 += INPUT_mem_r

	t7_t31_mem1 = S.Task('t7_t31_mem1', length=1, delay_cost=1)
	S += t7_t31_mem1 >= 64
	t7_t31_mem1 += INPUT_mem_r

	t7_t4_t2_mem0 = S.Task('t7_t4_t2_mem0', length=1, delay_cost=1)
	S += t7_t4_t2_mem0 >= 64
	t7_t4_t2_mem0 += ADD_mem[0]

	t7_t4_t2_mem1 = S.Task('t7_t4_t2_mem1', length=1, delay_cost=1)
	S += t7_t4_t2_mem1 >= 64
	t7_t4_t2_mem1 += ADD_mem[0]

	t7_t30_mem0 = S.Task('t7_t30_mem0', length=1, delay_cost=1)
	S += t7_t30_mem0 >= 65
	t7_t30_mem0 += INPUT_mem_r

	t7_t30_mem1 = S.Task('t7_t30_mem1', length=1, delay_cost=1)
	S += t7_t30_mem1 >= 65
	t7_t30_mem1 += INPUT_mem_r

	t7_t31 = S.Task('t7_t31', length=1, delay_cost=1)
	S += t7_t31 >= 65
	t7_t31 += ADD[0]

	t7_t4_t1_in = S.Task('t7_t4_t1_in', length=1, delay_cost=1)
	S += t7_t4_t1_in >= 65
	t7_t4_t1_in += MUL_in[0]

	t7_t4_t1_mem0 = S.Task('t7_t4_t1_mem0', length=1, delay_cost=1)
	S += t7_t4_t1_mem0 >= 65
	t7_t4_t1_mem0 += ADD_mem[0]

	t7_t4_t1_mem1 = S.Task('t7_t4_t1_mem1', length=1, delay_cost=1)
	S += t7_t4_t1_mem1 >= 65
	t7_t4_t1_mem1 += ADD_mem[0]

	t7_t4_t2 = S.Task('t7_t4_t2', length=1, delay_cost=1)
	S += t7_t4_t2 >= 65
	t7_t4_t2 += ADD[1]

	t7_t1_t2_mem0 = S.Task('t7_t1_t2_mem0', length=1, delay_cost=1)
	S += t7_t1_t2_mem0 >= 66
	t7_t1_t2_mem0 += INPUT_mem_r

	t7_t1_t2_mem1 = S.Task('t7_t1_t2_mem1', length=1, delay_cost=1)
	S += t7_t1_t2_mem1 >= 66
	t7_t1_t2_mem1 += INPUT_mem_r

	t7_t30 = S.Task('t7_t30', length=1, delay_cost=1)
	S += t7_t30 >= 66
	t7_t30 += ADD[2]

	t7_t4_t0_in = S.Task('t7_t4_t0_in', length=1, delay_cost=1)
	S += t7_t4_t0_in >= 66
	t7_t4_t0_in += MUL_in[0]

	t7_t4_t0_mem0 = S.Task('t7_t4_t0_mem0', length=1, delay_cost=1)
	S += t7_t4_t0_mem0 >= 66
	t7_t4_t0_mem0 += ADD_mem[0]

	t7_t4_t0_mem1 = S.Task('t7_t4_t0_mem1', length=1, delay_cost=1)
	S += t7_t4_t0_mem1 >= 66
	t7_t4_t0_mem1 += ADD_mem[2]

	t7_t4_t1 = S.Task('t7_t4_t1', length=7, delay_cost=1)
	S += t7_t4_t1 >= 66
	t7_t4_t1 += MUL[0]

	t7_t4_t3_mem0 = S.Task('t7_t4_t3_mem0', length=1, delay_cost=1)
	S += t7_t4_t3_mem0 >= 66
	t7_t4_t3_mem0 += ADD_mem[2]

	t7_t4_t3_mem1 = S.Task('t7_t4_t3_mem1', length=1, delay_cost=1)
	S += t7_t4_t3_mem1 >= 66
	t7_t4_t3_mem1 += ADD_mem[0]

	t7_t1_t2 = S.Task('t7_t1_t2', length=1, delay_cost=1)
	S += t7_t1_t2 >= 67
	t7_t1_t2 += ADD[2]

	t7_t1_t3_mem0 = S.Task('t7_t1_t3_mem0', length=1, delay_cost=1)
	S += t7_t1_t3_mem0 >= 67
	t7_t1_t3_mem0 += INPUT_mem_r

	t7_t1_t3_mem1 = S.Task('t7_t1_t3_mem1', length=1, delay_cost=1)
	S += t7_t1_t3_mem1 >= 67
	t7_t1_t3_mem1 += INPUT_mem_r

	t7_t4_t0 = S.Task('t7_t4_t0', length=7, delay_cost=1)
	S += t7_t4_t0 >= 67
	t7_t4_t0 += MUL[0]

	t7_t4_t3 = S.Task('t7_t4_t3', length=1, delay_cost=1)
	S += t7_t4_t3 >= 67
	t7_t4_t3 += ADD[0]

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	S += t200_mem0 >= 68
	t200_mem0 += ADD_mem[2]

	t200_mem1 = S.Task('t200_mem1', length=1, delay_cost=1)
	S += t200_mem1 >= 68
	t200_mem1 += INPUT_mem_r

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 68
	t4_t00_mem0 += INPUT_mem_r

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 68
	t4_t00_mem1 += ADD_mem[3]

	t7_t10_mem0 = S.Task('t7_t10_mem0', length=1, delay_cost=1)
	S += t7_t10_mem0 >= 68
	t7_t10_mem0 += MUL_mem[0]

	t7_t10_mem1 = S.Task('t7_t10_mem1', length=1, delay_cost=1)
	S += t7_t10_mem1 >= 68
	t7_t10_mem1 += MUL_mem[0]

	t7_t1_t3 = S.Task('t7_t1_t3', length=1, delay_cost=1)
	S += t7_t1_t3 >= 68
	t7_t1_t3 += ADD[3]

	t7_t1_t4_in = S.Task('t7_t1_t4_in', length=1, delay_cost=1)
	S += t7_t1_t4_in >= 68
	t7_t1_t4_in += MUL_in[0]

	t7_t1_t4_mem0 = S.Task('t7_t1_t4_mem0', length=1, delay_cost=1)
	S += t7_t1_t4_mem0 >= 68
	t7_t1_t4_mem0 += ADD_mem[2]

	t7_t1_t4_mem1 = S.Task('t7_t1_t4_mem1', length=1, delay_cost=1)
	S += t7_t1_t4_mem1 >= 68
	t7_t1_t4_mem1 += ADD_mem[3]

	t0_t01_mem0 = S.Task('t0_t01_mem0', length=1, delay_cost=1)
	S += t0_t01_mem0 >= 69
	t0_t01_mem0 += INPUT_mem_r

	t0_t01_mem1 = S.Task('t0_t01_mem1', length=1, delay_cost=1)
	S += t0_t01_mem1 >= 69
	t0_t01_mem1 += ADD_mem[3]

	t200 = S.Task('t200', length=1, delay_cost=1)
	S += t200 >= 69
	t200 += ADD[1]

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	S += t211_mem0 >= 69
	t211_mem0 += ADD_mem[3]

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	S += t211_mem1 >= 69
	t211_mem1 += INPUT_mem_r

	t4_t00 = S.Task('t4_t00', length=1, delay_cost=1)
	S += t4_t00 >= 69
	t4_t00 += ADD[3]

	t7_t10 = S.Task('t7_t10', length=1, delay_cost=1)
	S += t7_t10 >= 69
	t7_t10 += ADD[0]

	t7_t1_t4 = S.Task('t7_t1_t4', length=7, delay_cost=1)
	S += t7_t1_t4 >= 69
	t7_t1_t4 += MUL[0]

	t7_t1_t5_mem0 = S.Task('t7_t1_t5_mem0', length=1, delay_cost=1)
	S += t7_t1_t5_mem0 >= 69
	t7_t1_t5_mem0 += MUL_mem[0]

	t7_t1_t5_mem1 = S.Task('t7_t1_t5_mem1', length=1, delay_cost=1)
	S += t7_t1_t5_mem1 >= 69
	t7_t1_t5_mem1 += MUL_mem[0]

	t0_t00_mem0 = S.Task('t0_t00_mem0', length=1, delay_cost=1)
	S += t0_t00_mem0 >= 70
	t0_t00_mem0 += INPUT_mem_r

	t0_t00_mem1 = S.Task('t0_t00_mem1', length=1, delay_cost=1)
	S += t0_t00_mem1 >= 70
	t0_t00_mem1 += ADD_mem[1]

	t0_t01 = S.Task('t0_t01', length=1, delay_cost=1)
	S += t0_t01 >= 70
	t0_t01 += ADD[3]

	t211 = S.Task('t211', length=1, delay_cost=1)
	S += t211 >= 70
	t211 += ADD[2]

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	S += t4_t01_mem0 >= 70
	t4_t01_mem0 += INPUT_mem_r

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	S += t4_t01_mem1 >= 70
	t4_t01_mem1 += ADD_mem[0]

	t7_t1_t5 = S.Task('t7_t1_t5', length=1, delay_cost=1)
	S += t7_t1_t5 >= 70
	t7_t1_t5 += ADD[1]

	t0_t00 = S.Task('t0_t00', length=1, delay_cost=1)
	S += t0_t00 >= 71
	t0_t00 += ADD[2]

	t4_t01 = S.Task('t4_t01', length=1, delay_cost=1)
	S += t4_t01 >= 71
	t4_t01 += ADD[1]

	t800_mem0 = S.Task('t800_mem0', length=1, delay_cost=1)
	S += t800_mem0 >= 71
	t800_mem0 += ADD_mem[2]

	t800_mem1 = S.Task('t800_mem1', length=1, delay_cost=1)
	S += t800_mem1 >= 71
	t800_mem1 += INPUT_mem_r

	t801_mem0 = S.Task('t801_mem0', length=1, delay_cost=1)
	S += t801_mem0 >= 71
	t801_mem0 += ADD_mem[3]

	t801_mem1 = S.Task('t801_mem1', length=1, delay_cost=1)
	S += t801_mem1 >= 71
	t801_mem1 += INPUT_mem_r

	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	S += t210_mem0 >= 72
	t210_mem0 += ADD_mem[2]

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	S += t210_mem1 >= 72
	t210_mem1 += INPUT_mem_r

	t800 = S.Task('t800', length=1, delay_cost=1)
	S += t800 >= 72
	t800 += ADD[0]

	t801 = S.Task('t801', length=1, delay_cost=1)
	S += t801 >= 72
	t801 += ADD[2]

	t810_mem0 = S.Task('t810_mem0', length=1, delay_cost=1)
	S += t810_mem0 >= 72
	t810_mem0 += ADD_mem[2]

	t810_mem1 = S.Task('t810_mem1', length=1, delay_cost=1)
	S += t810_mem1 >= 72
	t810_mem1 += INPUT_mem_r

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	S += t201_mem0 >= 73
	t201_mem0 += ADD_mem[3]

	t201_mem1 = S.Task('t201_mem1', length=1, delay_cost=1)
	S += t201_mem1 >= 73
	t201_mem1 += INPUT_mem_r

	t210 = S.Task('t210', length=1, delay_cost=1)
	S += t210 >= 73
	t210 += ADD[2]

	t810 = S.Task('t810', length=1, delay_cost=1)
	S += t810 >= 73
	t810 += ADD[0]

	t811_mem0 = S.Task('t811_mem0', length=1, delay_cost=1)
	S += t811_mem0 >= 73
	t811_mem0 += ADD_mem[3]

	t811_mem1 = S.Task('t811_mem1', length=1, delay_cost=1)
	S += t811_mem1 >= 73
	t811_mem1 += INPUT_mem_r

	t201 = S.Task('t201', length=1, delay_cost=1)
	S += t201 >= 74
	t201 += ADD[2]

	t811 = S.Task('t811', length=1, delay_cost=1)
	S += t811 >= 74
	t811 += ADD[3]


	# new tasks
	t0_t2_t0_in = S.Task('t0_t2_t0_in', length=1, delay_cost=1)
	t0_t2_t0_in += alt(MUL_in)
	t0_t2_t0 = S.Task('t0_t2_t0', length=7, delay_cost=1)
	t0_t2_t0 += alt(MUL)
	S += t0_t2_t0>=t0_t2_t0_in

	t0_t2_t0_mem0 = S.Task('t0_t2_t0_mem0', length=1, delay_cost=1)
	t0_t2_t0_mem0 += ADD_mem[2]
	S += 71 < t0_t2_t0_mem0
	S += t0_t2_t0_mem0 <= t0_t2_t0

	t0_t2_t0_mem1 = S.Task('t0_t2_t0_mem1', length=1, delay_cost=1)
	t0_t2_t0_mem1 += ADD_mem[3]
	S += 12 < t0_t2_t0_mem1
	S += t0_t2_t0_mem1 <= t0_t2_t0

	t0_t2_t1_in = S.Task('t0_t2_t1_in', length=1, delay_cost=1)
	t0_t2_t1_in += alt(MUL_in)
	t0_t2_t1 = S.Task('t0_t2_t1', length=7, delay_cost=1)
	t0_t2_t1 += alt(MUL)
	S += t0_t2_t1>=t0_t2_t1_in

	t0_t2_t1_mem0 = S.Task('t0_t2_t1_mem0', length=1, delay_cost=1)
	t0_t2_t1_mem0 += ADD_mem[3]
	S += 70 < t0_t2_t1_mem0
	S += t0_t2_t1_mem0 <= t0_t2_t1

	t0_t2_t1_mem1 = S.Task('t0_t2_t1_mem1', length=1, delay_cost=1)
	t0_t2_t1_mem1 += ADD_mem[2]
	S += 10 < t0_t2_t1_mem1
	S += t0_t2_t1_mem1 <= t0_t2_t1

	t0_t2_t2 = S.Task('t0_t2_t2', length=1, delay_cost=1)
	t0_t2_t2 += alt(ADD)

	t0_t2_t2_mem0 = S.Task('t0_t2_t2_mem0', length=1, delay_cost=1)
	t0_t2_t2_mem0 += ADD_mem[2]
	S += 71 < t0_t2_t2_mem0
	S += t0_t2_t2_mem0 <= t0_t2_t2

	t0_t2_t2_mem1 = S.Task('t0_t2_t2_mem1', length=1, delay_cost=1)
	t0_t2_t2_mem1 += ADD_mem[3]
	S += 70 < t0_t2_t2_mem1
	S += t0_t2_t2_mem1 <= t0_t2_t2

	t0_t31 = S.Task('t0_t31', length=1, delay_cost=1)
	t0_t31 += alt(ADD)

	t0_t31_mem0 = S.Task('t0_t31_mem0', length=1, delay_cost=1)
	t0_t31_mem0 += MUL_mem[0]
	S += 30 < t0_t31_mem0
	S += t0_t31_mem0 <= t0_t31

	t0_t31_mem1 = S.Task('t0_t31_mem1', length=1, delay_cost=1)
	t0_t31_mem1 += ADD_mem[1]
	S += 16 < t0_t31_mem1
	S += t0_t31_mem1 <= t0_t31

	t010 = S.Task('t010', length=1, delay_cost=1)
	t010 += alt(ADD)

	t010_mem0 = S.Task('t010_mem0', length=1, delay_cost=1)
	t010_mem0 += ADD_mem[0]
	S += 15 < t010_mem0
	S += t010_mem0 <= t010

	t010_mem1 = S.Task('t010_mem1', length=1, delay_cost=1)
	t010_mem1 += ADD_mem[0]
	S += 15 < t010_mem1
	S += t010_mem1 <= t010

	t9_a1_0 = S.Task('t9_a1_0', length=1, delay_cost=1)
	t9_a1_0 += alt(ADD)

	t9_a1_0_mem0 = S.Task('t9_a1_0_mem0', length=1, delay_cost=1)
	t9_a1_0_mem0 += ADD_mem[0]
	S += 73 < t9_a1_0_mem0
	S += t9_a1_0_mem0 <= t9_a1_0

	t9_a1_0_mem1 = S.Task('t9_a1_0_mem1', length=1, delay_cost=1)
	t9_a1_0_mem1 += ADD_mem[3]
	S += 74 < t9_a1_0_mem1
	S += t9_a1_0_mem1 <= t9_a1_0

	t9_a1_1 = S.Task('t9_a1_1', length=1, delay_cost=1)
	t9_a1_1 += alt(ADD)

	t9_a1_1_mem0 = S.Task('t9_a1_1_mem0', length=1, delay_cost=1)
	t9_a1_1_mem0 += ADD_mem[3]
	S += 74 < t9_a1_1_mem0
	S += t9_a1_1_mem0 <= t9_a1_1

	t9_a1_1_mem1 = S.Task('t9_a1_1_mem1', length=1, delay_cost=1)
	t9_a1_1_mem1 += ADD_mem[0]
	S += 73 < t9_a1_1_mem1
	S += t9_a1_1_mem1 <= t9_a1_1

	t9_t10 = S.Task('t9_t10', length=1, delay_cost=1)
	t9_t10 += alt(ADD)

	t9_t10_mem0 = S.Task('t9_t10_mem0', length=1, delay_cost=1)
	t9_t10_mem0 += ADD_mem[0]
	S += 72 < t9_t10_mem0
	S += t9_t10_mem0 <= t9_t10

	t9_t10_mem1 = S.Task('t9_t10_mem1', length=1, delay_cost=1)
	t9_t10_mem1 += ADD_mem[0]
	S += 73 < t9_t10_mem1
	S += t9_t10_mem1 <= t9_t10

	t9_t11 = S.Task('t9_t11', length=1, delay_cost=1)
	t9_t11 += alt(ADD)

	t9_t11_mem0 = S.Task('t9_t11_mem0', length=1, delay_cost=1)
	t9_t11_mem0 += ADD_mem[2]
	S += 72 < t9_t11_mem0
	S += t9_t11_mem0 <= t9_t11

	t9_t11_mem1 = S.Task('t9_t11_mem1', length=1, delay_cost=1)
	t9_t11_mem1 += ADD_mem[3]
	S += 74 < t9_t11_mem1
	S += t9_t11_mem1 <= t9_t11

	t9_t3_t0_in = S.Task('t9_t3_t0_in', length=1, delay_cost=1)
	t9_t3_t0_in += alt(MUL_in)
	t9_t3_t0 = S.Task('t9_t3_t0', length=7, delay_cost=1)
	t9_t3_t0 += alt(MUL)
	S += t9_t3_t0>=t9_t3_t0_in

	t9_t3_t0_mem0 = S.Task('t9_t3_t0_mem0', length=1, delay_cost=1)
	t9_t3_t0_mem0 += ADD_mem[0]
	S += 72 < t9_t3_t0_mem0
	S += t9_t3_t0_mem0 <= t9_t3_t0

	t9_t3_t0_mem1 = S.Task('t9_t3_t0_mem1', length=1, delay_cost=1)
	t9_t3_t0_mem1 += ADD_mem[0]
	S += 73 < t9_t3_t0_mem1
	S += t9_t3_t0_mem1 <= t9_t3_t0

	t9_t3_t1_in = S.Task('t9_t3_t1_in', length=1, delay_cost=1)
	t9_t3_t1_in += alt(MUL_in)
	t9_t3_t1 = S.Task('t9_t3_t1', length=7, delay_cost=1)
	t9_t3_t1 += alt(MUL)
	S += t9_t3_t1>=t9_t3_t1_in

	t9_t3_t1_mem0 = S.Task('t9_t3_t1_mem0', length=1, delay_cost=1)
	t9_t3_t1_mem0 += ADD_mem[2]
	S += 72 < t9_t3_t1_mem0
	S += t9_t3_t1_mem0 <= t9_t3_t1

	t9_t3_t1_mem1 = S.Task('t9_t3_t1_mem1', length=1, delay_cost=1)
	t9_t3_t1_mem1 += ADD_mem[3]
	S += 74 < t9_t3_t1_mem1
	S += t9_t3_t1_mem1 <= t9_t3_t1

	t9_t3_t2 = S.Task('t9_t3_t2', length=1, delay_cost=1)
	t9_t3_t2 += alt(ADD)

	t9_t3_t2_mem0 = S.Task('t9_t3_t2_mem0', length=1, delay_cost=1)
	t9_t3_t2_mem0 += ADD_mem[0]
	S += 72 < t9_t3_t2_mem0
	S += t9_t3_t2_mem0 <= t9_t3_t2

	t9_t3_t2_mem1 = S.Task('t9_t3_t2_mem1', length=1, delay_cost=1)
	t9_t3_t2_mem1 += ADD_mem[2]
	S += 72 < t9_t3_t2_mem1
	S += t9_t3_t2_mem1 <= t9_t3_t2

	t9_t3_t3 = S.Task('t9_t3_t3', length=1, delay_cost=1)
	t9_t3_t3 += alt(ADD)

	t9_t3_t3_mem0 = S.Task('t9_t3_t3_mem0', length=1, delay_cost=1)
	t9_t3_t3_mem0 += ADD_mem[0]
	S += 73 < t9_t3_t3_mem0
	S += t9_t3_t3_mem0 <= t9_t3_t3

	t9_t3_t3_mem1 = S.Task('t9_t3_t3_mem1', length=1, delay_cost=1)
	t9_t3_t3_mem1 += ADD_mem[3]
	S += 74 < t9_t3_t3_mem1
	S += t9_t3_t3_mem1 <= t9_t3_t3

	t10_a1_0 = S.Task('t10_a1_0', length=1, delay_cost=1)
	t10_a1_0 += alt(ADD)

	t10_a1_0_mem0 = S.Task('t10_a1_0_mem0', length=1, delay_cost=1)
	t10_a1_0_mem0 += ADD_mem[2]
	S += 73 < t10_a1_0_mem0
	S += t10_a1_0_mem0 <= t10_a1_0

	t10_a1_0_mem1 = S.Task('t10_a1_0_mem1', length=1, delay_cost=1)
	t10_a1_0_mem1 += ADD_mem[2]
	S += 70 < t10_a1_0_mem1
	S += t10_a1_0_mem1 <= t10_a1_0

	t10_a1_1 = S.Task('t10_a1_1', length=1, delay_cost=1)
	t10_a1_1 += alt(ADD)

	t10_a1_1_mem0 = S.Task('t10_a1_1_mem0', length=1, delay_cost=1)
	t10_a1_1_mem0 += ADD_mem[2]
	S += 70 < t10_a1_1_mem0
	S += t10_a1_1_mem0 <= t10_a1_1

	t10_a1_1_mem1 = S.Task('t10_a1_1_mem1', length=1, delay_cost=1)
	t10_a1_1_mem1 += ADD_mem[2]
	S += 73 < t10_a1_1_mem1
	S += t10_a1_1_mem1 <= t10_a1_1

	t10_t10 = S.Task('t10_t10', length=1, delay_cost=1)
	t10_t10 += alt(ADD)

	t10_t10_mem0 = S.Task('t10_t10_mem0', length=1, delay_cost=1)
	t10_t10_mem0 += ADD_mem[1]
	S += 69 < t10_t10_mem0
	S += t10_t10_mem0 <= t10_t10

	t10_t10_mem1 = S.Task('t10_t10_mem1', length=1, delay_cost=1)
	t10_t10_mem1 += ADD_mem[2]
	S += 73 < t10_t10_mem1
	S += t10_t10_mem1 <= t10_t10

	t10_t11 = S.Task('t10_t11', length=1, delay_cost=1)
	t10_t11 += alt(ADD)

	t10_t11_mem0 = S.Task('t10_t11_mem0', length=1, delay_cost=1)
	t10_t11_mem0 += ADD_mem[2]
	S += 74 < t10_t11_mem0
	S += t10_t11_mem0 <= t10_t11

	t10_t11_mem1 = S.Task('t10_t11_mem1', length=1, delay_cost=1)
	t10_t11_mem1 += ADD_mem[2]
	S += 70 < t10_t11_mem1
	S += t10_t11_mem1 <= t10_t11

	t10_t3_t0_in = S.Task('t10_t3_t0_in', length=1, delay_cost=1)
	t10_t3_t0_in += alt(MUL_in)
	t10_t3_t0 = S.Task('t10_t3_t0', length=7, delay_cost=1)
	t10_t3_t0 += alt(MUL)
	S += t10_t3_t0>=t10_t3_t0_in

	t10_t3_t0_mem0 = S.Task('t10_t3_t0_mem0', length=1, delay_cost=1)
	t10_t3_t0_mem0 += ADD_mem[1]
	S += 69 < t10_t3_t0_mem0
	S += t10_t3_t0_mem0 <= t10_t3_t0

	t10_t3_t0_mem1 = S.Task('t10_t3_t0_mem1', length=1, delay_cost=1)
	t10_t3_t0_mem1 += ADD_mem[2]
	S += 73 < t10_t3_t0_mem1
	S += t10_t3_t0_mem1 <= t10_t3_t0

	t10_t3_t1_in = S.Task('t10_t3_t1_in', length=1, delay_cost=1)
	t10_t3_t1_in += alt(MUL_in)
	t10_t3_t1 = S.Task('t10_t3_t1', length=7, delay_cost=1)
	t10_t3_t1 += alt(MUL)
	S += t10_t3_t1>=t10_t3_t1_in

	t10_t3_t1_mem0 = S.Task('t10_t3_t1_mem0', length=1, delay_cost=1)
	t10_t3_t1_mem0 += ADD_mem[2]
	S += 74 < t10_t3_t1_mem0
	S += t10_t3_t1_mem0 <= t10_t3_t1

	t10_t3_t1_mem1 = S.Task('t10_t3_t1_mem1', length=1, delay_cost=1)
	t10_t3_t1_mem1 += ADD_mem[2]
	S += 70 < t10_t3_t1_mem1
	S += t10_t3_t1_mem1 <= t10_t3_t1

	t10_t3_t2 = S.Task('t10_t3_t2', length=1, delay_cost=1)
	t10_t3_t2 += alt(ADD)

	t10_t3_t2_mem0 = S.Task('t10_t3_t2_mem0', length=1, delay_cost=1)
	t10_t3_t2_mem0 += ADD_mem[1]
	S += 69 < t10_t3_t2_mem0
	S += t10_t3_t2_mem0 <= t10_t3_t2

	t10_t3_t2_mem1 = S.Task('t10_t3_t2_mem1', length=1, delay_cost=1)
	t10_t3_t2_mem1 += ADD_mem[2]
	S += 74 < t10_t3_t2_mem1
	S += t10_t3_t2_mem1 <= t10_t3_t2

	t10_t3_t3 = S.Task('t10_t3_t3', length=1, delay_cost=1)
	t10_t3_t3 += alt(ADD)

	t10_t3_t3_mem0 = S.Task('t10_t3_t3_mem0', length=1, delay_cost=1)
	t10_t3_t3_mem0 += ADD_mem[2]
	S += 73 < t10_t3_t3_mem0
	S += t10_t3_t3_mem0 <= t10_t3_t3

	t10_t3_t3_mem1 = S.Task('t10_t3_t3_mem1', length=1, delay_cost=1)
	t10_t3_t3_mem1 += ADD_mem[2]
	S += 70 < t10_t3_t3_mem1
	S += t10_t3_t3_mem1 <= t10_t3_t3

	t3_t01 = S.Task('t3_t01', length=1, delay_cost=1)
	t3_t01 += alt(ADD)

	t3_t01_mem0 = S.Task('t3_t01_mem0', length=1, delay_cost=1)
	t3_t01_mem0 += MUL_mem[0]
	S += 35 < t3_t01_mem0
	S += t3_t01_mem0 <= t3_t01

	t3_t01_mem1 = S.Task('t3_t01_mem1', length=1, delay_cost=1)
	t3_t01_mem1 += ADD_mem[1]
	S += 14 < t3_t01_mem1
	S += t3_t01_mem1 <= t3_t01

	t3_t11 = S.Task('t3_t11', length=1, delay_cost=1)
	t3_t11 += alt(ADD)

	t3_t11_mem0 = S.Task('t3_t11_mem0', length=1, delay_cost=1)
	t3_t11_mem0 += MUL_mem[0]
	S += 32 < t3_t11_mem0
	S += t3_t11_mem0 <= t3_t11

	t3_t11_mem1 = S.Task('t3_t11_mem1', length=1, delay_cost=1)
	t3_t11_mem1 += ADD_mem[0]
	S += 12 < t3_t11_mem1
	S += t3_t11_mem1 <= t3_t11

	t3_t4_t4_in = S.Task('t3_t4_t4_in', length=1, delay_cost=1)
	t3_t4_t4_in += alt(MUL_in)
	t3_t4_t4 = S.Task('t3_t4_t4', length=7, delay_cost=1)
	t3_t4_t4 += alt(MUL)
	S += t3_t4_t4>=t3_t4_t4_in

	t3_t4_t4_mem0 = S.Task('t3_t4_t4_mem0', length=1, delay_cost=1)
	t3_t4_t4_mem0 += ADD_mem[0]
	S += 20 < t3_t4_t4_mem0
	S += t3_t4_t4_mem0 <= t3_t4_t4

	t3_t4_t4_mem1 = S.Task('t3_t4_t4_mem1', length=1, delay_cost=1)
	t3_t4_t4_mem1 += ADD_mem[1]
	S += 22 < t3_t4_t4_mem1
	S += t3_t4_t4_mem1 <= t3_t4_t4

	t3_t40 = S.Task('t3_t40', length=1, delay_cost=1)
	t3_t40 += alt(ADD)

	t3_t40_mem0 = S.Task('t3_t40_mem0', length=1, delay_cost=1)
	t3_t40_mem0 += MUL_mem[0]
	S += 23 < t3_t40_mem0
	S += t3_t40_mem0 <= t3_t40

	t3_t40_mem1 = S.Task('t3_t40_mem1', length=1, delay_cost=1)
	t3_t40_mem1 += MUL_mem[0]
	S += 28 < t3_t40_mem1
	S += t3_t40_mem1 <= t3_t40

	t3_t4_t5 = S.Task('t3_t4_t5', length=1, delay_cost=1)
	t3_t4_t5 += alt(ADD)

	t3_t4_t5_mem0 = S.Task('t3_t4_t5_mem0', length=1, delay_cost=1)
	t3_t4_t5_mem0 += MUL_mem[0]
	S += 23 < t3_t4_t5_mem0
	S += t3_t4_t5_mem0 <= t3_t4_t5

	t3_t4_t5_mem1 = S.Task('t3_t4_t5_mem1', length=1, delay_cost=1)
	t3_t4_t5_mem1 += MUL_mem[0]
	S += 28 < t3_t4_t5_mem1
	S += t3_t4_t5_mem1 <= t3_t4_t5

	t3_t50 = S.Task('t3_t50', length=1, delay_cost=1)
	t3_t50 += alt(ADD)

	t3_t50_mem0 = S.Task('t3_t50_mem0', length=1, delay_cost=1)
	t3_t50_mem0 += ADD_mem[1]
	S += 13 < t3_t50_mem0
	S += t3_t50_mem0 <= t3_t50

	t3_t50_mem1 = S.Task('t3_t50_mem1', length=1, delay_cost=1)
	t3_t50_mem1 += ADD_mem[0]
	S += 10 < t3_t50_mem1
	S += t3_t50_mem1 <= t3_t50

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	t4_t2_t0_in += alt(MUL_in)
	t4_t2_t0 = S.Task('t4_t2_t0', length=7, delay_cost=1)
	t4_t2_t0 += alt(MUL)
	S += t4_t2_t0>=t4_t2_t0_in

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	t4_t2_t0_mem0 += ADD_mem[3]
	S += 69 < t4_t2_t0_mem0
	S += t4_t2_t0_mem0 <= t4_t2_t0

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	t4_t2_t0_mem1 += ADD_mem[0]
	S += 18 < t4_t2_t0_mem1
	S += t4_t2_t0_mem1 <= t4_t2_t0

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	t4_t2_t1_in += alt(MUL_in)
	t4_t2_t1 = S.Task('t4_t2_t1', length=7, delay_cost=1)
	t4_t2_t1 += alt(MUL)
	S += t4_t2_t1>=t4_t2_t1_in

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	t4_t2_t1_mem0 += ADD_mem[1]
	S += 71 < t4_t2_t1_mem0
	S += t4_t2_t1_mem0 <= t4_t2_t1

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	t4_t2_t1_mem1 += ADD_mem[0]
	S += 9 < t4_t2_t1_mem1
	S += t4_t2_t1_mem1 <= t4_t2_t1

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	t4_t2_t2 += alt(ADD)

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	t4_t2_t2_mem0 += ADD_mem[3]
	S += 69 < t4_t2_t2_mem0
	S += t4_t2_t2_mem0 <= t4_t2_t2

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	t4_t2_t2_mem1 += ADD_mem[1]
	S += 71 < t4_t2_t2_mem1
	S += t4_t2_t2_mem1 <= t4_t2_t2

	t4_t31 = S.Task('t4_t31', length=1, delay_cost=1)
	t4_t31 += alt(ADD)

	t4_t31_mem0 = S.Task('t4_t31_mem0', length=1, delay_cost=1)
	t4_t31_mem0 += MUL_mem[0]
	S += 63 < t4_t31_mem0
	S += t4_t31_mem0 <= t4_t31

	t4_t31_mem1 = S.Task('t4_t31_mem1', length=1, delay_cost=1)
	t4_t31_mem1 += ADD_mem[3]
	S += 11 < t4_t31_mem1
	S += t4_t31_mem1 <= t4_t31

	t410 = S.Task('t410', length=1, delay_cost=1)
	t410 += alt(ADD)

	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	t410_mem0 += ADD_mem[0]
	S += 17 < t410_mem0
	S += t410_mem0 <= t410

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	t410_mem1 += ADD_mem[0]
	S += 17 < t410_mem1
	S += t410_mem1 <= t410

	t5_t01 = S.Task('t5_t01', length=1, delay_cost=1)
	t5_t01 += alt(ADD)

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	t5_t01_mem0 += MUL_mem[0]
	S += 54 < t5_t01_mem0
	S += t5_t01_mem0 <= t5_t01

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	t5_t01_mem1 += ADD_mem[2]
	S += 48 < t5_t01_mem1
	S += t5_t01_mem1 <= t5_t01

	t5_t11 = S.Task('t5_t11', length=1, delay_cost=1)
	t5_t11 += alt(ADD)

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	t5_t11_mem0 += MUL_mem[0]
	S += 57 < t5_t11_mem0
	S += t5_t11_mem0 <= t5_t11

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	t5_t11_mem1 += ADD_mem[2]
	S += 46 < t5_t11_mem1
	S += t5_t11_mem1 <= t5_t11

	t5_t4_t4_in = S.Task('t5_t4_t4_in', length=1, delay_cost=1)
	t5_t4_t4_in += alt(MUL_in)
	t5_t4_t4 = S.Task('t5_t4_t4', length=7, delay_cost=1)
	t5_t4_t4 += alt(MUL)
	S += t5_t4_t4>=t5_t4_t4_in

	t5_t4_t4_mem0 = S.Task('t5_t4_t4_mem0', length=1, delay_cost=1)
	t5_t4_t4_mem0 += ADD_mem[0]
	S += 61 < t5_t4_t4_mem0
	S += t5_t4_t4_mem0 <= t5_t4_t4

	t5_t4_t4_mem1 = S.Task('t5_t4_t4_mem1', length=1, delay_cost=1)
	t5_t4_t4_mem1 += ADD_mem[0]
	S += 62 < t5_t4_t4_mem1
	S += t5_t4_t4_mem1 <= t5_t4_t4

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	t5_t40 += alt(ADD)

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	t5_t40_mem0 += MUL_mem[0]
	S += 66 < t5_t40_mem0
	S += t5_t40_mem0 <= t5_t40

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	t5_t40_mem1 += MUL_mem[0]
	S += 69 < t5_t40_mem1
	S += t5_t40_mem1 <= t5_t40

	t5_t4_t5 = S.Task('t5_t4_t5', length=1, delay_cost=1)
	t5_t4_t5 += alt(ADD)

	t5_t4_t5_mem0 = S.Task('t5_t4_t5_mem0', length=1, delay_cost=1)
	t5_t4_t5_mem0 += MUL_mem[0]
	S += 66 < t5_t4_t5_mem0
	S += t5_t4_t5_mem0 <= t5_t4_t5

	t5_t4_t5_mem1 = S.Task('t5_t4_t5_mem1', length=1, delay_cost=1)
	t5_t4_t5_mem1 += MUL_mem[0]
	S += 69 < t5_t4_t5_mem1
	S += t5_t4_t5_mem1 <= t5_t4_t5

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	t5_t50 += alt(ADD)

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	t5_t50_mem0 += ADD_mem[0]
	S += 47 < t5_t50_mem0
	S += t5_t50_mem0 <= t5_t50

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	t5_t50_mem1 += ADD_mem[1]
	S += 45 < t5_t50_mem1
	S += t5_t50_mem1 <= t5_t50

	t6_t01 = S.Task('t6_t01', length=1, delay_cost=1)
	t6_t01 += alt(ADD)

	t6_t01_mem0 = S.Task('t6_t01_mem0', length=1, delay_cost=1)
	t6_t01_mem0 += MUL_mem[0]
	S += 64 < t6_t01_mem0
	S += t6_t01_mem0 <= t6_t01

	t6_t01_mem1 = S.Task('t6_t01_mem1', length=1, delay_cost=1)
	t6_t01_mem1 += ADD_mem[0]
	S += 43 < t6_t01_mem1
	S += t6_t01_mem1 <= t6_t01

	t6_t11 = S.Task('t6_t11', length=1, delay_cost=1)
	t6_t11 += alt(ADD)

	t6_t11_mem0 = S.Task('t6_t11_mem0', length=1, delay_cost=1)
	t6_t11_mem0 += MUL_mem[0]
	S += 61 < t6_t11_mem0
	S += t6_t11_mem0 <= t6_t11

	t6_t11_mem1 = S.Task('t6_t11_mem1', length=1, delay_cost=1)
	t6_t11_mem1 += ADD_mem[0]
	S += 40 < t6_t11_mem1
	S += t6_t11_mem1 <= t6_t11

	t6_t4_t4_in = S.Task('t6_t4_t4_in', length=1, delay_cost=1)
	t6_t4_t4_in += alt(MUL_in)
	t6_t4_t4 = S.Task('t6_t4_t4', length=7, delay_cost=1)
	t6_t4_t4 += alt(MUL)
	S += t6_t4_t4>=t6_t4_t4_in

	t6_t4_t4_mem0 = S.Task('t6_t4_t4_mem0', length=1, delay_cost=1)
	t6_t4_t4_mem0 += ADD_mem[2]
	S += 52 < t6_t4_t4_mem0
	S += t6_t4_t4_mem0 <= t6_t4_t4

	t6_t4_t4_mem1 = S.Task('t6_t4_t4_mem1', length=1, delay_cost=1)
	t6_t4_t4_mem1 += ADD_mem[1]
	S += 49 < t6_t4_t4_mem1
	S += t6_t4_t4_mem1 <= t6_t4_t4

	t6_t40 = S.Task('t6_t40', length=1, delay_cost=1)
	t6_t40 += alt(ADD)

	t6_t40_mem0 = S.Task('t6_t40_mem0', length=1, delay_cost=1)
	t6_t40_mem0 += MUL_mem[0]
	S += 58 < t6_t40_mem0
	S += t6_t40_mem0 <= t6_t40

	t6_t40_mem1 = S.Task('t6_t40_mem1', length=1, delay_cost=1)
	t6_t40_mem1 += MUL_mem[0]
	S += 56 < t6_t40_mem1
	S += t6_t40_mem1 <= t6_t40

	t6_t4_t5 = S.Task('t6_t4_t5', length=1, delay_cost=1)
	t6_t4_t5 += alt(ADD)

	t6_t4_t5_mem0 = S.Task('t6_t4_t5_mem0', length=1, delay_cost=1)
	t6_t4_t5_mem0 += MUL_mem[0]
	S += 58 < t6_t4_t5_mem0
	S += t6_t4_t5_mem0 <= t6_t4_t5

	t6_t4_t5_mem1 = S.Task('t6_t4_t5_mem1', length=1, delay_cost=1)
	t6_t4_t5_mem1 += MUL_mem[0]
	S += 56 < t6_t4_t5_mem1
	S += t6_t4_t5_mem1 <= t6_t4_t5

	t6_t50 = S.Task('t6_t50', length=1, delay_cost=1)
	t6_t50 += alt(ADD)

	t6_t50_mem0 = S.Task('t6_t50_mem0', length=1, delay_cost=1)
	t6_t50_mem0 += ADD_mem[0]
	S += 49 < t6_t50_mem0
	S += t6_t50_mem0 <= t6_t50

	t6_t50_mem1 = S.Task('t6_t50_mem1', length=1, delay_cost=1)
	t6_t50_mem1 += ADD_mem[1]
	S += 42 < t6_t50_mem1
	S += t6_t50_mem1 <= t6_t50

	t7_t01 = S.Task('t7_t01', length=1, delay_cost=1)
	t7_t01 += alt(ADD)

	t7_t01_mem0 = S.Task('t7_t01_mem0', length=1, delay_cost=1)
	t7_t01_mem0 += MUL_mem[0]
	S += 51 < t7_t01_mem0
	S += t7_t01_mem0 <= t7_t01

	t7_t01_mem1 = S.Task('t7_t01_mem1', length=1, delay_cost=1)
	t7_t01_mem1 += ADD_mem[0]
	S += 41 < t7_t01_mem1
	S += t7_t01_mem1 <= t7_t01

	t7_t11 = S.Task('t7_t11', length=1, delay_cost=1)
	t7_t11 += alt(ADD)

	t7_t11_mem0 = S.Task('t7_t11_mem0', length=1, delay_cost=1)
	t7_t11_mem0 += MUL_mem[0]
	S += 75 < t7_t11_mem0
	S += t7_t11_mem0 <= t7_t11

	t7_t11_mem1 = S.Task('t7_t11_mem1', length=1, delay_cost=1)
	t7_t11_mem1 += ADD_mem[1]
	S += 70 < t7_t11_mem1
	S += t7_t11_mem1 <= t7_t11

	t7_t4_t4_in = S.Task('t7_t4_t4_in', length=1, delay_cost=1)
	t7_t4_t4_in += alt(MUL_in)
	t7_t4_t4 = S.Task('t7_t4_t4', length=7, delay_cost=1)
	t7_t4_t4 += alt(MUL)
	S += t7_t4_t4>=t7_t4_t4_in

	t7_t4_t4_mem0 = S.Task('t7_t4_t4_mem0', length=1, delay_cost=1)
	t7_t4_t4_mem0 += ADD_mem[1]
	S += 65 < t7_t4_t4_mem0
	S += t7_t4_t4_mem0 <= t7_t4_t4

	t7_t4_t4_mem1 = S.Task('t7_t4_t4_mem1', length=1, delay_cost=1)
	t7_t4_t4_mem1 += ADD_mem[0]
	S += 67 < t7_t4_t4_mem1
	S += t7_t4_t4_mem1 <= t7_t4_t4

	t7_t40 = S.Task('t7_t40', length=1, delay_cost=1)
	t7_t40 += alt(ADD)

	t7_t40_mem0 = S.Task('t7_t40_mem0', length=1, delay_cost=1)
	t7_t40_mem0 += MUL_mem[0]
	S += 73 < t7_t40_mem0
	S += t7_t40_mem0 <= t7_t40

	t7_t40_mem1 = S.Task('t7_t40_mem1', length=1, delay_cost=1)
	t7_t40_mem1 += MUL_mem[0]
	S += 72 < t7_t40_mem1
	S += t7_t40_mem1 <= t7_t40

	t7_t4_t5 = S.Task('t7_t4_t5', length=1, delay_cost=1)
	t7_t4_t5 += alt(ADD)

	t7_t4_t5_mem0 = S.Task('t7_t4_t5_mem0', length=1, delay_cost=1)
	t7_t4_t5_mem0 += MUL_mem[0]
	S += 73 < t7_t4_t5_mem0
	S += t7_t4_t5_mem0 <= t7_t4_t5

	t7_t4_t5_mem1 = S.Task('t7_t4_t5_mem1', length=1, delay_cost=1)
	t7_t4_t5_mem1 += MUL_mem[0]
	S += 72 < t7_t4_t5_mem1
	S += t7_t4_t5_mem1 <= t7_t4_t5

	t7_t50 = S.Task('t7_t50', length=1, delay_cost=1)
	t7_t50 += alt(ADD)

	t7_t50_mem0 = S.Task('t7_t50_mem0', length=1, delay_cost=1)
	t7_t50_mem0 += ADD_mem[3]
	S += 44 < t7_t50_mem0
	S += t7_t50_mem0 <= t7_t50

	t7_t50_mem1 = S.Task('t7_t50_mem1', length=1, delay_cost=1)
	t7_t50_mem1 += ADD_mem[0]
	S += 69 < t7_t50_mem1
	S += t7_t50_mem1 <= t7_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-318/scheduling/SQR012345_mul1_add4/SQR012345_4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution
