from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 95
	S = Scenario("SQR_0", horizon=horizon)

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
	c_t0_a1__x00 = S.Task('c_t0_a1__x00', length=1, delay_cost=1)
	c_t0_a1__x00 += alt(ADD)

	c_t0_a1__x00_mem0 = S.Task('c_t0_a1__x00_mem0', length=1, delay_cost=1)
	c_t0_a1__x00_mem0 += INPUT_mem_r
	S += c_t0_a1__x00_mem0 <= c_t0_a1__x00

	c_t0_a1__x10 = S.Task('c_t0_a1__x10', length=1, delay_cost=1)
	c_t0_a1__x10 += alt(ADD)

	c_t0_a1__x10_mem0 = S.Task('c_t0_a1__x10_mem0', length=1, delay_cost=1)
	c_t0_a1__x10_mem0 += INPUT_mem_r
	S += c_t0_a1__x10_mem0 <= c_t0_a1__x10

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	c_t0_t10 += alt(ADD)

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	c_t0_t10_mem0 += INPUT_mem_r
	S += c_t0_t10_mem0 <= c_t0_t10

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	c_t0_t10_mem1 += INPUT_mem_r
	S += c_t0_t10_mem1 <= c_t0_t10

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	c_t0_t11 += alt(ADD)

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += INPUT_mem_r
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += INPUT_mem_r
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	c_t0_t3_t0_in += alt(MUL_in)
	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=7, delay_cost=1)
	c_t0_t3_t0 += alt(MUL)
	S += c_t0_t3_t0>=c_t0_t3_t0_in

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	c_t0_t3_t0_mem0 += INPUT_mem_r
	S += c_t0_t3_t0_mem0 <= c_t0_t3_t0

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	c_t0_t3_t0_mem1 += INPUT_mem_r
	S += c_t0_t3_t0_mem1 <= c_t0_t3_t0

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	c_t0_t3_t1_in += alt(MUL_in)
	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=7, delay_cost=1)
	c_t0_t3_t1 += alt(MUL)
	S += c_t0_t3_t1>=c_t0_t3_t1_in

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	c_t0_t3_t1_mem0 += INPUT_mem_r
	S += c_t0_t3_t1_mem0 <= c_t0_t3_t1

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	c_t0_t3_t1_mem1 += INPUT_mem_r
	S += c_t0_t3_t1_mem1 <= c_t0_t3_t1

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	c_t0_t3_t2 += alt(ADD)

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	c_t0_t3_t2_mem0 += INPUT_mem_r
	S += c_t0_t3_t2_mem0 <= c_t0_t3_t2

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	c_t0_t3_t2_mem1 += INPUT_mem_r
	S += c_t0_t3_t2_mem1 <= c_t0_t3_t2

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	c_t0_t3_t3 += alt(ADD)

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	c_t0_t3_t3_mem0 += INPUT_mem_r
	S += c_t0_t3_t3_mem0 <= c_t0_t3_t3

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	c_t0_t3_t3_mem1 += INPUT_mem_r
	S += c_t0_t3_t3_mem1 <= c_t0_t3_t3

	c_t1_a1__x00 = S.Task('c_t1_a1__x00', length=1, delay_cost=1)
	c_t1_a1__x00 += alt(ADD)

	c_t1_a1__x00_mem0 = S.Task('c_t1_a1__x00_mem0', length=1, delay_cost=1)
	c_t1_a1__x00_mem0 += INPUT_mem_r
	S += c_t1_a1__x00_mem0 <= c_t1_a1__x00

	c_t1_a1__x10 = S.Task('c_t1_a1__x10', length=1, delay_cost=1)
	c_t1_a1__x10 += alt(ADD)

	c_t1_a1__x10_mem0 = S.Task('c_t1_a1__x10_mem0', length=1, delay_cost=1)
	c_t1_a1__x10_mem0 += INPUT_mem_r
	S += c_t1_a1__x10_mem0 <= c_t1_a1__x10

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	c_t1_t10 += alt(ADD)

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	c_t1_t10_mem0 += INPUT_mem_r
	S += c_t1_t10_mem0 <= c_t1_t10

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	c_t1_t10_mem1 += INPUT_mem_r
	S += c_t1_t10_mem1 <= c_t1_t10

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	c_t1_t11 += alt(ADD)

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += INPUT_mem_r
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += INPUT_mem_r
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	c_t1_t3_t0_in += alt(MUL_in)
	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=7, delay_cost=1)
	c_t1_t3_t0 += alt(MUL)
	S += c_t1_t3_t0>=c_t1_t3_t0_in

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	c_t1_t3_t0_mem0 += INPUT_mem_r
	S += c_t1_t3_t0_mem0 <= c_t1_t3_t0

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	c_t1_t3_t0_mem1 += INPUT_mem_r
	S += c_t1_t3_t0_mem1 <= c_t1_t3_t0

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	c_t1_t3_t1_in += alt(MUL_in)
	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=7, delay_cost=1)
	c_t1_t3_t1 += alt(MUL)
	S += c_t1_t3_t1>=c_t1_t3_t1_in

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	c_t1_t3_t1_mem0 += INPUT_mem_r
	S += c_t1_t3_t1_mem0 <= c_t1_t3_t1

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	c_t1_t3_t1_mem1 += INPUT_mem_r
	S += c_t1_t3_t1_mem1 <= c_t1_t3_t1

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	c_t1_t3_t2 += alt(ADD)

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	c_t1_t3_t2_mem0 += INPUT_mem_r
	S += c_t1_t3_t2_mem0 <= c_t1_t3_t2

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	c_t1_t3_t2_mem1 += INPUT_mem_r
	S += c_t1_t3_t2_mem1 <= c_t1_t3_t2

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	c_t1_t3_t3 += alt(ADD)

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	c_t1_t3_t3_mem0 += INPUT_mem_r
	S += c_t1_t3_t3_mem0 <= c_t1_t3_t3

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	c_t1_t3_t3_mem1 += INPUT_mem_r
	S += c_t1_t3_t3_mem1 <= c_t1_t3_t3

	c_t2_a1__x00 = S.Task('c_t2_a1__x00', length=1, delay_cost=1)
	c_t2_a1__x00 += alt(ADD)

	c_t2_a1__x00_mem0 = S.Task('c_t2_a1__x00_mem0', length=1, delay_cost=1)
	c_t2_a1__x00_mem0 += INPUT_mem_r
	S += c_t2_a1__x00_mem0 <= c_t2_a1__x00

	c_t2_a1__x10 = S.Task('c_t2_a1__x10', length=1, delay_cost=1)
	c_t2_a1__x10 += alt(ADD)

	c_t2_a1__x10_mem0 = S.Task('c_t2_a1__x10_mem0', length=1, delay_cost=1)
	c_t2_a1__x10_mem0 += INPUT_mem_r
	S += c_t2_a1__x10_mem0 <= c_t2_a1__x10

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	c_t2_t10 += alt(ADD)

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	c_t2_t10_mem0 += INPUT_mem_r
	S += c_t2_t10_mem0 <= c_t2_t10

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	c_t2_t10_mem1 += INPUT_mem_r
	S += c_t2_t10_mem1 <= c_t2_t10

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	c_t2_t11 += alt(ADD)

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += INPUT_mem_r
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += INPUT_mem_r
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	c_t2_t3_t0_in += alt(MUL_in)
	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=7, delay_cost=1)
	c_t2_t3_t0 += alt(MUL)
	S += c_t2_t3_t0>=c_t2_t3_t0_in

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	c_t2_t3_t0_mem0 += INPUT_mem_r
	S += c_t2_t3_t0_mem0 <= c_t2_t3_t0

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	c_t2_t3_t0_mem1 += INPUT_mem_r
	S += c_t2_t3_t0_mem1 <= c_t2_t3_t0

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	c_t2_t3_t1_in += alt(MUL_in)
	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=7, delay_cost=1)
	c_t2_t3_t1 += alt(MUL)
	S += c_t2_t3_t1>=c_t2_t3_t1_in

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	c_t2_t3_t1_mem0 += INPUT_mem_r
	S += c_t2_t3_t1_mem0 <= c_t2_t3_t1

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	c_t2_t3_t1_mem1 += INPUT_mem_r
	S += c_t2_t3_t1_mem1 <= c_t2_t3_t1

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	c_t2_t3_t2 += alt(ADD)

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	c_t2_t3_t2_mem0 += INPUT_mem_r
	S += c_t2_t3_t2_mem0 <= c_t2_t3_t2

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	c_t2_t3_t2_mem1 += INPUT_mem_r
	S += c_t2_t3_t2_mem1 <= c_t2_t3_t2

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	c_t2_t3_t3 += alt(ADD)

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	c_t2_t3_t3_mem0 += INPUT_mem_r
	S += c_t2_t3_t3_mem0 <= c_t2_t3_t3

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	c_t2_t3_t3_mem1 += INPUT_mem_r
	S += c_t2_t3_t3_mem1 <= c_t2_t3_t3

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	c_t3000 += alt(ADD)

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += INPUT_mem_r
	S += c_t3000_mem0 <= c_t3000

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += INPUT_mem_r
	S += c_t3000_mem1 <= c_t3000

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	c_t3001 += alt(ADD)

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += INPUT_mem_r
	S += c_t3001_mem0 <= c_t3001

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += INPUT_mem_r
	S += c_t3001_mem1 <= c_t3001

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	c_t3010 += alt(ADD)

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += INPUT_mem_r
	S += c_t3010_mem0 <= c_t3010

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += INPUT_mem_r
	S += c_t3010_mem1 <= c_t3010

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	c_t3011 += alt(ADD)

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += INPUT_mem_r
	S += c_t3011_mem0 <= c_t3011

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += INPUT_mem_r
	S += c_t3011_mem1 <= c_t3011

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	c_t4000 += alt(ADD)

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += INPUT_mem_r
	S += c_t4000_mem0 <= c_t4000

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += INPUT_mem_r
	S += c_t4000_mem1 <= c_t4000

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	c_t4001 += alt(ADD)

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	c_t4001_mem0 += INPUT_mem_r
	S += c_t4001_mem0 <= c_t4001

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	c_t4001_mem1 += INPUT_mem_r
	S += c_t4001_mem1 <= c_t4001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls12-1150/scheduling/SQR_mul1_add4/SQR_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

