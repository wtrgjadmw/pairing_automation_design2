from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("FROB_0", horizon=horizon)

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
	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	c10_t0_in += alt(MUL_in)
	c10_t0 = S.Task('c10_t0', length=7, delay_cost=1)
	c10_t0 += alt(MUL)
	S += c10_t0>=c10_t0_in

	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	c10_t0_mem0 += INPUT_mem_r
	S += c10_t0_mem0 <= c10_t0

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	c10_t0_mem1 += INPUT_mem_r
	S += c10_t0_mem1 <= c10_t0

	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	c10_t1_in += alt(MUL_in)
	c10_t1 = S.Task('c10_t1', length=7, delay_cost=1)
	c10_t1 += alt(MUL)
	S += c10_t1>=c10_t1_in

	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	c10_t1_mem0 += INPUT_mem_r
	S += c10_t1_mem0 <= c10_t1

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	c10_t1_mem1 += INPUT_mem_r
	S += c10_t1_mem1 <= c10_t1

	c10_t2 = S.Task('c10_t2', length=1, delay_cost=1)
	c10_t2 += alt(ADD)

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	c10_t2_mem0 += INPUT_mem_r
	S += c10_t2_mem0 <= c10_t2

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	c10_t2_mem1 += INPUT_mem_r
	S += c10_t2_mem1 <= c10_t2

	c10_t3 = S.Task('c10_t3', length=1, delay_cost=1)
	c10_t3 += alt(ADD)

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	c10_t3_mem0 += INPUT_mem_r
	S += c10_t3_mem0 <= c10_t3

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	c10_t3_mem1 += INPUT_mem_r
	S += c10_t3_mem1 <= c10_t3

	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	c20_t0_in += alt(MUL_in)
	c20_t0 = S.Task('c20_t0', length=7, delay_cost=1)
	c20_t0 += alt(MUL)
	S += c20_t0>=c20_t0_in

	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	c20_t0_mem0 += INPUT_mem_r
	S += c20_t0_mem0 <= c20_t0

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	c20_t0_mem1 += INPUT_mem_r
	S += c20_t0_mem1 <= c20_t0

	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	c20_t1_in += alt(MUL_in)
	c20_t1 = S.Task('c20_t1', length=7, delay_cost=1)
	c20_t1 += alt(MUL)
	S += c20_t1>=c20_t1_in

	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	c20_t1_mem0 += INPUT_mem_r
	S += c20_t1_mem0 <= c20_t1

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	c20_t1_mem1 += INPUT_mem_r
	S += c20_t1_mem1 <= c20_t1

	c20_t2 = S.Task('c20_t2', length=1, delay_cost=1)
	c20_t2 += alt(ADD)

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	c20_t2_mem0 += INPUT_mem_r
	S += c20_t2_mem0 <= c20_t2

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	c20_t2_mem1 += INPUT_mem_r
	S += c20_t2_mem1 <= c20_t2

	c20_t3 = S.Task('c20_t3', length=1, delay_cost=1)
	c20_t3 += alt(ADD)

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	c20_t3_mem0 += INPUT_mem_r
	S += c20_t3_mem0 <= c20_t3

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	c20_t3_mem1 += INPUT_mem_r
	S += c20_t3_mem1 <= c20_t3

	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	c01_t0_in += alt(MUL_in)
	c01_t0 = S.Task('c01_t0', length=7, delay_cost=1)
	c01_t0 += alt(MUL)
	S += c01_t0>=c01_t0_in

	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	c01_t0_mem0 += INPUT_mem_r
	S += c01_t0_mem0 <= c01_t0

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	c01_t0_mem1 += INPUT_mem_r
	S += c01_t0_mem1 <= c01_t0

	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	c01_t1_in += alt(MUL_in)
	c01_t1 = S.Task('c01_t1', length=7, delay_cost=1)
	c01_t1 += alt(MUL)
	S += c01_t1>=c01_t1_in

	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	c01_t1_mem0 += INPUT_mem_r
	S += c01_t1_mem0 <= c01_t1

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	c01_t1_mem1 += INPUT_mem_r
	S += c01_t1_mem1 <= c01_t1

	c01_t2 = S.Task('c01_t2', length=1, delay_cost=1)
	c01_t2 += alt(ADD)

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	c01_t2_mem0 += INPUT_mem_r
	S += c01_t2_mem0 <= c01_t2

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	c01_t2_mem1 += INPUT_mem_r
	S += c01_t2_mem1 <= c01_t2

	c01_t3 = S.Task('c01_t3', length=1, delay_cost=1)
	c01_t3 += alt(ADD)

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	c01_t3_mem0 += INPUT_mem_r
	S += c01_t3_mem0 <= c01_t3

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	c01_t3_mem1 += INPUT_mem_r
	S += c01_t3_mem1 <= c01_t3

	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	c11_t0_in += alt(MUL_in)
	c11_t0 = S.Task('c11_t0', length=7, delay_cost=1)
	c11_t0 += alt(MUL)
	S += c11_t0>=c11_t0_in

	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	c11_t0_mem0 += INPUT_mem_r
	S += c11_t0_mem0 <= c11_t0

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	c11_t0_mem1 += INPUT_mem_r
	S += c11_t0_mem1 <= c11_t0

	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	c11_t1_in += alt(MUL_in)
	c11_t1 = S.Task('c11_t1', length=7, delay_cost=1)
	c11_t1 += alt(MUL)
	S += c11_t1>=c11_t1_in

	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	c11_t1_mem0 += INPUT_mem_r
	S += c11_t1_mem0 <= c11_t1

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	c11_t1_mem1 += INPUT_mem_r
	S += c11_t1_mem1 <= c11_t1

	c11_t2 = S.Task('c11_t2', length=1, delay_cost=1)
	c11_t2 += alt(ADD)

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	c11_t2_mem0 += INPUT_mem_r
	S += c11_t2_mem0 <= c11_t2

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	c11_t2_mem1 += INPUT_mem_r
	S += c11_t2_mem1 <= c11_t2

	c11_t3 = S.Task('c11_t3', length=1, delay_cost=1)
	c11_t3 += alt(ADD)

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	c11_t3_mem0 += INPUT_mem_r
	S += c11_t3_mem0 <= c11_t3

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	c11_t3_mem1 += INPUT_mem_r
	S += c11_t3_mem1 <= c11_t3

	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	c21_t0_in += alt(MUL_in)
	c21_t0 = S.Task('c21_t0', length=7, delay_cost=1)
	c21_t0 += alt(MUL)
	S += c21_t0>=c21_t0_in

	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	c21_t0_mem0 += INPUT_mem_r
	S += c21_t0_mem0 <= c21_t0

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	c21_t0_mem1 += INPUT_mem_r
	S += c21_t0_mem1 <= c21_t0

	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	c21_t1_in += alt(MUL_in)
	c21_t1 = S.Task('c21_t1', length=7, delay_cost=1)
	c21_t1 += alt(MUL)
	S += c21_t1>=c21_t1_in

	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	c21_t1_mem0 += INPUT_mem_r
	S += c21_t1_mem0 <= c21_t1

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	c21_t1_mem1 += INPUT_mem_r
	S += c21_t1_mem1 <= c21_t1

	c21_t2 = S.Task('c21_t2', length=1, delay_cost=1)
	c21_t2 += alt(ADD)

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	c21_t2_mem0 += INPUT_mem_r
	S += c21_t2_mem0 <= c21_t2

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	c21_t2_mem1 += INPUT_mem_r
	S += c21_t2_mem1 <= c21_t2

	c21_t3 = S.Task('c21_t3', length=1, delay_cost=1)
	c21_t3 += alt(ADD)

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	c21_t3_mem0 += INPUT_mem_r
	S += c21_t3_mem0 <= c21_t3

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	c21_t3_mem1 += INPUT_mem_r
	S += c21_t3_mem1 <= c21_t3

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(ADD)

	S += 0<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += INPUT_mem_r
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += INPUT_mem_r
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(INPUT_mem_w)
	S += c000 <= c000_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(ADD)

	S += 0<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += INPUT_mem_r
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += INPUT_mem_r
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(INPUT_mem_w)
	S += c001 <= c001_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-1150/scheduling/FROB_mul1_add4/FROB_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

