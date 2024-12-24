from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 109
	S = Scenario("PDBL_1", horizon=horizon)

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
	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 0
	t10_t1_in += MUL_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 0
	t10_t1_mem0 += INPUT_mem_r

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 0
	t10_t1_mem1 += INPUT_mem_r

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 1
	t10_t0_in += MUL_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 1
	t10_t0_mem0 += INPUT_mem_r

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 1
	t10_t0_mem1 += INPUT_mem_r

	t10_t1 = S.Task('t10_t1', length=7, delay_cost=1)
	S += t10_t1 >= 1
	t10_t1 += MUL[0]

	t10_t0 = S.Task('t10_t0', length=7, delay_cost=1)
	S += t10_t0 >= 2
	t10_t0 += MUL[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 2
	t1_t3_in += MUL_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 2
	t1_t3_mem0 += INPUT_mem_r

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 2
	t1_t3_mem1 += INPUT_mem_r

	t1_t3 = S.Task('t1_t3', length=7, delay_cost=1)
	S += t1_t3 >= 3
	t1_t3 += MUL[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 3
	t5_t1_in += MUL_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 3
	t5_t1_mem0 += INPUT_mem_r

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 3
	t5_t1_mem1 += INPUT_mem_r

	t5_t1 = S.Task('t5_t1', length=7, delay_cost=1)
	S += t5_t1 >= 4
	t5_t1 += MUL[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 4
	t7_t3_in += MUL_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 4
	t7_t3_mem0 += INPUT_mem_r

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 4
	t7_t3_mem1 += INPUT_mem_r

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 5
	t5_t0_in += MUL_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 5
	t5_t0_mem0 += INPUT_mem_r

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 5
	t5_t0_mem1 += INPUT_mem_r

	t7_t3 = S.Task('t7_t3', length=7, delay_cost=1)
	S += t7_t3 >= 5
	t7_t3 += MUL[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 6
	t0_t3_in += MUL_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += INPUT_mem_r

	t5_t0 = S.Task('t5_t0', length=7, delay_cost=1)
	S += t5_t0 >= 6
	t5_t0 += MUL[0]

	t0_t3 = S.Task('t0_t3', length=7, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MUL[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 7
	t2_t2_mem0 += INPUT_mem_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 7
	t2_t2_mem1 += INPUT_mem_r

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 8
	t2_t2 += ADD[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 8
	t5_t3_mem0 += INPUT_mem_r

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 8
	t5_t3_mem1 += INPUT_mem_r

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 9
	t5_t2_mem0 += INPUT_mem_r

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 9
	t5_t2_mem1 += INPUT_mem_r

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 9
	t5_t3 += ADD[0]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 10
	t5_t2 += ADD[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 10
	t7_t0_mem0 += INPUT_mem_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 10
	t7_t0_mem1 += INPUT_mem_r

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 11
	t1_t1_mem0 += INPUT_mem_r

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 11
	t1_t1_mem1 += INPUT_mem_r

	t7_t0 = S.Task('t7_t0', length=1, delay_cost=1)
	S += t7_t0 >= 11
	t7_t0 += ADD[1]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 12
	t10_t2_mem0 += INPUT_mem_r

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 12
	t10_t2_mem1 += INPUT_mem_r

	t1_t1 = S.Task('t1_t1', length=1, delay_cost=1)
	S += t1_t1 >= 12
	t1_t1 += ADD[0]

	t10_t2 = S.Task('t10_t2', length=1, delay_cost=1)
	S += t10_t2 >= 13
	t10_t2 += ADD[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 13
	t1_t0_mem0 += INPUT_mem_r

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 13
	t1_t0_mem1 += INPUT_mem_r

	t1_t0 = S.Task('t1_t0', length=1, delay_cost=1)
	S += t1_t0 >= 14
	t1_t0 += ADD[2]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 14
	t7_t1_mem0 += INPUT_mem_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 14
	t7_t1_mem1 += INPUT_mem_r

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 15
	t10_t3_mem0 += INPUT_mem_r

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 15
	t10_t3_mem1 += INPUT_mem_r

	t7_t1 = S.Task('t7_t1', length=1, delay_cost=1)
	S += t7_t1 >= 15
	t7_t1 += ADD[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 16
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 16
	t0_t0_mem1 += INPUT_mem_r

	t10_t3 = S.Task('t10_t3', length=1, delay_cost=1)
	S += t10_t3 >= 16
	t10_t3 += ADD[2]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 17
	t0_t0 += ADD[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 17
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 17
	t0_t1_mem1 += INPUT_mem_r

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 18
	t0_t1 += ADD[1]


	# new tasks
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MUL_in)
	t0_t2 = S.Task('t0_t2', length=7, delay_cost=1)
	t0_t2 += alt(MUL)
	S += t0_t2>=t0_t2_in

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += ADD_mem[0]
	S += 17 < t0_t2_mem0
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += ADD_mem[1]
	S += 18 < t0_t2_mem1
	S += t0_t2_mem1 <= t0_t2

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(ADD)

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MUL_mem[0]
	S += 13 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(ADD)

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MUL_mem[0]
	S += 13 < t01_mem0
	S += t01_mem0 <= t01

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	t1_t2_in += alt(MUL_in)
	t1_t2 = S.Task('t1_t2', length=7, delay_cost=1)
	t1_t2 += alt(MUL)
	S += t1_t2>=t1_t2_in

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	t1_t2_mem0 += ADD_mem[2]
	S += 14 < t1_t2_mem0
	S += t1_t2_mem0 <= t1_t2

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	t1_t2_mem1 += ADD_mem[0]
	S += 12 < t1_t2_mem1
	S += t1_t2_mem1 <= t1_t2

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	t1_t5 += alt(ADD)

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	t1_t5_mem0 += MUL_mem[0]
	S += 9 < t1_t5_mem0
	S += t1_t5_mem0 <= t1_t5

	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(ADD)

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MUL_mem[0]
	S += 9 < t11_mem0
	S += t11_mem0 <= t11

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	t5_t4_in += alt(MUL_in)
	t5_t4 = S.Task('t5_t4', length=7, delay_cost=1)
	t5_t4 += alt(MUL)
	S += t5_t4>=t5_t4_in

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	t5_t4_mem0 += ADD_mem[0]
	S += 10 < t5_t4_mem0
	S += t5_t4_mem0 <= t5_t4

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	t5_t4_mem1 += ADD_mem[0]
	S += 9 < t5_t4_mem1
	S += t5_t4_mem1 <= t5_t4

	t50 = S.Task('t50', length=1, delay_cost=1)
	t50 += alt(ADD)

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += MUL_mem[0]
	S += 12 < t50_mem0
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += MUL_mem[0]
	S += 10 < t50_mem1
	S += t50_mem1 <= t50

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	t5_t5 += alt(ADD)

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += MUL_mem[0]
	S += 12 < t5_t5_mem0
	S += t5_t5_mem0 <= t5_t5

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	t5_t5_mem1 += MUL_mem[0]
	S += 10 < t5_t5_mem1
	S += t5_t5_mem1 <= t5_t5

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	t7_t2_in += alt(MUL_in)
	t7_t2 = S.Task('t7_t2', length=7, delay_cost=1)
	t7_t2 += alt(MUL)
	S += t7_t2>=t7_t2_in

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	t7_t2_mem0 += ADD_mem[1]
	S += 11 < t7_t2_mem0
	S += t7_t2_mem0 <= t7_t2

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	t7_t2_mem1 += ADD_mem[0]
	S += 15 < t7_t2_mem1
	S += t7_t2_mem1 <= t7_t2

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	t7_t5 += alt(ADD)

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += MUL_mem[0]
	S += 11 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t71 = S.Task('t71', length=1, delay_cost=1)
	t71 += alt(ADD)

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += MUL_mem[0]
	S += 11 < t71_mem0
	S += t71_mem0 <= t71

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	t10_t4_in += alt(MUL_in)
	t10_t4 = S.Task('t10_t4', length=7, delay_cost=1)
	t10_t4 += alt(MUL)
	S += t10_t4>=t10_t4_in

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	t10_t4_mem0 += ADD_mem[0]
	S += 13 < t10_t4_mem0
	S += t10_t4_mem0 <= t10_t4

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	t10_t4_mem1 += ADD_mem[2]
	S += 16 < t10_t4_mem1
	S += t10_t4_mem1 <= t10_t4

	t100 = S.Task('t100', length=1, delay_cost=1)
	t100 += alt(ADD)

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += MUL_mem[0]
	S += 8 < t100_mem0
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += MUL_mem[0]
	S += 7 < t100_mem1
	S += t100_mem1 <= t100

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	t10_t5 += alt(ADD)

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	t10_t5_mem0 += MUL_mem[0]
	S += 8 < t10_t5_mem0
	S += t10_t5_mem0 <= t10_t5

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	t10_t5_mem1 += MUL_mem[0]
	S += 7 < t10_t5_mem1
	S += t10_t5_mem1 <= t10_t5

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

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(ADD)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += alt(MUL_mem)
	S += (t1_t2*MUL[0]) < t10_mem0*MUL_mem[0]
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(ADD_mem)
	S += (t1_t5*ADD[0]) < t10_mem1*ADD_mem[0]
	S += (t1_t5*ADD[1]) < t10_mem1*ADD_mem[1]
	S += (t1_t5*ADD[2]) < t10_mem1*ADD_mem[2]
	S += (t1_t5*ADD[3]) < t10_mem1*ADD_mem[3]
	S += t10_mem1 <= t10

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	t2_t1_in += alt(MUL_in)
	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	t2_t1 += alt(MUL)
	S += t2_t1>=t2_t1_in

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	t2_t1_mem0 += INPUT_mem_r
	S += t2_t1_mem0 <= t2_t1

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	t2_t1_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t2_t1_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t2_t1_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t2_t1_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t2_t1_mem1*ADD_mem[3]
	S += t2_t1_mem1 <= t2_t1

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

	t60 = S.Task('t60', length=1, delay_cost=1)
	t60 += alt(ADD)

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += alt(ADD_mem)
	S += (t50*ADD[0]) < t60_mem0*ADD_mem[0]
	S += (t50*ADD[1]) < t60_mem0*ADD_mem[1]
	S += (t50*ADD[2]) < t60_mem0*ADD_mem[2]
	S += (t50*ADD[3]) < t60_mem0*ADD_mem[3]
	S += t60_mem0 <= t60

	t70 = S.Task('t70', length=1, delay_cost=1)
	t70 += alt(ADD)

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += alt(MUL_mem)
	S += (t7_t2*MUL[0]) < t70_mem0*MUL_mem[0]
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += alt(ADD_mem)
	S += (t7_t5*ADD[0]) < t70_mem1*ADD_mem[0]
	S += (t7_t5*ADD[1]) < t70_mem1*ADD_mem[1]
	S += (t7_t5*ADD[2]) < t70_mem1*ADD_mem[2]
	S += (t7_t5*ADD[3]) < t70_mem1*ADD_mem[3]
	S += t70_mem1 <= t70

	t81 = S.Task('t81', length=1, delay_cost=1)
	t81 += alt(ADD)

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += alt(ADD_mem)
	S += (t71*ADD[0]) < t81_mem0*ADD_mem[0]
	S += (t71*ADD[1]) < t81_mem0*ADD_mem[1]
	S += (t71*ADD[2]) < t81_mem0*ADD_mem[2]
	S += (t71*ADD[3]) < t81_mem0*ADD_mem[3]
	S += t81_mem0 <= t81

	t101 = S.Task('t101', length=1, delay_cost=1)
	t101 += alt(ADD)

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += alt(MUL_mem)
	S += (t10_t4*MUL[0]) < t101_mem0*MUL_mem[0]
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += alt(ADD_mem)
	S += (t10_t5*ADD[0]) < t101_mem1*ADD_mem[0]
	S += (t10_t5*ADD[1]) < t101_mem1*ADD_mem[1]
	S += (t10_t5*ADD[2]) < t101_mem1*ADD_mem[2]
	S += (t10_t5*ADD[3]) < t101_mem1*ADD_mem[3]
	S += t101_mem1 <= t101

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(ADD)

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(ADD_mem)
	S += (t100*ADD[0]) < t110_mem0*ADD_mem[0]
	S += (t100*ADD[1]) < t110_mem0*ADD_mem[1]
	S += (t100*ADD[2]) < t110_mem0*ADD_mem[2]
	S += (t100*ADD[3]) < t110_mem0*ADD_mem[3]
	S += t110_mem0 <= t110

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	t2_t0_in += alt(MUL_in)
	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	t2_t0 += alt(MUL)
	S += t2_t0>=t2_t0_in

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	t2_t0_mem0 += INPUT_mem_r
	S += t2_t0_mem0 <= t2_t0

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	t2_t0_mem1 += alt(ADD_mem)
	S += (t10*ADD[0]) < t2_t0_mem1*ADD_mem[0]
	S += (t10*ADD[1]) < t2_t0_mem1*ADD_mem[1]
	S += (t10*ADD[2]) < t2_t0_mem1*ADD_mem[2]
	S += (t10*ADD[3]) < t2_t0_mem1*ADD_mem[3]
	S += t2_t0_mem1 <= t2_t0

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	t2_t3 += alt(ADD)

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	t2_t3_mem0 += alt(ADD_mem)
	S += (t10*ADD[0]) < t2_t3_mem0*ADD_mem[0]
	S += (t10*ADD[1]) < t2_t3_mem0*ADD_mem[1]
	S += (t10*ADD[2]) < t2_t3_mem0*ADD_mem[2]
	S += (t10*ADD[3]) < t2_t3_mem0*ADD_mem[3]
	S += t2_t3_mem0 <= t2_t3

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	t2_t3_mem1 += alt(ADD_mem)
	S += (t11*ADD[0]) < t2_t3_mem1*ADD_mem[0]
	S += (t11*ADD[1]) < t2_t3_mem1*ADD_mem[1]
	S += (t11*ADD[2]) < t2_t3_mem1*ADD_mem[2]
	S += (t11*ADD[3]) < t2_t3_mem1*ADD_mem[3]
	S += t2_t3_mem1 <= t2_t3

	t61 = S.Task('t61', length=1, delay_cost=1)
	t61 += alt(ADD)

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += alt(ADD_mem)
	S += (t51*ADD[0]) < t61_mem0*ADD_mem[0]
	S += (t51*ADD[1]) < t61_mem0*ADD_mem[1]
	S += (t51*ADD[2]) < t61_mem0*ADD_mem[2]
	S += (t51*ADD[3]) < t61_mem0*ADD_mem[3]
	S += t61_mem0 <= t61

	t80 = S.Task('t80', length=1, delay_cost=1)
	t80 += alt(ADD)

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += alt(ADD_mem)
	S += (t70*ADD[0]) < t80_mem0*ADD_mem[0]
	S += (t70*ADD[1]) < t80_mem0*ADD_mem[1]
	S += (t70*ADD[2]) < t80_mem0*ADD_mem[2]
	S += (t70*ADD[3]) < t80_mem0*ADD_mem[3]
	S += t80_mem0 <= t80

	t91 = S.Task('t91', length=1, delay_cost=1)
	t91 += alt(ADD)

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += alt(ADD_mem)
	S += (t81*ADD[0]) < t91_mem0*ADD_mem[0]
	S += (t81*ADD[1]) < t91_mem0*ADD_mem[1]
	S += (t81*ADD[2]) < t91_mem0*ADD_mem[2]
	S += (t81*ADD[3]) < t91_mem0*ADD_mem[3]
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += alt(ADD_mem)
	S += (t71*ADD[0]) < t91_mem1*ADD_mem[0]
	S += (t71*ADD[1]) < t91_mem1*ADD_mem[1]
	S += (t71*ADD[2]) < t91_mem1*ADD_mem[2]
	S += (t71*ADD[3]) < t91_mem1*ADD_mem[3]
	S += t91_mem1 <= t91

	t111 = S.Task('t111', length=1, delay_cost=1)
	t111 += alt(ADD)

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(ADD_mem)
	S += (t101*ADD[0]) < t111_mem0*ADD_mem[0]
	S += (t101*ADD[1]) < t111_mem0*ADD_mem[1]
	S += (t101*ADD[2]) < t111_mem0*ADD_mem[2]
	S += (t101*ADD[3]) < t111_mem0*ADD_mem[3]
	S += t111_mem0 <= t111

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	t12_t0_in += alt(MUL_in)
	t12_t0 = S.Task('t12_t0', length=7, delay_cost=1)
	t12_t0 += alt(MUL)
	S += t12_t0>=t12_t0_in

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	t12_t0_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t12_t0_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t12_t0_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t12_t0_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t12_t0_mem0*ADD_mem[3]
	S += t12_t0_mem0 <= t12_t0

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	t12_t0_mem1 += alt(ADD_mem)
	S += (t110*ADD[0]) < t12_t0_mem1*ADD_mem[0]
	S += (t110*ADD[1]) < t12_t0_mem1*ADD_mem[1]
	S += (t110*ADD[2]) < t12_t0_mem1*ADD_mem[2]
	S += (t110*ADD[3]) < t12_t0_mem1*ADD_mem[3]
	S += t12_t0_mem1 <= t12_t0

	t12_t2 = S.Task('t12_t2', length=1, delay_cost=1)
	t12_t2 += alt(ADD)

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	t12_t2_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t12_t2_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t12_t2_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t12_t2_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t12_t2_mem0*ADD_mem[3]
	S += t12_t2_mem0 <= t12_t2

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	t12_t2_mem1 += alt(ADD_mem)
	S += (t01*ADD[0]) < t12_t2_mem1*ADD_mem[0]
	S += (t01*ADD[1]) < t12_t2_mem1*ADD_mem[1]
	S += (t01*ADD[2]) < t12_t2_mem1*ADD_mem[2]
	S += (t01*ADD[3]) < t12_t2_mem1*ADD_mem[3]
	S += t12_t2_mem1 <= t12_t2

	t18_t0 = S.Task('t18_t0', length=1, delay_cost=1)
	t18_t0 += alt(ADD)

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	t18_t0_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t18_t0_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t18_t0_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t18_t0_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t18_t0_mem0*ADD_mem[3]
	S += t18_t0_mem0 <= t18_t0

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	t18_t0_mem1 += alt(ADD_mem)
	S += (t01*ADD[0]) < t18_t0_mem1*ADD_mem[0]
	S += (t01*ADD[1]) < t18_t0_mem1*ADD_mem[1]
	S += (t01*ADD[2]) < t18_t0_mem1*ADD_mem[2]
	S += (t01*ADD[3]) < t18_t0_mem1*ADD_mem[3]
	S += t18_t0_mem1 <= t18_t0

	t18_t1 = S.Task('t18_t1', length=1, delay_cost=1)
	t18_t1 += alt(ADD)

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	t18_t1_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t18_t1_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t18_t1_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t18_t1_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t18_t1_mem0*ADD_mem[3]
	S += t18_t1_mem0 <= t18_t1

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	t18_t1_mem1 += alt(ADD_mem)
	S += (t01*ADD[0]) < t18_t1_mem1*ADD_mem[0]
	S += (t01*ADD[1]) < t18_t1_mem1*ADD_mem[1]
	S += (t01*ADD[2]) < t18_t1_mem1*ADD_mem[2]
	S += (t01*ADD[3]) < t18_t1_mem1*ADD_mem[3]
	S += t18_t1_mem1 <= t18_t1

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	t18_t3_in += alt(MUL_in)
	t18_t3 = S.Task('t18_t3', length=7, delay_cost=1)
	t18_t3 += alt(MUL)
	S += t18_t3>=t18_t3_in

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	t18_t3_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t18_t3_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t18_t3_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t18_t3_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t18_t3_mem0*ADD_mem[3]
	S += t18_t3_mem0 <= t18_t3

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	t18_t3_mem1 += alt(ADD_mem)
	S += (t01*ADD[0]) < t18_t3_mem1*ADD_mem[0]
	S += (t01*ADD[1]) < t18_t3_mem1*ADD_mem[1]
	S += (t01*ADD[2]) < t18_t3_mem1*ADD_mem[2]
	S += (t01*ADD[3]) < t18_t3_mem1*ADD_mem[3]
	S += t18_t3_mem1 <= t18_t3

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MUL_in)
	c010 = S.Task('c010', length=7, delay_cost=1)
	c010 += alt(MUL)
	S += c010>=c010_in

	S += 0<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(ADD_mem)
	S += (t110*ADD[0]) < c010_mem0*ADD_mem[0]
	S += (t110*ADD[1]) < c010_mem0*ADD_mem[1]
	S += (t110*ADD[2]) < c010_mem0*ADD_mem[2]
	S += (t110*ADD[3]) < c010_mem0*ADD_mem[3]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += INPUT_mem_r
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010 <= c010_w

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MUL_in)
	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	t2_t4 += alt(MUL)
	S += t2_t4>=t2_t4_in

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += ADD_mem[0]
	S += 8 < t2_t4_mem0
	S += t2_t4_mem0 <= t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += alt(ADD_mem)
	S += (t2_t3*ADD[0]) < t2_t4_mem1*ADD_mem[0]
	S += (t2_t3*ADD[1]) < t2_t4_mem1*ADD_mem[1]
	S += (t2_t3*ADD[2]) < t2_t4_mem1*ADD_mem[2]
	S += (t2_t3*ADD[3]) < t2_t4_mem1*ADD_mem[3]
	S += t2_t4_mem1 <= t2_t4

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(ADD)

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += alt(MUL_mem)
	S += (t2_t0*MUL[0]) < t20_mem0*MUL_mem[0]
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += alt(MUL_mem)
	S += (t2_t1*MUL[0]) < t20_mem1*MUL_mem[0]
	S += t20_mem1 <= t20

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	t2_t5 += alt(ADD)

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += alt(MUL_mem)
	S += (t2_t0*MUL[0]) < t2_t5_mem0*MUL_mem[0]
	S += t2_t5_mem0 <= t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += alt(MUL_mem)
	S += (t2_t1*MUL[0]) < t2_t5_mem1*MUL_mem[0]
	S += t2_t5_mem1 <= t2_t5

	t90 = S.Task('t90', length=1, delay_cost=1)
	t90 += alt(ADD)

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += alt(ADD_mem)
	S += (t80*ADD[0]) < t90_mem0*ADD_mem[0]
	S += (t80*ADD[1]) < t90_mem0*ADD_mem[1]
	S += (t80*ADD[2]) < t90_mem0*ADD_mem[2]
	S += (t80*ADD[3]) < t90_mem0*ADD_mem[3]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(ADD_mem)
	S += (t70*ADD[0]) < t90_mem1*ADD_mem[0]
	S += (t70*ADD[1]) < t90_mem1*ADD_mem[1]
	S += (t70*ADD[2]) < t90_mem1*ADD_mem[2]
	S += (t70*ADD[3]) < t90_mem1*ADD_mem[3]
	S += t90_mem1 <= t90

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	t12_t1_in += alt(MUL_in)
	t12_t1 = S.Task('t12_t1', length=7, delay_cost=1)
	t12_t1 += alt(MUL)
	S += t12_t1>=t12_t1_in

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	t12_t1_mem0 += alt(ADD_mem)
	S += (t01*ADD[0]) < t12_t1_mem0*ADD_mem[0]
	S += (t01*ADD[1]) < t12_t1_mem0*ADD_mem[1]
	S += (t01*ADD[2]) < t12_t1_mem0*ADD_mem[2]
	S += (t01*ADD[3]) < t12_t1_mem0*ADD_mem[3]
	S += t12_t1_mem0 <= t12_t1

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	t12_t1_mem1 += alt(ADD_mem)
	S += (t111*ADD[0]) < t12_t1_mem1*ADD_mem[0]
	S += (t111*ADD[1]) < t12_t1_mem1*ADD_mem[1]
	S += (t111*ADD[2]) < t12_t1_mem1*ADD_mem[2]
	S += (t111*ADD[3]) < t12_t1_mem1*ADD_mem[3]
	S += t12_t1_mem1 <= t12_t1

	t12_t3 = S.Task('t12_t3', length=1, delay_cost=1)
	t12_t3 += alt(ADD)

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	t12_t3_mem0 += alt(ADD_mem)
	S += (t110*ADD[0]) < t12_t3_mem0*ADD_mem[0]
	S += (t110*ADD[1]) < t12_t3_mem0*ADD_mem[1]
	S += (t110*ADD[2]) < t12_t3_mem0*ADD_mem[2]
	S += (t110*ADD[3]) < t12_t3_mem0*ADD_mem[3]
	S += t12_t3_mem0 <= t12_t3

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	t12_t3_mem1 += alt(ADD_mem)
	S += (t111*ADD[0]) < t12_t3_mem1*ADD_mem[0]
	S += (t111*ADD[1]) < t12_t3_mem1*ADD_mem[1]
	S += (t111*ADD[2]) < t12_t3_mem1*ADD_mem[2]
	S += (t111*ADD[3]) < t12_t3_mem1*ADD_mem[3]
	S += t12_t3_mem1 <= t12_t3

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	new_TX_t3 += alt(ADD)

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	new_TX_t3_mem0 += alt(ADD_mem)
	S += (t60*ADD[0]) < new_TX_t3_mem0*ADD_mem[0]
	S += (t60*ADD[1]) < new_TX_t3_mem0*ADD_mem[1]
	S += (t60*ADD[2]) < new_TX_t3_mem0*ADD_mem[2]
	S += (t60*ADD[3]) < new_TX_t3_mem0*ADD_mem[3]
	S += new_TX_t3_mem0 <= new_TX_t3

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	new_TX_t3_mem1 += alt(ADD_mem)
	S += (t61*ADD[0]) < new_TX_t3_mem1*ADD_mem[0]
	S += (t61*ADD[1]) < new_TX_t3_mem1*ADD_mem[1]
	S += (t61*ADD[2]) < new_TX_t3_mem1*ADD_mem[2]
	S += (t61*ADD[3]) < new_TX_t3_mem1*ADD_mem[3]
	S += new_TX_t3_mem1 <= new_TX_t3

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	t18_t2_in += alt(MUL_in)
	t18_t2 = S.Task('t18_t2', length=7, delay_cost=1)
	t18_t2 += alt(MUL)
	S += t18_t2>=t18_t2_in

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	t18_t2_mem0 += alt(ADD_mem)
	S += (t18_t0*ADD[0]) < t18_t2_mem0*ADD_mem[0]
	S += (t18_t0*ADD[1]) < t18_t2_mem0*ADD_mem[1]
	S += (t18_t0*ADD[2]) < t18_t2_mem0*ADD_mem[2]
	S += (t18_t0*ADD[3]) < t18_t2_mem0*ADD_mem[3]
	S += t18_t2_mem0 <= t18_t2

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	t18_t2_mem1 += alt(ADD_mem)
	S += (t18_t1*ADD[0]) < t18_t2_mem1*ADD_mem[0]
	S += (t18_t1*ADD[1]) < t18_t2_mem1*ADD_mem[1]
	S += (t18_t1*ADD[2]) < t18_t2_mem1*ADD_mem[2]
	S += (t18_t1*ADD[3]) < t18_t2_mem1*ADD_mem[3]
	S += t18_t2_mem1 <= t18_t2

	t18_t5 = S.Task('t18_t5', length=1, delay_cost=1)
	t18_t5 += alt(ADD)

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	t18_t5_mem0 += alt(MUL_mem)
	S += (t18_t3*MUL[0]) < t18_t5_mem0*MUL_mem[0]
	S += t18_t5_mem0 <= t18_t5

	t181 = S.Task('t181', length=1, delay_cost=1)
	t181 += alt(ADD)

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	t181_mem0 += alt(MUL_mem)
	S += (t18_t3*MUL[0]) < t181_mem0*MUL_mem[0]
	S += t181_mem0 <= t181

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MUL_in)
	c011 = S.Task('c011', length=7, delay_cost=1)
	c011 += alt(MUL)
	S += c011>=c011_in

	S += 0<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(ADD_mem)
	S += (t111*ADD[0]) < c011_mem0*ADD_mem[0]
	S += (t111*ADD[1]) < c011_mem0*ADD_mem[1]
	S += (t111*ADD[2]) < c011_mem0*ADD_mem[2]
	S += (t111*ADD[3]) < c011_mem0*ADD_mem[3]
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
	S += (t91*ADD[0]) < c201_mem0*ADD_mem[0]
	S += (t91*ADD[1]) < c201_mem0*ADD_mem[1]
	S += (t91*ADD[2]) < c201_mem0*ADD_mem[2]
	S += (t91*ADD[3]) < c201_mem0*ADD_mem[3]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += INPUT_mem_r
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201 <= c201_w

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
	t30_mem0 += alt(ADD_mem)
	S += (t20*ADD[0]) < t30_mem0*ADD_mem[0]
	S += (t20*ADD[1]) < t30_mem0*ADD_mem[1]
	S += (t20*ADD[2]) < t30_mem0*ADD_mem[2]
	S += (t20*ADD[3]) < t30_mem0*ADD_mem[3]
	S += t30_mem0 <= t30

	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	t12_t4_in += alt(MUL_in)
	t12_t4 = S.Task('t12_t4', length=7, delay_cost=1)
	t12_t4 += alt(MUL)
	S += t12_t4>=t12_t4_in

	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	t12_t4_mem0 += alt(ADD_mem)
	S += (t12_t2*ADD[0]) < t12_t4_mem0*ADD_mem[0]
	S += (t12_t2*ADD[1]) < t12_t4_mem0*ADD_mem[1]
	S += (t12_t2*ADD[2]) < t12_t4_mem0*ADD_mem[2]
	S += (t12_t2*ADD[3]) < t12_t4_mem0*ADD_mem[3]
	S += t12_t4_mem0 <= t12_t4

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	t12_t4_mem1 += alt(ADD_mem)
	S += (t12_t3*ADD[0]) < t12_t4_mem1*ADD_mem[0]
	S += (t12_t3*ADD[1]) < t12_t4_mem1*ADD_mem[1]
	S += (t12_t3*ADD[2]) < t12_t4_mem1*ADD_mem[2]
	S += (t12_t3*ADD[3]) < t12_t4_mem1*ADD_mem[3]
	S += t12_t4_mem1 <= t12_t4

	t120 = S.Task('t120', length=1, delay_cost=1)
	t120 += alt(ADD)

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += alt(MUL_mem)
	S += (t12_t0*MUL[0]) < t120_mem0*MUL_mem[0]
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += alt(MUL_mem)
	S += (t12_t1*MUL[0]) < t120_mem1*MUL_mem[0]
	S += t120_mem1 <= t120

	t12_t5 = S.Task('t12_t5', length=1, delay_cost=1)
	t12_t5 += alt(ADD)

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	t12_t5_mem0 += alt(MUL_mem)
	S += (t12_t0*MUL[0]) < t12_t5_mem0*MUL_mem[0]
	S += t12_t5_mem0 <= t12_t5

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	t12_t5_mem1 += alt(MUL_mem)
	S += (t12_t1*MUL[0]) < t12_t5_mem1*MUL_mem[0]
	S += t12_t5_mem1 <= t12_t5

	t180 = S.Task('t180', length=1, delay_cost=1)
	t180 += alt(ADD)

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	t180_mem0 += alt(MUL_mem)
	S += (t18_t2*MUL[0]) < t180_mem0*MUL_mem[0]
	S += t180_mem0 <= t180

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	t180_mem1 += alt(ADD_mem)
	S += (t18_t5*ADD[0]) < t180_mem1*ADD_mem[0]
	S += (t18_t5*ADD[1]) < t180_mem1*ADD_mem[1]
	S += (t18_t5*ADD[2]) < t180_mem1*ADD_mem[2]
	S += (t18_t5*ADD[3]) < t180_mem1*ADD_mem[3]
	S += t180_mem1 <= t180

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MUL_in)
	c200 = S.Task('c200', length=7, delay_cost=1)
	c200 += alt(MUL)
	S += c200>=c200_in

	S += 0<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(ADD_mem)
	S += (t90*ADD[0]) < c200_mem0*ADD_mem[0]
	S += (t90*ADD[1]) < c200_mem0*ADD_mem[1]
	S += (t90*ADD[2]) < c200_mem0*ADD_mem[2]
	S += (t90*ADD[3]) < c200_mem0*ADD_mem[3]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += INPUT_mem_r
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200 <= c200_w

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(ADD)

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(ADD_mem)
	S += (t21*ADD[0]) < t31_mem0*ADD_mem[0]
	S += (t21*ADD[1]) < t31_mem0*ADD_mem[1]
	S += (t21*ADD[2]) < t31_mem0*ADD_mem[2]
	S += (t21*ADD[3]) < t31_mem0*ADD_mem[3]
	S += t31_mem0 <= t31

	t40 = S.Task('t40', length=1, delay_cost=1)
	t40 += alt(ADD)

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(ADD_mem)
	S += (t30*ADD[0]) < t40_mem0*ADD_mem[0]
	S += (t30*ADD[1]) < t40_mem0*ADD_mem[1]
	S += (t30*ADD[2]) < t40_mem0*ADD_mem[2]
	S += (t30*ADD[3]) < t40_mem0*ADD_mem[3]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += alt(ADD_mem)
	S += (t20*ADD[0]) < t40_mem1*ADD_mem[0]
	S += (t20*ADD[1]) < t40_mem1*ADD_mem[1]
	S += (t20*ADD[2]) < t40_mem1*ADD_mem[2]
	S += (t20*ADD[3]) < t40_mem1*ADD_mem[3]
	S += t40_mem1 <= t40

	t121 = S.Task('t121', length=1, delay_cost=1)
	t121 += alt(ADD)

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(MUL_mem)
	S += (t12_t4*MUL[0]) < t121_mem0*MUL_mem[0]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += alt(ADD_mem)
	S += (t12_t5*ADD[0]) < t121_mem1*ADD_mem[0]
	S += (t12_t5*ADD[1]) < t121_mem1*ADD_mem[1]
	S += (t12_t5*ADD[2]) < t121_mem1*ADD_mem[2]
	S += (t12_t5*ADD[3]) < t121_mem1*ADD_mem[3]
	S += t121_mem1 <= t121

	t130 = S.Task('t130', length=1, delay_cost=1)
	t130 += alt(ADD)

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += alt(ADD_mem)
	S += (t120*ADD[0]) < t130_mem0*ADD_mem[0]
	S += (t120*ADD[1]) < t130_mem0*ADD_mem[1]
	S += (t120*ADD[2]) < t130_mem0*ADD_mem[2]
	S += (t120*ADD[3]) < t130_mem0*ADD_mem[3]
	S += t130_mem0 <= t130

	t41 = S.Task('t41', length=1, delay_cost=1)
	t41 += alt(ADD)

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += alt(ADD_mem)
	S += (t31*ADD[0]) < t41_mem0*ADD_mem[0]
	S += (t31*ADD[1]) < t41_mem0*ADD_mem[1]
	S += (t31*ADD[2]) < t41_mem0*ADD_mem[2]
	S += (t31*ADD[3]) < t41_mem0*ADD_mem[3]
	S += t41_mem0 <= t41

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	t41_mem1 += alt(ADD_mem)
	S += (t21*ADD[0]) < t41_mem1*ADD_mem[0]
	S += (t21*ADD[1]) < t41_mem1*ADD_mem[1]
	S += (t21*ADD[2]) < t41_mem1*ADD_mem[2]
	S += (t21*ADD[3]) < t41_mem1*ADD_mem[3]
	S += t41_mem1 <= t41

	t131 = S.Task('t131', length=1, delay_cost=1)
	t131 += alt(ADD)

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += alt(ADD_mem)
	S += (t121*ADD[0]) < t131_mem0*ADD_mem[0]
	S += (t121*ADD[1]) < t131_mem0*ADD_mem[1]
	S += (t121*ADD[2]) < t131_mem0*ADD_mem[2]
	S += (t121*ADD[3]) < t131_mem0*ADD_mem[3]
	S += t131_mem0 <= t131

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	new_TZ0 += alt(ADD)

	S += 16<new_TZ0

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += alt(ADD_mem)
	S += (t130*ADD[0]) < new_TZ0_mem0*ADD_mem[0]
	S += (t130*ADD[1]) < new_TZ0_mem0*ADD_mem[1]
	S += (t130*ADD[2]) < new_TZ0_mem0*ADD_mem[2]
	S += (t130*ADD[3]) < new_TZ0_mem0*ADD_mem[3]
	S += new_TZ0_mem0 <= new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(INPUT_mem_w)
	S += new_TZ0 <= new_TZ0_w

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(ADD)

	S += 0<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < c000_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < c000_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < c000_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < c000_mem0*ADD_mem[3]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(ADD_mem)
	S += (t40*ADD[0]) < c000_mem1*ADD_mem[0]
	S += (t40*ADD[1]) < c000_mem1*ADD_mem[1]
	S += (t40*ADD[2]) < c000_mem1*ADD_mem[2]
	S += (t40*ADD[3]) < c000_mem1*ADD_mem[3]
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(INPUT_mem_w)
	S += c000 <= c000_w

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(ADD)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(ADD_mem)
	S += (t40*ADD[0]) < t140_mem0*ADD_mem[0]
	S += (t40*ADD[1]) < t140_mem0*ADD_mem[1]
	S += (t40*ADD[2]) < t140_mem0*ADD_mem[2]
	S += (t40*ADD[3]) < t140_mem0*ADD_mem[3]
	S += t140_mem0 <= t140

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	new_TZ1 += alt(ADD)

	S += 16<new_TZ1

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(ADD_mem)
	S += (t131*ADD[0]) < new_TZ1_mem0*ADD_mem[0]
	S += (t131*ADD[1]) < new_TZ1_mem0*ADD_mem[1]
	S += (t131*ADD[2]) < new_TZ1_mem0*ADD_mem[2]
	S += (t131*ADD[3]) < new_TZ1_mem0*ADD_mem[3]
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(INPUT_mem_w)
	S += new_TZ1 <= new_TZ1_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(ADD)

	S += 0<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(ADD_mem)
	S += (t01*ADD[0]) < c001_mem0*ADD_mem[0]
	S += (t01*ADD[1]) < c001_mem0*ADD_mem[1]
	S += (t01*ADD[2]) < c001_mem0*ADD_mem[2]
	S += (t01*ADD[3]) < c001_mem0*ADD_mem[3]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(ADD_mem)
	S += (t41*ADD[0]) < c001_mem1*ADD_mem[0]
	S += (t41*ADD[1]) < c001_mem1*ADD_mem[1]
	S += (t41*ADD[2]) < c001_mem1*ADD_mem[2]
	S += (t41*ADD[3]) < c001_mem1*ADD_mem[3]
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(INPUT_mem_w)
	S += c001 <= c001_w

	t141 = S.Task('t141', length=1, delay_cost=1)
	t141 += alt(ADD)

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += alt(ADD_mem)
	S += (t41*ADD[0]) < t141_mem0*ADD_mem[0]
	S += (t41*ADD[1]) < t141_mem0*ADD_mem[1]
	S += (t41*ADD[2]) < t141_mem0*ADD_mem[2]
	S += (t41*ADD[3]) < t141_mem0*ADD_mem[3]
	S += t141_mem0 <= t141

	t150 = S.Task('t150', length=1, delay_cost=1)
	t150 += alt(ADD)

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(ADD_mem)
	S += (c000*ADD[0]) < t150_mem0*ADD_mem[0]
	S += (c000*ADD[1]) < t150_mem0*ADD_mem[1]
	S += (c000*ADD[2]) < t150_mem0*ADD_mem[2]
	S += (c000*ADD[3]) < t150_mem0*ADD_mem[3]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(ADD_mem)
	S += (t140*ADD[0]) < t150_mem1*ADD_mem[0]
	S += (t140*ADD[1]) < t150_mem1*ADD_mem[1]
	S += (t140*ADD[2]) < t150_mem1*ADD_mem[2]
	S += (t140*ADD[3]) < t150_mem1*ADD_mem[3]
	S += t150_mem1 <= t150

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(ADD)

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t160_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t160_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t160_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t160_mem0*ADD_mem[3]
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(ADD_mem)
	S += (c000*ADD[0]) < t160_mem1*ADD_mem[0]
	S += (c000*ADD[1]) < t160_mem1*ADD_mem[1]
	S += (c000*ADD[2]) < t160_mem1*ADD_mem[2]
	S += (c000*ADD[3]) < t160_mem1*ADD_mem[3]
	S += t160_mem1 <= t160

	b30 = S.Task('b30', length=1, delay_cost=1)
	b30 += alt(ADD)

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	b30_mem0 += alt(ADD_mem)
	S += (t140*ADD[0]) < b30_mem0*ADD_mem[0]
	S += (t140*ADD[1]) < b30_mem0*ADD_mem[1]
	S += (t140*ADD[2]) < b30_mem0*ADD_mem[2]
	S += (t140*ADD[3]) < b30_mem0*ADD_mem[3]
	S += b30_mem0 <= b30

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	b30_mem1 += alt(ADD_mem)
	S += (t40*ADD[0]) < b30_mem1*ADD_mem[0]
	S += (t40*ADD[1]) < b30_mem1*ADD_mem[1]
	S += (t40*ADD[2]) < b30_mem1*ADD_mem[2]
	S += (t40*ADD[3]) < b30_mem1*ADD_mem[3]
	S += b30_mem1 <= b30

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-1150/scheduling/PDBL_mul1_add4/PDBL_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

