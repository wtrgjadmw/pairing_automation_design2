from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 115
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
	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 0
	t7_t1_in += MUL_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 0
	t7_t1_mem0 += INPUT_mem_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 0
	t7_t1_mem1 += INPUT_mem_r

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 1
	t7_t0_in += MUL_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 1
	t7_t0_mem0 += INPUT_mem_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 1
	t7_t0_mem1 += INPUT_mem_r

	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	S += t7_t1 >= 1
	t7_t1 += MUL[0]

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 2
	t3_t1_in += MUL_in[0]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 2
	t3_t1_mem0 += INPUT_mem_r

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 2
	t3_t1_mem1 += INPUT_mem_r

	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	S += t7_t0 >= 2
	t7_t0 += MUL[0]

	t3_t1 = S.Task('t3_t1', length=7, delay_cost=1)
	S += t3_t1 >= 3
	t3_t1 += MUL[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 3
	t5_t1_in += MUL_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 3
	t5_t1_mem0 += INPUT_mem_r

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 3
	t5_t1_mem1 += INPUT_mem_r

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 4
	t0_t3_in += MUL_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += INPUT_mem_r

	t5_t1 = S.Task('t5_t1', length=7, delay_cost=1)
	S += t5_t1 >= 4
	t5_t1 += MUL[0]

	t0_t3 = S.Task('t0_t3', length=7, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MUL[0]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 5
	t6_t0_in += MUL_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 5
	t6_t0_mem0 += INPUT_mem_r

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 5
	t6_t0_mem1 += INPUT_mem_r

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 6
	t3_t0_in += MUL_in[0]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 6
	t3_t0_mem0 += INPUT_mem_r

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 6
	t3_t0_mem1 += INPUT_mem_r

	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	S += t6_t0 >= 6
	t6_t0 += MUL[0]

	t3_t0 = S.Task('t3_t0', length=7, delay_cost=1)
	S += t3_t0 >= 7
	t3_t0 += MUL[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 7
	t6_t1_in += MUL_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 7
	t6_t1_mem0 += INPUT_mem_r

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 7
	t6_t1_mem1 += INPUT_mem_r

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 8
	t5_t0_in += MUL_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 8
	t5_t0_mem0 += INPUT_mem_r

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 8
	t5_t0_mem1 += INPUT_mem_r

	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	S += t6_t1 >= 8
	t6_t1 += MUL[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 9
	t4_t3_in += MUL_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 9
	t4_t3_mem0 += INPUT_mem_r

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 9
	t4_t3_mem1 += INPUT_mem_r

	t5_t0 = S.Task('t5_t0', length=7, delay_cost=1)
	S += t5_t0 >= 9
	t5_t0 += MUL[0]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 10
	t4_t1_mem0 += INPUT_mem_r

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 10
	t4_t1_mem1 += INPUT_mem_r

	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	S += t4_t3 >= 10
	t4_t3 += MUL[0]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 11
	t4_t1 += ADD[0]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 11
	t6_t2_mem0 += INPUT_mem_r

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 11
	t6_t2_mem1 += INPUT_mem_r

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 12
	t3_t3_mem0 += INPUT_mem_r

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 12
	t3_t3_mem1 += INPUT_mem_r

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 12
	t6_t2 += ADD[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 13
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 13
	t0_t0_mem1 += INPUT_mem_r

	t3_t3 = S.Task('t3_t3', length=1, delay_cost=1)
	S += t3_t3 >= 13
	t3_t3 += ADD[1]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 14
	t0_t0 += ADD[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 14
	t5_t2_mem0 += INPUT_mem_r

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 14
	t5_t2_mem1 += INPUT_mem_r

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 15
	t11_mem0 += INPUT_mem_r

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 15
	t11_mem1 += INPUT_mem_r

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 15
	t5_t2 += ADD[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 16
	t10_mem0 += INPUT_mem_r

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 16
	t10_mem1 += INPUT_mem_r

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 16
	t11 += ADD[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 17
	t10 += ADD[1]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 17
	t3_t2_mem0 += INPUT_mem_r

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 17
	t3_t2_mem1 += INPUT_mem_r

	t3_t2 = S.Task('t3_t2', length=1, delay_cost=1)
	S += t3_t2 >= 18
	t3_t2 += ADD[1]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 18
	t4_t0_mem0 += INPUT_mem_r

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 18
	t4_t0_mem1 += INPUT_mem_r

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 19
	t4_t0 += ADD[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 19
	t5_t3_mem0 += INPUT_mem_r

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 19
	t5_t3_mem1 += INPUT_mem_r

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 20
	t5_t3 += ADD[2]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 20
	t7_t3_mem0 += INPUT_mem_r

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 20
	t7_t3_mem1 += INPUT_mem_r

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 21
	t7_t2_mem0 += INPUT_mem_r

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 21
	t7_t2_mem1 += INPUT_mem_r

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 21
	t7_t3 += ADD[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 22
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 22
	t0_t1_mem1 += INPUT_mem_r

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 22
	t7_t2 += ADD[2]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 23
	t0_t1 += ADD[3]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 23
	t6_t3_mem0 += INPUT_mem_r

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 23
	t6_t3_mem1 += INPUT_mem_r

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 24
	t6_t3 += ADD[1]


	# new tasks
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MUL_in)
	t0_t2 = S.Task('t0_t2', length=7, delay_cost=1)
	t0_t2 += alt(MUL)
	S += t0_t2>=t0_t2_in

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += ADD_mem[1]
	S += 15 < t0_t2_mem0
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += ADD_mem[3]
	S += 24 < t0_t2_mem1
	S += t0_t2_mem1 <= t0_t2

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(ADD)

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MUL_mem[0]
	S += 12 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(ADD)

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MUL_mem[0]
	S += 12 < t01_mem0
	S += t01_mem0 <= t01

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(ADD)

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += ADD_mem[1]
	S += 18 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += INPUT_mem_r
	S += t20_mem1 <= t20

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(ADD)

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += ADD_mem[0]
	S += 17 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += INPUT_mem_r
	S += t21_mem1 <= t21

	t80 = S.Task('t80', length=1, delay_cost=1)
	t80 += alt(ADD)

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += ADD_mem[1]
	S += 18 < t80_mem0
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += INPUT_mem_r
	S += t80_mem1 <= t80

	t81 = S.Task('t81', length=1, delay_cost=1)
	t81 += alt(ADD)

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += ADD_mem[0]
	S += 17 < t81_mem0
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += INPUT_mem_r
	S += t81_mem1 <= t81

	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	t3_t4_in += alt(MUL_in)
	t3_t4 = S.Task('t3_t4', length=7, delay_cost=1)
	t3_t4 += alt(MUL)
	S += t3_t4>=t3_t4_in

	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	t3_t4_mem0 += ADD_mem[1]
	S += 19 < t3_t4_mem0
	S += t3_t4_mem0 <= t3_t4

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	t3_t4_mem1 += ADD_mem[1]
	S += 14 < t3_t4_mem1
	S += t3_t4_mem1 <= t3_t4

	t30 = S.Task('t30', length=1, delay_cost=1)
	t30 += alt(ADD)

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MUL_mem[0]
	S += 14 < t30_mem0
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += MUL_mem[0]
	S += 10 < t30_mem1
	S += t30_mem1 <= t30

	t3_t5 = S.Task('t3_t5', length=1, delay_cost=1)
	t3_t5 += alt(ADD)

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	t3_t5_mem0 += MUL_mem[0]
	S += 14 < t3_t5_mem0
	S += t3_t5_mem0 <= t3_t5

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	t3_t5_mem1 += MUL_mem[0]
	S += 10 < t3_t5_mem1
	S += t3_t5_mem1 <= t3_t5

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	t4_t2_in += alt(MUL_in)
	t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
	t4_t2 += alt(MUL)
	S += t4_t2>=t4_t2_in

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	t4_t2_mem0 += ADD_mem[1]
	S += 20 < t4_t2_mem0
	S += t4_t2_mem0 <= t4_t2

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	t4_t2_mem1 += ADD_mem[0]
	S += 12 < t4_t2_mem1
	S += t4_t2_mem1 <= t4_t2

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	t4_t5 += alt(ADD)

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	t4_t5_mem0 += MUL_mem[0]
	S += 17 < t4_t5_mem0
	S += t4_t5_mem0 <= t4_t5

	t41 = S.Task('t41', length=1, delay_cost=1)
	t41 += alt(ADD)

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += MUL_mem[0]
	S += 17 < t41_mem0
	S += t41_mem0 <= t41

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	t5_t4_in += alt(MUL_in)
	t5_t4 = S.Task('t5_t4', length=7, delay_cost=1)
	t5_t4 += alt(MUL)
	S += t5_t4>=t5_t4_in

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	t5_t4_mem0 += ADD_mem[0]
	S += 16 < t5_t4_mem0
	S += t5_t4_mem0 <= t5_t4

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	t5_t4_mem1 += ADD_mem[2]
	S += 21 < t5_t4_mem1
	S += t5_t4_mem1 <= t5_t4

	t50 = S.Task('t50', length=1, delay_cost=1)
	t50 += alt(ADD)

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += MUL_mem[0]
	S += 16 < t50_mem0
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += MUL_mem[0]
	S += 11 < t50_mem1
	S += t50_mem1 <= t50

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	t5_t5 += alt(ADD)

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += MUL_mem[0]
	S += 16 < t5_t5_mem0
	S += t5_t5_mem0 <= t5_t5

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	t5_t5_mem1 += MUL_mem[0]
	S += 11 < t5_t5_mem1
	S += t5_t5_mem1 <= t5_t5

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MUL_in)
	t6_t4 = S.Task('t6_t4', length=7, delay_cost=1)
	t6_t4 += alt(MUL)
	S += t6_t4>=t6_t4_in

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += ADD_mem[0]
	S += 13 < t6_t4_mem0
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += ADD_mem[1]
	S += 25 < t6_t4_mem1
	S += t6_t4_mem1 <= t6_t4

	t60 = S.Task('t60', length=1, delay_cost=1)
	t60 += alt(ADD)

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += MUL_mem[0]
	S += 13 < t60_mem0
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += MUL_mem[0]
	S += 15 < t60_mem1
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	t6_t5 += alt(ADD)

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += MUL_mem[0]
	S += 13 < t6_t5_mem0
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += MUL_mem[0]
	S += 15 < t6_t5_mem1
	S += t6_t5_mem1 <= t6_t5

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	t7_t4_in += alt(MUL_in)
	t7_t4 = S.Task('t7_t4', length=7, delay_cost=1)
	t7_t4 += alt(MUL)
	S += t7_t4>=t7_t4_in

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	t7_t4_mem0 += ADD_mem[2]
	S += 23 < t7_t4_mem0
	S += t7_t4_mem0 <= t7_t4

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	t7_t4_mem1 += ADD_mem[1]
	S += 22 < t7_t4_mem1
	S += t7_t4_mem1 <= t7_t4

	t70 = S.Task('t70', length=1, delay_cost=1)
	t70 += alt(ADD)

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += MUL_mem[0]
	S += 9 < t70_mem0
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += MUL_mem[0]
	S += 8 < t70_mem1
	S += t70_mem1 <= t70

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	t7_t5 += alt(ADD)

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += MUL_mem[0]
	S += 9 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += MUL_mem[0]
	S += 8 < t7_t5_mem1
	S += t7_t5_mem1 <= t7_t5

	t00 = S.Task('t00', length=1, delay_cost=1)
	t00 += alt(ADD)

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += alt(MUL_mem)
	S += (t0_t2*MUL[0]) < t00_mem0*MUL_mem[0]
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += alt(ADD_mem)
	S += (t0_t5*ADD[0]) < t00_mem1*ADD_mem[0]
	S += (t0_t5*ADD[1]) < t00_mem1*ADD_mem[1]
	S += (t0_t5*ADD[2]) < t00_mem1*ADD_mem[2]
	S += (t0_t5*ADD[3]) < t00_mem1*ADD_mem[3]
	S += t00_mem1 <= t00

	t9_t0 = S.Task('t9_t0', length=1, delay_cost=1)
	t9_t0 += alt(ADD)

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	t9_t0_mem0 += alt(ADD_mem)
	S += (t80*ADD[0]) < t9_t0_mem0*ADD_mem[0]
	S += (t80*ADD[1]) < t9_t0_mem0*ADD_mem[1]
	S += (t80*ADD[2]) < t9_t0_mem0*ADD_mem[2]
	S += (t80*ADD[3]) < t9_t0_mem0*ADD_mem[3]
	S += t9_t0_mem0 <= t9_t0

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	t9_t0_mem1 += alt(ADD_mem)
	S += (t81*ADD[0]) < t9_t0_mem1*ADD_mem[0]
	S += (t81*ADD[1]) < t9_t0_mem1*ADD_mem[1]
	S += (t81*ADD[2]) < t9_t0_mem1*ADD_mem[2]
	S += (t81*ADD[3]) < t9_t0_mem1*ADD_mem[3]
	S += t9_t0_mem1 <= t9_t0

	t9_t1 = S.Task('t9_t1', length=1, delay_cost=1)
	t9_t1 += alt(ADD)

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	t9_t1_mem0 += alt(ADD_mem)
	S += (t80*ADD[0]) < t9_t1_mem0*ADD_mem[0]
	S += (t80*ADD[1]) < t9_t1_mem0*ADD_mem[1]
	S += (t80*ADD[2]) < t9_t1_mem0*ADD_mem[2]
	S += (t80*ADD[3]) < t9_t1_mem0*ADD_mem[3]
	S += t9_t1_mem0 <= t9_t1

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	t9_t1_mem1 += alt(ADD_mem)
	S += (t81*ADD[0]) < t9_t1_mem1*ADD_mem[0]
	S += (t81*ADD[1]) < t9_t1_mem1*ADD_mem[1]
	S += (t81*ADD[2]) < t9_t1_mem1*ADD_mem[2]
	S += (t81*ADD[3]) < t9_t1_mem1*ADD_mem[3]
	S += t9_t1_mem1 <= t9_t1

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	t9_t3_in += alt(MUL_in)
	t9_t3 = S.Task('t9_t3', length=7, delay_cost=1)
	t9_t3 += alt(MUL)
	S += t9_t3>=t9_t3_in

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	t9_t3_mem0 += alt(ADD_mem)
	S += (t80*ADD[0]) < t9_t3_mem0*ADD_mem[0]
	S += (t80*ADD[1]) < t9_t3_mem0*ADD_mem[1]
	S += (t80*ADD[2]) < t9_t3_mem0*ADD_mem[2]
	S += (t80*ADD[3]) < t9_t3_mem0*ADD_mem[3]
	S += t9_t3_mem0 <= t9_t3

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	t9_t3_mem1 += alt(ADD_mem)
	S += (t81*ADD[0]) < t9_t3_mem1*ADD_mem[0]
	S += (t81*ADD[1]) < t9_t3_mem1*ADD_mem[1]
	S += (t81*ADD[2]) < t9_t3_mem1*ADD_mem[2]
	S += (t81*ADD[3]) < t9_t3_mem1*ADD_mem[3]
	S += t9_t3_mem1 <= t9_t3

	t10_t0 = S.Task('t10_t0', length=1, delay_cost=1)
	t10_t0 += alt(ADD)

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	t10_t0_mem0 += alt(ADD_mem)
	S += (t20*ADD[0]) < t10_t0_mem0*ADD_mem[0]
	S += (t20*ADD[1]) < t10_t0_mem0*ADD_mem[1]
	S += (t20*ADD[2]) < t10_t0_mem0*ADD_mem[2]
	S += (t20*ADD[3]) < t10_t0_mem0*ADD_mem[3]
	S += t10_t0_mem0 <= t10_t0

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	t10_t0_mem1 += alt(ADD_mem)
	S += (t21*ADD[0]) < t10_t0_mem1*ADD_mem[0]
	S += (t21*ADD[1]) < t10_t0_mem1*ADD_mem[1]
	S += (t21*ADD[2]) < t10_t0_mem1*ADD_mem[2]
	S += (t21*ADD[3]) < t10_t0_mem1*ADD_mem[3]
	S += t10_t0_mem1 <= t10_t0

	t10_t1 = S.Task('t10_t1', length=1, delay_cost=1)
	t10_t1 += alt(ADD)

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	t10_t1_mem0 += alt(ADD_mem)
	S += (t20*ADD[0]) < t10_t1_mem0*ADD_mem[0]
	S += (t20*ADD[1]) < t10_t1_mem0*ADD_mem[1]
	S += (t20*ADD[2]) < t10_t1_mem0*ADD_mem[2]
	S += (t20*ADD[3]) < t10_t1_mem0*ADD_mem[3]
	S += t10_t1_mem0 <= t10_t1

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	t10_t1_mem1 += alt(ADD_mem)
	S += (t21*ADD[0]) < t10_t1_mem1*ADD_mem[0]
	S += (t21*ADD[1]) < t10_t1_mem1*ADD_mem[1]
	S += (t21*ADD[2]) < t10_t1_mem1*ADD_mem[2]
	S += (t21*ADD[3]) < t10_t1_mem1*ADD_mem[3]
	S += t10_t1_mem1 <= t10_t1

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	t10_t3_in += alt(MUL_in)
	t10_t3 = S.Task('t10_t3', length=7, delay_cost=1)
	t10_t3 += alt(MUL)
	S += t10_t3>=t10_t3_in

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	t10_t3_mem0 += alt(ADD_mem)
	S += (t20*ADD[0]) < t10_t3_mem0*ADD_mem[0]
	S += (t20*ADD[1]) < t10_t3_mem0*ADD_mem[1]
	S += (t20*ADD[2]) < t10_t3_mem0*ADD_mem[2]
	S += (t20*ADD[3]) < t10_t3_mem0*ADD_mem[3]
	S += t10_t3_mem0 <= t10_t3

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	t10_t3_mem1 += alt(ADD_mem)
	S += (t21*ADD[0]) < t10_t3_mem1*ADD_mem[0]
	S += (t21*ADD[1]) < t10_t3_mem1*ADD_mem[1]
	S += (t21*ADD[2]) < t10_t3_mem1*ADD_mem[2]
	S += (t21*ADD[3]) < t10_t3_mem1*ADD_mem[3]
	S += t10_t3_mem1 <= t10_t3

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(ADD)

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MUL_mem)
	S += (t3_t4*MUL[0]) < t31_mem0*MUL_mem[0]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(ADD_mem)
	S += (t3_t5*ADD[0]) < t31_mem1*ADD_mem[0]
	S += (t3_t5*ADD[1]) < t31_mem1*ADD_mem[1]
	S += (t3_t5*ADD[2]) < t31_mem1*ADD_mem[2]
	S += (t3_t5*ADD[3]) < t31_mem1*ADD_mem[3]
	S += t31_mem1 <= t31

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(ADD)

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t110_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t110_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t110_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t110_mem0*ADD_mem[3]
	S += t110_mem0 <= t110

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

	t51 = S.Task('t51', length=1, delay_cost=1)
	t51 += alt(ADD)

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	t51_mem0 += alt(MUL_mem)
	S += (t5_t4*MUL[0]) < t51_mem0*MUL_mem[0]
	S += t51_mem0 <= t51

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	t51_mem1 += alt(ADD_mem)
	S += (t5_t5*ADD[0]) < t51_mem1*ADD_mem[0]
	S += (t5_t5*ADD[1]) < t51_mem1*ADD_mem[1]
	S += (t5_t5*ADD[2]) < t51_mem1*ADD_mem[2]
	S += (t5_t5*ADD[3]) < t51_mem1*ADD_mem[3]
	S += t51_mem1 <= t51

	t61 = S.Task('t61', length=1, delay_cost=1)
	t61 += alt(ADD)

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += alt(MUL_mem)
	S += (t6_t4*MUL[0]) < t61_mem0*MUL_mem[0]
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += alt(ADD_mem)
	S += (t6_t5*ADD[0]) < t61_mem1*ADD_mem[0]
	S += (t6_t5*ADD[1]) < t61_mem1*ADD_mem[1]
	S += (t6_t5*ADD[2]) < t61_mem1*ADD_mem[2]
	S += (t6_t5*ADD[3]) < t61_mem1*ADD_mem[3]
	S += t61_mem1 <= t61

	t71 = S.Task('t71', length=1, delay_cost=1)
	t71 += alt(ADD)

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += alt(MUL_mem)
	S += (t7_t4*MUL[0]) < t71_mem0*MUL_mem[0]
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += alt(ADD_mem)
	S += (t7_t5*ADD[0]) < t71_mem1*ADD_mem[0]
	S += (t7_t5*ADD[1]) < t71_mem1*ADD_mem[1]
	S += (t7_t5*ADD[2]) < t71_mem1*ADD_mem[2]
	S += (t7_t5*ADD[3]) < t71_mem1*ADD_mem[3]
	S += t71_mem1 <= t71

	t290 = S.Task('t290', length=1, delay_cost=1)
	t290 += alt(ADD)

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	t290_mem0 += alt(ADD_mem)
	S += (t50*ADD[0]) < t290_mem0*ADD_mem[0]
	S += (t50*ADD[1]) < t290_mem0*ADD_mem[1]
	S += (t50*ADD[2]) < t290_mem0*ADD_mem[2]
	S += (t50*ADD[3]) < t290_mem0*ADD_mem[3]
	S += t290_mem0 <= t290

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(ADD)

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(ADD_mem)
	S += (t01*ADD[0]) < t151_mem0*ADD_mem[0]
	S += (t01*ADD[1]) < t151_mem0*ADD_mem[1]
	S += (t01*ADD[2]) < t151_mem0*ADD_mem[2]
	S += (t01*ADD[3]) < t151_mem0*ADD_mem[3]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(ADD_mem)
	S += (t41*ADD[0]) < t151_mem1*ADD_mem[0]
	S += (t41*ADD[1]) < t151_mem1*ADD_mem[1]
	S += (t41*ADD[2]) < t151_mem1*ADD_mem[2]
	S += (t41*ADD[3]) < t151_mem1*ADD_mem[3]
	S += t151_mem1 <= t151

	t220 = S.Task('t220', length=1, delay_cost=1)
	t220 += alt(ADD)

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	t220_mem0 += alt(ADD_mem)
	S += (t60*ADD[0]) < t220_mem0*ADD_mem[0]
	S += (t60*ADD[1]) < t220_mem0*ADD_mem[1]
	S += (t60*ADD[2]) < t220_mem0*ADD_mem[2]
	S += (t60*ADD[3]) < t220_mem0*ADD_mem[3]
	S += t220_mem0 <= t220

	t260 = S.Task('t260', length=1, delay_cost=1)
	t260 += alt(ADD)

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	t260_mem0 += alt(ADD_mem)
	S += (t70*ADD[0]) < t260_mem0*ADD_mem[0]
	S += (t70*ADD[1]) < t260_mem0*ADD_mem[1]
	S += (t70*ADD[2]) < t260_mem0*ADD_mem[2]
	S += (t70*ADD[3]) < t260_mem0*ADD_mem[3]
	S += t260_mem0 <= t260

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	t9_t2_in += alt(MUL_in)
	t9_t2 = S.Task('t9_t2', length=7, delay_cost=1)
	t9_t2 += alt(MUL)
	S += t9_t2>=t9_t2_in

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	t9_t2_mem0 += alt(ADD_mem)
	S += (t9_t0*ADD[0]) < t9_t2_mem0*ADD_mem[0]
	S += (t9_t0*ADD[1]) < t9_t2_mem0*ADD_mem[1]
	S += (t9_t0*ADD[2]) < t9_t2_mem0*ADD_mem[2]
	S += (t9_t0*ADD[3]) < t9_t2_mem0*ADD_mem[3]
	S += t9_t2_mem0 <= t9_t2

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	t9_t2_mem1 += alt(ADD_mem)
	S += (t9_t1*ADD[0]) < t9_t2_mem1*ADD_mem[0]
	S += (t9_t1*ADD[1]) < t9_t2_mem1*ADD_mem[1]
	S += (t9_t1*ADD[2]) < t9_t2_mem1*ADD_mem[2]
	S += (t9_t1*ADD[3]) < t9_t2_mem1*ADD_mem[3]
	S += t9_t2_mem1 <= t9_t2

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	t9_t5 += alt(ADD)

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += alt(MUL_mem)
	S += (t9_t3*MUL[0]) < t9_t5_mem0*MUL_mem[0]
	S += t9_t5_mem0 <= t9_t5

	t91 = S.Task('t91', length=1, delay_cost=1)
	t91 += alt(ADD)

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += alt(MUL_mem)
	S += (t9_t3*MUL[0]) < t91_mem0*MUL_mem[0]
	S += t91_mem0 <= t91

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	t10_t2_in += alt(MUL_in)
	t10_t2 = S.Task('t10_t2', length=7, delay_cost=1)
	t10_t2 += alt(MUL)
	S += t10_t2>=t10_t2_in

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	t10_t2_mem0 += alt(ADD_mem)
	S += (t10_t0*ADD[0]) < t10_t2_mem0*ADD_mem[0]
	S += (t10_t0*ADD[1]) < t10_t2_mem0*ADD_mem[1]
	S += (t10_t0*ADD[2]) < t10_t2_mem0*ADD_mem[2]
	S += (t10_t0*ADD[3]) < t10_t2_mem0*ADD_mem[3]
	S += t10_t2_mem0 <= t10_t2

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	t10_t2_mem1 += alt(ADD_mem)
	S += (t10_t1*ADD[0]) < t10_t2_mem1*ADD_mem[0]
	S += (t10_t1*ADD[1]) < t10_t2_mem1*ADD_mem[1]
	S += (t10_t1*ADD[2]) < t10_t2_mem1*ADD_mem[2]
	S += (t10_t1*ADD[3]) < t10_t2_mem1*ADD_mem[3]
	S += t10_t2_mem1 <= t10_t2

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	t10_t5 += alt(ADD)

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	t10_t5_mem0 += alt(MUL_mem)
	S += (t10_t3*MUL[0]) < t10_t5_mem0*MUL_mem[0]
	S += t10_t5_mem0 <= t10_t5

	t101 = S.Task('t101', length=1, delay_cost=1)
	t101 += alt(ADD)

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += alt(MUL_mem)
	S += (t10_t3*MUL[0]) < t101_mem0*MUL_mem[0]
	S += t101_mem0 <= t101

	t111 = S.Task('t111', length=1, delay_cost=1)
	t111 += alt(ADD)

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(ADD_mem)
	S += (t31*ADD[0]) < t111_mem0*ADD_mem[0]
	S += (t31*ADD[1]) < t111_mem0*ADD_mem[1]
	S += (t31*ADD[2]) < t111_mem0*ADD_mem[2]
	S += (t31*ADD[3]) < t111_mem0*ADD_mem[3]
	S += t111_mem0 <= t111

	t291 = S.Task('t291', length=1, delay_cost=1)
	t291 += alt(ADD)

	t291_mem0 = S.Task('t291_mem0', length=1, delay_cost=1)
	t291_mem0 += alt(ADD_mem)
	S += (t51*ADD[0]) < t291_mem0*ADD_mem[0]
	S += (t51*ADD[1]) < t291_mem0*ADD_mem[1]
	S += (t51*ADD[2]) < t291_mem0*ADD_mem[2]
	S += (t51*ADD[3]) < t291_mem0*ADD_mem[3]
	S += t291_mem0 <= t291

	t300 = S.Task('t300', length=1, delay_cost=1)
	t300 += alt(ADD)

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	t300_mem0 += alt(ADD_mem)
	S += (t290*ADD[0]) < t300_mem0*ADD_mem[0]
	S += (t290*ADD[1]) < t300_mem0*ADD_mem[1]
	S += (t290*ADD[2]) < t300_mem0*ADD_mem[2]
	S += (t290*ADD[3]) < t300_mem0*ADD_mem[3]
	S += t300_mem0 <= t300

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	t300_mem1 += alt(ADD_mem)
	S += (t50*ADD[0]) < t300_mem1*ADD_mem[0]
	S += (t50*ADD[1]) < t300_mem1*ADD_mem[1]
	S += (t50*ADD[2]) < t300_mem1*ADD_mem[2]
	S += (t50*ADD[3]) < t300_mem1*ADD_mem[3]
	S += t300_mem1 <= t300

	t150 = S.Task('t150', length=1, delay_cost=1)
	t150 += alt(ADD)

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t150_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t150_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t150_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t150_mem0*ADD_mem[3]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(ADD_mem)
	S += (t40*ADD[0]) < t150_mem1*ADD_mem[0]
	S += (t40*ADD[1]) < t150_mem1*ADD_mem[1]
	S += (t40*ADD[2]) < t150_mem1*ADD_mem[2]
	S += (t40*ADD[3]) < t150_mem1*ADD_mem[3]
	S += t150_mem1 <= t150

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(ADD)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += alt(ADD_mem)
	S += (t151*ADD[0]) < t161_mem0*ADD_mem[0]
	S += (t151*ADD[1]) < t161_mem0*ADD_mem[1]
	S += (t151*ADD[2]) < t161_mem0*ADD_mem[2]
	S += (t151*ADD[3]) < t161_mem0*ADD_mem[3]
	S += t161_mem0 <= t161

	t180 = S.Task('t180', length=1, delay_cost=1)
	t180 += alt(ADD)

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	t180_mem0 += alt(ADD_mem)
	S += (t40*ADD[0]) < t180_mem0*ADD_mem[0]
	S += (t40*ADD[1]) < t180_mem0*ADD_mem[1]
	S += (t40*ADD[2]) < t180_mem0*ADD_mem[2]
	S += (t40*ADD[3]) < t180_mem0*ADD_mem[3]
	S += t180_mem0 <= t180

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	t180_mem1 += alt(ADD_mem)
	S += (t41*ADD[0]) < t180_mem1*ADD_mem[0]
	S += (t41*ADD[1]) < t180_mem1*ADD_mem[1]
	S += (t41*ADD[2]) < t180_mem1*ADD_mem[2]
	S += (t41*ADD[3]) < t180_mem1*ADD_mem[3]
	S += t180_mem1 <= t180

	t181 = S.Task('t181', length=1, delay_cost=1)
	t181 += alt(ADD)

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	t181_mem0 += alt(ADD_mem)
	S += (t41*ADD[0]) < t181_mem0*ADD_mem[0]
	S += (t41*ADD[1]) < t181_mem0*ADD_mem[1]
	S += (t41*ADD[2]) < t181_mem0*ADD_mem[2]
	S += (t41*ADD[3]) < t181_mem0*ADD_mem[3]
	S += t181_mem0 <= t181

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	t181_mem1 += alt(ADD_mem)
	S += (t40*ADD[0]) < t181_mem1*ADD_mem[0]
	S += (t40*ADD[1]) < t181_mem1*ADD_mem[1]
	S += (t40*ADD[2]) < t181_mem1*ADD_mem[2]
	S += (t40*ADD[3]) < t181_mem1*ADD_mem[3]
	S += t181_mem1 <= t181

	t221 = S.Task('t221', length=1, delay_cost=1)
	t221 += alt(ADD)

	t221_mem0 = S.Task('t221_mem0', length=1, delay_cost=1)
	t221_mem0 += alt(ADD_mem)
	S += (t61*ADD[0]) < t221_mem0*ADD_mem[0]
	S += (t61*ADD[1]) < t221_mem0*ADD_mem[1]
	S += (t61*ADD[2]) < t221_mem0*ADD_mem[2]
	S += (t61*ADD[3]) < t221_mem0*ADD_mem[3]
	S += t221_mem0 <= t221

	t230 = S.Task('t230', length=1, delay_cost=1)
	t230 += alt(ADD)

	t230_mem0 = S.Task('t230_mem0', length=1, delay_cost=1)
	t230_mem0 += alt(ADD_mem)
	S += (t220*ADD[0]) < t230_mem0*ADD_mem[0]
	S += (t220*ADD[1]) < t230_mem0*ADD_mem[1]
	S += (t220*ADD[2]) < t230_mem0*ADD_mem[2]
	S += (t220*ADD[3]) < t230_mem0*ADD_mem[3]
	S += t230_mem0 <= t230

	t230_mem1 = S.Task('t230_mem1', length=1, delay_cost=1)
	t230_mem1 += alt(ADD_mem)
	S += (t60*ADD[0]) < t230_mem1*ADD_mem[0]
	S += (t60*ADD[1]) < t230_mem1*ADD_mem[1]
	S += (t60*ADD[2]) < t230_mem1*ADD_mem[2]
	S += (t60*ADD[3]) < t230_mem1*ADD_mem[3]
	S += t230_mem1 <= t230

	t261 = S.Task('t261', length=1, delay_cost=1)
	t261 += alt(ADD)

	t261_mem0 = S.Task('t261_mem0', length=1, delay_cost=1)
	t261_mem0 += alt(ADD_mem)
	S += (t71*ADD[0]) < t261_mem0*ADD_mem[0]
	S += (t71*ADD[1]) < t261_mem0*ADD_mem[1]
	S += (t71*ADD[2]) < t261_mem0*ADD_mem[2]
	S += (t71*ADD[3]) < t261_mem0*ADD_mem[3]
	S += t261_mem0 <= t261

	t270 = S.Task('t270', length=1, delay_cost=1)
	t270 += alt(ADD)

	t270_mem0 = S.Task('t270_mem0', length=1, delay_cost=1)
	t270_mem0 += alt(ADD_mem)
	S += (t260*ADD[0]) < t270_mem0*ADD_mem[0]
	S += (t260*ADD[1]) < t270_mem0*ADD_mem[1]
	S += (t260*ADD[2]) < t270_mem0*ADD_mem[2]
	S += (t260*ADD[3]) < t270_mem0*ADD_mem[3]
	S += t270_mem0 <= t270

	t270_mem1 = S.Task('t270_mem1', length=1, delay_cost=1)
	t270_mem1 += alt(ADD_mem)
	S += (t70*ADD[0]) < t270_mem1*ADD_mem[0]
	S += (t70*ADD[1]) < t270_mem1*ADD_mem[1]
	S += (t70*ADD[2]) < t270_mem1*ADD_mem[2]
	S += (t70*ADD[3]) < t270_mem1*ADD_mem[3]
	S += t270_mem1 <= t270

	t90 = S.Task('t90', length=1, delay_cost=1)
	t90 += alt(ADD)

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += alt(MUL_mem)
	S += (t9_t2*MUL[0]) < t90_mem0*MUL_mem[0]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(ADD_mem)
	S += (t9_t5*ADD[0]) < t90_mem1*ADD_mem[0]
	S += (t9_t5*ADD[1]) < t90_mem1*ADD_mem[1]
	S += (t9_t5*ADD[2]) < t90_mem1*ADD_mem[2]
	S += (t9_t5*ADD[3]) < t90_mem1*ADD_mem[3]
	S += t90_mem1 <= t90

	t100 = S.Task('t100', length=1, delay_cost=1)
	t100 += alt(ADD)

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += alt(MUL_mem)
	S += (t10_t2*MUL[0]) < t100_mem0*MUL_mem[0]
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += alt(ADD_mem)
	S += (t10_t5*ADD[0]) < t100_mem1*ADD_mem[0]
	S += (t10_t5*ADD[1]) < t100_mem1*ADD_mem[1]
	S += (t10_t5*ADD[2]) < t100_mem1*ADD_mem[2]
	S += (t10_t5*ADD[3]) < t100_mem1*ADD_mem[3]
	S += t100_mem1 <= t100

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
	t120_mem1 += alt(ADD_mem)
	S += (t111*ADD[0]) < t120_mem1*ADD_mem[0]
	S += (t111*ADD[1]) < t120_mem1*ADD_mem[1]
	S += (t111*ADD[2]) < t120_mem1*ADD_mem[2]
	S += (t111*ADD[3]) < t120_mem1*ADD_mem[3]
	S += t120_mem1 <= t120

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
	S += (t110*ADD[0]) < t121_mem1*ADD_mem[0]
	S += (t110*ADD[1]) < t121_mem1*ADD_mem[1]
	S += (t110*ADD[2]) < t121_mem1*ADD_mem[2]
	S += (t110*ADD[3]) < t121_mem1*ADD_mem[3]
	S += t121_mem1 <= t121

	t301 = S.Task('t301', length=1, delay_cost=1)
	t301 += alt(ADD)

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	t301_mem0 += alt(ADD_mem)
	S += (t291*ADD[0]) < t301_mem0*ADD_mem[0]
	S += (t291*ADD[1]) < t301_mem0*ADD_mem[1]
	S += (t291*ADD[2]) < t301_mem0*ADD_mem[2]
	S += (t291*ADD[3]) < t301_mem0*ADD_mem[3]
	S += t301_mem0 <= t301

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	t301_mem1 += alt(ADD_mem)
	S += (t51*ADD[0]) < t301_mem1*ADD_mem[0]
	S += (t51*ADD[1]) < t301_mem1*ADD_mem[1]
	S += (t51*ADD[2]) < t301_mem1*ADD_mem[2]
	S += (t51*ADD[3]) < t301_mem1*ADD_mem[3]
	S += t301_mem1 <= t301

	t310 = S.Task('t310', length=1, delay_cost=1)
	t310 += alt(ADD)

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	t310_mem0 += alt(ADD_mem)
	S += (t300*ADD[0]) < t310_mem0*ADD_mem[0]
	S += (t300*ADD[1]) < t310_mem0*ADD_mem[1]
	S += (t300*ADD[2]) < t310_mem0*ADD_mem[2]
	S += (t300*ADD[3]) < t310_mem0*ADD_mem[3]
	S += t310_mem0 <= t310

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	t310_mem1 += INPUT_mem_r
	S += t310_mem1 <= t310

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(ADD)

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += alt(ADD_mem)
	S += (t150*ADD[0]) < t160_mem0*ADD_mem[0]
	S += (t150*ADD[1]) < t160_mem0*ADD_mem[1]
	S += (t150*ADD[2]) < t160_mem0*ADD_mem[2]
	S += (t150*ADD[3]) < t160_mem0*ADD_mem[3]
	S += t160_mem0 <= t160

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(ADD)

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(ADD_mem)
	S += (t91*ADD[0]) < t171_mem0*ADD_mem[0]
	S += (t91*ADD[1]) < t171_mem0*ADD_mem[1]
	S += (t91*ADD[2]) < t171_mem0*ADD_mem[2]
	S += (t91*ADD[3]) < t171_mem0*ADD_mem[3]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(ADD_mem)
	S += (t161*ADD[0]) < t171_mem1*ADD_mem[0]
	S += (t161*ADD[1]) < t171_mem1*ADD_mem[1]
	S += (t161*ADD[2]) < t171_mem1*ADD_mem[2]
	S += (t161*ADD[3]) < t171_mem1*ADD_mem[3]
	S += t171_mem1 <= t171

	t190 = S.Task('t190', length=1, delay_cost=1)
	t190 += alt(ADD)

	t190_mem0 = S.Task('t190_mem0', length=1, delay_cost=1)
	t190_mem0 += alt(ADD_mem)
	S += (t180*ADD[0]) < t190_mem0*ADD_mem[0]
	S += (t180*ADD[1]) < t190_mem0*ADD_mem[1]
	S += (t180*ADD[2]) < t190_mem0*ADD_mem[2]
	S += (t180*ADD[3]) < t190_mem0*ADD_mem[3]
	S += t190_mem0 <= t190

	t190_mem1 = S.Task('t190_mem1', length=1, delay_cost=1)
	t190_mem1 += alt(ADD_mem)
	S += (t110*ADD[0]) < t190_mem1*ADD_mem[0]
	S += (t110*ADD[1]) < t190_mem1*ADD_mem[1]
	S += (t110*ADD[2]) < t190_mem1*ADD_mem[2]
	S += (t110*ADD[3]) < t190_mem1*ADD_mem[3]
	S += t190_mem1 <= t190

	t191 = S.Task('t191', length=1, delay_cost=1)
	t191 += alt(ADD)

	t191_mem0 = S.Task('t191_mem0', length=1, delay_cost=1)
	t191_mem0 += alt(ADD_mem)
	S += (t181*ADD[0]) < t191_mem0*ADD_mem[0]
	S += (t181*ADD[1]) < t191_mem0*ADD_mem[1]
	S += (t181*ADD[2]) < t191_mem0*ADD_mem[2]
	S += (t181*ADD[3]) < t191_mem0*ADD_mem[3]
	S += t191_mem0 <= t191

	t191_mem1 = S.Task('t191_mem1', length=1, delay_cost=1)
	t191_mem1 += alt(ADD_mem)
	S += (t111*ADD[0]) < t191_mem1*ADD_mem[0]
	S += (t111*ADD[1]) < t191_mem1*ADD_mem[1]
	S += (t111*ADD[2]) < t191_mem1*ADD_mem[2]
	S += (t111*ADD[3]) < t191_mem1*ADD_mem[3]
	S += t191_mem1 <= t191

	t231 = S.Task('t231', length=1, delay_cost=1)
	t231 += alt(ADD)

	t231_mem0 = S.Task('t231_mem0', length=1, delay_cost=1)
	t231_mem0 += alt(ADD_mem)
	S += (t221*ADD[0]) < t231_mem0*ADD_mem[0]
	S += (t221*ADD[1]) < t231_mem0*ADD_mem[1]
	S += (t221*ADD[2]) < t231_mem0*ADD_mem[2]
	S += (t221*ADD[3]) < t231_mem0*ADD_mem[3]
	S += t231_mem0 <= t231

	t231_mem1 = S.Task('t231_mem1', length=1, delay_cost=1)
	t231_mem1 += alt(ADD_mem)
	S += (t61*ADD[0]) < t231_mem1*ADD_mem[0]
	S += (t61*ADD[1]) < t231_mem1*ADD_mem[1]
	S += (t61*ADD[2]) < t231_mem1*ADD_mem[2]
	S += (t61*ADD[3]) < t231_mem1*ADD_mem[3]
	S += t231_mem1 <= t231

	t271 = S.Task('t271', length=1, delay_cost=1)
	t271 += alt(ADD)

	t271_mem0 = S.Task('t271_mem0', length=1, delay_cost=1)
	t271_mem0 += alt(ADD_mem)
	S += (t261*ADD[0]) < t271_mem0*ADD_mem[0]
	S += (t261*ADD[1]) < t271_mem0*ADD_mem[1]
	S += (t261*ADD[2]) < t271_mem0*ADD_mem[2]
	S += (t261*ADD[3]) < t271_mem0*ADD_mem[3]
	S += t271_mem0 <= t271

	t271_mem1 = S.Task('t271_mem1', length=1, delay_cost=1)
	t271_mem1 += alt(ADD_mem)
	S += (t71*ADD[0]) < t271_mem1*ADD_mem[0]
	S += (t71*ADD[1]) < t271_mem1*ADD_mem[1]
	S += (t71*ADD[2]) < t271_mem1*ADD_mem[2]
	S += (t71*ADD[3]) < t271_mem1*ADD_mem[3]
	S += t271_mem1 <= t271

	t280 = S.Task('t280', length=1, delay_cost=1)
	t280 += alt(ADD)

	t280_mem0 = S.Task('t280_mem0', length=1, delay_cost=1)
	t280_mem0 += alt(ADD_mem)
	S += (t270*ADD[0]) < t280_mem0*ADD_mem[0]
	S += (t270*ADD[1]) < t280_mem0*ADD_mem[1]
	S += (t270*ADD[2]) < t280_mem0*ADD_mem[2]
	S += (t270*ADD[3]) < t280_mem0*ADD_mem[3]
	S += t280_mem0 <= t280

	t280_mem1 = S.Task('t280_mem1', length=1, delay_cost=1)
	t280_mem1 += INPUT_mem_r
	S += t280_mem1 <= t280

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-440/scheduling/SQR012345_mul1_add4/SQR012345_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

