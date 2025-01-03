from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 150
	S = Scenario("PADD_3", horizon=horizon)

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
	t2_t1_t1_in = S.Task('t2_t1_t1_in', length=1, delay_cost=1)
	S += t2_t1_t1_in >= 0
	t2_t1_t1_in += MUL_in[0]

	t2_t1_t1_mem0 = S.Task('t2_t1_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_t1_mem0 >= 0
	t2_t1_t1_mem0 += INPUT_mem_r

	t2_t1_t1_mem1 = S.Task('t2_t1_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_t1_mem1 >= 0
	t2_t1_t1_mem1 += INPUT_mem_r

	t0_t1_t1_in = S.Task('t0_t1_t1_in', length=1, delay_cost=1)
	S += t0_t1_t1_in >= 1
	t0_t1_t1_in += MUL_in[0]

	t0_t1_t1_mem0 = S.Task('t0_t1_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_t1_mem0 >= 1
	t0_t1_t1_mem0 += INPUT_mem_r

	t0_t1_t1_mem1 = S.Task('t0_t1_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_t1_mem1 >= 1
	t0_t1_t1_mem1 += INPUT_mem_r

	t2_t1_t1 = S.Task('t2_t1_t1', length=7, delay_cost=1)
	S += t2_t1_t1 >= 1
	t2_t1_t1 += MUL[0]

	t0_t1_t1 = S.Task('t0_t1_t1', length=7, delay_cost=1)
	S += t0_t1_t1 >= 2
	t0_t1_t1 += MUL[0]

	t2_t0_t1_in = S.Task('t2_t0_t1_in', length=1, delay_cost=1)
	S += t2_t0_t1_in >= 2
	t2_t0_t1_in += MUL_in[0]

	t2_t0_t1_mem0 = S.Task('t2_t0_t1_mem0', length=1, delay_cost=1)
	S += t2_t0_t1_mem0 >= 2
	t2_t0_t1_mem0 += INPUT_mem_r

	t2_t0_t1_mem1 = S.Task('t2_t0_t1_mem1', length=1, delay_cost=1)
	S += t2_t0_t1_mem1 >= 2
	t2_t0_t1_mem1 += INPUT_mem_r

	t2_t0_t0_in = S.Task('t2_t0_t0_in', length=1, delay_cost=1)
	S += t2_t0_t0_in >= 3
	t2_t0_t0_in += MUL_in[0]

	t2_t0_t0_mem0 = S.Task('t2_t0_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_t0_mem0 >= 3
	t2_t0_t0_mem0 += INPUT_mem_r

	t2_t0_t0_mem1 = S.Task('t2_t0_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_t0_mem1 >= 3
	t2_t0_t0_mem1 += INPUT_mem_r

	t2_t0_t1 = S.Task('t2_t0_t1', length=7, delay_cost=1)
	S += t2_t0_t1 >= 3
	t2_t0_t1 += MUL[0]

	t2_t0_t0 = S.Task('t2_t0_t0', length=7, delay_cost=1)
	S += t2_t0_t0 >= 4
	t2_t0_t0 += MUL[0]

	t2_t1_t0_in = S.Task('t2_t1_t0_in', length=1, delay_cost=1)
	S += t2_t1_t0_in >= 4
	t2_t1_t0_in += MUL_in[0]

	t2_t1_t0_mem0 = S.Task('t2_t1_t0_mem0', length=1, delay_cost=1)
	S += t2_t1_t0_mem0 >= 4
	t2_t1_t0_mem0 += INPUT_mem_r

	t2_t1_t0_mem1 = S.Task('t2_t1_t0_mem1', length=1, delay_cost=1)
	S += t2_t1_t0_mem1 >= 4
	t2_t1_t0_mem1 += INPUT_mem_r

	t0_t1_t0_in = S.Task('t0_t1_t0_in', length=1, delay_cost=1)
	S += t0_t1_t0_in >= 5
	t0_t1_t0_in += MUL_in[0]

	t0_t1_t0_mem0 = S.Task('t0_t1_t0_mem0', length=1, delay_cost=1)
	S += t0_t1_t0_mem0 >= 5
	t0_t1_t0_mem0 += INPUT_mem_r

	t0_t1_t0_mem1 = S.Task('t0_t1_t0_mem1', length=1, delay_cost=1)
	S += t0_t1_t0_mem1 >= 5
	t0_t1_t0_mem1 += INPUT_mem_r

	t2_t1_t0 = S.Task('t2_t1_t0', length=7, delay_cost=1)
	S += t2_t1_t0 >= 5
	t2_t1_t0 += MUL[0]

	t0_t0_t1_in = S.Task('t0_t0_t1_in', length=1, delay_cost=1)
	S += t0_t0_t1_in >= 6
	t0_t0_t1_in += MUL_in[0]

	t0_t0_t1_mem0 = S.Task('t0_t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t0_t1_mem0 >= 6
	t0_t0_t1_mem0 += INPUT_mem_r

	t0_t0_t1_mem1 = S.Task('t0_t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t0_t1_mem1 >= 6
	t0_t0_t1_mem1 += INPUT_mem_r

	t0_t1_t0 = S.Task('t0_t1_t0', length=7, delay_cost=1)
	S += t0_t1_t0 >= 6
	t0_t1_t0 += MUL[0]

	t0_t0_t0_in = S.Task('t0_t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_t0_in >= 7
	t0_t0_t0_in += MUL_in[0]

	t0_t0_t0_mem0 = S.Task('t0_t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_t0_mem0 >= 7
	t0_t0_t0_mem0 += INPUT_mem_r

	t0_t0_t0_mem1 = S.Task('t0_t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_t0_mem1 >= 7
	t0_t0_t0_mem1 += INPUT_mem_r

	t0_t0_t1 = S.Task('t0_t0_t1', length=7, delay_cost=1)
	S += t0_t0_t1 >= 7
	t0_t0_t1 += MUL[0]

	t0_t0_t0 = S.Task('t0_t0_t0', length=7, delay_cost=1)
	S += t0_t0_t0 >= 8
	t0_t0_t0 += MUL[0]

	t9_t0_t2_mem0 = S.Task('t9_t0_t2_mem0', length=1, delay_cost=1)
	S += t9_t0_t2_mem0 >= 8
	t9_t0_t2_mem0 += INPUT_mem_r

	t9_t0_t2_mem1 = S.Task('t9_t0_t2_mem1', length=1, delay_cost=1)
	S += t9_t0_t2_mem1 >= 8
	t9_t0_t2_mem1 += INPUT_mem_r

	t0_t20_mem0 = S.Task('t0_t20_mem0', length=1, delay_cost=1)
	S += t0_t20_mem0 >= 9
	t0_t20_mem0 += INPUT_mem_r

	t0_t20_mem1 = S.Task('t0_t20_mem1', length=1, delay_cost=1)
	S += t0_t20_mem1 >= 9
	t0_t20_mem1 += INPUT_mem_r

	t9_t0_t2 = S.Task('t9_t0_t2', length=1, delay_cost=1)
	S += t9_t0_t2 >= 9
	t9_t0_t2 += ADD[0]

	t0_t0_t2_mem0 = S.Task('t0_t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t0_t2_mem0 >= 10
	t0_t0_t2_mem0 += INPUT_mem_r

	t0_t0_t2_mem1 = S.Task('t0_t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t0_t2_mem1 >= 10
	t0_t0_t2_mem1 += INPUT_mem_r

	t0_t20 = S.Task('t0_t20', length=1, delay_cost=1)
	S += t0_t20 >= 10
	t0_t20 += ADD[0]

	t0_t0_t2 = S.Task('t0_t0_t2', length=1, delay_cost=1)
	S += t0_t0_t2 >= 11
	t0_t0_t2 += ADD[0]

	t0_t21_mem0 = S.Task('t0_t21_mem0', length=1, delay_cost=1)
	S += t0_t21_mem0 >= 11
	t0_t21_mem0 += INPUT_mem_r

	t0_t21_mem1 = S.Task('t0_t21_mem1', length=1, delay_cost=1)
	S += t0_t21_mem1 >= 11
	t0_t21_mem1 += INPUT_mem_r

	t2_t00_mem0 = S.Task('t2_t00_mem0', length=1, delay_cost=1)
	S += t2_t00_mem0 >= 11
	t2_t00_mem0 += MUL_mem[0]

	t2_t00_mem1 = S.Task('t2_t00_mem1', length=1, delay_cost=1)
	S += t2_t00_mem1 >= 11
	t2_t00_mem1 += MUL_mem[0]

	t0_t21 = S.Task('t0_t21', length=1, delay_cost=1)
	S += t0_t21 >= 12
	t0_t21 += ADD[0]

	t2_t00 = S.Task('t2_t00', length=1, delay_cost=1)
	S += t2_t00 >= 12
	t2_t00 += ADD[3]

	t2_t10_mem0 = S.Task('t2_t10_mem0', length=1, delay_cost=1)
	S += t2_t10_mem0 >= 12
	t2_t10_mem0 += MUL_mem[0]

	t2_t10_mem1 = S.Task('t2_t10_mem1', length=1, delay_cost=1)
	S += t2_t10_mem1 >= 12
	t2_t10_mem1 += MUL_mem[0]

	t7_t20_mem0 = S.Task('t7_t20_mem0', length=1, delay_cost=1)
	S += t7_t20_mem0 >= 12
	t7_t20_mem0 += INPUT_mem_r

	t7_t20_mem1 = S.Task('t7_t20_mem1', length=1, delay_cost=1)
	S += t7_t20_mem1 >= 12
	t7_t20_mem1 += INPUT_mem_r

	t0_t10_mem0 = S.Task('t0_t10_mem0', length=1, delay_cost=1)
	S += t0_t10_mem0 >= 13
	t0_t10_mem0 += MUL_mem[0]

	t0_t10_mem1 = S.Task('t0_t10_mem1', length=1, delay_cost=1)
	S += t0_t10_mem1 >= 13
	t0_t10_mem1 += MUL_mem[0]

	t0_t4_t2_mem0 = S.Task('t0_t4_t2_mem0', length=1, delay_cost=1)
	S += t0_t4_t2_mem0 >= 13
	t0_t4_t2_mem0 += ADD_mem[0]

	t0_t4_t2_mem1 = S.Task('t0_t4_t2_mem1', length=1, delay_cost=1)
	S += t0_t4_t2_mem1 >= 13
	t0_t4_t2_mem1 += ADD_mem[0]

	t2_t10 = S.Task('t2_t10', length=1, delay_cost=1)
	S += t2_t10 >= 13
	t2_t10 += ADD[3]

	t2_t31_mem0 = S.Task('t2_t31_mem0', length=1, delay_cost=1)
	S += t2_t31_mem0 >= 13
	t2_t31_mem0 += INPUT_mem_r

	t2_t31_mem1 = S.Task('t2_t31_mem1', length=1, delay_cost=1)
	S += t2_t31_mem1 >= 13
	t2_t31_mem1 += INPUT_mem_r

	t7_t20 = S.Task('t7_t20', length=1, delay_cost=1)
	S += t7_t20 >= 13
	t7_t20 += ADD[0]

	t0_t10 = S.Task('t0_t10', length=1, delay_cost=1)
	S += t0_t10 >= 14
	t0_t10 += ADD[2]

	t0_t31_mem0 = S.Task('t0_t31_mem0', length=1, delay_cost=1)
	S += t0_t31_mem0 >= 14
	t0_t31_mem0 += INPUT_mem_r

	t0_t31_mem1 = S.Task('t0_t31_mem1', length=1, delay_cost=1)
	S += t0_t31_mem1 >= 14
	t0_t31_mem1 += INPUT_mem_r

	t0_t4_t2 = S.Task('t0_t4_t2', length=1, delay_cost=1)
	S += t0_t4_t2 >= 14
	t0_t4_t2 += ADD[3]

	t2_t0_t5_mem0 = S.Task('t2_t0_t5_mem0', length=1, delay_cost=1)
	S += t2_t0_t5_mem0 >= 14
	t2_t0_t5_mem0 += MUL_mem[0]

	t2_t0_t5_mem1 = S.Task('t2_t0_t5_mem1', length=1, delay_cost=1)
	S += t2_t0_t5_mem1 >= 14
	t2_t0_t5_mem1 += MUL_mem[0]

	t2_t31 = S.Task('t2_t31', length=1, delay_cost=1)
	S += t2_t31 >= 14
	t2_t31 += ADD[0]

	t2_t50_mem0 = S.Task('t2_t50_mem0', length=1, delay_cost=1)
	S += t2_t50_mem0 >= 14
	t2_t50_mem0 += ADD_mem[3]

	t2_t50_mem1 = S.Task('t2_t50_mem1', length=1, delay_cost=1)
	S += t2_t50_mem1 >= 14
	t2_t50_mem1 += ADD_mem[3]

	t0_t00_mem0 = S.Task('t0_t00_mem0', length=1, delay_cost=1)
	S += t0_t00_mem0 >= 15
	t0_t00_mem0 += MUL_mem[0]

	t0_t00_mem1 = S.Task('t0_t00_mem1', length=1, delay_cost=1)
	S += t0_t00_mem1 >= 15
	t0_t00_mem1 += MUL_mem[0]

	t0_t31 = S.Task('t0_t31', length=1, delay_cost=1)
	S += t0_t31 >= 15
	t0_t31 += ADD[2]

	t2_t0_t5 = S.Task('t2_t0_t5', length=1, delay_cost=1)
	S += t2_t0_t5 >= 15
	t2_t0_t5 += ADD[1]

	t2_t30_mem0 = S.Task('t2_t30_mem0', length=1, delay_cost=1)
	S += t2_t30_mem0 >= 15
	t2_t30_mem0 += INPUT_mem_r

	t2_t30_mem1 = S.Task('t2_t30_mem1', length=1, delay_cost=1)
	S += t2_t30_mem1 >= 15
	t2_t30_mem1 += INPUT_mem_r

	t2_t50 = S.Task('t2_t50', length=1, delay_cost=1)
	S += t2_t50 >= 15
	t2_t50 += ADD[0]

	t0_t00 = S.Task('t0_t00', length=1, delay_cost=1)
	S += t0_t00 >= 16
	t0_t00 += ADD[1]

	t0_t0_t5_mem0 = S.Task('t0_t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t0_t5_mem0 >= 16
	t0_t0_t5_mem0 += MUL_mem[0]

	t0_t0_t5_mem1 = S.Task('t0_t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t0_t5_mem1 >= 16
	t0_t0_t5_mem1 += MUL_mem[0]

	t0_t4_t1_in = S.Task('t0_t4_t1_in', length=1, delay_cost=1)
	S += t0_t4_t1_in >= 16
	t0_t4_t1_in += MUL_in[0]

	t0_t4_t1_mem0 = S.Task('t0_t4_t1_mem0', length=1, delay_cost=1)
	S += t0_t4_t1_mem0 >= 16
	t0_t4_t1_mem0 += ADD_mem[0]

	t0_t4_t1_mem1 = S.Task('t0_t4_t1_mem1', length=1, delay_cost=1)
	S += t0_t4_t1_mem1 >= 16
	t0_t4_t1_mem1 += ADD_mem[2]

	t2_t30 = S.Task('t2_t30', length=1, delay_cost=1)
	S += t2_t30 >= 16
	t2_t30 += ADD[0]

	t7_t1_t2_mem0 = S.Task('t7_t1_t2_mem0', length=1, delay_cost=1)
	S += t7_t1_t2_mem0 >= 16
	t7_t1_t2_mem0 += INPUT_mem_r

	t7_t1_t2_mem1 = S.Task('t7_t1_t2_mem1', length=1, delay_cost=1)
	S += t7_t1_t2_mem1 >= 16
	t7_t1_t2_mem1 += INPUT_mem_r

	t0_t0_t5 = S.Task('t0_t0_t5', length=1, delay_cost=1)
	S += t0_t0_t5 >= 17
	t0_t0_t5 += ADD[0]

	t0_t1_t5_mem0 = S.Task('t0_t1_t5_mem0', length=1, delay_cost=1)
	S += t0_t1_t5_mem0 >= 17
	t0_t1_t5_mem0 += MUL_mem[0]

	t0_t1_t5_mem1 = S.Task('t0_t1_t5_mem1', length=1, delay_cost=1)
	S += t0_t1_t5_mem1 >= 17
	t0_t1_t5_mem1 += MUL_mem[0]

	t0_t4_t1 = S.Task('t0_t4_t1', length=7, delay_cost=1)
	S += t0_t4_t1 >= 17
	t0_t4_t1 += MUL[0]

	t0_t50_mem0 = S.Task('t0_t50_mem0', length=1, delay_cost=1)
	S += t0_t50_mem0 >= 17
	t0_t50_mem0 += ADD_mem[1]

	t0_t50_mem1 = S.Task('t0_t50_mem1', length=1, delay_cost=1)
	S += t0_t50_mem1 >= 17
	t0_t50_mem1 += ADD_mem[2]

	t2_t21_mem0 = S.Task('t2_t21_mem0', length=1, delay_cost=1)
	S += t2_t21_mem0 >= 17
	t2_t21_mem0 += INPUT_mem_r

	t2_t21_mem1 = S.Task('t2_t21_mem1', length=1, delay_cost=1)
	S += t2_t21_mem1 >= 17
	t2_t21_mem1 += INPUT_mem_r

	t2_t4_t3_mem0 = S.Task('t2_t4_t3_mem0', length=1, delay_cost=1)
	S += t2_t4_t3_mem0 >= 17
	t2_t4_t3_mem0 += ADD_mem[0]

	t2_t4_t3_mem1 = S.Task('t2_t4_t3_mem1', length=1, delay_cost=1)
	S += t2_t4_t3_mem1 >= 17
	t2_t4_t3_mem1 += ADD_mem[0]

	t7_t1_t2 = S.Task('t7_t1_t2', length=1, delay_cost=1)
	S += t7_t1_t2 >= 17
	t7_t1_t2 += ADD[1]

	t0_t1_t5 = S.Task('t0_t1_t5', length=1, delay_cost=1)
	S += t0_t1_t5 >= 18
	t0_t1_t5 += ADD[3]

	t0_t50 = S.Task('t0_t50', length=1, delay_cost=1)
	S += t0_t50 >= 18
	t0_t50 += ADD[1]

	t2_t1_t5_mem0 = S.Task('t2_t1_t5_mem0', length=1, delay_cost=1)
	S += t2_t1_t5_mem0 >= 18
	t2_t1_t5_mem0 += MUL_mem[0]

	t2_t1_t5_mem1 = S.Task('t2_t1_t5_mem1', length=1, delay_cost=1)
	S += t2_t1_t5_mem1 >= 18
	t2_t1_t5_mem1 += MUL_mem[0]

	t2_t21 = S.Task('t2_t21', length=1, delay_cost=1)
	S += t2_t21 >= 18
	t2_t21 += ADD[0]

	t2_t4_t3 = S.Task('t2_t4_t3', length=1, delay_cost=1)
	S += t2_t4_t3 >= 18
	t2_t4_t3 += ADD[2]

	t9_t1_t2_mem0 = S.Task('t9_t1_t2_mem0', length=1, delay_cost=1)
	S += t9_t1_t2_mem0 >= 18
	t9_t1_t2_mem0 += INPUT_mem_r

	t9_t1_t2_mem1 = S.Task('t9_t1_t2_mem1', length=1, delay_cost=1)
	S += t9_t1_t2_mem1 >= 18
	t9_t1_t2_mem1 += INPUT_mem_r

	t2_t1_t5 = S.Task('t2_t1_t5', length=1, delay_cost=1)
	S += t2_t1_t5 >= 19
	t2_t1_t5 += ADD[1]

	t2_t4_t1_in = S.Task('t2_t4_t1_in', length=1, delay_cost=1)
	S += t2_t4_t1_in >= 19
	t2_t4_t1_in += MUL_in[0]

	t2_t4_t1_mem0 = S.Task('t2_t4_t1_mem0', length=1, delay_cost=1)
	S += t2_t4_t1_mem0 >= 19
	t2_t4_t1_mem0 += ADD_mem[0]

	t2_t4_t1_mem1 = S.Task('t2_t4_t1_mem1', length=1, delay_cost=1)
	S += t2_t4_t1_mem1 >= 19
	t2_t4_t1_mem1 += ADD_mem[0]

	t7_t21_mem0 = S.Task('t7_t21_mem0', length=1, delay_cost=1)
	S += t7_t21_mem0 >= 19
	t7_t21_mem0 += INPUT_mem_r

	t7_t21_mem1 = S.Task('t7_t21_mem1', length=1, delay_cost=1)
	S += t7_t21_mem1 >= 19
	t7_t21_mem1 += INPUT_mem_r

	t9_t1_t2 = S.Task('t9_t1_t2', length=1, delay_cost=1)
	S += t9_t1_t2 >= 19
	t9_t1_t2 += ADD[0]

	t0_t1_t3_mem0 = S.Task('t0_t1_t3_mem0', length=1, delay_cost=1)
	S += t0_t1_t3_mem0 >= 20
	t0_t1_t3_mem0 += INPUT_mem_r

	t0_t1_t3_mem1 = S.Task('t0_t1_t3_mem1', length=1, delay_cost=1)
	S += t0_t1_t3_mem1 >= 20
	t0_t1_t3_mem1 += INPUT_mem_r

	t2_t4_t1 = S.Task('t2_t4_t1', length=7, delay_cost=1)
	S += t2_t4_t1 >= 20
	t2_t4_t1 += MUL[0]

	t7_t21 = S.Task('t7_t21', length=1, delay_cost=1)
	S += t7_t21 >= 20
	t7_t21 += ADD[0]

	t0_t1_t3 = S.Task('t0_t1_t3', length=1, delay_cost=1)
	S += t0_t1_t3 >= 21
	t0_t1_t3 += ADD[0]

	t0_t30_mem0 = S.Task('t0_t30_mem0', length=1, delay_cost=1)
	S += t0_t30_mem0 >= 21
	t0_t30_mem0 += INPUT_mem_r

	t0_t30_mem1 = S.Task('t0_t30_mem1', length=1, delay_cost=1)
	S += t0_t30_mem1 >= 21
	t0_t30_mem1 += INPUT_mem_r

	t7_t4_t2_mem0 = S.Task('t7_t4_t2_mem0', length=1, delay_cost=1)
	S += t7_t4_t2_mem0 >= 21
	t7_t4_t2_mem0 += ADD_mem[0]

	t7_t4_t2_mem1 = S.Task('t7_t4_t2_mem1', length=1, delay_cost=1)
	S += t7_t4_t2_mem1 >= 21
	t7_t4_t2_mem1 += ADD_mem[0]

	t0_t1_t2_mem0 = S.Task('t0_t1_t2_mem0', length=1, delay_cost=1)
	S += t0_t1_t2_mem0 >= 22
	t0_t1_t2_mem0 += INPUT_mem_r

	t0_t1_t2_mem1 = S.Task('t0_t1_t2_mem1', length=1, delay_cost=1)
	S += t0_t1_t2_mem1 >= 22
	t0_t1_t2_mem1 += INPUT_mem_r

	t0_t30 = S.Task('t0_t30', length=1, delay_cost=1)
	S += t0_t30 >= 22
	t0_t30 += ADD[0]

	t7_t4_t2 = S.Task('t7_t4_t2', length=1, delay_cost=1)
	S += t7_t4_t2 >= 22
	t7_t4_t2 += ADD[1]

	t0_t1_t2 = S.Task('t0_t1_t2', length=1, delay_cost=1)
	S += t0_t1_t2 >= 23
	t0_t1_t2 += ADD[0]

	t0_t4_t0_in = S.Task('t0_t4_t0_in', length=1, delay_cost=1)
	S += t0_t4_t0_in >= 23
	t0_t4_t0_in += MUL_in[0]

	t0_t4_t0_mem0 = S.Task('t0_t4_t0_mem0', length=1, delay_cost=1)
	S += t0_t4_t0_mem0 >= 23
	t0_t4_t0_mem0 += ADD_mem[0]

	t0_t4_t0_mem1 = S.Task('t0_t4_t0_mem1', length=1, delay_cost=1)
	S += t0_t4_t0_mem1 >= 23
	t0_t4_t0_mem1 += ADD_mem[0]

	t7_t0_t2_mem0 = S.Task('t7_t0_t2_mem0', length=1, delay_cost=1)
	S += t7_t0_t2_mem0 >= 23
	t7_t0_t2_mem0 += INPUT_mem_r

	t7_t0_t2_mem1 = S.Task('t7_t0_t2_mem1', length=1, delay_cost=1)
	S += t7_t0_t2_mem1 >= 23
	t7_t0_t2_mem1 += INPUT_mem_r

	t0_t0_t3_mem0 = S.Task('t0_t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t0_t3_mem0 >= 24
	t0_t0_t3_mem0 += INPUT_mem_r

	t0_t0_t3_mem1 = S.Task('t0_t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t0_t3_mem1 >= 24
	t0_t0_t3_mem1 += INPUT_mem_r

	t0_t1_t4_in = S.Task('t0_t1_t4_in', length=1, delay_cost=1)
	S += t0_t1_t4_in >= 24
	t0_t1_t4_in += MUL_in[0]

	t0_t1_t4_mem0 = S.Task('t0_t1_t4_mem0', length=1, delay_cost=1)
	S += t0_t1_t4_mem0 >= 24
	t0_t1_t4_mem0 += ADD_mem[0]

	t0_t1_t4_mem1 = S.Task('t0_t1_t4_mem1', length=1, delay_cost=1)
	S += t0_t1_t4_mem1 >= 24
	t0_t1_t4_mem1 += ADD_mem[0]

	t0_t4_t0 = S.Task('t0_t4_t0', length=7, delay_cost=1)
	S += t0_t4_t0 >= 24
	t0_t4_t0 += MUL[0]

	t7_t0_t2 = S.Task('t7_t0_t2', length=1, delay_cost=1)
	S += t7_t0_t2 >= 24
	t7_t0_t2 += ADD[1]

	t0_t0_t3 = S.Task('t0_t0_t3', length=1, delay_cost=1)
	S += t0_t0_t3 >= 25
	t0_t0_t3 += ADD[3]

	t0_t1_t4 = S.Task('t0_t1_t4', length=7, delay_cost=1)
	S += t0_t1_t4 >= 25
	t0_t1_t4 += MUL[0]

	t0_t4_t3_mem0 = S.Task('t0_t4_t3_mem0', length=1, delay_cost=1)
	S += t0_t4_t3_mem0 >= 25
	t0_t4_t3_mem0 += ADD_mem[0]

	t0_t4_t3_mem1 = S.Task('t0_t4_t3_mem1', length=1, delay_cost=1)
	S += t0_t4_t3_mem1 >= 25
	t0_t4_t3_mem1 += ADD_mem[2]

	t2_t20_mem0 = S.Task('t2_t20_mem0', length=1, delay_cost=1)
	S += t2_t20_mem0 >= 25
	t2_t20_mem0 += INPUT_mem_r

	t2_t20_mem1 = S.Task('t2_t20_mem1', length=1, delay_cost=1)
	S += t2_t20_mem1 >= 25
	t2_t20_mem1 += INPUT_mem_r

	t0_t0_t4_in = S.Task('t0_t0_t4_in', length=1, delay_cost=1)
	S += t0_t0_t4_in >= 26
	t0_t0_t4_in += MUL_in[0]

	t0_t0_t4_mem0 = S.Task('t0_t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t0_t4_mem0 >= 26
	t0_t0_t4_mem0 += ADD_mem[0]

	t0_t0_t4_mem1 = S.Task('t0_t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t0_t4_mem1 >= 26
	t0_t0_t4_mem1 += ADD_mem[3]

	t0_t4_t3 = S.Task('t0_t4_t3', length=1, delay_cost=1)
	S += t0_t4_t3 >= 26
	t0_t4_t3 += ADD[0]

	t2_t1_t3_mem0 = S.Task('t2_t1_t3_mem0', length=1, delay_cost=1)
	S += t2_t1_t3_mem0 >= 26
	t2_t1_t3_mem0 += INPUT_mem_r

	t2_t1_t3_mem1 = S.Task('t2_t1_t3_mem1', length=1, delay_cost=1)
	S += t2_t1_t3_mem1 >= 26
	t2_t1_t3_mem1 += INPUT_mem_r

	t2_t20 = S.Task('t2_t20', length=1, delay_cost=1)
	S += t2_t20 >= 26
	t2_t20 += ADD[2]

	t0_t0_t4 = S.Task('t0_t0_t4', length=7, delay_cost=1)
	S += t0_t0_t4 >= 27
	t0_t0_t4 += MUL[0]

	t2_t1_t2_mem0 = S.Task('t2_t1_t2_mem0', length=1, delay_cost=1)
	S += t2_t1_t2_mem0 >= 27
	t2_t1_t2_mem0 += INPUT_mem_r

	t2_t1_t2_mem1 = S.Task('t2_t1_t2_mem1', length=1, delay_cost=1)
	S += t2_t1_t2_mem1 >= 27
	t2_t1_t2_mem1 += INPUT_mem_r

	t2_t1_t3 = S.Task('t2_t1_t3', length=1, delay_cost=1)
	S += t2_t1_t3 >= 27
	t2_t1_t3 += ADD[0]

	t2_t4_t0_in = S.Task('t2_t4_t0_in', length=1, delay_cost=1)
	S += t2_t4_t0_in >= 27
	t2_t4_t0_in += MUL_in[0]

	t2_t4_t0_mem0 = S.Task('t2_t4_t0_mem0', length=1, delay_cost=1)
	S += t2_t4_t0_mem0 >= 27
	t2_t4_t0_mem0 += ADD_mem[2]

	t2_t4_t0_mem1 = S.Task('t2_t4_t0_mem1', length=1, delay_cost=1)
	S += t2_t4_t0_mem1 >= 27
	t2_t4_t0_mem1 += ADD_mem[0]

	t2_t4_t2_mem0 = S.Task('t2_t4_t2_mem0', length=1, delay_cost=1)
	S += t2_t4_t2_mem0 >= 27
	t2_t4_t2_mem0 += ADD_mem[2]

	t2_t4_t2_mem1 = S.Task('t2_t4_t2_mem1', length=1, delay_cost=1)
	S += t2_t4_t2_mem1 >= 27
	t2_t4_t2_mem1 += ADD_mem[0]

	t0_t4_t4_in = S.Task('t0_t4_t4_in', length=1, delay_cost=1)
	S += t0_t4_t4_in >= 28
	t0_t4_t4_in += MUL_in[0]

	t0_t4_t4_mem0 = S.Task('t0_t4_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_t4_mem0 >= 28
	t0_t4_t4_mem0 += ADD_mem[3]

	t0_t4_t4_mem1 = S.Task('t0_t4_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_t4_mem1 >= 28
	t0_t4_t4_mem1 += ADD_mem[0]

	t2_t0_t3_mem0 = S.Task('t2_t0_t3_mem0', length=1, delay_cost=1)
	S += t2_t0_t3_mem0 >= 28
	t2_t0_t3_mem0 += INPUT_mem_r

	t2_t0_t3_mem1 = S.Task('t2_t0_t3_mem1', length=1, delay_cost=1)
	S += t2_t0_t3_mem1 >= 28
	t2_t0_t3_mem1 += INPUT_mem_r

	t2_t1_t2 = S.Task('t2_t1_t2', length=1, delay_cost=1)
	S += t2_t1_t2 >= 28
	t2_t1_t2 += ADD[0]

	t2_t4_t0 = S.Task('t2_t4_t0', length=7, delay_cost=1)
	S += t2_t4_t0 >= 28
	t2_t4_t0 += MUL[0]

	t2_t4_t2 = S.Task('t2_t4_t2', length=1, delay_cost=1)
	S += t2_t4_t2 >= 28
	t2_t4_t2 += ADD[1]

	t0_t4_t4 = S.Task('t0_t4_t4', length=7, delay_cost=1)
	S += t0_t4_t4 >= 29
	t0_t4_t4 += MUL[0]

	t2_t0_t2_mem0 = S.Task('t2_t0_t2_mem0', length=1, delay_cost=1)
	S += t2_t0_t2_mem0 >= 29
	t2_t0_t2_mem0 += INPUT_mem_r

	t2_t0_t2_mem1 = S.Task('t2_t0_t2_mem1', length=1, delay_cost=1)
	S += t2_t0_t2_mem1 >= 29
	t2_t0_t2_mem1 += INPUT_mem_r

	t2_t0_t3 = S.Task('t2_t0_t3', length=1, delay_cost=1)
	S += t2_t0_t3 >= 29
	t2_t0_t3 += ADD[3]

	t2_t1_t4_in = S.Task('t2_t1_t4_in', length=1, delay_cost=1)
	S += t2_t1_t4_in >= 29
	t2_t1_t4_in += MUL_in[0]

	t2_t1_t4_mem0 = S.Task('t2_t1_t4_mem0', length=1, delay_cost=1)
	S += t2_t1_t4_mem0 >= 29
	t2_t1_t4_mem0 += ADD_mem[0]

	t2_t1_t4_mem1 = S.Task('t2_t1_t4_mem1', length=1, delay_cost=1)
	S += t2_t1_t4_mem1 >= 29
	t2_t1_t4_mem1 += ADD_mem[0]

	new_TZ_t20_mem0 = S.Task('new_TZ_t20_mem0', length=1, delay_cost=1)
	S += new_TZ_t20_mem0 >= 30
	new_TZ_t20_mem0 += INPUT_mem_r

	new_TZ_t20_mem1 = S.Task('new_TZ_t20_mem1', length=1, delay_cost=1)
	S += new_TZ_t20_mem1 >= 30
	new_TZ_t20_mem1 += INPUT_mem_r

	t2_t0_t2 = S.Task('t2_t0_t2', length=1, delay_cost=1)
	S += t2_t0_t2 >= 30
	t2_t0_t2 += ADD[2]

	t2_t1_t4 = S.Task('t2_t1_t4', length=7, delay_cost=1)
	S += t2_t1_t4 >= 30
	t2_t1_t4 += MUL[0]

	t2_t4_t4_in = S.Task('t2_t4_t4_in', length=1, delay_cost=1)
	S += t2_t4_t4_in >= 30
	t2_t4_t4_in += MUL_in[0]

	t2_t4_t4_mem0 = S.Task('t2_t4_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_t4_mem0 >= 30
	t2_t4_t4_mem0 += ADD_mem[1]

	t2_t4_t4_mem1 = S.Task('t2_t4_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_t4_mem1 >= 30
	t2_t4_t4_mem1 += ADD_mem[2]

	new_TZ_t1_t2_mem0 = S.Task('new_TZ_t1_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_t2_mem0 >= 31
	new_TZ_t1_t2_mem0 += INPUT_mem_r

	new_TZ_t1_t2_mem1 = S.Task('new_TZ_t1_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_t2_mem1 >= 31
	new_TZ_t1_t2_mem1 += INPUT_mem_r

	new_TZ_t20 = S.Task('new_TZ_t20', length=1, delay_cost=1)
	S += new_TZ_t20 >= 31
	new_TZ_t20 += ADD[1]

	t0_t40_mem0 = S.Task('t0_t40_mem0', length=1, delay_cost=1)
	S += t0_t40_mem0 >= 31
	t0_t40_mem0 += MUL_mem[0]

	t0_t40_mem1 = S.Task('t0_t40_mem1', length=1, delay_cost=1)
	S += t0_t40_mem1 >= 31
	t0_t40_mem1 += MUL_mem[0]

	t2_t0_t4_in = S.Task('t2_t0_t4_in', length=1, delay_cost=1)
	S += t2_t0_t4_in >= 31
	t2_t0_t4_in += MUL_in[0]

	t2_t0_t4_mem0 = S.Task('t2_t0_t4_mem0', length=1, delay_cost=1)
	S += t2_t0_t4_mem0 >= 31
	t2_t0_t4_mem0 += ADD_mem[2]

	t2_t0_t4_mem1 = S.Task('t2_t0_t4_mem1', length=1, delay_cost=1)
	S += t2_t0_t4_mem1 >= 31
	t2_t0_t4_mem1 += ADD_mem[3]

	t2_t4_t4 = S.Task('t2_t4_t4', length=7, delay_cost=1)
	S += t2_t4_t4 >= 31
	t2_t4_t4 += MUL[0]

	new_TZ_t1_t2 = S.Task('new_TZ_t1_t2', length=1, delay_cost=1)
	S += new_TZ_t1_t2 >= 32
	new_TZ_t1_t2 += ADD[0]

	new_TZ_t21_mem0 = S.Task('new_TZ_t21_mem0', length=1, delay_cost=1)
	S += new_TZ_t21_mem0 >= 32
	new_TZ_t21_mem0 += INPUT_mem_r

	new_TZ_t21_mem1 = S.Task('new_TZ_t21_mem1', length=1, delay_cost=1)
	S += new_TZ_t21_mem1 >= 32
	new_TZ_t21_mem1 += INPUT_mem_r

	t0_t11_mem0 = S.Task('t0_t11_mem0', length=1, delay_cost=1)
	S += t0_t11_mem0 >= 32
	t0_t11_mem0 += MUL_mem[0]

	t0_t11_mem1 = S.Task('t0_t11_mem1', length=1, delay_cost=1)
	S += t0_t11_mem1 >= 32
	t0_t11_mem1 += ADD_mem[3]

	t0_t40 = S.Task('t0_t40', length=1, delay_cost=1)
	S += t0_t40 >= 32
	t0_t40 += ADD[1]

	t2_t0_t4 = S.Task('t2_t0_t4', length=7, delay_cost=1)
	S += t2_t0_t4 >= 32
	t2_t0_t4 += MUL[0]

	new_TZ_t21 = S.Task('new_TZ_t21', length=1, delay_cost=1)
	S += new_TZ_t21 >= 33
	new_TZ_t21 += ADD[3]

	t010_mem0 = S.Task('t010_mem0', length=1, delay_cost=1)
	S += t010_mem0 >= 33
	t010_mem0 += ADD_mem[1]

	t010_mem1 = S.Task('t010_mem1', length=1, delay_cost=1)
	S += t010_mem1 >= 33
	t010_mem1 += ADD_mem[1]

	t0_t11 = S.Task('t0_t11', length=1, delay_cost=1)
	S += t0_t11 >= 33
	t0_t11 += ADD[1]

	t0_t4_t5_mem0 = S.Task('t0_t4_t5_mem0', length=1, delay_cost=1)
	S += t0_t4_t5_mem0 >= 33
	t0_t4_t5_mem0 += MUL_mem[0]

	t0_t4_t5_mem1 = S.Task('t0_t4_t5_mem1', length=1, delay_cost=1)
	S += t0_t4_t5_mem1 >= 33
	t0_t4_t5_mem1 += MUL_mem[0]

	t9_t20_mem0 = S.Task('t9_t20_mem0', length=1, delay_cost=1)
	S += t9_t20_mem0 >= 33
	t9_t20_mem0 += INPUT_mem_r

	t9_t20_mem1 = S.Task('t9_t20_mem1', length=1, delay_cost=1)
	S += t9_t20_mem1 >= 33
	t9_t20_mem1 += INPUT_mem_r

	t010 = S.Task('t010', length=1, delay_cost=1)
	S += t010 >= 34
	t010 += ADD[0]

	t0_s00_mem0 = S.Task('t0_s00_mem0', length=1, delay_cost=1)
	S += t0_s00_mem0 >= 34
	t0_s00_mem0 += ADD_mem[2]

	t0_s00_mem1 = S.Task('t0_s00_mem1', length=1, delay_cost=1)
	S += t0_s00_mem1 >= 34
	t0_s00_mem1 += ADD_mem[1]

	t0_s01_mem0 = S.Task('t0_s01_mem0', length=1, delay_cost=1)
	S += t0_s01_mem0 >= 34
	t0_s01_mem0 += ADD_mem[1]

	t0_s01_mem1 = S.Task('t0_s01_mem1', length=1, delay_cost=1)
	S += t0_s01_mem1 >= 34
	t0_s01_mem1 += ADD_mem[2]

	t0_t01_mem0 = S.Task('t0_t01_mem0', length=1, delay_cost=1)
	S += t0_t01_mem0 >= 34
	t0_t01_mem0 += MUL_mem[0]

	t0_t01_mem1 = S.Task('t0_t01_mem1', length=1, delay_cost=1)
	S += t0_t01_mem1 >= 34
	t0_t01_mem1 += ADD_mem[0]

	t0_t4_t5 = S.Task('t0_t4_t5', length=1, delay_cost=1)
	S += t0_t4_t5 >= 34
	t0_t4_t5 += ADD[3]

	t16_t0_t2_mem0 = S.Task('t16_t0_t2_mem0', length=1, delay_cost=1)
	S += t16_t0_t2_mem0 >= 34
	t16_t0_t2_mem0 += INPUT_mem_r

	t16_t0_t2_mem1 = S.Task('t16_t0_t2_mem1', length=1, delay_cost=1)
	S += t16_t0_t2_mem1 >= 34
	t16_t0_t2_mem1 += INPUT_mem_r

	t9_t20 = S.Task('t9_t20', length=1, delay_cost=1)
	S += t9_t20 >= 34
	t9_t20 += ADD[2]

	new_TZ_t4_t2_mem0 = S.Task('new_TZ_t4_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_t2_mem0 >= 35
	new_TZ_t4_t2_mem0 += ADD_mem[1]

	new_TZ_t4_t2_mem1 = S.Task('new_TZ_t4_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_t2_mem1 >= 35
	new_TZ_t4_t2_mem1 += ADD_mem[3]

	t0_s00 = S.Task('t0_s00', length=1, delay_cost=1)
	S += t0_s00 >= 35
	t0_s00 += ADD[3]

	t0_s01 = S.Task('t0_s01', length=1, delay_cost=1)
	S += t0_s01 >= 35
	t0_s01 += ADD[1]

	t0_t01 = S.Task('t0_t01', length=1, delay_cost=1)
	S += t0_t01 >= 35
	t0_t01 += ADD[0]

	t16_t0_t2 = S.Task('t16_t0_t2', length=1, delay_cost=1)
	S += t16_t0_t2 >= 35
	t16_t0_t2 += ADD[2]

	t16_t1_t2_mem0 = S.Task('t16_t1_t2_mem0', length=1, delay_cost=1)
	S += t16_t1_t2_mem0 >= 35
	t16_t1_t2_mem0 += INPUT_mem_r

	t16_t1_t2_mem1 = S.Task('t16_t1_t2_mem1', length=1, delay_cost=1)
	S += t16_t1_t2_mem1 >= 35
	t16_t1_t2_mem1 += INPUT_mem_r

	t2_t40_mem0 = S.Task('t2_t40_mem0', length=1, delay_cost=1)
	S += t2_t40_mem0 >= 35
	t2_t40_mem0 += MUL_mem[0]

	t2_t40_mem1 = S.Task('t2_t40_mem1', length=1, delay_cost=1)
	S += t2_t40_mem1 >= 35
	t2_t40_mem1 += MUL_mem[0]

	new_TZ_t4_t2 = S.Task('new_TZ_t4_t2', length=1, delay_cost=1)
	S += new_TZ_t4_t2 >= 36
	new_TZ_t4_t2 += ADD[0]

	t000_mem0 = S.Task('t000_mem0', length=1, delay_cost=1)
	S += t000_mem0 >= 36
	t000_mem0 += ADD_mem[1]

	t000_mem1 = S.Task('t000_mem1', length=1, delay_cost=1)
	S += t000_mem1 >= 36
	t000_mem1 += ADD_mem[3]

	t0_t51_mem0 = S.Task('t0_t51_mem0', length=1, delay_cost=1)
	S += t0_t51_mem0 >= 36
	t0_t51_mem0 += ADD_mem[0]

	t0_t51_mem1 = S.Task('t0_t51_mem1', length=1, delay_cost=1)
	S += t0_t51_mem1 >= 36
	t0_t51_mem1 += ADD_mem[1]

	t16_t1_t2 = S.Task('t16_t1_t2', length=1, delay_cost=1)
	S += t16_t1_t2 >= 36
	t16_t1_t2 += ADD[2]

	t16_t20_mem0 = S.Task('t16_t20_mem0', length=1, delay_cost=1)
	S += t16_t20_mem0 >= 36
	t16_t20_mem0 += INPUT_mem_r

	t16_t20_mem1 = S.Task('t16_t20_mem1', length=1, delay_cost=1)
	S += t16_t20_mem1 >= 36
	t16_t20_mem1 += INPUT_mem_r

	t2_t40 = S.Task('t2_t40', length=1, delay_cost=1)
	S += t2_t40 >= 36
	t2_t40 += ADD[3]

	t2_t4_t5_mem0 = S.Task('t2_t4_t5_mem0', length=1, delay_cost=1)
	S += t2_t4_t5_mem0 >= 36
	t2_t4_t5_mem0 += MUL_mem[0]

	t2_t4_t5_mem1 = S.Task('t2_t4_t5_mem1', length=1, delay_cost=1)
	S += t2_t4_t5_mem1 >= 36
	t2_t4_t5_mem1 += MUL_mem[0]

	t000 = S.Task('t000', length=1, delay_cost=1)
	S += t000 >= 37
	t000 += ADD[3]

	t0_t41_mem0 = S.Task('t0_t41_mem0', length=1, delay_cost=1)
	S += t0_t41_mem0 >= 37
	t0_t41_mem0 += MUL_mem[0]

	t0_t41_mem1 = S.Task('t0_t41_mem1', length=1, delay_cost=1)
	S += t0_t41_mem1 >= 37
	t0_t41_mem1 += ADD_mem[3]

	t0_t51 = S.Task('t0_t51', length=1, delay_cost=1)
	S += t0_t51 >= 37
	t0_t51 += ADD[1]

	t16_t20 = S.Task('t16_t20', length=1, delay_cost=1)
	S += t16_t20 >= 37
	t16_t20 += ADD[2]

	t16_t21_mem0 = S.Task('t16_t21_mem0', length=1, delay_cost=1)
	S += t16_t21_mem0 >= 37
	t16_t21_mem0 += INPUT_mem_r

	t16_t21_mem1 = S.Task('t16_t21_mem1', length=1, delay_cost=1)
	S += t16_t21_mem1 >= 37
	t16_t21_mem1 += INPUT_mem_r

	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	S += t210_mem0 >= 37
	t210_mem0 += ADD_mem[3]

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	S += t210_mem1 >= 37
	t210_mem1 += ADD_mem[0]

	t2_t11_mem0 = S.Task('t2_t11_mem0', length=1, delay_cost=1)
	S += t2_t11_mem0 >= 37
	t2_t11_mem0 += MUL_mem[0]

	t2_t11_mem1 = S.Task('t2_t11_mem1', length=1, delay_cost=1)
	S += t2_t11_mem1 >= 37
	t2_t11_mem1 += ADD_mem[1]

	t2_t4_t5 = S.Task('t2_t4_t5', length=1, delay_cost=1)
	S += t2_t4_t5 >= 37
	t2_t4_t5 += ADD[0]

	t001_mem0 = S.Task('t001_mem0', length=1, delay_cost=1)
	S += t001_mem0 >= 38
	t001_mem0 += ADD_mem[0]

	t001_mem1 = S.Task('t001_mem1', length=1, delay_cost=1)
	S += t001_mem1 >= 38
	t001_mem1 += ADD_mem[1]

	t0_t41 = S.Task('t0_t41', length=1, delay_cost=1)
	S += t0_t41 >= 38
	t0_t41 += ADD[3]

	t16_t21 = S.Task('t16_t21', length=1, delay_cost=1)
	S += t16_t21 >= 38
	t16_t21 += ADD[2]

	t17_t0_t2_mem0 = S.Task('t17_t0_t2_mem0', length=1, delay_cost=1)
	S += t17_t0_t2_mem0 >= 38
	t17_t0_t2_mem0 += INPUT_mem_r

	t17_t0_t2_mem1 = S.Task('t17_t0_t2_mem1', length=1, delay_cost=1)
	S += t17_t0_t2_mem1 >= 38
	t17_t0_t2_mem1 += INPUT_mem_r

	t210 = S.Task('t210', length=1, delay_cost=1)
	S += t210 >= 38
	t210 += ADD[1]

	t2_t11 = S.Task('t2_t11', length=1, delay_cost=1)
	S += t2_t11 >= 38
	t2_t11 += ADD[0]

	t2_t41_mem0 = S.Task('t2_t41_mem0', length=1, delay_cost=1)
	S += t2_t41_mem0 >= 38
	t2_t41_mem0 += MUL_mem[0]

	t2_t41_mem1 = S.Task('t2_t41_mem1', length=1, delay_cost=1)
	S += t2_t41_mem1 >= 38
	t2_t41_mem1 += ADD_mem[0]

	t001 = S.Task('t001', length=1, delay_cost=1)
	S += t001 >= 39
	t001 += ADD[2]

	t17_t0_t2 = S.Task('t17_t0_t2', length=1, delay_cost=1)
	S += t17_t0_t2 >= 39
	t17_t0_t2 += ADD[1]

	t17_t1_t2_mem0 = S.Task('t17_t1_t2_mem0', length=1, delay_cost=1)
	S += t17_t1_t2_mem0 >= 39
	t17_t1_t2_mem0 += INPUT_mem_r

	t17_t1_t2_mem1 = S.Task('t17_t1_t2_mem1', length=1, delay_cost=1)
	S += t17_t1_t2_mem1 >= 39
	t17_t1_t2_mem1 += INPUT_mem_r

	t2_s00_mem0 = S.Task('t2_s00_mem0', length=1, delay_cost=1)
	S += t2_s00_mem0 >= 39
	t2_s00_mem0 += ADD_mem[3]

	t2_s00_mem1 = S.Task('t2_s00_mem1', length=1, delay_cost=1)
	S += t2_s00_mem1 >= 39
	t2_s00_mem1 += ADD_mem[0]

	t2_s01_mem0 = S.Task('t2_s01_mem0', length=1, delay_cost=1)
	S += t2_s01_mem0 >= 39
	t2_s01_mem0 += ADD_mem[0]

	t2_s01_mem1 = S.Task('t2_s01_mem1', length=1, delay_cost=1)
	S += t2_s01_mem1 >= 39
	t2_s01_mem1 += ADD_mem[3]

	t2_t01_mem0 = S.Task('t2_t01_mem0', length=1, delay_cost=1)
	S += t2_t01_mem0 >= 39
	t2_t01_mem0 += MUL_mem[0]

	t2_t01_mem1 = S.Task('t2_t01_mem1', length=1, delay_cost=1)
	S += t2_t01_mem1 >= 39
	t2_t01_mem1 += ADD_mem[1]

	t2_t41 = S.Task('t2_t41', length=1, delay_cost=1)
	S += t2_t41 >= 39
	t2_t41 += ADD[3]

	t011_mem0 = S.Task('t011_mem0', length=1, delay_cost=1)
	S += t011_mem0 >= 40
	t011_mem0 += ADD_mem[3]

	t011_mem1 = S.Task('t011_mem1', length=1, delay_cost=1)
	S += t011_mem1 >= 40
	t011_mem1 += ADD_mem[1]

	t16_t4_t2_mem0 = S.Task('t16_t4_t2_mem0', length=1, delay_cost=1)
	S += t16_t4_t2_mem0 >= 40
	t16_t4_t2_mem0 += ADD_mem[2]

	t16_t4_t2_mem1 = S.Task('t16_t4_t2_mem1', length=1, delay_cost=1)
	S += t16_t4_t2_mem1 >= 40
	t16_t4_t2_mem1 += ADD_mem[2]

	t17_t1_t2 = S.Task('t17_t1_t2', length=1, delay_cost=1)
	S += t17_t1_t2 >= 40
	t17_t1_t2 += ADD[2]

	t17_t20_mem0 = S.Task('t17_t20_mem0', length=1, delay_cost=1)
	S += t17_t20_mem0 >= 40
	t17_t20_mem0 += INPUT_mem_r

	t17_t20_mem1 = S.Task('t17_t20_mem1', length=1, delay_cost=1)
	S += t17_t20_mem1 >= 40
	t17_t20_mem1 += INPUT_mem_r

	t2_s00 = S.Task('t2_s00', length=1, delay_cost=1)
	S += t2_s00 >= 40
	t2_s00 += ADD[3]

	t2_s01 = S.Task('t2_s01', length=1, delay_cost=1)
	S += t2_s01 >= 40
	t2_s01 += ADD[0]

	t2_t01 = S.Task('t2_t01', length=1, delay_cost=1)
	S += t2_t01 >= 40
	t2_t01 += ADD[1]

	t011 = S.Task('t011', length=1, delay_cost=1)
	S += t011 >= 41
	t011 += ADD[0]

	t16_t4_t2 = S.Task('t16_t4_t2', length=1, delay_cost=1)
	S += t16_t4_t2 >= 41
	t16_t4_t2 += ADD[1]

	t17_t20 = S.Task('t17_t20', length=1, delay_cost=1)
	S += t17_t20 >= 41
	t17_t20 += ADD[2]

	t17_t21_mem0 = S.Task('t17_t21_mem0', length=1, delay_cost=1)
	S += t17_t21_mem0 >= 41
	t17_t21_mem0 += INPUT_mem_r

	t17_t21_mem1 = S.Task('t17_t21_mem1', length=1, delay_cost=1)
	S += t17_t21_mem1 >= 41
	t17_t21_mem1 += INPUT_mem_r

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	S += t200_mem0 >= 41
	t200_mem0 += ADD_mem[3]

	t200_mem1 = S.Task('t200_mem1', length=1, delay_cost=1)
	S += t200_mem1 >= 41
	t200_mem1 += ADD_mem[3]

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	S += t201_mem0 >= 41
	t201_mem0 += ADD_mem[1]

	t201_mem1 = S.Task('t201_mem1', length=1, delay_cost=1)
	S += t201_mem1 >= 41
	t201_mem1 += ADD_mem[0]

	t2_t51_mem0 = S.Task('t2_t51_mem0', length=1, delay_cost=1)
	S += t2_t51_mem0 >= 41
	t2_t51_mem0 += ADD_mem[1]

	t2_t51_mem1 = S.Task('t2_t51_mem1', length=1, delay_cost=1)
	S += t2_t51_mem1 >= 41
	t2_t51_mem1 += ADD_mem[0]

	t17_t21 = S.Task('t17_t21', length=1, delay_cost=1)
	S += t17_t21 >= 42
	t17_t21 += ADD[0]

	t200 = S.Task('t200', length=1, delay_cost=1)
	S += t200 >= 42
	t200 += ADD[2]

	t201 = S.Task('t201', length=1, delay_cost=1)
	S += t201 >= 42
	t201 += ADD[1]

	t2_t51 = S.Task('t2_t51', length=1, delay_cost=1)
	S += t2_t51 >= 42
	t2_t51 += ADD[3]

	t9_t21_mem0 = S.Task('t9_t21_mem0', length=1, delay_cost=1)
	S += t9_t21_mem0 >= 42
	t9_t21_mem0 += INPUT_mem_r

	t9_t21_mem1 = S.Task('t9_t21_mem1', length=1, delay_cost=1)
	S += t9_t21_mem1 >= 42
	t9_t21_mem1 += INPUT_mem_r

	new_TZ_t0_t2_mem0 = S.Task('new_TZ_t0_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_t2_mem0 >= 43
	new_TZ_t0_t2_mem0 += INPUT_mem_r

	new_TZ_t0_t2_mem1 = S.Task('new_TZ_t0_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_t2_mem1 >= 43
	new_TZ_t0_t2_mem1 += INPUT_mem_r

	t17_t4_t2_mem0 = S.Task('t17_t4_t2_mem0', length=1, delay_cost=1)
	S += t17_t4_t2_mem0 >= 43
	t17_t4_t2_mem0 += ADD_mem[2]

	t17_t4_t2_mem1 = S.Task('t17_t4_t2_mem1', length=1, delay_cost=1)
	S += t17_t4_t2_mem1 >= 43
	t17_t4_t2_mem1 += ADD_mem[0]

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	S += t211_mem0 >= 43
	t211_mem0 += ADD_mem[3]

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	S += t211_mem1 >= 43
	t211_mem1 += ADD_mem[3]

	t9_t21 = S.Task('t9_t21', length=1, delay_cost=1)
	S += t9_t21 >= 43
	t9_t21 += ADD[0]

	new_TZ_t0_t2 = S.Task('new_TZ_t0_t2', length=1, delay_cost=1)
	S += new_TZ_t0_t2 >= 44
	new_TZ_t0_t2 += ADD[0]

	t14_t1_t2_mem0 = S.Task('t14_t1_t2_mem0', length=1, delay_cost=1)
	S += t14_t1_t2_mem0 >= 44
	t14_t1_t2_mem0 += INPUT_mem_r

	t14_t1_t2_mem1 = S.Task('t14_t1_t2_mem1', length=1, delay_cost=1)
	S += t14_t1_t2_mem1 >= 44
	t14_t1_t2_mem1 += INPUT_mem_r

	t17_t4_t2 = S.Task('t17_t4_t2', length=1, delay_cost=1)
	S += t17_t4_t2 >= 44
	t17_t4_t2 += ADD[1]

	t211 = S.Task('t211', length=1, delay_cost=1)
	S += t211 >= 44
	t211 += ADD[3]

	t9_t4_t2_mem0 = S.Task('t9_t4_t2_mem0', length=1, delay_cost=1)
	S += t9_t4_t2_mem0 >= 44
	t9_t4_t2_mem0 += ADD_mem[2]

	t9_t4_t2_mem1 = S.Task('t9_t4_t2_mem1', length=1, delay_cost=1)
	S += t9_t4_t2_mem1 >= 44
	t9_t4_t2_mem1 += ADD_mem[0]

	t14_t0_t2_mem0 = S.Task('t14_t0_t2_mem0', length=1, delay_cost=1)
	S += t14_t0_t2_mem0 >= 45
	t14_t0_t2_mem0 += INPUT_mem_r

	t14_t0_t2_mem1 = S.Task('t14_t0_t2_mem1', length=1, delay_cost=1)
	S += t14_t0_t2_mem1 >= 45
	t14_t0_t2_mem1 += INPUT_mem_r

	t14_t1_t2 = S.Task('t14_t1_t2', length=1, delay_cost=1)
	S += t14_t1_t2 >= 45
	t14_t1_t2 += ADD[0]

	t9_t4_t2 = S.Task('t9_t4_t2', length=1, delay_cost=1)
	S += t9_t4_t2 >= 45
	t9_t4_t2 += ADD[1]

	t14_t0_t2 = S.Task('t14_t0_t2', length=1, delay_cost=1)
	S += t14_t0_t2 >= 46
	t14_t0_t2 += ADD[1]

	t14_t20_mem0 = S.Task('t14_t20_mem0', length=1, delay_cost=1)
	S += t14_t20_mem0 >= 46
	t14_t20_mem0 += INPUT_mem_r

	t14_t20_mem1 = S.Task('t14_t20_mem1', length=1, delay_cost=1)
	S += t14_t20_mem1 >= 46
	t14_t20_mem1 += INPUT_mem_r

	t14_t20 = S.Task('t14_t20', length=1, delay_cost=1)
	S += t14_t20 >= 47
	t14_t20 += ADD[1]

	t14_t21_mem0 = S.Task('t14_t21_mem0', length=1, delay_cost=1)
	S += t14_t21_mem0 >= 47
	t14_t21_mem0 += INPUT_mem_r

	t14_t21_mem1 = S.Task('t14_t21_mem1', length=1, delay_cost=1)
	S += t14_t21_mem1 >= 47
	t14_t21_mem1 += INPUT_mem_r

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 48
	t110_mem0 += INPUT_mem_r

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 48
	t110_mem1 += ADD_mem[0]

	t14_t21 = S.Task('t14_t21', length=1, delay_cost=1)
	S += t14_t21 >= 48
	t14_t21 += ADD[2]

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	S += t300_mem0 >= 48
	t300_mem0 += INPUT_mem_r

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	S += t300_mem1 >= 48
	t300_mem1 += ADD_mem[2]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 49
	t101_mem0 += INPUT_mem_r

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 49
	t101_mem1 += ADD_mem[2]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 49
	t110 += ADD[2]

	t14_t4_t2_mem0 = S.Task('t14_t4_t2_mem0', length=1, delay_cost=1)
	S += t14_t4_t2_mem0 >= 49
	t14_t4_t2_mem0 += ADD_mem[1]

	t14_t4_t2_mem1 = S.Task('t14_t4_t2_mem1', length=1, delay_cost=1)
	S += t14_t4_t2_mem1 >= 49
	t14_t4_t2_mem1 += ADD_mem[2]

	t300 = S.Task('t300', length=1, delay_cost=1)
	S += t300 >= 49
	t300 += ADD[0]

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	S += t310_mem0 >= 49
	t310_mem0 += INPUT_mem_r

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	S += t310_mem1 >= 49
	t310_mem1 += ADD_mem[1]

	c1010_in = S.Task('c1010_in', length=1, delay_cost=1)
	S += c1010_in >= 50
	c1010_in += MUL_in[0]

	c1010_mem0 = S.Task('c1010_mem0', length=1, delay_cost=1)
	S += c1010_mem0 >= 50
	c1010_mem0 += ADD_mem[2]

	c1010_mem1 = S.Task('c1010_mem1', length=1, delay_cost=1)
	S += c1010_mem1 >= 50
	c1010_mem1 += INPUT_mem_r

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 50
	t101 += ADD[2]

	t14_t4_t2 = S.Task('t14_t4_t2', length=1, delay_cost=1)
	S += t14_t4_t2 >= 50
	t14_t4_t2 += ADD[0]

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	S += t301_mem0 >= 50
	t301_mem0 += INPUT_mem_r

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	S += t301_mem1 >= 50
	t301_mem1 += ADD_mem[1]

	t310 = S.Task('t310', length=1, delay_cost=1)
	S += t310 >= 50
	t310 += ADD[3]

	c0010_in = S.Task('c0010_in', length=1, delay_cost=1)
	S += c0010_in >= 51
	c0010_in += MUL_in[0]

	c0010_mem0 = S.Task('c0010_mem0', length=1, delay_cost=1)
	S += c0010_mem0 >= 51
	c0010_mem0 += ADD_mem[3]

	c0010_mem1 = S.Task('c0010_mem1', length=1, delay_cost=1)
	S += c0010_mem1 >= 51
	c0010_mem1 += INPUT_mem_r

	c1010 = S.Task('c1010', length=7, delay_cost=1)
	S += c1010 >= 51
	c1010 += MUL[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 51
	t100_mem0 += INPUT_mem_r

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 51
	t100_mem1 += ADD_mem[3]

	t301 = S.Task('t301', length=1, delay_cost=1)
	S += t301 >= 51
	t301 += ADD[0]

	c0010 = S.Task('c0010', length=7, delay_cost=1)
	S += c0010 >= 52
	c0010 += MUL[0]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 52
	t100 += ADD[3]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 52
	t111_mem0 += INPUT_mem_r

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 52
	t111_mem1 += ADD_mem[0]

	t16_t1_t0_in = S.Task('t16_t1_t0_in', length=1, delay_cost=1)
	S += t16_t1_t0_in >= 52
	t16_t1_t0_in += MUL_in[0]

	t16_t1_t0_mem0 = S.Task('t16_t1_t0_mem0', length=1, delay_cost=1)
	S += t16_t1_t0_mem0 >= 52
	t16_t1_t0_mem0 += INPUT_mem_r

	t16_t1_t0_mem1 = S.Task('t16_t1_t0_mem1', length=1, delay_cost=1)
	S += t16_t1_t0_mem1 >= 52
	t16_t1_t0_mem1 += ADD_mem[3]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 53
	t111 += ADD[3]

	t16_t1_t0 = S.Task('t16_t1_t0', length=7, delay_cost=1)
	S += t16_t1_t0 >= 53
	t16_t1_t0 += MUL[0]

	t17_t1_t0_in = S.Task('t17_t1_t0_in', length=1, delay_cost=1)
	S += t17_t1_t0_in >= 53
	t17_t1_t0_in += MUL_in[0]

	t17_t1_t0_mem0 = S.Task('t17_t1_t0_mem0', length=1, delay_cost=1)
	S += t17_t1_t0_mem0 >= 53
	t17_t1_t0_mem0 += INPUT_mem_r

	t17_t1_t0_mem1 = S.Task('t17_t1_t0_mem1', length=1, delay_cost=1)
	S += t17_t1_t0_mem1 >= 53
	t17_t1_t0_mem1 += ADD_mem[2]

	t311_mem0 = S.Task('t311_mem0', length=1, delay_cost=1)
	S += t311_mem0 >= 53
	t311_mem0 += INPUT_mem_r

	t311_mem1 = S.Task('t311_mem1', length=1, delay_cost=1)
	S += t311_mem1 >= 53
	t311_mem1 += ADD_mem[3]

	t17_t1_t0 = S.Task('t17_t1_t0', length=7, delay_cost=1)
	S += t17_t1_t0 >= 54
	t17_t1_t0 += MUL[0]

	t311 = S.Task('t311', length=1, delay_cost=1)
	S += t311 >= 54
	t311 += ADD[3]

	c1010_w = S.Task('c1010_w', length=1, delay_cost=1)
	S += c1010_w >= 58
	c1010_w += INPUT_mem_w

	c0010_w = S.Task('c0010_w', length=1, delay_cost=1)
	S += c0010_w >= 59
	c0010_w += INPUT_mem_w


	# new tasks
	t4_a1_0 = S.Task('t4_a1_0', length=1, delay_cost=1)
	t4_a1_0 += alt(ADD)

	t4_a1_0_mem0 = S.Task('t4_a1_0_mem0', length=1, delay_cost=1)
	t4_a1_0_mem0 += ADD_mem[2]
	S += 50 < t4_a1_0_mem0
	S += t4_a1_0_mem0 <= t4_a1_0

	t4_a1_0_mem1 = S.Task('t4_a1_0_mem1', length=1, delay_cost=1)
	t4_a1_0_mem1 += ADD_mem[3]
	S += 54 < t4_a1_0_mem1
	S += t4_a1_0_mem1 <= t4_a1_0

	t4_a1_1 = S.Task('t4_a1_1', length=1, delay_cost=1)
	t4_a1_1 += alt(ADD)

	t4_a1_1_mem0 = S.Task('t4_a1_1_mem0', length=1, delay_cost=1)
	t4_a1_1_mem0 += ADD_mem[3]
	S += 54 < t4_a1_1_mem0
	S += t4_a1_1_mem0 <= t4_a1_1

	t4_a1_1_mem1 = S.Task('t4_a1_1_mem1', length=1, delay_cost=1)
	t4_a1_1_mem1 += ADD_mem[2]
	S += 50 < t4_a1_1_mem1
	S += t4_a1_1_mem1 <= t4_a1_1

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	t4_t10 += alt(ADD)

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	t4_t10_mem0 += ADD_mem[3]
	S += 53 < t4_t10_mem0
	S += t4_t10_mem0 <= t4_t10

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	t4_t10_mem1 += ADD_mem[2]
	S += 50 < t4_t10_mem1
	S += t4_t10_mem1 <= t4_t10

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	t4_t11 += alt(ADD)

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	t4_t11_mem0 += ADD_mem[2]
	S += 51 < t4_t11_mem0
	S += t4_t11_mem0 <= t4_t11

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	t4_t11_mem1 += ADD_mem[3]
	S += 54 < t4_t11_mem1
	S += t4_t11_mem1 <= t4_t11

	t4_t3_t0_in = S.Task('t4_t3_t0_in', length=1, delay_cost=1)
	t4_t3_t0_in += alt(MUL_in)
	t4_t3_t0 = S.Task('t4_t3_t0', length=7, delay_cost=1)
	t4_t3_t0 += alt(MUL)
	S += t4_t3_t0>=t4_t3_t0_in

	t4_t3_t0_mem0 = S.Task('t4_t3_t0_mem0', length=1, delay_cost=1)
	t4_t3_t0_mem0 += ADD_mem[3]
	S += 53 < t4_t3_t0_mem0
	S += t4_t3_t0_mem0 <= t4_t3_t0

	t4_t3_t0_mem1 = S.Task('t4_t3_t0_mem1', length=1, delay_cost=1)
	t4_t3_t0_mem1 += ADD_mem[2]
	S += 50 < t4_t3_t0_mem1
	S += t4_t3_t0_mem1 <= t4_t3_t0

	t4_t3_t1_in = S.Task('t4_t3_t1_in', length=1, delay_cost=1)
	t4_t3_t1_in += alt(MUL_in)
	t4_t3_t1 = S.Task('t4_t3_t1', length=7, delay_cost=1)
	t4_t3_t1 += alt(MUL)
	S += t4_t3_t1>=t4_t3_t1_in

	t4_t3_t1_mem0 = S.Task('t4_t3_t1_mem0', length=1, delay_cost=1)
	t4_t3_t1_mem0 += ADD_mem[2]
	S += 51 < t4_t3_t1_mem0
	S += t4_t3_t1_mem0 <= t4_t3_t1

	t4_t3_t1_mem1 = S.Task('t4_t3_t1_mem1', length=1, delay_cost=1)
	t4_t3_t1_mem1 += ADD_mem[3]
	S += 54 < t4_t3_t1_mem1
	S += t4_t3_t1_mem1 <= t4_t3_t1

	t4_t3_t2 = S.Task('t4_t3_t2', length=1, delay_cost=1)
	t4_t3_t2 += alt(ADD)

	t4_t3_t2_mem0 = S.Task('t4_t3_t2_mem0', length=1, delay_cost=1)
	t4_t3_t2_mem0 += ADD_mem[3]
	S += 53 < t4_t3_t2_mem0
	S += t4_t3_t2_mem0 <= t4_t3_t2

	t4_t3_t2_mem1 = S.Task('t4_t3_t2_mem1', length=1, delay_cost=1)
	t4_t3_t2_mem1 += ADD_mem[2]
	S += 51 < t4_t3_t2_mem1
	S += t4_t3_t2_mem1 <= t4_t3_t2

	t4_t3_t3 = S.Task('t4_t3_t3', length=1, delay_cost=1)
	t4_t3_t3 += alt(ADD)

	t4_t3_t3_mem0 = S.Task('t4_t3_t3_mem0', length=1, delay_cost=1)
	t4_t3_t3_mem0 += ADD_mem[2]
	S += 50 < t4_t3_t3_mem0
	S += t4_t3_t3_mem0 <= t4_t3_t3

	t4_t3_t3_mem1 = S.Task('t4_t3_t3_mem1', length=1, delay_cost=1)
	t4_t3_t3_mem1 += ADD_mem[3]
	S += 54 < t4_t3_t3_mem1
	S += t4_t3_t3_mem1 <= t4_t3_t3

	t5_a1_0 = S.Task('t5_a1_0', length=1, delay_cost=1)
	t5_a1_0 += alt(ADD)

	t5_a1_0_mem0 = S.Task('t5_a1_0_mem0', length=1, delay_cost=1)
	t5_a1_0_mem0 += ADD_mem[3]
	S += 51 < t5_a1_0_mem0
	S += t5_a1_0_mem0 <= t5_a1_0

	t5_a1_0_mem1 = S.Task('t5_a1_0_mem1', length=1, delay_cost=1)
	t5_a1_0_mem1 += ADD_mem[3]
	S += 55 < t5_a1_0_mem1
	S += t5_a1_0_mem1 <= t5_a1_0

	t5_a1_1 = S.Task('t5_a1_1', length=1, delay_cost=1)
	t5_a1_1 += alt(ADD)

	t5_a1_1_mem0 = S.Task('t5_a1_1_mem0', length=1, delay_cost=1)
	t5_a1_1_mem0 += ADD_mem[3]
	S += 55 < t5_a1_1_mem0
	S += t5_a1_1_mem0 <= t5_a1_1

	t5_a1_1_mem1 = S.Task('t5_a1_1_mem1', length=1, delay_cost=1)
	t5_a1_1_mem1 += ADD_mem[3]
	S += 51 < t5_a1_1_mem1
	S += t5_a1_1_mem1 <= t5_a1_1

	t5_t10 = S.Task('t5_t10', length=1, delay_cost=1)
	t5_t10 += alt(ADD)

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	t5_t10_mem0 += ADD_mem[0]
	S += 50 < t5_t10_mem0
	S += t5_t10_mem0 <= t5_t10

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	t5_t10_mem1 += ADD_mem[3]
	S += 51 < t5_t10_mem1
	S += t5_t10_mem1 <= t5_t10

	t5_t11 = S.Task('t5_t11', length=1, delay_cost=1)
	t5_t11 += alt(ADD)

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	t5_t11_mem0 += ADD_mem[0]
	S += 52 < t5_t11_mem0
	S += t5_t11_mem0 <= t5_t11

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	t5_t11_mem1 += ADD_mem[3]
	S += 55 < t5_t11_mem1
	S += t5_t11_mem1 <= t5_t11

	t5_t3_t0_in = S.Task('t5_t3_t0_in', length=1, delay_cost=1)
	t5_t3_t0_in += alt(MUL_in)
	t5_t3_t0 = S.Task('t5_t3_t0', length=7, delay_cost=1)
	t5_t3_t0 += alt(MUL)
	S += t5_t3_t0>=t5_t3_t0_in

	t5_t3_t0_mem0 = S.Task('t5_t3_t0_mem0', length=1, delay_cost=1)
	t5_t3_t0_mem0 += ADD_mem[0]
	S += 50 < t5_t3_t0_mem0
	S += t5_t3_t0_mem0 <= t5_t3_t0

	t5_t3_t0_mem1 = S.Task('t5_t3_t0_mem1', length=1, delay_cost=1)
	t5_t3_t0_mem1 += ADD_mem[3]
	S += 51 < t5_t3_t0_mem1
	S += t5_t3_t0_mem1 <= t5_t3_t0

	t5_t3_t1_in = S.Task('t5_t3_t1_in', length=1, delay_cost=1)
	t5_t3_t1_in += alt(MUL_in)
	t5_t3_t1 = S.Task('t5_t3_t1', length=7, delay_cost=1)
	t5_t3_t1 += alt(MUL)
	S += t5_t3_t1>=t5_t3_t1_in

	t5_t3_t1_mem0 = S.Task('t5_t3_t1_mem0', length=1, delay_cost=1)
	t5_t3_t1_mem0 += ADD_mem[0]
	S += 52 < t5_t3_t1_mem0
	S += t5_t3_t1_mem0 <= t5_t3_t1

	t5_t3_t1_mem1 = S.Task('t5_t3_t1_mem1', length=1, delay_cost=1)
	t5_t3_t1_mem1 += ADD_mem[3]
	S += 55 < t5_t3_t1_mem1
	S += t5_t3_t1_mem1 <= t5_t3_t1

	t5_t3_t2 = S.Task('t5_t3_t2', length=1, delay_cost=1)
	t5_t3_t2 += alt(ADD)

	t5_t3_t2_mem0 = S.Task('t5_t3_t2_mem0', length=1, delay_cost=1)
	t5_t3_t2_mem0 += ADD_mem[0]
	S += 50 < t5_t3_t2_mem0
	S += t5_t3_t2_mem0 <= t5_t3_t2

	t5_t3_t2_mem1 = S.Task('t5_t3_t2_mem1', length=1, delay_cost=1)
	t5_t3_t2_mem1 += ADD_mem[0]
	S += 52 < t5_t3_t2_mem1
	S += t5_t3_t2_mem1 <= t5_t3_t2

	t5_t3_t3 = S.Task('t5_t3_t3', length=1, delay_cost=1)
	t5_t3_t3 += alt(ADD)

	t5_t3_t3_mem0 = S.Task('t5_t3_t3_mem0', length=1, delay_cost=1)
	t5_t3_t3_mem0 += ADD_mem[3]
	S += 51 < t5_t3_t3_mem0
	S += t5_t3_t3_mem0 <= t5_t3_t3

	t5_t3_t3_mem1 = S.Task('t5_t3_t3_mem1', length=1, delay_cost=1)
	t5_t3_t3_mem1 += ADD_mem[3]
	S += 55 < t5_t3_t3_mem1
	S += t5_t3_t3_mem1 <= t5_t3_t3

	t6_t0_t2 = S.Task('t6_t0_t2', length=1, delay_cost=1)
	t6_t0_t2 += alt(ADD)

	t6_t0_t2_mem0 = S.Task('t6_t0_t2_mem0', length=1, delay_cost=1)
	t6_t0_t2_mem0 += ADD_mem[0]
	S += 50 < t6_t0_t2_mem0
	S += t6_t0_t2_mem0 <= t6_t0_t2

	t6_t0_t2_mem1 = S.Task('t6_t0_t2_mem1', length=1, delay_cost=1)
	t6_t0_t2_mem1 += ADD_mem[0]
	S += 52 < t6_t0_t2_mem1
	S += t6_t0_t2_mem1 <= t6_t0_t2

	t6_t1_t2 = S.Task('t6_t1_t2', length=1, delay_cost=1)
	t6_t1_t2 += alt(ADD)

	t6_t1_t2_mem0 = S.Task('t6_t1_t2_mem0', length=1, delay_cost=1)
	t6_t1_t2_mem0 += ADD_mem[3]
	S += 51 < t6_t1_t2_mem0
	S += t6_t1_t2_mem0 <= t6_t1_t2

	t6_t1_t2_mem1 = S.Task('t6_t1_t2_mem1', length=1, delay_cost=1)
	t6_t1_t2_mem1 += ADD_mem[3]
	S += 55 < t6_t1_t2_mem1
	S += t6_t1_t2_mem1 <= t6_t1_t2

	t6_t20 = S.Task('t6_t20', length=1, delay_cost=1)
	t6_t20 += alt(ADD)

	t6_t20_mem0 = S.Task('t6_t20_mem0', length=1, delay_cost=1)
	t6_t20_mem0 += ADD_mem[0]
	S += 50 < t6_t20_mem0
	S += t6_t20_mem0 <= t6_t20

	t6_t20_mem1 = S.Task('t6_t20_mem1', length=1, delay_cost=1)
	t6_t20_mem1 += ADD_mem[3]
	S += 51 < t6_t20_mem1
	S += t6_t20_mem1 <= t6_t20

	t6_t21 = S.Task('t6_t21', length=1, delay_cost=1)
	t6_t21 += alt(ADD)

	t6_t21_mem0 = S.Task('t6_t21_mem0', length=1, delay_cost=1)
	t6_t21_mem0 += ADD_mem[0]
	S += 52 < t6_t21_mem0
	S += t6_t21_mem0 <= t6_t21

	t6_t21_mem1 = S.Task('t6_t21_mem1', length=1, delay_cost=1)
	t6_t21_mem1 += ADD_mem[3]
	S += 55 < t6_t21_mem1
	S += t6_t21_mem1 <= t6_t21

	new_TX_t0_t2 = S.Task('new_TX_t0_t2', length=1, delay_cost=1)
	new_TX_t0_t2 += alt(ADD)

	new_TX_t0_t2_mem0 = S.Task('new_TX_t0_t2_mem0', length=1, delay_cost=1)
	new_TX_t0_t2_mem0 += ADD_mem[0]
	S += 50 < new_TX_t0_t2_mem0
	S += new_TX_t0_t2_mem0 <= new_TX_t0_t2

	new_TX_t0_t2_mem1 = S.Task('new_TX_t0_t2_mem1', length=1, delay_cost=1)
	new_TX_t0_t2_mem1 += ADD_mem[0]
	S += 52 < new_TX_t0_t2_mem1
	S += new_TX_t0_t2_mem1 <= new_TX_t0_t2

	new_TX_t1_t2 = S.Task('new_TX_t1_t2', length=1, delay_cost=1)
	new_TX_t1_t2 += alt(ADD)

	new_TX_t1_t2_mem0 = S.Task('new_TX_t1_t2_mem0', length=1, delay_cost=1)
	new_TX_t1_t2_mem0 += ADD_mem[3]
	S += 51 < new_TX_t1_t2_mem0
	S += new_TX_t1_t2_mem0 <= new_TX_t1_t2

	new_TX_t1_t2_mem1 = S.Task('new_TX_t1_t2_mem1', length=1, delay_cost=1)
	new_TX_t1_t2_mem1 += ADD_mem[3]
	S += 55 < new_TX_t1_t2_mem1
	S += new_TX_t1_t2_mem1 <= new_TX_t1_t2

	new_TX_t20 = S.Task('new_TX_t20', length=1, delay_cost=1)
	new_TX_t20 += alt(ADD)

	new_TX_t20_mem0 = S.Task('new_TX_t20_mem0', length=1, delay_cost=1)
	new_TX_t20_mem0 += ADD_mem[0]
	S += 50 < new_TX_t20_mem0
	S += new_TX_t20_mem0 <= new_TX_t20

	new_TX_t20_mem1 = S.Task('new_TX_t20_mem1', length=1, delay_cost=1)
	new_TX_t20_mem1 += ADD_mem[3]
	S += 51 < new_TX_t20_mem1
	S += new_TX_t20_mem1 <= new_TX_t20

	new_TX_t21 = S.Task('new_TX_t21', length=1, delay_cost=1)
	new_TX_t21 += alt(ADD)

	new_TX_t21_mem0 = S.Task('new_TX_t21_mem0', length=1, delay_cost=1)
	new_TX_t21_mem0 += ADD_mem[0]
	S += 52 < new_TX_t21_mem0
	S += new_TX_t21_mem0 <= new_TX_t21

	new_TX_t21_mem1 = S.Task('new_TX_t21_mem1', length=1, delay_cost=1)
	new_TX_t21_mem1 += ADD_mem[3]
	S += 55 < new_TX_t21_mem1
	S += new_TX_t21_mem1 <= new_TX_t21

	t13_t0_t2 = S.Task('t13_t0_t2', length=1, delay_cost=1)
	t13_t0_t2 += alt(ADD)

	t13_t0_t2_mem0 = S.Task('t13_t0_t2_mem0', length=1, delay_cost=1)
	t13_t0_t2_mem0 += ADD_mem[3]
	S += 53 < t13_t0_t2_mem0
	S += t13_t0_t2_mem0 <= t13_t0_t2

	t13_t0_t2_mem1 = S.Task('t13_t0_t2_mem1', length=1, delay_cost=1)
	t13_t0_t2_mem1 += ADD_mem[2]
	S += 51 < t13_t0_t2_mem1
	S += t13_t0_t2_mem1 <= t13_t0_t2

	t13_t1_t2 = S.Task('t13_t1_t2', length=1, delay_cost=1)
	t13_t1_t2 += alt(ADD)

	t13_t1_t2_mem0 = S.Task('t13_t1_t2_mem0', length=1, delay_cost=1)
	t13_t1_t2_mem0 += ADD_mem[2]
	S += 50 < t13_t1_t2_mem0
	S += t13_t1_t2_mem0 <= t13_t1_t2

	t13_t1_t2_mem1 = S.Task('t13_t1_t2_mem1', length=1, delay_cost=1)
	t13_t1_t2_mem1 += ADD_mem[3]
	S += 54 < t13_t1_t2_mem1
	S += t13_t1_t2_mem1 <= t13_t1_t2

	t13_t20 = S.Task('t13_t20', length=1, delay_cost=1)
	t13_t20 += alt(ADD)

	t13_t20_mem0 = S.Task('t13_t20_mem0', length=1, delay_cost=1)
	t13_t20_mem0 += ADD_mem[3]
	S += 53 < t13_t20_mem0
	S += t13_t20_mem0 <= t13_t20

	t13_t20_mem1 = S.Task('t13_t20_mem1', length=1, delay_cost=1)
	t13_t20_mem1 += ADD_mem[2]
	S += 50 < t13_t20_mem1
	S += t13_t20_mem1 <= t13_t20

	t13_t21 = S.Task('t13_t21', length=1, delay_cost=1)
	t13_t21 += alt(ADD)

	t13_t21_mem0 = S.Task('t13_t21_mem0', length=1, delay_cost=1)
	t13_t21_mem0 += ADD_mem[2]
	S += 51 < t13_t21_mem0
	S += t13_t21_mem0 <= t13_t21

	t13_t21_mem1 = S.Task('t13_t21_mem1', length=1, delay_cost=1)
	t13_t21_mem1 += ADD_mem[3]
	S += 54 < t13_t21_mem1
	S += t13_t21_mem1 <= t13_t21

	c0000_in = S.Task('c0000_in', length=1, delay_cost=1)
	c0000_in += alt(MUL_in)
	c0000 = S.Task('c0000', length=7, delay_cost=1)
	c0000 += alt(MUL)
	S += c0000>=c0000_in

	S += 0<c0000

	c0000_mem0 = S.Task('c0000_mem0', length=1, delay_cost=1)
	c0000_mem0 += ADD_mem[0]
	S += 50 < c0000_mem0
	S += c0000_mem0 <= c0000

	c0000_mem1 = S.Task('c0000_mem1', length=1, delay_cost=1)
	c0000_mem1 += INPUT_mem_r
	S += c0000_mem1 <= c0000

	c0000_w = S.Task('c0000_w', length=1, delay_cost=1)
	c0000_w += alt(INPUT_mem_w)
	S += c0000 <= c0000_w

	c0001_in = S.Task('c0001_in', length=1, delay_cost=1)
	c0001_in += alt(MUL_in)
	c0001 = S.Task('c0001', length=7, delay_cost=1)
	c0001 += alt(MUL)
	S += c0001>=c0001_in

	S += 0<c0001

	c0001_mem0 = S.Task('c0001_mem0', length=1, delay_cost=1)
	c0001_mem0 += ADD_mem[0]
	S += 52 < c0001_mem0
	S += c0001_mem0 <= c0001

	c0001_mem1 = S.Task('c0001_mem1', length=1, delay_cost=1)
	c0001_mem1 += INPUT_mem_r
	S += c0001_mem1 <= c0001

	c0001_w = S.Task('c0001_w', length=1, delay_cost=1)
	c0001_w += alt(INPUT_mem_w)
	S += c0001 <= c0001_w

	c0011_in = S.Task('c0011_in', length=1, delay_cost=1)
	c0011_in += alt(MUL_in)
	c0011 = S.Task('c0011', length=7, delay_cost=1)
	c0011 += alt(MUL)
	S += c0011>=c0011_in

	S += 0<c0011

	c0011_mem0 = S.Task('c0011_mem0', length=1, delay_cost=1)
	c0011_mem0 += ADD_mem[3]
	S += 55 < c0011_mem0
	S += c0011_mem0 <= c0011

	c0011_mem1 = S.Task('c0011_mem1', length=1, delay_cost=1)
	c0011_mem1 += INPUT_mem_r
	S += c0011_mem1 <= c0011

	c0011_w = S.Task('c0011_w', length=1, delay_cost=1)
	c0011_w += alt(INPUT_mem_w)
	S += c0011 <= c0011_w

	c1000_in = S.Task('c1000_in', length=1, delay_cost=1)
	c1000_in += alt(MUL_in)
	c1000 = S.Task('c1000', length=7, delay_cost=1)
	c1000 += alt(MUL)
	S += c1000>=c1000_in

	S += 0<c1000

	c1000_mem0 = S.Task('c1000_mem0', length=1, delay_cost=1)
	c1000_mem0 += ADD_mem[3]
	S += 53 < c1000_mem0
	S += c1000_mem0 <= c1000

	c1000_mem1 = S.Task('c1000_mem1', length=1, delay_cost=1)
	c1000_mem1 += INPUT_mem_r
	S += c1000_mem1 <= c1000

	c1000_w = S.Task('c1000_w', length=1, delay_cost=1)
	c1000_w += alt(INPUT_mem_w)
	S += c1000 <= c1000_w

	c1001_in = S.Task('c1001_in', length=1, delay_cost=1)
	c1001_in += alt(MUL_in)
	c1001 = S.Task('c1001', length=7, delay_cost=1)
	c1001 += alt(MUL)
	S += c1001>=c1001_in

	S += 0<c1001

	c1001_mem0 = S.Task('c1001_mem0', length=1, delay_cost=1)
	c1001_mem0 += ADD_mem[2]
	S += 51 < c1001_mem0
	S += c1001_mem0 <= c1001

	c1001_mem1 = S.Task('c1001_mem1', length=1, delay_cost=1)
	c1001_mem1 += INPUT_mem_r
	S += c1001_mem1 <= c1001

	c1001_w = S.Task('c1001_w', length=1, delay_cost=1)
	c1001_w += alt(INPUT_mem_w)
	S += c1001 <= c1001_w

	c1011_in = S.Task('c1011_in', length=1, delay_cost=1)
	c1011_in += alt(MUL_in)
	c1011 = S.Task('c1011', length=7, delay_cost=1)
	c1011 += alt(MUL)
	S += c1011>=c1011_in

	S += 0<c1011

	c1011_mem0 = S.Task('c1011_mem0', length=1, delay_cost=1)
	c1011_mem0 += ADD_mem[3]
	S += 54 < c1011_mem0
	S += c1011_mem0 <= c1011

	c1011_mem1 = S.Task('c1011_mem1', length=1, delay_cost=1)
	c1011_mem1 += INPUT_mem_r
	S += c1011_mem1 <= c1011

	c1011_w = S.Task('c1011_w', length=1, delay_cost=1)
	c1011_w += alt(INPUT_mem_w)
	S += c1011 <= c1011_w

	t16_t0_t0_in = S.Task('t16_t0_t0_in', length=1, delay_cost=1)
	t16_t0_t0_in += alt(MUL_in)
	t16_t0_t0 = S.Task('t16_t0_t0', length=7, delay_cost=1)
	t16_t0_t0 += alt(MUL)
	S += t16_t0_t0>=t16_t0_t0_in

	t16_t0_t0_mem0 = S.Task('t16_t0_t0_mem0', length=1, delay_cost=1)
	t16_t0_t0_mem0 += INPUT_mem_r
	S += t16_t0_t0_mem0 <= t16_t0_t0

	t16_t0_t0_mem1 = S.Task('t16_t0_t0_mem1', length=1, delay_cost=1)
	t16_t0_t0_mem1 += ADD_mem[0]
	S += 50 < t16_t0_t0_mem1
	S += t16_t0_t0_mem1 <= t16_t0_t0

	t16_t0_t1_in = S.Task('t16_t0_t1_in', length=1, delay_cost=1)
	t16_t0_t1_in += alt(MUL_in)
	t16_t0_t1 = S.Task('t16_t0_t1', length=7, delay_cost=1)
	t16_t0_t1 += alt(MUL)
	S += t16_t0_t1>=t16_t0_t1_in

	t16_t0_t1_mem0 = S.Task('t16_t0_t1_mem0', length=1, delay_cost=1)
	t16_t0_t1_mem0 += INPUT_mem_r
	S += t16_t0_t1_mem0 <= t16_t0_t1

	t16_t0_t1_mem1 = S.Task('t16_t0_t1_mem1', length=1, delay_cost=1)
	t16_t0_t1_mem1 += ADD_mem[0]
	S += 52 < t16_t0_t1_mem1
	S += t16_t0_t1_mem1 <= t16_t0_t1

	t16_t0_t3 = S.Task('t16_t0_t3', length=1, delay_cost=1)
	t16_t0_t3 += alt(ADD)

	t16_t0_t3_mem0 = S.Task('t16_t0_t3_mem0', length=1, delay_cost=1)
	t16_t0_t3_mem0 += ADD_mem[0]
	S += 50 < t16_t0_t3_mem0
	S += t16_t0_t3_mem0 <= t16_t0_t3

	t16_t0_t3_mem1 = S.Task('t16_t0_t3_mem1', length=1, delay_cost=1)
	t16_t0_t3_mem1 += ADD_mem[0]
	S += 52 < t16_t0_t3_mem1
	S += t16_t0_t3_mem1 <= t16_t0_t3

	t16_t1_t1_in = S.Task('t16_t1_t1_in', length=1, delay_cost=1)
	t16_t1_t1_in += alt(MUL_in)
	t16_t1_t1 = S.Task('t16_t1_t1', length=7, delay_cost=1)
	t16_t1_t1 += alt(MUL)
	S += t16_t1_t1>=t16_t1_t1_in

	t16_t1_t1_mem0 = S.Task('t16_t1_t1_mem0', length=1, delay_cost=1)
	t16_t1_t1_mem0 += INPUT_mem_r
	S += t16_t1_t1_mem0 <= t16_t1_t1

	t16_t1_t1_mem1 = S.Task('t16_t1_t1_mem1', length=1, delay_cost=1)
	t16_t1_t1_mem1 += ADD_mem[3]
	S += 55 < t16_t1_t1_mem1
	S += t16_t1_t1_mem1 <= t16_t1_t1

	t16_t1_t3 = S.Task('t16_t1_t3', length=1, delay_cost=1)
	t16_t1_t3 += alt(ADD)

	t16_t1_t3_mem0 = S.Task('t16_t1_t3_mem0', length=1, delay_cost=1)
	t16_t1_t3_mem0 += ADD_mem[3]
	S += 51 < t16_t1_t3_mem0
	S += t16_t1_t3_mem0 <= t16_t1_t3

	t16_t1_t3_mem1 = S.Task('t16_t1_t3_mem1', length=1, delay_cost=1)
	t16_t1_t3_mem1 += ADD_mem[3]
	S += 55 < t16_t1_t3_mem1
	S += t16_t1_t3_mem1 <= t16_t1_t3

	t16_t30 = S.Task('t16_t30', length=1, delay_cost=1)
	t16_t30 += alt(ADD)

	t16_t30_mem0 = S.Task('t16_t30_mem0', length=1, delay_cost=1)
	t16_t30_mem0 += ADD_mem[0]
	S += 50 < t16_t30_mem0
	S += t16_t30_mem0 <= t16_t30

	t16_t30_mem1 = S.Task('t16_t30_mem1', length=1, delay_cost=1)
	t16_t30_mem1 += ADD_mem[3]
	S += 51 < t16_t30_mem1
	S += t16_t30_mem1 <= t16_t30

	t16_t31 = S.Task('t16_t31', length=1, delay_cost=1)
	t16_t31 += alt(ADD)

	t16_t31_mem0 = S.Task('t16_t31_mem0', length=1, delay_cost=1)
	t16_t31_mem0 += ADD_mem[0]
	S += 52 < t16_t31_mem0
	S += t16_t31_mem0 <= t16_t31

	t16_t31_mem1 = S.Task('t16_t31_mem1', length=1, delay_cost=1)
	t16_t31_mem1 += ADD_mem[3]
	S += 55 < t16_t31_mem1
	S += t16_t31_mem1 <= t16_t31

	t17_t0_t0_in = S.Task('t17_t0_t0_in', length=1, delay_cost=1)
	t17_t0_t0_in += alt(MUL_in)
	t17_t0_t0 = S.Task('t17_t0_t0', length=7, delay_cost=1)
	t17_t0_t0 += alt(MUL)
	S += t17_t0_t0>=t17_t0_t0_in

	t17_t0_t0_mem0 = S.Task('t17_t0_t0_mem0', length=1, delay_cost=1)
	t17_t0_t0_mem0 += INPUT_mem_r
	S += t17_t0_t0_mem0 <= t17_t0_t0

	t17_t0_t0_mem1 = S.Task('t17_t0_t0_mem1', length=1, delay_cost=1)
	t17_t0_t0_mem1 += ADD_mem[3]
	S += 53 < t17_t0_t0_mem1
	S += t17_t0_t0_mem1 <= t17_t0_t0

	t17_t0_t1_in = S.Task('t17_t0_t1_in', length=1, delay_cost=1)
	t17_t0_t1_in += alt(MUL_in)
	t17_t0_t1 = S.Task('t17_t0_t1', length=7, delay_cost=1)
	t17_t0_t1 += alt(MUL)
	S += t17_t0_t1>=t17_t0_t1_in

	t17_t0_t1_mem0 = S.Task('t17_t0_t1_mem0', length=1, delay_cost=1)
	t17_t0_t1_mem0 += INPUT_mem_r
	S += t17_t0_t1_mem0 <= t17_t0_t1

	t17_t0_t1_mem1 = S.Task('t17_t0_t1_mem1', length=1, delay_cost=1)
	t17_t0_t1_mem1 += ADD_mem[2]
	S += 51 < t17_t0_t1_mem1
	S += t17_t0_t1_mem1 <= t17_t0_t1

	t17_t0_t3 = S.Task('t17_t0_t3', length=1, delay_cost=1)
	t17_t0_t3 += alt(ADD)

	t17_t0_t3_mem0 = S.Task('t17_t0_t3_mem0', length=1, delay_cost=1)
	t17_t0_t3_mem0 += ADD_mem[3]
	S += 53 < t17_t0_t3_mem0
	S += t17_t0_t3_mem0 <= t17_t0_t3

	t17_t0_t3_mem1 = S.Task('t17_t0_t3_mem1', length=1, delay_cost=1)
	t17_t0_t3_mem1 += ADD_mem[2]
	S += 51 < t17_t0_t3_mem1
	S += t17_t0_t3_mem1 <= t17_t0_t3

	t17_t1_t1_in = S.Task('t17_t1_t1_in', length=1, delay_cost=1)
	t17_t1_t1_in += alt(MUL_in)
	t17_t1_t1 = S.Task('t17_t1_t1', length=7, delay_cost=1)
	t17_t1_t1 += alt(MUL)
	S += t17_t1_t1>=t17_t1_t1_in

	t17_t1_t1_mem0 = S.Task('t17_t1_t1_mem0', length=1, delay_cost=1)
	t17_t1_t1_mem0 += INPUT_mem_r
	S += t17_t1_t1_mem0 <= t17_t1_t1

	t17_t1_t1_mem1 = S.Task('t17_t1_t1_mem1', length=1, delay_cost=1)
	t17_t1_t1_mem1 += ADD_mem[3]
	S += 54 < t17_t1_t1_mem1
	S += t17_t1_t1_mem1 <= t17_t1_t1

	t17_t1_t3 = S.Task('t17_t1_t3', length=1, delay_cost=1)
	t17_t1_t3 += alt(ADD)

	t17_t1_t3_mem0 = S.Task('t17_t1_t3_mem0', length=1, delay_cost=1)
	t17_t1_t3_mem0 += ADD_mem[2]
	S += 50 < t17_t1_t3_mem0
	S += t17_t1_t3_mem0 <= t17_t1_t3

	t17_t1_t3_mem1 = S.Task('t17_t1_t3_mem1', length=1, delay_cost=1)
	t17_t1_t3_mem1 += ADD_mem[3]
	S += 54 < t17_t1_t3_mem1
	S += t17_t1_t3_mem1 <= t17_t1_t3

	t17_t30 = S.Task('t17_t30', length=1, delay_cost=1)
	t17_t30 += alt(ADD)

	t17_t30_mem0 = S.Task('t17_t30_mem0', length=1, delay_cost=1)
	t17_t30_mem0 += ADD_mem[3]
	S += 53 < t17_t30_mem0
	S += t17_t30_mem0 <= t17_t30

	t17_t30_mem1 = S.Task('t17_t30_mem1', length=1, delay_cost=1)
	t17_t30_mem1 += ADD_mem[2]
	S += 50 < t17_t30_mem1
	S += t17_t30_mem1 <= t17_t30

	t17_t31 = S.Task('t17_t31', length=1, delay_cost=1)
	t17_t31 += alt(ADD)

	t17_t31_mem0 = S.Task('t17_t31_mem0', length=1, delay_cost=1)
	t17_t31_mem0 += ADD_mem[2]
	S += 51 < t17_t31_mem0
	S += t17_t31_mem0 <= t17_t31

	t17_t31_mem1 = S.Task('t17_t31_mem1', length=1, delay_cost=1)
	t17_t31_mem1 += ADD_mem[3]
	S += 54 < t17_t31_mem1
	S += t17_t31_mem1 <= t17_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls24-509/scheduling/PADD_mul1_add4/PADD_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

