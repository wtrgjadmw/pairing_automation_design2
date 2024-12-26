from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 170
	S = Scenario("FROB_5", horizon=horizon)

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

	c_f111_s00_mem0 = S.Task('c_f111_s00_mem0', length=1, delay_cost=1)
	S += c_f111_s00_mem0 >= 7
	c_f111_s00_mem0 += MUL_mem[0]

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

	c_f111_s00 = S.Task('c_f111_s00', length=1, delay_cost=1)
	S += c_f111_s00 >= 8
	c_f111_s00 += ADD[1]

	c_f021_t0 = S.Task('c_f021_t0', length=7, delay_cost=1)
	S += c_f021_t0 >= 9
	c_f021_t0 += MUL[0]

	c_f111_s01_mem0 = S.Task('c_f111_s01_mem0', length=1, delay_cost=1)
	S += c_f111_s01_mem0 >= 9
	c_f111_s01_mem0 += ADD_mem[1]

	c_f111_s01_mem1 = S.Task('c_f111_s01_mem1', length=1, delay_cost=1)
	S += c_f111_s01_mem1 >= 9
	c_f111_s01_mem1 += MUL_mem[0]

	c_f121_t1_in = S.Task('c_f121_t1_in', length=1, delay_cost=1)
	S += c_f121_t1_in >= 9
	c_f121_t1_in += MUL_in[0]

	c_f121_t1_mem0 = S.Task('c_f121_t1_mem0', length=1, delay_cost=1)
	S += c_f121_t1_mem0 >= 9
	c_f121_t1_mem0 += INPUT_mem_r

	c_f121_t1_mem1 = S.Task('c_f121_t1_mem1', length=1, delay_cost=1)
	S += c_f121_t1_mem1 >= 9
	c_f121_t1_mem1 += INPUT_mem_r

	c10_t0_s00_mem0 = S.Task('c10_t0_s00_mem0', length=1, delay_cost=1)
	S += c10_t0_s00_mem0 >= 10
	c10_t0_s00_mem0 += MUL_mem[0]

	c_f111_s01 = S.Task('c_f111_s01', length=1, delay_cost=1)
	S += c_f111_s01 >= 10
	c_f111_s01 += ADD[2]

	c_f111_s02_mem0 = S.Task('c_f111_s02_mem0', length=1, delay_cost=1)
	S += c_f111_s02_mem0 >= 10
	c_f111_s02_mem0 += ADD_mem[2]

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

	c10_t0_s00 = S.Task('c10_t0_s00', length=1, delay_cost=1)
	S += c10_t0_s00 >= 11
	c10_t0_s00 += ADD[2]

	c_f011_t5_mem0 = S.Task('c_f011_t5_mem0', length=1, delay_cost=1)
	S += c_f011_t5_mem0 >= 11
	c_f011_t5_mem0 += MUL_mem[0]

	c_f011_t5_mem1 = S.Task('c_f011_t5_mem1', length=1, delay_cost=1)
	S += c_f011_t5_mem1 >= 11
	c_f011_t5_mem1 += MUL_mem[0]

	c_f101_t0_in = S.Task('c_f101_t0_in', length=1, delay_cost=1)
	S += c_f101_t0_in >= 11
	c_f101_t0_in += MUL_in[0]

	c_f101_t0_mem0 = S.Task('c_f101_t0_mem0', length=1, delay_cost=1)
	S += c_f101_t0_mem0 >= 11
	c_f101_t0_mem0 += INPUT_mem_r

	c_f101_t0_mem1 = S.Task('c_f101_t0_mem1', length=1, delay_cost=1)
	S += c_f101_t0_mem1 >= 11
	c_f101_t0_mem1 += INPUT_mem_r

	c_f111_s02 = S.Task('c_f111_s02', length=1, delay_cost=1)
	S += c_f111_s02 >= 11
	c_f111_s02 += ADD[1]

	c_f111_t0 = S.Task('c_f111_t0', length=7, delay_cost=1)
	S += c_f111_t0 >= 11
	c_f111_t0 += MUL[0]

	c10_t0_s01_mem0 = S.Task('c10_t0_s01_mem0', length=1, delay_cost=1)
	S += c10_t0_s01_mem0 >= 12
	c10_t0_s01_mem0 += ADD_mem[2]

	c10_t0_s01_mem1 = S.Task('c10_t0_s01_mem1', length=1, delay_cost=1)
	S += c10_t0_s01_mem1 >= 12
	c10_t0_s01_mem1 += MUL_mem[0]

	c_f011_s00_mem0 = S.Task('c_f011_s00_mem0', length=1, delay_cost=1)
	S += c_f011_s00_mem0 >= 12
	c_f011_s00_mem0 += MUL_mem[0]

	c_f011_t5 = S.Task('c_f011_t5', length=1, delay_cost=1)
	S += c_f011_t5 >= 12
	c_f011_t5 += ADD[2]

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

	c_f111_s03_mem0 = S.Task('c_f111_s03_mem0', length=1, delay_cost=1)
	S += c_f111_s03_mem0 >= 12
	c_f111_s03_mem0 += ADD_mem[1]

	c001_t1_in = S.Task('c001_t1_in', length=1, delay_cost=1)
	S += c001_t1_in >= 13
	c001_t1_in += MUL_in[0]

	c001_t1_mem0 = S.Task('c001_t1_mem0', length=1, delay_cost=1)
	S += c001_t1_mem0 >= 13
	c001_t1_mem0 += INPUT_mem_r

	c001_t1_mem1 = S.Task('c001_t1_mem1', length=1, delay_cost=1)
	S += c001_t1_mem1 >= 13
	c001_t1_mem1 += INPUT_mem_r

	c10_t0_s01 = S.Task('c10_t0_s01', length=1, delay_cost=1)
	S += c10_t0_s01 >= 13
	c10_t0_s01 += ADD[1]

	c10_t0_s02_mem0 = S.Task('c10_t0_s02_mem0', length=1, delay_cost=1)
	S += c10_t0_s02_mem0 >= 13
	c10_t0_s02_mem0 += ADD_mem[1]

	c_f011_s00 = S.Task('c_f011_s00', length=1, delay_cost=1)
	S += c_f011_s00 >= 13
	c_f011_s00 += ADD[2]

	c_f021_t1 = S.Task('c_f021_t1', length=7, delay_cost=1)
	S += c_f021_t1 >= 13
	c_f021_t1 += MUL[0]

	c_f101_s00_mem0 = S.Task('c_f101_s00_mem0', length=1, delay_cost=1)
	S += c_f101_s00_mem0 >= 13
	c_f101_s00_mem0 += MUL_mem[0]

	c_f111_s03 = S.Task('c_f111_s03', length=1, delay_cost=1)
	S += c_f111_s03 >= 13
	c_f111_s03 += ADD[3]

	c001_t1 = S.Task('c001_t1', length=7, delay_cost=1)
	S += c001_t1 >= 14
	c001_t1 += MUL[0]

	c10_t0_s02 = S.Task('c10_t0_s02', length=1, delay_cost=1)
	S += c10_t0_s02 >= 14
	c10_t0_s02 += ADD[1]

	c10_t0_t5_mem0 = S.Task('c10_t0_t5_mem0', length=1, delay_cost=1)
	S += c10_t0_t5_mem0 >= 14
	c10_t0_t5_mem0 += MUL_mem[0]

	c10_t0_t5_mem1 = S.Task('c10_t0_t5_mem1', length=1, delay_cost=1)
	S += c10_t0_t5_mem1 >= 14
	c10_t0_t5_mem1 += MUL_mem[0]

	c10_t30_mem0 = S.Task('c10_t30_mem0', length=1, delay_cost=1)
	S += c10_t30_mem0 >= 14
	c10_t30_mem0 += INPUT_mem_r

	c10_t30_mem1 = S.Task('c10_t30_mem1', length=1, delay_cost=1)
	S += c10_t30_mem1 >= 14
	c10_t30_mem1 += INPUT_mem_r

	c_f101_s00 = S.Task('c_f101_s00', length=1, delay_cost=1)
	S += c_f101_s00 >= 14
	c_f101_s00 += ADD[2]

	c10_t0_s03_mem0 = S.Task('c10_t0_s03_mem0', length=1, delay_cost=1)
	S += c10_t0_s03_mem0 >= 15
	c10_t0_s03_mem0 += ADD_mem[1]

	c10_t0_t5 = S.Task('c10_t0_t5', length=1, delay_cost=1)
	S += c10_t0_t5 >= 15
	c10_t0_t5 += ADD[2]

	c10_t30 = S.Task('c10_t30', length=1, delay_cost=1)
	S += c10_t30 >= 15
	c10_t30 += ADD[1]

	c_f011_s01_mem0 = S.Task('c_f011_s01_mem0', length=1, delay_cost=1)
	S += c_f011_s01_mem0 >= 15
	c_f011_s01_mem0 += ADD_mem[2]

	c_f011_s01_mem1 = S.Task('c_f011_s01_mem1', length=1, delay_cost=1)
	S += c_f011_s01_mem1 >= 15
	c_f011_s01_mem1 += MUL_mem[0]

	c_f101_s01_mem0 = S.Task('c_f101_s01_mem0', length=1, delay_cost=1)
	S += c_f101_s01_mem0 >= 15
	c_f101_s01_mem0 += ADD_mem[2]

	c_f101_s01_mem1 = S.Task('c_f101_s01_mem1', length=1, delay_cost=1)
	S += c_f101_s01_mem1 >= 15
	c_f101_s01_mem1 += MUL_mem[0]

	c_f101_t2_mem0 = S.Task('c_f101_t2_mem0', length=1, delay_cost=1)
	S += c_f101_t2_mem0 >= 15
	c_f101_t2_mem0 += INPUT_mem_r

	c_f101_t2_mem1 = S.Task('c_f101_t2_mem1', length=1, delay_cost=1)
	S += c_f101_t2_mem1 >= 15
	c_f101_t2_mem1 += INPUT_mem_r

	c10_t0_s03 = S.Task('c10_t0_s03', length=1, delay_cost=1)
	S += c10_t0_s03 >= 16
	c10_t0_s03 += ADD[2]

	c_f011_s01 = S.Task('c_f011_s01', length=1, delay_cost=1)
	S += c_f011_s01 >= 16
	c_f011_s01 += ADD[3]

	c_f011_s02_mem0 = S.Task('c_f011_s02_mem0', length=1, delay_cost=1)
	S += c_f011_s02_mem0 >= 16
	c_f011_s02_mem0 += ADD_mem[3]

	c_f021_t2_mem0 = S.Task('c_f021_t2_mem0', length=1, delay_cost=1)
	S += c_f021_t2_mem0 >= 16
	c_f021_t2_mem0 += INPUT_mem_r

	c_f021_t2_mem1 = S.Task('c_f021_t2_mem1', length=1, delay_cost=1)
	S += c_f021_t2_mem1 >= 16
	c_f021_t2_mem1 += INPUT_mem_r

	c_f101_s01 = S.Task('c_f101_s01', length=1, delay_cost=1)
	S += c_f101_s01 >= 16
	c_f101_s01 += ADD[1]

	c_f101_s02_mem0 = S.Task('c_f101_s02_mem0', length=1, delay_cost=1)
	S += c_f101_s02_mem0 >= 16
	c_f101_s02_mem0 += ADD_mem[1]

	c_f101_t2 = S.Task('c_f101_t2', length=1, delay_cost=1)
	S += c_f101_t2 >= 16
	c_f101_t2 += ADD[0]

	c_f121_t5_mem0 = S.Task('c_f121_t5_mem0', length=1, delay_cost=1)
	S += c_f121_t5_mem0 >= 16
	c_f121_t5_mem0 += MUL_mem[0]

	c_f121_t5_mem1 = S.Task('c_f121_t5_mem1', length=1, delay_cost=1)
	S += c_f121_t5_mem1 >= 16
	c_f121_t5_mem1 += MUL_mem[0]

	c_f011_s02 = S.Task('c_f011_s02', length=1, delay_cost=1)
	S += c_f011_s02 >= 17
	c_f011_s02 += ADD[1]

	c_f011_t3_mem0 = S.Task('c_f011_t3_mem0', length=1, delay_cost=1)
	S += c_f011_t3_mem0 >= 17
	c_f011_t3_mem0 += INPUT_mem_r

	c_f011_t3_mem1 = S.Task('c_f011_t3_mem1', length=1, delay_cost=1)
	S += c_f011_t3_mem1 >= 17
	c_f011_t3_mem1 += INPUT_mem_r

	c_f021_t2 = S.Task('c_f021_t2', length=1, delay_cost=1)
	S += c_f021_t2 >= 17
	c_f021_t2 += ADD[0]

	c_f101_s02 = S.Task('c_f101_s02', length=1, delay_cost=1)
	S += c_f101_s02 >= 17
	c_f101_s02 += ADD[3]

	c_f111_t5_mem0 = S.Task('c_f111_t5_mem0', length=1, delay_cost=1)
	S += c_f111_t5_mem0 >= 17
	c_f111_t5_mem0 += MUL_mem[0]

	c_f111_t5_mem1 = S.Task('c_f111_t5_mem1', length=1, delay_cost=1)
	S += c_f111_t5_mem1 >= 17
	c_f111_t5_mem1 += MUL_mem[0]

	c_f121_t5 = S.Task('c_f121_t5', length=1, delay_cost=1)
	S += c_f121_t5 >= 17
	c_f121_t5 += ADD[2]

	c10_t1_t3_mem0 = S.Task('c10_t1_t3_mem0', length=1, delay_cost=1)
	S += c10_t1_t3_mem0 >= 18
	c10_t1_t3_mem0 += INPUT_mem_r

	c10_t1_t3_mem1 = S.Task('c10_t1_t3_mem1', length=1, delay_cost=1)
	S += c10_t1_t3_mem1 >= 18
	c10_t1_t3_mem1 += INPUT_mem_r

	c_f011_s03_mem0 = S.Task('c_f011_s03_mem0', length=1, delay_cost=1)
	S += c_f011_s03_mem0 >= 18
	c_f011_s03_mem0 += ADD_mem[1]

	c_f011_t3 = S.Task('c_f011_t3', length=1, delay_cost=1)
	S += c_f011_t3 >= 18
	c_f011_t3 += ADD[0]

	c_f101_s03_mem0 = S.Task('c_f101_s03_mem0', length=1, delay_cost=1)
	S += c_f101_s03_mem0 >= 18
	c_f101_s03_mem0 += ADD_mem[3]

	c_f101_t5_mem0 = S.Task('c_f101_t5_mem0', length=1, delay_cost=1)
	S += c_f101_t5_mem0 >= 18
	c_f101_t5_mem0 += MUL_mem[0]

	c_f101_t5_mem1 = S.Task('c_f101_t5_mem1', length=1, delay_cost=1)
	S += c_f101_t5_mem1 >= 18
	c_f101_t5_mem1 += MUL_mem[0]

	c_f111_t5 = S.Task('c_f111_t5', length=1, delay_cost=1)
	S += c_f111_t5 >= 18
	c_f111_t5 += ADD[1]

	c10_t1_t3 = S.Task('c10_t1_t3', length=1, delay_cost=1)
	S += c10_t1_t3 >= 19
	c10_t1_t3 += ADD[0]

	c_f011_s03 = S.Task('c_f011_s03', length=1, delay_cost=1)
	S += c_f011_s03 >= 19
	c_f011_s03 += ADD[2]

	c_f021_s00_mem0 = S.Task('c_f021_s00_mem0', length=1, delay_cost=1)
	S += c_f021_s00_mem0 >= 19
	c_f021_s00_mem0 += MUL_mem[0]

	c_f021_t3_mem0 = S.Task('c_f021_t3_mem0', length=1, delay_cost=1)
	S += c_f021_t3_mem0 >= 19
	c_f021_t3_mem0 += INPUT_mem_r

	c_f021_t3_mem1 = S.Task('c_f021_t3_mem1', length=1, delay_cost=1)
	S += c_f021_t3_mem1 >= 19
	c_f021_t3_mem1 += INPUT_mem_r

	c_f101_s03 = S.Task('c_f101_s03', length=1, delay_cost=1)
	S += c_f101_s03 >= 19
	c_f101_s03 += ADD[1]

	c_f101_t5 = S.Task('c_f101_t5', length=1, delay_cost=1)
	S += c_f101_t5 >= 19
	c_f101_t5 += ADD[3]

	c_f121_s00_mem0 = S.Task('c_f121_s00_mem0', length=1, delay_cost=1)
	S += c_f121_s00_mem0 >= 19
	c_f121_s00_mem0 += MUL_mem[0]

	c001_t5_mem0 = S.Task('c001_t5_mem0', length=1, delay_cost=1)
	S += c001_t5_mem0 >= 20
	c001_t5_mem0 += MUL_mem[0]

	c001_t5_mem1 = S.Task('c001_t5_mem1', length=1, delay_cost=1)
	S += c001_t5_mem1 >= 20
	c001_t5_mem1 += MUL_mem[0]

	c_f021_s00 = S.Task('c_f021_s00', length=1, delay_cost=1)
	S += c_f021_s00 >= 20
	c_f021_s00 += ADD[2]

	c_f021_t3 = S.Task('c_f021_t3', length=1, delay_cost=1)
	S += c_f021_t3 >= 20
	c_f021_t3 += ADD[0]

	c_f021_t4_in = S.Task('c_f021_t4_in', length=1, delay_cost=1)
	S += c_f021_t4_in >= 20
	c_f021_t4_in += MUL_in[0]

	c_f021_t4_mem0 = S.Task('c_f021_t4_mem0', length=1, delay_cost=1)
	S += c_f021_t4_mem0 >= 20
	c_f021_t4_mem0 += ADD_mem[0]

	c_f021_t4_mem1 = S.Task('c_f021_t4_mem1', length=1, delay_cost=1)
	S += c_f021_t4_mem1 >= 20
	c_f021_t4_mem1 += ADD_mem[0]

	c_f111_t3_mem0 = S.Task('c_f111_t3_mem0', length=1, delay_cost=1)
	S += c_f111_t3_mem0 >= 20
	c_f111_t3_mem0 += INPUT_mem_r

	c_f111_t3_mem1 = S.Task('c_f111_t3_mem1', length=1, delay_cost=1)
	S += c_f111_t3_mem1 >= 20
	c_f111_t3_mem1 += INPUT_mem_r

	c_f121_s00 = S.Task('c_f121_s00', length=1, delay_cost=1)
	S += c_f121_s00 >= 20
	c_f121_s00 += ADD[1]

	c001_s00_mem0 = S.Task('c001_s00_mem0', length=1, delay_cost=1)
	S += c001_s00_mem0 >= 21
	c001_s00_mem0 += MUL_mem[0]

	c001_t5 = S.Task('c001_t5', length=1, delay_cost=1)
	S += c001_t5 >= 21
	c001_t5 += ADD[0]

	c_f011_t2_mem0 = S.Task('c_f011_t2_mem0', length=1, delay_cost=1)
	S += c_f011_t2_mem0 >= 21
	c_f011_t2_mem0 += INPUT_mem_r

	c_f011_t2_mem1 = S.Task('c_f011_t2_mem1', length=1, delay_cost=1)
	S += c_f011_t2_mem1 >= 21
	c_f011_t2_mem1 += INPUT_mem_r

	c_f021_s01_mem0 = S.Task('c_f021_s01_mem0', length=1, delay_cost=1)
	S += c_f021_s01_mem0 >= 21
	c_f021_s01_mem0 += ADD_mem[2]

	c_f021_s01_mem1 = S.Task('c_f021_s01_mem1', length=1, delay_cost=1)
	S += c_f021_s01_mem1 >= 21
	c_f021_s01_mem1 += MUL_mem[0]

	c_f021_t4 = S.Task('c_f021_t4', length=7, delay_cost=1)
	S += c_f021_t4 >= 21
	c_f021_t4 += MUL[0]

	c_f111_t3 = S.Task('c_f111_t3', length=1, delay_cost=1)
	S += c_f111_t3 >= 21
	c_f111_t3 += ADD[3]

	c001_s00 = S.Task('c001_s00', length=1, delay_cost=1)
	S += c001_s00 >= 22
	c001_s00 += ADD[1]

	c_f011_t2 = S.Task('c_f011_t2', length=1, delay_cost=1)
	S += c_f011_t2 >= 22
	c_f011_t2 += ADD[3]

	c_f011_t4_in = S.Task('c_f011_t4_in', length=1, delay_cost=1)
	S += c_f011_t4_in >= 22
	c_f011_t4_in += MUL_in[0]

	c_f011_t4_mem0 = S.Task('c_f011_t4_mem0', length=1, delay_cost=1)
	S += c_f011_t4_mem0 >= 22
	c_f011_t4_mem0 += ADD_mem[3]

	c_f011_t4_mem1 = S.Task('c_f011_t4_mem1', length=1, delay_cost=1)
	S += c_f011_t4_mem1 >= 22
	c_f011_t4_mem1 += ADD_mem[0]

	c_f021_s01 = S.Task('c_f021_s01', length=1, delay_cost=1)
	S += c_f021_s01 >= 22
	c_f021_s01 += ADD[0]

	c_f021_s02_mem0 = S.Task('c_f021_s02_mem0', length=1, delay_cost=1)
	S += c_f021_s02_mem0 >= 22
	c_f021_s02_mem0 += ADD_mem[0]

	c_f021_t5_mem0 = S.Task('c_f021_t5_mem0', length=1, delay_cost=1)
	S += c_f021_t5_mem0 >= 22
	c_f021_t5_mem0 += MUL_mem[0]

	c_f021_t5_mem1 = S.Task('c_f021_t5_mem1', length=1, delay_cost=1)
	S += c_f021_t5_mem1 >= 22
	c_f021_t5_mem1 += MUL_mem[0]

	c_f111_t2_mem0 = S.Task('c_f111_t2_mem0', length=1, delay_cost=1)
	S += c_f111_t2_mem0 >= 22
	c_f111_t2_mem0 += INPUT_mem_r

	c_f111_t2_mem1 = S.Task('c_f111_t2_mem1', length=1, delay_cost=1)
	S += c_f111_t2_mem1 >= 22
	c_f111_t2_mem1 += INPUT_mem_r

	c001_s01_mem0 = S.Task('c001_s01_mem0', length=1, delay_cost=1)
	S += c001_s01_mem0 >= 23
	c001_s01_mem0 += ADD_mem[1]

	c001_s01_mem1 = S.Task('c001_s01_mem1', length=1, delay_cost=1)
	S += c001_s01_mem1 >= 23
	c001_s01_mem1 += MUL_mem[0]

	c10_t0_t3_mem0 = S.Task('c10_t0_t3_mem0', length=1, delay_cost=1)
	S += c10_t0_t3_mem0 >= 23
	c10_t0_t3_mem0 += INPUT_mem_r

	c10_t0_t3_mem1 = S.Task('c10_t0_t3_mem1', length=1, delay_cost=1)
	S += c10_t0_t3_mem1 >= 23
	c10_t0_t3_mem1 += INPUT_mem_r

	c_f011_t4 = S.Task('c_f011_t4', length=7, delay_cost=1)
	S += c_f011_t4 >= 23
	c_f011_t4 += MUL[0]

	c_f021_s02 = S.Task('c_f021_s02', length=1, delay_cost=1)
	S += c_f021_s02 >= 23
	c_f021_s02 += ADD[0]

	c_f021_t5 = S.Task('c_f021_t5', length=1, delay_cost=1)
	S += c_f021_t5 >= 23
	c_f021_t5 += ADD[1]

	c_f111_t2 = S.Task('c_f111_t2', length=1, delay_cost=1)
	S += c_f111_t2 >= 23
	c_f111_t2 += ADD[3]

	c_f111_t4_in = S.Task('c_f111_t4_in', length=1, delay_cost=1)
	S += c_f111_t4_in >= 23
	c_f111_t4_in += MUL_in[0]

	c_f111_t4_mem0 = S.Task('c_f111_t4_mem0', length=1, delay_cost=1)
	S += c_f111_t4_mem0 >= 23
	c_f111_t4_mem0 += ADD_mem[3]

	c_f111_t4_mem1 = S.Task('c_f111_t4_mem1', length=1, delay_cost=1)
	S += c_f111_t4_mem1 >= 23
	c_f111_t4_mem1 += ADD_mem[3]

	c_f121_s01_mem0 = S.Task('c_f121_s01_mem0', length=1, delay_cost=1)
	S += c_f121_s01_mem0 >= 23
	c_f121_s01_mem0 += ADD_mem[1]

	c_f121_s01_mem1 = S.Task('c_f121_s01_mem1', length=1, delay_cost=1)
	S += c_f121_s01_mem1 >= 23
	c_f121_s01_mem1 += MUL_mem[0]

	c001_s01 = S.Task('c001_s01', length=1, delay_cost=1)
	S += c001_s01 >= 24
	c001_s01 += ADD[2]

	c001_s02_mem0 = S.Task('c001_s02_mem0', length=1, delay_cost=1)
	S += c001_s02_mem0 >= 24
	c001_s02_mem0 += ADD_mem[2]

	c10_t0_s04_mem0 = S.Task('c10_t0_s04_mem0', length=1, delay_cost=1)
	S += c10_t0_s04_mem0 >= 24
	c10_t0_s04_mem0 += ADD_mem[2]

	c10_t0_s04_mem1 = S.Task('c10_t0_s04_mem1', length=1, delay_cost=1)
	S += c10_t0_s04_mem1 >= 24
	c10_t0_s04_mem1 += MUL_mem[0]

	c10_t0_t3 = S.Task('c10_t0_t3', length=1, delay_cost=1)
	S += c10_t0_t3 >= 24
	c10_t0_t3 += ADD[0]

	c_f021_s03_mem0 = S.Task('c_f021_s03_mem0', length=1, delay_cost=1)
	S += c_f021_s03_mem0 >= 24
	c_f021_s03_mem0 += ADD_mem[0]

	c_f101_t3_mem0 = S.Task('c_f101_t3_mem0', length=1, delay_cost=1)
	S += c_f101_t3_mem0 >= 24
	c_f101_t3_mem0 += INPUT_mem_r

	c_f101_t3_mem1 = S.Task('c_f101_t3_mem1', length=1, delay_cost=1)
	S += c_f101_t3_mem1 >= 24
	c_f101_t3_mem1 += INPUT_mem_r

	c_f111_t4 = S.Task('c_f111_t4', length=7, delay_cost=1)
	S += c_f111_t4 >= 24
	c_f111_t4 += MUL[0]

	c_f121_s01 = S.Task('c_f121_s01', length=1, delay_cost=1)
	S += c_f121_s01 >= 24
	c_f121_s01 += ADD[1]

	c001_s02 = S.Task('c001_s02', length=1, delay_cost=1)
	S += c001_s02 >= 25
	c001_s02 += ADD[1]

	c10_t0_s04 = S.Task('c10_t0_s04', length=1, delay_cost=1)
	S += c10_t0_s04 >= 25
	c10_t0_s04 += ADD[0]

	c10_t0_t2_mem0 = S.Task('c10_t0_t2_mem0', length=1, delay_cost=1)
	S += c10_t0_t2_mem0 >= 25
	c10_t0_t2_mem0 += INPUT_mem_r

	c10_t0_t2_mem1 = S.Task('c10_t0_t2_mem1', length=1, delay_cost=1)
	S += c10_t0_t2_mem1 >= 25
	c10_t0_t2_mem1 += INPUT_mem_r

	c_f011_s04_mem0 = S.Task('c_f011_s04_mem0', length=1, delay_cost=1)
	S += c_f011_s04_mem0 >= 25
	c_f011_s04_mem0 += ADD_mem[2]

	c_f011_s04_mem1 = S.Task('c_f011_s04_mem1', length=1, delay_cost=1)
	S += c_f011_s04_mem1 >= 25
	c_f011_s04_mem1 += MUL_mem[0]

	c_f021_s03 = S.Task('c_f021_s03', length=1, delay_cost=1)
	S += c_f021_s03 >= 25
	c_f021_s03 += ADD[3]

	c_f101_t3 = S.Task('c_f101_t3', length=1, delay_cost=1)
	S += c_f101_t3 >= 25
	c_f101_t3 += ADD[2]

	c_f101_t4_in = S.Task('c_f101_t4_in', length=1, delay_cost=1)
	S += c_f101_t4_in >= 25
	c_f101_t4_in += MUL_in[0]

	c_f101_t4_mem0 = S.Task('c_f101_t4_mem0', length=1, delay_cost=1)
	S += c_f101_t4_mem0 >= 25
	c_f101_t4_mem0 += ADD_mem[0]

	c_f101_t4_mem1 = S.Task('c_f101_t4_mem1', length=1, delay_cost=1)
	S += c_f101_t4_mem1 >= 25
	c_f101_t4_mem1 += ADD_mem[2]

	c_f111_s04_mem0 = S.Task('c_f111_s04_mem0', length=1, delay_cost=1)
	S += c_f111_s04_mem0 >= 25
	c_f111_s04_mem0 += ADD_mem[3]

	c_f111_s04_mem1 = S.Task('c_f111_s04_mem1', length=1, delay_cost=1)
	S += c_f111_s04_mem1 >= 25
	c_f111_s04_mem1 += MUL_mem[0]

	c_f121_s02_mem0 = S.Task('c_f121_s02_mem0', length=1, delay_cost=1)
	S += c_f121_s02_mem0 >= 25
	c_f121_s02_mem0 += ADD_mem[1]

	c001_s03_mem0 = S.Task('c001_s03_mem0', length=1, delay_cost=1)
	S += c001_s03_mem0 >= 26
	c001_s03_mem0 += ADD_mem[1]

	c001_t3_mem0 = S.Task('c001_t3_mem0', length=1, delay_cost=1)
	S += c001_t3_mem0 >= 26
	c001_t3_mem0 += INPUT_mem_r

	c001_t3_mem1 = S.Task('c001_t3_mem1', length=1, delay_cost=1)
	S += c001_t3_mem1 >= 26
	c001_t3_mem1 += INPUT_mem_r

	c10_t0_t2 = S.Task('c10_t0_t2', length=1, delay_cost=1)
	S += c10_t0_t2 >= 26
	c10_t0_t2 += ADD[0]

	c10_t0_t4_in = S.Task('c10_t0_t4_in', length=1, delay_cost=1)
	S += c10_t0_t4_in >= 26
	c10_t0_t4_in += MUL_in[0]

	c10_t0_t4_mem0 = S.Task('c10_t0_t4_mem0', length=1, delay_cost=1)
	S += c10_t0_t4_mem0 >= 26
	c10_t0_t4_mem0 += ADD_mem[0]

	c10_t0_t4_mem1 = S.Task('c10_t0_t4_mem1', length=1, delay_cost=1)
	S += c10_t0_t4_mem1 >= 26
	c10_t0_t4_mem1 += ADD_mem[0]

	c_f011_s04 = S.Task('c_f011_s04', length=1, delay_cost=1)
	S += c_f011_s04 >= 26
	c_f011_s04 += ADD[2]

	c_f021_s04_mem0 = S.Task('c_f021_s04_mem0', length=1, delay_cost=1)
	S += c_f021_s04_mem0 >= 26
	c_f021_s04_mem0 += ADD_mem[3]

	c_f021_s04_mem1 = S.Task('c_f021_s04_mem1', length=1, delay_cost=1)
	S += c_f021_s04_mem1 >= 26
	c_f021_s04_mem1 += MUL_mem[0]

	c_f101_s04_mem0 = S.Task('c_f101_s04_mem0', length=1, delay_cost=1)
	S += c_f101_s04_mem0 >= 26
	c_f101_s04_mem0 += ADD_mem[1]

	c_f101_s04_mem1 = S.Task('c_f101_s04_mem1', length=1, delay_cost=1)
	S += c_f101_s04_mem1 >= 26
	c_f101_s04_mem1 += MUL_mem[0]

	c_f101_t4 = S.Task('c_f101_t4', length=7, delay_cost=1)
	S += c_f101_t4 >= 26
	c_f101_t4 += MUL[0]

	c_f111_s04 = S.Task('c_f111_s04', length=1, delay_cost=1)
	S += c_f111_s04 >= 26
	c_f111_s04 += ADD[3]

	c_f121_s02 = S.Task('c_f121_s02', length=1, delay_cost=1)
	S += c_f121_s02 >= 26
	c_f121_s02 += ADD[1]

	c001_s03 = S.Task('c001_s03', length=1, delay_cost=1)
	S += c001_s03 >= 27
	c001_s03 += ADD[3]

	c001_t2_mem0 = S.Task('c001_t2_mem0', length=1, delay_cost=1)
	S += c001_t2_mem0 >= 27
	c001_t2_mem0 += INPUT_mem_r

	c001_t2_mem1 = S.Task('c001_t2_mem1', length=1, delay_cost=1)
	S += c001_t2_mem1 >= 27
	c001_t2_mem1 += INPUT_mem_r

	c001_t3 = S.Task('c001_t3', length=1, delay_cost=1)
	S += c001_t3 >= 27
	c001_t3 += ADD[2]

	c10_t0_t4 = S.Task('c10_t0_t4', length=7, delay_cost=1)
	S += c10_t0_t4 >= 27
	c10_t0_t4 += MUL[0]

	c_f021_s04 = S.Task('c_f021_s04', length=1, delay_cost=1)
	S += c_f021_s04 >= 27
	c_f021_s04 += ADD[0]

	c_f101_s04 = S.Task('c_f101_s04', length=1, delay_cost=1)
	S += c_f101_s04 >= 27
	c_f101_s04 += ADD[1]

	c_f121_s03_mem0 = S.Task('c_f121_s03_mem0', length=1, delay_cost=1)
	S += c_f121_s03_mem0 >= 27
	c_f121_s03_mem0 += ADD_mem[1]

	c001_s04_mem0 = S.Task('c001_s04_mem0', length=1, delay_cost=1)
	S += c001_s04_mem0 >= 28
	c001_s04_mem0 += ADD_mem[3]

	c001_s04_mem1 = S.Task('c001_s04_mem1', length=1, delay_cost=1)
	S += c001_s04_mem1 >= 28
	c001_s04_mem1 += MUL_mem[0]

	c001_t2 = S.Task('c001_t2', length=1, delay_cost=1)
	S += c001_t2 >= 28
	c001_t2 += ADD[1]

	c001_t4_in = S.Task('c001_t4_in', length=1, delay_cost=1)
	S += c001_t4_in >= 28
	c001_t4_in += MUL_in[0]

	c001_t4_mem0 = S.Task('c001_t4_mem0', length=1, delay_cost=1)
	S += c001_t4_mem0 >= 28
	c001_t4_mem0 += ADD_mem[1]

	c001_t4_mem1 = S.Task('c001_t4_mem1', length=1, delay_cost=1)
	S += c001_t4_mem1 >= 28
	c001_t4_mem1 += ADD_mem[2]

	c_f0211_mem0 = S.Task('c_f0211_mem0', length=1, delay_cost=1)
	S += c_f0211_mem0 >= 28
	c_f0211_mem0 += MUL_mem[0]

	c_f0211_mem1 = S.Task('c_f0211_mem1', length=1, delay_cost=1)
	S += c_f0211_mem1 >= 28
	c_f0211_mem1 += ADD_mem[1]

	c_f121_s03 = S.Task('c_f121_s03', length=1, delay_cost=1)
	S += c_f121_s03 >= 28
	c_f121_s03 += ADD[0]

	c_f121_t3_mem0 = S.Task('c_f121_t3_mem0', length=1, delay_cost=1)
	S += c_f121_t3_mem0 >= 28
	c_f121_t3_mem0 += INPUT_mem_r

	c_f121_t3_mem1 = S.Task('c_f121_t3_mem1', length=1, delay_cost=1)
	S += c_f121_t3_mem1 >= 28
	c_f121_t3_mem1 += INPUT_mem_r

	c001_s04 = S.Task('c001_s04', length=1, delay_cost=1)
	S += c001_s04 >= 29
	c001_s04 += ADD[2]

	c001_t4 = S.Task('c001_t4', length=7, delay_cost=1)
	S += c001_t4 >= 29
	c001_t4 += MUL[0]

	c_f0211 = S.Task('c_f0211', length=1, delay_cost=1)
	S += c_f0211 >= 29
	c_f0211 += ADD[0]

	c_f121_s04_mem0 = S.Task('c_f121_s04_mem0', length=1, delay_cost=1)
	S += c_f121_s04_mem0 >= 29
	c_f121_s04_mem0 += ADD_mem[0]

	c_f121_s04_mem1 = S.Task('c_f121_s04_mem1', length=1, delay_cost=1)
	S += c_f121_s04_mem1 >= 29
	c_f121_s04_mem1 += MUL_mem[0]

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

	c_f0111_mem0 = S.Task('c_f0111_mem0', length=1, delay_cost=1)
	S += c_f0111_mem0 >= 30
	c_f0111_mem0 += MUL_mem[0]

	c_f0111_mem1 = S.Task('c_f0111_mem1', length=1, delay_cost=1)
	S += c_f0111_mem1 >= 30
	c_f0111_mem1 += ADD_mem[2]

	c_f121_s04 = S.Task('c_f121_s04', length=1, delay_cost=1)
	S += c_f121_s04 >= 30
	c_f121_s04 += ADD[0]

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

	c_f0111 = S.Task('c_f0111', length=1, delay_cost=1)
	S += c_f0111 >= 31
	c_f0111 += ADD[1]

	c_f1111_mem0 = S.Task('c_f1111_mem0', length=1, delay_cost=1)
	S += c_f1111_mem0 >= 31
	c_f1111_mem0 += MUL_mem[0]

	c_f1111_mem1 = S.Task('c_f1111_mem1', length=1, delay_cost=1)
	S += c_f1111_mem1 >= 31
	c_f1111_mem1 += ADD_mem[1]

	c0000_mem0 = S.Task('c0000_mem0', length=1, delay_cost=1)
	S += c0000_mem0 >= 32
	c0000_mem0 += INPUT_mem_r

	c0000_mem1 = S.Task('c0000_mem1', length=1, delay_cost=1)
	S += c0000_mem1 >= 32
	c0000_mem1 += INPUT_mem_r

	c11_t0_t0 = S.Task('c11_t0_t0', length=7, delay_cost=1)
	S += c11_t0_t0 >= 32
	c11_t0_t0 += MUL[0]

	c_f1111 = S.Task('c_f1111', length=1, delay_cost=1)
	S += c_f1111 >= 32
	c_f1111 += ADD[1]

	c_f121_t4_in = S.Task('c_f121_t4_in', length=1, delay_cost=1)
	S += c_f121_t4_in >= 32
	c_f121_t4_in += MUL_in[0]

	c_f121_t4_mem0 = S.Task('c_f121_t4_mem0', length=1, delay_cost=1)
	S += c_f121_t4_mem0 >= 32
	c_f121_t4_mem0 += ADD_mem[3]

	c_f121_t4_mem1 = S.Task('c_f121_t4_mem1', length=1, delay_cost=1)
	S += c_f121_t4_mem1 >= 32
	c_f121_t4_mem1 += ADD_mem[1]

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

	c_f1011_mem0 = S.Task('c_f1011_mem0', length=1, delay_cost=1)
	S += c_f1011_mem0 >= 33
	c_f1011_mem0 += MUL_mem[0]

	c_f1011_mem1 = S.Task('c_f1011_mem1', length=1, delay_cost=1)
	S += c_f1011_mem1 >= 33
	c_f1011_mem1 += ADD_mem[3]

	c_f121_t4 = S.Task('c_f121_t4', length=7, delay_cost=1)
	S += c_f121_t4 >= 33
	c_f121_t4 += MUL[0]

	c0000_w = S.Task('c0000_w', length=1, delay_cost=1)
	S += c0000_w >= 34
	c0000_w += INPUT_mem_w

	c02_t0_t1 = S.Task('c02_t0_t1', length=7, delay_cost=1)
	S += c02_t0_t1 >= 34
	c02_t0_t1 += MUL[0]

	c10_t01_mem0 = S.Task('c10_t01_mem0', length=1, delay_cost=1)
	S += c10_t01_mem0 >= 34
	c10_t01_mem0 += MUL_mem[0]

	c10_t01_mem1 = S.Task('c10_t01_mem1', length=1, delay_cost=1)
	S += c10_t01_mem1 >= 34
	c10_t01_mem1 += ADD_mem[2]

	c12_t0_t0_in = S.Task('c12_t0_t0_in', length=1, delay_cost=1)
	S += c12_t0_t0_in >= 34
	c12_t0_t0_in += MUL_in[0]

	c12_t0_t0_mem0 = S.Task('c12_t0_t0_mem0', length=1, delay_cost=1)
	S += c12_t0_t0_mem0 >= 34
	c12_t0_t0_mem0 += INPUT_mem_r

	c12_t0_t0_mem1 = S.Task('c12_t0_t0_mem1', length=1, delay_cost=1)
	S += c12_t0_t0_mem1 >= 34
	c12_t0_t0_mem1 += INPUT_mem_r

	c_f1011 = S.Task('c_f1011', length=1, delay_cost=1)
	S += c_f1011 >= 34
	c_f1011 += ADD[1]

	c10_t01 = S.Task('c10_t01', length=1, delay_cost=1)
	S += c10_t01 >= 35
	c10_t01 += ADD[1]

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

	c0011_mem0 = S.Task('c0011_mem0', length=1, delay_cost=1)
	S += c0011_mem0 >= 36
	c0011_mem0 += MUL_mem[0]

	c0011_mem1 = S.Task('c0011_mem1', length=1, delay_cost=1)
	S += c0011_mem1 >= 36
	c0011_mem1 += ADD_mem[0]

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

	c0011 = S.Task('c0011', length=1, delay_cost=1)
	S += c0011 >= 37
	c0011 += ADD[1]

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

	c11_t0_s00_mem0 = S.Task('c11_t0_s00_mem0', length=1, delay_cost=1)
	S += c11_t0_s00_mem0 >= 37
	c11_t0_s00_mem0 += MUL_mem[0]

	c0011_w = S.Task('c0011_w', length=1, delay_cost=1)
	S += c0011_w >= 38
	c0011_w += INPUT_mem_w

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

	c11_t0_s00 = S.Task('c11_t0_s00', length=1, delay_cost=1)
	S += c11_t0_s00 >= 38
	c11_t0_s00 += ADD[2]

	c11_t0_t5_mem0 = S.Task('c11_t0_t5_mem0', length=1, delay_cost=1)
	S += c11_t0_t5_mem0 >= 38
	c11_t0_t5_mem0 += MUL_mem[0]

	c11_t0_t5_mem1 = S.Task('c11_t0_t5_mem1', length=1, delay_cost=1)
	S += c11_t0_t5_mem1 >= 38
	c11_t0_t5_mem1 += MUL_mem[0]

	c01_t0_t0 = S.Task('c01_t0_t0', length=7, delay_cost=1)
	S += c01_t0_t0 >= 39
	c01_t0_t0 += MUL[0]

	c01_t30_mem0 = S.Task('c01_t30_mem0', length=1, delay_cost=1)
	S += c01_t30_mem0 >= 39
	c01_t30_mem0 += INPUT_mem_r

	c01_t30_mem1 = S.Task('c01_t30_mem1', length=1, delay_cost=1)
	S += c01_t30_mem1 >= 39
	c01_t30_mem1 += INPUT_mem_r

	c11_t0_s01_mem0 = S.Task('c11_t0_s01_mem0', length=1, delay_cost=1)
	S += c11_t0_s01_mem0 >= 39
	c11_t0_s01_mem0 += ADD_mem[2]

	c11_t0_s01_mem1 = S.Task('c11_t0_s01_mem1', length=1, delay_cost=1)
	S += c11_t0_s01_mem1 >= 39
	c11_t0_s01_mem1 += MUL_mem[0]

	c11_t0_t5 = S.Task('c11_t0_t5', length=1, delay_cost=1)
	S += c11_t0_t5 >= 39
	c11_t0_t5 += ADD[2]

	c01_t30 = S.Task('c01_t30', length=1, delay_cost=1)
	S += c01_t30 >= 40
	c01_t30 += ADD[2]

	c02_t0_s00_mem0 = S.Task('c02_t0_s00_mem0', length=1, delay_cost=1)
	S += c02_t0_s00_mem0 >= 40
	c02_t0_s00_mem0 += MUL_mem[0]

	c11_t0_s01 = S.Task('c11_t0_s01', length=1, delay_cost=1)
	S += c11_t0_s01 >= 40
	c11_t0_s01 += ADD[0]

	c11_t0_s02_mem0 = S.Task('c11_t0_s02_mem0', length=1, delay_cost=1)
	S += c11_t0_s02_mem0 >= 40
	c11_t0_s02_mem0 += ADD_mem[0]

	c12_t31_mem0 = S.Task('c12_t31_mem0', length=1, delay_cost=1)
	S += c12_t31_mem0 >= 40
	c12_t31_mem0 += INPUT_mem_r

	c12_t31_mem1 = S.Task('c12_t31_mem1', length=1, delay_cost=1)
	S += c12_t31_mem1 >= 40
	c12_t31_mem1 += INPUT_mem_r

	c_f1211_mem0 = S.Task('c_f1211_mem0', length=1, delay_cost=1)
	S += c_f1211_mem0 >= 40
	c_f1211_mem0 += MUL_mem[0]

	c_f1211_mem1 = S.Task('c_f1211_mem1', length=1, delay_cost=1)
	S += c_f1211_mem1 >= 40
	c_f1211_mem1 += ADD_mem[2]

	c02_t0_s00 = S.Task('c02_t0_s00', length=1, delay_cost=1)
	S += c02_t0_s00 >= 41
	c02_t0_s00 += ADD[1]

	c11_t0_s02 = S.Task('c11_t0_s02', length=1, delay_cost=1)
	S += c11_t0_s02 >= 41
	c11_t0_s02 += ADD[3]

	c12_t0_t3_mem0 = S.Task('c12_t0_t3_mem0', length=1, delay_cost=1)
	S += c12_t0_t3_mem0 >= 41
	c12_t0_t3_mem0 += INPUT_mem_r

	c12_t0_t3_mem1 = S.Task('c12_t0_t3_mem1', length=1, delay_cost=1)
	S += c12_t0_t3_mem1 >= 41
	c12_t0_t3_mem1 += INPUT_mem_r

	c12_t31 = S.Task('c12_t31', length=1, delay_cost=1)
	S += c12_t31 >= 41
	c12_t31 += ADD[2]

	c_f1211 = S.Task('c_f1211', length=1, delay_cost=1)
	S += c_f1211 >= 41
	c_f1211 += ADD[0]

	c02_t0_s01_mem0 = S.Task('c02_t0_s01_mem0', length=1, delay_cost=1)
	S += c02_t0_s01_mem0 >= 42
	c02_t0_s01_mem0 += ADD_mem[1]

	c02_t0_s01_mem1 = S.Task('c02_t0_s01_mem1', length=1, delay_cost=1)
	S += c02_t0_s01_mem1 >= 42
	c02_t0_s01_mem1 += MUL_mem[0]

	c02_t31_mem0 = S.Task('c02_t31_mem0', length=1, delay_cost=1)
	S += c02_t31_mem0 >= 42
	c02_t31_mem0 += INPUT_mem_r

	c02_t31_mem1 = S.Task('c02_t31_mem1', length=1, delay_cost=1)
	S += c02_t31_mem1 >= 42
	c02_t31_mem1 += INPUT_mem_r

	c11_t0_s03_mem0 = S.Task('c11_t0_s03_mem0', length=1, delay_cost=1)
	S += c11_t0_s03_mem0 >= 42
	c11_t0_s03_mem0 += ADD_mem[3]

	c12_t0_s00_mem0 = S.Task('c12_t0_s00_mem0', length=1, delay_cost=1)
	S += c12_t0_s00_mem0 >= 42
	c12_t0_s00_mem0 += MUL_mem[0]

	c12_t0_t3 = S.Task('c12_t0_t3', length=1, delay_cost=1)
	S += c12_t0_t3 >= 42
	c12_t0_t3 += ADD[0]

	c02_t0_s01 = S.Task('c02_t0_s01', length=1, delay_cost=1)
	S += c02_t0_s01 >= 43
	c02_t0_s01 += ADD[0]

	c02_t0_s02_mem0 = S.Task('c02_t0_s02_mem0', length=1, delay_cost=1)
	S += c02_t0_s02_mem0 >= 43
	c02_t0_s02_mem0 += ADD_mem[0]

	c02_t30_mem0 = S.Task('c02_t30_mem0', length=1, delay_cost=1)
	S += c02_t30_mem0 >= 43
	c02_t30_mem0 += INPUT_mem_r

	c02_t30_mem1 = S.Task('c02_t30_mem1', length=1, delay_cost=1)
	S += c02_t30_mem1 >= 43
	c02_t30_mem1 += INPUT_mem_r

	c02_t31 = S.Task('c02_t31', length=1, delay_cost=1)
	S += c02_t31 >= 43
	c02_t31 += ADD[1]

	c11_t0_s03 = S.Task('c11_t0_s03', length=1, delay_cost=1)
	S += c11_t0_s03 >= 43
	c11_t0_s03 += ADD[3]

	c12_t0_s00 = S.Task('c12_t0_s00', length=1, delay_cost=1)
	S += c12_t0_s00 >= 43
	c12_t0_s00 += ADD[2]

	c12_t0_t5_mem0 = S.Task('c12_t0_t5_mem0', length=1, delay_cost=1)
	S += c12_t0_t5_mem0 >= 43
	c12_t0_t5_mem0 += MUL_mem[0]

	c12_t0_t5_mem1 = S.Task('c12_t0_t5_mem1', length=1, delay_cost=1)
	S += c12_t0_t5_mem1 >= 43
	c12_t0_t5_mem1 += MUL_mem[0]

	c01_t0_s00_mem0 = S.Task('c01_t0_s00_mem0', length=1, delay_cost=1)
	S += c01_t0_s00_mem0 >= 44
	c01_t0_s00_mem0 += MUL_mem[0]

	c02_t0_s02 = S.Task('c02_t0_s02', length=1, delay_cost=1)
	S += c02_t0_s02 >= 44
	c02_t0_s02 += ADD[3]

	c02_t30 = S.Task('c02_t30', length=1, delay_cost=1)
	S += c02_t30 >= 44
	c02_t30 += ADD[0]

	c02_t4_t3_mem0 = S.Task('c02_t4_t3_mem0', length=1, delay_cost=1)
	S += c02_t4_t3_mem0 >= 44
	c02_t4_t3_mem0 += ADD_mem[0]

	c02_t4_t3_mem1 = S.Task('c02_t4_t3_mem1', length=1, delay_cost=1)
	S += c02_t4_t3_mem1 >= 44
	c02_t4_t3_mem1 += ADD_mem[1]

	c12_t0_s01_mem0 = S.Task('c12_t0_s01_mem0', length=1, delay_cost=1)
	S += c12_t0_s01_mem0 >= 44
	c12_t0_s01_mem0 += ADD_mem[2]

	c12_t0_s01_mem1 = S.Task('c12_t0_s01_mem1', length=1, delay_cost=1)
	S += c12_t0_s01_mem1 >= 44
	c12_t0_s01_mem1 += MUL_mem[0]

	c12_t0_t2_mem0 = S.Task('c12_t0_t2_mem0', length=1, delay_cost=1)
	S += c12_t0_t2_mem0 >= 44
	c12_t0_t2_mem0 += INPUT_mem_r

	c12_t0_t2_mem1 = S.Task('c12_t0_t2_mem1', length=1, delay_cost=1)
	S += c12_t0_t2_mem1 >= 44
	c12_t0_t2_mem1 += INPUT_mem_r

	c12_t0_t5 = S.Task('c12_t0_t5', length=1, delay_cost=1)
	S += c12_t0_t5 >= 44
	c12_t0_t5 += ADD[2]

	c01_t0_s00 = S.Task('c01_t0_s00', length=1, delay_cost=1)
	S += c01_t0_s00 >= 45
	c01_t0_s00 += ADD[3]

	c01_t0_t5_mem0 = S.Task('c01_t0_t5_mem0', length=1, delay_cost=1)
	S += c01_t0_t5_mem0 >= 45
	c01_t0_t5_mem0 += MUL_mem[0]

	c01_t0_t5_mem1 = S.Task('c01_t0_t5_mem1', length=1, delay_cost=1)
	S += c01_t0_t5_mem1 >= 45
	c01_t0_t5_mem1 += MUL_mem[0]

	c02_t0_s03_mem0 = S.Task('c02_t0_s03_mem0', length=1, delay_cost=1)
	S += c02_t0_s03_mem0 >= 45
	c02_t0_s03_mem0 += ADD_mem[3]

	c02_t4_t3 = S.Task('c02_t4_t3', length=1, delay_cost=1)
	S += c02_t4_t3 >= 45
	c02_t4_t3 += ADD[2]

	c12_t0_s01 = S.Task('c12_t0_s01', length=1, delay_cost=1)
	S += c12_t0_s01 >= 45
	c12_t0_s01 += ADD[1]

	c12_t0_s02_mem0 = S.Task('c12_t0_s02_mem0', length=1, delay_cost=1)
	S += c12_t0_s02_mem0 >= 45
	c12_t0_s02_mem0 += ADD_mem[1]

	c12_t0_t2 = S.Task('c12_t0_t2', length=1, delay_cost=1)
	S += c12_t0_t2 >= 45
	c12_t0_t2 += ADD[0]

	c12_t0_t4_in = S.Task('c12_t0_t4_in', length=1, delay_cost=1)
	S += c12_t0_t4_in >= 45
	c12_t0_t4_in += MUL_in[0]

	c12_t0_t4_mem0 = S.Task('c12_t0_t4_mem0', length=1, delay_cost=1)
	S += c12_t0_t4_mem0 >= 45
	c12_t0_t4_mem0 += ADD_mem[0]

	c12_t0_t4_mem1 = S.Task('c12_t0_t4_mem1', length=1, delay_cost=1)
	S += c12_t0_t4_mem1 >= 45
	c12_t0_t4_mem1 += ADD_mem[0]

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

	c01_t0_t5 = S.Task('c01_t0_t5', length=1, delay_cost=1)
	S += c01_t0_t5 >= 46
	c01_t0_t5 += ADD[2]

	c02_t0_s03 = S.Task('c02_t0_s03', length=1, delay_cost=1)
	S += c02_t0_s03 >= 46
	c02_t0_s03 += ADD[0]

	c02_t0_t5_mem0 = S.Task('c02_t0_t5_mem0', length=1, delay_cost=1)
	S += c02_t0_t5_mem0 >= 46
	c02_t0_t5_mem0 += MUL_mem[0]

	c02_t0_t5_mem1 = S.Task('c02_t0_t5_mem1', length=1, delay_cost=1)
	S += c02_t0_t5_mem1 >= 46
	c02_t0_t5_mem1 += MUL_mem[0]

	c12_t0_s02 = S.Task('c12_t0_s02', length=1, delay_cost=1)
	S += c12_t0_s02 >= 46
	c12_t0_s02 += ADD[3]

	c12_t0_t4 = S.Task('c12_t0_t4', length=7, delay_cost=1)
	S += c12_t0_t4 >= 46
	c12_t0_t4 += MUL[0]

	c12_t30 = S.Task('c12_t30', length=1, delay_cost=1)
	S += c12_t30 >= 46
	c12_t30 += ADD[1]

	c12_t4_t3_mem0 = S.Task('c12_t4_t3_mem0', length=1, delay_cost=1)
	S += c12_t4_t3_mem0 >= 46
	c12_t4_t3_mem0 += ADD_mem[1]

	c12_t4_t3_mem1 = S.Task('c12_t4_t3_mem1', length=1, delay_cost=1)
	S += c12_t4_t3_mem1 >= 46
	c12_t4_t3_mem1 += ADD_mem[2]

	c01_t0_s01_mem0 = S.Task('c01_t0_s01_mem0', length=1, delay_cost=1)
	S += c01_t0_s01_mem0 >= 47
	c01_t0_s01_mem0 += ADD_mem[3]

	c01_t0_s01_mem1 = S.Task('c01_t0_s01_mem1', length=1, delay_cost=1)
	S += c01_t0_s01_mem1 >= 47
	c01_t0_s01_mem1 += MUL_mem[0]

	c01_t0_t3 = S.Task('c01_t0_t3', length=1, delay_cost=1)
	S += c01_t0_t3 >= 47
	c01_t0_t3 += ADD[3]

	c01_t31_mem0 = S.Task('c01_t31_mem0', length=1, delay_cost=1)
	S += c01_t31_mem0 >= 47
	c01_t31_mem0 += INPUT_mem_r

	c01_t31_mem1 = S.Task('c01_t31_mem1', length=1, delay_cost=1)
	S += c01_t31_mem1 >= 47
	c01_t31_mem1 += INPUT_mem_r

	c02_t0_s04_mem0 = S.Task('c02_t0_s04_mem0', length=1, delay_cost=1)
	S += c02_t0_s04_mem0 >= 47
	c02_t0_s04_mem0 += ADD_mem[0]

	c02_t0_s04_mem1 = S.Task('c02_t0_s04_mem1', length=1, delay_cost=1)
	S += c02_t0_s04_mem1 >= 47
	c02_t0_s04_mem1 += MUL_mem[0]

	c02_t0_t5 = S.Task('c02_t0_t5', length=1, delay_cost=1)
	S += c02_t0_t5 >= 47
	c02_t0_t5 += ADD[2]

	c12_t0_s03_mem0 = S.Task('c12_t0_s03_mem0', length=1, delay_cost=1)
	S += c12_t0_s03_mem0 >= 47
	c12_t0_s03_mem0 += ADD_mem[3]

	c12_t4_t3 = S.Task('c12_t4_t3', length=1, delay_cost=1)
	S += c12_t4_t3 >= 47
	c12_t4_t3 += ADD[0]

	c01_t0_s01 = S.Task('c01_t0_s01', length=1, delay_cost=1)
	S += c01_t0_s01 >= 48
	c01_t0_s01 += ADD[0]

	c01_t0_s02_mem0 = S.Task('c01_t0_s02_mem0', length=1, delay_cost=1)
	S += c01_t0_s02_mem0 >= 48
	c01_t0_s02_mem0 += ADD_mem[0]

	c01_t31 = S.Task('c01_t31', length=1, delay_cost=1)
	S += c01_t31 >= 48
	c01_t31 += ADD[2]

	c01_t4_t3_mem0 = S.Task('c01_t4_t3_mem0', length=1, delay_cost=1)
	S += c01_t4_t3_mem0 >= 48
	c01_t4_t3_mem0 += ADD_mem[2]

	c01_t4_t3_mem1 = S.Task('c01_t4_t3_mem1', length=1, delay_cost=1)
	S += c01_t4_t3_mem1 >= 48
	c01_t4_t3_mem1 += ADD_mem[2]

	c02_t0_s04 = S.Task('c02_t0_s04', length=1, delay_cost=1)
	S += c02_t0_s04 >= 48
	c02_t0_s04 += ADD[1]

	c11_t0_s04_mem0 = S.Task('c11_t0_s04_mem0', length=1, delay_cost=1)
	S += c11_t0_s04_mem0 >= 48
	c11_t0_s04_mem0 += ADD_mem[3]

	c11_t0_s04_mem1 = S.Task('c11_t0_s04_mem1', length=1, delay_cost=1)
	S += c11_t0_s04_mem1 >= 48
	c11_t0_s04_mem1 += MUL_mem[0]

	c11_t0_t2_mem0 = S.Task('c11_t0_t2_mem0', length=1, delay_cost=1)
	S += c11_t0_t2_mem0 >= 48
	c11_t0_t2_mem0 += INPUT_mem_r

	c11_t0_t2_mem1 = S.Task('c11_t0_t2_mem1', length=1, delay_cost=1)
	S += c11_t0_t2_mem1 >= 48
	c11_t0_t2_mem1 += INPUT_mem_r

	c12_t0_s03 = S.Task('c12_t0_s03', length=1, delay_cost=1)
	S += c12_t0_s03 >= 48
	c12_t0_s03 += ADD[3]

	c01_t0_s02 = S.Task('c01_t0_s02', length=1, delay_cost=1)
	S += c01_t0_s02 >= 49
	c01_t0_s02 += ADD[3]

	c01_t4_t3 = S.Task('c01_t4_t3', length=1, delay_cost=1)
	S += c01_t4_t3 >= 49
	c01_t4_t3 += ADD[2]

	c11_t0_s04 = S.Task('c11_t0_s04', length=1, delay_cost=1)
	S += c11_t0_s04 >= 49
	c11_t0_s04 += ADD[0]

	c11_t0_t2 = S.Task('c11_t0_t2', length=1, delay_cost=1)
	S += c11_t0_t2 >= 49
	c11_t0_t2 += ADD[1]

	c12_t0_s04_mem0 = S.Task('c12_t0_s04_mem0', length=1, delay_cost=1)
	S += c12_t0_s04_mem0 >= 49
	c12_t0_s04_mem0 += ADD_mem[3]

	c12_t0_s04_mem1 = S.Task('c12_t0_s04_mem1', length=1, delay_cost=1)
	S += c12_t0_s04_mem1 >= 49
	c12_t0_s04_mem1 += MUL_mem[0]

	c12_t1_t3_mem0 = S.Task('c12_t1_t3_mem0', length=1, delay_cost=1)
	S += c12_t1_t3_mem0 >= 49
	c12_t1_t3_mem0 += INPUT_mem_r

	c12_t1_t3_mem1 = S.Task('c12_t1_t3_mem1', length=1, delay_cost=1)
	S += c12_t1_t3_mem1 >= 49
	c12_t1_t3_mem1 += INPUT_mem_r

	c01_t0_s03_mem0 = S.Task('c01_t0_s03_mem0', length=1, delay_cost=1)
	S += c01_t0_s03_mem0 >= 50
	c01_t0_s03_mem0 += ADD_mem[3]

	c01_t0_t2_mem0 = S.Task('c01_t0_t2_mem0', length=1, delay_cost=1)
	S += c01_t0_t2_mem0 >= 50
	c01_t0_t2_mem0 += INPUT_mem_r

	c01_t0_t2_mem1 = S.Task('c01_t0_t2_mem1', length=1, delay_cost=1)
	S += c01_t0_t2_mem1 >= 50
	c01_t0_t2_mem1 += INPUT_mem_r

	c12_t0_s04 = S.Task('c12_t0_s04', length=1, delay_cost=1)
	S += c12_t0_s04 >= 50
	c12_t0_s04 += ADD[1]

	c12_t1_t3 = S.Task('c12_t1_t3', length=1, delay_cost=1)
	S += c12_t1_t3 >= 50
	c12_t1_t3 += ADD[0]

	c01_t0_s03 = S.Task('c01_t0_s03', length=1, delay_cost=1)
	S += c01_t0_s03 >= 51
	c01_t0_s03 += ADD[2]

	c01_t0_t2 = S.Task('c01_t0_t2', length=1, delay_cost=1)
	S += c01_t0_t2 >= 51
	c01_t0_t2 += ADD[0]

	c01_t0_t4_in = S.Task('c01_t0_t4_in', length=1, delay_cost=1)
	S += c01_t0_t4_in >= 51
	c01_t0_t4_in += MUL_in[0]

	c01_t0_t4_mem0 = S.Task('c01_t0_t4_mem0', length=1, delay_cost=1)
	S += c01_t0_t4_mem0 >= 51
	c01_t0_t4_mem0 += ADD_mem[0]

	c01_t0_t4_mem1 = S.Task('c01_t0_t4_mem1', length=1, delay_cost=1)
	S += c01_t0_t4_mem1 >= 51
	c01_t0_t4_mem1 += ADD_mem[3]

	c02_t1_t3_mem0 = S.Task('c02_t1_t3_mem0', length=1, delay_cost=1)
	S += c02_t1_t3_mem0 >= 51
	c02_t1_t3_mem0 += INPUT_mem_r

	c02_t1_t3_mem1 = S.Task('c02_t1_t3_mem1', length=1, delay_cost=1)
	S += c02_t1_t3_mem1 >= 51
	c02_t1_t3_mem1 += INPUT_mem_r

	c01_t0_s04_mem0 = S.Task('c01_t0_s04_mem0', length=1, delay_cost=1)
	S += c01_t0_s04_mem0 >= 52
	c01_t0_s04_mem0 += ADD_mem[2]

	c01_t0_s04_mem1 = S.Task('c01_t0_s04_mem1', length=1, delay_cost=1)
	S += c01_t0_s04_mem1 >= 52
	c01_t0_s04_mem1 += MUL_mem[0]

	c01_t0_t4 = S.Task('c01_t0_t4', length=7, delay_cost=1)
	S += c01_t0_t4 >= 52
	c01_t0_t4 += MUL[0]

	c01_t1_t3_mem0 = S.Task('c01_t1_t3_mem0', length=1, delay_cost=1)
	S += c01_t1_t3_mem0 >= 52
	c01_t1_t3_mem0 += INPUT_mem_r

	c01_t1_t3_mem1 = S.Task('c01_t1_t3_mem1', length=1, delay_cost=1)
	S += c01_t1_t3_mem1 >= 52
	c01_t1_t3_mem1 += INPUT_mem_r

	c02_t1_t3 = S.Task('c02_t1_t3', length=1, delay_cost=1)
	S += c02_t1_t3 >= 52
	c02_t1_t3 += ADD[0]

	c01_t0_s04 = S.Task('c01_t0_s04', length=1, delay_cost=1)
	S += c01_t0_s04 >= 53
	c01_t0_s04 += ADD[0]

	c01_t1_t3 = S.Task('c01_t1_t3', length=1, delay_cost=1)
	S += c01_t1_t3 >= 53
	c01_t1_t3 += ADD[2]

	c02_t0_t3_mem0 = S.Task('c02_t0_t3_mem0', length=1, delay_cost=1)
	S += c02_t0_t3_mem0 >= 53
	c02_t0_t3_mem0 += INPUT_mem_r

	c02_t0_t3_mem1 = S.Task('c02_t0_t3_mem1', length=1, delay_cost=1)
	S += c02_t0_t3_mem1 >= 53
	c02_t0_t3_mem1 += INPUT_mem_r

	c12_t01_mem0 = S.Task('c12_t01_mem0', length=1, delay_cost=1)
	S += c12_t01_mem0 >= 53
	c12_t01_mem0 += MUL_mem[0]

	c12_t01_mem1 = S.Task('c12_t01_mem1', length=1, delay_cost=1)
	S += c12_t01_mem1 >= 53
	c12_t01_mem1 += ADD_mem[2]

	c02_t0_t3 = S.Task('c02_t0_t3', length=1, delay_cost=1)
	S += c02_t0_t3 >= 54
	c02_t0_t3 += ADD[0]

	c10_t31_mem0 = S.Task('c10_t31_mem0', length=1, delay_cost=1)
	S += c10_t31_mem0 >= 54
	c10_t31_mem0 += INPUT_mem_r

	c10_t31_mem1 = S.Task('c10_t31_mem1', length=1, delay_cost=1)
	S += c10_t31_mem1 >= 54
	c10_t31_mem1 += INPUT_mem_r

	c12_t01 = S.Task('c12_t01', length=1, delay_cost=1)
	S += c12_t01 >= 54
	c12_t01 += ADD[1]

	c02_t0_t2_mem0 = S.Task('c02_t0_t2_mem0', length=1, delay_cost=1)
	S += c02_t0_t2_mem0 >= 55
	c02_t0_t2_mem0 += INPUT_mem_r

	c02_t0_t2_mem1 = S.Task('c02_t0_t2_mem1', length=1, delay_cost=1)
	S += c02_t0_t2_mem1 >= 55
	c02_t0_t2_mem1 += INPUT_mem_r

	c10_t31 = S.Task('c10_t31', length=1, delay_cost=1)
	S += c10_t31 >= 55
	c10_t31 += ADD[0]

	c10_t4_t3_mem0 = S.Task('c10_t4_t3_mem0', length=1, delay_cost=1)
	S += c10_t4_t3_mem0 >= 55
	c10_t4_t3_mem0 += ADD_mem[1]

	c10_t4_t3_mem1 = S.Task('c10_t4_t3_mem1', length=1, delay_cost=1)
	S += c10_t4_t3_mem1 >= 55
	c10_t4_t3_mem1 += ADD_mem[0]

	c02_t0_t2 = S.Task('c02_t0_t2', length=1, delay_cost=1)
	S += c02_t0_t2 >= 56
	c02_t0_t2 += ADD[0]

	c02_t0_t4_in = S.Task('c02_t0_t4_in', length=1, delay_cost=1)
	S += c02_t0_t4_in >= 56
	c02_t0_t4_in += MUL_in[0]

	c02_t0_t4_mem0 = S.Task('c02_t0_t4_mem0', length=1, delay_cost=1)
	S += c02_t0_t4_mem0 >= 56
	c02_t0_t4_mem0 += ADD_mem[0]

	c02_t0_t4_mem1 = S.Task('c02_t0_t4_mem1', length=1, delay_cost=1)
	S += c02_t0_t4_mem1 >= 56
	c02_t0_t4_mem1 += ADD_mem[0]

	c10_t4_t3 = S.Task('c10_t4_t3', length=1, delay_cost=1)
	S += c10_t4_t3 >= 56
	c10_t4_t3 += ADD[1]

	c11_t31_mem0 = S.Task('c11_t31_mem0', length=1, delay_cost=1)
	S += c11_t31_mem0 >= 56
	c11_t31_mem0 += INPUT_mem_r

	c11_t31_mem1 = S.Task('c11_t31_mem1', length=1, delay_cost=1)
	S += c11_t31_mem1 >= 56
	c11_t31_mem1 += INPUT_mem_r

	c02_t0_t4 = S.Task('c02_t0_t4', length=7, delay_cost=1)
	S += c02_t0_t4 >= 57
	c02_t0_t4 += MUL[0]

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

	c11_t4_t3_mem0 = S.Task('c11_t4_t3_mem0', length=1, delay_cost=1)
	S += c11_t4_t3_mem0 >= 58
	c11_t4_t3_mem0 += ADD_mem[0]

	c11_t4_t3_mem1 = S.Task('c11_t4_t3_mem1', length=1, delay_cost=1)
	S += c11_t4_t3_mem1 >= 58
	c11_t4_t3_mem1 += ADD_mem[0]

	c01_t01_mem0 = S.Task('c01_t01_mem0', length=1, delay_cost=1)
	S += c01_t01_mem0 >= 59
	c01_t01_mem0 += MUL_mem[0]

	c01_t01_mem1 = S.Task('c01_t01_mem1', length=1, delay_cost=1)
	S += c01_t01_mem1 >= 59
	c01_t01_mem1 += ADD_mem[2]

	c11_t0_t3_mem0 = S.Task('c11_t0_t3_mem0', length=1, delay_cost=1)
	S += c11_t0_t3_mem0 >= 59
	c11_t0_t3_mem0 += INPUT_mem_r

	c11_t0_t3_mem1 = S.Task('c11_t0_t3_mem1', length=1, delay_cost=1)
	S += c11_t0_t3_mem1 >= 59
	c11_t0_t3_mem1 += INPUT_mem_r

	c11_t1_t3 = S.Task('c11_t1_t3', length=1, delay_cost=1)
	S += c11_t1_t3 >= 59
	c11_t1_t3 += ADD[0]

	c11_t4_t3 = S.Task('c11_t4_t3', length=1, delay_cost=1)
	S += c11_t4_t3 >= 59
	c11_t4_t3 += ADD[2]

	c0001_mem0 = S.Task('c0001_mem0', length=1, delay_cost=1)
	S += c0001_mem0 >= 60
	c0001_mem0 += INPUT_mem_r

	c0001_mem1 = S.Task('c0001_mem1', length=1, delay_cost=1)
	S += c0001_mem1 >= 60
	c0001_mem1 += INPUT_mem_r

	c01_t01 = S.Task('c01_t01', length=1, delay_cost=1)
	S += c01_t01 >= 60
	c01_t01 += ADD[0]

	c11_t0_t3 = S.Task('c11_t0_t3', length=1, delay_cost=1)
	S += c11_t0_t3 >= 60
	c11_t0_t3 += ADD[3]

	c11_t0_t4_in = S.Task('c11_t0_t4_in', length=1, delay_cost=1)
	S += c11_t0_t4_in >= 60
	c11_t0_t4_in += MUL_in[0]

	c11_t0_t4_mem0 = S.Task('c11_t0_t4_mem0', length=1, delay_cost=1)
	S += c11_t0_t4_mem0 >= 60
	c11_t0_t4_mem0 += ADD_mem[1]

	c11_t0_t4_mem1 = S.Task('c11_t0_t4_mem1', length=1, delay_cost=1)
	S += c11_t0_t4_mem1 >= 60
	c11_t0_t4_mem1 += ADD_mem[3]

	c0001 = S.Task('c0001', length=1, delay_cost=1)
	S += c0001 >= 61
	c0001 += ADD[3]

	c01_t21_mem0 = S.Task('c01_t21_mem0', length=1, delay_cost=1)
	S += c01_t21_mem0 >= 61
	c01_t21_mem0 += ADD_mem[1]

	c01_t21_mem1 = S.Task('c01_t21_mem1', length=1, delay_cost=1)
	S += c01_t21_mem1 >= 61
	c01_t21_mem1 += INPUT_mem_r

	c02_t1_t1_in = S.Task('c02_t1_t1_in', length=1, delay_cost=1)
	S += c02_t1_t1_in >= 61
	c02_t1_t1_in += MUL_in[0]

	c02_t1_t1_mem0 = S.Task('c02_t1_t1_mem0', length=1, delay_cost=1)
	S += c02_t1_t1_mem0 >= 61
	c02_t1_t1_mem0 += ADD_mem[0]

	c02_t1_t1_mem1 = S.Task('c02_t1_t1_mem1', length=1, delay_cost=1)
	S += c02_t1_t1_mem1 >= 61
	c02_t1_t1_mem1 += INPUT_mem_r

	c11_t0_t4 = S.Task('c11_t0_t4', length=7, delay_cost=1)
	S += c11_t0_t4 >= 61
	c11_t0_t4 += MUL[0]

	c0001_w = S.Task('c0001_w', length=1, delay_cost=1)
	S += c0001_w >= 62
	c0001_w += INPUT_mem_w

	c01_t21 = S.Task('c01_t21', length=1, delay_cost=1)
	S += c01_t21 >= 62
	c01_t21 += ADD[0]

	c02_t1_t1 = S.Task('c02_t1_t1', length=7, delay_cost=1)
	S += c02_t1_t1 >= 62
	c02_t1_t1 += MUL[0]

	c12_t1_t1_in = S.Task('c12_t1_t1_in', length=1, delay_cost=1)
	S += c12_t1_t1_in >= 62
	c12_t1_t1_in += MUL_in[0]

	c12_t1_t1_mem0 = S.Task('c12_t1_t1_mem0', length=1, delay_cost=1)
	S += c12_t1_t1_mem0 >= 62
	c12_t1_t1_mem0 += ADD_mem[0]

	c12_t1_t1_mem1 = S.Task('c12_t1_t1_mem1', length=1, delay_cost=1)
	S += c12_t1_t1_mem1 >= 62
	c12_t1_t1_mem1 += INPUT_mem_r

	c12_t21_mem0 = S.Task('c12_t21_mem0', length=1, delay_cost=1)
	S += c12_t21_mem0 >= 62
	c12_t21_mem0 += ADD_mem[0]

	c12_t21_mem1 = S.Task('c12_t21_mem1', length=1, delay_cost=1)
	S += c12_t21_mem1 >= 62
	c12_t21_mem1 += INPUT_mem_r

	c11_t1_t1_in = S.Task('c11_t1_t1_in', length=1, delay_cost=1)
	S += c11_t1_t1_in >= 63
	c11_t1_t1_in += MUL_in[0]

	c11_t1_t1_mem0 = S.Task('c11_t1_t1_mem0', length=1, delay_cost=1)
	S += c11_t1_t1_mem0 >= 63
	c11_t1_t1_mem0 += ADD_mem[1]

	c11_t1_t1_mem1 = S.Task('c11_t1_t1_mem1', length=1, delay_cost=1)
	S += c11_t1_t1_mem1 >= 63
	c11_t1_t1_mem1 += INPUT_mem_r

	c11_t21_mem0 = S.Task('c11_t21_mem0', length=1, delay_cost=1)
	S += c11_t21_mem0 >= 63
	c11_t21_mem0 += ADD_mem[1]

	c11_t21_mem1 = S.Task('c11_t21_mem1', length=1, delay_cost=1)
	S += c11_t21_mem1 >= 63
	c11_t21_mem1 += INPUT_mem_r

	c12_t1_t1 = S.Task('c12_t1_t1', length=7, delay_cost=1)
	S += c12_t1_t1 >= 63
	c12_t1_t1 += MUL[0]

	c12_t21 = S.Task('c12_t21', length=1, delay_cost=1)
	S += c12_t21 >= 63
	c12_t21 += ADD[0]

	c01_t1_t1_in = S.Task('c01_t1_t1_in', length=1, delay_cost=1)
	S += c01_t1_t1_in >= 64
	c01_t1_t1_in += MUL_in[0]

	c01_t1_t1_mem0 = S.Task('c01_t1_t1_mem0', length=1, delay_cost=1)
	S += c01_t1_t1_mem0 >= 64
	c01_t1_t1_mem0 += ADD_mem[1]

	c01_t1_t1_mem1 = S.Task('c01_t1_t1_mem1', length=1, delay_cost=1)
	S += c01_t1_t1_mem1 >= 64
	c01_t1_t1_mem1 += INPUT_mem_r

	c02_t01_mem0 = S.Task('c02_t01_mem0', length=1, delay_cost=1)
	S += c02_t01_mem0 >= 64
	c02_t01_mem0 += MUL_mem[0]

	c02_t01_mem1 = S.Task('c02_t01_mem1', length=1, delay_cost=1)
	S += c02_t01_mem1 >= 64
	c02_t01_mem1 += ADD_mem[2]

	c10_t21_mem0 = S.Task('c10_t21_mem0', length=1, delay_cost=1)
	S += c10_t21_mem0 >= 64
	c10_t21_mem0 += ADD_mem[1]

	c10_t21_mem1 = S.Task('c10_t21_mem1', length=1, delay_cost=1)
	S += c10_t21_mem1 >= 64
	c10_t21_mem1 += INPUT_mem_r

	c11_t1_t1 = S.Task('c11_t1_t1', length=7, delay_cost=1)
	S += c11_t1_t1 >= 64
	c11_t1_t1 += MUL[0]

	c11_t21 = S.Task('c11_t21', length=1, delay_cost=1)
	S += c11_t21 >= 64
	c11_t21 += ADD[3]

	c01_t1_t1 = S.Task('c01_t1_t1', length=7, delay_cost=1)
	S += c01_t1_t1 >= 65
	c01_t1_t1 += MUL[0]

	c02_t01 = S.Task('c02_t01', length=1, delay_cost=1)
	S += c02_t01 >= 65
	c02_t01 += ADD[1]

	c02_t21_mem0 = S.Task('c02_t21_mem0', length=1, delay_cost=1)
	S += c02_t21_mem0 >= 65
	c02_t21_mem0 += ADD_mem[0]

	c02_t21_mem1 = S.Task('c02_t21_mem1', length=1, delay_cost=1)
	S += c02_t21_mem1 >= 65
	c02_t21_mem1 += INPUT_mem_r

	c10_t1_t1_in = S.Task('c10_t1_t1_in', length=1, delay_cost=1)
	S += c10_t1_t1_in >= 65
	c10_t1_t1_in += MUL_in[0]

	c10_t1_t1_mem0 = S.Task('c10_t1_t1_mem0', length=1, delay_cost=1)
	S += c10_t1_t1_mem0 >= 65
	c10_t1_t1_mem0 += ADD_mem[1]

	c10_t1_t1_mem1 = S.Task('c10_t1_t1_mem1', length=1, delay_cost=1)
	S += c10_t1_t1_mem1 >= 65
	c10_t1_t1_mem1 += INPUT_mem_r

	c10_t21 = S.Task('c10_t21', length=1, delay_cost=1)
	S += c10_t21 >= 65
	c10_t21 += ADD[3]

	c01_t4_t1_in = S.Task('c01_t4_t1_in', length=1, delay_cost=1)
	S += c01_t4_t1_in >= 66
	c01_t4_t1_in += MUL_in[0]

	c01_t4_t1_mem0 = S.Task('c01_t4_t1_mem0', length=1, delay_cost=1)
	S += c01_t4_t1_mem0 >= 66
	c01_t4_t1_mem0 += ADD_mem[0]

	c01_t4_t1_mem1 = S.Task('c01_t4_t1_mem1', length=1, delay_cost=1)
	S += c01_t4_t1_mem1 >= 66
	c01_t4_t1_mem1 += ADD_mem[2]

	c02_t21 = S.Task('c02_t21', length=1, delay_cost=1)
	S += c02_t21 >= 66
	c02_t21 += ADD[1]

	c10_t1_t1 = S.Task('c10_t1_t1', length=7, delay_cost=1)
	S += c10_t1_t1 >= 66
	c10_t1_t1 += MUL[0]

	c01_t4_t1 = S.Task('c01_t4_t1', length=7, delay_cost=1)
	S += c01_t4_t1 >= 67
	c01_t4_t1 += MUL[0]

	c02_t4_t1_in = S.Task('c02_t4_t1_in', length=1, delay_cost=1)
	S += c02_t4_t1_in >= 67
	c02_t4_t1_in += MUL_in[0]

	c02_t4_t1_mem0 = S.Task('c02_t4_t1_mem0', length=1, delay_cost=1)
	S += c02_t4_t1_mem0 >= 67
	c02_t4_t1_mem0 += ADD_mem[1]

	c02_t4_t1_mem1 = S.Task('c02_t4_t1_mem1', length=1, delay_cost=1)
	S += c02_t4_t1_mem1 >= 67
	c02_t4_t1_mem1 += ADD_mem[1]

	c02_t4_t1 = S.Task('c02_t4_t1', length=7, delay_cost=1)
	S += c02_t4_t1 >= 68
	c02_t4_t1 += MUL[0]

	c10_t4_t1_in = S.Task('c10_t4_t1_in', length=1, delay_cost=1)
	S += c10_t4_t1_in >= 68
	c10_t4_t1_in += MUL_in[0]

	c10_t4_t1_mem0 = S.Task('c10_t4_t1_mem0', length=1, delay_cost=1)
	S += c10_t4_t1_mem0 >= 68
	c10_t4_t1_mem0 += ADD_mem[3]

	c10_t4_t1_mem1 = S.Task('c10_t4_t1_mem1', length=1, delay_cost=1)
	S += c10_t4_t1_mem1 >= 68
	c10_t4_t1_mem1 += ADD_mem[0]

	c11_t01_mem0 = S.Task('c11_t01_mem0', length=1, delay_cost=1)
	S += c11_t01_mem0 >= 68
	c11_t01_mem0 += MUL_mem[0]

	c11_t01_mem1 = S.Task('c11_t01_mem1', length=1, delay_cost=1)
	S += c11_t01_mem1 >= 68
	c11_t01_mem1 += ADD_mem[2]

	c02_t1_s00_mem0 = S.Task('c02_t1_s00_mem0', length=1, delay_cost=1)
	S += c02_t1_s00_mem0 >= 69
	c02_t1_s00_mem0 += MUL_mem[0]

	c10_t4_t1 = S.Task('c10_t4_t1', length=7, delay_cost=1)
	S += c10_t4_t1 >= 69
	c10_t4_t1 += MUL[0]

	c11_t01 = S.Task('c11_t01', length=1, delay_cost=1)
	S += c11_t01 >= 69
	c11_t01 += ADD[1]

	c11_t4_t1_in = S.Task('c11_t4_t1_in', length=1, delay_cost=1)
	S += c11_t4_t1_in >= 69
	c11_t4_t1_in += MUL_in[0]

	c11_t4_t1_mem0 = S.Task('c11_t4_t1_mem0', length=1, delay_cost=1)
	S += c11_t4_t1_mem0 >= 69
	c11_t4_t1_mem0 += ADD_mem[3]

	c11_t4_t1_mem1 = S.Task('c11_t4_t1_mem1', length=1, delay_cost=1)
	S += c11_t4_t1_mem1 >= 69
	c11_t4_t1_mem1 += ADD_mem[0]

	c02_t1_s00 = S.Task('c02_t1_s00', length=1, delay_cost=1)
	S += c02_t1_s00 >= 70
	c02_t1_s00 += ADD[0]

	c11_t4_t1 = S.Task('c11_t4_t1', length=7, delay_cost=1)
	S += c11_t4_t1 >= 70
	c11_t4_t1 += MUL[0]

	c12_t1_s00_mem0 = S.Task('c12_t1_s00_mem0', length=1, delay_cost=1)
	S += c12_t1_s00_mem0 >= 70
	c12_t1_s00_mem0 += MUL_mem[0]

	c12_t4_t1_in = S.Task('c12_t4_t1_in', length=1, delay_cost=1)
	S += c12_t4_t1_in >= 70
	c12_t4_t1_in += MUL_in[0]

	c12_t4_t1_mem0 = S.Task('c12_t4_t1_mem0', length=1, delay_cost=1)
	S += c12_t4_t1_mem0 >= 70
	c12_t4_t1_mem0 += ADD_mem[0]

	c12_t4_t1_mem1 = S.Task('c12_t4_t1_mem1', length=1, delay_cost=1)
	S += c12_t4_t1_mem1 >= 70
	c12_t4_t1_mem1 += ADD_mem[2]

	c02_t1_s01_mem0 = S.Task('c02_t1_s01_mem0', length=1, delay_cost=1)
	S += c02_t1_s01_mem0 >= 71
	c02_t1_s01_mem0 += ADD_mem[0]

	c02_t1_s01_mem1 = S.Task('c02_t1_s01_mem1', length=1, delay_cost=1)
	S += c02_t1_s01_mem1 >= 71
	c02_t1_s01_mem1 += MUL_mem[0]

	c11_t1_s00_mem0 = S.Task('c11_t1_s00_mem0', length=1, delay_cost=1)
	S += c11_t1_s00_mem0 >= 71
	c11_t1_s00_mem0 += MUL_mem[0]

	c12_t1_s00 = S.Task('c12_t1_s00', length=1, delay_cost=1)
	S += c12_t1_s00 >= 71
	c12_t1_s00 += ADD[3]

	c12_t4_t1 = S.Task('c12_t4_t1', length=7, delay_cost=1)
	S += c12_t4_t1 >= 71
	c12_t4_t1 += MUL[0]

	c01_t1_s00_mem0 = S.Task('c01_t1_s00_mem0', length=1, delay_cost=1)
	S += c01_t1_s00_mem0 >= 72
	c01_t1_s00_mem0 += MUL_mem[0]

	c02_t1_s01 = S.Task('c02_t1_s01', length=1, delay_cost=1)
	S += c02_t1_s01 >= 72
	c02_t1_s01 += ADD[1]

	c11_t1_s00 = S.Task('c11_t1_s00', length=1, delay_cost=1)
	S += c11_t1_s00 >= 72
	c11_t1_s00 += ADD[2]

	c12_t1_s01_mem0 = S.Task('c12_t1_s01_mem0', length=1, delay_cost=1)
	S += c12_t1_s01_mem0 >= 72
	c12_t1_s01_mem0 += ADD_mem[3]

	c12_t1_s01_mem1 = S.Task('c12_t1_s01_mem1', length=1, delay_cost=1)
	S += c12_t1_s01_mem1 >= 72
	c12_t1_s01_mem1 += MUL_mem[0]

	c01_t1_s00 = S.Task('c01_t1_s00', length=1, delay_cost=1)
	S += c01_t1_s00 >= 73
	c01_t1_s00 += ADD[0]

	c10_t1_s00_mem0 = S.Task('c10_t1_s00_mem0', length=1, delay_cost=1)
	S += c10_t1_s00_mem0 >= 73
	c10_t1_s00_mem0 += MUL_mem[0]

	c11_t1_s01_mem0 = S.Task('c11_t1_s01_mem0', length=1, delay_cost=1)
	S += c11_t1_s01_mem0 >= 73
	c11_t1_s01_mem0 += ADD_mem[2]

	c11_t1_s01_mem1 = S.Task('c11_t1_s01_mem1', length=1, delay_cost=1)
	S += c11_t1_s01_mem1 >= 73
	c11_t1_s01_mem1 += MUL_mem[0]

	c12_t1_s01 = S.Task('c12_t1_s01', length=1, delay_cost=1)
	S += c12_t1_s01 >= 73
	c12_t1_s01 += ADD[2]

	c01_t1_s01_mem0 = S.Task('c01_t1_s01_mem0', length=1, delay_cost=1)
	S += c01_t1_s01_mem0 >= 74
	c01_t1_s01_mem0 += ADD_mem[0]

	c01_t1_s01_mem1 = S.Task('c01_t1_s01_mem1', length=1, delay_cost=1)
	S += c01_t1_s01_mem1 >= 74
	c01_t1_s01_mem1 += MUL_mem[0]

	c01_t4_s00_mem0 = S.Task('c01_t4_s00_mem0', length=1, delay_cost=1)
	S += c01_t4_s00_mem0 >= 74
	c01_t4_s00_mem0 += MUL_mem[0]

	c10_t1_s00 = S.Task('c10_t1_s00', length=1, delay_cost=1)
	S += c10_t1_s00 >= 74
	c10_t1_s00 += ADD[1]

	c11_t1_s01 = S.Task('c11_t1_s01', length=1, delay_cost=1)
	S += c11_t1_s01 >= 74
	c11_t1_s01 += ADD[2]

	c01_t1_s01 = S.Task('c01_t1_s01', length=1, delay_cost=1)
	S += c01_t1_s01 >= 75
	c01_t1_s01 += ADD[0]

	c01_t4_s00 = S.Task('c01_t4_s00', length=1, delay_cost=1)
	S += c01_t4_s00 >= 75
	c01_t4_s00 += ADD[2]

	c02_t4_s00_mem0 = S.Task('c02_t4_s00_mem0', length=1, delay_cost=1)
	S += c02_t4_s00_mem0 >= 75
	c02_t4_s00_mem0 += MUL_mem[0]

	c10_t1_s01_mem0 = S.Task('c10_t1_s01_mem0', length=1, delay_cost=1)
	S += c10_t1_s01_mem0 >= 75
	c10_t1_s01_mem0 += ADD_mem[1]

	c10_t1_s01_mem1 = S.Task('c10_t1_s01_mem1', length=1, delay_cost=1)
	S += c10_t1_s01_mem1 >= 75
	c10_t1_s01_mem1 += MUL_mem[0]

	c02_t4_s00 = S.Task('c02_t4_s00', length=1, delay_cost=1)
	S += c02_t4_s00 >= 76
	c02_t4_s00 += ADD[3]

	c10_t1_s01 = S.Task('c10_t1_s01', length=1, delay_cost=1)
	S += c10_t1_s01 >= 76
	c10_t1_s01 += ADD[0]

	c10_t4_s00_mem0 = S.Task('c10_t4_s00_mem0', length=1, delay_cost=1)
	S += c10_t4_s00_mem0 >= 76
	c10_t4_s00_mem0 += MUL_mem[0]

	c10_t4_s00 = S.Task('c10_t4_s00', length=1, delay_cost=1)
	S += c10_t4_s00 >= 77
	c10_t4_s00 += ADD[2]

	c11_t4_s00_mem0 = S.Task('c11_t4_s00_mem0', length=1, delay_cost=1)
	S += c11_t4_s00_mem0 >= 77
	c11_t4_s00_mem0 += MUL_mem[0]

	c11_t4_s00 = S.Task('c11_t4_s00', length=1, delay_cost=1)
	S += c11_t4_s00 >= 78
	c11_t4_s00 += ADD[3]

	c12_t4_s00_mem0 = S.Task('c12_t4_s00_mem0', length=1, delay_cost=1)
	S += c12_t4_s00_mem0 >= 78
	c12_t4_s00_mem0 += MUL_mem[0]

	c12_t4_s00 = S.Task('c12_t4_s00', length=1, delay_cost=1)
	S += c12_t4_s00 >= 79
	c12_t4_s00 += ADD[1]


	# new tasks
	c_f1010 = S.Task('c_f1010', length=1, delay_cost=1)
	c_f1010 += alt(ADD)

	c_f1010_mem0 = S.Task('c_f1010_mem0', length=1, delay_cost=1)
	c_f1010_mem0 += MUL_mem[0]
	S += 18 < c_f1010_mem0
	S += c_f1010_mem0 <= c_f1010

	c_f1010_mem1 = S.Task('c_f1010_mem1', length=1, delay_cost=1)
	c_f1010_mem1 += ADD_mem[1]
	S += 27 < c_f1010_mem1
	S += c_f1010_mem1 <= c_f1010

	c_f0110 = S.Task('c_f0110', length=1, delay_cost=1)
	c_f0110 += alt(ADD)

	c_f0110_mem0 = S.Task('c_f0110_mem0', length=1, delay_cost=1)
	c_f0110_mem0 += MUL_mem[0]
	S += 9 < c_f0110_mem0
	S += c_f0110_mem0 <= c_f0110

	c_f0110_mem1 = S.Task('c_f0110_mem1', length=1, delay_cost=1)
	c_f0110_mem1 += ADD_mem[2]
	S += 26 < c_f0110_mem1
	S += c_f0110_mem1 <= c_f0110

	c_f1110 = S.Task('c_f1110', length=1, delay_cost=1)
	c_f1110 += alt(ADD)

	c_f1110_mem0 = S.Task('c_f1110_mem0', length=1, delay_cost=1)
	c_f1110_mem0 += MUL_mem[0]
	S += 17 < c_f1110_mem0
	S += c_f1110_mem0 <= c_f1110

	c_f1110_mem1 = S.Task('c_f1110_mem1', length=1, delay_cost=1)
	c_f1110_mem1 += ADD_mem[3]
	S += 26 < c_f1110_mem1
	S += c_f1110_mem1 <= c_f1110

	c_f0210 = S.Task('c_f0210', length=1, delay_cost=1)
	c_f0210 += alt(ADD)

	c_f0210_mem0 = S.Task('c_f0210_mem0', length=1, delay_cost=1)
	c_f0210_mem0 += MUL_mem[0]
	S += 15 < c_f0210_mem0
	S += c_f0210_mem0 <= c_f0210

	c_f0210_mem1 = S.Task('c_f0210_mem1', length=1, delay_cost=1)
	c_f0210_mem1 += ADD_mem[0]
	S += 27 < c_f0210_mem1
	S += c_f0210_mem1 <= c_f0210

	c_f1210 = S.Task('c_f1210', length=1, delay_cost=1)
	c_f1210 += alt(ADD)

	c_f1210_mem0 = S.Task('c_f1210_mem0', length=1, delay_cost=1)
	c_f1210_mem0 += MUL_mem[0]
	S += 8 < c_f1210_mem0
	S += c_f1210_mem0 <= c_f1210

	c_f1210_mem1 = S.Task('c_f1210_mem1', length=1, delay_cost=1)
	c_f1210_mem1 += ADD_mem[0]
	S += 30 < c_f1210_mem1
	S += c_f1210_mem1 <= c_f1210

	c0010 = S.Task('c0010', length=1, delay_cost=1)
	c0010 += alt(ADD)

	S += 28<c0010

	c0010_mem0 = S.Task('c0010_mem0', length=1, delay_cost=1)
	c0010_mem0 += MUL_mem[0]
	S += 14 < c0010_mem0
	S += c0010_mem0 <= c0010

	c0010_mem1 = S.Task('c0010_mem1', length=1, delay_cost=1)
	c0010_mem1 += ADD_mem[2]
	S += 29 < c0010_mem1
	S += c0010_mem1 <= c0010

	c0010_w = S.Task('c0010_w', length=1, delay_cost=1)
	c0010_w += alt(INPUT_mem_w)
	S += c0010 <= c0010_w

	c10_t00 = S.Task('c10_t00', length=1, delay_cost=1)
	c10_t00 += alt(ADD)

	c10_t00_mem0 = S.Task('c10_t00_mem0', length=1, delay_cost=1)
	c10_t00_mem0 += MUL_mem[0]
	S += 12 < c10_t00_mem0
	S += c10_t00_mem0 <= c10_t00

	c10_t00_mem1 = S.Task('c10_t00_mem1', length=1, delay_cost=1)
	c10_t00_mem1 += ADD_mem[0]
	S += 25 < c10_t00_mem1
	S += c10_t00_mem1 <= c10_t00

	c10_t1_s02 = S.Task('c10_t1_s02', length=1, delay_cost=1)
	c10_t1_s02 += alt(ADD)

	c10_t1_s02_mem0 = S.Task('c10_t1_s02_mem0', length=1, delay_cost=1)
	c10_t1_s02_mem0 += ADD_mem[0]
	S += 76 < c10_t1_s02_mem0
	S += c10_t1_s02_mem0 <= c10_t1_s02

	c10_t4_s01 = S.Task('c10_t4_s01', length=1, delay_cost=1)
	c10_t4_s01 += alt(ADD)

	c10_t4_s01_mem0 = S.Task('c10_t4_s01_mem0', length=1, delay_cost=1)
	c10_t4_s01_mem0 += ADD_mem[2]
	S += 77 < c10_t4_s01_mem0
	S += c10_t4_s01_mem0 <= c10_t4_s01

	c10_t4_s01_mem1 = S.Task('c10_t4_s01_mem1', length=1, delay_cost=1)
	c10_t4_s01_mem1 += MUL_mem[0]
	S += 75 < c10_t4_s01_mem1
	S += c10_t4_s01_mem1 <= c10_t4_s01

	c01_t00 = S.Task('c01_t00', length=1, delay_cost=1)
	c01_t00 += alt(ADD)

	c01_t00_mem0 = S.Task('c01_t00_mem0', length=1, delay_cost=1)
	c01_t00_mem0 += MUL_mem[0]
	S += 45 < c01_t00_mem0
	S += c01_t00_mem0 <= c01_t00

	c01_t00_mem1 = S.Task('c01_t00_mem1', length=1, delay_cost=1)
	c01_t00_mem1 += ADD_mem[0]
	S += 53 < c01_t00_mem1
	S += c01_t00_mem1 <= c01_t00

	c01_t1_s02 = S.Task('c01_t1_s02', length=1, delay_cost=1)
	c01_t1_s02 += alt(ADD)

	c01_t1_s02_mem0 = S.Task('c01_t1_s02_mem0', length=1, delay_cost=1)
	c01_t1_s02_mem0 += ADD_mem[0]
	S += 75 < c01_t1_s02_mem0
	S += c01_t1_s02_mem0 <= c01_t1_s02

	c01_t4_s01 = S.Task('c01_t4_s01', length=1, delay_cost=1)
	c01_t4_s01 += alt(ADD)

	c01_t4_s01_mem0 = S.Task('c01_t4_s01_mem0', length=1, delay_cost=1)
	c01_t4_s01_mem0 += ADD_mem[2]
	S += 75 < c01_t4_s01_mem0
	S += c01_t4_s01_mem0 <= c01_t4_s01

	c01_t4_s01_mem1 = S.Task('c01_t4_s01_mem1', length=1, delay_cost=1)
	c01_t4_s01_mem1 += MUL_mem[0]
	S += 73 < c01_t4_s01_mem1
	S += c01_t4_s01_mem1 <= c01_t4_s01

	c11_t00 = S.Task('c11_t00', length=1, delay_cost=1)
	c11_t00 += alt(ADD)

	c11_t00_mem0 = S.Task('c11_t00_mem0', length=1, delay_cost=1)
	c11_t00_mem0 += MUL_mem[0]
	S += 38 < c11_t00_mem0
	S += c11_t00_mem0 <= c11_t00

	c11_t00_mem1 = S.Task('c11_t00_mem1', length=1, delay_cost=1)
	c11_t00_mem1 += ADD_mem[0]
	S += 49 < c11_t00_mem1
	S += c11_t00_mem1 <= c11_t00

	c11_t1_s02 = S.Task('c11_t1_s02', length=1, delay_cost=1)
	c11_t1_s02 += alt(ADD)

	c11_t1_s02_mem0 = S.Task('c11_t1_s02_mem0', length=1, delay_cost=1)
	c11_t1_s02_mem0 += ADD_mem[2]
	S += 74 < c11_t1_s02_mem0
	S += c11_t1_s02_mem0 <= c11_t1_s02

	c11_t4_s01 = S.Task('c11_t4_s01', length=1, delay_cost=1)
	c11_t4_s01 += alt(ADD)

	c11_t4_s01_mem0 = S.Task('c11_t4_s01_mem0', length=1, delay_cost=1)
	c11_t4_s01_mem0 += ADD_mem[3]
	S += 78 < c11_t4_s01_mem0
	S += c11_t4_s01_mem0 <= c11_t4_s01

	c11_t4_s01_mem1 = S.Task('c11_t4_s01_mem1', length=1, delay_cost=1)
	c11_t4_s01_mem1 += MUL_mem[0]
	S += 76 < c11_t4_s01_mem1
	S += c11_t4_s01_mem1 <= c11_t4_s01

	c02_t00 = S.Task('c02_t00', length=1, delay_cost=1)
	c02_t00 += alt(ADD)

	c02_t00_mem0 = S.Task('c02_t00_mem0', length=1, delay_cost=1)
	c02_t00_mem0 += MUL_mem[0]
	S += 43 < c02_t00_mem0
	S += c02_t00_mem0 <= c02_t00

	c02_t00_mem1 = S.Task('c02_t00_mem1', length=1, delay_cost=1)
	c02_t00_mem1 += ADD_mem[1]
	S += 48 < c02_t00_mem1
	S += c02_t00_mem1 <= c02_t00

	c02_t1_s02 = S.Task('c02_t1_s02', length=1, delay_cost=1)
	c02_t1_s02 += alt(ADD)

	c02_t1_s02_mem0 = S.Task('c02_t1_s02_mem0', length=1, delay_cost=1)
	c02_t1_s02_mem0 += ADD_mem[1]
	S += 72 < c02_t1_s02_mem0
	S += c02_t1_s02_mem0 <= c02_t1_s02

	c02_t4_s01 = S.Task('c02_t4_s01', length=1, delay_cost=1)
	c02_t4_s01 += alt(ADD)

	c02_t4_s01_mem0 = S.Task('c02_t4_s01_mem0', length=1, delay_cost=1)
	c02_t4_s01_mem0 += ADD_mem[3]
	S += 76 < c02_t4_s01_mem0
	S += c02_t4_s01_mem0 <= c02_t4_s01

	c02_t4_s01_mem1 = S.Task('c02_t4_s01_mem1', length=1, delay_cost=1)
	c02_t4_s01_mem1 += MUL_mem[0]
	S += 74 < c02_t4_s01_mem1
	S += c02_t4_s01_mem1 <= c02_t4_s01

	c12_t00 = S.Task('c12_t00', length=1, delay_cost=1)
	c12_t00 += alt(ADD)

	c12_t00_mem0 = S.Task('c12_t00_mem0', length=1, delay_cost=1)
	c12_t00_mem0 += MUL_mem[0]
	S += 41 < c12_t00_mem0
	S += c12_t00_mem0 <= c12_t00

	c12_t00_mem1 = S.Task('c12_t00_mem1', length=1, delay_cost=1)
	c12_t00_mem1 += ADD_mem[1]
	S += 50 < c12_t00_mem1
	S += c12_t00_mem1 <= c12_t00

	c12_t1_s02 = S.Task('c12_t1_s02', length=1, delay_cost=1)
	c12_t1_s02 += alt(ADD)

	c12_t1_s02_mem0 = S.Task('c12_t1_s02_mem0', length=1, delay_cost=1)
	c12_t1_s02_mem0 += ADD_mem[2]
	S += 73 < c12_t1_s02_mem0
	S += c12_t1_s02_mem0 <= c12_t1_s02

	c12_t4_s01 = S.Task('c12_t4_s01', length=1, delay_cost=1)
	c12_t4_s01 += alt(ADD)

	c12_t4_s01_mem0 = S.Task('c12_t4_s01_mem0', length=1, delay_cost=1)
	c12_t4_s01_mem0 += ADD_mem[1]
	S += 79 < c12_t4_s01_mem0
	S += c12_t4_s01_mem0 <= c12_t4_s01

	c12_t4_s01_mem1 = S.Task('c12_t4_s01_mem1', length=1, delay_cost=1)
	c12_t4_s01_mem1 += MUL_mem[0]
	S += 77 < c12_t4_s01_mem1
	S += c12_t4_s01_mem1 <= c12_t4_s01

	c10_t1_t0_in = S.Task('c10_t1_t0_in', length=1, delay_cost=1)
	c10_t1_t0_in += alt(MUL_in)
	c10_t1_t0 = S.Task('c10_t1_t0', length=7, delay_cost=1)
	c10_t1_t0 += alt(MUL)
	S += c10_t1_t0>=c10_t1_t0_in

	c10_t1_t0_mem0 = S.Task('c10_t1_t0_mem0', length=1, delay_cost=1)
	c10_t1_t0_mem0 += alt(ADD_mem)
	S += (c_f1010*ADD[0]) < c10_t1_t0_mem0*ADD_mem[0]
	S += (c_f1010*ADD[1]) < c10_t1_t0_mem0*ADD_mem[1]
	S += (c_f1010*ADD[2]) < c10_t1_t0_mem0*ADD_mem[2]
	S += (c_f1010*ADD[3]) < c10_t1_t0_mem0*ADD_mem[3]
	S += c10_t1_t0_mem0 <= c10_t1_t0

	c10_t1_t0_mem1 = S.Task('c10_t1_t0_mem1', length=1, delay_cost=1)
	c10_t1_t0_mem1 += INPUT_mem_r
	S += c10_t1_t0_mem1 <= c10_t1_t0

	c10_t1_t2 = S.Task('c10_t1_t2', length=1, delay_cost=1)
	c10_t1_t2 += alt(ADD)

	c10_t1_t2_mem0 = S.Task('c10_t1_t2_mem0', length=1, delay_cost=1)
	c10_t1_t2_mem0 += alt(ADD_mem)
	S += (c_f1010*ADD[0]) < c10_t1_t2_mem0*ADD_mem[0]
	S += (c_f1010*ADD[1]) < c10_t1_t2_mem0*ADD_mem[1]
	S += (c_f1010*ADD[2]) < c10_t1_t2_mem0*ADD_mem[2]
	S += (c_f1010*ADD[3]) < c10_t1_t2_mem0*ADD_mem[3]
	S += c10_t1_t2_mem0 <= c10_t1_t2

	c10_t1_t2_mem1 = S.Task('c10_t1_t2_mem1', length=1, delay_cost=1)
	c10_t1_t2_mem1 += ADD_mem[1]
	S += 34 < c10_t1_t2_mem1
	S += c10_t1_t2_mem1 <= c10_t1_t2

	c10_t1_s03 = S.Task('c10_t1_s03', length=1, delay_cost=1)
	c10_t1_s03 += alt(ADD)

	c10_t1_s03_mem0 = S.Task('c10_t1_s03_mem0', length=1, delay_cost=1)
	c10_t1_s03_mem0 += alt(ADD_mem)
	S += (c10_t1_s02*ADD[0]) < c10_t1_s03_mem0*ADD_mem[0]
	S += (c10_t1_s02*ADD[1]) < c10_t1_s03_mem0*ADD_mem[1]
	S += (c10_t1_s02*ADD[2]) < c10_t1_s03_mem0*ADD_mem[2]
	S += (c10_t1_s02*ADD[3]) < c10_t1_s03_mem0*ADD_mem[3]
	S += c10_t1_s03_mem0 <= c10_t1_s03

	c10_t20 = S.Task('c10_t20', length=1, delay_cost=1)
	c10_t20 += alt(ADD)

	c10_t20_mem0 = S.Task('c10_t20_mem0', length=1, delay_cost=1)
	c10_t20_mem0 += INPUT_mem_r
	S += c10_t20_mem0 <= c10_t20

	c10_t20_mem1 = S.Task('c10_t20_mem1', length=1, delay_cost=1)
	c10_t20_mem1 += alt(ADD_mem)
	S += (c_f1010*ADD[0]) < c10_t20_mem1*ADD_mem[0]
	S += (c_f1010*ADD[1]) < c10_t20_mem1*ADD_mem[1]
	S += (c_f1010*ADD[2]) < c10_t20_mem1*ADD_mem[2]
	S += (c_f1010*ADD[3]) < c10_t20_mem1*ADD_mem[3]
	S += c10_t20_mem1 <= c10_t20

	c10_t4_s02 = S.Task('c10_t4_s02', length=1, delay_cost=1)
	c10_t4_s02 += alt(ADD)

	c10_t4_s02_mem0 = S.Task('c10_t4_s02_mem0', length=1, delay_cost=1)
	c10_t4_s02_mem0 += alt(ADD_mem)
	S += (c10_t4_s01*ADD[0]) < c10_t4_s02_mem0*ADD_mem[0]
	S += (c10_t4_s01*ADD[1]) < c10_t4_s02_mem0*ADD_mem[1]
	S += (c10_t4_s01*ADD[2]) < c10_t4_s02_mem0*ADD_mem[2]
	S += (c10_t4_s01*ADD[3]) < c10_t4_s02_mem0*ADD_mem[3]
	S += c10_t4_s02_mem0 <= c10_t4_s02

	c01_t1_t0_in = S.Task('c01_t1_t0_in', length=1, delay_cost=1)
	c01_t1_t0_in += alt(MUL_in)
	c01_t1_t0 = S.Task('c01_t1_t0', length=7, delay_cost=1)
	c01_t1_t0 += alt(MUL)
	S += c01_t1_t0>=c01_t1_t0_in

	c01_t1_t0_mem0 = S.Task('c01_t1_t0_mem0', length=1, delay_cost=1)
	c01_t1_t0_mem0 += alt(ADD_mem)
	S += (c_f0110*ADD[0]) < c01_t1_t0_mem0*ADD_mem[0]
	S += (c_f0110*ADD[1]) < c01_t1_t0_mem0*ADD_mem[1]
	S += (c_f0110*ADD[2]) < c01_t1_t0_mem0*ADD_mem[2]
	S += (c_f0110*ADD[3]) < c01_t1_t0_mem0*ADD_mem[3]
	S += c01_t1_t0_mem0 <= c01_t1_t0

	c01_t1_t0_mem1 = S.Task('c01_t1_t0_mem1', length=1, delay_cost=1)
	c01_t1_t0_mem1 += INPUT_mem_r
	S += c01_t1_t0_mem1 <= c01_t1_t0

	c01_t1_t2 = S.Task('c01_t1_t2', length=1, delay_cost=1)
	c01_t1_t2 += alt(ADD)

	c01_t1_t2_mem0 = S.Task('c01_t1_t2_mem0', length=1, delay_cost=1)
	c01_t1_t2_mem0 += alt(ADD_mem)
	S += (c_f0110*ADD[0]) < c01_t1_t2_mem0*ADD_mem[0]
	S += (c_f0110*ADD[1]) < c01_t1_t2_mem0*ADD_mem[1]
	S += (c_f0110*ADD[2]) < c01_t1_t2_mem0*ADD_mem[2]
	S += (c_f0110*ADD[3]) < c01_t1_t2_mem0*ADD_mem[3]
	S += c01_t1_t2_mem0 <= c01_t1_t2

	c01_t1_t2_mem1 = S.Task('c01_t1_t2_mem1', length=1, delay_cost=1)
	c01_t1_t2_mem1 += ADD_mem[1]
	S += 31 < c01_t1_t2_mem1
	S += c01_t1_t2_mem1 <= c01_t1_t2

	c01_t1_s03 = S.Task('c01_t1_s03', length=1, delay_cost=1)
	c01_t1_s03 += alt(ADD)

	c01_t1_s03_mem0 = S.Task('c01_t1_s03_mem0', length=1, delay_cost=1)
	c01_t1_s03_mem0 += alt(ADD_mem)
	S += (c01_t1_s02*ADD[0]) < c01_t1_s03_mem0*ADD_mem[0]
	S += (c01_t1_s02*ADD[1]) < c01_t1_s03_mem0*ADD_mem[1]
	S += (c01_t1_s02*ADD[2]) < c01_t1_s03_mem0*ADD_mem[2]
	S += (c01_t1_s02*ADD[3]) < c01_t1_s03_mem0*ADD_mem[3]
	S += c01_t1_s03_mem0 <= c01_t1_s03

	c01_t20 = S.Task('c01_t20', length=1, delay_cost=1)
	c01_t20 += alt(ADD)

	c01_t20_mem0 = S.Task('c01_t20_mem0', length=1, delay_cost=1)
	c01_t20_mem0 += INPUT_mem_r
	S += c01_t20_mem0 <= c01_t20

	c01_t20_mem1 = S.Task('c01_t20_mem1', length=1, delay_cost=1)
	c01_t20_mem1 += alt(ADD_mem)
	S += (c_f0110*ADD[0]) < c01_t20_mem1*ADD_mem[0]
	S += (c_f0110*ADD[1]) < c01_t20_mem1*ADD_mem[1]
	S += (c_f0110*ADD[2]) < c01_t20_mem1*ADD_mem[2]
	S += (c_f0110*ADD[3]) < c01_t20_mem1*ADD_mem[3]
	S += c01_t20_mem1 <= c01_t20

	c01_t4_s02 = S.Task('c01_t4_s02', length=1, delay_cost=1)
	c01_t4_s02 += alt(ADD)

	c01_t4_s02_mem0 = S.Task('c01_t4_s02_mem0', length=1, delay_cost=1)
	c01_t4_s02_mem0 += alt(ADD_mem)
	S += (c01_t4_s01*ADD[0]) < c01_t4_s02_mem0*ADD_mem[0]
	S += (c01_t4_s01*ADD[1]) < c01_t4_s02_mem0*ADD_mem[1]
	S += (c01_t4_s01*ADD[2]) < c01_t4_s02_mem0*ADD_mem[2]
	S += (c01_t4_s01*ADD[3]) < c01_t4_s02_mem0*ADD_mem[3]
	S += c01_t4_s02_mem0 <= c01_t4_s02

	c11_t1_t0_in = S.Task('c11_t1_t0_in', length=1, delay_cost=1)
	c11_t1_t0_in += alt(MUL_in)
	c11_t1_t0 = S.Task('c11_t1_t0', length=7, delay_cost=1)
	c11_t1_t0 += alt(MUL)
	S += c11_t1_t0>=c11_t1_t0_in

	c11_t1_t0_mem0 = S.Task('c11_t1_t0_mem0', length=1, delay_cost=1)
	c11_t1_t0_mem0 += alt(ADD_mem)
	S += (c_f1110*ADD[0]) < c11_t1_t0_mem0*ADD_mem[0]
	S += (c_f1110*ADD[1]) < c11_t1_t0_mem0*ADD_mem[1]
	S += (c_f1110*ADD[2]) < c11_t1_t0_mem0*ADD_mem[2]
	S += (c_f1110*ADD[3]) < c11_t1_t0_mem0*ADD_mem[3]
	S += c11_t1_t0_mem0 <= c11_t1_t0

	c11_t1_t0_mem1 = S.Task('c11_t1_t0_mem1', length=1, delay_cost=1)
	c11_t1_t0_mem1 += INPUT_mem_r
	S += c11_t1_t0_mem1 <= c11_t1_t0

	c11_t1_t2 = S.Task('c11_t1_t2', length=1, delay_cost=1)
	c11_t1_t2 += alt(ADD)

	c11_t1_t2_mem0 = S.Task('c11_t1_t2_mem0', length=1, delay_cost=1)
	c11_t1_t2_mem0 += alt(ADD_mem)
	S += (c_f1110*ADD[0]) < c11_t1_t2_mem0*ADD_mem[0]
	S += (c_f1110*ADD[1]) < c11_t1_t2_mem0*ADD_mem[1]
	S += (c_f1110*ADD[2]) < c11_t1_t2_mem0*ADD_mem[2]
	S += (c_f1110*ADD[3]) < c11_t1_t2_mem0*ADD_mem[3]
	S += c11_t1_t2_mem0 <= c11_t1_t2

	c11_t1_t2_mem1 = S.Task('c11_t1_t2_mem1', length=1, delay_cost=1)
	c11_t1_t2_mem1 += ADD_mem[1]
	S += 32 < c11_t1_t2_mem1
	S += c11_t1_t2_mem1 <= c11_t1_t2

	c11_t1_s03 = S.Task('c11_t1_s03', length=1, delay_cost=1)
	c11_t1_s03 += alt(ADD)

	c11_t1_s03_mem0 = S.Task('c11_t1_s03_mem0', length=1, delay_cost=1)
	c11_t1_s03_mem0 += alt(ADD_mem)
	S += (c11_t1_s02*ADD[0]) < c11_t1_s03_mem0*ADD_mem[0]
	S += (c11_t1_s02*ADD[1]) < c11_t1_s03_mem0*ADD_mem[1]
	S += (c11_t1_s02*ADD[2]) < c11_t1_s03_mem0*ADD_mem[2]
	S += (c11_t1_s02*ADD[3]) < c11_t1_s03_mem0*ADD_mem[3]
	S += c11_t1_s03_mem0 <= c11_t1_s03

	c11_t20 = S.Task('c11_t20', length=1, delay_cost=1)
	c11_t20 += alt(ADD)

	c11_t20_mem0 = S.Task('c11_t20_mem0', length=1, delay_cost=1)
	c11_t20_mem0 += INPUT_mem_r
	S += c11_t20_mem0 <= c11_t20

	c11_t20_mem1 = S.Task('c11_t20_mem1', length=1, delay_cost=1)
	c11_t20_mem1 += alt(ADD_mem)
	S += (c_f1110*ADD[0]) < c11_t20_mem1*ADD_mem[0]
	S += (c_f1110*ADD[1]) < c11_t20_mem1*ADD_mem[1]
	S += (c_f1110*ADD[2]) < c11_t20_mem1*ADD_mem[2]
	S += (c_f1110*ADD[3]) < c11_t20_mem1*ADD_mem[3]
	S += c11_t20_mem1 <= c11_t20

	c11_t4_s02 = S.Task('c11_t4_s02', length=1, delay_cost=1)
	c11_t4_s02 += alt(ADD)

	c11_t4_s02_mem0 = S.Task('c11_t4_s02_mem0', length=1, delay_cost=1)
	c11_t4_s02_mem0 += alt(ADD_mem)
	S += (c11_t4_s01*ADD[0]) < c11_t4_s02_mem0*ADD_mem[0]
	S += (c11_t4_s01*ADD[1]) < c11_t4_s02_mem0*ADD_mem[1]
	S += (c11_t4_s01*ADD[2]) < c11_t4_s02_mem0*ADD_mem[2]
	S += (c11_t4_s01*ADD[3]) < c11_t4_s02_mem0*ADD_mem[3]
	S += c11_t4_s02_mem0 <= c11_t4_s02

	c02_t1_t0_in = S.Task('c02_t1_t0_in', length=1, delay_cost=1)
	c02_t1_t0_in += alt(MUL_in)
	c02_t1_t0 = S.Task('c02_t1_t0', length=7, delay_cost=1)
	c02_t1_t0 += alt(MUL)
	S += c02_t1_t0>=c02_t1_t0_in

	c02_t1_t0_mem0 = S.Task('c02_t1_t0_mem0', length=1, delay_cost=1)
	c02_t1_t0_mem0 += alt(ADD_mem)
	S += (c_f0210*ADD[0]) < c02_t1_t0_mem0*ADD_mem[0]
	S += (c_f0210*ADD[1]) < c02_t1_t0_mem0*ADD_mem[1]
	S += (c_f0210*ADD[2]) < c02_t1_t0_mem0*ADD_mem[2]
	S += (c_f0210*ADD[3]) < c02_t1_t0_mem0*ADD_mem[3]
	S += c02_t1_t0_mem0 <= c02_t1_t0

	c02_t1_t0_mem1 = S.Task('c02_t1_t0_mem1', length=1, delay_cost=1)
	c02_t1_t0_mem1 += INPUT_mem_r
	S += c02_t1_t0_mem1 <= c02_t1_t0

	c02_t1_t2 = S.Task('c02_t1_t2', length=1, delay_cost=1)
	c02_t1_t2 += alt(ADD)

	c02_t1_t2_mem0 = S.Task('c02_t1_t2_mem0', length=1, delay_cost=1)
	c02_t1_t2_mem0 += alt(ADD_mem)
	S += (c_f0210*ADD[0]) < c02_t1_t2_mem0*ADD_mem[0]
	S += (c_f0210*ADD[1]) < c02_t1_t2_mem0*ADD_mem[1]
	S += (c_f0210*ADD[2]) < c02_t1_t2_mem0*ADD_mem[2]
	S += (c_f0210*ADD[3]) < c02_t1_t2_mem0*ADD_mem[3]
	S += c02_t1_t2_mem0 <= c02_t1_t2

	c02_t1_t2_mem1 = S.Task('c02_t1_t2_mem1', length=1, delay_cost=1)
	c02_t1_t2_mem1 += ADD_mem[0]
	S += 29 < c02_t1_t2_mem1
	S += c02_t1_t2_mem1 <= c02_t1_t2

	c02_t1_s03 = S.Task('c02_t1_s03', length=1, delay_cost=1)
	c02_t1_s03 += alt(ADD)

	c02_t1_s03_mem0 = S.Task('c02_t1_s03_mem0', length=1, delay_cost=1)
	c02_t1_s03_mem0 += alt(ADD_mem)
	S += (c02_t1_s02*ADD[0]) < c02_t1_s03_mem0*ADD_mem[0]
	S += (c02_t1_s02*ADD[1]) < c02_t1_s03_mem0*ADD_mem[1]
	S += (c02_t1_s02*ADD[2]) < c02_t1_s03_mem0*ADD_mem[2]
	S += (c02_t1_s02*ADD[3]) < c02_t1_s03_mem0*ADD_mem[3]
	S += c02_t1_s03_mem0 <= c02_t1_s03

	c02_t20 = S.Task('c02_t20', length=1, delay_cost=1)
	c02_t20 += alt(ADD)

	c02_t20_mem0 = S.Task('c02_t20_mem0', length=1, delay_cost=1)
	c02_t20_mem0 += INPUT_mem_r
	S += c02_t20_mem0 <= c02_t20

	c02_t20_mem1 = S.Task('c02_t20_mem1', length=1, delay_cost=1)
	c02_t20_mem1 += alt(ADD_mem)
	S += (c_f0210*ADD[0]) < c02_t20_mem1*ADD_mem[0]
	S += (c_f0210*ADD[1]) < c02_t20_mem1*ADD_mem[1]
	S += (c_f0210*ADD[2]) < c02_t20_mem1*ADD_mem[2]
	S += (c_f0210*ADD[3]) < c02_t20_mem1*ADD_mem[3]
	S += c02_t20_mem1 <= c02_t20

	c02_t4_s02 = S.Task('c02_t4_s02', length=1, delay_cost=1)
	c02_t4_s02 += alt(ADD)

	c02_t4_s02_mem0 = S.Task('c02_t4_s02_mem0', length=1, delay_cost=1)
	c02_t4_s02_mem0 += alt(ADD_mem)
	S += (c02_t4_s01*ADD[0]) < c02_t4_s02_mem0*ADD_mem[0]
	S += (c02_t4_s01*ADD[1]) < c02_t4_s02_mem0*ADD_mem[1]
	S += (c02_t4_s01*ADD[2]) < c02_t4_s02_mem0*ADD_mem[2]
	S += (c02_t4_s01*ADD[3]) < c02_t4_s02_mem0*ADD_mem[3]
	S += c02_t4_s02_mem0 <= c02_t4_s02

	c12_t1_t0_in = S.Task('c12_t1_t0_in', length=1, delay_cost=1)
	c12_t1_t0_in += alt(MUL_in)
	c12_t1_t0 = S.Task('c12_t1_t0', length=7, delay_cost=1)
	c12_t1_t0 += alt(MUL)
	S += c12_t1_t0>=c12_t1_t0_in

	c12_t1_t0_mem0 = S.Task('c12_t1_t0_mem0', length=1, delay_cost=1)
	c12_t1_t0_mem0 += alt(ADD_mem)
	S += (c_f1210*ADD[0]) < c12_t1_t0_mem0*ADD_mem[0]
	S += (c_f1210*ADD[1]) < c12_t1_t0_mem0*ADD_mem[1]
	S += (c_f1210*ADD[2]) < c12_t1_t0_mem0*ADD_mem[2]
	S += (c_f1210*ADD[3]) < c12_t1_t0_mem0*ADD_mem[3]
	S += c12_t1_t0_mem0 <= c12_t1_t0

	c12_t1_t0_mem1 = S.Task('c12_t1_t0_mem1', length=1, delay_cost=1)
	c12_t1_t0_mem1 += INPUT_mem_r
	S += c12_t1_t0_mem1 <= c12_t1_t0

	c12_t1_t2 = S.Task('c12_t1_t2', length=1, delay_cost=1)
	c12_t1_t2 += alt(ADD)

	c12_t1_t2_mem0 = S.Task('c12_t1_t2_mem0', length=1, delay_cost=1)
	c12_t1_t2_mem0 += alt(ADD_mem)
	S += (c_f1210*ADD[0]) < c12_t1_t2_mem0*ADD_mem[0]
	S += (c_f1210*ADD[1]) < c12_t1_t2_mem0*ADD_mem[1]
	S += (c_f1210*ADD[2]) < c12_t1_t2_mem0*ADD_mem[2]
	S += (c_f1210*ADD[3]) < c12_t1_t2_mem0*ADD_mem[3]
	S += c12_t1_t2_mem0 <= c12_t1_t2

	c12_t1_t2_mem1 = S.Task('c12_t1_t2_mem1', length=1, delay_cost=1)
	c12_t1_t2_mem1 += ADD_mem[0]
	S += 41 < c12_t1_t2_mem1
	S += c12_t1_t2_mem1 <= c12_t1_t2

	c12_t1_s03 = S.Task('c12_t1_s03', length=1, delay_cost=1)
	c12_t1_s03 += alt(ADD)

	c12_t1_s03_mem0 = S.Task('c12_t1_s03_mem0', length=1, delay_cost=1)
	c12_t1_s03_mem0 += alt(ADD_mem)
	S += (c12_t1_s02*ADD[0]) < c12_t1_s03_mem0*ADD_mem[0]
	S += (c12_t1_s02*ADD[1]) < c12_t1_s03_mem0*ADD_mem[1]
	S += (c12_t1_s02*ADD[2]) < c12_t1_s03_mem0*ADD_mem[2]
	S += (c12_t1_s02*ADD[3]) < c12_t1_s03_mem0*ADD_mem[3]
	S += c12_t1_s03_mem0 <= c12_t1_s03

	c12_t20 = S.Task('c12_t20', length=1, delay_cost=1)
	c12_t20 += alt(ADD)

	c12_t20_mem0 = S.Task('c12_t20_mem0', length=1, delay_cost=1)
	c12_t20_mem0 += INPUT_mem_r
	S += c12_t20_mem0 <= c12_t20

	c12_t20_mem1 = S.Task('c12_t20_mem1', length=1, delay_cost=1)
	c12_t20_mem1 += alt(ADD_mem)
	S += (c_f1210*ADD[0]) < c12_t20_mem1*ADD_mem[0]
	S += (c_f1210*ADD[1]) < c12_t20_mem1*ADD_mem[1]
	S += (c_f1210*ADD[2]) < c12_t20_mem1*ADD_mem[2]
	S += (c_f1210*ADD[3]) < c12_t20_mem1*ADD_mem[3]
	S += c12_t20_mem1 <= c12_t20

	c12_t4_s02 = S.Task('c12_t4_s02', length=1, delay_cost=1)
	c12_t4_s02 += alt(ADD)

	c12_t4_s02_mem0 = S.Task('c12_t4_s02_mem0', length=1, delay_cost=1)
	c12_t4_s02_mem0 += alt(ADD_mem)
	S += (c12_t4_s01*ADD[0]) < c12_t4_s02_mem0*ADD_mem[0]
	S += (c12_t4_s01*ADD[1]) < c12_t4_s02_mem0*ADD_mem[1]
	S += (c12_t4_s01*ADD[2]) < c12_t4_s02_mem0*ADD_mem[2]
	S += (c12_t4_s01*ADD[3]) < c12_t4_s02_mem0*ADD_mem[3]
	S += c12_t4_s02_mem0 <= c12_t4_s02

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls24-315/scheduling/FROB_mul1_add4/FROB_5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

