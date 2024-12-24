from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("CONJ_0", horizon=horizon)

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

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(ADD)

	S += 0<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += INPUT_mem_r
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += INPUT_mem_r
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010 <= c010_w

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(ADD)

	S += 0<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += INPUT_mem_r
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += INPUT_mem_r
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(INPUT_mem_w)
	S += c011 <= c011_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(ADD)

	S += 0<c100

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += INPUT_mem_r
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += INPUT_mem_r
	S += c100_mem1 <= c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(INPUT_mem_w)
	S += c100 <= c100_w

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(ADD)

	S += 0<c101

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += INPUT_mem_r
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += INPUT_mem_r
	S += c101_mem1 <= c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(INPUT_mem_w)
	S += c101 <= c101_w

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(ADD)

	S += 0<c110

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += INPUT_mem_r
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += INPUT_mem_r
	S += c110_mem1 <= c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(INPUT_mem_w)
	S += c110 <= c110_w

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(ADD)

	S += 0<c111

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += INPUT_mem_r
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += INPUT_mem_r
	S += c111_mem1 <= c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(INPUT_mem_w)
	S += c111 <= c111_w

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(ADD)

	S += 0<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += INPUT_mem_r
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += INPUT_mem_r
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200 <= c200_w

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(ADD)

	S += 0<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += INPUT_mem_r
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += INPUT_mem_r
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201 <= c201_w

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(ADD)

	S += 0<c210

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += INPUT_mem_r
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += INPUT_mem_r
	S += c210_mem1 <= c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(INPUT_mem_w)
	S += c210 <= c210_w

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(ADD)

	S += 0<c211

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += INPUT_mem_r
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += INPUT_mem_r
	S += c211_mem1 <= c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(INPUT_mem_w)
	S += c211 <= c211_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design2/bls12-461/scheduling/CONJ_mul1_add4/CONJ_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

