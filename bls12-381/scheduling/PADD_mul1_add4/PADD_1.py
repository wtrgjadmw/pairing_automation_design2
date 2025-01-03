from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 105
	S = Scenario("PADD_1", horizon=horizon)

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

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 10
	t14_t2_mem0 += INPUT_mem_r

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 10
	t14_t2_mem1 += INPUT_mem_r

	t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
	S += t14_t2 >= 11
	t14_t2 += ADD[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 11
	t2_t2_mem0 += INPUT_mem_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 11
	t2_t2_mem1 += INPUT_mem_r

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 12
	t16_t2_mem0 += INPUT_mem_r

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 12
	t16_t2_mem1 += INPUT_mem_r

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 12
	t2_t2 += ADD[2]

	t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
	S += t16_t2 >= 13
	t16_t2 += ADD[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 13
	t17_t2_mem0 += INPUT_mem_r

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 13
	t17_t2_mem1 += INPUT_mem_r

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 14
	t17_t2 += ADD[2]


	# new tasks
	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	t0_t4_in += alt(MUL_in)
	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	t0_t4 += alt(MUL)
	S += t0_t4>=t0_t4_in

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	t0_t4_mem0 += ADD_mem[2]
	S += 11 < t0_t4_mem0
	S += t0_t4_mem0 <= t0_t4

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	t0_t4_mem1 += ADD_mem[3]
	S += 8 < t0_t4_mem1
	S += t0_t4_mem1 <= t0_t4

	t00 = S.Task('t00', length=1, delay_cost=1)
	t00 += alt(ADD)

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += MUL_mem[0]
	S += 10 < t00_mem0
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += MUL_mem[0]
	S += 8 < t00_mem1
	S += t00_mem1 <= t00

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(ADD)

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MUL_mem[0]
	S += 10 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MUL_mem[0]
	S += 8 < t0_t5_mem1
	S += t0_t5_mem1 <= t0_t5

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MUL_in)
	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	t2_t4 += alt(MUL)
	S += t2_t4>=t2_t4_in

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += ADD_mem[2]
	S += 13 < t2_t4_mem0
	S += t2_t4_mem0 <= t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += ADD_mem[3]
	S += 10 < t2_t4_mem1
	S += t2_t4_mem1 <= t2_t4

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(ADD)

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MUL_mem[0]
	S += 9 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MUL_mem[0]
	S += 11 < t20_mem1
	S += t20_mem1 <= t20

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	t2_t5 += alt(ADD)

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += MUL_mem[0]
	S += 9 < t2_t5_mem0
	S += t2_t5_mem0 <= t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += MUL_mem[0]
	S += 11 < t2_t5_mem1
	S += t2_t5_mem1 <= t2_t5

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(ADD)

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += alt(MUL_mem)
	S += (t0_t4*MUL[0]) < t01_mem0*MUL_mem[0]
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += alt(ADD_mem)
	S += (t0_t5*ADD[0]) < t01_mem1*ADD_mem[0]
	S += (t0_t5*ADD[1]) < t01_mem1*ADD_mem[1]
	S += (t0_t5*ADD[2]) < t01_mem1*ADD_mem[2]
	S += (t0_t5*ADD[3]) < t01_mem1*ADD_mem[3]
	S += t01_mem1 <= t01

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(ADD)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += INPUT_mem_r
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(ADD_mem)
	S += (t00*ADD[0]) < t10_mem1*ADD_mem[0]
	S += (t00*ADD[1]) < t10_mem1*ADD_mem[1]
	S += (t00*ADD[2]) < t10_mem1*ADD_mem[2]
	S += (t00*ADD[3]) < t10_mem1*ADD_mem[3]
	S += t10_mem1 <= t10

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(ADD)

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += alt(MUL_mem)
	S += (t2_t4*MUL[0]) < t21_mem0*MUL_mem[0]
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += alt(ADD_mem)
	S += (t2_t5*ADD[0]) < t21_mem1*ADD_mem[0]
	S += (t2_t5*ADD[1]) < t21_mem1*ADD_mem[1]
	S += (t2_t5*ADD[2]) < t21_mem1*ADD_mem[2]
	S += (t2_t5*ADD[3]) < t21_mem1*ADD_mem[3]
	S += t21_mem1 <= t21

	t30 = S.Task('t30', length=1, delay_cost=1)
	t30 += alt(ADD)

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += INPUT_mem_r
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += alt(ADD_mem)
	S += (t20*ADD[0]) < t30_mem1*ADD_mem[0]
	S += (t20*ADD[1]) < t30_mem1*ADD_mem[1]
	S += (t20*ADD[2]) < t30_mem1*ADD_mem[2]
	S += (t20*ADD[3]) < t30_mem1*ADD_mem[3]
	S += t30_mem1 <= t30

	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(ADD)

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += INPUT_mem_r
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(ADD_mem)
	S += (t01*ADD[0]) < t11_mem1*ADD_mem[0]
	S += (t01*ADD[1]) < t11_mem1*ADD_mem[1]
	S += (t01*ADD[2]) < t11_mem1*ADD_mem[2]
	S += (t01*ADD[3]) < t11_mem1*ADD_mem[3]
	S += t11_mem1 <= t11

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(ADD)

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += INPUT_mem_r
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(ADD_mem)
	S += (t21*ADD[0]) < t31_mem1*ADD_mem[0]
	S += (t21*ADD[1]) < t31_mem1*ADD_mem[1]
	S += (t21*ADD[2]) < t31_mem1*ADD_mem[2]
	S += (t21*ADD[3]) < t31_mem1*ADD_mem[3]
	S += t31_mem1 <= t31

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MUL_in)
	c010 = S.Task('c010', length=7, delay_cost=1)
	c010 += alt(MUL)
	S += c010>=c010_in

	S += 0<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < c010_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < c010_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < c010_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < c010_mem0*ADD_mem[3]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += INPUT_mem_r
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010 <= c010_w

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MUL_in)
	c200 = S.Task('c200', length=7, delay_cost=1)
	c200 += alt(MUL)
	S += c200>=c200_in

	S += 0<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < c200_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < c200_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < c200_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < c200_mem0*ADD_mem[3]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += INPUT_mem_r
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200 <= c200_w

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	t16_t0_in += alt(MUL_in)
	t16_t0 = S.Task('t16_t0', length=7, delay_cost=1)
	t16_t0 += alt(MUL)
	S += t16_t0>=t16_t0_in

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	t16_t0_mem0 += INPUT_mem_r
	S += t16_t0_mem0 <= t16_t0

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	t16_t0_mem1 += alt(ADD_mem)
	S += (t30*ADD[0]) < t16_t0_mem1*ADD_mem[0]
	S += (t30*ADD[1]) < t16_t0_mem1*ADD_mem[1]
	S += (t30*ADD[2]) < t16_t0_mem1*ADD_mem[2]
	S += (t30*ADD[3]) < t16_t0_mem1*ADD_mem[3]
	S += t16_t0_mem1 <= t16_t0

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	t17_t0_in += alt(MUL_in)
	t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
	t17_t0 += alt(MUL)
	S += t17_t0>=t17_t0_in

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	t17_t0_mem0 += INPUT_mem_r
	S += t17_t0_mem0 <= t17_t0

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	t17_t0_mem1 += alt(ADD_mem)
	S += (t10*ADD[0]) < t17_t0_mem1*ADD_mem[0]
	S += (t10*ADD[1]) < t17_t0_mem1*ADD_mem[1]
	S += (t10*ADD[2]) < t17_t0_mem1*ADD_mem[2]
	S += (t10*ADD[3]) < t17_t0_mem1*ADD_mem[3]
	S += t17_t0_mem1 <= t17_t0

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	t4_t0 += alt(ADD)

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	t4_t0_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < t4_t0_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < t4_t0_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < t4_t0_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < t4_t0_mem0*ADD_mem[3]
	S += t4_t0_mem0 <= t4_t0

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	t4_t0_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t4_t0_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t4_t0_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t4_t0_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t4_t0_mem1*ADD_mem[3]
	S += t4_t0_mem1 <= t4_t0

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	t4_t1 += alt(ADD)

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	t4_t1_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < t4_t1_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < t4_t1_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < t4_t1_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < t4_t1_mem0*ADD_mem[3]
	S += t4_t1_mem0 <= t4_t1

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	t4_t1_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t4_t1_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t4_t1_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t4_t1_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t4_t1_mem1*ADD_mem[3]
	S += t4_t1_mem1 <= t4_t1

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	t4_t3_in += alt(MUL_in)
	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	t4_t3 += alt(MUL)
	S += t4_t3>=t4_t3_in

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	t4_t3_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < t4_t3_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < t4_t3_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < t4_t3_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < t4_t3_mem0*ADD_mem[3]
	S += t4_t3_mem0 <= t4_t3

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	t4_t3_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t4_t3_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t4_t3_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t4_t3_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t4_t3_mem1*ADD_mem[3]
	S += t4_t3_mem1 <= t4_t3

	t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
	t5_t0 += alt(ADD)

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	t5_t0_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t5_t0_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t5_t0_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t5_t0_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t5_t0_mem0*ADD_mem[3]
	S += t5_t0_mem0 <= t5_t0

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	t5_t0_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < t5_t0_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < t5_t0_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < t5_t0_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < t5_t0_mem1*ADD_mem[3]
	S += t5_t0_mem1 <= t5_t0

	t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
	t5_t1 += alt(ADD)

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	t5_t1_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t5_t1_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t5_t1_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t5_t1_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t5_t1_mem0*ADD_mem[3]
	S += t5_t1_mem0 <= t5_t1

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	t5_t1_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < t5_t1_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < t5_t1_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < t5_t1_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < t5_t1_mem1*ADD_mem[3]
	S += t5_t1_mem1 <= t5_t1

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	t5_t3_in += alt(MUL_in)
	t5_t3 = S.Task('t5_t3', length=7, delay_cost=1)
	t5_t3 += alt(MUL)
	S += t5_t3>=t5_t3_in

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	t5_t3_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t5_t3_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t5_t3_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t5_t3_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t5_t3_mem0*ADD_mem[3]
	S += t5_t3_mem0 <= t5_t3

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	t5_t3_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < t5_t3_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < t5_t3_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < t5_t3_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < t5_t3_mem1*ADD_mem[3]
	S += t5_t3_mem1 <= t5_t3

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	t6_t2 += alt(ADD)

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	t6_t2_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t6_t2_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t6_t2_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t6_t2_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t6_t2_mem0*ADD_mem[3]
	S += t6_t2_mem0 <= t6_t2

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	t6_t2_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < t6_t2_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < t6_t2_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < t6_t2_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < t6_t2_mem1*ADD_mem[3]
	S += t6_t2_mem1 <= t6_t2

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	new_TX_t2 += alt(ADD)

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	new_TX_t2_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < new_TX_t2_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < new_TX_t2_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < new_TX_t2_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < new_TX_t2_mem0*ADD_mem[3]
	S += new_TX_t2_mem0 <= new_TX_t2

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	new_TX_t2_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < new_TX_t2_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < new_TX_t2_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < new_TX_t2_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < new_TX_t2_mem1*ADD_mem[3]
	S += new_TX_t2_mem1 <= new_TX_t2

	t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
	t13_t2 += alt(ADD)

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	t13_t2_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < t13_t2_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < t13_t2_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < t13_t2_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < t13_t2_mem0*ADD_mem[3]
	S += t13_t2_mem0 <= t13_t2

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	t13_t2_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t13_t2_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t13_t2_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t13_t2_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t13_t2_mem1*ADD_mem[3]
	S += t13_t2_mem1 <= t13_t2

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MUL_in)
	c011 = S.Task('c011', length=7, delay_cost=1)
	c011 += alt(MUL)
	S += c011>=c011_in

	S += 0<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(ADD_mem)
	S += (t31*ADD[0]) < c011_mem0*ADD_mem[0]
	S += (t31*ADD[1]) < c011_mem0*ADD_mem[1]
	S += (t31*ADD[2]) < c011_mem0*ADD_mem[2]
	S += (t31*ADD[3]) < c011_mem0*ADD_mem[3]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += INPUT_mem_r
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(INPUT_mem_w)
	S += c011 <= c011_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MUL_in)
	c201 = S.Task('c201', length=7, delay_cost=1)
	c201 += alt(MUL)
	S += c201>=c201_in

	S += 0<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(ADD_mem)
	S += (t11*ADD[0]) < c201_mem0*ADD_mem[0]
	S += (t11*ADD[1]) < c201_mem0*ADD_mem[1]
	S += (t11*ADD[2]) < c201_mem0*ADD_mem[2]
	S += (t11*ADD[3]) < c201_mem0*ADD_mem[3]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += INPUT_mem_r
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201 <= c201_w

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	t16_t1_in += alt(MUL_in)
	t16_t1 = S.Task('t16_t1', length=7, delay_cost=1)
	t16_t1 += alt(MUL)
	S += t16_t1>=t16_t1_in

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	t16_t1_mem0 += INPUT_mem_r
	S += t16_t1_mem0 <= t16_t1

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	t16_t1_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < t16_t1_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < t16_t1_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < t16_t1_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < t16_t1_mem1*ADD_mem[3]
	S += t16_t1_mem1 <= t16_t1

	t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
	t16_t3 += alt(ADD)

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	t16_t3_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t16_t3_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t16_t3_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t16_t3_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t16_t3_mem0*ADD_mem[3]
	S += t16_t3_mem0 <= t16_t3

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	t16_t3_mem1 += alt(ADD_mem)
	S += (t31*ADD[0]) < t16_t3_mem1*ADD_mem[0]
	S += (t31*ADD[1]) < t16_t3_mem1*ADD_mem[1]
	S += (t31*ADD[2]) < t16_t3_mem1*ADD_mem[2]
	S += (t31*ADD[3]) < t16_t3_mem1*ADD_mem[3]
	S += t16_t3_mem1 <= t16_t3

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	t17_t1_in += alt(MUL_in)
	t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
	t17_t1 += alt(MUL)
	S += t17_t1>=t17_t1_in

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	t17_t1_mem0 += INPUT_mem_r
	S += t17_t1_mem0 <= t17_t1

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	t17_t1_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t17_t1_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t17_t1_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t17_t1_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t17_t1_mem1*ADD_mem[3]
	S += t17_t1_mem1 <= t17_t1

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	t17_t3 += alt(ADD)

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	t17_t3_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < t17_t3_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < t17_t3_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < t17_t3_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < t17_t3_mem0*ADD_mem[3]
	S += t17_t3_mem0 <= t17_t3

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	t17_t3_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t17_t3_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t17_t3_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t17_t3_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t17_t3_mem1*ADD_mem[3]
	S += t17_t3_mem1 <= t17_t3

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	t4_t2_in += alt(MUL_in)
	t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
	t4_t2 += alt(MUL)
	S += t4_t2>=t4_t2_in

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	t4_t2_mem0 += alt(ADD_mem)
	S += (t4_t0*ADD[0]) < t4_t2_mem0*ADD_mem[0]
	S += (t4_t0*ADD[1]) < t4_t2_mem0*ADD_mem[1]
	S += (t4_t0*ADD[2]) < t4_t2_mem0*ADD_mem[2]
	S += (t4_t0*ADD[3]) < t4_t2_mem0*ADD_mem[3]
	S += t4_t2_mem0 <= t4_t2

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	t4_t2_mem1 += alt(ADD_mem)
	S += (t4_t1*ADD[0]) < t4_t2_mem1*ADD_mem[0]
	S += (t4_t1*ADD[1]) < t4_t2_mem1*ADD_mem[1]
	S += (t4_t1*ADD[2]) < t4_t2_mem1*ADD_mem[2]
	S += (t4_t1*ADD[3]) < t4_t2_mem1*ADD_mem[3]
	S += t4_t2_mem1 <= t4_t2

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	t4_t5 += alt(ADD)

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	t4_t5_mem0 += alt(MUL_mem)
	S += (t4_t3*MUL[0]) < t4_t5_mem0*MUL_mem[0]
	S += t4_t5_mem0 <= t4_t5

	t41 = S.Task('t41', length=1, delay_cost=1)
	t41 += alt(ADD)

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += alt(MUL_mem)
	S += (t4_t3*MUL[0]) < t41_mem0*MUL_mem[0]
	S += t41_mem0 <= t41

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	t5_t2_in += alt(MUL_in)
	t5_t2 = S.Task('t5_t2', length=7, delay_cost=1)
	t5_t2 += alt(MUL)
	S += t5_t2>=t5_t2_in

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	t5_t2_mem0 += alt(ADD_mem)
	S += (t5_t0*ADD[0]) < t5_t2_mem0*ADD_mem[0]
	S += (t5_t0*ADD[1]) < t5_t2_mem0*ADD_mem[1]
	S += (t5_t0*ADD[2]) < t5_t2_mem0*ADD_mem[2]
	S += (t5_t0*ADD[3]) < t5_t2_mem0*ADD_mem[3]
	S += t5_t2_mem0 <= t5_t2

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	t5_t2_mem1 += alt(ADD_mem)
	S += (t5_t1*ADD[0]) < t5_t2_mem1*ADD_mem[0]
	S += (t5_t1*ADD[1]) < t5_t2_mem1*ADD_mem[1]
	S += (t5_t1*ADD[2]) < t5_t2_mem1*ADD_mem[2]
	S += (t5_t1*ADD[3]) < t5_t2_mem1*ADD_mem[3]
	S += t5_t2_mem1 <= t5_t2

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	t5_t5 += alt(ADD)

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += alt(MUL_mem)
	S += (t5_t3*MUL[0]) < t5_t5_mem0*MUL_mem[0]
	S += t5_t5_mem0 <= t5_t5

	t51 = S.Task('t51', length=1, delay_cost=1)
	t51 += alt(ADD)

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	t51_mem0 += alt(MUL_mem)
	S += (t5_t3*MUL[0]) < t51_mem0*MUL_mem[0]
	S += t51_mem0 <= t51

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	t16_t4_in += alt(MUL_in)
	t16_t4 = S.Task('t16_t4', length=7, delay_cost=1)
	t16_t4 += alt(MUL)
	S += t16_t4>=t16_t4_in

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	t16_t4_mem0 += ADD_mem[0]
	S += 14 < t16_t4_mem0
	S += t16_t4_mem0 <= t16_t4

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	t16_t4_mem1 += alt(ADD_mem)
	S += (t16_t3*ADD[0]) < t16_t4_mem1*ADD_mem[0]
	S += (t16_t3*ADD[1]) < t16_t4_mem1*ADD_mem[1]
	S += (t16_t3*ADD[2]) < t16_t4_mem1*ADD_mem[2]
	S += (t16_t3*ADD[3]) < t16_t4_mem1*ADD_mem[3]
	S += t16_t4_mem1 <= t16_t4

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(ADD)

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += alt(MUL_mem)
	S += (t16_t0*MUL[0]) < t160_mem0*MUL_mem[0]
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MUL_mem)
	S += (t16_t1*MUL[0]) < t160_mem1*MUL_mem[0]
	S += t160_mem1 <= t160

	t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
	t16_t5 += alt(ADD)

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	t16_t5_mem0 += alt(MUL_mem)
	S += (t16_t0*MUL[0]) < t16_t5_mem0*MUL_mem[0]
	S += t16_t5_mem0 <= t16_t5

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	t16_t5_mem1 += alt(MUL_mem)
	S += (t16_t1*MUL[0]) < t16_t5_mem1*MUL_mem[0]
	S += t16_t5_mem1 <= t16_t5

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	t17_t4_in += alt(MUL_in)
	t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
	t17_t4 += alt(MUL)
	S += t17_t4>=t17_t4_in

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	t17_t4_mem0 += ADD_mem[2]
	S += 15 < t17_t4_mem0
	S += t17_t4_mem0 <= t17_t4

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	t17_t4_mem1 += alt(ADD_mem)
	S += (t17_t3*ADD[0]) < t17_t4_mem1*ADD_mem[0]
	S += (t17_t3*ADD[1]) < t17_t4_mem1*ADD_mem[1]
	S += (t17_t3*ADD[2]) < t17_t4_mem1*ADD_mem[2]
	S += (t17_t3*ADD[3]) < t17_t4_mem1*ADD_mem[3]
	S += t17_t4_mem1 <= t17_t4

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(ADD)

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += alt(MUL_mem)
	S += (t17_t0*MUL[0]) < t170_mem0*MUL_mem[0]
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MUL_mem)
	S += (t17_t1*MUL[0]) < t170_mem1*MUL_mem[0]
	S += t170_mem1 <= t170

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	t17_t5 += alt(ADD)

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	t17_t5_mem0 += alt(MUL_mem)
	S += (t17_t0*MUL[0]) < t17_t5_mem0*MUL_mem[0]
	S += t17_t5_mem0 <= t17_t5

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	t17_t5_mem1 += alt(MUL_mem)
	S += (t17_t1*MUL[0]) < t17_t5_mem1*MUL_mem[0]
	S += t17_t5_mem1 <= t17_t5

	t40 = S.Task('t40', length=1, delay_cost=1)
	t40 += alt(ADD)

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(MUL_mem)
	S += (t4_t2*MUL[0]) < t40_mem0*MUL_mem[0]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += alt(ADD_mem)
	S += (t4_t5*ADD[0]) < t40_mem1*ADD_mem[0]
	S += (t4_t5*ADD[1]) < t40_mem1*ADD_mem[1]
	S += (t4_t5*ADD[2]) < t40_mem1*ADD_mem[2]
	S += (t4_t5*ADD[3]) < t40_mem1*ADD_mem[3]
	S += t40_mem1 <= t40

	t50 = S.Task('t50', length=1, delay_cost=1)
	t50 += alt(ADD)

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += alt(MUL_mem)
	S += (t5_t2*MUL[0]) < t50_mem0*MUL_mem[0]
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += alt(ADD_mem)
	S += (t5_t5*ADD[0]) < t50_mem1*ADD_mem[0]
	S += (t5_t5*ADD[1]) < t50_mem1*ADD_mem[1]
	S += (t5_t5*ADD[2]) < t50_mem1*ADD_mem[2]
	S += (t5_t5*ADD[3]) < t50_mem1*ADD_mem[3]
	S += t50_mem1 <= t50

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	t6_t1_in += alt(MUL_in)
	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	t6_t1 += alt(MUL)
	S += t6_t1>=t6_t1_in

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	t6_t1_mem0 += alt(ADD_mem)
	S += (t31*ADD[0]) < t6_t1_mem0*ADD_mem[0]
	S += (t31*ADD[1]) < t6_t1_mem0*ADD_mem[1]
	S += (t31*ADD[2]) < t6_t1_mem0*ADD_mem[2]
	S += (t31*ADD[3]) < t6_t1_mem0*ADD_mem[3]
	S += t6_t1_mem0 <= t6_t1

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	t6_t1_mem1 += alt(ADD_mem)
	S += (t51*ADD[0]) < t6_t1_mem1*ADD_mem[0]
	S += (t51*ADD[1]) < t6_t1_mem1*ADD_mem[1]
	S += (t51*ADD[2]) < t6_t1_mem1*ADD_mem[2]
	S += (t51*ADD[3]) < t6_t1_mem1*ADD_mem[3]
	S += t6_t1_mem1 <= t6_t1

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	t7_t1_in += alt(MUL_in)
	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	t7_t1 += alt(MUL)
	S += t7_t1>=t7_t1_in

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	t7_t1_mem0 += INPUT_mem_r
	S += t7_t1_mem0 <= t7_t1

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	t7_t1_mem1 += alt(ADD_mem)
	S += (t41*ADD[0]) < t7_t1_mem1*ADD_mem[0]
	S += (t41*ADD[1]) < t7_t1_mem1*ADD_mem[1]
	S += (t41*ADD[2]) < t7_t1_mem1*ADD_mem[2]
	S += (t41*ADD[3]) < t7_t1_mem1*ADD_mem[3]
	S += t7_t1_mem1 <= t7_t1

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	t9_t1_in += alt(MUL_in)
	t9_t1 = S.Task('t9_t1', length=7, delay_cost=1)
	t9_t1 += alt(MUL)
	S += t9_t1>=t9_t1_in

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	t9_t1_mem0 += INPUT_mem_r
	S += t9_t1_mem0 <= t9_t1

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	t9_t1_mem1 += alt(ADD_mem)
	S += (t51*ADD[0]) < t9_t1_mem1*ADD_mem[0]
	S += (t51*ADD[1]) < t9_t1_mem1*ADD_mem[1]
	S += (t51*ADD[2]) < t9_t1_mem1*ADD_mem[2]
	S += (t51*ADD[3]) < t9_t1_mem1*ADD_mem[3]
	S += t9_t1_mem1 <= t9_t1

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(ADD)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += alt(MUL_mem)
	S += (t16_t4*MUL[0]) < t161_mem0*MUL_mem[0]
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += alt(ADD_mem)
	S += (t16_t5*ADD[0]) < t161_mem1*ADD_mem[0]
	S += (t16_t5*ADD[1]) < t161_mem1*ADD_mem[1]
	S += (t16_t5*ADD[2]) < t161_mem1*ADD_mem[2]
	S += (t16_t5*ADD[3]) < t161_mem1*ADD_mem[3]
	S += t161_mem1 <= t161

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(ADD)

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MUL_mem)
	S += (t17_t4*MUL[0]) < t171_mem0*MUL_mem[0]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(ADD_mem)
	S += (t17_t5*ADD[0]) < t171_mem1*ADD_mem[0]
	S += (t17_t5*ADD[1]) < t171_mem1*ADD_mem[1]
	S += (t17_t5*ADD[2]) < t171_mem1*ADD_mem[2]
	S += (t17_t5*ADD[3]) < t171_mem1*ADD_mem[3]
	S += t171_mem1 <= t171

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(ADD)

	S += 0<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(ADD_mem)
	S += (t160*ADD[0]) < c000_mem0*ADD_mem[0]
	S += (t160*ADD[1]) < c000_mem0*ADD_mem[1]
	S += (t160*ADD[2]) < c000_mem0*ADD_mem[2]
	S += (t160*ADD[3]) < c000_mem0*ADD_mem[3]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(ADD_mem)
	S += (t170*ADD[0]) < c000_mem1*ADD_mem[0]
	S += (t170*ADD[1]) < c000_mem1*ADD_mem[1]
	S += (t170*ADD[2]) < c000_mem1*ADD_mem[2]
	S += (t170*ADD[3]) < c000_mem1*ADD_mem[3]
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(INPUT_mem_w)
	S += c000 <= c000_w

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	t6_t0_in += alt(MUL_in)
	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	t6_t0 += alt(MUL)
	S += t6_t0>=t6_t0_in

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	t6_t0_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t6_t0_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t6_t0_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t6_t0_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t6_t0_mem0*ADD_mem[3]
	S += t6_t0_mem0 <= t6_t0

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	t6_t0_mem1 += alt(ADD_mem)
	S += (t50*ADD[0]) < t6_t0_mem1*ADD_mem[0]
	S += (t50*ADD[1]) < t6_t0_mem1*ADD_mem[1]
	S += (t50*ADD[2]) < t6_t0_mem1*ADD_mem[2]
	S += (t50*ADD[3]) < t6_t0_mem1*ADD_mem[3]
	S += t6_t0_mem1 <= t6_t0

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	t6_t3 += alt(ADD)

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	t6_t3_mem0 += alt(ADD_mem)
	S += (t50*ADD[0]) < t6_t3_mem0*ADD_mem[0]
	S += (t50*ADD[1]) < t6_t3_mem0*ADD_mem[1]
	S += (t50*ADD[2]) < t6_t3_mem0*ADD_mem[2]
	S += (t50*ADD[3]) < t6_t3_mem0*ADD_mem[3]
	S += t6_t3_mem0 <= t6_t3

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	t6_t3_mem1 += alt(ADD_mem)
	S += (t51*ADD[0]) < t6_t3_mem1*ADD_mem[0]
	S += (t51*ADD[1]) < t6_t3_mem1*ADD_mem[1]
	S += (t51*ADD[2]) < t6_t3_mem1*ADD_mem[2]
	S += (t51*ADD[3]) < t6_t3_mem1*ADD_mem[3]
	S += t6_t3_mem1 <= t6_t3

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	t7_t0_in += alt(MUL_in)
	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	t7_t0 += alt(MUL)
	S += t7_t0>=t7_t0_in

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	t7_t0_mem0 += INPUT_mem_r
	S += t7_t0_mem0 <= t7_t0

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	t7_t0_mem1 += alt(ADD_mem)
	S += (t40*ADD[0]) < t7_t0_mem1*ADD_mem[0]
	S += (t40*ADD[1]) < t7_t0_mem1*ADD_mem[1]
	S += (t40*ADD[2]) < t7_t0_mem1*ADD_mem[2]
	S += (t40*ADD[3]) < t7_t0_mem1*ADD_mem[3]
	S += t7_t0_mem1 <= t7_t0

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	t7_t3 += alt(ADD)

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	t7_t3_mem0 += alt(ADD_mem)
	S += (t40*ADD[0]) < t7_t3_mem0*ADD_mem[0]
	S += (t40*ADD[1]) < t7_t3_mem0*ADD_mem[1]
	S += (t40*ADD[2]) < t7_t3_mem0*ADD_mem[2]
	S += (t40*ADD[3]) < t7_t3_mem0*ADD_mem[3]
	S += t7_t3_mem0 <= t7_t3

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	t7_t3_mem1 += alt(ADD_mem)
	S += (t41*ADD[0]) < t7_t3_mem1*ADD_mem[0]
	S += (t41*ADD[1]) < t7_t3_mem1*ADD_mem[1]
	S += (t41*ADD[2]) < t7_t3_mem1*ADD_mem[2]
	S += (t41*ADD[3]) < t7_t3_mem1*ADD_mem[3]
	S += t7_t3_mem1 <= t7_t3

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	t9_t0_in += alt(MUL_in)
	t9_t0 = S.Task('t9_t0', length=7, delay_cost=1)
	t9_t0 += alt(MUL)
	S += t9_t0>=t9_t0_in

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	t9_t0_mem0 += INPUT_mem_r
	S += t9_t0_mem0 <= t9_t0

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	t9_t0_mem1 += alt(ADD_mem)
	S += (t50*ADD[0]) < t9_t0_mem1*ADD_mem[0]
	S += (t50*ADD[1]) < t9_t0_mem1*ADD_mem[1]
	S += (t50*ADD[2]) < t9_t0_mem1*ADD_mem[2]
	S += (t50*ADD[3]) < t9_t0_mem1*ADD_mem[3]
	S += t9_t0_mem1 <= t9_t0

	t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
	t9_t3 += alt(ADD)

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	t9_t3_mem0 += alt(ADD_mem)
	S += (t50*ADD[0]) < t9_t3_mem0*ADD_mem[0]
	S += (t50*ADD[1]) < t9_t3_mem0*ADD_mem[1]
	S += (t50*ADD[2]) < t9_t3_mem0*ADD_mem[2]
	S += (t50*ADD[3]) < t9_t3_mem0*ADD_mem[3]
	S += t9_t3_mem0 <= t9_t3

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	t9_t3_mem1 += alt(ADD_mem)
	S += (t51*ADD[0]) < t9_t3_mem1*ADD_mem[0]
	S += (t51*ADD[1]) < t9_t3_mem1*ADD_mem[1]
	S += (t51*ADD[2]) < t9_t3_mem1*ADD_mem[2]
	S += (t51*ADD[3]) < t9_t3_mem1*ADD_mem[3]
	S += t9_t3_mem1 <= t9_t3

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(ADD)

	S += 0<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(ADD_mem)
	S += (t161*ADD[0]) < c001_mem0*ADD_mem[0]
	S += (t161*ADD[1]) < c001_mem0*ADD_mem[1]
	S += (t161*ADD[2]) < c001_mem0*ADD_mem[2]
	S += (t161*ADD[3]) < c001_mem0*ADD_mem[3]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(ADD_mem)
	S += (t171*ADD[0]) < c001_mem1*ADD_mem[0]
	S += (t171*ADD[1]) < c001_mem1*ADD_mem[1]
	S += (t171*ADD[2]) < c001_mem1*ADD_mem[2]
	S += (t171*ADD[3]) < c001_mem1*ADD_mem[3]
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(INPUT_mem_w)
	S += c001 <= c001_w

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MUL_in)
	t6_t4 = S.Task('t6_t4', length=7, delay_cost=1)
	t6_t4 += alt(MUL)
	S += t6_t4>=t6_t4_in

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += alt(ADD_mem)
	S += (t6_t2*ADD[0]) < t6_t4_mem0*ADD_mem[0]
	S += (t6_t2*ADD[1]) < t6_t4_mem0*ADD_mem[1]
	S += (t6_t2*ADD[2]) < t6_t4_mem0*ADD_mem[2]
	S += (t6_t2*ADD[3]) < t6_t4_mem0*ADD_mem[3]
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += alt(ADD_mem)
	S += (t6_t3*ADD[0]) < t6_t4_mem1*ADD_mem[0]
	S += (t6_t3*ADD[1]) < t6_t4_mem1*ADD_mem[1]
	S += (t6_t3*ADD[2]) < t6_t4_mem1*ADD_mem[2]
	S += (t6_t3*ADD[3]) < t6_t4_mem1*ADD_mem[3]
	S += t6_t4_mem1 <= t6_t4

	t60 = S.Task('t60', length=1, delay_cost=1)
	t60 += alt(ADD)

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += alt(MUL_mem)
	S += (t6_t0*MUL[0]) < t60_mem0*MUL_mem[0]
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += alt(MUL_mem)
	S += (t6_t1*MUL[0]) < t60_mem1*MUL_mem[0]
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	t6_t5 += alt(ADD)

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += alt(MUL_mem)
	S += (t6_t0*MUL[0]) < t6_t5_mem0*MUL_mem[0]
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += alt(MUL_mem)
	S += (t6_t1*MUL[0]) < t6_t5_mem1*MUL_mem[0]
	S += t6_t5_mem1 <= t6_t5

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	t7_t4_in += alt(MUL_in)
	t7_t4 = S.Task('t7_t4', length=7, delay_cost=1)
	t7_t4 += alt(MUL)
	S += t7_t4>=t7_t4_in

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	t7_t4_mem0 += ADD_mem[0]
	S += 7 < t7_t4_mem0
	S += t7_t4_mem0 <= t7_t4

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	t7_t4_mem1 += alt(ADD_mem)
	S += (t7_t3*ADD[0]) < t7_t4_mem1*ADD_mem[0]
	S += (t7_t3*ADD[1]) < t7_t4_mem1*ADD_mem[1]
	S += (t7_t3*ADD[2]) < t7_t4_mem1*ADD_mem[2]
	S += (t7_t3*ADD[3]) < t7_t4_mem1*ADD_mem[3]
	S += t7_t4_mem1 <= t7_t4

	t70 = S.Task('t70', length=1, delay_cost=1)
	t70 += alt(ADD)

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += alt(MUL_mem)
	S += (t7_t0*MUL[0]) < t70_mem0*MUL_mem[0]
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += alt(MUL_mem)
	S += (t7_t1*MUL[0]) < t70_mem1*MUL_mem[0]
	S += t70_mem1 <= t70

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	t7_t5 += alt(ADD)

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += alt(MUL_mem)
	S += (t7_t0*MUL[0]) < t7_t5_mem0*MUL_mem[0]
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += alt(MUL_mem)
	S += (t7_t1*MUL[0]) < t7_t5_mem1*MUL_mem[0]
	S += t7_t5_mem1 <= t7_t5

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	t9_t4_in += alt(MUL_in)
	t9_t4 = S.Task('t9_t4', length=7, delay_cost=1)
	t9_t4 += alt(MUL)
	S += t9_t4>=t9_t4_in

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	t9_t4_mem0 += ADD_mem[0]
	S += 6 < t9_t4_mem0
	S += t9_t4_mem0 <= t9_t4

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	t9_t4_mem1 += alt(ADD_mem)
	S += (t9_t3*ADD[0]) < t9_t4_mem1*ADD_mem[0]
	S += (t9_t3*ADD[1]) < t9_t4_mem1*ADD_mem[1]
	S += (t9_t3*ADD[2]) < t9_t4_mem1*ADD_mem[2]
	S += (t9_t3*ADD[3]) < t9_t4_mem1*ADD_mem[3]
	S += t9_t4_mem1 <= t9_t4

	t90 = S.Task('t90', length=1, delay_cost=1)
	t90 += alt(ADD)

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += alt(MUL_mem)
	S += (t9_t0*MUL[0]) < t90_mem0*MUL_mem[0]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(MUL_mem)
	S += (t9_t1*MUL[0]) < t90_mem1*MUL_mem[0]
	S += t90_mem1 <= t90

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	t9_t5 += alt(ADD)

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += alt(MUL_mem)
	S += (t9_t0*MUL[0]) < t9_t5_mem0*MUL_mem[0]
	S += t9_t5_mem0 <= t9_t5

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	t9_t5_mem1 += alt(MUL_mem)
	S += (t9_t1*MUL[0]) < t9_t5_mem1*MUL_mem[0]
	S += t9_t5_mem1 <= t9_t5

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-381/scheduling/PADD_mul1_add4/PADD_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

