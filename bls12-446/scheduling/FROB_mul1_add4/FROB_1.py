from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 113
	S = Scenario("FROB_1", horizon=horizon)

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
	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 0
	c000_mem0 += INPUT_mem_r

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 0
	c000_mem1 += INPUT_mem_r

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 1
	c000 += ADD[3]

	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	S += c10_t0_in >= 1
	c10_t0_in += MUL_in[0]

	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	S += c10_t0_mem0 >= 1
	c10_t0_mem0 += INPUT_mem_r

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	S += c10_t0_mem1 >= 1
	c10_t0_mem1 += INPUT_mem_r

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 2
	c000_w += INPUT_mem_w

	c10_t0 = S.Task('c10_t0', length=7, delay_cost=1)
	S += c10_t0 >= 2
	c10_t0 += MUL[0]

	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	S += c11_t0_in >= 2
	c11_t0_in += MUL_in[0]

	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	S += c11_t0_mem0 >= 2
	c11_t0_mem0 += INPUT_mem_r

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	S += c11_t0_mem1 >= 2
	c11_t0_mem1 += INPUT_mem_r

	c11_t0 = S.Task('c11_t0', length=7, delay_cost=1)
	S += c11_t0 >= 3
	c11_t0 += MUL[0]

	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	S += c11_t1_in >= 3
	c11_t1_in += MUL_in[0]

	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	S += c11_t1_mem0 >= 3
	c11_t1_mem0 += INPUT_mem_r

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	S += c11_t1_mem1 >= 3
	c11_t1_mem1 += INPUT_mem_r

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 4
	c001_mem0 += INPUT_mem_r

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 4
	c001_mem1 += INPUT_mem_r

	c11_t1 = S.Task('c11_t1', length=7, delay_cost=1)
	S += c11_t1 >= 4
	c11_t1 += MUL[0]

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 5
	c001 += ADD[2]

	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	S += c20_t0_in >= 5
	c20_t0_in += MUL_in[0]

	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	S += c20_t0_mem0 >= 5
	c20_t0_mem0 += INPUT_mem_r

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	S += c20_t0_mem1 >= 5
	c20_t0_mem1 += INPUT_mem_r

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 6
	c001_w += INPUT_mem_w

	c20_t0 = S.Task('c20_t0', length=7, delay_cost=1)
	S += c20_t0 >= 6
	c20_t0 += MUL[0]

	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	S += c21_t0_in >= 6
	c21_t0_in += MUL_in[0]

	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	S += c21_t0_mem0 >= 6
	c21_t0_mem0 += INPUT_mem_r

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	S += c21_t0_mem1 >= 6
	c21_t0_mem1 += INPUT_mem_r

	c21_t0 = S.Task('c21_t0', length=7, delay_cost=1)
	S += c21_t0 >= 7
	c21_t0 += MUL[0]

	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	S += c21_t1_in >= 7
	c21_t1_in += MUL_in[0]

	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	S += c21_t1_mem0 >= 7
	c21_t1_mem0 += INPUT_mem_r

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	S += c21_t1_mem1 >= 7
	c21_t1_mem1 += INPUT_mem_r

	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	S += c20_t1_in >= 8
	c20_t1_in += MUL_in[0]

	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	S += c20_t1_mem0 >= 8
	c20_t1_mem0 += INPUT_mem_r

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	S += c20_t1_mem1 >= 8
	c20_t1_mem1 += INPUT_mem_r

	c21_t1 = S.Task('c21_t1', length=7, delay_cost=1)
	S += c21_t1 >= 8
	c21_t1 += MUL[0]

	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	S += c10_t1_in >= 9
	c10_t1_in += MUL_in[0]

	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	S += c10_t1_mem0 >= 9
	c10_t1_mem0 += INPUT_mem_r

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	S += c10_t1_mem1 >= 9
	c10_t1_mem1 += INPUT_mem_r

	c20_t1 = S.Task('c20_t1', length=7, delay_cost=1)
	S += c20_t1 >= 9
	c20_t1 += MUL[0]

	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	S += c01_t1_in >= 10
	c01_t1_in += MUL_in[0]

	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	S += c01_t1_mem0 >= 10
	c01_t1_mem0 += INPUT_mem_r

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	S += c01_t1_mem1 >= 10
	c01_t1_mem1 += INPUT_mem_r

	c10_t1 = S.Task('c10_t1', length=7, delay_cost=1)
	S += c10_t1 >= 10
	c10_t1 += MUL[0]

	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	S += c01_t0_in >= 11
	c01_t0_in += MUL_in[0]

	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	S += c01_t0_mem0 >= 11
	c01_t0_mem0 += INPUT_mem_r

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	S += c01_t0_mem1 >= 11
	c01_t0_mem1 += INPUT_mem_r

	c01_t1 = S.Task('c01_t1', length=7, delay_cost=1)
	S += c01_t1 >= 11
	c01_t1 += MUL[0]

	c01_t0 = S.Task('c01_t0', length=7, delay_cost=1)
	S += c01_t0 >= 12
	c01_t0 += MUL[0]

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	S += c20_t3_mem0 >= 12
	c20_t3_mem0 += INPUT_mem_r

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	S += c20_t3_mem1 >= 12
	c20_t3_mem1 += INPUT_mem_r

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	S += c01_t2_mem0 >= 13
	c01_t2_mem0 += INPUT_mem_r

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	S += c01_t2_mem1 >= 13
	c01_t2_mem1 += INPUT_mem_r

	c20_t3 = S.Task('c20_t3', length=1, delay_cost=1)
	S += c20_t3 >= 13
	c20_t3 += ADD[1]

	c01_t2 = S.Task('c01_t2', length=1, delay_cost=1)
	S += c01_t2 >= 14
	c01_t2 += ADD[0]

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	S += c10_t2_mem0 >= 14
	c10_t2_mem0 += INPUT_mem_r

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	S += c10_t2_mem1 >= 14
	c10_t2_mem1 += INPUT_mem_r

	c10_t2 = S.Task('c10_t2', length=1, delay_cost=1)
	S += c10_t2 >= 15
	c10_t2 += ADD[3]

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	S += c20_t2_mem0 >= 15
	c20_t2_mem0 += INPUT_mem_r

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	S += c20_t2_mem1 >= 15
	c20_t2_mem1 += INPUT_mem_r

	c20_t2 = S.Task('c20_t2', length=1, delay_cost=1)
	S += c20_t2 >= 16
	c20_t2 += ADD[2]

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	S += c21_t2_mem0 >= 16
	c21_t2_mem0 += INPUT_mem_r

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	S += c21_t2_mem1 >= 16
	c21_t2_mem1 += INPUT_mem_r

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	S += c11_t3_mem0 >= 17
	c11_t3_mem0 += INPUT_mem_r

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	S += c11_t3_mem1 >= 17
	c11_t3_mem1 += INPUT_mem_r

	c21_t2 = S.Task('c21_t2', length=1, delay_cost=1)
	S += c21_t2 >= 17
	c21_t2 += ADD[2]

	c11_t3 = S.Task('c11_t3', length=1, delay_cost=1)
	S += c11_t3 >= 18
	c11_t3 += ADD[1]

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	S += c21_t3_mem0 >= 18
	c21_t3_mem0 += INPUT_mem_r

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	S += c21_t3_mem1 >= 18
	c21_t3_mem1 += INPUT_mem_r

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	S += c01_t3_mem0 >= 19
	c01_t3_mem0 += INPUT_mem_r

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	S += c01_t3_mem1 >= 19
	c01_t3_mem1 += INPUT_mem_r

	c21_t3 = S.Task('c21_t3', length=1, delay_cost=1)
	S += c21_t3 >= 19
	c21_t3 += ADD[0]

	c01_t3 = S.Task('c01_t3', length=1, delay_cost=1)
	S += c01_t3 >= 20
	c01_t3 += ADD[0]

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	S += c11_t2_mem0 >= 20
	c11_t2_mem0 += INPUT_mem_r

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	S += c11_t2_mem1 >= 20
	c11_t2_mem1 += INPUT_mem_r

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	S += c10_t3_mem0 >= 21
	c10_t3_mem0 += INPUT_mem_r

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	S += c10_t3_mem1 >= 21
	c10_t3_mem1 += INPUT_mem_r

	c11_t2 = S.Task('c11_t2', length=1, delay_cost=1)
	S += c11_t2 >= 21
	c11_t2 += ADD[1]

	c10_t3 = S.Task('c10_t3', length=1, delay_cost=1)
	S += c10_t3 >= 22
	c10_t3 += ADD[0]


	# new tasks
	c10_t4_in = S.Task('c10_t4_in', length=1, delay_cost=1)
	c10_t4_in += alt(MUL_in)
	c10_t4 = S.Task('c10_t4', length=7, delay_cost=1)
	c10_t4 += alt(MUL)
	S += c10_t4>=c10_t4_in

	c10_t4_mem0 = S.Task('c10_t4_mem0', length=1, delay_cost=1)
	c10_t4_mem0 += ADD_mem[3]
	S += 15 < c10_t4_mem0
	S += c10_t4_mem0 <= c10_t4

	c10_t4_mem1 = S.Task('c10_t4_mem1', length=1, delay_cost=1)
	c10_t4_mem1 += ADD_mem[0]
	S += 22 < c10_t4_mem1
	S += c10_t4_mem1 <= c10_t4

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(ADD)

	S += 15<c100

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += MUL_mem[0]
	S += 8 < c100_mem0
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += MUL_mem[0]
	S += 16 < c100_mem1
	S += c100_mem1 <= c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(INPUT_mem_w)
	S += c100 <= c100_w

	c10_t5 = S.Task('c10_t5', length=1, delay_cost=1)
	c10_t5 += alt(ADD)

	c10_t5_mem0 = S.Task('c10_t5_mem0', length=1, delay_cost=1)
	c10_t5_mem0 += MUL_mem[0]
	S += 8 < c10_t5_mem0
	S += c10_t5_mem0 <= c10_t5

	c10_t5_mem1 = S.Task('c10_t5_mem1', length=1, delay_cost=1)
	c10_t5_mem1 += MUL_mem[0]
	S += 16 < c10_t5_mem1
	S += c10_t5_mem1 <= c10_t5

	c20_t4_in = S.Task('c20_t4_in', length=1, delay_cost=1)
	c20_t4_in += alt(MUL_in)
	c20_t4 = S.Task('c20_t4', length=7, delay_cost=1)
	c20_t4 += alt(MUL)
	S += c20_t4>=c20_t4_in

	c20_t4_mem0 = S.Task('c20_t4_mem0', length=1, delay_cost=1)
	c20_t4_mem0 += ADD_mem[2]
	S += 16 < c20_t4_mem0
	S += c20_t4_mem0 <= c20_t4

	c20_t4_mem1 = S.Task('c20_t4_mem1', length=1, delay_cost=1)
	c20_t4_mem1 += ADD_mem[1]
	S += 13 < c20_t4_mem1
	S += c20_t4_mem1 <= c20_t4

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(ADD)

	S += 16<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MUL_mem[0]
	S += 12 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MUL_mem[0]
	S += 15 < c200_mem1
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200 <= c200_w

	c20_t5 = S.Task('c20_t5', length=1, delay_cost=1)
	c20_t5 += alt(ADD)

	c20_t5_mem0 = S.Task('c20_t5_mem0', length=1, delay_cost=1)
	c20_t5_mem0 += MUL_mem[0]
	S += 12 < c20_t5_mem0
	S += c20_t5_mem0 <= c20_t5

	c20_t5_mem1 = S.Task('c20_t5_mem1', length=1, delay_cost=1)
	c20_t5_mem1 += MUL_mem[0]
	S += 15 < c20_t5_mem1
	S += c20_t5_mem1 <= c20_t5

	c01_t4_in = S.Task('c01_t4_in', length=1, delay_cost=1)
	c01_t4_in += alt(MUL_in)
	c01_t4 = S.Task('c01_t4', length=7, delay_cost=1)
	c01_t4 += alt(MUL)
	S += c01_t4>=c01_t4_in

	c01_t4_mem0 = S.Task('c01_t4_mem0', length=1, delay_cost=1)
	c01_t4_mem0 += ADD_mem[0]
	S += 14 < c01_t4_mem0
	S += c01_t4_mem0 <= c01_t4

	c01_t4_mem1 = S.Task('c01_t4_mem1', length=1, delay_cost=1)
	c01_t4_mem1 += ADD_mem[0]
	S += 20 < c01_t4_mem1
	S += c01_t4_mem1 <= c01_t4

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(ADD)

	S += 14<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MUL_mem[0]
	S += 18 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += MUL_mem[0]
	S += 17 < c010_mem1
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010 <= c010_w

	c01_t5 = S.Task('c01_t5', length=1, delay_cost=1)
	c01_t5 += alt(ADD)

	c01_t5_mem0 = S.Task('c01_t5_mem0', length=1, delay_cost=1)
	c01_t5_mem0 += MUL_mem[0]
	S += 18 < c01_t5_mem0
	S += c01_t5_mem0 <= c01_t5

	c01_t5_mem1 = S.Task('c01_t5_mem1', length=1, delay_cost=1)
	c01_t5_mem1 += MUL_mem[0]
	S += 17 < c01_t5_mem1
	S += c01_t5_mem1 <= c01_t5

	c11_t4_in = S.Task('c11_t4_in', length=1, delay_cost=1)
	c11_t4_in += alt(MUL_in)
	c11_t4 = S.Task('c11_t4', length=7, delay_cost=1)
	c11_t4 += alt(MUL)
	S += c11_t4>=c11_t4_in

	c11_t4_mem0 = S.Task('c11_t4_mem0', length=1, delay_cost=1)
	c11_t4_mem0 += ADD_mem[1]
	S += 21 < c11_t4_mem0
	S += c11_t4_mem0 <= c11_t4

	c11_t4_mem1 = S.Task('c11_t4_mem1', length=1, delay_cost=1)
	c11_t4_mem1 += ADD_mem[1]
	S += 18 < c11_t4_mem1
	S += c11_t4_mem1 <= c11_t4

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(ADD)

	S += 21<c110

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MUL_mem[0]
	S += 9 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MUL_mem[0]
	S += 10 < c110_mem1
	S += c110_mem1 <= c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(INPUT_mem_w)
	S += c110 <= c110_w

	c11_t5 = S.Task('c11_t5', length=1, delay_cost=1)
	c11_t5 += alt(ADD)

	c11_t5_mem0 = S.Task('c11_t5_mem0', length=1, delay_cost=1)
	c11_t5_mem0 += MUL_mem[0]
	S += 9 < c11_t5_mem0
	S += c11_t5_mem0 <= c11_t5

	c11_t5_mem1 = S.Task('c11_t5_mem1', length=1, delay_cost=1)
	c11_t5_mem1 += MUL_mem[0]
	S += 10 < c11_t5_mem1
	S += c11_t5_mem1 <= c11_t5

	c21_t4_in = S.Task('c21_t4_in', length=1, delay_cost=1)
	c21_t4_in += alt(MUL_in)
	c21_t4 = S.Task('c21_t4', length=7, delay_cost=1)
	c21_t4 += alt(MUL)
	S += c21_t4>=c21_t4_in

	c21_t4_mem0 = S.Task('c21_t4_mem0', length=1, delay_cost=1)
	c21_t4_mem0 += ADD_mem[2]
	S += 17 < c21_t4_mem0
	S += c21_t4_mem0 <= c21_t4

	c21_t4_mem1 = S.Task('c21_t4_mem1', length=1, delay_cost=1)
	c21_t4_mem1 += ADD_mem[0]
	S += 19 < c21_t4_mem1
	S += c21_t4_mem1 <= c21_t4

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(ADD)

	S += 17<c210

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MUL_mem[0]
	S += 13 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MUL_mem[0]
	S += 14 < c210_mem1
	S += c210_mem1 <= c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(INPUT_mem_w)
	S += c210 <= c210_w

	c21_t5 = S.Task('c21_t5', length=1, delay_cost=1)
	c21_t5 += alt(ADD)

	c21_t5_mem0 = S.Task('c21_t5_mem0', length=1, delay_cost=1)
	c21_t5_mem0 += MUL_mem[0]
	S += 13 < c21_t5_mem0
	S += c21_t5_mem0 <= c21_t5

	c21_t5_mem1 = S.Task('c21_t5_mem1', length=1, delay_cost=1)
	c21_t5_mem1 += MUL_mem[0]
	S += 14 < c21_t5_mem1
	S += c21_t5_mem1 <= c21_t5

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(ADD)

	S += 15<c101

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MUL_mem)
	S += (c10_t4*MUL[0]) < c101_mem0*MUL_mem[0]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(ADD_mem)
	S += (c10_t5*ADD[0]) < c101_mem1*ADD_mem[0]
	S += (c10_t5*ADD[1]) < c101_mem1*ADD_mem[1]
	S += (c10_t5*ADD[2]) < c101_mem1*ADD_mem[2]
	S += (c10_t5*ADD[3]) < c101_mem1*ADD_mem[3]
	S += c101_mem1 <= c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(INPUT_mem_w)
	S += c101 <= c101_w

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(ADD)

	S += 16<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MUL_mem)
	S += (c20_t4*MUL[0]) < c201_mem0*MUL_mem[0]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(ADD_mem)
	S += (c20_t5*ADD[0]) < c201_mem1*ADD_mem[0]
	S += (c20_t5*ADD[1]) < c201_mem1*ADD_mem[1]
	S += (c20_t5*ADD[2]) < c201_mem1*ADD_mem[2]
	S += (c20_t5*ADD[3]) < c201_mem1*ADD_mem[3]
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201 <= c201_w

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(ADD)

	S += 14<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MUL_mem)
	S += (c01_t4*MUL[0]) < c011_mem0*MUL_mem[0]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(ADD_mem)
	S += (c01_t5*ADD[0]) < c011_mem1*ADD_mem[0]
	S += (c01_t5*ADD[1]) < c011_mem1*ADD_mem[1]
	S += (c01_t5*ADD[2]) < c011_mem1*ADD_mem[2]
	S += (c01_t5*ADD[3]) < c011_mem1*ADD_mem[3]
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(INPUT_mem_w)
	S += c011 <= c011_w

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(ADD)

	S += 21<c111

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MUL_mem)
	S += (c11_t4*MUL[0]) < c111_mem0*MUL_mem[0]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += alt(ADD_mem)
	S += (c11_t5*ADD[0]) < c111_mem1*ADD_mem[0]
	S += (c11_t5*ADD[1]) < c111_mem1*ADD_mem[1]
	S += (c11_t5*ADD[2]) < c111_mem1*ADD_mem[2]
	S += (c11_t5*ADD[3]) < c111_mem1*ADD_mem[3]
	S += c111_mem1 <= c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(INPUT_mem_w)
	S += c111 <= c111_w

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(ADD)

	S += 17<c211

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MUL_mem)
	S += (c21_t4*MUL[0]) < c211_mem0*MUL_mem[0]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(ADD_mem)
	S += (c21_t5*ADD[0]) < c211_mem1*ADD_mem[0]
	S += (c21_t5*ADD[1]) < c211_mem1*ADD_mem[1]
	S += (c21_t5*ADD[2]) < c211_mem1*ADD_mem[2]
	S += (c21_t5*ADD[3]) < c211_mem1*ADD_mem[3]
	S += c211_mem1 <= c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(INPUT_mem_w)
	S += c211 <= c211_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-446/scheduling/FROB_mul1_add4/FROB_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

