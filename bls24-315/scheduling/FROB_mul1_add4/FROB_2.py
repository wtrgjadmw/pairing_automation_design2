from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 151
	S = Scenario("FROB_2", horizon=horizon)

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
	c_f111_t1_in = S.Task('c_f111_t1_in', length=1, delay_cost=1)
	S += c_f111_t1_in >= 0
	c_f111_t1_in += MUL_in[0]

	c_f111_t1_mem0 = S.Task('c_f111_t1_mem0', length=1, delay_cost=1)
	S += c_f111_t1_mem0 >= 0
	c_f111_t1_mem0 += INPUT_mem_r

	c_f111_t1_mem1 = S.Task('c_f111_t1_mem1', length=1, delay_cost=1)
	S += c_f111_t1_mem1 >= 0
	c_f111_t1_mem1 += INPUT_mem_r

	c_f111_t1 = S.Task('c_f111_t1', length=7, delay_cost=1)
	S += c_f111_t1 >= 1
	c_f111_t1 += MUL[0]

	c_f121_t0_in = S.Task('c_f121_t0_in', length=1, delay_cost=1)
	S += c_f121_t0_in >= 1
	c_f121_t0_in += MUL_in[0]

	c_f121_t0_mem0 = S.Task('c_f121_t0_mem0', length=1, delay_cost=1)
	S += c_f121_t0_mem0 >= 1
	c_f121_t0_mem0 += INPUT_mem_r

	c_f121_t0_mem1 = S.Task('c_f121_t0_mem1', length=1, delay_cost=1)
	S += c_f121_t0_mem1 >= 1
	c_f121_t0_mem1 += INPUT_mem_r

	c_f011_t0_in = S.Task('c_f011_t0_in', length=1, delay_cost=1)
	S += c_f011_t0_in >= 2
	c_f011_t0_in += MUL_in[0]

	c_f011_t0_mem0 = S.Task('c_f011_t0_mem0', length=1, delay_cost=1)
	S += c_f011_t0_mem0 >= 2
	c_f011_t0_mem0 += INPUT_mem_r

	c_f011_t0_mem1 = S.Task('c_f011_t0_mem1', length=1, delay_cost=1)
	S += c_f011_t0_mem1 >= 2
	c_f011_t0_mem1 += INPUT_mem_r

	c_f121_t0 = S.Task('c_f121_t0', length=7, delay_cost=1)
	S += c_f121_t0 >= 2
	c_f121_t0 += MUL[0]

	c10_t0_t1_in = S.Task('c10_t0_t1_in', length=1, delay_cost=1)
	S += c10_t0_t1_in >= 3
	c10_t0_t1_in += MUL_in[0]

	c10_t0_t1_mem0 = S.Task('c10_t0_t1_mem0', length=1, delay_cost=1)
	S += c10_t0_t1_mem0 >= 3
	c10_t0_t1_mem0 += INPUT_mem_r

	c10_t0_t1_mem1 = S.Task('c10_t0_t1_mem1', length=1, delay_cost=1)
	S += c10_t0_t1_mem1 >= 3
	c10_t0_t1_mem1 += INPUT_mem_r

	c_f011_t0 = S.Task('c_f011_t0', length=7, delay_cost=1)
	S += c_f011_t0 >= 3
	c_f011_t0 += MUL[0]

	c10_t0_t1 = S.Task('c10_t0_t1', length=7, delay_cost=1)
	S += c10_t0_t1 >= 4
	c10_t0_t1 += MUL[0]

	c_f011_t1_in = S.Task('c_f011_t1_in', length=1, delay_cost=1)
	S += c_f011_t1_in >= 4
	c_f011_t1_in += MUL_in[0]

	c_f011_t1_mem0 = S.Task('c_f011_t1_mem0', length=1, delay_cost=1)
	S += c_f011_t1_mem0 >= 4
	c_f011_t1_mem0 += INPUT_mem_r

	c_f011_t1_mem1 = S.Task('c_f011_t1_mem1', length=1, delay_cost=1)
	S += c_f011_t1_mem1 >= 4
	c_f011_t1_mem1 += INPUT_mem_r

	c10_t0_t0_in = S.Task('c10_t0_t0_in', length=1, delay_cost=1)
	S += c10_t0_t0_in >= 5
	c10_t0_t0_in += MUL_in[0]

	c10_t0_t0_mem0 = S.Task('c10_t0_t0_mem0', length=1, delay_cost=1)
	S += c10_t0_t0_mem0 >= 5
	c10_t0_t0_mem0 += INPUT_mem_r

	c10_t0_t0_mem1 = S.Task('c10_t0_t0_mem1', length=1, delay_cost=1)
	S += c10_t0_t0_mem1 >= 5
	c10_t0_t0_mem1 += INPUT_mem_r

	c_f011_t1 = S.Task('c_f011_t1', length=7, delay_cost=1)
	S += c_f011_t1 >= 5
	c_f011_t1 += MUL[0]

	c10_t0_t0 = S.Task('c10_t0_t0', length=7, delay_cost=1)
	S += c10_t0_t0 >= 6
	c10_t0_t0 += MUL[0]

	c_f101_t1_in = S.Task('c_f101_t1_in', length=1, delay_cost=1)
	S += c_f101_t1_in >= 6
	c_f101_t1_in += MUL_in[0]

	c_f101_t1_mem0 = S.Task('c_f101_t1_mem0', length=1, delay_cost=1)
	S += c_f101_t1_mem0 >= 6
	c_f101_t1_mem0 += INPUT_mem_r

	c_f101_t1_mem1 = S.Task('c_f101_t1_mem1', length=1, delay_cost=1)
	S += c_f101_t1_mem1 >= 6
	c_f101_t1_mem1 += INPUT_mem_r

	c001_t0_in = S.Task('c001_t0_in', length=1, delay_cost=1)
	S += c001_t0_in >= 7
	c001_t0_in += MUL_in[0]

	c001_t0_mem0 = S.Task('c001_t0_mem0', length=1, delay_cost=1)
	S += c001_t0_mem0 >= 7
	c001_t0_mem0 += INPUT_mem_r

	c001_t0_mem1 = S.Task('c001_t0_mem1', length=1, delay_cost=1)
	S += c001_t0_mem1 >= 7
	c001_t0_mem1 += INPUT_mem_r

	c_f101_t1 = S.Task('c_f101_t1', length=7, delay_cost=1)
	S += c_f101_t1 >= 7
	c_f101_t1 += MUL[0]

	c001_t0 = S.Task('c001_t0', length=7, delay_cost=1)
	S += c001_t0 >= 8
	c001_t0 += MUL[0]

	c_f021_t0_in = S.Task('c_f021_t0_in', length=1, delay_cost=1)
	S += c_f021_t0_in >= 8
	c_f021_t0_in += MUL_in[0]

	c_f021_t0_mem0 = S.Task('c_f021_t0_mem0', length=1, delay_cost=1)
	S += c_f021_t0_mem0 >= 8
	c_f021_t0_mem0 += INPUT_mem_r

	c_f021_t0_mem1 = S.Task('c_f021_t0_mem1', length=1, delay_cost=1)
	S += c_f021_t0_mem1 >= 8
	c_f021_t0_mem1 += INPUT_mem_r

	c_f021_t0 = S.Task('c_f021_t0', length=7, delay_cost=1)
	S += c_f021_t0 >= 9
	c_f021_t0 += MUL[0]

	c_f121_t1_in = S.Task('c_f121_t1_in', length=1, delay_cost=1)
	S += c_f121_t1_in >= 9
	c_f121_t1_in += MUL_in[0]

	c_f121_t1_mem0 = S.Task('c_f121_t1_mem0', length=1, delay_cost=1)
	S += c_f121_t1_mem0 >= 9
	c_f121_t1_mem0 += INPUT_mem_r

	c_f121_t1_mem1 = S.Task('c_f121_t1_mem1', length=1, delay_cost=1)
	S += c_f121_t1_mem1 >= 9
	c_f121_t1_mem1 += INPUT_mem_r

	c_f111_t0_in = S.Task('c_f111_t0_in', length=1, delay_cost=1)
	S += c_f111_t0_in >= 10
	c_f111_t0_in += MUL_in[0]

	c_f111_t0_mem0 = S.Task('c_f111_t0_mem0', length=1, delay_cost=1)
	S += c_f111_t0_mem0 >= 10
	c_f111_t0_mem0 += INPUT_mem_r

	c_f111_t0_mem1 = S.Task('c_f111_t0_mem1', length=1, delay_cost=1)
	S += c_f111_t0_mem1 >= 10
	c_f111_t0_mem1 += INPUT_mem_r

	c_f121_t1 = S.Task('c_f121_t1', length=7, delay_cost=1)
	S += c_f121_t1 >= 10
	c_f121_t1 += MUL[0]

	c_f101_t0_in = S.Task('c_f101_t0_in', length=1, delay_cost=1)
	S += c_f101_t0_in >= 11
	c_f101_t0_in += MUL_in[0]

	c_f101_t0_mem0 = S.Task('c_f101_t0_mem0', length=1, delay_cost=1)
	S += c_f101_t0_mem0 >= 11
	c_f101_t0_mem0 += INPUT_mem_r

	c_f101_t0_mem1 = S.Task('c_f101_t0_mem1', length=1, delay_cost=1)
	S += c_f101_t0_mem1 >= 11
	c_f101_t0_mem1 += INPUT_mem_r

	c_f111_t0 = S.Task('c_f111_t0', length=7, delay_cost=1)
	S += c_f111_t0 >= 11
	c_f111_t0 += MUL[0]

	c_f021_t1_in = S.Task('c_f021_t1_in', length=1, delay_cost=1)
	S += c_f021_t1_in >= 12
	c_f021_t1_in += MUL_in[0]

	c_f021_t1_mem0 = S.Task('c_f021_t1_mem0', length=1, delay_cost=1)
	S += c_f021_t1_mem0 >= 12
	c_f021_t1_mem0 += INPUT_mem_r

	c_f021_t1_mem1 = S.Task('c_f021_t1_mem1', length=1, delay_cost=1)
	S += c_f021_t1_mem1 >= 12
	c_f021_t1_mem1 += INPUT_mem_r

	c_f101_t0 = S.Task('c_f101_t0', length=7, delay_cost=1)
	S += c_f101_t0 >= 12
	c_f101_t0 += MUL[0]

	c001_t1_in = S.Task('c001_t1_in', length=1, delay_cost=1)
	S += c001_t1_in >= 13
	c001_t1_in += MUL_in[0]

	c001_t1_mem0 = S.Task('c001_t1_mem0', length=1, delay_cost=1)
	S += c001_t1_mem0 >= 13
	c001_t1_mem0 += INPUT_mem_r

	c001_t1_mem1 = S.Task('c001_t1_mem1', length=1, delay_cost=1)
	S += c001_t1_mem1 >= 13
	c001_t1_mem1 += INPUT_mem_r

	c_f021_t1 = S.Task('c_f021_t1', length=7, delay_cost=1)
	S += c_f021_t1 >= 13
	c_f021_t1 += MUL[0]

	c001_t1 = S.Task('c001_t1', length=7, delay_cost=1)
	S += c001_t1 >= 14
	c001_t1 += MUL[0]

	c10_t30_mem0 = S.Task('c10_t30_mem0', length=1, delay_cost=1)
	S += c10_t30_mem0 >= 14
	c10_t30_mem0 += INPUT_mem_r

	c10_t30_mem1 = S.Task('c10_t30_mem1', length=1, delay_cost=1)
	S += c10_t30_mem1 >= 14
	c10_t30_mem1 += INPUT_mem_r

	c10_t30 = S.Task('c10_t30', length=1, delay_cost=1)
	S += c10_t30 >= 15
	c10_t30 += ADD[1]

	c_f101_t2_mem0 = S.Task('c_f101_t2_mem0', length=1, delay_cost=1)
	S += c_f101_t2_mem0 >= 15
	c_f101_t2_mem0 += INPUT_mem_r

	c_f101_t2_mem1 = S.Task('c_f101_t2_mem1', length=1, delay_cost=1)
	S += c_f101_t2_mem1 >= 15
	c_f101_t2_mem1 += INPUT_mem_r

	c_f021_t2_mem0 = S.Task('c_f021_t2_mem0', length=1, delay_cost=1)
	S += c_f021_t2_mem0 >= 16
	c_f021_t2_mem0 += INPUT_mem_r

	c_f021_t2_mem1 = S.Task('c_f021_t2_mem1', length=1, delay_cost=1)
	S += c_f021_t2_mem1 >= 16
	c_f021_t2_mem1 += INPUT_mem_r

	c_f101_t2 = S.Task('c_f101_t2', length=1, delay_cost=1)
	S += c_f101_t2 >= 16
	c_f101_t2 += ADD[0]

	c_f011_t3_mem0 = S.Task('c_f011_t3_mem0', length=1, delay_cost=1)
	S += c_f011_t3_mem0 >= 17
	c_f011_t3_mem0 += INPUT_mem_r

	c_f011_t3_mem1 = S.Task('c_f011_t3_mem1', length=1, delay_cost=1)
	S += c_f011_t3_mem1 >= 17
	c_f011_t3_mem1 += INPUT_mem_r

	c_f021_t2 = S.Task('c_f021_t2', length=1, delay_cost=1)
	S += c_f021_t2 >= 17
	c_f021_t2 += ADD[0]

	c10_t1_t3_mem0 = S.Task('c10_t1_t3_mem0', length=1, delay_cost=1)
	S += c10_t1_t3_mem0 >= 18
	c10_t1_t3_mem0 += INPUT_mem_r

	c10_t1_t3_mem1 = S.Task('c10_t1_t3_mem1', length=1, delay_cost=1)
	S += c10_t1_t3_mem1 >= 18
	c10_t1_t3_mem1 += INPUT_mem_r

	c_f011_t3 = S.Task('c_f011_t3', length=1, delay_cost=1)
	S += c_f011_t3 >= 18
	c_f011_t3 += ADD[0]

	c10_t1_t3 = S.Task('c10_t1_t3', length=1, delay_cost=1)
	S += c10_t1_t3 >= 19
	c10_t1_t3 += ADD[0]

	c_f021_t3_mem0 = S.Task('c_f021_t3_mem0', length=1, delay_cost=1)
	S += c_f021_t3_mem0 >= 19
	c_f021_t3_mem0 += INPUT_mem_r

	c_f021_t3_mem1 = S.Task('c_f021_t3_mem1', length=1, delay_cost=1)
	S += c_f021_t3_mem1 >= 19
	c_f021_t3_mem1 += INPUT_mem_r

	c_f021_t3 = S.Task('c_f021_t3', length=1, delay_cost=1)
	S += c_f021_t3 >= 20
	c_f021_t3 += ADD[0]

	c_f111_t3_mem0 = S.Task('c_f111_t3_mem0', length=1, delay_cost=1)
	S += c_f111_t3_mem0 >= 20
	c_f111_t3_mem0 += INPUT_mem_r

	c_f111_t3_mem1 = S.Task('c_f111_t3_mem1', length=1, delay_cost=1)
	S += c_f111_t3_mem1 >= 20
	c_f111_t3_mem1 += INPUT_mem_r

	c_f011_t2_mem0 = S.Task('c_f011_t2_mem0', length=1, delay_cost=1)
	S += c_f011_t2_mem0 >= 21
	c_f011_t2_mem0 += INPUT_mem_r

	c_f011_t2_mem1 = S.Task('c_f011_t2_mem1', length=1, delay_cost=1)
	S += c_f011_t2_mem1 >= 21
	c_f011_t2_mem1 += INPUT_mem_r

	c_f111_t3 = S.Task('c_f111_t3', length=1, delay_cost=1)
	S += c_f111_t3 >= 21
	c_f111_t3 += ADD[3]

	c_f011_t2 = S.Task('c_f011_t2', length=1, delay_cost=1)
	S += c_f011_t2 >= 22
	c_f011_t2 += ADD[3]

	c_f111_t2_mem0 = S.Task('c_f111_t2_mem0', length=1, delay_cost=1)
	S += c_f111_t2_mem0 >= 22
	c_f111_t2_mem0 += INPUT_mem_r

	c_f111_t2_mem1 = S.Task('c_f111_t2_mem1', length=1, delay_cost=1)
	S += c_f111_t2_mem1 >= 22
	c_f111_t2_mem1 += INPUT_mem_r

	c10_t0_t3_mem0 = S.Task('c10_t0_t3_mem0', length=1, delay_cost=1)
	S += c10_t0_t3_mem0 >= 23
	c10_t0_t3_mem0 += INPUT_mem_r

	c10_t0_t3_mem1 = S.Task('c10_t0_t3_mem1', length=1, delay_cost=1)
	S += c10_t0_t3_mem1 >= 23
	c10_t0_t3_mem1 += INPUT_mem_r

	c_f111_t2 = S.Task('c_f111_t2', length=1, delay_cost=1)
	S += c_f111_t2 >= 23
	c_f111_t2 += ADD[3]

	c10_t0_t3 = S.Task('c10_t0_t3', length=1, delay_cost=1)
	S += c10_t0_t3 >= 24
	c10_t0_t3 += ADD[0]

	c_f101_t3_mem0 = S.Task('c_f101_t3_mem0', length=1, delay_cost=1)
	S += c_f101_t3_mem0 >= 24
	c_f101_t3_mem0 += INPUT_mem_r

	c_f101_t3_mem1 = S.Task('c_f101_t3_mem1', length=1, delay_cost=1)
	S += c_f101_t3_mem1 >= 24
	c_f101_t3_mem1 += INPUT_mem_r

	c10_t0_t2_mem0 = S.Task('c10_t0_t2_mem0', length=1, delay_cost=1)
	S += c10_t0_t2_mem0 >= 25
	c10_t0_t2_mem0 += INPUT_mem_r

	c10_t0_t2_mem1 = S.Task('c10_t0_t2_mem1', length=1, delay_cost=1)
	S += c10_t0_t2_mem1 >= 25
	c10_t0_t2_mem1 += INPUT_mem_r

	c_f101_t3 = S.Task('c_f101_t3', length=1, delay_cost=1)
	S += c_f101_t3 >= 25
	c_f101_t3 += ADD[2]

	c001_t3_mem0 = S.Task('c001_t3_mem0', length=1, delay_cost=1)
	S += c001_t3_mem0 >= 26
	c001_t3_mem0 += INPUT_mem_r

	c001_t3_mem1 = S.Task('c001_t3_mem1', length=1, delay_cost=1)
	S += c001_t3_mem1 >= 26
	c001_t3_mem1 += INPUT_mem_r

	c10_t0_t2 = S.Task('c10_t0_t2', length=1, delay_cost=1)
	S += c10_t0_t2 >= 26
	c10_t0_t2 += ADD[0]

	c001_t2_mem0 = S.Task('c001_t2_mem0', length=1, delay_cost=1)
	S += c001_t2_mem0 >= 27
	c001_t2_mem0 += INPUT_mem_r

	c001_t2_mem1 = S.Task('c001_t2_mem1', length=1, delay_cost=1)
	S += c001_t2_mem1 >= 27
	c001_t2_mem1 += INPUT_mem_r

	c001_t3 = S.Task('c001_t3', length=1, delay_cost=1)
	S += c001_t3 >= 27
	c001_t3 += ADD[2]

	c001_t2 = S.Task('c001_t2', length=1, delay_cost=1)
	S += c001_t2 >= 28
	c001_t2 += ADD[1]

	c_f121_t3_mem0 = S.Task('c_f121_t3_mem0', length=1, delay_cost=1)
	S += c_f121_t3_mem0 >= 28
	c_f121_t3_mem0 += INPUT_mem_r

	c_f121_t3_mem1 = S.Task('c_f121_t3_mem1', length=1, delay_cost=1)
	S += c_f121_t3_mem1 >= 28
	c_f121_t3_mem1 += INPUT_mem_r

	c_f121_t2_mem0 = S.Task('c_f121_t2_mem0', length=1, delay_cost=1)
	S += c_f121_t2_mem0 >= 29
	c_f121_t2_mem0 += INPUT_mem_r

	c_f121_t2_mem1 = S.Task('c_f121_t2_mem1', length=1, delay_cost=1)
	S += c_f121_t2_mem1 >= 29
	c_f121_t2_mem1 += INPUT_mem_r

	c_f121_t3 = S.Task('c_f121_t3', length=1, delay_cost=1)
	S += c_f121_t3 >= 29
	c_f121_t3 += ADD[1]

	c11_t0_t1_in = S.Task('c11_t0_t1_in', length=1, delay_cost=1)
	S += c11_t0_t1_in >= 30
	c11_t0_t1_in += MUL_in[0]

	c11_t0_t1_mem0 = S.Task('c11_t0_t1_mem0', length=1, delay_cost=1)
	S += c11_t0_t1_mem0 >= 30
	c11_t0_t1_mem0 += INPUT_mem_r

	c11_t0_t1_mem1 = S.Task('c11_t0_t1_mem1', length=1, delay_cost=1)
	S += c11_t0_t1_mem1 >= 30
	c11_t0_t1_mem1 += INPUT_mem_r

	c_f121_t2 = S.Task('c_f121_t2', length=1, delay_cost=1)
	S += c_f121_t2 >= 30
	c_f121_t2 += ADD[3]

	c11_t0_t0_in = S.Task('c11_t0_t0_in', length=1, delay_cost=1)
	S += c11_t0_t0_in >= 31
	c11_t0_t0_in += MUL_in[0]

	c11_t0_t0_mem0 = S.Task('c11_t0_t0_mem0', length=1, delay_cost=1)
	S += c11_t0_t0_mem0 >= 31
	c11_t0_t0_mem0 += INPUT_mem_r

	c11_t0_t0_mem1 = S.Task('c11_t0_t0_mem1', length=1, delay_cost=1)
	S += c11_t0_t0_mem1 >= 31
	c11_t0_t0_mem1 += INPUT_mem_r

	c11_t0_t1 = S.Task('c11_t0_t1', length=7, delay_cost=1)
	S += c11_t0_t1 >= 31
	c11_t0_t1 += MUL[0]

	c0000_mem0 = S.Task('c0000_mem0', length=1, delay_cost=1)
	S += c0000_mem0 >= 32
	c0000_mem0 += INPUT_mem_r

	c0000_mem1 = S.Task('c0000_mem1', length=1, delay_cost=1)
	S += c0000_mem1 >= 32
	c0000_mem1 += INPUT_mem_r

	c11_t0_t0 = S.Task('c11_t0_t0', length=7, delay_cost=1)
	S += c11_t0_t0 >= 32
	c11_t0_t0 += MUL[0]

	c0000 = S.Task('c0000', length=1, delay_cost=1)
	S += c0000 >= 33
	c0000 += ADD[0]

	c02_t0_t1_in = S.Task('c02_t0_t1_in', length=1, delay_cost=1)
	S += c02_t0_t1_in >= 33
	c02_t0_t1_in += MUL_in[0]

	c02_t0_t1_mem0 = S.Task('c02_t0_t1_mem0', length=1, delay_cost=1)
	S += c02_t0_t1_mem0 >= 33
	c02_t0_t1_mem0 += INPUT_mem_r

	c02_t0_t1_mem1 = S.Task('c02_t0_t1_mem1', length=1, delay_cost=1)
	S += c02_t0_t1_mem1 >= 33
	c02_t0_t1_mem1 += INPUT_mem_r

	c0000_w = S.Task('c0000_w', length=1, delay_cost=1)
	S += c0000_w >= 34
	c0000_w += INPUT_mem_w

	c02_t0_t1 = S.Task('c02_t0_t1', length=7, delay_cost=1)
	S += c02_t0_t1 >= 34
	c02_t0_t1 += MUL[0]

	c12_t0_t0_in = S.Task('c12_t0_t0_in', length=1, delay_cost=1)
	S += c12_t0_t0_in >= 34
	c12_t0_t0_in += MUL_in[0]

	c12_t0_t0_mem0 = S.Task('c12_t0_t0_mem0', length=1, delay_cost=1)
	S += c12_t0_t0_mem0 >= 34
	c12_t0_t0_mem0 += INPUT_mem_r

	c12_t0_t0_mem1 = S.Task('c12_t0_t0_mem1', length=1, delay_cost=1)
	S += c12_t0_t0_mem1 >= 34
	c12_t0_t0_mem1 += INPUT_mem_r

	c12_t0_t0 = S.Task('c12_t0_t0', length=7, delay_cost=1)
	S += c12_t0_t0 >= 35
	c12_t0_t0 += MUL[0]

	c12_t0_t1_in = S.Task('c12_t0_t1_in', length=1, delay_cost=1)
	S += c12_t0_t1_in >= 35
	c12_t0_t1_in += MUL_in[0]

	c12_t0_t1_mem0 = S.Task('c12_t0_t1_mem0', length=1, delay_cost=1)
	S += c12_t0_t1_mem0 >= 35
	c12_t0_t1_mem0 += INPUT_mem_r

	c12_t0_t1_mem1 = S.Task('c12_t0_t1_mem1', length=1, delay_cost=1)
	S += c12_t0_t1_mem1 >= 35
	c12_t0_t1_mem1 += INPUT_mem_r

	c02_t0_t0_in = S.Task('c02_t0_t0_in', length=1, delay_cost=1)
	S += c02_t0_t0_in >= 36
	c02_t0_t0_in += MUL_in[0]

	c02_t0_t0_mem0 = S.Task('c02_t0_t0_mem0', length=1, delay_cost=1)
	S += c02_t0_t0_mem0 >= 36
	c02_t0_t0_mem0 += INPUT_mem_r

	c02_t0_t0_mem1 = S.Task('c02_t0_t0_mem1', length=1, delay_cost=1)
	S += c02_t0_t0_mem1 >= 36
	c02_t0_t0_mem1 += INPUT_mem_r

	c12_t0_t1 = S.Task('c12_t0_t1', length=7, delay_cost=1)
	S += c12_t0_t1 >= 36
	c12_t0_t1 += MUL[0]

	c01_t0_t1_in = S.Task('c01_t0_t1_in', length=1, delay_cost=1)
	S += c01_t0_t1_in >= 37
	c01_t0_t1_in += MUL_in[0]

	c01_t0_t1_mem0 = S.Task('c01_t0_t1_mem0', length=1, delay_cost=1)
	S += c01_t0_t1_mem0 >= 37
	c01_t0_t1_mem0 += INPUT_mem_r

	c01_t0_t1_mem1 = S.Task('c01_t0_t1_mem1', length=1, delay_cost=1)
	S += c01_t0_t1_mem1 >= 37
	c01_t0_t1_mem1 += INPUT_mem_r

	c02_t0_t0 = S.Task('c02_t0_t0', length=7, delay_cost=1)
	S += c02_t0_t0 >= 37
	c02_t0_t0 += MUL[0]

	c01_t0_t0_in = S.Task('c01_t0_t0_in', length=1, delay_cost=1)
	S += c01_t0_t0_in >= 38
	c01_t0_t0_in += MUL_in[0]

	c01_t0_t0_mem0 = S.Task('c01_t0_t0_mem0', length=1, delay_cost=1)
	S += c01_t0_t0_mem0 >= 38
	c01_t0_t0_mem0 += INPUT_mem_r

	c01_t0_t0_mem1 = S.Task('c01_t0_t0_mem1', length=1, delay_cost=1)
	S += c01_t0_t0_mem1 >= 38
	c01_t0_t0_mem1 += INPUT_mem_r

	c01_t0_t1 = S.Task('c01_t0_t1', length=7, delay_cost=1)
	S += c01_t0_t1 >= 38
	c01_t0_t1 += MUL[0]

	c01_t0_t0 = S.Task('c01_t0_t0', length=7, delay_cost=1)
	S += c01_t0_t0 >= 39
	c01_t0_t0 += MUL[0]

	c01_t30_mem0 = S.Task('c01_t30_mem0', length=1, delay_cost=1)
	S += c01_t30_mem0 >= 39
	c01_t30_mem0 += INPUT_mem_r

	c01_t30_mem1 = S.Task('c01_t30_mem1', length=1, delay_cost=1)
	S += c01_t30_mem1 >= 39
	c01_t30_mem1 += INPUT_mem_r

	c01_t30 = S.Task('c01_t30', length=1, delay_cost=1)
	S += c01_t30 >= 40
	c01_t30 += ADD[2]

	c12_t31_mem0 = S.Task('c12_t31_mem0', length=1, delay_cost=1)
	S += c12_t31_mem0 >= 40
	c12_t31_mem0 += INPUT_mem_r

	c12_t31_mem1 = S.Task('c12_t31_mem1', length=1, delay_cost=1)
	S += c12_t31_mem1 >= 40
	c12_t31_mem1 += INPUT_mem_r

	c12_t0_t3_mem0 = S.Task('c12_t0_t3_mem0', length=1, delay_cost=1)
	S += c12_t0_t3_mem0 >= 41
	c12_t0_t3_mem0 += INPUT_mem_r

	c12_t0_t3_mem1 = S.Task('c12_t0_t3_mem1', length=1, delay_cost=1)
	S += c12_t0_t3_mem1 >= 41
	c12_t0_t3_mem1 += INPUT_mem_r

	c12_t31 = S.Task('c12_t31', length=1, delay_cost=1)
	S += c12_t31 >= 41
	c12_t31 += ADD[2]

	c02_t31_mem0 = S.Task('c02_t31_mem0', length=1, delay_cost=1)
	S += c02_t31_mem0 >= 42
	c02_t31_mem0 += INPUT_mem_r

	c02_t31_mem1 = S.Task('c02_t31_mem1', length=1, delay_cost=1)
	S += c02_t31_mem1 >= 42
	c02_t31_mem1 += INPUT_mem_r

	c12_t0_t3 = S.Task('c12_t0_t3', length=1, delay_cost=1)
	S += c12_t0_t3 >= 42
	c12_t0_t3 += ADD[0]

	c02_t30_mem0 = S.Task('c02_t30_mem0', length=1, delay_cost=1)
	S += c02_t30_mem0 >= 43
	c02_t30_mem0 += INPUT_mem_r

	c02_t30_mem1 = S.Task('c02_t30_mem1', length=1, delay_cost=1)
	S += c02_t30_mem1 >= 43
	c02_t30_mem1 += INPUT_mem_r

	c02_t31 = S.Task('c02_t31', length=1, delay_cost=1)
	S += c02_t31 >= 43
	c02_t31 += ADD[1]

	c02_t30 = S.Task('c02_t30', length=1, delay_cost=1)
	S += c02_t30 >= 44
	c02_t30 += ADD[0]

	c12_t0_t2_mem0 = S.Task('c12_t0_t2_mem0', length=1, delay_cost=1)
	S += c12_t0_t2_mem0 >= 44
	c12_t0_t2_mem0 += INPUT_mem_r

	c12_t0_t2_mem1 = S.Task('c12_t0_t2_mem1', length=1, delay_cost=1)
	S += c12_t0_t2_mem1 >= 44
	c12_t0_t2_mem1 += INPUT_mem_r

	c12_t0_t2 = S.Task('c12_t0_t2', length=1, delay_cost=1)
	S += c12_t0_t2 >= 45
	c12_t0_t2 += ADD[0]

	c12_t30_mem0 = S.Task('c12_t30_mem0', length=1, delay_cost=1)
	S += c12_t30_mem0 >= 45
	c12_t30_mem0 += INPUT_mem_r

	c12_t30_mem1 = S.Task('c12_t30_mem1', length=1, delay_cost=1)
	S += c12_t30_mem1 >= 45
	c12_t30_mem1 += INPUT_mem_r

	c01_t0_t3_mem0 = S.Task('c01_t0_t3_mem0', length=1, delay_cost=1)
	S += c01_t0_t3_mem0 >= 46
	c01_t0_t3_mem0 += INPUT_mem_r

	c01_t0_t3_mem1 = S.Task('c01_t0_t3_mem1', length=1, delay_cost=1)
	S += c01_t0_t3_mem1 >= 46
	c01_t0_t3_mem1 += INPUT_mem_r

	c12_t30 = S.Task('c12_t30', length=1, delay_cost=1)
	S += c12_t30 >= 46
	c12_t30 += ADD[1]

	c01_t0_t3 = S.Task('c01_t0_t3', length=1, delay_cost=1)
	S += c01_t0_t3 >= 47
	c01_t0_t3 += ADD[3]

	c01_t31_mem0 = S.Task('c01_t31_mem0', length=1, delay_cost=1)
	S += c01_t31_mem0 >= 47
	c01_t31_mem0 += INPUT_mem_r

	c01_t31_mem1 = S.Task('c01_t31_mem1', length=1, delay_cost=1)
	S += c01_t31_mem1 >= 47
	c01_t31_mem1 += INPUT_mem_r

	c01_t31 = S.Task('c01_t31', length=1, delay_cost=1)
	S += c01_t31 >= 48
	c01_t31 += ADD[2]

	c11_t0_t2_mem0 = S.Task('c11_t0_t2_mem0', length=1, delay_cost=1)
	S += c11_t0_t2_mem0 >= 48
	c11_t0_t2_mem0 += INPUT_mem_r

	c11_t0_t2_mem1 = S.Task('c11_t0_t2_mem1', length=1, delay_cost=1)
	S += c11_t0_t2_mem1 >= 48
	c11_t0_t2_mem1 += INPUT_mem_r

	c11_t0_t2 = S.Task('c11_t0_t2', length=1, delay_cost=1)
	S += c11_t0_t2 >= 49
	c11_t0_t2 += ADD[1]

	c12_t1_t3_mem0 = S.Task('c12_t1_t3_mem0', length=1, delay_cost=1)
	S += c12_t1_t3_mem0 >= 49
	c12_t1_t3_mem0 += INPUT_mem_r

	c12_t1_t3_mem1 = S.Task('c12_t1_t3_mem1', length=1, delay_cost=1)
	S += c12_t1_t3_mem1 >= 49
	c12_t1_t3_mem1 += INPUT_mem_r

	c01_t0_t2_mem0 = S.Task('c01_t0_t2_mem0', length=1, delay_cost=1)
	S += c01_t0_t2_mem0 >= 50
	c01_t0_t2_mem0 += INPUT_mem_r

	c01_t0_t2_mem1 = S.Task('c01_t0_t2_mem1', length=1, delay_cost=1)
	S += c01_t0_t2_mem1 >= 50
	c01_t0_t2_mem1 += INPUT_mem_r

	c12_t1_t3 = S.Task('c12_t1_t3', length=1, delay_cost=1)
	S += c12_t1_t3 >= 50
	c12_t1_t3 += ADD[0]

	c01_t0_t2 = S.Task('c01_t0_t2', length=1, delay_cost=1)
	S += c01_t0_t2 >= 51
	c01_t0_t2 += ADD[0]

	c02_t1_t3_mem0 = S.Task('c02_t1_t3_mem0', length=1, delay_cost=1)
	S += c02_t1_t3_mem0 >= 51
	c02_t1_t3_mem0 += INPUT_mem_r

	c02_t1_t3_mem1 = S.Task('c02_t1_t3_mem1', length=1, delay_cost=1)
	S += c02_t1_t3_mem1 >= 51
	c02_t1_t3_mem1 += INPUT_mem_r

	c01_t1_t3_mem0 = S.Task('c01_t1_t3_mem0', length=1, delay_cost=1)
	S += c01_t1_t3_mem0 >= 52
	c01_t1_t3_mem0 += INPUT_mem_r

	c01_t1_t3_mem1 = S.Task('c01_t1_t3_mem1', length=1, delay_cost=1)
	S += c01_t1_t3_mem1 >= 52
	c01_t1_t3_mem1 += INPUT_mem_r

	c02_t1_t3 = S.Task('c02_t1_t3', length=1, delay_cost=1)
	S += c02_t1_t3 >= 52
	c02_t1_t3 += ADD[0]

	c01_t1_t3 = S.Task('c01_t1_t3', length=1, delay_cost=1)
	S += c01_t1_t3 >= 53
	c01_t1_t3 += ADD[2]

	c02_t0_t3_mem0 = S.Task('c02_t0_t3_mem0', length=1, delay_cost=1)
	S += c02_t0_t3_mem0 >= 53
	c02_t0_t3_mem0 += INPUT_mem_r

	c02_t0_t3_mem1 = S.Task('c02_t0_t3_mem1', length=1, delay_cost=1)
	S += c02_t0_t3_mem1 >= 53
	c02_t0_t3_mem1 += INPUT_mem_r

	c02_t0_t3 = S.Task('c02_t0_t3', length=1, delay_cost=1)
	S += c02_t0_t3 >= 54
	c02_t0_t3 += ADD[0]

	c10_t31_mem0 = S.Task('c10_t31_mem0', length=1, delay_cost=1)
	S += c10_t31_mem0 >= 54
	c10_t31_mem0 += INPUT_mem_r

	c10_t31_mem1 = S.Task('c10_t31_mem1', length=1, delay_cost=1)
	S += c10_t31_mem1 >= 54
	c10_t31_mem1 += INPUT_mem_r

	c02_t0_t2_mem0 = S.Task('c02_t0_t2_mem0', length=1, delay_cost=1)
	S += c02_t0_t2_mem0 >= 55
	c02_t0_t2_mem0 += INPUT_mem_r

	c02_t0_t2_mem1 = S.Task('c02_t0_t2_mem1', length=1, delay_cost=1)
	S += c02_t0_t2_mem1 >= 55
	c02_t0_t2_mem1 += INPUT_mem_r

	c10_t31 = S.Task('c10_t31', length=1, delay_cost=1)
	S += c10_t31 >= 55
	c10_t31 += ADD[0]

	c02_t0_t2 = S.Task('c02_t0_t2', length=1, delay_cost=1)
	S += c02_t0_t2 >= 56
	c02_t0_t2 += ADD[0]

	c11_t31_mem0 = S.Task('c11_t31_mem0', length=1, delay_cost=1)
	S += c11_t31_mem0 >= 56
	c11_t31_mem0 += INPUT_mem_r

	c11_t31_mem1 = S.Task('c11_t31_mem1', length=1, delay_cost=1)
	S += c11_t31_mem1 >= 56
	c11_t31_mem1 += INPUT_mem_r

	c11_t30_mem0 = S.Task('c11_t30_mem0', length=1, delay_cost=1)
	S += c11_t30_mem0 >= 57
	c11_t30_mem0 += INPUT_mem_r

	c11_t30_mem1 = S.Task('c11_t30_mem1', length=1, delay_cost=1)
	S += c11_t30_mem1 >= 57
	c11_t30_mem1 += INPUT_mem_r

	c11_t31 = S.Task('c11_t31', length=1, delay_cost=1)
	S += c11_t31 >= 57
	c11_t31 += ADD[0]

	c11_t1_t3_mem0 = S.Task('c11_t1_t3_mem0', length=1, delay_cost=1)
	S += c11_t1_t3_mem0 >= 58
	c11_t1_t3_mem0 += INPUT_mem_r

	c11_t1_t3_mem1 = S.Task('c11_t1_t3_mem1', length=1, delay_cost=1)
	S += c11_t1_t3_mem1 >= 58
	c11_t1_t3_mem1 += INPUT_mem_r

	c11_t30 = S.Task('c11_t30', length=1, delay_cost=1)
	S += c11_t30 >= 58
	c11_t30 += ADD[0]

	c11_t0_t3_mem0 = S.Task('c11_t0_t3_mem0', length=1, delay_cost=1)
	S += c11_t0_t3_mem0 >= 59
	c11_t0_t3_mem0 += INPUT_mem_r

	c11_t0_t3_mem1 = S.Task('c11_t0_t3_mem1', length=1, delay_cost=1)
	S += c11_t0_t3_mem1 >= 59
	c11_t0_t3_mem1 += INPUT_mem_r

	c11_t1_t3 = S.Task('c11_t1_t3', length=1, delay_cost=1)
	S += c11_t1_t3 >= 59
	c11_t1_t3 += ADD[0]

	c11_t0_t3 = S.Task('c11_t0_t3', length=1, delay_cost=1)
	S += c11_t0_t3 >= 60
	c11_t0_t3 += ADD[3]


	# new tasks
	c0001 = S.Task('c0001', length=1, delay_cost=1)
	c0001 += alt(ADD)

	S += 0<c0001

	c0001_mem0 = S.Task('c0001_mem0', length=1, delay_cost=1)
	c0001_mem0 += INPUT_mem_r
	S += c0001_mem0 <= c0001

	c0001_mem1 = S.Task('c0001_mem1', length=1, delay_cost=1)
	c0001_mem1 += INPUT_mem_r
	S += c0001_mem1 <= c0001

	c0001_w = S.Task('c0001_w', length=1, delay_cost=1)
	c0001_w += alt(INPUT_mem_w)
	S += c0001 <= c0001_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls24-315/scheduling/FROB_mul1_add4/FROB_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

