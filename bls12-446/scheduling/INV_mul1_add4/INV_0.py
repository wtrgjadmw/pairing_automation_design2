from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 131
	S = Scenario("INV_0", horizon=horizon)

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

	# new tasks
	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	c_aa_a1_0 += alt(ADD)

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	c_aa_a1_0_mem0 += INPUT_mem_r
	S += c_aa_a1_0_mem0 <= c_aa_a1_0

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	c_aa_a1_0_mem1 += INPUT_mem_r
	S += c_aa_a1_0_mem1 <= c_aa_a1_0

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	c_aa_a1_1 += alt(ADD)

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	c_aa_a1_1_mem0 += INPUT_mem_r
	S += c_aa_a1_1_mem0 <= c_aa_a1_1

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	c_aa_a1_1_mem1 += INPUT_mem_r
	S += c_aa_a1_1_mem1 <= c_aa_a1_1

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	c_aa_t10 += alt(ADD)

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	c_aa_t10_mem0 += INPUT_mem_r
	S += c_aa_t10_mem0 <= c_aa_t10

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	c_aa_t10_mem1 += INPUT_mem_r
	S += c_aa_t10_mem1 <= c_aa_t10

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	c_aa_t11 += alt(ADD)

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	c_aa_t11_mem0 += INPUT_mem_r
	S += c_aa_t11_mem0 <= c_aa_t11

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	c_aa_t11_mem1 += INPUT_mem_r
	S += c_aa_t11_mem1 <= c_aa_t11

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	c_aa_t3_t0_in += alt(MUL_in)
	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=7, delay_cost=1)
	c_aa_t3_t0 += alt(MUL)
	S += c_aa_t3_t0>=c_aa_t3_t0_in

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	c_aa_t3_t0_mem0 += INPUT_mem_r
	S += c_aa_t3_t0_mem0 <= c_aa_t3_t0

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	c_aa_t3_t0_mem1 += INPUT_mem_r
	S += c_aa_t3_t0_mem1 <= c_aa_t3_t0

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	c_aa_t3_t1_in += alt(MUL_in)
	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=7, delay_cost=1)
	c_aa_t3_t1 += alt(MUL)
	S += c_aa_t3_t1>=c_aa_t3_t1_in

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	c_aa_t3_t1_mem0 += INPUT_mem_r
	S += c_aa_t3_t1_mem0 <= c_aa_t3_t1

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	c_aa_t3_t1_mem1 += INPUT_mem_r
	S += c_aa_t3_t1_mem1 <= c_aa_t3_t1

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	c_aa_t3_t2 += alt(ADD)

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	c_aa_t3_t2_mem0 += INPUT_mem_r
	S += c_aa_t3_t2_mem0 <= c_aa_t3_t2

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	c_aa_t3_t2_mem1 += INPUT_mem_r
	S += c_aa_t3_t2_mem1 <= c_aa_t3_t2

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	c_aa_t3_t3 += alt(ADD)

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	c_aa_t3_t3_mem0 += INPUT_mem_r
	S += c_aa_t3_t3_mem0 <= c_aa_t3_t3

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	c_aa_t3_t3_mem1 += INPUT_mem_r
	S += c_aa_t3_t3_mem1 <= c_aa_t3_t3

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	c_bb_a1_0 += alt(ADD)

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	c_bb_a1_0_mem0 += INPUT_mem_r
	S += c_bb_a1_0_mem0 <= c_bb_a1_0

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	c_bb_a1_0_mem1 += INPUT_mem_r
	S += c_bb_a1_0_mem1 <= c_bb_a1_0

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	c_bb_a1_1 += alt(ADD)

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	c_bb_a1_1_mem0 += INPUT_mem_r
	S += c_bb_a1_1_mem0 <= c_bb_a1_1

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	c_bb_a1_1_mem1 += INPUT_mem_r
	S += c_bb_a1_1_mem1 <= c_bb_a1_1

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	c_bb_t10 += alt(ADD)

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	c_bb_t10_mem0 += INPUT_mem_r
	S += c_bb_t10_mem0 <= c_bb_t10

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	c_bb_t10_mem1 += INPUT_mem_r
	S += c_bb_t10_mem1 <= c_bb_t10

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	c_bb_t11 += alt(ADD)

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	c_bb_t11_mem0 += INPUT_mem_r
	S += c_bb_t11_mem0 <= c_bb_t11

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	c_bb_t11_mem1 += INPUT_mem_r
	S += c_bb_t11_mem1 <= c_bb_t11

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	c_bb_t3_t0_in += alt(MUL_in)
	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=7, delay_cost=1)
	c_bb_t3_t0 += alt(MUL)
	S += c_bb_t3_t0>=c_bb_t3_t0_in

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	c_bb_t3_t0_mem0 += INPUT_mem_r
	S += c_bb_t3_t0_mem0 <= c_bb_t3_t0

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	c_bb_t3_t0_mem1 += INPUT_mem_r
	S += c_bb_t3_t0_mem1 <= c_bb_t3_t0

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	c_bb_t3_t1_in += alt(MUL_in)
	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=7, delay_cost=1)
	c_bb_t3_t1 += alt(MUL)
	S += c_bb_t3_t1>=c_bb_t3_t1_in

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	c_bb_t3_t1_mem0 += INPUT_mem_r
	S += c_bb_t3_t1_mem0 <= c_bb_t3_t1

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	c_bb_t3_t1_mem1 += INPUT_mem_r
	S += c_bb_t3_t1_mem1 <= c_bb_t3_t1

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	c_bb_t3_t2 += alt(ADD)

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	c_bb_t3_t2_mem0 += INPUT_mem_r
	S += c_bb_t3_t2_mem0 <= c_bb_t3_t2

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	c_bb_t3_t2_mem1 += INPUT_mem_r
	S += c_bb_t3_t2_mem1 <= c_bb_t3_t2

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	c_bb_t3_t3 += alt(ADD)

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	c_bb_t3_t3_mem0 += INPUT_mem_r
	S += c_bb_t3_t3_mem0 <= c_bb_t3_t3

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	c_bb_t3_t3_mem1 += INPUT_mem_r
	S += c_bb_t3_t3_mem1 <= c_bb_t3_t3

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	c_cc_a1_0 += alt(ADD)

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	c_cc_a1_0_mem0 += INPUT_mem_r
	S += c_cc_a1_0_mem0 <= c_cc_a1_0

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	c_cc_a1_0_mem1 += INPUT_mem_r
	S += c_cc_a1_0_mem1 <= c_cc_a1_0

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	c_cc_a1_1 += alt(ADD)

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	c_cc_a1_1_mem0 += INPUT_mem_r
	S += c_cc_a1_1_mem0 <= c_cc_a1_1

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	c_cc_a1_1_mem1 += INPUT_mem_r
	S += c_cc_a1_1_mem1 <= c_cc_a1_1

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	c_cc_t10 += alt(ADD)

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	c_cc_t10_mem0 += INPUT_mem_r
	S += c_cc_t10_mem0 <= c_cc_t10

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	c_cc_t10_mem1 += INPUT_mem_r
	S += c_cc_t10_mem1 <= c_cc_t10

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	c_cc_t11 += alt(ADD)

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	c_cc_t11_mem0 += INPUT_mem_r
	S += c_cc_t11_mem0 <= c_cc_t11

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	c_cc_t11_mem1 += INPUT_mem_r
	S += c_cc_t11_mem1 <= c_cc_t11

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	c_cc_t3_t0_in += alt(MUL_in)
	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=7, delay_cost=1)
	c_cc_t3_t0 += alt(MUL)
	S += c_cc_t3_t0>=c_cc_t3_t0_in

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	c_cc_t3_t0_mem0 += INPUT_mem_r
	S += c_cc_t3_t0_mem0 <= c_cc_t3_t0

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	c_cc_t3_t0_mem1 += INPUT_mem_r
	S += c_cc_t3_t0_mem1 <= c_cc_t3_t0

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	c_cc_t3_t1_in += alt(MUL_in)
	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=7, delay_cost=1)
	c_cc_t3_t1 += alt(MUL)
	S += c_cc_t3_t1>=c_cc_t3_t1_in

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	c_cc_t3_t1_mem0 += INPUT_mem_r
	S += c_cc_t3_t1_mem0 <= c_cc_t3_t1

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	c_cc_t3_t1_mem1 += INPUT_mem_r
	S += c_cc_t3_t1_mem1 <= c_cc_t3_t1

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	c_cc_t3_t2 += alt(ADD)

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	c_cc_t3_t2_mem0 += INPUT_mem_r
	S += c_cc_t3_t2_mem0 <= c_cc_t3_t2

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	c_cc_t3_t2_mem1 += INPUT_mem_r
	S += c_cc_t3_t2_mem1 <= c_cc_t3_t2

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	c_cc_t3_t3 += alt(ADD)

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	c_cc_t3_t3_mem0 += INPUT_mem_r
	S += c_cc_t3_t3_mem0 <= c_cc_t3_t3

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	c_cc_t3_t3_mem1 += INPUT_mem_r
	S += c_cc_t3_t3_mem1 <= c_cc_t3_t3

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	c_ab_t0_t0_in += alt(MUL_in)
	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=7, delay_cost=1)
	c_ab_t0_t0 += alt(MUL)
	S += c_ab_t0_t0>=c_ab_t0_t0_in

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	c_ab_t0_t0_mem0 += INPUT_mem_r
	S += c_ab_t0_t0_mem0 <= c_ab_t0_t0

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	c_ab_t0_t0_mem1 += INPUT_mem_r
	S += c_ab_t0_t0_mem1 <= c_ab_t0_t0

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	c_ab_t0_t1_in += alt(MUL_in)
	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=7, delay_cost=1)
	c_ab_t0_t1 += alt(MUL)
	S += c_ab_t0_t1>=c_ab_t0_t1_in

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	c_ab_t0_t1_mem0 += INPUT_mem_r
	S += c_ab_t0_t1_mem0 <= c_ab_t0_t1

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	c_ab_t0_t1_mem1 += INPUT_mem_r
	S += c_ab_t0_t1_mem1 <= c_ab_t0_t1

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	c_ab_t0_t2 += alt(ADD)

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	c_ab_t0_t2_mem0 += INPUT_mem_r
	S += c_ab_t0_t2_mem0 <= c_ab_t0_t2

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	c_ab_t0_t2_mem1 += INPUT_mem_r
	S += c_ab_t0_t2_mem1 <= c_ab_t0_t2

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	c_ab_t0_t3 += alt(ADD)

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	c_ab_t0_t3_mem0 += INPUT_mem_r
	S += c_ab_t0_t3_mem0 <= c_ab_t0_t3

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	c_ab_t0_t3_mem1 += INPUT_mem_r
	S += c_ab_t0_t3_mem1 <= c_ab_t0_t3

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	c_ab_t1_t0_in += alt(MUL_in)
	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=7, delay_cost=1)
	c_ab_t1_t0 += alt(MUL)
	S += c_ab_t1_t0>=c_ab_t1_t0_in

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	c_ab_t1_t0_mem0 += INPUT_mem_r
	S += c_ab_t1_t0_mem0 <= c_ab_t1_t0

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	c_ab_t1_t0_mem1 += INPUT_mem_r
	S += c_ab_t1_t0_mem1 <= c_ab_t1_t0

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	c_ab_t1_t1_in += alt(MUL_in)
	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=7, delay_cost=1)
	c_ab_t1_t1 += alt(MUL)
	S += c_ab_t1_t1>=c_ab_t1_t1_in

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	c_ab_t1_t1_mem0 += INPUT_mem_r
	S += c_ab_t1_t1_mem0 <= c_ab_t1_t1

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	c_ab_t1_t1_mem1 += INPUT_mem_r
	S += c_ab_t1_t1_mem1 <= c_ab_t1_t1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-446/scheduling/INV_mul1_add4/INV_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

