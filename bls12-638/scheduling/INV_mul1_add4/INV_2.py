from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 151
	S = Scenario("INV_2", horizon=horizon)

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

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=7, delay_cost=1)
	S += c_aa_t3_t0 >= 10
	c_aa_t3_t0 += MUL[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 10
	c_ab_t0_t2_mem0 += INPUT_mem_r

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 10
	c_ab_t0_t2_mem1 += INPUT_mem_r

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 11
	c_ab_t0_t2 += ADD[3]

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

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 12
	c_cc_t3_t3 += ADD[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 13
	c_aa_t3_t3 += ADD[1]

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

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 14
	c_cc_t3_t2 += ADD[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 15
	c_aa_a1_0 += ADD[2]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 15
	c_bb_a1_0_mem0 += INPUT_mem_r

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 15
	c_bb_a1_0_mem1 += INPUT_mem_r

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 16
	c_ab_t0_t3_mem0 += INPUT_mem_r

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 16
	c_ab_t0_t3_mem1 += INPUT_mem_r

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 16
	c_bb_a1_0 += ADD[0]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 17
	c_ab_t0_t3 += ADD[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 17
	c_bb_a1_1_mem0 += INPUT_mem_r

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 17
	c_bb_a1_1_mem1 += INPUT_mem_r

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 18
	c_bb_a1_1 += ADD[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 18
	c_cc_t10_mem0 += INPUT_mem_r

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 18
	c_cc_t10_mem1 += INPUT_mem_r

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 19
	c_cc_a1_1_mem0 += INPUT_mem_r

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 19
	c_cc_a1_1_mem1 += INPUT_mem_r

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 19
	c_cc_t10 += ADD[0]

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

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 23
	c_aa_t10 += ADD[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 23
	c_cc_a1_0_mem0 += INPUT_mem_r

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 23
	c_cc_a1_0_mem1 += INPUT_mem_r

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

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 25
	c_aa_t3_t2 += ADD[2]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 26
	c_aa_a1_1 += ADD[1]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 26
	c_bb_t3_t3_mem0 += INPUT_mem_r

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 26
	c_bb_t3_t3_mem1 += INPUT_mem_r

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

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 30
	c_bb_t10 += ADD[2]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 30
	c_bc_t0_t1_in += MUL_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 30
	c_bc_t0_t1_mem0 += INPUT_mem_r

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 30
	c_bc_t0_t1_mem1 += INPUT_mem_r

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

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 41
	c_ab_t1_t3 += ADD[3]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 41
	c_bc_t0_t2_mem0 += INPUT_mem_r

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 41
	c_bc_t0_t2_mem1 += INPUT_mem_r

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 42
	c_ac_t21_mem0 += INPUT_mem_r

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 42
	c_ac_t21_mem1 += INPUT_mem_r

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 42
	c_bc_t0_t2 += ADD[2]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 43
	c_ac_t1_t3_mem0 += INPUT_mem_r

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 43
	c_ac_t1_t3_mem1 += INPUT_mem_r

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 43
	c_ac_t21 += ADD[0]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 44
	c_ac_t1_t3 += ADD[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 44
	c_ac_t30_mem0 += INPUT_mem_r

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 44
	c_ac_t30_mem1 += INPUT_mem_r

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 45
	c_ac_t0_t3_mem0 += INPUT_mem_r

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 45
	c_ac_t0_t3_mem1 += INPUT_mem_r

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 45
	c_ac_t30 += ADD[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 46
	c_ab_t21_mem0 += INPUT_mem_r

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 46
	c_ab_t21_mem1 += INPUT_mem_r

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 46
	c_ac_t0_t3 += ADD[0]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 47
	c_ab_t21 += ADD[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 47
	c_bc_t31_mem0 += INPUT_mem_r

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 47
	c_bc_t31_mem1 += INPUT_mem_r

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 48
	c_ac_t1_t2_mem0 += INPUT_mem_r

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 48
	c_ac_t1_t2_mem1 += INPUT_mem_r

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 48
	c_bc_t31 += ADD[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	S += c_ac_t1_t2 >= 49
	c_ac_t1_t2 += ADD[3]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 49
	c_ac_t20_mem0 += INPUT_mem_r

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 49
	c_ac_t20_mem1 += INPUT_mem_r

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

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 53
	c_ab_t30 += ADD[2]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 53
	c_ac_t0_t2_mem0 += INPUT_mem_r

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 53
	c_ac_t0_t2_mem1 += INPUT_mem_r

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 54
	c_ac_t0_t2 += ADD[3]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 54
	c_bc_t21_mem0 += INPUT_mem_r

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 54
	c_bc_t21_mem1 += INPUT_mem_r

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 55
	c_ab_t1_t2_mem0 += INPUT_mem_r

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 55
	c_ab_t1_t2_mem1 += INPUT_mem_r

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 55
	c_bc_t21 += ADD[3]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 56
	c_ab_t1_t2 += ADD[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 56
	c_bc_t20_mem0 += INPUT_mem_r

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 56
	c_bc_t20_mem1 += INPUT_mem_r

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 57
	c_bc_t1_t3_mem0 += INPUT_mem_r

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 57
	c_bc_t1_t3_mem1 += INPUT_mem_r

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 57
	c_bc_t20 += ADD[2]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 58
	c_bc_t1_t2_mem0 += INPUT_mem_r

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 58
	c_bc_t1_t2_mem1 += INPUT_mem_r

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 58
	c_bc_t1_t3 += ADD[2]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 59
	c_bc_t0_t3_mem0 += INPUT_mem_r

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 59
	c_bc_t0_t3_mem1 += INPUT_mem_r

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 59
	c_bc_t1_t2 += ADD[0]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 60
	c_bc_t0_t3 += ADD[3]


	# new tasks
	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	c_pbc_t0_t3 += alt(ADD)

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	c_pbc_t0_t3_mem0 += INPUT_mem_r
	S += c_pbc_t0_t3_mem0 <= c_pbc_t0_t3

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	c_pbc_t0_t3_mem1 += INPUT_mem_r
	S += c_pbc_t0_t3_mem1 <= c_pbc_t0_t3

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	c_pbc_t1_t3 += alt(ADD)

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	c_pbc_t1_t3_mem0 += INPUT_mem_r
	S += c_pbc_t1_t3_mem0 <= c_pbc_t1_t3

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	c_pbc_t1_t3_mem1 += INPUT_mem_r
	S += c_pbc_t1_t3_mem1 <= c_pbc_t1_t3

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	c_pbc_t30 += alt(ADD)

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	c_pbc_t30_mem0 += INPUT_mem_r
	S += c_pbc_t30_mem0 <= c_pbc_t30

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	c_pbc_t30_mem1 += INPUT_mem_r
	S += c_pbc_t30_mem1 <= c_pbc_t30

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	c_pbc_t31 += alt(ADD)

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	c_pbc_t31_mem0 += INPUT_mem_r
	S += c_pbc_t31_mem0 <= c_pbc_t31

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	c_pbc_t31_mem1 += INPUT_mem_r
	S += c_pbc_t31_mem1 <= c_pbc_t31

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	c_pcb_t0_t3 += alt(ADD)

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	c_pcb_t0_t3_mem0 += INPUT_mem_r
	S += c_pcb_t0_t3_mem0 <= c_pcb_t0_t3

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	c_pcb_t0_t3_mem1 += INPUT_mem_r
	S += c_pcb_t0_t3_mem1 <= c_pcb_t0_t3

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	c_pcb_t1_t3 += alt(ADD)

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	c_pcb_t1_t3_mem0 += INPUT_mem_r
	S += c_pcb_t1_t3_mem0 <= c_pcb_t1_t3

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	c_pcb_t1_t3_mem1 += INPUT_mem_r
	S += c_pcb_t1_t3_mem1 <= c_pcb_t1_t3

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	c_pcb_t30 += alt(ADD)

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	c_pcb_t30_mem0 += INPUT_mem_r
	S += c_pcb_t30_mem0 <= c_pcb_t30

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	c_pcb_t30_mem1 += INPUT_mem_r
	S += c_pcb_t30_mem1 <= c_pcb_t30

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	c_pcb_t31 += alt(ADD)

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	c_pcb_t31_mem0 += INPUT_mem_r
	S += c_pcb_t31_mem0 <= c_pcb_t31

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	c_pcb_t31_mem1 += INPUT_mem_r
	S += c_pcb_t31_mem1 <= c_pcb_t31

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	c_paa_t0_t3 += alt(ADD)

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	c_paa_t0_t3_mem0 += INPUT_mem_r
	S += c_paa_t0_t3_mem0 <= c_paa_t0_t3

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	c_paa_t0_t3_mem1 += INPUT_mem_r
	S += c_paa_t0_t3_mem1 <= c_paa_t0_t3

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	c_paa_t1_t3 += alt(ADD)

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	c_paa_t1_t3_mem0 += INPUT_mem_r
	S += c_paa_t1_t3_mem0 <= c_paa_t1_t3

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	c_paa_t1_t3_mem1 += INPUT_mem_r
	S += c_paa_t1_t3_mem1 <= c_paa_t1_t3

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	c_paa_t30 += alt(ADD)

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	c_paa_t30_mem0 += INPUT_mem_r
	S += c_paa_t30_mem0 <= c_paa_t30

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	c_paa_t30_mem1 += INPUT_mem_r
	S += c_paa_t30_mem1 <= c_paa_t30

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	c_paa_t31 += alt(ADD)

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	c_paa_t31_mem0 += INPUT_mem_r
	S += c_paa_t31_mem0 <= c_paa_t31

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	c_paa_t31_mem1 += INPUT_mem_r
	S += c_paa_t31_mem1 <= c_paa_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-638/scheduling/INV_mul1_add4/INV_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

