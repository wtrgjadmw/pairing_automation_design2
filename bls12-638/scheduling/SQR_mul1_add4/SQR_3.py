from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 131
	S = Scenario("SQR_3", horizon=horizon)

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
	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 0
	c_t2_t3_t1_in += MUL_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 0
	c_t2_t3_t1_mem0 += INPUT_mem_r

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 0
	c_t2_t3_t1_mem1 += INPUT_mem_r

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 1
	c_t2_t3_t0_in += MUL_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 1
	c_t2_t3_t0_mem0 += INPUT_mem_r

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 1
	c_t2_t3_t0_mem1 += INPUT_mem_r

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=7, delay_cost=1)
	S += c_t2_t3_t1 >= 1
	c_t2_t3_t1 += MUL[0]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 2
	c_t1_t3_t1_in += MUL_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 2
	c_t1_t3_t1_mem0 += INPUT_mem_r

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 2
	c_t1_t3_t1_mem1 += INPUT_mem_r

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=7, delay_cost=1)
	S += c_t2_t3_t0 >= 2
	c_t2_t3_t0 += MUL[0]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 3
	c_t1_t3_t0_in += MUL_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 3
	c_t1_t3_t0_mem0 += INPUT_mem_r

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 3
	c_t1_t3_t0_mem1 += INPUT_mem_r

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=7, delay_cost=1)
	S += c_t1_t3_t1 >= 3
	c_t1_t3_t1 += MUL[0]

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 4
	c_t0_t3_t1_in += MUL_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 4
	c_t0_t3_t1_mem0 += INPUT_mem_r

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 4
	c_t0_t3_t1_mem1 += INPUT_mem_r

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=7, delay_cost=1)
	S += c_t1_t3_t0 >= 4
	c_t1_t3_t0 += MUL[0]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 5
	c_t0_t3_t0_in += MUL_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 5
	c_t0_t3_t0_mem0 += INPUT_mem_r

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 5
	c_t0_t3_t0_mem1 += INPUT_mem_r

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=7, delay_cost=1)
	S += c_t0_t3_t1 >= 5
	c_t0_t3_t1 += MUL[0]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=7, delay_cost=1)
	S += c_t0_t3_t0 >= 6
	c_t0_t3_t0 += MUL[0]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 6
	c_t1_a1_1_mem0 += INPUT_mem_r

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 6
	c_t1_a1_1_mem1 += INPUT_mem_r

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=1, delay_cost=1)
	S += c_t1_a1_1 >= 7
	c_t1_a1_1 += ADD[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 7
	c_t4001_mem0 += INPUT_mem_r

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 7
	c_t4001_mem1 += INPUT_mem_r

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem0 >= 8
	c_t2_t3_t5_mem0 += MUL_mem[0]

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem1 >= 8
	c_t2_t3_t5_mem1 += MUL_mem[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 8
	c_t4000_mem0 += INPUT_mem_r

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 8
	c_t4000_mem1 += INPUT_mem_r

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 8
	c_t4001 += ADD[1]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 9
	c_t2_t30_mem0 += MUL_mem[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 9
	c_t2_t30_mem1 += MUL_mem[0]

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=1, delay_cost=1)
	S += c_t2_t3_t5 >= 9
	c_t2_t3_t5 += ADD[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 9
	c_t3011_mem0 += INPUT_mem_r

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 9
	c_t3011_mem1 += INPUT_mem_r

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 9
	c_t4000 += ADD[3]

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem0 >= 9
	c_t4_t3_t2_mem0 += ADD_mem[3]

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem1 >= 9
	c_t4_t3_t2_mem1 += ADD_mem[1]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 10
	c_t1_t30_mem0 += MUL_mem[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 10
	c_t1_t30_mem1 += MUL_mem[0]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 10
	c_t1_t3_t2_mem0 += INPUT_mem_r

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 10
	c_t1_t3_t2_mem1 += INPUT_mem_r

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	S += c_t2_t30 >= 10
	c_t2_t30 += ADD[0]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 10
	c_t3011 += ADD[3]

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=1, delay_cost=1)
	S += c_t4_t3_t2 >= 10
	c_t4_t3_t2 += ADD[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 11
	c_t0_t10_mem0 += INPUT_mem_r

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 11
	c_t0_t10_mem1 += INPUT_mem_r

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 11
	c_t1_t30 += ADD[2]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	S += c_t1_t3_t2 >= 11
	c_t1_t3_t2 += ADD[0]

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem0 >= 11
	c_t1_t3_t5_mem0 += MUL_mem[0]

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem1 >= 11
	c_t1_t3_t5_mem1 += MUL_mem[0]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 12
	c_t0_t10 += ADD[3]

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem0 >= 12
	c_t0_t3_t5_mem0 += MUL_mem[0]

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem1 >= 12
	c_t0_t3_t5_mem1 += MUL_mem[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 12
	c_t1_t10_mem0 += INPUT_mem_r

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 12
	c_t1_t10_mem1 += INPUT_mem_r

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=1, delay_cost=1)
	S += c_t1_t3_t5 >= 12
	c_t1_t3_t5 += ADD[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 13
	c_t0_t30_mem0 += MUL_mem[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 13
	c_t0_t30_mem1 += MUL_mem[0]

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=1, delay_cost=1)
	S += c_t0_t3_t5 >= 13
	c_t0_t3_t5 += ADD[0]

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 13
	c_t1_t10 += ADD[3]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 13
	c_t1_t11_mem0 += INPUT_mem_r

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 13
	c_t1_t11_mem1 += INPUT_mem_r

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 14
	c_t0_t30 += ADD[1]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 14
	c_t0_t3_t3_mem0 += INPUT_mem_r

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 14
	c_t0_t3_t3_mem1 += INPUT_mem_r

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 14
	c_t1_t11 += ADD[0]

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem0 >= 14
	c_t1_t2_t3_mem0 += ADD_mem[3]

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem1 >= 14
	c_t1_t2_t3_mem1 += ADD_mem[0]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	S += c_t0_t3_t3 >= 15
	c_t0_t3_t3 += ADD[0]

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=1, delay_cost=1)
	S += c_t1_t2_t3 >= 15
	c_t1_t2_t3 += ADD[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 15
	c_t3001_mem0 += INPUT_mem_r

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 15
	c_t3001_mem1 += INPUT_mem_r

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 16
	c_t2_t3_t3_mem0 += INPUT_mem_r

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 16
	c_t2_t3_t3_mem1 += INPUT_mem_r

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 16
	c_t3001 += ADD[3]

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	S += c_t3_t3_t1_in >= 16
	c_t3_t3_t1_in += MUL_in[0]

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem0 >= 16
	c_t3_t3_t1_mem0 += ADD_mem[3]

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem1 >= 16
	c_t3_t3_t1_mem1 += ADD_mem[3]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 17
	c_t0_t11_mem0 += INPUT_mem_r

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 17
	c_t0_t11_mem1 += INPUT_mem_r

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	S += c_t2_t3_t3 >= 17
	c_t2_t3_t3 += ADD[2]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 17
	c_t3_t11_mem0 += ADD_mem[3]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 17
	c_t3_t11_mem1 += ADD_mem[3]

	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=7, delay_cost=1)
	S += c_t3_t3_t1 >= 17
	c_t3_t3_t1 += MUL[0]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 18
	c_t0_a1_0_mem0 += INPUT_mem_r

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 18
	c_t0_a1_0_mem1 += INPUT_mem_r

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 18
	c_t0_t11 += ADD[0]

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem0 >= 18
	c_t0_t2_t3_mem0 += ADD_mem[3]

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem1 >= 18
	c_t0_t2_t3_mem1 += ADD_mem[0]

	c_t3_t11 = S.Task('c_t3_t11', length=1, delay_cost=1)
	S += c_t3_t11 >= 18
	c_t3_t11 += ADD[3]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=1, delay_cost=1)
	S += c_t0_a1_0 >= 19
	c_t0_a1_0 += ADD[0]

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=1, delay_cost=1)
	S += c_t0_t2_t3 >= 19
	c_t0_t2_t3 += ADD[1]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 19
	c_t3000_mem0 += INPUT_mem_r

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 19
	c_t3000_mem1 += INPUT_mem_r

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 20
	c_t0_t3_t2_mem0 += INPUT_mem_r

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 20
	c_t0_t3_t2_mem1 += INPUT_mem_r

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 20
	c_t3000 += ADD[3]

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem0 >= 20
	c_t3_t3_t2_mem0 += ADD_mem[3]

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem1 >= 20
	c_t3_t3_t2_mem1 += ADD_mem[3]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	S += c_t0_t3_t2 >= 21
	c_t0_t3_t2 += ADD[2]

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	S += c_t0_t3_t4_in >= 21
	c_t0_t3_t4_in += MUL_in[0]

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem0 >= 21
	c_t0_t3_t4_mem0 += ADD_mem[2]

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem1 >= 21
	c_t0_t3_t4_mem1 += ADD_mem[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 21
	c_t3010_mem0 += INPUT_mem_r

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 21
	c_t3010_mem1 += INPUT_mem_r

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=1, delay_cost=1)
	S += c_t3_t3_t2 >= 21
	c_t3_t3_t2 += ADD[3]

	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=7, delay_cost=1)
	S += c_t0_t3_t4 >= 22
	c_t0_t3_t4 += MUL[0]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 22
	c_t1_a1_0_mem0 += INPUT_mem_r

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 22
	c_t1_a1_0_mem1 += INPUT_mem_r

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 22
	c_t3010 += ADD[1]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 22
	c_t3_t10_mem0 += ADD_mem[3]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 22
	c_t3_t10_mem1 += ADD_mem[1]

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	S += c_t3_t3_t0_in >= 22
	c_t3_t3_t0_in += MUL_in[0]

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem0 >= 22
	c_t3_t3_t0_mem0 += ADD_mem[3]

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem1 >= 22
	c_t3_t3_t0_mem1 += ADD_mem[1]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=1, delay_cost=1)
	S += c_t1_a1_0 >= 23
	c_t1_a1_0 += ADD[0]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 23
	c_t2_t3_t2_mem0 += INPUT_mem_r

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 23
	c_t2_t3_t2_mem1 += INPUT_mem_r

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	S += c_t3_a1_0_mem0 >= 23
	c_t3_a1_0_mem0 += ADD_mem[1]

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	S += c_t3_a1_0_mem1 >= 23
	c_t3_a1_0_mem1 += ADD_mem[3]

	c_t3_t10 = S.Task('c_t3_t10', length=1, delay_cost=1)
	S += c_t3_t10 >= 23
	c_t3_t10 += ADD[2]

	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=7, delay_cost=1)
	S += c_t3_t3_t0 >= 23
	c_t3_t3_t0 += MUL[0]

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem0 >= 23
	c_t3_t3_t3_mem0 += ADD_mem[1]

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem1 >= 23
	c_t3_t3_t3_mem1 += ADD_mem[3]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 24
	c_t2_t11_mem0 += INPUT_mem_r

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 24
	c_t2_t11_mem1 += INPUT_mem_r

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	S += c_t2_t3_t2 >= 24
	c_t2_t3_t2 += ADD[3]

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	S += c_t2_t3_t4_in >= 24
	c_t2_t3_t4_in += MUL_in[0]

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem0 >= 24
	c_t2_t3_t4_mem0 += ADD_mem[3]

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem1 >= 24
	c_t2_t3_t4_mem1 += ADD_mem[2]

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=1, delay_cost=1)
	S += c_t3_a1_0 >= 24
	c_t3_a1_0 += ADD[0]

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	S += c_t3_a1_1_mem0 >= 24
	c_t3_a1_1_mem0 += ADD_mem[3]

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	S += c_t3_a1_1_mem1 >= 24
	c_t3_a1_1_mem1 += ADD_mem[1]

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=1, delay_cost=1)
	S += c_t3_t3_t3 >= 24
	c_t3_t3_t3 += ADD[2]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 25
	c_t2_t10_mem0 += INPUT_mem_r

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 25
	c_t2_t10_mem1 += INPUT_mem_r

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 25
	c_t2_t11 += ADD[3]

	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=7, delay_cost=1)
	S += c_t2_t3_t4 >= 25
	c_t2_t3_t4 += MUL[0]

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=1, delay_cost=1)
	S += c_t3_a1_1 >= 25
	c_t3_a1_1 += ADD[2]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 26
	c_t2_a1_1_mem0 += INPUT_mem_r

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 26
	c_t2_a1_1_mem1 += INPUT_mem_r

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 26
	c_t2_t10 += ADD[1]

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem0 >= 26
	c_t2_t2_t3_mem0 += ADD_mem[1]

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem1 >= 26
	c_t2_t2_t3_mem1 += ADD_mem[3]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 27
	c_t0_a1_1_mem0 += INPUT_mem_r

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 27
	c_t0_a1_1_mem1 += INPUT_mem_r

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=1, delay_cost=1)
	S += c_t2_a1_1 >= 27
	c_t2_a1_1 += ADD[0]

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=1, delay_cost=1)
	S += c_t2_t2_t3 >= 27
	c_t2_t2_t3 += ADD[3]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=1, delay_cost=1)
	S += c_t0_a1_1 >= 28
	c_t0_a1_1 += ADD[1]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 28
	c_t2_a1_0_mem0 += INPUT_mem_r

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 28
	c_t2_a1_0_mem1 += INPUT_mem_r

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 29
	c_t1_t3_t3_mem0 += INPUT_mem_r

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 29
	c_t1_t3_t3_mem1 += INPUT_mem_r

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=1, delay_cost=1)
	S += c_t2_a1_0 >= 29
	c_t2_a1_0 += ADD[0]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	S += c_t1_t3_t3 >= 30
	c_t1_t3_t3 += ADD[2]

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	S += c_t1_t3_t4_in >= 30
	c_t1_t3_t4_in += MUL_in[0]

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem0 >= 30
	c_t1_t3_t4_mem0 += ADD_mem[0]

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem1 >= 30
	c_t1_t3_t4_mem1 += ADD_mem[2]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 30
	c_t4010_mem0 += INPUT_mem_r

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 30
	c_t4010_mem1 += INPUT_mem_r

	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=7, delay_cost=1)
	S += c_t1_t3_t4 >= 31
	c_t1_t3_t4 += MUL[0]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 31
	c_t4010 += ADD[0]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 31
	c_t4_t10_mem0 += ADD_mem[3]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 31
	c_t4_t10_mem1 += ADD_mem[0]

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	S += c_t4_t3_t0_in >= 31
	c_t4_t3_t0_in += MUL_in[0]

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem0 >= 31
	c_t4_t3_t0_mem0 += ADD_mem[3]

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem1 >= 31
	c_t4_t3_t0_mem1 += ADD_mem[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 31
	c_t5000_mem0 += INPUT_mem_r

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 31
	c_t5000_mem1 += INPUT_mem_r

	c_t4_t10 = S.Task('c_t4_t10', length=1, delay_cost=1)
	S += c_t4_t10 >= 32
	c_t4_t10 += ADD[1]

	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=7, delay_cost=1)
	S += c_t4_t3_t0 >= 32
	c_t4_t3_t0 += MUL[0]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 32
	c_t5000 += ADD[0]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 32
	c_t5011_mem0 += INPUT_mem_r

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 32
	c_t5011_mem1 += INPUT_mem_r

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 33
	c_t5010_mem0 += INPUT_mem_r

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 33
	c_t5010_mem1 += INPUT_mem_r

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 33
	c_t5011 += ADD[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 34
	c_t4011_mem0 += INPUT_mem_r

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 34
	c_t4011_mem1 += INPUT_mem_r

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 34
	c_t5010 += ADD[2]

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	S += c_t5_a1_1_mem0 >= 34
	c_t5_a1_1_mem0 += ADD_mem[1]

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	S += c_t5_a1_1_mem1 >= 34
	c_t5_a1_1_mem1 += ADD_mem[2]

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	S += c_t5_t3_t0_in >= 34
	c_t5_t3_t0_in += MUL_in[0]

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem0 >= 34
	c_t5_t3_t0_mem0 += ADD_mem[0]

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem1 >= 34
	c_t5_t3_t0_mem1 += ADD_mem[2]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 35
	c_t4011 += ADD[3]

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	S += c_t4_a1_0_mem0 >= 35
	c_t4_a1_0_mem0 += ADD_mem[0]

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	S += c_t4_a1_0_mem1 >= 35
	c_t4_a1_0_mem1 += ADD_mem[3]

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	S += c_t4_t3_t1_in >= 35
	c_t4_t3_t1_in += MUL_in[0]

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem0 >= 35
	c_t4_t3_t1_mem0 += ADD_mem[1]

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem1 >= 35
	c_t4_t3_t1_mem1 += ADD_mem[3]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 35
	c_t5001_mem0 += INPUT_mem_r

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 35
	c_t5001_mem1 += INPUT_mem_r

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	S += c_t5_a1_0_mem0 >= 35
	c_t5_a1_0_mem0 += ADD_mem[2]

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	S += c_t5_a1_0_mem1 >= 35
	c_t5_a1_0_mem1 += ADD_mem[1]

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=1, delay_cost=1)
	S += c_t5_a1_1 >= 35
	c_t5_a1_1 += ADD[0]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 35
	c_t5_t10_mem0 += ADD_mem[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 35
	c_t5_t10_mem1 += ADD_mem[2]

	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=7, delay_cost=1)
	S += c_t5_t3_t0 >= 35
	c_t5_t3_t0 += MUL[0]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 36
	c_t1_t00_mem0 += INPUT_mem_r

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 36
	c_t1_t00_mem1 += ADD_mem[0]

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=1, delay_cost=1)
	S += c_t4_a1_0 >= 36
	c_t4_a1_0 += ADD[0]

	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=7, delay_cost=1)
	S += c_t4_t3_t1 >= 36
	c_t4_t3_t1 += MUL[0]

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem0 >= 36
	c_t4_t3_t3_mem0 += ADD_mem[0]

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem1 >= 36
	c_t4_t3_t3_mem1 += ADD_mem[3]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 36
	c_t5001 += ADD[3]

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=1, delay_cost=1)
	S += c_t5_a1_0 >= 36
	c_t5_a1_0 += ADD[2]

	c_t5_t10 = S.Task('c_t5_t10', length=1, delay_cost=1)
	S += c_t5_t10 >= 36
	c_t5_t10 += ADD[1]

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	S += c_t5_t3_t1_in >= 36
	c_t5_t3_t1_in += MUL_in[0]

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem0 >= 36
	c_t5_t3_t1_mem0 += ADD_mem[3]

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem1 >= 36
	c_t5_t3_t1_mem1 += ADD_mem[1]

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem0 >= 36
	c_t5_t3_t3_mem0 += ADD_mem[2]

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem1 >= 36
	c_t5_t3_t3_mem1 += ADD_mem[1]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 37
	c_t0_t01_mem0 += INPUT_mem_r

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 37
	c_t0_t01_mem1 += ADD_mem[1]

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	S += c_t1_t00 >= 37
	c_t1_t00 += ADD[0]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 37
	c_t2_t00_mem0 += INPUT_mem_r

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 37
	c_t2_t00_mem1 += ADD_mem[0]

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=1, delay_cost=1)
	S += c_t4_t3_t3 >= 37
	c_t4_t3_t3 += ADD[3]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 37
	c_t5_t11_mem0 += ADD_mem[3]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 37
	c_t5_t11_mem1 += ADD_mem[1]

	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=7, delay_cost=1)
	S += c_t5_t3_t1 >= 37
	c_t5_t3_t1 += MUL[0]

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem0 >= 37
	c_t5_t3_t2_mem0 += ADD_mem[0]

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem1 >= 37
	c_t5_t3_t2_mem1 += ADD_mem[3]

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=1, delay_cost=1)
	S += c_t5_t3_t3 >= 37
	c_t5_t3_t3 += ADD[2]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 38
	c_t0_t00_mem0 += INPUT_mem_r

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 38
	c_t0_t00_mem1 += ADD_mem[0]

	c_t0_t01 = S.Task('c_t0_t01', length=1, delay_cost=1)
	S += c_t0_t01 >= 38
	c_t0_t01 += ADD[2]

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	S += c_t2_t00 >= 38
	c_t2_t00 += ADD[3]

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	S += c_t4_a1_1_mem0 >= 38
	c_t4_a1_1_mem0 += ADD_mem[3]

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	S += c_t4_a1_1_mem1 >= 38
	c_t4_a1_1_mem1 += ADD_mem[0]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 38
	c_t4_t11_mem0 += ADD_mem[1]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 38
	c_t4_t11_mem1 += ADD_mem[3]

	c_t5_t11 = S.Task('c_t5_t11', length=1, delay_cost=1)
	S += c_t5_t11 >= 38
	c_t5_t11 += ADD[1]

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=1, delay_cost=1)
	S += c_t5_t3_t2 >= 38
	c_t5_t3_t2 += ADD[0]

	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	S += c_t0_t00 >= 39
	c_t0_t00 += ADD[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 39
	c_t1_t01_mem0 += INPUT_mem_r

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 39
	c_t1_t01_mem1 += ADD_mem[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 39
	c_t2_t01_mem0 += INPUT_mem_r

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 39
	c_t2_t01_mem1 += ADD_mem[0]

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=1, delay_cost=1)
	S += c_t4_a1_1 >= 39
	c_t4_a1_1 += ADD[2]

	c_t4_t11 = S.Task('c_t4_t11', length=1, delay_cost=1)
	S += c_t4_t11 >= 39
	c_t4_t11 += ADD[1]

	c_t1_t01 = S.Task('c_t1_t01', length=1, delay_cost=1)
	S += c_t1_t01 >= 40
	c_t1_t01 += ADD[3]

	c_t2_t01 = S.Task('c_t2_t01', length=1, delay_cost=1)
	S += c_t2_t01 >= 40
	c_t2_t01 += ADD[0]


	# new tasks
	c_t0_t2_t0_in = S.Task('c_t0_t2_t0_in', length=1, delay_cost=1)
	c_t0_t2_t0_in += alt(MUL_in)
	c_t0_t2_t0 = S.Task('c_t0_t2_t0', length=7, delay_cost=1)
	c_t0_t2_t0 += alt(MUL)
	S += c_t0_t2_t0>=c_t0_t2_t0_in

	c_t0_t2_t0_mem0 = S.Task('c_t0_t2_t0_mem0', length=1, delay_cost=1)
	c_t0_t2_t0_mem0 += ADD_mem[3]
	S += 39 < c_t0_t2_t0_mem0
	S += c_t0_t2_t0_mem0 <= c_t0_t2_t0

	c_t0_t2_t0_mem1 = S.Task('c_t0_t2_t0_mem1', length=1, delay_cost=1)
	c_t0_t2_t0_mem1 += ADD_mem[3]
	S += 12 < c_t0_t2_t0_mem1
	S += c_t0_t2_t0_mem1 <= c_t0_t2_t0

	c_t0_t2_t1_in = S.Task('c_t0_t2_t1_in', length=1, delay_cost=1)
	c_t0_t2_t1_in += alt(MUL_in)
	c_t0_t2_t1 = S.Task('c_t0_t2_t1', length=7, delay_cost=1)
	c_t0_t2_t1 += alt(MUL)
	S += c_t0_t2_t1>=c_t0_t2_t1_in

	c_t0_t2_t1_mem0 = S.Task('c_t0_t2_t1_mem0', length=1, delay_cost=1)
	c_t0_t2_t1_mem0 += ADD_mem[2]
	S += 38 < c_t0_t2_t1_mem0
	S += c_t0_t2_t1_mem0 <= c_t0_t2_t1

	c_t0_t2_t1_mem1 = S.Task('c_t0_t2_t1_mem1', length=1, delay_cost=1)
	c_t0_t2_t1_mem1 += ADD_mem[0]
	S += 18 < c_t0_t2_t1_mem1
	S += c_t0_t2_t1_mem1 <= c_t0_t2_t1

	c_t0_t2_t2 = S.Task('c_t0_t2_t2', length=1, delay_cost=1)
	c_t0_t2_t2 += alt(ADD)

	c_t0_t2_t2_mem0 = S.Task('c_t0_t2_t2_mem0', length=1, delay_cost=1)
	c_t0_t2_t2_mem0 += ADD_mem[3]
	S += 39 < c_t0_t2_t2_mem0
	S += c_t0_t2_t2_mem0 <= c_t0_t2_t2

	c_t0_t2_t2_mem1 = S.Task('c_t0_t2_t2_mem1', length=1, delay_cost=1)
	c_t0_t2_t2_mem1 += ADD_mem[2]
	S += 38 < c_t0_t2_t2_mem1
	S += c_t0_t2_t2_mem1 <= c_t0_t2_t2

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	c_t0_t31 += alt(ADD)

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	c_t0_t31_mem0 += MUL_mem[0]
	S += 28 < c_t0_t31_mem0
	S += c_t0_t31_mem0 <= c_t0_t31

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	c_t0_t31_mem1 += ADD_mem[0]
	S += 13 < c_t0_t31_mem1
	S += c_t0_t31_mem1 <= c_t0_t31

	c_t010 = S.Task('c_t010', length=1, delay_cost=1)
	c_t010 += alt(ADD)

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	c_t010_mem0 += ADD_mem[1]
	S += 14 < c_t010_mem0
	S += c_t010_mem0 <= c_t010

	c_t1_t2_t0_in = S.Task('c_t1_t2_t0_in', length=1, delay_cost=1)
	c_t1_t2_t0_in += alt(MUL_in)
	c_t1_t2_t0 = S.Task('c_t1_t2_t0', length=7, delay_cost=1)
	c_t1_t2_t0 += alt(MUL)
	S += c_t1_t2_t0>=c_t1_t2_t0_in

	c_t1_t2_t0_mem0 = S.Task('c_t1_t2_t0_mem0', length=1, delay_cost=1)
	c_t1_t2_t0_mem0 += ADD_mem[0]
	S += 37 < c_t1_t2_t0_mem0
	S += c_t1_t2_t0_mem0 <= c_t1_t2_t0

	c_t1_t2_t0_mem1 = S.Task('c_t1_t2_t0_mem1', length=1, delay_cost=1)
	c_t1_t2_t0_mem1 += ADD_mem[3]
	S += 13 < c_t1_t2_t0_mem1
	S += c_t1_t2_t0_mem1 <= c_t1_t2_t0

	c_t1_t2_t1_in = S.Task('c_t1_t2_t1_in', length=1, delay_cost=1)
	c_t1_t2_t1_in += alt(MUL_in)
	c_t1_t2_t1 = S.Task('c_t1_t2_t1', length=7, delay_cost=1)
	c_t1_t2_t1 += alt(MUL)
	S += c_t1_t2_t1>=c_t1_t2_t1_in

	c_t1_t2_t1_mem0 = S.Task('c_t1_t2_t1_mem0', length=1, delay_cost=1)
	c_t1_t2_t1_mem0 += ADD_mem[3]
	S += 40 < c_t1_t2_t1_mem0
	S += c_t1_t2_t1_mem0 <= c_t1_t2_t1

	c_t1_t2_t1_mem1 = S.Task('c_t1_t2_t1_mem1', length=1, delay_cost=1)
	c_t1_t2_t1_mem1 += ADD_mem[0]
	S += 14 < c_t1_t2_t1_mem1
	S += c_t1_t2_t1_mem1 <= c_t1_t2_t1

	c_t1_t2_t2 = S.Task('c_t1_t2_t2', length=1, delay_cost=1)
	c_t1_t2_t2 += alt(ADD)

	c_t1_t2_t2_mem0 = S.Task('c_t1_t2_t2_mem0', length=1, delay_cost=1)
	c_t1_t2_t2_mem0 += ADD_mem[0]
	S += 37 < c_t1_t2_t2_mem0
	S += c_t1_t2_t2_mem0 <= c_t1_t2_t2

	c_t1_t2_t2_mem1 = S.Task('c_t1_t2_t2_mem1', length=1, delay_cost=1)
	c_t1_t2_t2_mem1 += ADD_mem[3]
	S += 40 < c_t1_t2_t2_mem1
	S += c_t1_t2_t2_mem1 <= c_t1_t2_t2

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	c_t1_t31 += alt(ADD)

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	c_t1_t31_mem0 += MUL_mem[0]
	S += 37 < c_t1_t31_mem0
	S += c_t1_t31_mem0 <= c_t1_t31

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	c_t1_t31_mem1 += ADD_mem[0]
	S += 12 < c_t1_t31_mem1
	S += c_t1_t31_mem1 <= c_t1_t31

	c_t110 = S.Task('c_t110', length=1, delay_cost=1)
	c_t110 += alt(ADD)

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	c_t110_mem0 += ADD_mem[2]
	S += 11 < c_t110_mem0
	S += c_t110_mem0 <= c_t110

	c_t2_t2_t0_in = S.Task('c_t2_t2_t0_in', length=1, delay_cost=1)
	c_t2_t2_t0_in += alt(MUL_in)
	c_t2_t2_t0 = S.Task('c_t2_t2_t0', length=7, delay_cost=1)
	c_t2_t2_t0 += alt(MUL)
	S += c_t2_t2_t0>=c_t2_t2_t0_in

	c_t2_t2_t0_mem0 = S.Task('c_t2_t2_t0_mem0', length=1, delay_cost=1)
	c_t2_t2_t0_mem0 += ADD_mem[3]
	S += 38 < c_t2_t2_t0_mem0
	S += c_t2_t2_t0_mem0 <= c_t2_t2_t0

	c_t2_t2_t0_mem1 = S.Task('c_t2_t2_t0_mem1', length=1, delay_cost=1)
	c_t2_t2_t0_mem1 += ADD_mem[1]
	S += 26 < c_t2_t2_t0_mem1
	S += c_t2_t2_t0_mem1 <= c_t2_t2_t0

	c_t2_t2_t1_in = S.Task('c_t2_t2_t1_in', length=1, delay_cost=1)
	c_t2_t2_t1_in += alt(MUL_in)
	c_t2_t2_t1 = S.Task('c_t2_t2_t1', length=7, delay_cost=1)
	c_t2_t2_t1 += alt(MUL)
	S += c_t2_t2_t1>=c_t2_t2_t1_in

	c_t2_t2_t1_mem0 = S.Task('c_t2_t2_t1_mem0', length=1, delay_cost=1)
	c_t2_t2_t1_mem0 += ADD_mem[0]
	S += 40 < c_t2_t2_t1_mem0
	S += c_t2_t2_t1_mem0 <= c_t2_t2_t1

	c_t2_t2_t1_mem1 = S.Task('c_t2_t2_t1_mem1', length=1, delay_cost=1)
	c_t2_t2_t1_mem1 += ADD_mem[3]
	S += 25 < c_t2_t2_t1_mem1
	S += c_t2_t2_t1_mem1 <= c_t2_t2_t1

	c_t2_t2_t2 = S.Task('c_t2_t2_t2', length=1, delay_cost=1)
	c_t2_t2_t2 += alt(ADD)

	c_t2_t2_t2_mem0 = S.Task('c_t2_t2_t2_mem0', length=1, delay_cost=1)
	c_t2_t2_t2_mem0 += ADD_mem[3]
	S += 38 < c_t2_t2_t2_mem0
	S += c_t2_t2_t2_mem0 <= c_t2_t2_t2

	c_t2_t2_t2_mem1 = S.Task('c_t2_t2_t2_mem1', length=1, delay_cost=1)
	c_t2_t2_t2_mem1 += ADD_mem[0]
	S += 40 < c_t2_t2_t2_mem1
	S += c_t2_t2_t2_mem1 <= c_t2_t2_t2

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	c_t2_t31 += alt(ADD)

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t31_mem0 += MUL_mem[0]
	S += 31 < c_t2_t31_mem0
	S += c_t2_t31_mem0 <= c_t2_t31

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t31_mem1 += ADD_mem[1]
	S += 9 < c_t2_t31_mem1
	S += c_t2_t31_mem1 <= c_t2_t31

	c_t210 = S.Task('c_t210', length=1, delay_cost=1)
	c_t210 += alt(ADD)

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	c_t210_mem0 += ADD_mem[0]
	S += 10 < c_t210_mem0
	S += c_t210_mem0 <= c_t210

	c_t3_t00 = S.Task('c_t3_t00', length=1, delay_cost=1)
	c_t3_t00 += alt(ADD)

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	c_t3_t00_mem0 += ADD_mem[3]
	S += 20 < c_t3_t00_mem0
	S += c_t3_t00_mem0 <= c_t3_t00

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	c_t3_t00_mem1 += ADD_mem[0]
	S += 24 < c_t3_t00_mem1
	S += c_t3_t00_mem1 <= c_t3_t00

	c_t3_t01 = S.Task('c_t3_t01', length=1, delay_cost=1)
	c_t3_t01 += alt(ADD)

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	c_t3_t01_mem0 += ADD_mem[3]
	S += 16 < c_t3_t01_mem0
	S += c_t3_t01_mem0 <= c_t3_t01

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	c_t3_t01_mem1 += ADD_mem[2]
	S += 25 < c_t3_t01_mem1
	S += c_t3_t01_mem1 <= c_t3_t01

	c_t3_t2_t3 = S.Task('c_t3_t2_t3', length=1, delay_cost=1)
	c_t3_t2_t3 += alt(ADD)

	c_t3_t2_t3_mem0 = S.Task('c_t3_t2_t3_mem0', length=1, delay_cost=1)
	c_t3_t2_t3_mem0 += ADD_mem[2]
	S += 23 < c_t3_t2_t3_mem0
	S += c_t3_t2_t3_mem0 <= c_t3_t2_t3

	c_t3_t2_t3_mem1 = S.Task('c_t3_t2_t3_mem1', length=1, delay_cost=1)
	c_t3_t2_t3_mem1 += ADD_mem[3]
	S += 18 < c_t3_t2_t3_mem1
	S += c_t3_t2_t3_mem1 <= c_t3_t2_t3

	c_t3_t3_t4_in = S.Task('c_t3_t3_t4_in', length=1, delay_cost=1)
	c_t3_t3_t4_in += alt(MUL_in)
	c_t3_t3_t4 = S.Task('c_t3_t3_t4', length=7, delay_cost=1)
	c_t3_t3_t4 += alt(MUL)
	S += c_t3_t3_t4>=c_t3_t3_t4_in

	c_t3_t3_t4_mem0 = S.Task('c_t3_t3_t4_mem0', length=1, delay_cost=1)
	c_t3_t3_t4_mem0 += ADD_mem[3]
	S += 21 < c_t3_t3_t4_mem0
	S += c_t3_t3_t4_mem0 <= c_t3_t3_t4

	c_t3_t3_t4_mem1 = S.Task('c_t3_t3_t4_mem1', length=1, delay_cost=1)
	c_t3_t3_t4_mem1 += ADD_mem[2]
	S += 24 < c_t3_t3_t4_mem1
	S += c_t3_t3_t4_mem1 <= c_t3_t3_t4

	c_t3_t30 = S.Task('c_t3_t30', length=1, delay_cost=1)
	c_t3_t30 += alt(ADD)

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	c_t3_t30_mem0 += MUL_mem[0]
	S += 29 < c_t3_t30_mem0
	S += c_t3_t30_mem0 <= c_t3_t30

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	c_t3_t30_mem1 += MUL_mem[0]
	S += 23 < c_t3_t30_mem1
	S += c_t3_t30_mem1 <= c_t3_t30

	c_t3_t3_t5 = S.Task('c_t3_t3_t5', length=1, delay_cost=1)
	c_t3_t3_t5 += alt(ADD)

	c_t3_t3_t5_mem0 = S.Task('c_t3_t3_t5_mem0', length=1, delay_cost=1)
	c_t3_t3_t5_mem0 += MUL_mem[0]
	S += 29 < c_t3_t3_t5_mem0
	S += c_t3_t3_t5_mem0 <= c_t3_t3_t5

	c_t3_t3_t5_mem1 = S.Task('c_t3_t3_t5_mem1', length=1, delay_cost=1)
	c_t3_t3_t5_mem1 += MUL_mem[0]
	S += 23 < c_t3_t3_t5_mem1
	S += c_t3_t3_t5_mem1 <= c_t3_t3_t5

	c_t4_t00 = S.Task('c_t4_t00', length=1, delay_cost=1)
	c_t4_t00 += alt(ADD)

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	c_t4_t00_mem0 += ADD_mem[3]
	S += 9 < c_t4_t00_mem0
	S += c_t4_t00_mem0 <= c_t4_t00

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	c_t4_t00_mem1 += ADD_mem[0]
	S += 36 < c_t4_t00_mem1
	S += c_t4_t00_mem1 <= c_t4_t00

	c_t4_t01 = S.Task('c_t4_t01', length=1, delay_cost=1)
	c_t4_t01 += alt(ADD)

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	c_t4_t01_mem0 += ADD_mem[1]
	S += 8 < c_t4_t01_mem0
	S += c_t4_t01_mem0 <= c_t4_t01

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	c_t4_t01_mem1 += ADD_mem[2]
	S += 39 < c_t4_t01_mem1
	S += c_t4_t01_mem1 <= c_t4_t01

	c_t4_t2_t3 = S.Task('c_t4_t2_t3', length=1, delay_cost=1)
	c_t4_t2_t3 += alt(ADD)

	c_t4_t2_t3_mem0 = S.Task('c_t4_t2_t3_mem0', length=1, delay_cost=1)
	c_t4_t2_t3_mem0 += ADD_mem[1]
	S += 32 < c_t4_t2_t3_mem0
	S += c_t4_t2_t3_mem0 <= c_t4_t2_t3

	c_t4_t2_t3_mem1 = S.Task('c_t4_t2_t3_mem1', length=1, delay_cost=1)
	c_t4_t2_t3_mem1 += ADD_mem[1]
	S += 39 < c_t4_t2_t3_mem1
	S += c_t4_t2_t3_mem1 <= c_t4_t2_t3

	c_t4_t3_t4_in = S.Task('c_t4_t3_t4_in', length=1, delay_cost=1)
	c_t4_t3_t4_in += alt(MUL_in)
	c_t4_t3_t4 = S.Task('c_t4_t3_t4', length=7, delay_cost=1)
	c_t4_t3_t4 += alt(MUL)
	S += c_t4_t3_t4>=c_t4_t3_t4_in

	c_t4_t3_t4_mem0 = S.Task('c_t4_t3_t4_mem0', length=1, delay_cost=1)
	c_t4_t3_t4_mem0 += ADD_mem[1]
	S += 10 < c_t4_t3_t4_mem0
	S += c_t4_t3_t4_mem0 <= c_t4_t3_t4

	c_t4_t3_t4_mem1 = S.Task('c_t4_t3_t4_mem1', length=1, delay_cost=1)
	c_t4_t3_t4_mem1 += ADD_mem[3]
	S += 37 < c_t4_t3_t4_mem1
	S += c_t4_t3_t4_mem1 <= c_t4_t3_t4

	c_t4_t30 = S.Task('c_t4_t30', length=1, delay_cost=1)
	c_t4_t30 += alt(ADD)

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	c_t4_t30_mem0 += MUL_mem[0]
	S += 38 < c_t4_t30_mem0
	S += c_t4_t30_mem0 <= c_t4_t30

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	c_t4_t30_mem1 += MUL_mem[0]
	S += 42 < c_t4_t30_mem1
	S += c_t4_t30_mem1 <= c_t4_t30

	c_t4_t3_t5 = S.Task('c_t4_t3_t5', length=1, delay_cost=1)
	c_t4_t3_t5 += alt(ADD)

	c_t4_t3_t5_mem0 = S.Task('c_t4_t3_t5_mem0', length=1, delay_cost=1)
	c_t4_t3_t5_mem0 += MUL_mem[0]
	S += 38 < c_t4_t3_t5_mem0
	S += c_t4_t3_t5_mem0 <= c_t4_t3_t5

	c_t4_t3_t5_mem1 = S.Task('c_t4_t3_t5_mem1', length=1, delay_cost=1)
	c_t4_t3_t5_mem1 += MUL_mem[0]
	S += 42 < c_t4_t3_t5_mem1
	S += c_t4_t3_t5_mem1 <= c_t4_t3_t5

	c_t5_t00 = S.Task('c_t5_t00', length=1, delay_cost=1)
	c_t5_t00 += alt(ADD)

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	c_t5_t00_mem0 += ADD_mem[0]
	S += 32 < c_t5_t00_mem0
	S += c_t5_t00_mem0 <= c_t5_t00

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	c_t5_t00_mem1 += ADD_mem[2]
	S += 36 < c_t5_t00_mem1
	S += c_t5_t00_mem1 <= c_t5_t00

	c_t5_t01 = S.Task('c_t5_t01', length=1, delay_cost=1)
	c_t5_t01 += alt(ADD)

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	c_t5_t01_mem0 += ADD_mem[3]
	S += 36 < c_t5_t01_mem0
	S += c_t5_t01_mem0 <= c_t5_t01

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	c_t5_t01_mem1 += ADD_mem[0]
	S += 35 < c_t5_t01_mem1
	S += c_t5_t01_mem1 <= c_t5_t01

	c_t5_t2_t3 = S.Task('c_t5_t2_t3', length=1, delay_cost=1)
	c_t5_t2_t3 += alt(ADD)

	c_t5_t2_t3_mem0 = S.Task('c_t5_t2_t3_mem0', length=1, delay_cost=1)
	c_t5_t2_t3_mem0 += ADD_mem[1]
	S += 36 < c_t5_t2_t3_mem0
	S += c_t5_t2_t3_mem0 <= c_t5_t2_t3

	c_t5_t2_t3_mem1 = S.Task('c_t5_t2_t3_mem1', length=1, delay_cost=1)
	c_t5_t2_t3_mem1 += ADD_mem[1]
	S += 38 < c_t5_t2_t3_mem1
	S += c_t5_t2_t3_mem1 <= c_t5_t2_t3

	c_t5_t3_t4_in = S.Task('c_t5_t3_t4_in', length=1, delay_cost=1)
	c_t5_t3_t4_in += alt(MUL_in)
	c_t5_t3_t4 = S.Task('c_t5_t3_t4', length=7, delay_cost=1)
	c_t5_t3_t4 += alt(MUL)
	S += c_t5_t3_t4>=c_t5_t3_t4_in

	c_t5_t3_t4_mem0 = S.Task('c_t5_t3_t4_mem0', length=1, delay_cost=1)
	c_t5_t3_t4_mem0 += ADD_mem[0]
	S += 38 < c_t5_t3_t4_mem0
	S += c_t5_t3_t4_mem0 <= c_t5_t3_t4

	c_t5_t3_t4_mem1 = S.Task('c_t5_t3_t4_mem1', length=1, delay_cost=1)
	c_t5_t3_t4_mem1 += ADD_mem[2]
	S += 37 < c_t5_t3_t4_mem1
	S += c_t5_t3_t4_mem1 <= c_t5_t3_t4

	c_t5_t30 = S.Task('c_t5_t30', length=1, delay_cost=1)
	c_t5_t30 += alt(ADD)

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	c_t5_t30_mem0 += MUL_mem[0]
	S += 41 < c_t5_t30_mem0
	S += c_t5_t30_mem0 <= c_t5_t30

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	c_t5_t30_mem1 += MUL_mem[0]
	S += 43 < c_t5_t30_mem1
	S += c_t5_t30_mem1 <= c_t5_t30

	c_t5_t3_t5 = S.Task('c_t5_t3_t5', length=1, delay_cost=1)
	c_t5_t3_t5 += alt(ADD)

	c_t5_t3_t5_mem0 = S.Task('c_t5_t3_t5_mem0', length=1, delay_cost=1)
	c_t5_t3_t5_mem0 += MUL_mem[0]
	S += 41 < c_t5_t3_t5_mem0
	S += c_t5_t3_t5_mem0 <= c_t5_t3_t5

	c_t5_t3_t5_mem1 = S.Task('c_t5_t3_t5_mem1', length=1, delay_cost=1)
	c_t5_t3_t5_mem1 += MUL_mem[0]
	S += 43 < c_t5_t3_t5_mem1
	S += c_t5_t3_t5_mem1 <= c_t5_t3_t5

	c_t0_t2_t4_in = S.Task('c_t0_t2_t4_in', length=1, delay_cost=1)
	c_t0_t2_t4_in += alt(MUL_in)
	c_t0_t2_t4 = S.Task('c_t0_t2_t4', length=7, delay_cost=1)
	c_t0_t2_t4 += alt(MUL)
	S += c_t0_t2_t4>=c_t0_t2_t4_in

	c_t0_t2_t4_mem0 = S.Task('c_t0_t2_t4_mem0', length=1, delay_cost=1)
	c_t0_t2_t4_mem0 += alt(ADD_mem)
	S += (c_t0_t2_t2*ADD[0]) < c_t0_t2_t4_mem0*ADD_mem[0]
	S += (c_t0_t2_t2*ADD[1]) < c_t0_t2_t4_mem0*ADD_mem[1]
	S += (c_t0_t2_t2*ADD[2]) < c_t0_t2_t4_mem0*ADD_mem[2]
	S += (c_t0_t2_t2*ADD[3]) < c_t0_t2_t4_mem0*ADD_mem[3]
	S += c_t0_t2_t4_mem0 <= c_t0_t2_t4

	c_t0_t2_t4_mem1 = S.Task('c_t0_t2_t4_mem1', length=1, delay_cost=1)
	c_t0_t2_t4_mem1 += ADD_mem[1]
	S += 19 < c_t0_t2_t4_mem1
	S += c_t0_t2_t4_mem1 <= c_t0_t2_t4

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	c_t0_t20 += alt(ADD)

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	c_t0_t20_mem0 += alt(MUL_mem)
	S += (c_t0_t2_t0*MUL[0]) < c_t0_t20_mem0*MUL_mem[0]
	S += c_t0_t20_mem0 <= c_t0_t20

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	c_t0_t20_mem1 += alt(MUL_mem)
	S += (c_t0_t2_t1*MUL[0]) < c_t0_t20_mem1*MUL_mem[0]
	S += c_t0_t20_mem1 <= c_t0_t20

	c_t0_t2_t5 = S.Task('c_t0_t2_t5', length=1, delay_cost=1)
	c_t0_t2_t5 += alt(ADD)

	c_t0_t2_t5_mem0 = S.Task('c_t0_t2_t5_mem0', length=1, delay_cost=1)
	c_t0_t2_t5_mem0 += alt(MUL_mem)
	S += (c_t0_t2_t0*MUL[0]) < c_t0_t2_t5_mem0*MUL_mem[0]
	S += c_t0_t2_t5_mem0 <= c_t0_t2_t5

	c_t0_t2_t5_mem1 = S.Task('c_t0_t2_t5_mem1', length=1, delay_cost=1)
	c_t0_t2_t5_mem1 += alt(MUL_mem)
	S += (c_t0_t2_t1*MUL[0]) < c_t0_t2_t5_mem1*MUL_mem[0]
	S += c_t0_t2_t5_mem1 <= c_t0_t2_t5

	c_t0_t40 = S.Task('c_t0_t40', length=1, delay_cost=1)
	c_t0_t40 += alt(ADD)

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	c_t0_t40_mem0 += ADD_mem[1]
	S += 14 < c_t0_t40_mem0
	S += c_t0_t40_mem0 <= c_t0_t40

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	c_t0_t40_mem1 += alt(ADD_mem)
	S += (c_t0_t31*ADD[0]) < c_t0_t40_mem1*ADD_mem[0]
	S += (c_t0_t31*ADD[1]) < c_t0_t40_mem1*ADD_mem[1]
	S += (c_t0_t31*ADD[2]) < c_t0_t40_mem1*ADD_mem[2]
	S += (c_t0_t31*ADD[3]) < c_t0_t40_mem1*ADD_mem[3]
	S += c_t0_t40_mem1 <= c_t0_t40

	c_t0_t41 = S.Task('c_t0_t41', length=1, delay_cost=1)
	c_t0_t41 += alt(ADD)

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	c_t0_t41_mem0 += alt(ADD_mem)
	S += (c_t0_t31*ADD[0]) < c_t0_t41_mem0*ADD_mem[0]
	S += (c_t0_t31*ADD[1]) < c_t0_t41_mem0*ADD_mem[1]
	S += (c_t0_t31*ADD[2]) < c_t0_t41_mem0*ADD_mem[2]
	S += (c_t0_t31*ADD[3]) < c_t0_t41_mem0*ADD_mem[3]
	S += c_t0_t41_mem0 <= c_t0_t41

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	c_t0_t41_mem1 += ADD_mem[1]
	S += 14 < c_t0_t41_mem1
	S += c_t0_t41_mem1 <= c_t0_t41

	c_t011 = S.Task('c_t011', length=1, delay_cost=1)
	c_t011 += alt(ADD)

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	c_t011_mem0 += alt(ADD_mem)
	S += (c_t0_t31*ADD[0]) < c_t011_mem0*ADD_mem[0]
	S += (c_t0_t31*ADD[1]) < c_t011_mem0*ADD_mem[1]
	S += (c_t0_t31*ADD[2]) < c_t011_mem0*ADD_mem[2]
	S += (c_t0_t31*ADD[3]) < c_t011_mem0*ADD_mem[3]
	S += c_t011_mem0 <= c_t011

	c_t1_t2_t4_in = S.Task('c_t1_t2_t4_in', length=1, delay_cost=1)
	c_t1_t2_t4_in += alt(MUL_in)
	c_t1_t2_t4 = S.Task('c_t1_t2_t4', length=7, delay_cost=1)
	c_t1_t2_t4 += alt(MUL)
	S += c_t1_t2_t4>=c_t1_t2_t4_in

	c_t1_t2_t4_mem0 = S.Task('c_t1_t2_t4_mem0', length=1, delay_cost=1)
	c_t1_t2_t4_mem0 += alt(ADD_mem)
	S += (c_t1_t2_t2*ADD[0]) < c_t1_t2_t4_mem0*ADD_mem[0]
	S += (c_t1_t2_t2*ADD[1]) < c_t1_t2_t4_mem0*ADD_mem[1]
	S += (c_t1_t2_t2*ADD[2]) < c_t1_t2_t4_mem0*ADD_mem[2]
	S += (c_t1_t2_t2*ADD[3]) < c_t1_t2_t4_mem0*ADD_mem[3]
	S += c_t1_t2_t4_mem0 <= c_t1_t2_t4

	c_t1_t2_t4_mem1 = S.Task('c_t1_t2_t4_mem1', length=1, delay_cost=1)
	c_t1_t2_t4_mem1 += ADD_mem[1]
	S += 15 < c_t1_t2_t4_mem1
	S += c_t1_t2_t4_mem1 <= c_t1_t2_t4

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	c_t1_t20 += alt(ADD)

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	c_t1_t20_mem0 += alt(MUL_mem)
	S += (c_t1_t2_t0*MUL[0]) < c_t1_t20_mem0*MUL_mem[0]
	S += c_t1_t20_mem0 <= c_t1_t20

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	c_t1_t20_mem1 += alt(MUL_mem)
	S += (c_t1_t2_t1*MUL[0]) < c_t1_t20_mem1*MUL_mem[0]
	S += c_t1_t20_mem1 <= c_t1_t20

	c_t1_t2_t5 = S.Task('c_t1_t2_t5', length=1, delay_cost=1)
	c_t1_t2_t5 += alt(ADD)

	c_t1_t2_t5_mem0 = S.Task('c_t1_t2_t5_mem0', length=1, delay_cost=1)
	c_t1_t2_t5_mem0 += alt(MUL_mem)
	S += (c_t1_t2_t0*MUL[0]) < c_t1_t2_t5_mem0*MUL_mem[0]
	S += c_t1_t2_t5_mem0 <= c_t1_t2_t5

	c_t1_t2_t5_mem1 = S.Task('c_t1_t2_t5_mem1', length=1, delay_cost=1)
	c_t1_t2_t5_mem1 += alt(MUL_mem)
	S += (c_t1_t2_t1*MUL[0]) < c_t1_t2_t5_mem1*MUL_mem[0]
	S += c_t1_t2_t5_mem1 <= c_t1_t2_t5

	c_t1_t40 = S.Task('c_t1_t40', length=1, delay_cost=1)
	c_t1_t40 += alt(ADD)

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	c_t1_t40_mem0 += ADD_mem[2]
	S += 11 < c_t1_t40_mem0
	S += c_t1_t40_mem0 <= c_t1_t40

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	c_t1_t40_mem1 += alt(ADD_mem)
	S += (c_t1_t31*ADD[0]) < c_t1_t40_mem1*ADD_mem[0]
	S += (c_t1_t31*ADD[1]) < c_t1_t40_mem1*ADD_mem[1]
	S += (c_t1_t31*ADD[2]) < c_t1_t40_mem1*ADD_mem[2]
	S += (c_t1_t31*ADD[3]) < c_t1_t40_mem1*ADD_mem[3]
	S += c_t1_t40_mem1 <= c_t1_t40

	c_t1_t41 = S.Task('c_t1_t41', length=1, delay_cost=1)
	c_t1_t41 += alt(ADD)

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	c_t1_t41_mem0 += alt(ADD_mem)
	S += (c_t1_t31*ADD[0]) < c_t1_t41_mem0*ADD_mem[0]
	S += (c_t1_t31*ADD[1]) < c_t1_t41_mem0*ADD_mem[1]
	S += (c_t1_t31*ADD[2]) < c_t1_t41_mem0*ADD_mem[2]
	S += (c_t1_t31*ADD[3]) < c_t1_t41_mem0*ADD_mem[3]
	S += c_t1_t41_mem0 <= c_t1_t41

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	c_t1_t41_mem1 += ADD_mem[2]
	S += 11 < c_t1_t41_mem1
	S += c_t1_t41_mem1 <= c_t1_t41

	c_t111 = S.Task('c_t111', length=1, delay_cost=1)
	c_t111 += alt(ADD)

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	c_t111_mem0 += alt(ADD_mem)
	S += (c_t1_t31*ADD[0]) < c_t111_mem0*ADD_mem[0]
	S += (c_t1_t31*ADD[1]) < c_t111_mem0*ADD_mem[1]
	S += (c_t1_t31*ADD[2]) < c_t111_mem0*ADD_mem[2]
	S += (c_t1_t31*ADD[3]) < c_t111_mem0*ADD_mem[3]
	S += c_t111_mem0 <= c_t111

	c_t2_t2_t4_in = S.Task('c_t2_t2_t4_in', length=1, delay_cost=1)
	c_t2_t2_t4_in += alt(MUL_in)
	c_t2_t2_t4 = S.Task('c_t2_t2_t4', length=7, delay_cost=1)
	c_t2_t2_t4 += alt(MUL)
	S += c_t2_t2_t4>=c_t2_t2_t4_in

	c_t2_t2_t4_mem0 = S.Task('c_t2_t2_t4_mem0', length=1, delay_cost=1)
	c_t2_t2_t4_mem0 += alt(ADD_mem)
	S += (c_t2_t2_t2*ADD[0]) < c_t2_t2_t4_mem0*ADD_mem[0]
	S += (c_t2_t2_t2*ADD[1]) < c_t2_t2_t4_mem0*ADD_mem[1]
	S += (c_t2_t2_t2*ADD[2]) < c_t2_t2_t4_mem0*ADD_mem[2]
	S += (c_t2_t2_t2*ADD[3]) < c_t2_t2_t4_mem0*ADD_mem[3]
	S += c_t2_t2_t4_mem0 <= c_t2_t2_t4

	c_t2_t2_t4_mem1 = S.Task('c_t2_t2_t4_mem1', length=1, delay_cost=1)
	c_t2_t2_t4_mem1 += ADD_mem[3]
	S += 27 < c_t2_t2_t4_mem1
	S += c_t2_t2_t4_mem1 <= c_t2_t2_t4

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	c_t2_t20 += alt(ADD)

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	c_t2_t20_mem0 += alt(MUL_mem)
	S += (c_t2_t2_t0*MUL[0]) < c_t2_t20_mem0*MUL_mem[0]
	S += c_t2_t20_mem0 <= c_t2_t20

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	c_t2_t20_mem1 += alt(MUL_mem)
	S += (c_t2_t2_t1*MUL[0]) < c_t2_t20_mem1*MUL_mem[0]
	S += c_t2_t20_mem1 <= c_t2_t20

	c_t2_t2_t5 = S.Task('c_t2_t2_t5', length=1, delay_cost=1)
	c_t2_t2_t5 += alt(ADD)

	c_t2_t2_t5_mem0 = S.Task('c_t2_t2_t5_mem0', length=1, delay_cost=1)
	c_t2_t2_t5_mem0 += alt(MUL_mem)
	S += (c_t2_t2_t0*MUL[0]) < c_t2_t2_t5_mem0*MUL_mem[0]
	S += c_t2_t2_t5_mem0 <= c_t2_t2_t5

	c_t2_t2_t5_mem1 = S.Task('c_t2_t2_t5_mem1', length=1, delay_cost=1)
	c_t2_t2_t5_mem1 += alt(MUL_mem)
	S += (c_t2_t2_t1*MUL[0]) < c_t2_t2_t5_mem1*MUL_mem[0]
	S += c_t2_t2_t5_mem1 <= c_t2_t2_t5

	c_t2_t40 = S.Task('c_t2_t40', length=1, delay_cost=1)
	c_t2_t40 += alt(ADD)

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	c_t2_t40_mem0 += ADD_mem[0]
	S += 10 < c_t2_t40_mem0
	S += c_t2_t40_mem0 <= c_t2_t40

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	c_t2_t40_mem1 += alt(ADD_mem)
	S += (c_t2_t31*ADD[0]) < c_t2_t40_mem1*ADD_mem[0]
	S += (c_t2_t31*ADD[1]) < c_t2_t40_mem1*ADD_mem[1]
	S += (c_t2_t31*ADD[2]) < c_t2_t40_mem1*ADD_mem[2]
	S += (c_t2_t31*ADD[3]) < c_t2_t40_mem1*ADD_mem[3]
	S += c_t2_t40_mem1 <= c_t2_t40

	c_t2_t41 = S.Task('c_t2_t41', length=1, delay_cost=1)
	c_t2_t41 += alt(ADD)

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	c_t2_t41_mem0 += alt(ADD_mem)
	S += (c_t2_t31*ADD[0]) < c_t2_t41_mem0*ADD_mem[0]
	S += (c_t2_t31*ADD[1]) < c_t2_t41_mem0*ADD_mem[1]
	S += (c_t2_t31*ADD[2]) < c_t2_t41_mem0*ADD_mem[2]
	S += (c_t2_t31*ADD[3]) < c_t2_t41_mem0*ADD_mem[3]
	S += c_t2_t41_mem0 <= c_t2_t41

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	c_t2_t41_mem1 += ADD_mem[0]
	S += 10 < c_t2_t41_mem1
	S += c_t2_t41_mem1 <= c_t2_t41

	c_t211 = S.Task('c_t211', length=1, delay_cost=1)
	c_t211 += alt(ADD)

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	c_t211_mem0 += alt(ADD_mem)
	S += (c_t2_t31*ADD[0]) < c_t211_mem0*ADD_mem[0]
	S += (c_t2_t31*ADD[1]) < c_t211_mem0*ADD_mem[1]
	S += (c_t2_t31*ADD[2]) < c_t211_mem0*ADD_mem[2]
	S += (c_t2_t31*ADD[3]) < c_t211_mem0*ADD_mem[3]
	S += c_t211_mem0 <= c_t211

	c_t3_t2_t0_in = S.Task('c_t3_t2_t0_in', length=1, delay_cost=1)
	c_t3_t2_t0_in += alt(MUL_in)
	c_t3_t2_t0 = S.Task('c_t3_t2_t0', length=7, delay_cost=1)
	c_t3_t2_t0 += alt(MUL)
	S += c_t3_t2_t0>=c_t3_t2_t0_in

	c_t3_t2_t0_mem0 = S.Task('c_t3_t2_t0_mem0', length=1, delay_cost=1)
	c_t3_t2_t0_mem0 += alt(ADD_mem)
	S += (c_t3_t00*ADD[0]) < c_t3_t2_t0_mem0*ADD_mem[0]
	S += (c_t3_t00*ADD[1]) < c_t3_t2_t0_mem0*ADD_mem[1]
	S += (c_t3_t00*ADD[2]) < c_t3_t2_t0_mem0*ADD_mem[2]
	S += (c_t3_t00*ADD[3]) < c_t3_t2_t0_mem0*ADD_mem[3]
	S += c_t3_t2_t0_mem0 <= c_t3_t2_t0

	c_t3_t2_t0_mem1 = S.Task('c_t3_t2_t0_mem1', length=1, delay_cost=1)
	c_t3_t2_t0_mem1 += ADD_mem[2]
	S += 23 < c_t3_t2_t0_mem1
	S += c_t3_t2_t0_mem1 <= c_t3_t2_t0

	c_t3_t2_t1_in = S.Task('c_t3_t2_t1_in', length=1, delay_cost=1)
	c_t3_t2_t1_in += alt(MUL_in)
	c_t3_t2_t1 = S.Task('c_t3_t2_t1', length=7, delay_cost=1)
	c_t3_t2_t1 += alt(MUL)
	S += c_t3_t2_t1>=c_t3_t2_t1_in

	c_t3_t2_t1_mem0 = S.Task('c_t3_t2_t1_mem0', length=1, delay_cost=1)
	c_t3_t2_t1_mem0 += alt(ADD_mem)
	S += (c_t3_t01*ADD[0]) < c_t3_t2_t1_mem0*ADD_mem[0]
	S += (c_t3_t01*ADD[1]) < c_t3_t2_t1_mem0*ADD_mem[1]
	S += (c_t3_t01*ADD[2]) < c_t3_t2_t1_mem0*ADD_mem[2]
	S += (c_t3_t01*ADD[3]) < c_t3_t2_t1_mem0*ADD_mem[3]
	S += c_t3_t2_t1_mem0 <= c_t3_t2_t1

	c_t3_t2_t1_mem1 = S.Task('c_t3_t2_t1_mem1', length=1, delay_cost=1)
	c_t3_t2_t1_mem1 += ADD_mem[3]
	S += 18 < c_t3_t2_t1_mem1
	S += c_t3_t2_t1_mem1 <= c_t3_t2_t1

	c_t3_t2_t2 = S.Task('c_t3_t2_t2', length=1, delay_cost=1)
	c_t3_t2_t2 += alt(ADD)

	c_t3_t2_t2_mem0 = S.Task('c_t3_t2_t2_mem0', length=1, delay_cost=1)
	c_t3_t2_t2_mem0 += alt(ADD_mem)
	S += (c_t3_t00*ADD[0]) < c_t3_t2_t2_mem0*ADD_mem[0]
	S += (c_t3_t00*ADD[1]) < c_t3_t2_t2_mem0*ADD_mem[1]
	S += (c_t3_t00*ADD[2]) < c_t3_t2_t2_mem0*ADD_mem[2]
	S += (c_t3_t00*ADD[3]) < c_t3_t2_t2_mem0*ADD_mem[3]
	S += c_t3_t2_t2_mem0 <= c_t3_t2_t2

	c_t3_t2_t2_mem1 = S.Task('c_t3_t2_t2_mem1', length=1, delay_cost=1)
	c_t3_t2_t2_mem1 += alt(ADD_mem)
	S += (c_t3_t01*ADD[0]) < c_t3_t2_t2_mem1*ADD_mem[0]
	S += (c_t3_t01*ADD[1]) < c_t3_t2_t2_mem1*ADD_mem[1]
	S += (c_t3_t01*ADD[2]) < c_t3_t2_t2_mem1*ADD_mem[2]
	S += (c_t3_t01*ADD[3]) < c_t3_t2_t2_mem1*ADD_mem[3]
	S += c_t3_t2_t2_mem1 <= c_t3_t2_t2

	c_t3_t31 = S.Task('c_t3_t31', length=1, delay_cost=1)
	c_t3_t31 += alt(ADD)

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	c_t3_t31_mem0 += alt(MUL_mem)
	S += (c_t3_t3_t4*MUL[0]) < c_t3_t31_mem0*MUL_mem[0]
	S += c_t3_t31_mem0 <= c_t3_t31

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	c_t3_t31_mem1 += alt(ADD_mem)
	S += (c_t3_t3_t5*ADD[0]) < c_t3_t31_mem1*ADD_mem[0]
	S += (c_t3_t3_t5*ADD[1]) < c_t3_t31_mem1*ADD_mem[1]
	S += (c_t3_t3_t5*ADD[2]) < c_t3_t31_mem1*ADD_mem[2]
	S += (c_t3_t3_t5*ADD[3]) < c_t3_t31_mem1*ADD_mem[3]
	S += c_t3_t31_mem1 <= c_t3_t31

	c_t310 = S.Task('c_t310', length=1, delay_cost=1)
	c_t310 += alt(ADD)

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	c_t310_mem0 += alt(ADD_mem)
	S += (c_t3_t30*ADD[0]) < c_t310_mem0*ADD_mem[0]
	S += (c_t3_t30*ADD[1]) < c_t310_mem0*ADD_mem[1]
	S += (c_t3_t30*ADD[2]) < c_t310_mem0*ADD_mem[2]
	S += (c_t3_t30*ADD[3]) < c_t310_mem0*ADD_mem[3]
	S += c_t310_mem0 <= c_t310

	c_t4_t2_t0_in = S.Task('c_t4_t2_t0_in', length=1, delay_cost=1)
	c_t4_t2_t0_in += alt(MUL_in)
	c_t4_t2_t0 = S.Task('c_t4_t2_t0', length=7, delay_cost=1)
	c_t4_t2_t0 += alt(MUL)
	S += c_t4_t2_t0>=c_t4_t2_t0_in

	c_t4_t2_t0_mem0 = S.Task('c_t4_t2_t0_mem0', length=1, delay_cost=1)
	c_t4_t2_t0_mem0 += alt(ADD_mem)
	S += (c_t4_t00*ADD[0]) < c_t4_t2_t0_mem0*ADD_mem[0]
	S += (c_t4_t00*ADD[1]) < c_t4_t2_t0_mem0*ADD_mem[1]
	S += (c_t4_t00*ADD[2]) < c_t4_t2_t0_mem0*ADD_mem[2]
	S += (c_t4_t00*ADD[3]) < c_t4_t2_t0_mem0*ADD_mem[3]
	S += c_t4_t2_t0_mem0 <= c_t4_t2_t0

	c_t4_t2_t0_mem1 = S.Task('c_t4_t2_t0_mem1', length=1, delay_cost=1)
	c_t4_t2_t0_mem1 += ADD_mem[1]
	S += 32 < c_t4_t2_t0_mem1
	S += c_t4_t2_t0_mem1 <= c_t4_t2_t0

	c_t4_t2_t1_in = S.Task('c_t4_t2_t1_in', length=1, delay_cost=1)
	c_t4_t2_t1_in += alt(MUL_in)
	c_t4_t2_t1 = S.Task('c_t4_t2_t1', length=7, delay_cost=1)
	c_t4_t2_t1 += alt(MUL)
	S += c_t4_t2_t1>=c_t4_t2_t1_in

	c_t4_t2_t1_mem0 = S.Task('c_t4_t2_t1_mem0', length=1, delay_cost=1)
	c_t4_t2_t1_mem0 += alt(ADD_mem)
	S += (c_t4_t01*ADD[0]) < c_t4_t2_t1_mem0*ADD_mem[0]
	S += (c_t4_t01*ADD[1]) < c_t4_t2_t1_mem0*ADD_mem[1]
	S += (c_t4_t01*ADD[2]) < c_t4_t2_t1_mem0*ADD_mem[2]
	S += (c_t4_t01*ADD[3]) < c_t4_t2_t1_mem0*ADD_mem[3]
	S += c_t4_t2_t1_mem0 <= c_t4_t2_t1

	c_t4_t2_t1_mem1 = S.Task('c_t4_t2_t1_mem1', length=1, delay_cost=1)
	c_t4_t2_t1_mem1 += ADD_mem[1]
	S += 39 < c_t4_t2_t1_mem1
	S += c_t4_t2_t1_mem1 <= c_t4_t2_t1

	c_t4_t2_t2 = S.Task('c_t4_t2_t2', length=1, delay_cost=1)
	c_t4_t2_t2 += alt(ADD)

	c_t4_t2_t2_mem0 = S.Task('c_t4_t2_t2_mem0', length=1, delay_cost=1)
	c_t4_t2_t2_mem0 += alt(ADD_mem)
	S += (c_t4_t00*ADD[0]) < c_t4_t2_t2_mem0*ADD_mem[0]
	S += (c_t4_t00*ADD[1]) < c_t4_t2_t2_mem0*ADD_mem[1]
	S += (c_t4_t00*ADD[2]) < c_t4_t2_t2_mem0*ADD_mem[2]
	S += (c_t4_t00*ADD[3]) < c_t4_t2_t2_mem0*ADD_mem[3]
	S += c_t4_t2_t2_mem0 <= c_t4_t2_t2

	c_t4_t2_t2_mem1 = S.Task('c_t4_t2_t2_mem1', length=1, delay_cost=1)
	c_t4_t2_t2_mem1 += alt(ADD_mem)
	S += (c_t4_t01*ADD[0]) < c_t4_t2_t2_mem1*ADD_mem[0]
	S += (c_t4_t01*ADD[1]) < c_t4_t2_t2_mem1*ADD_mem[1]
	S += (c_t4_t01*ADD[2]) < c_t4_t2_t2_mem1*ADD_mem[2]
	S += (c_t4_t01*ADD[3]) < c_t4_t2_t2_mem1*ADD_mem[3]
	S += c_t4_t2_t2_mem1 <= c_t4_t2_t2

	c_t4_t31 = S.Task('c_t4_t31', length=1, delay_cost=1)
	c_t4_t31 += alt(ADD)

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	c_t4_t31_mem0 += alt(MUL_mem)
	S += (c_t4_t3_t4*MUL[0]) < c_t4_t31_mem0*MUL_mem[0]
	S += c_t4_t31_mem0 <= c_t4_t31

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	c_t4_t31_mem1 += alt(ADD_mem)
	S += (c_t4_t3_t5*ADD[0]) < c_t4_t31_mem1*ADD_mem[0]
	S += (c_t4_t3_t5*ADD[1]) < c_t4_t31_mem1*ADD_mem[1]
	S += (c_t4_t3_t5*ADD[2]) < c_t4_t31_mem1*ADD_mem[2]
	S += (c_t4_t3_t5*ADD[3]) < c_t4_t31_mem1*ADD_mem[3]
	S += c_t4_t31_mem1 <= c_t4_t31

	c_t410 = S.Task('c_t410', length=1, delay_cost=1)
	c_t410 += alt(ADD)

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	c_t410_mem0 += alt(ADD_mem)
	S += (c_t4_t30*ADD[0]) < c_t410_mem0*ADD_mem[0]
	S += (c_t4_t30*ADD[1]) < c_t410_mem0*ADD_mem[1]
	S += (c_t4_t30*ADD[2]) < c_t410_mem0*ADD_mem[2]
	S += (c_t4_t30*ADD[3]) < c_t410_mem0*ADD_mem[3]
	S += c_t410_mem0 <= c_t410

	c_t5_t2_t0_in = S.Task('c_t5_t2_t0_in', length=1, delay_cost=1)
	c_t5_t2_t0_in += alt(MUL_in)
	c_t5_t2_t0 = S.Task('c_t5_t2_t0', length=7, delay_cost=1)
	c_t5_t2_t0 += alt(MUL)
	S += c_t5_t2_t0>=c_t5_t2_t0_in

	c_t5_t2_t0_mem0 = S.Task('c_t5_t2_t0_mem0', length=1, delay_cost=1)
	c_t5_t2_t0_mem0 += alt(ADD_mem)
	S += (c_t5_t00*ADD[0]) < c_t5_t2_t0_mem0*ADD_mem[0]
	S += (c_t5_t00*ADD[1]) < c_t5_t2_t0_mem0*ADD_mem[1]
	S += (c_t5_t00*ADD[2]) < c_t5_t2_t0_mem0*ADD_mem[2]
	S += (c_t5_t00*ADD[3]) < c_t5_t2_t0_mem0*ADD_mem[3]
	S += c_t5_t2_t0_mem0 <= c_t5_t2_t0

	c_t5_t2_t0_mem1 = S.Task('c_t5_t2_t0_mem1', length=1, delay_cost=1)
	c_t5_t2_t0_mem1 += ADD_mem[1]
	S += 36 < c_t5_t2_t0_mem1
	S += c_t5_t2_t0_mem1 <= c_t5_t2_t0

	c_t5_t2_t1_in = S.Task('c_t5_t2_t1_in', length=1, delay_cost=1)
	c_t5_t2_t1_in += alt(MUL_in)
	c_t5_t2_t1 = S.Task('c_t5_t2_t1', length=7, delay_cost=1)
	c_t5_t2_t1 += alt(MUL)
	S += c_t5_t2_t1>=c_t5_t2_t1_in

	c_t5_t2_t1_mem0 = S.Task('c_t5_t2_t1_mem0', length=1, delay_cost=1)
	c_t5_t2_t1_mem0 += alt(ADD_mem)
	S += (c_t5_t01*ADD[0]) < c_t5_t2_t1_mem0*ADD_mem[0]
	S += (c_t5_t01*ADD[1]) < c_t5_t2_t1_mem0*ADD_mem[1]
	S += (c_t5_t01*ADD[2]) < c_t5_t2_t1_mem0*ADD_mem[2]
	S += (c_t5_t01*ADD[3]) < c_t5_t2_t1_mem0*ADD_mem[3]
	S += c_t5_t2_t1_mem0 <= c_t5_t2_t1

	c_t5_t2_t1_mem1 = S.Task('c_t5_t2_t1_mem1', length=1, delay_cost=1)
	c_t5_t2_t1_mem1 += ADD_mem[1]
	S += 38 < c_t5_t2_t1_mem1
	S += c_t5_t2_t1_mem1 <= c_t5_t2_t1

	c_t5_t2_t2 = S.Task('c_t5_t2_t2', length=1, delay_cost=1)
	c_t5_t2_t2 += alt(ADD)

	c_t5_t2_t2_mem0 = S.Task('c_t5_t2_t2_mem0', length=1, delay_cost=1)
	c_t5_t2_t2_mem0 += alt(ADD_mem)
	S += (c_t5_t00*ADD[0]) < c_t5_t2_t2_mem0*ADD_mem[0]
	S += (c_t5_t00*ADD[1]) < c_t5_t2_t2_mem0*ADD_mem[1]
	S += (c_t5_t00*ADD[2]) < c_t5_t2_t2_mem0*ADD_mem[2]
	S += (c_t5_t00*ADD[3]) < c_t5_t2_t2_mem0*ADD_mem[3]
	S += c_t5_t2_t2_mem0 <= c_t5_t2_t2

	c_t5_t2_t2_mem1 = S.Task('c_t5_t2_t2_mem1', length=1, delay_cost=1)
	c_t5_t2_t2_mem1 += alt(ADD_mem)
	S += (c_t5_t01*ADD[0]) < c_t5_t2_t2_mem1*ADD_mem[0]
	S += (c_t5_t01*ADD[1]) < c_t5_t2_t2_mem1*ADD_mem[1]
	S += (c_t5_t01*ADD[2]) < c_t5_t2_t2_mem1*ADD_mem[2]
	S += (c_t5_t01*ADD[3]) < c_t5_t2_t2_mem1*ADD_mem[3]
	S += c_t5_t2_t2_mem1 <= c_t5_t2_t2

	c_t5_t31 = S.Task('c_t5_t31', length=1, delay_cost=1)
	c_t5_t31 += alt(ADD)

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	c_t5_t31_mem0 += alt(MUL_mem)
	S += (c_t5_t3_t4*MUL[0]) < c_t5_t31_mem0*MUL_mem[0]
	S += c_t5_t31_mem0 <= c_t5_t31

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	c_t5_t31_mem1 += alt(ADD_mem)
	S += (c_t5_t3_t5*ADD[0]) < c_t5_t31_mem1*ADD_mem[0]
	S += (c_t5_t3_t5*ADD[1]) < c_t5_t31_mem1*ADD_mem[1]
	S += (c_t5_t3_t5*ADD[2]) < c_t5_t31_mem1*ADD_mem[2]
	S += (c_t5_t3_t5*ADD[3]) < c_t5_t31_mem1*ADD_mem[3]
	S += c_t5_t31_mem1 <= c_t5_t31

	c_t510 = S.Task('c_t510', length=1, delay_cost=1)
	c_t510 += alt(ADD)

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	c_t510_mem0 += alt(ADD_mem)
	S += (c_t5_t30*ADD[0]) < c_t510_mem0*ADD_mem[0]
	S += (c_t5_t30*ADD[1]) < c_t510_mem0*ADD_mem[1]
	S += (c_t5_t30*ADD[2]) < c_t510_mem0*ADD_mem[2]
	S += (c_t5_t30*ADD[3]) < c_t510_mem0*ADD_mem[3]
	S += c_t510_mem0 <= c_t510

	c_s0010 = S.Task('c_s0010', length=1, delay_cost=1)
	c_s0010 += alt(ADD)

	c_s0010_mem0 = S.Task('c_s0010_mem0', length=1, delay_cost=1)
	c_s0010_mem0 += alt(ADD_mem)
	S += (c_t010*ADD[0]) < c_s0010_mem0*ADD_mem[0]
	S += (c_t010*ADD[1]) < c_s0010_mem0*ADD_mem[1]
	S += (c_t010*ADD[2]) < c_s0010_mem0*ADD_mem[2]
	S += (c_t010*ADD[3]) < c_s0010_mem0*ADD_mem[3]
	S += c_s0010_mem0 <= c_s0010

	c_s0010_mem1 = S.Task('c_s0010_mem1', length=1, delay_cost=1)
	c_s0010_mem1 += alt(ADD_mem)
	S += (c_t110*ADD[0]) < c_s0010_mem1*ADD_mem[0]
	S += (c_t110*ADD[1]) < c_s0010_mem1*ADD_mem[1]
	S += (c_t110*ADD[2]) < c_s0010_mem1*ADD_mem[2]
	S += (c_t110*ADD[3]) < c_s0010_mem1*ADD_mem[3]
	S += c_s0010_mem1 <= c_s0010

	c_s1010 = S.Task('c_s1010', length=1, delay_cost=1)
	c_s1010 += alt(ADD)

	c_s1010_mem0 = S.Task('c_s1010_mem0', length=1, delay_cost=1)
	c_s1010_mem0 += alt(ADD_mem)
	S += (c_t110*ADD[0]) < c_s1010_mem0*ADD_mem[0]
	S += (c_t110*ADD[1]) < c_s1010_mem0*ADD_mem[1]
	S += (c_t110*ADD[2]) < c_s1010_mem0*ADD_mem[2]
	S += (c_t110*ADD[3]) < c_s1010_mem0*ADD_mem[3]
	S += c_s1010_mem0 <= c_s1010

	c_s1010_mem1 = S.Task('c_s1010_mem1', length=1, delay_cost=1)
	c_s1010_mem1 += alt(ADD_mem)
	S += (c_t210*ADD[0]) < c_s1010_mem1*ADD_mem[0]
	S += (c_t210*ADD[1]) < c_s1010_mem1*ADD_mem[1]
	S += (c_t210*ADD[2]) < c_s1010_mem1*ADD_mem[2]
	S += (c_t210*ADD[3]) < c_s1010_mem1*ADD_mem[3]
	S += c_s1010_mem1 <= c_s1010

	c_s2010 = S.Task('c_s2010', length=1, delay_cost=1)
	c_s2010 += alt(ADD)

	c_s2010_mem0 = S.Task('c_s2010_mem0', length=1, delay_cost=1)
	c_s2010_mem0 += alt(ADD_mem)
	S += (c_t210*ADD[0]) < c_s2010_mem0*ADD_mem[0]
	S += (c_t210*ADD[1]) < c_s2010_mem0*ADD_mem[1]
	S += (c_t210*ADD[2]) < c_s2010_mem0*ADD_mem[2]
	S += (c_t210*ADD[3]) < c_s2010_mem0*ADD_mem[3]
	S += c_s2010_mem0 <= c_s2010

	c_s2010_mem1 = S.Task('c_s2010_mem1', length=1, delay_cost=1)
	c_s2010_mem1 += alt(ADD_mem)
	S += (c_t010*ADD[0]) < c_s2010_mem1*ADD_mem[0]
	S += (c_t010*ADD[1]) < c_s2010_mem1*ADD_mem[1]
	S += (c_t010*ADD[2]) < c_s2010_mem1*ADD_mem[2]
	S += (c_t010*ADD[3]) < c_s2010_mem1*ADD_mem[3]
	S += c_s2010_mem1 <= c_s2010

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-638/scheduling/SQR_mul1_add4/SQR_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

