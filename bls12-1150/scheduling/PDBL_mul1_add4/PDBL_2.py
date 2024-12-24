from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 137
	S = Scenario("PDBL_2", horizon=horizon)

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

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 8
	t100_mem0 += MUL_mem[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 8
	t100_mem1 += MUL_mem[0]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 8
	t2_t2 += ADD[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 8
	t5_t3_mem0 += INPUT_mem_r

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 8
	t5_t3_mem1 += INPUT_mem_r

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 9
	t100 += ADD[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 9
	t11_mem0 += MUL_mem[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 9
	t1_t5_mem0 += MUL_mem[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 9
	t5_t2_mem0 += INPUT_mem_r

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 9
	t5_t2_mem1 += INPUT_mem_r

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 9
	t5_t3 += ADD[0]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 10
	t10_t5_mem0 += MUL_mem[0]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 10
	t10_t5_mem1 += MUL_mem[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 10
	t11 += ADD[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 10
	t110_mem0 += ADD_mem[1]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 10
	t1_t5 += ADD[2]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 10
	t5_t2 += ADD[0]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 10
	t5_t4_in += MUL_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 10
	t5_t4_mem0 += ADD_mem[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 10
	t5_t4_mem1 += ADD_mem[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 10
	t7_t0_mem0 += INPUT_mem_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 10
	t7_t0_mem1 += INPUT_mem_r

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 11
	t10_t5 += ADD[2]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 11
	t110 += ADD[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 11
	t1_t1_mem0 += INPUT_mem_r

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 11
	t1_t1_mem1 += INPUT_mem_r

	t5_t4 = S.Task('t5_t4', length=7, delay_cost=1)
	S += t5_t4 >= 11
	t5_t4 += MUL[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 11
	t71_mem0 += MUL_mem[0]

	t7_t0 = S.Task('t7_t0', length=1, delay_cost=1)
	S += t7_t0 >= 11
	t7_t0 += ADD[1]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 11
	t7_t5_mem0 += MUL_mem[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 12
	t10_t2_mem0 += INPUT_mem_r

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 12
	t10_t2_mem1 += INPUT_mem_r

	t1_t1 = S.Task('t1_t1', length=1, delay_cost=1)
	S += t1_t1 >= 12
	t1_t1 += ADD[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 12
	t50_mem0 += MUL_mem[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 12
	t50_mem1 += MUL_mem[0]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 12
	t71 += ADD[2]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 12
	t7_t5 += ADD[3]

	t10_t2 = S.Task('t10_t2', length=1, delay_cost=1)
	S += t10_t2 >= 13
	t10_t2 += ADD[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 13
	t1_t0_mem0 += INPUT_mem_r

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 13
	t1_t0_mem1 += INPUT_mem_r

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 13
	t50 += ADD[2]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 13
	t81_mem0 += ADD_mem[2]

	t1_t0 = S.Task('t1_t0', length=1, delay_cost=1)
	S += t1_t0 >= 14
	t1_t0 += ADD[2]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 14
	t1_t2_in += MUL_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 14
	t1_t2_mem0 += ADD_mem[2]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 14
	t1_t2_mem1 += ADD_mem[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 14
	t5_t5_mem0 += MUL_mem[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 14
	t5_t5_mem1 += MUL_mem[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 14
	t60_mem0 += ADD_mem[2]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 14
	t7_t1_mem0 += INPUT_mem_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 14
	t7_t1_mem1 += INPUT_mem_r

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 14
	t81 += ADD[0]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 15
	t10_t3_mem0 += INPUT_mem_r

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 15
	t10_t3_mem1 += INPUT_mem_r

	t1_t2 = S.Task('t1_t2', length=7, delay_cost=1)
	S += t1_t2 >= 15
	t1_t2 += MUL[0]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 15
	t5_t5 += ADD[1]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 15
	t60 += ADD[3]

	t7_t1 = S.Task('t7_t1', length=1, delay_cost=1)
	S += t7_t1 >= 15
	t7_t1 += ADD[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 15
	t7_t2_in += MUL_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 15
	t7_t2_mem0 += ADD_mem[1]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 15
	t7_t2_mem1 += ADD_mem[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 15
	t91_mem0 += ADD_mem[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 15
	t91_mem1 += ADD_mem[2]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 16
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 16
	t0_t0_mem1 += INPUT_mem_r

	t10_t3 = S.Task('t10_t3', length=1, delay_cost=1)
	S += t10_t3 >= 16
	t10_t3 += ADD[2]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 16
	t10_t4_in += MUL_in[0]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 16
	t10_t4_mem0 += ADD_mem[0]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 16
	t10_t4_mem1 += ADD_mem[2]

	t7_t2 = S.Task('t7_t2', length=7, delay_cost=1)
	S += t7_t2 >= 16
	t7_t2 += MUL[0]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 16
	t91 += ADD[1]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 17
	t0_t0 += ADD[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 17
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 17
	t0_t1_mem1 += INPUT_mem_r

	t10_t4 = S.Task('t10_t4', length=7, delay_cost=1)
	S += t10_t4 >= 17
	t10_t4 += MUL[0]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 18
	t0_t1 += ADD[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 18
	t0_t2_in += MUL_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 18
	t0_t2_mem0 += ADD_mem[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 18
	t0_t2_mem1 += ADD_mem[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 18
	t51_mem0 += MUL_mem[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 18
	t51_mem1 += ADD_mem[1]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 19
	c201_in += MUL_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 19
	c201_mem0 += ADD_mem[1]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 19
	c201_mem1 += INPUT_mem_r

	t0_t2 = S.Task('t0_t2', length=7, delay_cost=1)
	S += t0_t2 >= 19
	t0_t2 += MUL[0]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 19
	t51 += ADD[2]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 20
	c010_in += MUL_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 20
	c010_mem0 += ADD_mem[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 20
	c010_mem1 += INPUT_mem_r

	c201 = S.Task('c201', length=7, delay_cost=1)
	S += c201 >= 20
	c201 += MUL[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 20
	t61_mem0 += ADD_mem[2]

	c010 = S.Task('c010', length=7, delay_cost=1)
	S += c010 >= 21
	c010 += MUL[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 21
	t2_t1_in += MUL_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 21
	t2_t1_mem0 += INPUT_mem_r

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 21
	t2_t1_mem1 += ADD_mem[1]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 21
	t61 += ADD[2]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 22
	new_TX_t3_mem0 += ADD_mem[3]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 22
	new_TX_t3_mem1 += ADD_mem[2]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 22
	t10_mem0 += MUL_mem[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 22
	t10_mem1 += ADD_mem[2]

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 22
	t2_t1 += MUL[0]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 23
	new_TX_t3 += ADD[1]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 23
	t10 += ADD[3]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 23
	t70_mem0 += MUL_mem[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 23
	t70_mem1 += ADD_mem[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 24
	t101_mem0 += MUL_mem[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 24
	t101_mem1 += ADD_mem[2]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 24
	t2_t0_in += MUL_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 24
	t2_t0_mem0 += INPUT_mem_r

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 24
	t2_t0_mem1 += ADD_mem[3]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 24
	t2_t3_mem0 += ADD_mem[3]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 24
	t2_t3_mem1 += ADD_mem[1]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 24
	t70 += ADD[1]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 25
	t101 += ADD[2]

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 25
	t2_t0 += MUL[0]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 25
	t2_t3 += ADD[3]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 25
	t80_mem0 += ADD_mem[1]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 26
	t111_mem0 += ADD_mem[2]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 26
	t2_t4_in += MUL_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 26
	t2_t4_mem0 += ADD_mem[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 26
	t2_t4_mem1 += ADD_mem[3]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 26
	t80 += ADD[2]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 27
	c201_w += INPUT_mem_w

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 27
	t111 += ADD[2]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 27
	t2_t4 += MUL[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 27
	t90_mem0 += ADD_mem[2]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 27
	t90_mem1 += ADD_mem[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 28
	c010_w += INPUT_mem_w

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 28
	t12_t3_mem0 += ADD_mem[0]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 28
	t12_t3_mem1 += ADD_mem[2]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 28
	t18_t1_mem0 += ADD_mem[3]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 28
	t18_t1_mem1 += ADD_mem[1]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 28
	t90 += ADD[1]

	t12_t3 = S.Task('t12_t3', length=1, delay_cost=1)
	S += t12_t3 >= 29
	t12_t3 += ADD[0]

	t18_t1 = S.Task('t18_t1', length=1, delay_cost=1)
	S += t18_t1 >= 29
	t18_t1 += ADD[3]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 30
	c011_in += MUL_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 30
	c011_mem0 += ADD_mem[2]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 30
	c011_mem1 += INPUT_mem_r

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 30
	t18_t0_mem0 += ADD_mem[3]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 30
	t18_t0_mem1 += ADD_mem[1]

	c011 = S.Task('c011', length=7, delay_cost=1)
	S += c011 >= 31
	c011 += MUL[0]

	t18_t0 = S.Task('t18_t0', length=1, delay_cost=1)
	S += t18_t0 >= 31
	t18_t0 += ADD[1]

	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	S += t12_t4_in >= 32
	t12_t4_in += MUL_in[0]

	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	S += t12_t4_mem0 >= 32
	t12_t4_mem0 += ADD_mem[3]

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	S += t12_t4_mem1 >= 32
	t12_t4_mem1 += ADD_mem[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 32
	t20_mem0 += MUL_mem[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 32
	t20_mem1 += MUL_mem[0]

	t12_t4 = S.Task('t12_t4', length=7, delay_cost=1)
	S += t12_t4 >= 33
	t12_t4 += MUL[0]

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 33
	t18_t2_in += MUL_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 33
	t18_t2_mem0 += ADD_mem[1]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 33
	t18_t2_mem1 += ADD_mem[3]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 33
	t20 += ADD[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 33
	t2_t5_mem0 += MUL_mem[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 33
	t2_t5_mem1 += MUL_mem[0]

	t18_t2 = S.Task('t18_t2', length=7, delay_cost=1)
	S += t18_t2 >= 34
	t18_t2 += MUL[0]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 34
	t2_t5 += ADD[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 34
	t30_mem0 += ADD_mem[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 35
	t21_mem0 += MUL_mem[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 35
	t21_mem1 += ADD_mem[3]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 35
	t30 += ADD[2]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 36
	t21 += ADD[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 36
	t40_mem0 += ADD_mem[2]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 36
	t40_mem1 += ADD_mem[1]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 37
	t120_mem0 += MUL_mem[0]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 37
	t120_mem1 += MUL_mem[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 37
	t31_mem0 += ADD_mem[0]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 37
	t40 += ADD[1]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 38
	c011_w += INPUT_mem_w

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 38
	t120 += ADD[3]

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	S += t12_t5_mem0 >= 38
	t12_t5_mem0 += MUL_mem[0]

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	S += t12_t5_mem1 >= 38
	t12_t5_mem1 += MUL_mem[0]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 38
	t140_mem0 += ADD_mem[1]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 38
	t31 += ADD[0]

	t12_t5 = S.Task('t12_t5', length=1, delay_cost=1)
	S += t12_t5 >= 39
	t12_t5 += ADD[1]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 39
	t130_mem0 += ADD_mem[3]

	t140 = S.Task('t140', length=1, delay_cost=1)
	S += t140 >= 39
	t140 += ADD[0]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 39
	t181_mem0 += MUL_mem[0]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 39
	t18_t5_mem0 += MUL_mem[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 39
	t41_mem0 += ADD_mem[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 39
	t41_mem1 += ADD_mem[0]

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	S += b30_mem0 >= 40
	b30_mem0 += ADD_mem[0]

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	S += b30_mem1 >= 40
	b30_mem1 += ADD_mem[1]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 40
	t121_mem0 += MUL_mem[0]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 40
	t121_mem1 += ADD_mem[1]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 40
	t130 += ADD[1]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 40
	t150_mem0 += ADD_mem[2]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 40
	t150_mem1 += ADD_mem[0]

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 40
	t181 += ADD[3]

	t18_t5 = S.Task('t18_t5', length=1, delay_cost=1)
	S += t18_t5 >= 40
	t18_t5 += ADD[2]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 40
	t41 += ADD[0]

	b30 = S.Task('b30', length=1, delay_cost=1)
	S += b30 >= 41
	b30 += ADD[2]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 41
	new_TZ0_mem0 += ADD_mem[1]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 41
	t121 += ADD[1]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 41
	t141_mem0 += ADD_mem[0]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 41
	t150 += ADD[3]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 41
	t180_mem0 += MUL_mem[0]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 41
	t180_mem1 += ADD_mem[2]

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	S += new_TZ0 >= 42
	new_TZ0 += ADD[1]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 42
	t131_mem0 += ADD_mem[1]

	t141 = S.Task('t141', length=1, delay_cost=1)
	S += t141 >= 42
	t141 += ADD[0]

	t180 = S.Task('t180', length=1, delay_cost=1)
	S += t180 >= 42
	t180 += ADD[2]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 43
	new_TZ0_w += INPUT_mem_w

	t131 = S.Task('t131', length=1, delay_cost=1)
	S += t131 >= 43
	t131 += ADD[3]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 44
	new_TZ1_mem0 += ADD_mem[3]

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	S += new_TZ1 >= 45
	new_TZ1 += ADD[3]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 46
	new_TZ1_w += INPUT_mem_w


	# new tasks
	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(ADD)

	S += t0_t5<1000

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MUL_mem[0]
	S += 13 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(ADD)

	S += t01<29

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MUL_mem[0]
	S += 13 < t01_mem0
	S += t01_mem0 <= t01

	t00 = S.Task('t00', length=1, delay_cost=1)
	t00 += alt(ADD)

	S += t00<29

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += MUL_mem[0]
	S += 25 < t00_mem0
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += alt(ADD_mem)
	S += (t0_t5*ADD[0]) < t00_mem1*ADD_mem[0]
	S += (t0_t5*ADD[1]) < t00_mem1*ADD_mem[1]
	S += (t0_t5*ADD[2]) < t00_mem1*ADD_mem[2]
	S += (t0_t5*ADD[3]) < t00_mem1*ADD_mem[3]
	S += t00_mem1 <= t00

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	t12_t0_in += alt(MUL_in)
	t12_t0 = S.Task('t12_t0', length=7, delay_cost=1)
	t12_t0 += alt(MUL)
	S += t12_t0>=t12_t0_in

	S += t12_t0<38

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	t12_t0_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < t12_t0_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < t12_t0_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < t12_t0_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < t12_t0_mem0*ADD_mem[3]
	S += t12_t0_mem0 <= t12_t0

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	t12_t0_mem1 += ADD_mem[0]
	S += 11 < t12_t0_mem1
	S += t12_t0_mem1 <= t12_t0

	t12_t2 = S.Task('t12_t2', length=1, delay_cost=1)
	t12_t2 += alt(ADD)

	S += t12_t2<33

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

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	t18_t3_in += alt(MUL_in)
	t18_t3 = S.Task('t18_t3', length=7, delay_cost=1)
	t18_t3 += alt(MUL)
	S += t18_t3>=t18_t3_in

	S += t18_t3<40

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

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	t12_t1_in += alt(MUL_in)
	t12_t1 = S.Task('t12_t1', length=7, delay_cost=1)
	t12_t1 += alt(MUL)
	S += t12_t1>=t12_t1_in

	S += t12_t1<38

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	t12_t1_mem0 += alt(ADD_mem)
	S += (t01*ADD[0]) < t12_t1_mem0*ADD_mem[0]
	S += (t01*ADD[1]) < t12_t1_mem0*ADD_mem[1]
	S += (t01*ADD[2]) < t12_t1_mem0*ADD_mem[2]
	S += (t01*ADD[3]) < t12_t1_mem0*ADD_mem[3]
	S += t12_t1_mem0 <= t12_t1

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	t12_t1_mem1 += ADD_mem[2]
	S += 27 < t12_t1_mem1
	S += t12_t1_mem1 <= t12_t1

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MUL_in)
	c200 = S.Task('c200', length=7, delay_cost=1)
	c200 += alt(MUL)
	S += c200>=c200_in

	S += 0<c200

	S += c200<1000

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += ADD_mem[1]
	S += 28 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += INPUT_mem_r
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200 <= c200_w

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(ADD)

	S += 0<c000

	S += c000<41

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(ADD_mem)
	S += (t00*ADD[0]) < c000_mem0*ADD_mem[0]
	S += (t00*ADD[1]) < c000_mem0*ADD_mem[1]
	S += (t00*ADD[2]) < c000_mem0*ADD_mem[2]
	S += (t00*ADD[3]) < c000_mem0*ADD_mem[3]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += ADD_mem[1]
	S += 37 < c000_mem1
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(INPUT_mem_w)
	S += c000 <= c000_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(ADD)

	S += 0<c001

	S += c001<1000

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(ADD_mem)
	S += (t01*ADD[0]) < c001_mem0*ADD_mem[0]
	S += (t01*ADD[1]) < c001_mem0*ADD_mem[1]
	S += (t01*ADD[2]) < c001_mem0*ADD_mem[2]
	S += (t01*ADD[3]) < c001_mem0*ADD_mem[3]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += ADD_mem[0]
	S += 40 < c001_mem1
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(INPUT_mem_w)
	S += c001 <= c001_w

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(ADD)

	S += t160<1000

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

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(ADD)

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(ADD_mem)
	S += (c001*ADD[0]) < t151_mem0*ADD_mem[0]
	S += (c001*ADD[1]) < t151_mem0*ADD_mem[1]
	S += (c001*ADD[2]) < t151_mem0*ADD_mem[2]
	S += (c001*ADD[3]) < t151_mem0*ADD_mem[3]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += ADD_mem[0]
	S += 42 < t151_mem1
	S += t151_mem1 <= t151

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MUL_in)
	new_TX_t0 = S.Task('new_TX_t0', length=7, delay_cost=1)
	new_TX_t0 += alt(MUL)
	S += new_TX_t0>=new_TX_t0_in

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += ADD_mem[3]
	S += 41 < new_TX_t0_mem0
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += ADD_mem[3]
	S += 15 < new_TX_t0_mem1
	S += new_TX_t0_mem1 <= new_TX_t0

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(ADD)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += alt(ADD_mem)
	S += (t01*ADD[0]) < t161_mem0*ADD_mem[0]
	S += (t01*ADD[1]) < t161_mem0*ADD_mem[1]
	S += (t01*ADD[2]) < t161_mem0*ADD_mem[2]
	S += (t01*ADD[3]) < t161_mem0*ADD_mem[3]
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += alt(ADD_mem)
	S += (c001*ADD[0]) < t161_mem1*ADD_mem[0]
	S += (c001*ADD[1]) < t161_mem1*ADD_mem[1]
	S += (c001*ADD[2]) < t161_mem1*ADD_mem[2]
	S += (c001*ADD[3]) < t161_mem1*ADD_mem[3]
	S += t161_mem1 <= t161

	b31 = S.Task('b31', length=1, delay_cost=1)
	b31 += alt(ADD)

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	b31_mem0 += ADD_mem[0]
	S += 42 < b31_mem0
	S += b31_mem0 <= b31

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	b31_mem1 += ADD_mem[0]
	S += 40 < b31_mem1
	S += b31_mem1 <= b31

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	t17_t0_in += alt(MUL_in)
	t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
	t17_t0 += alt(MUL)
	S += t17_t0>=t17_t0_in

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	t17_t0_mem0 += ADD_mem[2]
	S += 41 < t17_t0_mem0
	S += t17_t0_mem0 <= t17_t0

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	t17_t0_mem1 += alt(ADD_mem)
	S += (t160*ADD[0]) < t17_t0_mem1*ADD_mem[0]
	S += (t160*ADD[1]) < t17_t0_mem1*ADD_mem[1]
	S += (t160*ADD[2]) < t17_t0_mem1*ADD_mem[2]
	S += (t160*ADD[3]) < t17_t0_mem1*ADD_mem[3]
	S += t17_t0_mem1 <= t17_t0

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MUL_in)
	new_TX_t1 = S.Task('new_TX_t1', length=7, delay_cost=1)
	new_TX_t1 += alt(MUL)
	S += new_TX_t1>=new_TX_t1_in

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += alt(ADD_mem)
	S += (t151*ADD[0]) < new_TX_t1_mem0*ADD_mem[0]
	S += (t151*ADD[1]) < new_TX_t1_mem0*ADD_mem[1]
	S += (t151*ADD[2]) < new_TX_t1_mem0*ADD_mem[2]
	S += (t151*ADD[3]) < new_TX_t1_mem0*ADD_mem[3]
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += ADD_mem[2]
	S += 21 < new_TX_t1_mem1
	S += new_TX_t1_mem1 <= new_TX_t1

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	new_TX_t2 += alt(ADD)

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	new_TX_t2_mem0 += ADD_mem[3]
	S += 41 < new_TX_t2_mem0
	S += new_TX_t2_mem0 <= new_TX_t2

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	new_TX_t2_mem1 += alt(ADD_mem)
	S += (t151*ADD[0]) < new_TX_t2_mem1*ADD_mem[0]
	S += (t151*ADD[1]) < new_TX_t2_mem1*ADD_mem[1]
	S += (t151*ADD[2]) < new_TX_t2_mem1*ADD_mem[2]
	S += (t151*ADD[3]) < new_TX_t2_mem1*ADD_mem[3]
	S += new_TX_t2_mem1 <= new_TX_t2

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	t17_t1_in += alt(MUL_in)
	t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
	t17_t1 += alt(MUL)
	S += t17_t1>=t17_t1_in

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	t17_t1_mem0 += alt(ADD_mem)
	S += (b31*ADD[0]) < t17_t1_mem0*ADD_mem[0]
	S += (b31*ADD[1]) < t17_t1_mem0*ADD_mem[1]
	S += (b31*ADD[2]) < t17_t1_mem0*ADD_mem[2]
	S += (b31*ADD[3]) < t17_t1_mem0*ADD_mem[3]
	S += t17_t1_mem0 <= t17_t1

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	t17_t1_mem1 += alt(ADD_mem)
	S += (t161*ADD[0]) < t17_t1_mem1*ADD_mem[0]
	S += (t161*ADD[1]) < t17_t1_mem1*ADD_mem[1]
	S += (t161*ADD[2]) < t17_t1_mem1*ADD_mem[2]
	S += (t161*ADD[3]) < t17_t1_mem1*ADD_mem[3]
	S += t17_t1_mem1 <= t17_t1

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	t17_t2 += alt(ADD)

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	t17_t2_mem0 += ADD_mem[2]
	S += 41 < t17_t2_mem0
	S += t17_t2_mem0 <= t17_t2

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	t17_t2_mem1 += alt(ADD_mem)
	S += (b31*ADD[0]) < t17_t2_mem1*ADD_mem[0]
	S += (b31*ADD[1]) < t17_t2_mem1*ADD_mem[1]
	S += (b31*ADD[2]) < t17_t2_mem1*ADD_mem[2]
	S += (b31*ADD[3]) < t17_t2_mem1*ADD_mem[3]
	S += t17_t2_mem1 <= t17_t2

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	t17_t3 += alt(ADD)

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	t17_t3_mem0 += alt(ADD_mem)
	S += (t160*ADD[0]) < t17_t3_mem0*ADD_mem[0]
	S += (t160*ADD[1]) < t17_t3_mem0*ADD_mem[1]
	S += (t160*ADD[2]) < t17_t3_mem0*ADD_mem[2]
	S += (t160*ADD[3]) < t17_t3_mem0*ADD_mem[3]
	S += t17_t3_mem0 <= t17_t3

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	t17_t3_mem1 += alt(ADD_mem)
	S += (t161*ADD[0]) < t17_t3_mem1*ADD_mem[0]
	S += (t161*ADD[1]) < t17_t3_mem1*ADD_mem[1]
	S += (t161*ADD[2]) < t17_t3_mem1*ADD_mem[2]
	S += (t161*ADD[3]) < t17_t3_mem1*ADD_mem[3]
	S += t17_t3_mem1 <= t17_t3

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MUL_in)
	new_TX_t4 = S.Task('new_TX_t4', length=7, delay_cost=1)
	new_TX_t4 += alt(MUL)
	S += new_TX_t4>=new_TX_t4_in

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += alt(ADD_mem)
	S += (new_TX_t2*ADD[0]) < new_TX_t4_mem0*ADD_mem[0]
	S += (new_TX_t2*ADD[1]) < new_TX_t4_mem0*ADD_mem[1]
	S += (new_TX_t2*ADD[2]) < new_TX_t4_mem0*ADD_mem[2]
	S += (new_TX_t2*ADD[3]) < new_TX_t4_mem0*ADD_mem[3]
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += ADD_mem[1]
	S += 23 < new_TX_t4_mem1
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	new_TX0 += alt(ADD)

	S += 15<new_TX0

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

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	t17_t4_in += alt(MUL_in)
	t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
	t17_t4 += alt(MUL)
	S += t17_t4>=t17_t4_in

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	t17_t4_mem0 += alt(ADD_mem)
	S += (t17_t2*ADD[0]) < t17_t4_mem0*ADD_mem[0]
	S += (t17_t2*ADD[1]) < t17_t4_mem0*ADD_mem[1]
	S += (t17_t2*ADD[2]) < t17_t4_mem0*ADD_mem[2]
	S += (t17_t2*ADD[3]) < t17_t4_mem0*ADD_mem[3]
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

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	new_TX1 += alt(ADD)

	S += 15<new_TX1

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

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	new_TY0 += alt(ADD)

	S += 18<new_TY0

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += alt(ADD_mem)
	S += (t170*ADD[0]) < new_TY0_mem0*ADD_mem[0]
	S += (t170*ADD[1]) < new_TY0_mem0*ADD_mem[1]
	S += (t170*ADD[2]) < new_TY0_mem0*ADD_mem[2]
	S += (t170*ADD[3]) < new_TY0_mem0*ADD_mem[3]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += ADD_mem[2]
	S += 42 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(INPUT_mem_w)
	S += new_TY0 <= new_TY0_w

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	new_TY1 += alt(ADD)

	S += 18<new_TY1

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += alt(ADD_mem)
	S += (t171*ADD[0]) < new_TY1_mem0*ADD_mem[0]
	S += (t171*ADD[1]) < new_TY1_mem0*ADD_mem[1]
	S += (t171*ADD[2]) < new_TY1_mem0*ADD_mem[2]
	S += (t171*ADD[3]) < new_TY1_mem0*ADD_mem[3]
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += ADD_mem[3]
	S += 40 < new_TY1_mem1
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

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-1150/scheduling/PDBL_mul1_add4/PDBL_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

