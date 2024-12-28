from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 141
	S = Scenario("PADD_2", horizon=horizon)

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
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 0
	t0_t1_in += MUL_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 0
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 0
	t0_t1_mem1 += INPUT_mem_r

	t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
	S += t0_t1 >= 1
	t0_t1 += MUL[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 1
	t2_t0_in += MUL_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 1
	t2_t0_mem0 += INPUT_mem_r

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 1
	t2_t0_mem1 += INPUT_mem_r

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 2
	t0_t0_in += MUL_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 2
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 2
	t0_t0_mem1 += INPUT_mem_r

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 2
	t2_t0 += MUL[0]

	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	S += t0_t0 >= 3
	t0_t0 += MUL[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 3
	t2_t1_in += MUL_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 3
	t2_t1_mem0 += INPUT_mem_r

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 3
	t2_t1_mem1 += INPUT_mem_r

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 4
	t2_t1 += MUL[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 4
	t9_t2_mem0 += INPUT_mem_r

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 4
	t9_t2_mem1 += INPUT_mem_r

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 5
	t7_t2_mem0 += INPUT_mem_r

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 5
	t7_t2_mem1 += INPUT_mem_r

	t9_t2 = S.Task('t9_t2', length=1, delay_cost=1)
	S += t9_t2 >= 5
	t9_t2 += ADD[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += INPUT_mem_r

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 6
	t7_t2 += ADD[0]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 7
	new_TZ_t2_mem0 += INPUT_mem_r

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 7
	new_TZ_t2_mem1 += INPUT_mem_r

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += ADD[3]

	new_TZ_t2 = S.Task('new_TZ_t2', length=1, delay_cost=1)
	S += new_TZ_t2 >= 8
	new_TZ_t2 += ADD[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 8
	t2_t3_mem0 += INPUT_mem_r

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 8
	t2_t3_mem1 += INPUT_mem_r

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 9
	t0_t2_mem0 += INPUT_mem_r

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 9
	t0_t2_mem1 += INPUT_mem_r

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 9
	t2_t3 += ADD[3]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 10
	t0_t2 += ADD[2]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 10
	t0_t5_mem0 += MUL_mem[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 10
	t0_t5_mem1 += MUL_mem[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 10
	t14_t2_mem0 += INPUT_mem_r

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 10
	t14_t2_mem1 += INPUT_mem_r

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 11
	t0_t4_in += MUL_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 11
	t0_t4_mem0 += ADD_mem[2]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 11
	t0_t4_mem1 += ADD_mem[3]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 11
	t0_t5 += ADD[1]

	t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
	S += t14_t2 >= 11
	t14_t2 += ADD[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 11
	t20_mem0 += MUL_mem[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 11
	t20_mem1 += MUL_mem[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 11
	t2_t2_mem0 += INPUT_mem_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 11
	t2_t2_mem1 += INPUT_mem_r

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 12
	t00_mem0 += MUL_mem[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 12
	t00_mem1 += MUL_mem[0]

	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	S += t0_t4 >= 12
	t0_t4 += MUL[0]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 12
	t16_t2_mem0 += INPUT_mem_r

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 12
	t16_t2_mem1 += INPUT_mem_r

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 12
	t20 += ADD[1]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 12
	t2_t2 += ADD[2]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 13
	t00 += ADD[2]

	t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
	S += t16_t2 >= 13
	t16_t2 += ADD[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 13
	t17_t2_mem0 += INPUT_mem_r

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 13
	t17_t2_mem1 += INPUT_mem_r

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 13
	t2_t4_in += MUL_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 13
	t2_t4_mem0 += ADD_mem[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 13
	t2_t4_mem1 += ADD_mem[3]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 13
	t2_t5_mem0 += MUL_mem[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 13
	t2_t5_mem1 += MUL_mem[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 14
	t10_mem0 += INPUT_mem_r

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 14
	t10_mem1 += ADD_mem[2]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 14
	t17_t2 += ADD[2]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 14
	t2_t4 += MUL[0]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 14
	t2_t5 += ADD[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 14
	t30_mem0 += INPUT_mem_r

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 14
	t30_mem1 += ADD_mem[1]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 15
	t10 += ADD[2]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 15
	t30 += ADD[0]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 16
	c200_in += MUL_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 16
	c200_mem0 += ADD_mem[2]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 16
	c200_mem1 += INPUT_mem_r

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 17
	c010_in += MUL_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 17
	c010_mem0 += ADD_mem[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 17
	c010_mem1 += INPUT_mem_r

	c200 = S.Task('c200', length=7, delay_cost=1)
	S += c200 >= 17
	c200 += MUL[0]

	c010 = S.Task('c010', length=7, delay_cost=1)
	S += c010 >= 18
	c010 += MUL[0]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 18
	t16_t0_in += MUL_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 18
	t16_t0_mem0 += INPUT_mem_r

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 18
	t16_t0_mem1 += ADD_mem[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 19
	t01_mem0 += MUL_mem[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 19
	t01_mem1 += ADD_mem[1]

	t16_t0 = S.Task('t16_t0', length=7, delay_cost=1)
	S += t16_t0 >= 19
	t16_t0 += MUL[0]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 19
	t17_t0_in += MUL_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 19
	t17_t0_mem0 += INPUT_mem_r

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 19
	t17_t0_mem1 += ADD_mem[2]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 20
	t01 += ADD[2]

	t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
	S += t17_t0 >= 20
	t17_t0 += MUL[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 21
	t11_mem0 += INPUT_mem_r

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 21
	t11_mem1 += ADD_mem[2]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 21
	t21_mem0 += MUL_mem[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 21
	t21_mem1 += ADD_mem[1]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 22
	t11 += ADD[3]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 22
	t21 += ADD[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 23
	t31_mem0 += INPUT_mem_r

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 23
	t31_mem1 += ADD_mem[0]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 23
	t4_t0_mem0 += ADD_mem[2]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 23
	t4_t0_mem1 += ADD_mem[3]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 23
	t4_t3_in += MUL_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 23
	t4_t3_mem0 += ADD_mem[2]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 23
	t4_t3_mem1 += ADD_mem[3]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 24
	c200_w += INPUT_mem_w

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 24
	t17_t1_in += MUL_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 24
	t17_t1_mem0 += INPUT_mem_r

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 24
	t17_t1_mem1 += ADD_mem[3]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 24
	t31 += ADD[1]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 24
	t4_t0 += ADD[3]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 24
	t4_t1_mem0 += ADD_mem[2]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 24
	t4_t1_mem1 += ADD_mem[3]

	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	S += t4_t3 >= 24
	t4_t3 += MUL[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 25
	c010_w += INPUT_mem_w

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 25
	t13_t2_mem0 += ADD_mem[2]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 25
	t13_t2_mem1 += ADD_mem[3]

	t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
	S += t17_t1 >= 25
	t17_t1 += MUL[0]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 25
	t17_t3_mem0 += ADD_mem[2]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 25
	t17_t3_mem1 += ADD_mem[3]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 25
	t4_t1 += ADD[3]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 25
	t5_t3_in += MUL_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 25
	t5_t3_mem0 += ADD_mem[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 25
	t5_t3_mem1 += ADD_mem[1]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 25
	t6_t2_mem0 += ADD_mem[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 25
	t6_t2_mem1 += ADD_mem[1]

	t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
	S += t13_t2 >= 26
	t13_t2 += ADD[1]

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	S += t17_t3 >= 26
	t17_t3 += ADD[2]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 26
	t4_t2_in += MUL_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 26
	t4_t2_mem0 += ADD_mem[3]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 26
	t4_t2_mem1 += ADD_mem[3]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 26
	t5_t0_mem0 += ADD_mem[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 26
	t5_t0_mem1 += ADD_mem[1]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 26
	t5_t1_mem0 += ADD_mem[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 26
	t5_t1_mem1 += ADD_mem[1]

	t5_t3 = S.Task('t5_t3', length=7, delay_cost=1)
	S += t5_t3 >= 26
	t5_t3 += MUL[0]

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 26
	t6_t2 += ADD[0]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 27
	new_TX_t2_mem0 += ADD_mem[0]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 27
	new_TX_t2_mem1 += ADD_mem[1]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 27
	t16_t3_mem0 += ADD_mem[0]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 27
	t16_t3_mem1 += ADD_mem[1]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 27
	t17_t4_in += MUL_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 27
	t17_t4_mem0 += ADD_mem[2]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 27
	t17_t4_mem1 += ADD_mem[2]

	t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
	S += t4_t2 >= 27
	t4_t2 += MUL[0]

	t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
	S += t5_t0 >= 27
	t5_t0 += ADD[0]

	t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
	S += t5_t1 >= 27
	t5_t1 += ADD[1]

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	S += new_TX_t2 >= 28
	new_TX_t2 += ADD[3]

	t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
	S += t16_t3 >= 28
	t16_t3 += ADD[1]

	t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
	S += t17_t4 >= 28
	t17_t4 += MUL[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 28
	t5_t2_in += MUL_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 28
	t5_t2_mem0 += ADD_mem[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 28
	t5_t2_mem1 += ADD_mem[1]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 29
	t16_t1_in += MUL_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 29
	t16_t1_mem0 += INPUT_mem_r

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 29
	t16_t1_mem1 += ADD_mem[1]

	t5_t2 = S.Task('t5_t2', length=7, delay_cost=1)
	S += t5_t2 >= 29
	t5_t2 += MUL[0]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 30
	c201_in += MUL_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 30
	c201_mem0 += ADD_mem[3]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 30
	c201_mem1 += INPUT_mem_r

	t16_t1 = S.Task('t16_t1', length=7, delay_cost=1)
	S += t16_t1 >= 30
	t16_t1 += MUL[0]

	c201 = S.Task('c201', length=7, delay_cost=1)
	S += c201 >= 31
	c201 += MUL[0]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 31
	t16_t4_in += MUL_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 31
	t16_t4_mem0 += ADD_mem[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 31
	t16_t4_mem1 += ADD_mem[1]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 31
	t41_mem0 += MUL_mem[0]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 31
	t4_t5_mem0 += MUL_mem[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 32
	c011_in += MUL_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 32
	c011_mem0 += ADD_mem[1]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 32
	c011_mem1 += INPUT_mem_r

	t16_t4 = S.Task('t16_t4', length=7, delay_cost=1)
	S += t16_t4 >= 32
	t16_t4 += MUL[0]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 32
	t17_t5_mem0 += MUL_mem[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 32
	t17_t5_mem1 += MUL_mem[0]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 32
	t41 += ADD[1]

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	S += t4_t5 >= 32
	t4_t5 += ADD[2]

	c011 = S.Task('c011', length=7, delay_cost=1)
	S += c011 >= 33
	c011 += MUL[0]

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	S += t17_t5 >= 33
	t17_t5 += ADD[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 33
	t51_mem0 += MUL_mem[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 33
	t5_t5_mem0 += MUL_mem[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 33
	t7_t1_in += MUL_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 33
	t7_t1_mem0 += INPUT_mem_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 33
	t7_t1_mem1 += ADD_mem[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 34
	t40_mem0 += MUL_mem[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 34
	t40_mem1 += ADD_mem[2]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 34
	t51 += ADD[0]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 34
	t5_t5 += ADD[3]

	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	S += t7_t1 >= 34
	t7_t1 += MUL[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 35
	t170_mem0 += MUL_mem[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 35
	t170_mem1 += MUL_mem[0]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 35
	t40 += ADD[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 35
	t6_t1_in += MUL_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 35
	t6_t1_mem0 += ADD_mem[1]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 35
	t6_t1_mem1 += ADD_mem[0]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 36
	t170 += ADD[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 36
	t171_mem0 += MUL_mem[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 36
	t171_mem1 += ADD_mem[1]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 36
	t50_mem0 += MUL_mem[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 36
	t50_mem1 += ADD_mem[3]

	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	S += t6_t1 >= 36
	t6_t1 += MUL[0]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 36
	t7_t0_in += MUL_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 36
	t7_t0_mem0 += INPUT_mem_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 36
	t7_t0_mem1 += ADD_mem[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 36
	t7_t3_mem0 += ADD_mem[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 36
	t7_t3_mem1 += ADD_mem[1]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 37
	t16_t5_mem0 += MUL_mem[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 37
	t16_t5_mem1 += MUL_mem[0]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 37
	t171 += ADD[0]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 37
	t50 += ADD[1]

	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	S += t7_t0 >= 37
	t7_t0 += MUL[0]

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 37
	t7_t3 += ADD[2]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 37
	t9_t1_in += MUL_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 37
	t9_t1_mem0 += INPUT_mem_r

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 37
	t9_t1_mem1 += ADD_mem[0]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 38
	c201_w += INPUT_mem_w

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 38
	t160_mem0 += MUL_mem[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 38
	t160_mem1 += MUL_mem[0]

	t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
	S += t16_t5 >= 38
	t16_t5 += ADD[2]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 38
	t9_t0_in += MUL_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 38
	t9_t0_mem0 += INPUT_mem_r

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 38
	t9_t0_mem1 += ADD_mem[1]

	t9_t1 = S.Task('t9_t1', length=7, delay_cost=1)
	S += t9_t1 >= 38
	t9_t1 += MUL[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 38
	t9_t3_mem0 += ADD_mem[1]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 38
	t9_t3_mem1 += ADD_mem[0]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 39
	t160 += ADD[0]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 39
	t161_mem0 += MUL_mem[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 39
	t161_mem1 += ADD_mem[2]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 39
	t6_t0_in += MUL_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 39
	t6_t0_mem0 += ADD_mem[0]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 39
	t6_t0_mem1 += ADD_mem[1]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 39
	t6_t3_mem0 += ADD_mem[1]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 39
	t6_t3_mem1 += ADD_mem[0]

	t9_t0 = S.Task('t9_t0', length=7, delay_cost=1)
	S += t9_t0 >= 39
	t9_t0 += MUL[0]

	t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
	S += t9_t3 >= 39
	t9_t3 += ADD[1]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 40
	c000_mem0 += ADD_mem[0]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 40
	c000_mem1 += ADD_mem[3]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 40
	c011_w += INPUT_mem_w

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 40
	t161 += ADD[2]

	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	S += t6_t0 >= 40
	t6_t0 += MUL[0]

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 40
	t6_t3 += ADD[3]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 40
	t9_t4_in += MUL_in[0]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 40
	t9_t4_mem0 += ADD_mem[0]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 40
	t9_t4_mem1 += ADD_mem[1]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 41
	c000 += ADD[2]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 41
	c001_mem0 += ADD_mem[2]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 41
	c001_mem1 += ADD_mem[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 41
	t6_t4_in += MUL_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 41
	t6_t4_mem0 += ADD_mem[0]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 41
	t6_t4_mem1 += ADD_mem[3]

	t9_t4 = S.Task('t9_t4', length=7, delay_cost=1)
	S += t9_t4 >= 41
	t9_t4 += MUL[0]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 42
	c000_w += INPUT_mem_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 42
	c001 += ADD[1]

	t6_t4 = S.Task('t6_t4', length=7, delay_cost=1)
	S += t6_t4 >= 42
	t6_t4 += MUL[0]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 42
	t7_t4_in += MUL_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 42
	t7_t4_mem0 += ADD_mem[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 42
	t7_t4_mem1 += ADD_mem[2]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 43
	c001_w += INPUT_mem_w

	t7_t4 = S.Task('t7_t4', length=7, delay_cost=1)
	S += t7_t4 >= 43
	t7_t4 += MUL[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 44
	t70_mem0 += MUL_mem[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 44
	t70_mem1 += MUL_mem[0]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 45
	t70 += ADD[2]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 45
	t7_t5_mem0 += MUL_mem[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 45
	t7_t5_mem1 += MUL_mem[0]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 46
	t7_t5 += ADD[3]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 46
	t9_t5_mem0 += MUL_mem[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 46
	t9_t5_mem1 += MUL_mem[0]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 47
	t6_t5_mem0 += MUL_mem[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 47
	t6_t5_mem1 += MUL_mem[0]

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	S += t9_t5 >= 47
	t9_t5 += ADD[3]

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	S += t6_t5 >= 48
	t6_t5 += ADD[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 48
	t90_mem0 += MUL_mem[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 48
	t90_mem1 += MUL_mem[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 49
	t60_mem0 += MUL_mem[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 49
	t60_mem1 += MUL_mem[0]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 49
	t90 += ADD[0]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 50
	t60 += ADD[0]


	# new tasks
	t61 = S.Task('t61', length=1, delay_cost=1)
	t61 += alt(ADD)

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += MUL_mem[0]
	S += 49 < t61_mem0
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += ADD_mem[3]
	S += 49 < t61_mem1
	S += t61_mem1 <= t61

	t71 = S.Task('t71', length=1, delay_cost=1)
	t71 += alt(ADD)

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += MUL_mem[0]
	S += 50 < t71_mem0
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += ADD_mem[3]
	S += 47 < t71_mem1
	S += t71_mem1 <= t71

	t80 = S.Task('t80', length=1, delay_cost=1)
	t80 += alt(ADD)

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += ADD_mem[0]
	S += 51 < t80_mem0
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += ADD_mem[2]
	S += 46 < t80_mem1
	S += t80_mem1 <= t80

	t91 = S.Task('t91', length=1, delay_cost=1)
	t91 += alt(ADD)

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += MUL_mem[0]
	S += 48 < t91_mem0
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += ADD_mem[3]
	S += 48 < t91_mem1
	S += t91_mem1 <= t91

	t100 = S.Task('t100', length=1, delay_cost=1)
	t100 += alt(ADD)

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += ADD_mem[0]
	S += 50 < t100_mem0
	S += t100_mem0 <= t100

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	t14_t0_in += alt(MUL_in)
	t14_t0 = S.Task('t14_t0', length=7, delay_cost=1)
	t14_t0 += alt(MUL)
	S += t14_t0>=t14_t0_in

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	t14_t0_mem0 += INPUT_mem_r
	S += t14_t0_mem0 <= t14_t0

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	t14_t0_mem1 += ADD_mem[0]
	S += 51 < t14_t0_mem1
	S += t14_t0_mem1 <= t14_t0

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	new_TZ_t0_in += alt(MUL_in)
	new_TZ_t0 = S.Task('new_TZ_t0', length=7, delay_cost=1)
	new_TZ_t0 += alt(MUL)
	S += new_TZ_t0>=new_TZ_t0_in

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	new_TZ_t0_mem0 += INPUT_mem_r
	S += new_TZ_t0_mem0 <= new_TZ_t0

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	new_TZ_t0_mem1 += ADD_mem[0]
	S += 51 < new_TZ_t0_mem1
	S += new_TZ_t0_mem1 <= new_TZ_t0

	t81 = S.Task('t81', length=1, delay_cost=1)
	t81 += alt(ADD)

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += alt(ADD_mem)
	S += (t61*ADD[0]) < t81_mem0*ADD_mem[0]
	S += (t61*ADD[1]) < t81_mem0*ADD_mem[1]
	S += (t61*ADD[2]) < t81_mem0*ADD_mem[2]
	S += (t61*ADD[3]) < t81_mem0*ADD_mem[3]
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += alt(ADD_mem)
	S += (t71*ADD[0]) < t81_mem1*ADD_mem[0]
	S += (t71*ADD[1]) < t81_mem1*ADD_mem[1]
	S += (t71*ADD[2]) < t81_mem1*ADD_mem[2]
	S += (t71*ADD[3]) < t81_mem1*ADD_mem[3]
	S += t81_mem1 <= t81

	t101 = S.Task('t101', length=1, delay_cost=1)
	t101 += alt(ADD)

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += alt(ADD_mem)
	S += (t91*ADD[0]) < t101_mem0*ADD_mem[0]
	S += (t91*ADD[1]) < t101_mem0*ADD_mem[1]
	S += (t91*ADD[2]) < t101_mem0*ADD_mem[2]
	S += (t91*ADD[3]) < t101_mem0*ADD_mem[3]
	S += t101_mem0 <= t101

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(ADD)

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(ADD_mem)
	S += (t80*ADD[0]) < t110_mem0*ADD_mem[0]
	S += (t80*ADD[1]) < t110_mem0*ADD_mem[1]
	S += (t80*ADD[2]) < t110_mem0*ADD_mem[2]
	S += (t80*ADD[3]) < t110_mem0*ADD_mem[3]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(ADD_mem)
	S += (t100*ADD[0]) < t110_mem1*ADD_mem[0]
	S += (t100*ADD[1]) < t110_mem1*ADD_mem[1]
	S += (t100*ADD[2]) < t110_mem1*ADD_mem[2]
	S += (t100*ADD[3]) < t110_mem1*ADD_mem[3]
	S += t110_mem1 <= t110

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	t14_t1_in += alt(MUL_in)
	t14_t1 = S.Task('t14_t1', length=7, delay_cost=1)
	t14_t1 += alt(MUL)
	S += t14_t1>=t14_t1_in

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	t14_t1_mem0 += INPUT_mem_r
	S += t14_t1_mem0 <= t14_t1

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	t14_t1_mem1 += alt(ADD_mem)
	S += (t61*ADD[0]) < t14_t1_mem1*ADD_mem[0]
	S += (t61*ADD[1]) < t14_t1_mem1*ADD_mem[1]
	S += (t61*ADD[2]) < t14_t1_mem1*ADD_mem[2]
	S += (t61*ADD[3]) < t14_t1_mem1*ADD_mem[3]
	S += t14_t1_mem1 <= t14_t1

	t14_t3 = S.Task('t14_t3', length=1, delay_cost=1)
	t14_t3 += alt(ADD)

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	t14_t3_mem0 += ADD_mem[0]
	S += 51 < t14_t3_mem0
	S += t14_t3_mem0 <= t14_t3

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	t14_t3_mem1 += alt(ADD_mem)
	S += (t61*ADD[0]) < t14_t3_mem1*ADD_mem[0]
	S += (t61*ADD[1]) < t14_t3_mem1*ADD_mem[1]
	S += (t61*ADD[2]) < t14_t3_mem1*ADD_mem[2]
	S += (t61*ADD[3]) < t14_t3_mem1*ADD_mem[3]
	S += t14_t3_mem1 <= t14_t3

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	new_TZ_t1_in += alt(MUL_in)
	new_TZ_t1 = S.Task('new_TZ_t1', length=7, delay_cost=1)
	new_TZ_t1 += alt(MUL)
	S += new_TZ_t1>=new_TZ_t1_in

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	new_TZ_t1_mem0 += INPUT_mem_r
	S += new_TZ_t1_mem0 <= new_TZ_t1

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	new_TZ_t1_mem1 += alt(ADD_mem)
	S += (t61*ADD[0]) < new_TZ_t1_mem1*ADD_mem[0]
	S += (t61*ADD[1]) < new_TZ_t1_mem1*ADD_mem[1]
	S += (t61*ADD[2]) < new_TZ_t1_mem1*ADD_mem[2]
	S += (t61*ADD[3]) < new_TZ_t1_mem1*ADD_mem[3]
	S += new_TZ_t1_mem1 <= new_TZ_t1

	new_TZ_t3 = S.Task('new_TZ_t3', length=1, delay_cost=1)
	new_TZ_t3 += alt(ADD)

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	new_TZ_t3_mem0 += ADD_mem[0]
	S += 51 < new_TZ_t3_mem0
	S += new_TZ_t3_mem0 <= new_TZ_t3

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	new_TZ_t3_mem1 += alt(ADD_mem)
	S += (t61*ADD[0]) < new_TZ_t3_mem1*ADD_mem[0]
	S += (t61*ADD[1]) < new_TZ_t3_mem1*ADD_mem[1]
	S += (t61*ADD[2]) < new_TZ_t3_mem1*ADD_mem[2]
	S += (t61*ADD[3]) < new_TZ_t3_mem1*ADD_mem[3]
	S += new_TZ_t3_mem1 <= new_TZ_t3

	t111 = S.Task('t111', length=1, delay_cost=1)
	t111 += alt(ADD)

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(ADD_mem)
	S += (t81*ADD[0]) < t111_mem0*ADD_mem[0]
	S += (t81*ADD[1]) < t111_mem0*ADD_mem[1]
	S += (t81*ADD[2]) < t111_mem0*ADD_mem[2]
	S += (t81*ADD[3]) < t111_mem0*ADD_mem[3]
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += alt(ADD_mem)
	S += (t101*ADD[0]) < t111_mem1*ADD_mem[0]
	S += (t101*ADD[1]) < t111_mem1*ADD_mem[1]
	S += (t101*ADD[2]) < t111_mem1*ADD_mem[2]
	S += (t101*ADD[3]) < t111_mem1*ADD_mem[3]
	S += t111_mem1 <= t111

	t120 = S.Task('t120', length=1, delay_cost=1)
	t120 += alt(ADD)

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += alt(ADD_mem)
	S += (t110*ADD[0]) < t120_mem0*ADD_mem[0]
	S += (t110*ADD[1]) < t120_mem0*ADD_mem[1]
	S += (t110*ADD[2]) < t120_mem0*ADD_mem[2]
	S += (t110*ADD[3]) < t120_mem0*ADD_mem[3]
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += ADD_mem[0]
	S += 50 < t120_mem1
	S += t120_mem1 <= t120

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MUL_in)
	new_TX_t0 = S.Task('new_TX_t0', length=7, delay_cost=1)
	new_TX_t0 += alt(MUL)
	S += new_TX_t0>=new_TX_t0_in

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += ADD_mem[0]
	S += 16 < new_TX_t0_mem0
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += alt(ADD_mem)
	S += (t110*ADD[0]) < new_TX_t0_mem1*ADD_mem[0]
	S += (t110*ADD[1]) < new_TX_t0_mem1*ADD_mem[1]
	S += (t110*ADD[2]) < new_TX_t0_mem1*ADD_mem[2]
	S += (t110*ADD[3]) < new_TX_t0_mem1*ADD_mem[3]
	S += new_TX_t0_mem1 <= new_TX_t0

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	t14_t4_in += alt(MUL_in)
	t14_t4 = S.Task('t14_t4', length=7, delay_cost=1)
	t14_t4 += alt(MUL)
	S += t14_t4>=t14_t4_in

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	t14_t4_mem0 += ADD_mem[0]
	S += 12 < t14_t4_mem0
	S += t14_t4_mem0 <= t14_t4

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	t14_t4_mem1 += alt(ADD_mem)
	S += (t14_t3*ADD[0]) < t14_t4_mem1*ADD_mem[0]
	S += (t14_t3*ADD[1]) < t14_t4_mem1*ADD_mem[1]
	S += (t14_t3*ADD[2]) < t14_t4_mem1*ADD_mem[2]
	S += (t14_t3*ADD[3]) < t14_t4_mem1*ADD_mem[3]
	S += t14_t4_mem1 <= t14_t4

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(ADD)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(MUL_mem)
	S += (t14_t0*MUL[0]) < t140_mem0*MUL_mem[0]
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MUL_mem)
	S += (t14_t1*MUL[0]) < t140_mem1*MUL_mem[0]
	S += t140_mem1 <= t140

	t14_t5 = S.Task('t14_t5', length=1, delay_cost=1)
	t14_t5 += alt(ADD)

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	t14_t5_mem0 += alt(MUL_mem)
	S += (t14_t0*MUL[0]) < t14_t5_mem0*MUL_mem[0]
	S += t14_t5_mem0 <= t14_t5

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	t14_t5_mem1 += alt(MUL_mem)
	S += (t14_t1*MUL[0]) < t14_t5_mem1*MUL_mem[0]
	S += t14_t5_mem1 <= t14_t5

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	new_TZ_t4_in += alt(MUL_in)
	new_TZ_t4 = S.Task('new_TZ_t4', length=7, delay_cost=1)
	new_TZ_t4 += alt(MUL)
	S += new_TZ_t4>=new_TZ_t4_in

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	new_TZ_t4_mem0 += ADD_mem[1]
	S += 9 < new_TZ_t4_mem0
	S += new_TZ_t4_mem0 <= new_TZ_t4

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	new_TZ_t4_mem1 += alt(ADD_mem)
	S += (new_TZ_t3*ADD[0]) < new_TZ_t4_mem1*ADD_mem[0]
	S += (new_TZ_t3*ADD[1]) < new_TZ_t4_mem1*ADD_mem[1]
	S += (new_TZ_t3*ADD[2]) < new_TZ_t4_mem1*ADD_mem[2]
	S += (new_TZ_t3*ADD[3]) < new_TZ_t4_mem1*ADD_mem[3]
	S += new_TZ_t4_mem1 <= new_TZ_t4

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	new_TZ0 += alt(ADD)

	S += 37<new_TZ0

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += alt(MUL_mem)
	S += (new_TZ_t0*MUL[0]) < new_TZ0_mem0*MUL_mem[0]
	S += new_TZ0_mem0 <= new_TZ0

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	new_TZ0_mem1 += alt(MUL_mem)
	S += (new_TZ_t1*MUL[0]) < new_TZ0_mem1*MUL_mem[0]
	S += new_TZ0_mem1 <= new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(INPUT_mem_w)
	S += new_TZ0 <= new_TZ0_w

	new_TZ_t5 = S.Task('new_TZ_t5', length=1, delay_cost=1)
	new_TZ_t5 += alt(ADD)

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	new_TZ_t5_mem0 += alt(MUL_mem)
	S += (new_TZ_t0*MUL[0]) < new_TZ_t5_mem0*MUL_mem[0]
	S += new_TZ_t5_mem0 <= new_TZ_t5

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	new_TZ_t5_mem1 += alt(MUL_mem)
	S += (new_TZ_t1*MUL[0]) < new_TZ_t5_mem1*MUL_mem[0]
	S += new_TZ_t5_mem1 <= new_TZ_t5

	t121 = S.Task('t121', length=1, delay_cost=1)
	t121 += alt(ADD)

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(ADD_mem)
	S += (t111*ADD[0]) < t121_mem0*ADD_mem[0]
	S += (t111*ADD[1]) < t121_mem0*ADD_mem[1]
	S += (t111*ADD[2]) < t121_mem0*ADD_mem[2]
	S += (t111*ADD[3]) < t121_mem0*ADD_mem[3]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += alt(ADD_mem)
	S += (t91*ADD[0]) < t121_mem1*ADD_mem[0]
	S += (t91*ADD[1]) < t121_mem1*ADD_mem[1]
	S += (t91*ADD[2]) < t121_mem1*ADD_mem[2]
	S += (t91*ADD[3]) < t121_mem1*ADD_mem[3]
	S += t121_mem1 <= t121

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MUL_in)
	new_TX_t1 = S.Task('new_TX_t1', length=7, delay_cost=1)
	new_TX_t1 += alt(MUL)
	S += new_TX_t1>=new_TX_t1_in

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += ADD_mem[1]
	S += 25 < new_TX_t1_mem0
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += alt(ADD_mem)
	S += (t111*ADD[0]) < new_TX_t1_mem1*ADD_mem[0]
	S += (t111*ADD[1]) < new_TX_t1_mem1*ADD_mem[1]
	S += (t111*ADD[2]) < new_TX_t1_mem1*ADD_mem[2]
	S += (t111*ADD[3]) < new_TX_t1_mem1*ADD_mem[3]
	S += new_TX_t1_mem1 <= new_TX_t1

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	new_TX_t3 += alt(ADD)

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	new_TX_t3_mem0 += alt(ADD_mem)
	S += (t110*ADD[0]) < new_TX_t3_mem0*ADD_mem[0]
	S += (t110*ADD[1]) < new_TX_t3_mem0*ADD_mem[1]
	S += (t110*ADD[2]) < new_TX_t3_mem0*ADD_mem[2]
	S += (t110*ADD[3]) < new_TX_t3_mem0*ADD_mem[3]
	S += new_TX_t3_mem0 <= new_TX_t3

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	new_TX_t3_mem1 += alt(ADD_mem)
	S += (t111*ADD[0]) < new_TX_t3_mem1*ADD_mem[0]
	S += (t111*ADD[1]) < new_TX_t3_mem1*ADD_mem[1]
	S += (t111*ADD[2]) < new_TX_t3_mem1*ADD_mem[2]
	S += (t111*ADD[3]) < new_TX_t3_mem1*ADD_mem[3]
	S += new_TX_t3_mem1 <= new_TX_t3

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	t13_t0_in += alt(MUL_in)
	t13_t0 = S.Task('t13_t0', length=7, delay_cost=1)
	t13_t0 += alt(MUL)
	S += t13_t0>=t13_t0_in

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	t13_t0_mem0 += ADD_mem[2]
	S += 16 < t13_t0_mem0
	S += t13_t0_mem0 <= t13_t0

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	t13_t0_mem1 += alt(ADD_mem)
	S += (t120*ADD[0]) < t13_t0_mem1*ADD_mem[0]
	S += (t120*ADD[1]) < t13_t0_mem1*ADD_mem[1]
	S += (t120*ADD[2]) < t13_t0_mem1*ADD_mem[2]
	S += (t120*ADD[3]) < t13_t0_mem1*ADD_mem[3]
	S += t13_t0_mem1 <= t13_t0

	t141 = S.Task('t141', length=1, delay_cost=1)
	t141 += alt(ADD)

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += alt(MUL_mem)
	S += (t14_t4*MUL[0]) < t141_mem0*MUL_mem[0]
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(ADD_mem)
	S += (t14_t5*ADD[0]) < t141_mem1*ADD_mem[0]
	S += (t14_t5*ADD[1]) < t141_mem1*ADD_mem[1]
	S += (t14_t5*ADD[2]) < t141_mem1*ADD_mem[2]
	S += (t14_t5*ADD[3]) < t141_mem1*ADD_mem[3]
	S += t141_mem1 <= t141

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	new_TZ1 += alt(ADD)

	S += 34<new_TZ1

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(MUL_mem)
	S += (new_TZ_t4*MUL[0]) < new_TZ1_mem0*MUL_mem[0]
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	new_TZ1_mem1 += alt(ADD_mem)
	S += (new_TZ_t5*ADD[0]) < new_TZ1_mem1*ADD_mem[0]
	S += (new_TZ_t5*ADD[1]) < new_TZ1_mem1*ADD_mem[1]
	S += (new_TZ_t5*ADD[2]) < new_TZ1_mem1*ADD_mem[2]
	S += (new_TZ_t5*ADD[3]) < new_TZ1_mem1*ADD_mem[3]
	S += new_TZ1_mem1 <= new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(INPUT_mem_w)
	S += new_TZ1 <= new_TZ1_w

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MUL_in)
	new_TX_t4 = S.Task('new_TX_t4', length=7, delay_cost=1)
	new_TX_t4 += alt(MUL)
	S += new_TX_t4>=new_TX_t4_in

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += ADD_mem[3]
	S += 29 < new_TX_t4_mem0
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += alt(ADD_mem)
	S += (new_TX_t3*ADD[0]) < new_TX_t4_mem1*ADD_mem[0]
	S += (new_TX_t3*ADD[1]) < new_TX_t4_mem1*ADD_mem[1]
	S += (new_TX_t3*ADD[2]) < new_TX_t4_mem1*ADD_mem[2]
	S += (new_TX_t3*ADD[3]) < new_TX_t4_mem1*ADD_mem[3]
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	new_TX0 += alt(ADD)

	S += 39<new_TX0

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	new_TX0_mem0 += alt(MUL_mem)
	S += (new_TX_t0*MUL[0]) < new_TX0_mem0*MUL_mem[0]
	S += new_TX0_mem0 <= new_TX0

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	new_TX0_mem1 += alt(MUL_mem)
	S += (new_TX_t1*MUL[0]) < new_TX0_mem1*MUL_mem[0]
	S += new_TX0_mem1 <= new_TX0

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	new_TX0_w += alt(INPUT_mem_w)
	S += new_TX0 <= new_TX0_w

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	new_TX_t5 += alt(ADD)

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	new_TX_t5_mem0 += alt(MUL_mem)
	S += (new_TX_t0*MUL[0]) < new_TX_t5_mem0*MUL_mem[0]
	S += new_TX_t5_mem0 <= new_TX_t5

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	new_TX_t5_mem1 += alt(MUL_mem)
	S += (new_TX_t1*MUL[0]) < new_TX_t5_mem1*MUL_mem[0]
	S += new_TX_t5_mem1 <= new_TX_t5

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	t13_t1_in += alt(MUL_in)
	t13_t1 = S.Task('t13_t1', length=7, delay_cost=1)
	t13_t1 += alt(MUL)
	S += t13_t1>=t13_t1_in

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	t13_t1_mem0 += ADD_mem[3]
	S += 23 < t13_t1_mem0
	S += t13_t1_mem0 <= t13_t1

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	t13_t1_mem1 += alt(ADD_mem)
	S += (t121*ADD[0]) < t13_t1_mem1*ADD_mem[0]
	S += (t121*ADD[1]) < t13_t1_mem1*ADD_mem[1]
	S += (t121*ADD[2]) < t13_t1_mem1*ADD_mem[2]
	S += (t121*ADD[3]) < t13_t1_mem1*ADD_mem[3]
	S += t13_t1_mem1 <= t13_t1

	t13_t3 = S.Task('t13_t3', length=1, delay_cost=1)
	t13_t3 += alt(ADD)

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	t13_t3_mem0 += alt(ADD_mem)
	S += (t120*ADD[0]) < t13_t3_mem0*ADD_mem[0]
	S += (t120*ADD[1]) < t13_t3_mem0*ADD_mem[1]
	S += (t120*ADD[2]) < t13_t3_mem0*ADD_mem[2]
	S += (t120*ADD[3]) < t13_t3_mem0*ADD_mem[3]
	S += t13_t3_mem0 <= t13_t3

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	t13_t3_mem1 += alt(ADD_mem)
	S += (t121*ADD[0]) < t13_t3_mem1*ADD_mem[0]
	S += (t121*ADD[1]) < t13_t3_mem1*ADD_mem[1]
	S += (t121*ADD[2]) < t13_t3_mem1*ADD_mem[2]
	S += (t121*ADD[3]) < t13_t3_mem1*ADD_mem[3]
	S += t13_t3_mem1 <= t13_t3

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	new_TX1 += alt(ADD)

	S += 38<new_TX1

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	new_TX1_mem0 += alt(MUL_mem)
	S += (new_TX_t4*MUL[0]) < new_TX1_mem0*MUL_mem[0]
	S += new_TX1_mem0 <= new_TX1

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	new_TX1_mem1 += alt(ADD_mem)
	S += (new_TX_t5*ADD[0]) < new_TX1_mem1*ADD_mem[0]
	S += (new_TX_t5*ADD[1]) < new_TX1_mem1*ADD_mem[1]
	S += (new_TX_t5*ADD[2]) < new_TX1_mem1*ADD_mem[2]
	S += (new_TX_t5*ADD[3]) < new_TX1_mem1*ADD_mem[3]
	S += new_TX1_mem1 <= new_TX1

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	new_TX1_w += alt(INPUT_mem_w)
	S += new_TX1 <= new_TX1_w

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	t13_t4_in += alt(MUL_in)
	t13_t4 = S.Task('t13_t4', length=7, delay_cost=1)
	t13_t4 += alt(MUL)
	S += t13_t4>=t13_t4_in

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	t13_t4_mem0 += ADD_mem[1]
	S += 27 < t13_t4_mem0
	S += t13_t4_mem0 <= t13_t4

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	t13_t4_mem1 += alt(ADD_mem)
	S += (t13_t3*ADD[0]) < t13_t4_mem1*ADD_mem[0]
	S += (t13_t3*ADD[1]) < t13_t4_mem1*ADD_mem[1]
	S += (t13_t3*ADD[2]) < t13_t4_mem1*ADD_mem[2]
	S += (t13_t3*ADD[3]) < t13_t4_mem1*ADD_mem[3]
	S += t13_t4_mem1 <= t13_t4

	t130 = S.Task('t130', length=1, delay_cost=1)
	t130 += alt(ADD)

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += alt(MUL_mem)
	S += (t13_t0*MUL[0]) < t130_mem0*MUL_mem[0]
	S += t130_mem0 <= t130

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	t130_mem1 += alt(MUL_mem)
	S += (t13_t1*MUL[0]) < t130_mem1*MUL_mem[0]
	S += t130_mem1 <= t130

	t13_t5 = S.Task('t13_t5', length=1, delay_cost=1)
	t13_t5 += alt(ADD)

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	t13_t5_mem0 += alt(MUL_mem)
	S += (t13_t0*MUL[0]) < t13_t5_mem0*MUL_mem[0]
	S += t13_t5_mem0 <= t13_t5

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	t13_t5_mem1 += alt(MUL_mem)
	S += (t13_t1*MUL[0]) < t13_t5_mem1*MUL_mem[0]
	S += t13_t5_mem1 <= t13_t5

	t131 = S.Task('t131', length=1, delay_cost=1)
	t131 += alt(ADD)

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += alt(MUL_mem)
	S += (t13_t4*MUL[0]) < t131_mem0*MUL_mem[0]
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += alt(ADD_mem)
	S += (t13_t5*ADD[0]) < t131_mem1*ADD_mem[0]
	S += (t13_t5*ADD[1]) < t131_mem1*ADD_mem[1]
	S += (t13_t5*ADD[2]) < t131_mem1*ADD_mem[2]
	S += (t13_t5*ADD[3]) < t131_mem1*ADD_mem[3]
	S += t131_mem1 <= t131

	t150 = S.Task('t150', length=1, delay_cost=1)
	t150 += alt(ADD)

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(ADD_mem)
	S += (t130*ADD[0]) < t150_mem0*ADD_mem[0]
	S += (t130*ADD[1]) < t150_mem0*ADD_mem[1]
	S += (t130*ADD[2]) < t150_mem0*ADD_mem[2]
	S += (t130*ADD[3]) < t150_mem0*ADD_mem[3]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(ADD_mem)
	S += (t140*ADD[0]) < t150_mem1*ADD_mem[0]
	S += (t140*ADD[1]) < t150_mem1*ADD_mem[1]
	S += (t140*ADD[2]) < t150_mem1*ADD_mem[2]
	S += (t140*ADD[3]) < t150_mem1*ADD_mem[3]
	S += t150_mem1 <= t150

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(ADD)

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(ADD_mem)
	S += (t131*ADD[0]) < t151_mem0*ADD_mem[0]
	S += (t131*ADD[1]) < t151_mem0*ADD_mem[1]
	S += (t131*ADD[2]) < t151_mem0*ADD_mem[2]
	S += (t131*ADD[3]) < t151_mem0*ADD_mem[3]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(ADD_mem)
	S += (t141*ADD[0]) < t151_mem1*ADD_mem[0]
	S += (t141*ADD[1]) < t151_mem1*ADD_mem[1]
	S += (t141*ADD[2]) < t151_mem1*ADD_mem[2]
	S += (t141*ADD[3]) < t151_mem1*ADD_mem[3]
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	new_TY0 += alt(ADD)

	S += 15<new_TY0

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += INPUT_mem_r
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += alt(ADD_mem)
	S += (t150*ADD[0]) < new_TY0_mem1*ADD_mem[0]
	S += (t150*ADD[1]) < new_TY0_mem1*ADD_mem[1]
	S += (t150*ADD[2]) < new_TY0_mem1*ADD_mem[2]
	S += (t150*ADD[3]) < new_TY0_mem1*ADD_mem[3]
	S += new_TY0_mem1 <= new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(INPUT_mem_w)
	S += new_TY0 <= new_TY0_w

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	new_TY1 += alt(ADD)

	S += 22<new_TY1

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += INPUT_mem_r
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += alt(ADD_mem)
	S += (t151*ADD[0]) < new_TY1_mem1*ADD_mem[0]
	S += (t151*ADD[1]) < new_TY1_mem1*ADD_mem[1]
	S += (t151*ADD[2]) < new_TY1_mem1*ADD_mem[2]
	S += (t151*ADD[3]) < new_TY1_mem1*ADD_mem[3]
	S += new_TY1_mem1 <= new_TY1

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	new_TY1_w += alt(INPUT_mem_w)
	S += new_TY1 <= new_TY1_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-1150/scheduling/PADD_mul1_add4/PADD_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

