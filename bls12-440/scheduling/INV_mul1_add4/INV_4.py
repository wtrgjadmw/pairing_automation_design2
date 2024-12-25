from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 166
	S = Scenario("INV_4", horizon=horizon)

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
	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 0
	c_cc_t3_t1_in += MUL_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 0
	c_cc_t3_t1_mem0 += INPUT_mem_r

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 0
	c_cc_t3_t1_mem1 += INPUT_mem_r

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 1
	c_cc_t3_t0_in += MUL_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 1
	c_cc_t3_t0_mem0 += INPUT_mem_r

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 1
	c_cc_t3_t0_mem1 += INPUT_mem_r

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=7, delay_cost=1)
	S += c_cc_t3_t1 >= 1
	c_cc_t3_t1 += MUL[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 2
	c_ab_t0_t1_in += MUL_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 2
	c_ab_t0_t1_mem0 += INPUT_mem_r

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 2
	c_ab_t0_t1_mem1 += INPUT_mem_r

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=7, delay_cost=1)
	S += c_cc_t3_t0 >= 2
	c_cc_t3_t0 += MUL[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=7, delay_cost=1)
	S += c_ab_t0_t1 >= 3
	c_ab_t0_t1 += MUL[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 3
	c_ab_t1_t1_in += MUL_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 3
	c_ab_t1_t1_mem0 += INPUT_mem_r

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 3
	c_ab_t1_t1_mem1 += INPUT_mem_r

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 4
	c_ab_t1_t0_in += MUL_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 4
	c_ab_t1_t0_mem0 += INPUT_mem_r

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 4
	c_ab_t1_t0_mem1 += INPUT_mem_r

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=7, delay_cost=1)
	S += c_ab_t1_t1 >= 4
	c_ab_t1_t1 += MUL[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=7, delay_cost=1)
	S += c_ab_t1_t0 >= 5
	c_ab_t1_t0 += MUL[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 5
	c_bb_t3_t0_in += MUL_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 5
	c_bb_t3_t0_mem0 += INPUT_mem_r

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 5
	c_bb_t3_t0_mem1 += INPUT_mem_r

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=7, delay_cost=1)
	S += c_bb_t3_t0 >= 6
	c_bb_t3_t0 += MUL[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 6
	c_bb_t3_t1_in += MUL_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 6
	c_bb_t3_t1_mem0 += INPUT_mem_r

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 6
	c_bb_t3_t1_mem1 += INPUT_mem_r

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 7
	c_ab_t0_t0_in += MUL_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 7
	c_ab_t0_t0_mem0 += INPUT_mem_r

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 7
	c_ab_t0_t0_mem1 += INPUT_mem_r

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=7, delay_cost=1)
	S += c_bb_t3_t1 >= 7
	c_bb_t3_t1 += MUL[0]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 8
	c_aa_t3_t1_in += MUL_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 8
	c_aa_t3_t1_mem0 += INPUT_mem_r

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 8
	c_aa_t3_t1_mem1 += INPUT_mem_r

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=7, delay_cost=1)
	S += c_ab_t0_t0 >= 8
	c_ab_t0_t0 += MUL[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 9
	c_aa_t3_t0_in += MUL_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 9
	c_aa_t3_t0_mem0 += INPUT_mem_r

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 9
	c_aa_t3_t0_mem1 += INPUT_mem_r

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=7, delay_cost=1)
	S += c_aa_t3_t1 >= 9
	c_aa_t3_t1 += MUL[0]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 9
	c_cc_t3_t5_mem0 += MUL_mem[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 9
	c_cc_t3_t5_mem1 += MUL_mem[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=7, delay_cost=1)
	S += c_aa_t3_t0 >= 10
	c_aa_t3_t0 += MUL[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 10
	c_ab_t0_t2_mem0 += INPUT_mem_r

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 10
	c_ab_t0_t2_mem1 += INPUT_mem_r

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 10
	c_cc_t30_mem0 += MUL_mem[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 10
	c_cc_t30_mem1 += MUL_mem[0]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=1, delay_cost=1)
	S += c_cc_t3_t5 >= 10
	c_cc_t3_t5 += ADD[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 11
	c_ab_t0_t2 += ADD[3]

	c_cc_t30 = S.Task('c_cc_t30', length=1, delay_cost=1)
	S += c_cc_t30 >= 11
	c_cc_t30 += ADD[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 11
	c_cc_t3_t3_mem0 += INPUT_mem_r

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 11
	c_cc_t3_t3_mem1 += INPUT_mem_r

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 12
	c_aa_t3_t3_mem0 += INPUT_mem_r

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 12
	c_aa_t3_t3_mem1 += INPUT_mem_r

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 12
	c_ab_t10_mem0 += MUL_mem[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 12
	c_ab_t10_mem1 += MUL_mem[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 12
	c_cc_t3_t3 += ADD[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 13
	c_aa_t3_t3 += ADD[1]

	c_ab_t10 = S.Task('c_ab_t10', length=1, delay_cost=1)
	S += c_ab_t10 >= 13
	c_ab_t10 += ADD[2]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 13
	c_ab_t1_t5_mem0 += MUL_mem[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 13
	c_ab_t1_t5_mem1 += MUL_mem[0]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 13
	c_cc_t3_t2_mem0 += INPUT_mem_r

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 13
	c_cc_t3_t2_mem1 += INPUT_mem_r

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 14
	c_aa_a1_0_mem0 += INPUT_mem_r

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 14
	c_aa_a1_0_mem1 += INPUT_mem_r

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=1, delay_cost=1)
	S += c_ab_t1_t5 >= 14
	c_ab_t1_t5 += ADD[1]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 14
	c_bb_t3_t5_mem0 += MUL_mem[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 14
	c_bb_t3_t5_mem1 += MUL_mem[0]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 14
	c_cc_t3_t2 += ADD[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 15
	c_aa_a1_0 += ADD[2]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 15
	c_ab_t00_mem0 += MUL_mem[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 15
	c_ab_t00_mem1 += MUL_mem[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 15
	c_bb_a1_0_mem0 += INPUT_mem_r

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 15
	c_bb_a1_0_mem1 += INPUT_mem_r

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=1, delay_cost=1)
	S += c_bb_t3_t5 >= 15
	c_bb_t3_t5 += ADD[0]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 15
	c_cc_t3_t4_in += MUL_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 15
	c_cc_t3_t4_mem0 += ADD_mem[0]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 15
	c_cc_t3_t4_mem1 += ADD_mem[0]

	c_ab_t00 = S.Task('c_ab_t00', length=1, delay_cost=1)
	S += c_ab_t00 >= 16
	c_ab_t00 += ADD[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 16
	c_ab_t0_t3_mem0 += INPUT_mem_r

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 16
	c_ab_t0_t3_mem1 += INPUT_mem_r

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 16
	c_bb_a1_0 += ADD[0]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 16
	c_bb_t30_mem0 += MUL_mem[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 16
	c_bb_t30_mem1 += MUL_mem[0]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=7, delay_cost=1)
	S += c_cc_t3_t4 >= 16
	c_cc_t3_t4 += MUL[0]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 17
	c_aa_t30_mem0 += MUL_mem[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 17
	c_aa_t30_mem1 += MUL_mem[0]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 17
	c_ab_t0_t3 += ADD[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 17
	c_bb_a1_1_mem0 += INPUT_mem_r

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 17
	c_bb_a1_1_mem1 += INPUT_mem_r

	c_bb_t30 = S.Task('c_bb_t30', length=1, delay_cost=1)
	S += c_bb_t30 >= 17
	c_bb_t30 += ADD[1]

	c_aa_t30 = S.Task('c_aa_t30', length=1, delay_cost=1)
	S += c_aa_t30 >= 18
	c_aa_t30 += ADD[2]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 18
	c_aa_t3_t5_mem0 += MUL_mem[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 18
	c_aa_t3_t5_mem1 += MUL_mem[0]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 18
	c_ab_t0_t4_in += MUL_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 18
	c_ab_t0_t4_mem0 += ADD_mem[3]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 18
	c_ab_t0_t4_mem1 += ADD_mem[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 18
	c_bb_a1_1 += ADD[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 18
	c_cc_t10_mem0 += INPUT_mem_r

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 18
	c_cc_t10_mem1 += INPUT_mem_r

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=1, delay_cost=1)
	S += c_aa_t3_t5 >= 19
	c_aa_t3_t5 += ADD[2]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=7, delay_cost=1)
	S += c_ab_t0_t4 >= 19
	c_ab_t0_t4 += MUL[0]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 19
	c_ab_t0_t5_mem0 += MUL_mem[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 19
	c_ab_t0_t5_mem1 += MUL_mem[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 19
	c_cc_a1_1_mem0 += INPUT_mem_r

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 19
	c_cc_a1_1_mem1 += INPUT_mem_r

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 19
	c_cc_t10 += ADD[0]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=1, delay_cost=1)
	S += c_ab_t0_t5 >= 20
	c_ab_t0_t5 += ADD[2]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 20
	c_cc_a1_1 += ADD[3]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 20
	c_cc_t11_mem0 += INPUT_mem_r

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 20
	c_cc_t11_mem1 += INPUT_mem_r

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 21
	c_aa_t11_mem0 += INPUT_mem_r

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 21
	c_aa_t11_mem1 += INPUT_mem_r

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 21
	c_cc_t11 += ADD[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 22
	c_aa_t10_mem0 += INPUT_mem_r

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 22
	c_aa_t10_mem1 += INPUT_mem_r

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 22
	c_aa_t11 += ADD[0]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 22
	c_cc_t2_t3_mem0 += ADD_mem[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 22
	c_cc_t2_t3_mem1 += ADD_mem[0]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 23
	c_aa_t10 += ADD[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 23
	c_cc_a1_0_mem0 += INPUT_mem_r

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 23
	c_cc_a1_0_mem1 += INPUT_mem_r

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=1, delay_cost=1)
	S += c_cc_t2_t3 >= 23
	c_cc_t2_t3 += ADD[1]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 24
	c_aa_t2_t3_mem0 += ADD_mem[0]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 24
	c_aa_t2_t3_mem1 += ADD_mem[0]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 24
	c_aa_t3_t2_mem0 += INPUT_mem_r

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 24
	c_aa_t3_t2_mem1 += INPUT_mem_r

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 24
	c_cc_a1_0 += ADD[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 25
	c_aa_a1_1_mem0 += INPUT_mem_r

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 25
	c_aa_a1_1_mem1 += INPUT_mem_r

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=1, delay_cost=1)
	S += c_aa_t2_t3 >= 25
	c_aa_t2_t3 += ADD[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 25
	c_aa_t3_t2 += ADD[2]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 26
	c_aa_a1_1 += ADD[1]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 26
	c_aa_t3_t4_in += MUL_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 26
	c_aa_t3_t4_mem0 += ADD_mem[2]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 26
	c_aa_t3_t4_mem1 += ADD_mem[1]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 26
	c_bb_t3_t3_mem0 += INPUT_mem_r

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 26
	c_bb_t3_t3_mem1 += INPUT_mem_r

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=7, delay_cost=1)
	S += c_aa_t3_t4 >= 27
	c_aa_t3_t4 += MUL[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 27
	c_bb_t3_t2_mem0 += INPUT_mem_r

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 27
	c_bb_t3_t2_mem1 += INPUT_mem_r

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 27
	c_bb_t3_t3 += ADD[0]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 28
	c_bb_t11_mem0 += INPUT_mem_r

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 28
	c_bb_t11_mem1 += INPUT_mem_r

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 28
	c_bb_t3_t2 += ADD[2]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 29
	c_bb_t10_mem0 += INPUT_mem_r

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 29
	c_bb_t10_mem1 += INPUT_mem_r

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 29
	c_bb_t11 += ADD[2]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 29
	c_bb_t3_t4_in += MUL_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 29
	c_bb_t3_t4_mem0 += ADD_mem[2]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 29
	c_bb_t3_t4_mem1 += ADD_mem[0]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 30
	c_bb_t10 += ADD[2]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=7, delay_cost=1)
	S += c_bb_t3_t4 >= 30
	c_bb_t3_t4 += MUL[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 30
	c_bc_t0_t1_in += MUL_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 30
	c_bc_t0_t1_mem0 += INPUT_mem_r

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 30
	c_bc_t0_t1_mem1 += INPUT_mem_r

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 31
	c_bb_t2_t3_mem0 += ADD_mem[2]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 31
	c_bb_t2_t3_mem1 += ADD_mem[2]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=7, delay_cost=1)
	S += c_bc_t0_t1 >= 31
	c_bc_t0_t1 += MUL[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 31
	c_bc_t1_t0_in += MUL_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 31
	c_bc_t1_t0_mem0 += INPUT_mem_r

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 31
	c_bc_t1_t0_mem1 += INPUT_mem_r

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=1, delay_cost=1)
	S += c_bb_t2_t3 >= 32
	c_bb_t2_t3 += ADD[0]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=7, delay_cost=1)
	S += c_bc_t1_t0 >= 32
	c_bc_t1_t0 += MUL[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 32
	c_bc_t1_t1_in += MUL_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 32
	c_bc_t1_t1_mem0 += INPUT_mem_r

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 32
	c_bc_t1_t1_mem1 += INPUT_mem_r

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 33
	c_bc_t0_t0_in += MUL_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 33
	c_bc_t0_t0_mem0 += INPUT_mem_r

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 33
	c_bc_t0_t0_mem1 += INPUT_mem_r

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=7, delay_cost=1)
	S += c_bc_t1_t1 >= 33
	c_bc_t1_t1 += MUL[0]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 34
	c_ac_t1_t1_in += MUL_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 34
	c_ac_t1_t1_mem0 += INPUT_mem_r

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 34
	c_ac_t1_t1_mem1 += INPUT_mem_r

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=7, delay_cost=1)
	S += c_bc_t0_t0 >= 34
	c_bc_t0_t0 += MUL[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 35
	c_ac_t1_t0_in += MUL_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 35
	c_ac_t1_t0_mem0 += INPUT_mem_r

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 35
	c_ac_t1_t0_mem1 += INPUT_mem_r

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=7, delay_cost=1)
	S += c_ac_t1_t1 >= 35
	c_ac_t1_t1 += MUL[0]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 36
	c_ac_t0_t1_in += MUL_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 36
	c_ac_t0_t1_mem0 += INPUT_mem_r

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 36
	c_ac_t0_t1_mem1 += INPUT_mem_r

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=7, delay_cost=1)
	S += c_ac_t1_t0 >= 36
	c_ac_t1_t0 += MUL[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 37
	c_ac_t0_t0_in += MUL_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 37
	c_ac_t0_t0_mem0 += INPUT_mem_r

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 37
	c_ac_t0_t0_mem1 += INPUT_mem_r

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=7, delay_cost=1)
	S += c_ac_t0_t1 >= 37
	c_ac_t0_t1 += MUL[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 38
	c_ab_t31_mem0 += INPUT_mem_r

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 38
	c_ab_t31_mem1 += INPUT_mem_r

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=7, delay_cost=1)
	S += c_ac_t0_t0 >= 38
	c_ac_t0_t0 += MUL[0]

	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	S += c_ab_t31 >= 39
	c_ab_t31 += ADD[2]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 39
	c_ac_t31_mem0 += INPUT_mem_r

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 39
	c_ac_t31_mem1 += INPUT_mem_r

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 40
	c_ab_t1_t3_mem0 += INPUT_mem_r

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 40
	c_ab_t1_t3_mem1 += INPUT_mem_r

	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	S += c_ac_t31 >= 40
	c_ac_t31 += ADD[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 40
	c_bc_t10_mem0 += MUL_mem[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 40
	c_bc_t10_mem1 += MUL_mem[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 41
	c_ab_t1_t3 += ADD[3]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 41
	c_bc_t00_mem0 += MUL_mem[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 41
	c_bc_t00_mem1 += MUL_mem[0]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 41
	c_bc_t0_t2_mem0 += INPUT_mem_r

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 41
	c_bc_t0_t2_mem1 += INPUT_mem_r

	c_bc_t10 = S.Task('c_bc_t10', length=1, delay_cost=1)
	S += c_bc_t10 >= 41
	c_bc_t10 += ADD[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 42
	c_ac_t21_mem0 += INPUT_mem_r

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 42
	c_ac_t21_mem1 += INPUT_mem_r

	c_bc_t00 = S.Task('c_bc_t00', length=1, delay_cost=1)
	S += c_bc_t00 >= 42
	c_bc_t00 += ADD[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 42
	c_bc_t0_t2 += ADD[2]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 42
	c_bc_t0_t5_mem0 += MUL_mem[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 42
	c_bc_t0_t5_mem1 += MUL_mem[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 43
	c_ac_t10_mem0 += MUL_mem[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 43
	c_ac_t10_mem1 += MUL_mem[0]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 43
	c_ac_t1_t3_mem0 += INPUT_mem_r

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 43
	c_ac_t1_t3_mem1 += INPUT_mem_r

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 43
	c_ac_t21 += ADD[0]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=1, delay_cost=1)
	S += c_bc_t0_t5 >= 43
	c_bc_t0_t5 += ADD[1]

	c_ac_t10 = S.Task('c_ac_t10', length=1, delay_cost=1)
	S += c_ac_t10 >= 44
	c_ac_t10 += ADD[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 44
	c_ac_t1_t3 += ADD[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 44
	c_ac_t1_t5_mem0 += MUL_mem[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 44
	c_ac_t1_t5_mem1 += MUL_mem[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 44
	c_ac_t30_mem0 += INPUT_mem_r

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 44
	c_ac_t30_mem1 += INPUT_mem_r

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 44
	c_ac_t4_t1_in += MUL_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 44
	c_ac_t4_t1_mem0 += ADD_mem[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 44
	c_ac_t4_t1_mem1 += ADD_mem[0]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 45
	c_ac_t0_t3_mem0 += INPUT_mem_r

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 45
	c_ac_t0_t3_mem1 += INPUT_mem_r

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 45
	c_ac_t0_t5_mem0 += MUL_mem[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 45
	c_ac_t0_t5_mem1 += MUL_mem[0]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=1, delay_cost=1)
	S += c_ac_t1_t5 >= 45
	c_ac_t1_t5 += ADD[2]

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 45
	c_ac_t30 += ADD[0]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=7, delay_cost=1)
	S += c_ac_t4_t1 >= 45
	c_ac_t4_t1 += MUL[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 46
	c_ab_t21_mem0 += INPUT_mem_r

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 46
	c_ab_t21_mem1 += INPUT_mem_r

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 46
	c_ac_t00_mem0 += MUL_mem[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 46
	c_ac_t00_mem1 += MUL_mem[0]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 46
	c_ac_t0_t3 += ADD[0]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=1, delay_cost=1)
	S += c_ac_t0_t5 >= 46
	c_ac_t0_t5 += ADD[1]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 46
	c_ac_t4_t3_mem0 += ADD_mem[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 46
	c_ac_t4_t3_mem1 += ADD_mem[0]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 47
	c_ab_t21 += ADD[1]

	c_ac_t00 = S.Task('c_ac_t00', length=1, delay_cost=1)
	S += c_ac_t00 >= 47
	c_ac_t00 += ADD[3]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=1, delay_cost=1)
	S += c_ac_t4_t3 >= 47
	c_ac_t4_t3 += ADD[0]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 47
	c_bc_t1_t5_mem0 += MUL_mem[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 47
	c_bc_t1_t5_mem1 += MUL_mem[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 47
	c_bc_t31_mem0 += INPUT_mem_r

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 47
	c_bc_t31_mem1 += INPUT_mem_r

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 48
	c_ab_t4_t1_in += MUL_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 48
	c_ab_t4_t1_mem0 += ADD_mem[1]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 48
	c_ab_t4_t1_mem1 += ADD_mem[2]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 48
	c_ac_t1_t2_mem0 += INPUT_mem_r

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 48
	c_ac_t1_t2_mem1 += INPUT_mem_r

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=1, delay_cost=1)
	S += c_bc_t1_t5 >= 48
	c_bc_t1_t5 += ADD[1]

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 48
	c_bc_t31 += ADD[0]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=7, delay_cost=1)
	S += c_ab_t4_t1 >= 49
	c_ab_t4_t1 += MUL[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	S += c_ac_t1_t2 >= 49
	c_ac_t1_t2 += ADD[3]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 49
	c_ac_t20_mem0 += INPUT_mem_r

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 49
	c_ac_t20_mem1 += INPUT_mem_r

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 50
	c_ac_t1_t4_in += MUL_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 50
	c_ac_t1_t4_mem0 += ADD_mem[3]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 50
	c_ac_t1_t4_mem1 += ADD_mem[0]

	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	S += c_ac_t20 >= 50
	c_ac_t20 += ADD[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 50
	c_bc_t30_mem0 += INPUT_mem_r

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 50
	c_bc_t30_mem1 += INPUT_mem_r

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 51
	c_ab_t20_mem0 += INPUT_mem_r

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 51
	c_ab_t20_mem1 += INPUT_mem_r

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=7, delay_cost=1)
	S += c_ac_t1_t4 >= 51
	c_ac_t1_t4 += MUL[0]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 51
	c_ac_t4_t0_in += MUL_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 51
	c_ac_t4_t0_mem0 += ADD_mem[0]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 51
	c_ac_t4_t0_mem1 += ADD_mem[0]

	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	S += c_bc_t30 >= 51
	c_bc_t30 += ADD[1]

	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	S += c_ab_t20 >= 52
	c_ab_t20 += ADD[3]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 52
	c_ab_t30_mem0 += INPUT_mem_r

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 52
	c_ab_t30_mem1 += INPUT_mem_r

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=7, delay_cost=1)
	S += c_ac_t4_t0 >= 52
	c_ac_t4_t0 += MUL[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 52
	c_ac_t4_t2_mem0 += ADD_mem[0]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 52
	c_ac_t4_t2_mem1 += ADD_mem[0]

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 53
	c_ab_t30 += ADD[2]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 53
	c_ab_t4_t2_mem0 += ADD_mem[3]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 53
	c_ab_t4_t2_mem1 += ADD_mem[1]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 53
	c_ac_t0_t2_mem0 += INPUT_mem_r

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 53
	c_ac_t0_t2_mem1 += INPUT_mem_r

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=1, delay_cost=1)
	S += c_ac_t4_t2 >= 53
	c_ac_t4_t2 += ADD[1]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 53
	c_bc_t4_t3_mem0 += ADD_mem[1]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 53
	c_bc_t4_t3_mem1 += ADD_mem[0]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 54
	c_ab_t4_t0_in += MUL_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 54
	c_ab_t4_t0_mem0 += ADD_mem[3]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 54
	c_ab_t4_t0_mem1 += ADD_mem[2]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=1, delay_cost=1)
	S += c_ab_t4_t2 >= 54
	c_ab_t4_t2 += ADD[2]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 54
	c_ac_t0_t2 += ADD[3]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 54
	c_bc_t21_mem0 += INPUT_mem_r

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 54
	c_bc_t21_mem1 += INPUT_mem_r

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=1, delay_cost=1)
	S += c_bc_t4_t3 >= 54
	c_bc_t4_t3 += ADD[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 55
	c_ab_t1_t2_mem0 += INPUT_mem_r

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 55
	c_ab_t1_t2_mem1 += INPUT_mem_r

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=7, delay_cost=1)
	S += c_ab_t4_t0 >= 55
	c_ab_t4_t0 += MUL[0]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 55
	c_ab_t4_t3_mem0 += ADD_mem[2]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 55
	c_ab_t4_t3_mem1 += ADD_mem[2]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 55
	c_ac_t0_t4_in += MUL_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 55
	c_ac_t0_t4_mem0 += ADD_mem[3]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 55
	c_ac_t0_t4_mem1 += ADD_mem[0]

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 55
	c_bc_t21 += ADD[3]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 56
	c_ab_t1_t2 += ADD[0]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=1, delay_cost=1)
	S += c_ab_t4_t3 >= 56
	c_ab_t4_t3 += ADD[2]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=7, delay_cost=1)
	S += c_ac_t0_t4 >= 56
	c_ac_t0_t4 += MUL[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 56
	c_bc_t20_mem0 += INPUT_mem_r

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 56
	c_bc_t20_mem1 += INPUT_mem_r

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 56
	c_bc_t4_t1_in += MUL_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 56
	c_bc_t4_t1_mem0 += ADD_mem[3]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 56
	c_bc_t4_t1_mem1 += ADD_mem[0]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 57
	c_ab_t1_t4_in += MUL_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 57
	c_ab_t1_t4_mem0 += ADD_mem[0]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 57
	c_ab_t1_t4_mem1 += ADD_mem[3]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 57
	c_bc_t1_t3_mem0 += INPUT_mem_r

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 57
	c_bc_t1_t3_mem1 += INPUT_mem_r

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 57
	c_bc_t20 += ADD[2]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=7, delay_cost=1)
	S += c_bc_t4_t1 >= 57
	c_bc_t4_t1 += MUL[0]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=7, delay_cost=1)
	S += c_ab_t1_t4 >= 58
	c_ab_t1_t4 += MUL[0]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 58
	c_bc_t1_t2_mem0 += INPUT_mem_r

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 58
	c_bc_t1_t2_mem1 += INPUT_mem_r

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 58
	c_bc_t1_t3 += ADD[2]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 58
	c_bc_t4_t0_in += MUL_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 58
	c_bc_t4_t0_mem0 += ADD_mem[2]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 58
	c_bc_t4_t0_mem1 += ADD_mem[1]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 58
	c_bc_t4_t2_mem0 += ADD_mem[2]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 58
	c_bc_t4_t2_mem1 += ADD_mem[3]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 59
	c_bc_t0_t3_mem0 += INPUT_mem_r

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 59
	c_bc_t0_t3_mem1 += INPUT_mem_r

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 59
	c_bc_t1_t2 += ADD[0]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=7, delay_cost=1)
	S += c_bc_t4_t0 >= 59
	c_bc_t4_t0 += MUL[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=1, delay_cost=1)
	S += c_bc_t4_t2 >= 59
	c_bc_t4_t2 += ADD[2]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 60
	c_bc_t0_t3 += ADD[3]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 60
	c_bc_t1_t4_in += MUL_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 60
	c_bc_t1_t4_mem0 += ADD_mem[0]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 60
	c_bc_t1_t4_mem1 += ADD_mem[2]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 60
	c_pcb_t1_t3_mem0 += INPUT_mem_r

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 60
	c_pcb_t1_t3_mem1 += INPUT_mem_r

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 61
	c_bc_t0_t4_in += MUL_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 61
	c_bc_t0_t4_mem0 += ADD_mem[2]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 61
	c_bc_t0_t4_mem1 += ADD_mem[3]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=7, delay_cost=1)
	S += c_bc_t1_t4 >= 61
	c_bc_t1_t4 += MUL[0]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	S += c_pcb_t1_t3 >= 61
	c_pcb_t1_t3 += ADD[0]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 61
	c_pcb_t30_mem0 += INPUT_mem_r

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 61
	c_pcb_t30_mem1 += INPUT_mem_r

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=7, delay_cost=1)
	S += c_bc_t0_t4 >= 62
	c_bc_t0_t4 += MUL[0]

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	S += c_pcb_t30 >= 62
	c_pcb_t30 += ADD[0]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 62
	c_pcb_t31_mem0 += INPUT_mem_r

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 62
	c_pcb_t31_mem1 += INPUT_mem_r

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 63
	c_paa_t0_t3_mem0 += INPUT_mem_r

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 63
	c_paa_t0_t3_mem1 += INPUT_mem_r

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	S += c_pcb_t31 >= 63
	c_pcb_t31 += ADD[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	S += c_paa_t0_t3 >= 64
	c_paa_t0_t3 += ADD[0]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 64
	c_paa_t1_t3_mem0 += INPUT_mem_r

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 64
	c_paa_t1_t3_mem1 += INPUT_mem_r

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 64
	c_pcb_t4_t3_mem0 += ADD_mem[0]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 64
	c_pcb_t4_t3_mem1 += ADD_mem[0]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	S += c_paa_t1_t3 >= 65
	c_paa_t1_t3 += ADD[3]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 65
	c_paa_t30_mem0 += INPUT_mem_r

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 65
	c_paa_t30_mem1 += INPUT_mem_r

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=1, delay_cost=1)
	S += c_pcb_t4_t3 >= 65
	c_pcb_t4_t3 += ADD[0]

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	S += c_paa_t30 >= 66
	c_paa_t30 += ADD[1]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 66
	c_paa_t31_mem0 += INPUT_mem_r

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 66
	c_paa_t31_mem1 += INPUT_mem_r

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	S += c_paa_t31 >= 67
	c_paa_t31 += ADD[0]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 67
	c_pbc_t0_t3_mem0 += INPUT_mem_r

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 67
	c_pbc_t0_t3_mem1 += INPUT_mem_r

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 68
	c_paa_t4_t3_mem0 += ADD_mem[1]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 68
	c_paa_t4_t3_mem1 += ADD_mem[0]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	S += c_pbc_t0_t3 >= 68
	c_pbc_t0_t3 += ADD[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 68
	c_pbc_t30_mem0 += INPUT_mem_r

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 68
	c_pbc_t30_mem1 += INPUT_mem_r

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=1, delay_cost=1)
	S += c_paa_t4_t3 >= 69
	c_paa_t4_t3 += ADD[3]

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	S += c_pbc_t30 >= 69
	c_pbc_t30 += ADD[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 69
	c_pbc_t31_mem0 += INPUT_mem_r

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 69
	c_pbc_t31_mem1 += INPUT_mem_r

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	S += c_pbc_t31 >= 70
	c_pbc_t31 += ADD[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 70
	c_pcb_t0_t3_mem0 += INPUT_mem_r

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 70
	c_pcb_t0_t3_mem1 += INPUT_mem_r

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 71
	c_pbc_t1_t3_mem0 += INPUT_mem_r

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 71
	c_pbc_t1_t3_mem1 += INPUT_mem_r

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 71
	c_pbc_t4_t3_mem0 += ADD_mem[0]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 71
	c_pbc_t4_t3_mem1 += ADD_mem[0]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	S += c_pcb_t0_t3 >= 71
	c_pcb_t0_t3 += ADD[3]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 72
	c_aa_t01_mem0 += INPUT_mem_r

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 72
	c_aa_t01_mem1 += ADD_mem[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 72
	c_bb_t01_mem0 += INPUT_mem_r

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 72
	c_bb_t01_mem1 += ADD_mem[0]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	S += c_pbc_t1_t3 >= 72
	c_pbc_t1_t3 += ADD[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=1, delay_cost=1)
	S += c_pbc_t4_t3 >= 72
	c_pbc_t4_t3 += ADD[0]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 73
	c_aa_t00_mem0 += INPUT_mem_r

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 73
	c_aa_t00_mem1 += ADD_mem[2]

	c_aa_t01 = S.Task('c_aa_t01', length=1, delay_cost=1)
	S += c_aa_t01 >= 73
	c_aa_t01 += ADD[2]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 73
	c_bb_t00_mem0 += INPUT_mem_r

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 73
	c_bb_t00_mem1 += ADD_mem[0]

	c_bb_t01 = S.Task('c_bb_t01', length=1, delay_cost=1)
	S += c_bb_t01 >= 73
	c_bb_t01 += ADD[1]

	c_aa_t00 = S.Task('c_aa_t00', length=1, delay_cost=1)
	S += c_aa_t00 >= 74
	c_aa_t00 += ADD[3]

	c_bb_t00 = S.Task('c_bb_t00', length=1, delay_cost=1)
	S += c_bb_t00 >= 74
	c_bb_t00 += ADD[0]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 74
	c_cc_t00_mem0 += INPUT_mem_r

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 74
	c_cc_t00_mem1 += ADD_mem[0]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 74
	c_cc_t01_mem0 += INPUT_mem_r

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 74
	c_cc_t01_mem1 += ADD_mem[3]

	c_cc_t00 = S.Task('c_cc_t00', length=1, delay_cost=1)
	S += c_cc_t00 >= 75
	c_cc_t00 += ADD[1]

	c_cc_t01 = S.Task('c_cc_t01', length=1, delay_cost=1)
	S += c_cc_t01 >= 75
	c_cc_t01 += ADD[2]


	# new tasks
	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	c_aa_t2_t0_in += alt(MUL_in)
	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=7, delay_cost=1)
	c_aa_t2_t0 += alt(MUL)
	S += c_aa_t2_t0>=c_aa_t2_t0_in

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	c_aa_t2_t0_mem0 += ADD_mem[3]
	S += 75 < c_aa_t2_t0_mem0
	S += c_aa_t2_t0_mem0 <= c_aa_t2_t0

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	c_aa_t2_t0_mem1 += ADD_mem[0]
	S += 24 < c_aa_t2_t0_mem1
	S += c_aa_t2_t0_mem1 <= c_aa_t2_t0

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	c_aa_t2_t1_in += alt(MUL_in)
	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=7, delay_cost=1)
	c_aa_t2_t1 += alt(MUL)
	S += c_aa_t2_t1>=c_aa_t2_t1_in

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	c_aa_t2_t1_mem0 += ADD_mem[2]
	S += 74 < c_aa_t2_t1_mem0
	S += c_aa_t2_t1_mem0 <= c_aa_t2_t1

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	c_aa_t2_t1_mem1 += ADD_mem[0]
	S += 23 < c_aa_t2_t1_mem1
	S += c_aa_t2_t1_mem1 <= c_aa_t2_t1

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=1, delay_cost=1)
	c_aa_t2_t2 += alt(ADD)

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	c_aa_t2_t2_mem0 += ADD_mem[3]
	S += 75 < c_aa_t2_t2_mem0
	S += c_aa_t2_t2_mem0 <= c_aa_t2_t2

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	c_aa_t2_t2_mem1 += ADD_mem[2]
	S += 74 < c_aa_t2_t2_mem1
	S += c_aa_t2_t2_mem1 <= c_aa_t2_t2

	c_aa_t31 = S.Task('c_aa_t31', length=1, delay_cost=1)
	c_aa_t31 += alt(ADD)

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	c_aa_t31_mem0 += MUL_mem[0]
	S += 34 < c_aa_t31_mem0
	S += c_aa_t31_mem0 <= c_aa_t31

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	c_aa_t31_mem1 += ADD_mem[2]
	S += 20 < c_aa_t31_mem1
	S += c_aa_t31_mem1 <= c_aa_t31

	c_aa10 = S.Task('c_aa10', length=1, delay_cost=1)
	c_aa10 += alt(ADD)

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	c_aa10_mem0 += ADD_mem[2]
	S += 19 < c_aa10_mem0
	S += c_aa10_mem0 <= c_aa10

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	c_bb_t2_t0_in += alt(MUL_in)
	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=7, delay_cost=1)
	c_bb_t2_t0 += alt(MUL)
	S += c_bb_t2_t0>=c_bb_t2_t0_in

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	c_bb_t2_t0_mem0 += ADD_mem[0]
	S += 75 < c_bb_t2_t0_mem0
	S += c_bb_t2_t0_mem0 <= c_bb_t2_t0

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	c_bb_t2_t0_mem1 += ADD_mem[2]
	S += 31 < c_bb_t2_t0_mem1
	S += c_bb_t2_t0_mem1 <= c_bb_t2_t0

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	c_bb_t2_t1_in += alt(MUL_in)
	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=7, delay_cost=1)
	c_bb_t2_t1 += alt(MUL)
	S += c_bb_t2_t1>=c_bb_t2_t1_in

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	c_bb_t2_t1_mem0 += ADD_mem[1]
	S += 74 < c_bb_t2_t1_mem0
	S += c_bb_t2_t1_mem0 <= c_bb_t2_t1

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	c_bb_t2_t1_mem1 += ADD_mem[2]
	S += 30 < c_bb_t2_t1_mem1
	S += c_bb_t2_t1_mem1 <= c_bb_t2_t1

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=1, delay_cost=1)
	c_bb_t2_t2 += alt(ADD)

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	c_bb_t2_t2_mem0 += ADD_mem[0]
	S += 75 < c_bb_t2_t2_mem0
	S += c_bb_t2_t2_mem0 <= c_bb_t2_t2

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	c_bb_t2_t2_mem1 += ADD_mem[1]
	S += 74 < c_bb_t2_t2_mem1
	S += c_bb_t2_t2_mem1 <= c_bb_t2_t2

	c_bb_t31 = S.Task('c_bb_t31', length=1, delay_cost=1)
	c_bb_t31 += alt(ADD)

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	c_bb_t31_mem0 += MUL_mem[0]
	S += 37 < c_bb_t31_mem0
	S += c_bb_t31_mem0 <= c_bb_t31

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	c_bb_t31_mem1 += ADD_mem[0]
	S += 16 < c_bb_t31_mem1
	S += c_bb_t31_mem1 <= c_bb_t31

	c_bb10 = S.Task('c_bb10', length=1, delay_cost=1)
	c_bb10 += alt(ADD)

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	c_bb10_mem0 += ADD_mem[1]
	S += 18 < c_bb10_mem0
	S += c_bb10_mem0 <= c_bb10

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	c_cc_t2_t0_in += alt(MUL_in)
	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=7, delay_cost=1)
	c_cc_t2_t0 += alt(MUL)
	S += c_cc_t2_t0>=c_cc_t2_t0_in

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	c_cc_t2_t0_mem0 += ADD_mem[1]
	S += 76 < c_cc_t2_t0_mem0
	S += c_cc_t2_t0_mem0 <= c_cc_t2_t0

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	c_cc_t2_t0_mem1 += ADD_mem[0]
	S += 20 < c_cc_t2_t0_mem1
	S += c_cc_t2_t0_mem1 <= c_cc_t2_t0

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	c_cc_t2_t1_in += alt(MUL_in)
	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=7, delay_cost=1)
	c_cc_t2_t1 += alt(MUL)
	S += c_cc_t2_t1>=c_cc_t2_t1_in

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	c_cc_t2_t1_mem0 += ADD_mem[2]
	S += 76 < c_cc_t2_t1_mem0
	S += c_cc_t2_t1_mem0 <= c_cc_t2_t1

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	c_cc_t2_t1_mem1 += ADD_mem[0]
	S += 22 < c_cc_t2_t1_mem1
	S += c_cc_t2_t1_mem1 <= c_cc_t2_t1

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=1, delay_cost=1)
	c_cc_t2_t2 += alt(ADD)

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	c_cc_t2_t2_mem0 += ADD_mem[1]
	S += 76 < c_cc_t2_t2_mem0
	S += c_cc_t2_t2_mem0 <= c_cc_t2_t2

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	c_cc_t2_t2_mem1 += ADD_mem[2]
	S += 76 < c_cc_t2_t2_mem1
	S += c_cc_t2_t2_mem1 <= c_cc_t2_t2

	c_cc_t31 = S.Task('c_cc_t31', length=1, delay_cost=1)
	c_cc_t31 += alt(ADD)

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	c_cc_t31_mem0 += MUL_mem[0]
	S += 23 < c_cc_t31_mem0
	S += c_cc_t31_mem0 <= c_cc_t31

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	c_cc_t31_mem1 += ADD_mem[0]
	S += 11 < c_cc_t31_mem1
	S += c_cc_t31_mem1 <= c_cc_t31

	c_cc10 = S.Task('c_cc10', length=1, delay_cost=1)
	c_cc10 += alt(ADD)

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	c_cc10_mem0 += ADD_mem[0]
	S += 12 < c_cc10_mem0
	S += c_cc10_mem0 <= c_cc10

	c_ab_t01 = S.Task('c_ab_t01', length=1, delay_cost=1)
	c_ab_t01 += alt(ADD)

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	c_ab_t01_mem0 += MUL_mem[0]
	S += 26 < c_ab_t01_mem0
	S += c_ab_t01_mem0 <= c_ab_t01

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	c_ab_t01_mem1 += ADD_mem[2]
	S += 21 < c_ab_t01_mem1
	S += c_ab_t01_mem1 <= c_ab_t01

	c_ab_t11 = S.Task('c_ab_t11', length=1, delay_cost=1)
	c_ab_t11 += alt(ADD)

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	c_ab_t11_mem0 += MUL_mem[0]
	S += 65 < c_ab_t11_mem0
	S += c_ab_t11_mem0 <= c_ab_t11

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	c_ab_t11_mem1 += ADD_mem[1]
	S += 15 < c_ab_t11_mem1
	S += c_ab_t11_mem1 <= c_ab_t11

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	c_ab_t4_t4_in += alt(MUL_in)
	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=7, delay_cost=1)
	c_ab_t4_t4 += alt(MUL)
	S += c_ab_t4_t4>=c_ab_t4_t4_in

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	c_ab_t4_t4_mem0 += ADD_mem[2]
	S += 55 < c_ab_t4_t4_mem0
	S += c_ab_t4_t4_mem0 <= c_ab_t4_t4

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	c_ab_t4_t4_mem1 += ADD_mem[2]
	S += 57 < c_ab_t4_t4_mem1
	S += c_ab_t4_t4_mem1 <= c_ab_t4_t4

	c_ab_t40 = S.Task('c_ab_t40', length=1, delay_cost=1)
	c_ab_t40 += alt(ADD)

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	c_ab_t40_mem0 += MUL_mem[0]
	S += 62 < c_ab_t40_mem0
	S += c_ab_t40_mem0 <= c_ab_t40

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	c_ab_t40_mem1 += MUL_mem[0]
	S += 56 < c_ab_t40_mem1
	S += c_ab_t40_mem1 <= c_ab_t40

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=1, delay_cost=1)
	c_ab_t4_t5 += alt(ADD)

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	c_ab_t4_t5_mem0 += MUL_mem[0]
	S += 62 < c_ab_t4_t5_mem0
	S += c_ab_t4_t5_mem0 <= c_ab_t4_t5

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	c_ab_t4_t5_mem1 += MUL_mem[0]
	S += 56 < c_ab_t4_t5_mem1
	S += c_ab_t4_t5_mem1 <= c_ab_t4_t5

	c_ab_t50 = S.Task('c_ab_t50', length=1, delay_cost=1)
	c_ab_t50 += alt(ADD)

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	c_ab_t50_mem0 += ADD_mem[1]
	S += 17 < c_ab_t50_mem0
	S += c_ab_t50_mem0 <= c_ab_t50

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	c_ab_t50_mem1 += ADD_mem[2]
	S += 14 < c_ab_t50_mem1
	S += c_ab_t50_mem1 <= c_ab_t50

	c_bc_t01 = S.Task('c_bc_t01', length=1, delay_cost=1)
	c_bc_t01 += alt(ADD)

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	c_bc_t01_mem0 += MUL_mem[0]
	S += 69 < c_bc_t01_mem0
	S += c_bc_t01_mem0 <= c_bc_t01

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	c_bc_t01_mem1 += ADD_mem[1]
	S += 44 < c_bc_t01_mem1
	S += c_bc_t01_mem1 <= c_bc_t01

	c_bc_t11 = S.Task('c_bc_t11', length=1, delay_cost=1)
	c_bc_t11 += alt(ADD)

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	c_bc_t11_mem0 += MUL_mem[0]
	S += 68 < c_bc_t11_mem0
	S += c_bc_t11_mem0 <= c_bc_t11

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	c_bc_t11_mem1 += ADD_mem[1]
	S += 49 < c_bc_t11_mem1
	S += c_bc_t11_mem1 <= c_bc_t11

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	c_bc_t4_t4_in += alt(MUL_in)
	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=7, delay_cost=1)
	c_bc_t4_t4 += alt(MUL)
	S += c_bc_t4_t4>=c_bc_t4_t4_in

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	c_bc_t4_t4_mem0 += ADD_mem[2]
	S += 60 < c_bc_t4_t4_mem0
	S += c_bc_t4_t4_mem0 <= c_bc_t4_t4

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	c_bc_t4_t4_mem1 += ADD_mem[0]
	S += 55 < c_bc_t4_t4_mem1
	S += c_bc_t4_t4_mem1 <= c_bc_t4_t4

	c_bc_t40 = S.Task('c_bc_t40', length=1, delay_cost=1)
	c_bc_t40 += alt(ADD)

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	c_bc_t40_mem0 += MUL_mem[0]
	S += 66 < c_bc_t40_mem0
	S += c_bc_t40_mem0 <= c_bc_t40

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	c_bc_t40_mem1 += MUL_mem[0]
	S += 64 < c_bc_t40_mem1
	S += c_bc_t40_mem1 <= c_bc_t40

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=1, delay_cost=1)
	c_bc_t4_t5 += alt(ADD)

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	c_bc_t4_t5_mem0 += MUL_mem[0]
	S += 66 < c_bc_t4_t5_mem0
	S += c_bc_t4_t5_mem0 <= c_bc_t4_t5

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	c_bc_t4_t5_mem1 += MUL_mem[0]
	S += 64 < c_bc_t4_t5_mem1
	S += c_bc_t4_t5_mem1 <= c_bc_t4_t5

	c_bc_t50 = S.Task('c_bc_t50', length=1, delay_cost=1)
	c_bc_t50 += alt(ADD)

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	c_bc_t50_mem0 += ADD_mem[0]
	S += 43 < c_bc_t50_mem0
	S += c_bc_t50_mem0 <= c_bc_t50

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	c_bc_t50_mem1 += ADD_mem[0]
	S += 42 < c_bc_t50_mem1
	S += c_bc_t50_mem1 <= c_bc_t50

	c_ac_t01 = S.Task('c_ac_t01', length=1, delay_cost=1)
	c_ac_t01 += alt(ADD)

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	c_ac_t01_mem0 += MUL_mem[0]
	S += 63 < c_ac_t01_mem0
	S += c_ac_t01_mem0 <= c_ac_t01

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	c_ac_t01_mem1 += ADD_mem[1]
	S += 47 < c_ac_t01_mem1
	S += c_ac_t01_mem1 <= c_ac_t01

	c_ac_t11 = S.Task('c_ac_t11', length=1, delay_cost=1)
	c_ac_t11 += alt(ADD)

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	c_ac_t11_mem0 += MUL_mem[0]
	S += 58 < c_ac_t11_mem0
	S += c_ac_t11_mem0 <= c_ac_t11

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	c_ac_t11_mem1 += ADD_mem[2]
	S += 46 < c_ac_t11_mem1
	S += c_ac_t11_mem1 <= c_ac_t11

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	c_ac_t4_t4_in += alt(MUL_in)
	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=7, delay_cost=1)
	c_ac_t4_t4 += alt(MUL)
	S += c_ac_t4_t4>=c_ac_t4_t4_in

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	c_ac_t4_t4_mem0 += ADD_mem[1]
	S += 54 < c_ac_t4_t4_mem0
	S += c_ac_t4_t4_mem0 <= c_ac_t4_t4

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	c_ac_t4_t4_mem1 += ADD_mem[0]
	S += 48 < c_ac_t4_t4_mem1
	S += c_ac_t4_t4_mem1 <= c_ac_t4_t4

	c_ac_t40 = S.Task('c_ac_t40', length=1, delay_cost=1)
	c_ac_t40 += alt(ADD)

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	c_ac_t40_mem0 += MUL_mem[0]
	S += 59 < c_ac_t40_mem0
	S += c_ac_t40_mem0 <= c_ac_t40

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	c_ac_t40_mem1 += MUL_mem[0]
	S += 52 < c_ac_t40_mem1
	S += c_ac_t40_mem1 <= c_ac_t40

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=1, delay_cost=1)
	c_ac_t4_t5 += alt(ADD)

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	c_ac_t4_t5_mem0 += MUL_mem[0]
	S += 59 < c_ac_t4_t5_mem0
	S += c_ac_t4_t5_mem0 <= c_ac_t4_t5

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	c_ac_t4_t5_mem1 += MUL_mem[0]
	S += 52 < c_ac_t4_t5_mem1
	S += c_ac_t4_t5_mem1 <= c_ac_t4_t5

	c_ac_t50 = S.Task('c_ac_t50', length=1, delay_cost=1)
	c_ac_t50 += alt(ADD)

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	c_ac_t50_mem0 += ADD_mem[3]
	S += 48 < c_ac_t50_mem0
	S += c_ac_t50_mem0 <= c_ac_t50

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	c_ac_t50_mem1 += ADD_mem[1]
	S += 45 < c_ac_t50_mem1
	S += c_ac_t50_mem1 <= c_ac_t50

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	c_aa_t2_t4_in += alt(MUL_in)
	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=7, delay_cost=1)
	c_aa_t2_t4 += alt(MUL)
	S += c_aa_t2_t4>=c_aa_t2_t4_in

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	c_aa_t2_t4_mem0 += alt(ADD_mem)
	S += (c_aa_t2_t2*ADD[0]) < c_aa_t2_t4_mem0*ADD_mem[0]
	S += (c_aa_t2_t2*ADD[1]) < c_aa_t2_t4_mem0*ADD_mem[1]
	S += (c_aa_t2_t2*ADD[2]) < c_aa_t2_t4_mem0*ADD_mem[2]
	S += (c_aa_t2_t2*ADD[3]) < c_aa_t2_t4_mem0*ADD_mem[3]
	S += c_aa_t2_t4_mem0 <= c_aa_t2_t4

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	c_aa_t2_t4_mem1 += ADD_mem[0]
	S += 26 < c_aa_t2_t4_mem1
	S += c_aa_t2_t4_mem1 <= c_aa_t2_t4

	c_aa_t20 = S.Task('c_aa_t20', length=1, delay_cost=1)
	c_aa_t20 += alt(ADD)

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	c_aa_t20_mem0 += alt(MUL_mem)
	S += (c_aa_t2_t0*MUL[0]) < c_aa_t20_mem0*MUL_mem[0]
	S += c_aa_t20_mem0 <= c_aa_t20

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	c_aa_t20_mem1 += alt(MUL_mem)
	S += (c_aa_t2_t1*MUL[0]) < c_aa_t20_mem1*MUL_mem[0]
	S += c_aa_t20_mem1 <= c_aa_t20

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=1, delay_cost=1)
	c_aa_t2_t5 += alt(ADD)

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	c_aa_t2_t5_mem0 += alt(MUL_mem)
	S += (c_aa_t2_t0*MUL[0]) < c_aa_t2_t5_mem0*MUL_mem[0]
	S += c_aa_t2_t5_mem0 <= c_aa_t2_t5

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	c_aa_t2_t5_mem1 += alt(MUL_mem)
	S += (c_aa_t2_t1*MUL[0]) < c_aa_t2_t5_mem1*MUL_mem[0]
	S += c_aa_t2_t5_mem1 <= c_aa_t2_t5

	c_aa_t40 = S.Task('c_aa_t40', length=1, delay_cost=1)
	c_aa_t40 += alt(ADD)

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	c_aa_t40_mem0 += ADD_mem[2]
	S += 19 < c_aa_t40_mem0
	S += c_aa_t40_mem0 <= c_aa_t40

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	c_aa_t40_mem1 += alt(ADD_mem)
	S += (c_aa_t31*ADD[0]) < c_aa_t40_mem1*ADD_mem[0]
	S += (c_aa_t31*ADD[1]) < c_aa_t40_mem1*ADD_mem[1]
	S += (c_aa_t31*ADD[2]) < c_aa_t40_mem1*ADD_mem[2]
	S += (c_aa_t31*ADD[3]) < c_aa_t40_mem1*ADD_mem[3]
	S += c_aa_t40_mem1 <= c_aa_t40

	c_aa_t41 = S.Task('c_aa_t41', length=1, delay_cost=1)
	c_aa_t41 += alt(ADD)

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	c_aa_t41_mem0 += alt(ADD_mem)
	S += (c_aa_t31*ADD[0]) < c_aa_t41_mem0*ADD_mem[0]
	S += (c_aa_t31*ADD[1]) < c_aa_t41_mem0*ADD_mem[1]
	S += (c_aa_t31*ADD[2]) < c_aa_t41_mem0*ADD_mem[2]
	S += (c_aa_t31*ADD[3]) < c_aa_t41_mem0*ADD_mem[3]
	S += c_aa_t41_mem0 <= c_aa_t41

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	c_aa_t41_mem1 += ADD_mem[2]
	S += 19 < c_aa_t41_mem1
	S += c_aa_t41_mem1 <= c_aa_t41

	c_aa11 = S.Task('c_aa11', length=1, delay_cost=1)
	c_aa11 += alt(ADD)

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	c_aa11_mem0 += alt(ADD_mem)
	S += (c_aa_t31*ADD[0]) < c_aa11_mem0*ADD_mem[0]
	S += (c_aa_t31*ADD[1]) < c_aa11_mem0*ADD_mem[1]
	S += (c_aa_t31*ADD[2]) < c_aa11_mem0*ADD_mem[2]
	S += (c_aa_t31*ADD[3]) < c_aa11_mem0*ADD_mem[3]
	S += c_aa11_mem0 <= c_aa11

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	c_bb_t2_t4_in += alt(MUL_in)
	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=7, delay_cost=1)
	c_bb_t2_t4 += alt(MUL)
	S += c_bb_t2_t4>=c_bb_t2_t4_in

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	c_bb_t2_t4_mem0 += alt(ADD_mem)
	S += (c_bb_t2_t2*ADD[0]) < c_bb_t2_t4_mem0*ADD_mem[0]
	S += (c_bb_t2_t2*ADD[1]) < c_bb_t2_t4_mem0*ADD_mem[1]
	S += (c_bb_t2_t2*ADD[2]) < c_bb_t2_t4_mem0*ADD_mem[2]
	S += (c_bb_t2_t2*ADD[3]) < c_bb_t2_t4_mem0*ADD_mem[3]
	S += c_bb_t2_t4_mem0 <= c_bb_t2_t4

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	c_bb_t2_t4_mem1 += ADD_mem[0]
	S += 33 < c_bb_t2_t4_mem1
	S += c_bb_t2_t4_mem1 <= c_bb_t2_t4

	c_bb_t20 = S.Task('c_bb_t20', length=1, delay_cost=1)
	c_bb_t20 += alt(ADD)

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	c_bb_t20_mem0 += alt(MUL_mem)
	S += (c_bb_t2_t0*MUL[0]) < c_bb_t20_mem0*MUL_mem[0]
	S += c_bb_t20_mem0 <= c_bb_t20

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	c_bb_t20_mem1 += alt(MUL_mem)
	S += (c_bb_t2_t1*MUL[0]) < c_bb_t20_mem1*MUL_mem[0]
	S += c_bb_t20_mem1 <= c_bb_t20

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=1, delay_cost=1)
	c_bb_t2_t5 += alt(ADD)

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	c_bb_t2_t5_mem0 += alt(MUL_mem)
	S += (c_bb_t2_t0*MUL[0]) < c_bb_t2_t5_mem0*MUL_mem[0]
	S += c_bb_t2_t5_mem0 <= c_bb_t2_t5

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	c_bb_t2_t5_mem1 += alt(MUL_mem)
	S += (c_bb_t2_t1*MUL[0]) < c_bb_t2_t5_mem1*MUL_mem[0]
	S += c_bb_t2_t5_mem1 <= c_bb_t2_t5

	c_bb_t40 = S.Task('c_bb_t40', length=1, delay_cost=1)
	c_bb_t40 += alt(ADD)

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	c_bb_t40_mem0 += ADD_mem[1]
	S += 18 < c_bb_t40_mem0
	S += c_bb_t40_mem0 <= c_bb_t40

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	c_bb_t40_mem1 += alt(ADD_mem)
	S += (c_bb_t31*ADD[0]) < c_bb_t40_mem1*ADD_mem[0]
	S += (c_bb_t31*ADD[1]) < c_bb_t40_mem1*ADD_mem[1]
	S += (c_bb_t31*ADD[2]) < c_bb_t40_mem1*ADD_mem[2]
	S += (c_bb_t31*ADD[3]) < c_bb_t40_mem1*ADD_mem[3]
	S += c_bb_t40_mem1 <= c_bb_t40

	c_bb_t41 = S.Task('c_bb_t41', length=1, delay_cost=1)
	c_bb_t41 += alt(ADD)

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	c_bb_t41_mem0 += alt(ADD_mem)
	S += (c_bb_t31*ADD[0]) < c_bb_t41_mem0*ADD_mem[0]
	S += (c_bb_t31*ADD[1]) < c_bb_t41_mem0*ADD_mem[1]
	S += (c_bb_t31*ADD[2]) < c_bb_t41_mem0*ADD_mem[2]
	S += (c_bb_t31*ADD[3]) < c_bb_t41_mem0*ADD_mem[3]
	S += c_bb_t41_mem0 <= c_bb_t41

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	c_bb_t41_mem1 += ADD_mem[1]
	S += 18 < c_bb_t41_mem1
	S += c_bb_t41_mem1 <= c_bb_t41

	c_bb11 = S.Task('c_bb11', length=1, delay_cost=1)
	c_bb11 += alt(ADD)

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	c_bb11_mem0 += alt(ADD_mem)
	S += (c_bb_t31*ADD[0]) < c_bb11_mem0*ADD_mem[0]
	S += (c_bb_t31*ADD[1]) < c_bb11_mem0*ADD_mem[1]
	S += (c_bb_t31*ADD[2]) < c_bb11_mem0*ADD_mem[2]
	S += (c_bb_t31*ADD[3]) < c_bb11_mem0*ADD_mem[3]
	S += c_bb11_mem0 <= c_bb11

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	c_cc_t2_t4_in += alt(MUL_in)
	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=7, delay_cost=1)
	c_cc_t2_t4 += alt(MUL)
	S += c_cc_t2_t4>=c_cc_t2_t4_in

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	c_cc_t2_t4_mem0 += alt(ADD_mem)
	S += (c_cc_t2_t2*ADD[0]) < c_cc_t2_t4_mem0*ADD_mem[0]
	S += (c_cc_t2_t2*ADD[1]) < c_cc_t2_t4_mem0*ADD_mem[1]
	S += (c_cc_t2_t2*ADD[2]) < c_cc_t2_t4_mem0*ADD_mem[2]
	S += (c_cc_t2_t2*ADD[3]) < c_cc_t2_t4_mem0*ADD_mem[3]
	S += c_cc_t2_t4_mem0 <= c_cc_t2_t4

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	c_cc_t2_t4_mem1 += ADD_mem[1]
	S += 24 < c_cc_t2_t4_mem1
	S += c_cc_t2_t4_mem1 <= c_cc_t2_t4

	c_cc_t20 = S.Task('c_cc_t20', length=1, delay_cost=1)
	c_cc_t20 += alt(ADD)

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	c_cc_t20_mem0 += alt(MUL_mem)
	S += (c_cc_t2_t0*MUL[0]) < c_cc_t20_mem0*MUL_mem[0]
	S += c_cc_t20_mem0 <= c_cc_t20

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	c_cc_t20_mem1 += alt(MUL_mem)
	S += (c_cc_t2_t1*MUL[0]) < c_cc_t20_mem1*MUL_mem[0]
	S += c_cc_t20_mem1 <= c_cc_t20

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=1, delay_cost=1)
	c_cc_t2_t5 += alt(ADD)

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	c_cc_t2_t5_mem0 += alt(MUL_mem)
	S += (c_cc_t2_t0*MUL[0]) < c_cc_t2_t5_mem0*MUL_mem[0]
	S += c_cc_t2_t5_mem0 <= c_cc_t2_t5

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	c_cc_t2_t5_mem1 += alt(MUL_mem)
	S += (c_cc_t2_t1*MUL[0]) < c_cc_t2_t5_mem1*MUL_mem[0]
	S += c_cc_t2_t5_mem1 <= c_cc_t2_t5

	c_cc_t40 = S.Task('c_cc_t40', length=1, delay_cost=1)
	c_cc_t40 += alt(ADD)

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	c_cc_t40_mem0 += ADD_mem[0]
	S += 12 < c_cc_t40_mem0
	S += c_cc_t40_mem0 <= c_cc_t40

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	c_cc_t40_mem1 += alt(ADD_mem)
	S += (c_cc_t31*ADD[0]) < c_cc_t40_mem1*ADD_mem[0]
	S += (c_cc_t31*ADD[1]) < c_cc_t40_mem1*ADD_mem[1]
	S += (c_cc_t31*ADD[2]) < c_cc_t40_mem1*ADD_mem[2]
	S += (c_cc_t31*ADD[3]) < c_cc_t40_mem1*ADD_mem[3]
	S += c_cc_t40_mem1 <= c_cc_t40

	c_cc_t41 = S.Task('c_cc_t41', length=1, delay_cost=1)
	c_cc_t41 += alt(ADD)

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	c_cc_t41_mem0 += alt(ADD_mem)
	S += (c_cc_t31*ADD[0]) < c_cc_t41_mem0*ADD_mem[0]
	S += (c_cc_t31*ADD[1]) < c_cc_t41_mem0*ADD_mem[1]
	S += (c_cc_t31*ADD[2]) < c_cc_t41_mem0*ADD_mem[2]
	S += (c_cc_t31*ADD[3]) < c_cc_t41_mem0*ADD_mem[3]
	S += c_cc_t41_mem0 <= c_cc_t41

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	c_cc_t41_mem1 += ADD_mem[0]
	S += 12 < c_cc_t41_mem1
	S += c_cc_t41_mem1 <= c_cc_t41

	c_cc11 = S.Task('c_cc11', length=1, delay_cost=1)
	c_cc11 += alt(ADD)

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	c_cc11_mem0 += alt(ADD_mem)
	S += (c_cc_t31*ADD[0]) < c_cc11_mem0*ADD_mem[0]
	S += (c_cc_t31*ADD[1]) < c_cc11_mem0*ADD_mem[1]
	S += (c_cc_t31*ADD[2]) < c_cc11_mem0*ADD_mem[2]
	S += (c_cc_t31*ADD[3]) < c_cc11_mem0*ADD_mem[3]
	S += c_cc11_mem0 <= c_cc11

	c_ab_t41 = S.Task('c_ab_t41', length=1, delay_cost=1)
	c_ab_t41 += alt(ADD)

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	c_ab_t41_mem0 += alt(MUL_mem)
	S += (c_ab_t4_t4*MUL[0]) < c_ab_t41_mem0*MUL_mem[0]
	S += c_ab_t41_mem0 <= c_ab_t41

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	c_ab_t41_mem1 += alt(ADD_mem)
	S += (c_ab_t4_t5*ADD[0]) < c_ab_t41_mem1*ADD_mem[0]
	S += (c_ab_t4_t5*ADD[1]) < c_ab_t41_mem1*ADD_mem[1]
	S += (c_ab_t4_t5*ADD[2]) < c_ab_t41_mem1*ADD_mem[2]
	S += (c_ab_t4_t5*ADD[3]) < c_ab_t41_mem1*ADD_mem[3]
	S += c_ab_t41_mem1 <= c_ab_t41

	c_ab_s00 = S.Task('c_ab_s00', length=1, delay_cost=1)
	c_ab_s00 += alt(ADD)

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	c_ab_s00_mem0 += ADD_mem[2]
	S += 14 < c_ab_s00_mem0
	S += c_ab_s00_mem0 <= c_ab_s00

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	c_ab_s00_mem1 += alt(ADD_mem)
	S += (c_ab_t11*ADD[0]) < c_ab_s00_mem1*ADD_mem[0]
	S += (c_ab_t11*ADD[1]) < c_ab_s00_mem1*ADD_mem[1]
	S += (c_ab_t11*ADD[2]) < c_ab_s00_mem1*ADD_mem[2]
	S += (c_ab_t11*ADD[3]) < c_ab_s00_mem1*ADD_mem[3]
	S += c_ab_s00_mem1 <= c_ab_s00

	c_ab_s01 = S.Task('c_ab_s01', length=1, delay_cost=1)
	c_ab_s01 += alt(ADD)

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	c_ab_s01_mem0 += alt(ADD_mem)
	S += (c_ab_t11*ADD[0]) < c_ab_s01_mem0*ADD_mem[0]
	S += (c_ab_t11*ADD[1]) < c_ab_s01_mem0*ADD_mem[1]
	S += (c_ab_t11*ADD[2]) < c_ab_s01_mem0*ADD_mem[2]
	S += (c_ab_t11*ADD[3]) < c_ab_s01_mem0*ADD_mem[3]
	S += c_ab_s01_mem0 <= c_ab_s01

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	c_ab_s01_mem1 += ADD_mem[2]
	S += 14 < c_ab_s01_mem1
	S += c_ab_s01_mem1 <= c_ab_s01

	c_ab_t51 = S.Task('c_ab_t51', length=1, delay_cost=1)
	c_ab_t51 += alt(ADD)

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	c_ab_t51_mem0 += alt(ADD_mem)
	S += (c_ab_t01*ADD[0]) < c_ab_t51_mem0*ADD_mem[0]
	S += (c_ab_t01*ADD[1]) < c_ab_t51_mem0*ADD_mem[1]
	S += (c_ab_t01*ADD[2]) < c_ab_t51_mem0*ADD_mem[2]
	S += (c_ab_t01*ADD[3]) < c_ab_t51_mem0*ADD_mem[3]
	S += c_ab_t51_mem0 <= c_ab_t51

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	c_ab_t51_mem1 += alt(ADD_mem)
	S += (c_ab_t11*ADD[0]) < c_ab_t51_mem1*ADD_mem[0]
	S += (c_ab_t11*ADD[1]) < c_ab_t51_mem1*ADD_mem[1]
	S += (c_ab_t11*ADD[2]) < c_ab_t51_mem1*ADD_mem[2]
	S += (c_ab_t11*ADD[3]) < c_ab_t51_mem1*ADD_mem[3]
	S += c_ab_t51_mem1 <= c_ab_t51

	c_ab10 = S.Task('c_ab10', length=1, delay_cost=1)
	c_ab10 += alt(ADD)

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	c_ab10_mem0 += alt(ADD_mem)
	S += (c_ab_t40*ADD[0]) < c_ab10_mem0*ADD_mem[0]
	S += (c_ab_t40*ADD[1]) < c_ab10_mem0*ADD_mem[1]
	S += (c_ab_t40*ADD[2]) < c_ab10_mem0*ADD_mem[2]
	S += (c_ab_t40*ADD[3]) < c_ab10_mem0*ADD_mem[3]
	S += c_ab10_mem0 <= c_ab10

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	c_ab10_mem1 += alt(ADD_mem)
	S += (c_ab_t50*ADD[0]) < c_ab10_mem1*ADD_mem[0]
	S += (c_ab_t50*ADD[1]) < c_ab10_mem1*ADD_mem[1]
	S += (c_ab_t50*ADD[2]) < c_ab10_mem1*ADD_mem[2]
	S += (c_ab_t50*ADD[3]) < c_ab10_mem1*ADD_mem[3]
	S += c_ab10_mem1 <= c_ab10

	c_bc_t41 = S.Task('c_bc_t41', length=1, delay_cost=1)
	c_bc_t41 += alt(ADD)

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	c_bc_t41_mem0 += alt(MUL_mem)
	S += (c_bc_t4_t4*MUL[0]) < c_bc_t41_mem0*MUL_mem[0]
	S += c_bc_t41_mem0 <= c_bc_t41

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	c_bc_t41_mem1 += alt(ADD_mem)
	S += (c_bc_t4_t5*ADD[0]) < c_bc_t41_mem1*ADD_mem[0]
	S += (c_bc_t4_t5*ADD[1]) < c_bc_t41_mem1*ADD_mem[1]
	S += (c_bc_t4_t5*ADD[2]) < c_bc_t41_mem1*ADD_mem[2]
	S += (c_bc_t4_t5*ADD[3]) < c_bc_t41_mem1*ADD_mem[3]
	S += c_bc_t41_mem1 <= c_bc_t41

	c_bc_s00 = S.Task('c_bc_s00', length=1, delay_cost=1)
	c_bc_s00 += alt(ADD)

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	c_bc_s00_mem0 += ADD_mem[0]
	S += 42 < c_bc_s00_mem0
	S += c_bc_s00_mem0 <= c_bc_s00

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	c_bc_s00_mem1 += alt(ADD_mem)
	S += (c_bc_t11*ADD[0]) < c_bc_s00_mem1*ADD_mem[0]
	S += (c_bc_t11*ADD[1]) < c_bc_s00_mem1*ADD_mem[1]
	S += (c_bc_t11*ADD[2]) < c_bc_s00_mem1*ADD_mem[2]
	S += (c_bc_t11*ADD[3]) < c_bc_s00_mem1*ADD_mem[3]
	S += c_bc_s00_mem1 <= c_bc_s00

	c_bc_s01 = S.Task('c_bc_s01', length=1, delay_cost=1)
	c_bc_s01 += alt(ADD)

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	c_bc_s01_mem0 += alt(ADD_mem)
	S += (c_bc_t11*ADD[0]) < c_bc_s01_mem0*ADD_mem[0]
	S += (c_bc_t11*ADD[1]) < c_bc_s01_mem0*ADD_mem[1]
	S += (c_bc_t11*ADD[2]) < c_bc_s01_mem0*ADD_mem[2]
	S += (c_bc_t11*ADD[3]) < c_bc_s01_mem0*ADD_mem[3]
	S += c_bc_s01_mem0 <= c_bc_s01

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	c_bc_s01_mem1 += ADD_mem[0]
	S += 42 < c_bc_s01_mem1
	S += c_bc_s01_mem1 <= c_bc_s01

	c_bc_t51 = S.Task('c_bc_t51', length=1, delay_cost=1)
	c_bc_t51 += alt(ADD)

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	c_bc_t51_mem0 += alt(ADD_mem)
	S += (c_bc_t01*ADD[0]) < c_bc_t51_mem0*ADD_mem[0]
	S += (c_bc_t01*ADD[1]) < c_bc_t51_mem0*ADD_mem[1]
	S += (c_bc_t01*ADD[2]) < c_bc_t51_mem0*ADD_mem[2]
	S += (c_bc_t01*ADD[3]) < c_bc_t51_mem0*ADD_mem[3]
	S += c_bc_t51_mem0 <= c_bc_t51

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	c_bc_t51_mem1 += alt(ADD_mem)
	S += (c_bc_t11*ADD[0]) < c_bc_t51_mem1*ADD_mem[0]
	S += (c_bc_t11*ADD[1]) < c_bc_t51_mem1*ADD_mem[1]
	S += (c_bc_t11*ADD[2]) < c_bc_t51_mem1*ADD_mem[2]
	S += (c_bc_t11*ADD[3]) < c_bc_t51_mem1*ADD_mem[3]
	S += c_bc_t51_mem1 <= c_bc_t51

	c_bc10 = S.Task('c_bc10', length=1, delay_cost=1)
	c_bc10 += alt(ADD)

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	c_bc10_mem0 += alt(ADD_mem)
	S += (c_bc_t40*ADD[0]) < c_bc10_mem0*ADD_mem[0]
	S += (c_bc_t40*ADD[1]) < c_bc10_mem0*ADD_mem[1]
	S += (c_bc_t40*ADD[2]) < c_bc10_mem0*ADD_mem[2]
	S += (c_bc_t40*ADD[3]) < c_bc10_mem0*ADD_mem[3]
	S += c_bc10_mem0 <= c_bc10

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	c_bc10_mem1 += alt(ADD_mem)
	S += (c_bc_t50*ADD[0]) < c_bc10_mem1*ADD_mem[0]
	S += (c_bc_t50*ADD[1]) < c_bc10_mem1*ADD_mem[1]
	S += (c_bc_t50*ADD[2]) < c_bc10_mem1*ADD_mem[2]
	S += (c_bc_t50*ADD[3]) < c_bc10_mem1*ADD_mem[3]
	S += c_bc10_mem1 <= c_bc10

	c_ac_t41 = S.Task('c_ac_t41', length=1, delay_cost=1)
	c_ac_t41 += alt(ADD)

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	c_ac_t41_mem0 += alt(MUL_mem)
	S += (c_ac_t4_t4*MUL[0]) < c_ac_t41_mem0*MUL_mem[0]
	S += c_ac_t41_mem0 <= c_ac_t41

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	c_ac_t41_mem1 += alt(ADD_mem)
	S += (c_ac_t4_t5*ADD[0]) < c_ac_t41_mem1*ADD_mem[0]
	S += (c_ac_t4_t5*ADD[1]) < c_ac_t41_mem1*ADD_mem[1]
	S += (c_ac_t4_t5*ADD[2]) < c_ac_t41_mem1*ADD_mem[2]
	S += (c_ac_t4_t5*ADD[3]) < c_ac_t41_mem1*ADD_mem[3]
	S += c_ac_t41_mem1 <= c_ac_t41

	c_ac_s00 = S.Task('c_ac_s00', length=1, delay_cost=1)
	c_ac_s00 += alt(ADD)

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	c_ac_s00_mem0 += ADD_mem[1]
	S += 45 < c_ac_s00_mem0
	S += c_ac_s00_mem0 <= c_ac_s00

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	c_ac_s00_mem1 += alt(ADD_mem)
	S += (c_ac_t11*ADD[0]) < c_ac_s00_mem1*ADD_mem[0]
	S += (c_ac_t11*ADD[1]) < c_ac_s00_mem1*ADD_mem[1]
	S += (c_ac_t11*ADD[2]) < c_ac_s00_mem1*ADD_mem[2]
	S += (c_ac_t11*ADD[3]) < c_ac_s00_mem1*ADD_mem[3]
	S += c_ac_s00_mem1 <= c_ac_s00

	c_ac_s01 = S.Task('c_ac_s01', length=1, delay_cost=1)
	c_ac_s01 += alt(ADD)

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	c_ac_s01_mem0 += alt(ADD_mem)
	S += (c_ac_t11*ADD[0]) < c_ac_s01_mem0*ADD_mem[0]
	S += (c_ac_t11*ADD[1]) < c_ac_s01_mem0*ADD_mem[1]
	S += (c_ac_t11*ADD[2]) < c_ac_s01_mem0*ADD_mem[2]
	S += (c_ac_t11*ADD[3]) < c_ac_s01_mem0*ADD_mem[3]
	S += c_ac_s01_mem0 <= c_ac_s01

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	c_ac_s01_mem1 += ADD_mem[1]
	S += 45 < c_ac_s01_mem1
	S += c_ac_s01_mem1 <= c_ac_s01

	c_ac_t51 = S.Task('c_ac_t51', length=1, delay_cost=1)
	c_ac_t51 += alt(ADD)

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	c_ac_t51_mem0 += alt(ADD_mem)
	S += (c_ac_t01*ADD[0]) < c_ac_t51_mem0*ADD_mem[0]
	S += (c_ac_t01*ADD[1]) < c_ac_t51_mem0*ADD_mem[1]
	S += (c_ac_t01*ADD[2]) < c_ac_t51_mem0*ADD_mem[2]
	S += (c_ac_t01*ADD[3]) < c_ac_t51_mem0*ADD_mem[3]
	S += c_ac_t51_mem0 <= c_ac_t51

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	c_ac_t51_mem1 += alt(ADD_mem)
	S += (c_ac_t11*ADD[0]) < c_ac_t51_mem1*ADD_mem[0]
	S += (c_ac_t11*ADD[1]) < c_ac_t51_mem1*ADD_mem[1]
	S += (c_ac_t11*ADD[2]) < c_ac_t51_mem1*ADD_mem[2]
	S += (c_ac_t11*ADD[3]) < c_ac_t51_mem1*ADD_mem[3]
	S += c_ac_t51_mem1 <= c_ac_t51

	c_ac10 = S.Task('c_ac10', length=1, delay_cost=1)
	c_ac10 += alt(ADD)

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	c_ac10_mem0 += alt(ADD_mem)
	S += (c_ac_t40*ADD[0]) < c_ac10_mem0*ADD_mem[0]
	S += (c_ac_t40*ADD[1]) < c_ac10_mem0*ADD_mem[1]
	S += (c_ac_t40*ADD[2]) < c_ac10_mem0*ADD_mem[2]
	S += (c_ac_t40*ADD[3]) < c_ac10_mem0*ADD_mem[3]
	S += c_ac10_mem0 <= c_ac10

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	c_ac10_mem1 += alt(ADD_mem)
	S += (c_ac_t50*ADD[0]) < c_ac10_mem1*ADD_mem[0]
	S += (c_ac_t50*ADD[1]) < c_ac10_mem1*ADD_mem[1]
	S += (c_ac_t50*ADD[2]) < c_ac10_mem1*ADD_mem[2]
	S += (c_ac_t50*ADD[3]) < c_ac10_mem1*ADD_mem[3]
	S += c_ac10_mem1 <= c_ac10

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-440/scheduling/INV_mul1_add4/INV_4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

