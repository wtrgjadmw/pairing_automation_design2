from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("SQR012345_0", horizon=horizon)

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
	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	t0_t0 += alt(ADD)

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	t0_t0_mem0 += INPUT_mem_r
	S += t0_t0_mem0 <= t0_t0

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	t0_t0_mem1 += INPUT_mem_r
	S += t0_t0_mem1 <= t0_t0

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	t0_t1 += alt(ADD)

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	t0_t1_mem0 += INPUT_mem_r
	S += t0_t1_mem0 <= t0_t1

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	t0_t1_mem1 += INPUT_mem_r
	S += t0_t1_mem1 <= t0_t1

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	t0_t3_in += alt(MUL_in)
	t0_t3 = S.Task('t0_t3', length=7, delay_cost=1)
	t0_t3 += alt(MUL)
	S += t0_t3>=t0_t3_in

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	t0_t3_mem0 += INPUT_mem_r
	S += t0_t3_mem0 <= t0_t3

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	t0_t3_mem1 += INPUT_mem_r
	S += t0_t3_mem1 <= t0_t3

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(ADD)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += INPUT_mem_r
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += INPUT_mem_r
	S += t10_mem1 <= t10

	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(ADD)

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += INPUT_mem_r
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += INPUT_mem_r
	S += t11_mem1 <= t11

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	t3_t0_in += alt(MUL_in)
	t3_t0 = S.Task('t3_t0', length=7, delay_cost=1)
	t3_t0 += alt(MUL)
	S += t3_t0>=t3_t0_in

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	t3_t0_mem0 += INPUT_mem_r
	S += t3_t0_mem0 <= t3_t0

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	t3_t0_mem1 += INPUT_mem_r
	S += t3_t0_mem1 <= t3_t0

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	t3_t1_in += alt(MUL_in)
	t3_t1 = S.Task('t3_t1', length=7, delay_cost=1)
	t3_t1 += alt(MUL)
	S += t3_t1>=t3_t1_in

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	t3_t1_mem0 += INPUT_mem_r
	S += t3_t1_mem0 <= t3_t1

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	t3_t1_mem1 += INPUT_mem_r
	S += t3_t1_mem1 <= t3_t1

	t3_t2 = S.Task('t3_t2', length=1, delay_cost=1)
	t3_t2 += alt(ADD)

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	t3_t2_mem0 += INPUT_mem_r
	S += t3_t2_mem0 <= t3_t2

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	t3_t2_mem1 += INPUT_mem_r
	S += t3_t2_mem1 <= t3_t2

	t3_t3 = S.Task('t3_t3', length=1, delay_cost=1)
	t3_t3 += alt(ADD)

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	t3_t3_mem0 += INPUT_mem_r
	S += t3_t3_mem0 <= t3_t3

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	t3_t3_mem1 += INPUT_mem_r
	S += t3_t3_mem1 <= t3_t3

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	t4_t0 += alt(ADD)

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	t4_t0_mem0 += INPUT_mem_r
	S += t4_t0_mem0 <= t4_t0

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	t4_t0_mem1 += INPUT_mem_r
	S += t4_t0_mem1 <= t4_t0

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	t4_t1 += alt(ADD)

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	t4_t1_mem0 += INPUT_mem_r
	S += t4_t1_mem0 <= t4_t1

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	t4_t1_mem1 += INPUT_mem_r
	S += t4_t1_mem1 <= t4_t1

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	t4_t3_in += alt(MUL_in)
	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	t4_t3 += alt(MUL)
	S += t4_t3>=t4_t3_in

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	t4_t3_mem0 += INPUT_mem_r
	S += t4_t3_mem0 <= t4_t3

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	t4_t3_mem1 += INPUT_mem_r
	S += t4_t3_mem1 <= t4_t3

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	t5_t0_in += alt(MUL_in)
	t5_t0 = S.Task('t5_t0', length=7, delay_cost=1)
	t5_t0 += alt(MUL)
	S += t5_t0>=t5_t0_in

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	t5_t0_mem0 += INPUT_mem_r
	S += t5_t0_mem0 <= t5_t0

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	t5_t0_mem1 += INPUT_mem_r
	S += t5_t0_mem1 <= t5_t0

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	t5_t1_in += alt(MUL_in)
	t5_t1 = S.Task('t5_t1', length=7, delay_cost=1)
	t5_t1 += alt(MUL)
	S += t5_t1>=t5_t1_in

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	t5_t1_mem0 += INPUT_mem_r
	S += t5_t1_mem0 <= t5_t1

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	t5_t1_mem1 += INPUT_mem_r
	S += t5_t1_mem1 <= t5_t1

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	t5_t2 += alt(ADD)

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	t5_t2_mem0 += INPUT_mem_r
	S += t5_t2_mem0 <= t5_t2

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	t5_t2_mem1 += INPUT_mem_r
	S += t5_t2_mem1 <= t5_t2

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	t5_t3 += alt(ADD)

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	t5_t3_mem0 += INPUT_mem_r
	S += t5_t3_mem0 <= t5_t3

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	t5_t3_mem1 += INPUT_mem_r
	S += t5_t3_mem1 <= t5_t3

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	t6_t0_in += alt(MUL_in)
	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	t6_t0 += alt(MUL)
	S += t6_t0>=t6_t0_in

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	t6_t0_mem0 += INPUT_mem_r
	S += t6_t0_mem0 <= t6_t0

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	t6_t0_mem1 += INPUT_mem_r
	S += t6_t0_mem1 <= t6_t0

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	t6_t1_in += alt(MUL_in)
	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	t6_t1 += alt(MUL)
	S += t6_t1>=t6_t1_in

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	t6_t1_mem0 += INPUT_mem_r
	S += t6_t1_mem0 <= t6_t1

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	t6_t1_mem1 += INPUT_mem_r
	S += t6_t1_mem1 <= t6_t1

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	t6_t2 += alt(ADD)

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	t6_t2_mem0 += INPUT_mem_r
	S += t6_t2_mem0 <= t6_t2

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	t6_t2_mem1 += INPUT_mem_r
	S += t6_t2_mem1 <= t6_t2

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	t6_t3 += alt(ADD)

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	t6_t3_mem0 += INPUT_mem_r
	S += t6_t3_mem0 <= t6_t3

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	t6_t3_mem1 += INPUT_mem_r
	S += t6_t3_mem1 <= t6_t3

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	t7_t0_in += alt(MUL_in)
	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	t7_t0 += alt(MUL)
	S += t7_t0>=t7_t0_in

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	t7_t0_mem0 += INPUT_mem_r
	S += t7_t0_mem0 <= t7_t0

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	t7_t0_mem1 += INPUT_mem_r
	S += t7_t0_mem1 <= t7_t0

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	t7_t1_in += alt(MUL_in)
	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	t7_t1 += alt(MUL)
	S += t7_t1>=t7_t1_in

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	t7_t1_mem0 += INPUT_mem_r
	S += t7_t1_mem0 <= t7_t1

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	t7_t1_mem1 += INPUT_mem_r
	S += t7_t1_mem1 <= t7_t1

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	t7_t2 += alt(ADD)

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	t7_t2_mem0 += INPUT_mem_r
	S += t7_t2_mem0 <= t7_t2

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	t7_t2_mem1 += INPUT_mem_r
	S += t7_t2_mem1 <= t7_t2

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	t7_t3 += alt(ADD)

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	t7_t3_mem0 += INPUT_mem_r
	S += t7_t3_mem0 <= t7_t3

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	t7_t3_mem1 += INPUT_mem_r
	S += t7_t3_mem1 <= t7_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-381/scheduling/SQR012345_mul1_add4/SQR012345_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

