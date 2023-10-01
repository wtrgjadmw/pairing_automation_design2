from pyschedule import Scenario, solvers, plotters, alt

def solve_conj_mul1_add4_0(ConstStep, ExpStep):
	horizon = 90
	S=Scenario("conj_mul1_add4_0",horizon = horizon)

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
	C000 = S.Task('C000', length=1, delay_cost=1)
	C000 += alt(ADD)

	C000_mem0 = S.Task('C000_mem0', length=1, delay_cost=1)
	C000_mem0 += INPUT_mem_r
	S += C000_mem0<=C000

	C000_mem1 = S.Task('C000_mem1', length=1, delay_cost=1)
	C000_mem1 += INPUT_mem_r
	S += C000_mem1<=C000

	C000_w = S.Task('C000_w', length=1, delay_cost=1)
	C000_w += alt(INPUT_mem_w)
	S += 0 < C000_w
	S += C000-1 <= C000_w

	C001 = S.Task('C001', length=1, delay_cost=1)
	C001 += alt(ADD)

	C001_mem0 = S.Task('C001_mem0', length=1, delay_cost=1)
	C001_mem0 += INPUT_mem_r
	S += C001_mem0<=C001

	C001_mem1 = S.Task('C001_mem1', length=1, delay_cost=1)
	C001_mem1 += INPUT_mem_r
	S += C001_mem1<=C001

	C001_w = S.Task('C001_w', length=1, delay_cost=1)
	C001_w += alt(INPUT_mem_w)
	S += 0 < C001_w
	S += C001-1 <= C001_w

	C010 = S.Task('C010', length=1, delay_cost=1)
	C010 += alt(ADD)

	C010_mem0 = S.Task('C010_mem0', length=1, delay_cost=1)
	C010_mem0 += INPUT_mem_r
	S += C010_mem0<=C010

	C010_mem1 = S.Task('C010_mem1', length=1, delay_cost=1)
	C010_mem1 += INPUT_mem_r
	S += C010_mem1<=C010

	C010_w = S.Task('C010_w', length=1, delay_cost=1)
	C010_w += alt(INPUT_mem_w)
	S += 0 < C010_w
	S += C010-1 <= C010_w

	C011 = S.Task('C011', length=1, delay_cost=1)
	C011 += alt(ADD)

	C011_mem0 = S.Task('C011_mem0', length=1, delay_cost=1)
	C011_mem0 += INPUT_mem_r
	S += C011_mem0<=C011

	C011_mem1 = S.Task('C011_mem1', length=1, delay_cost=1)
	C011_mem1 += INPUT_mem_r
	S += C011_mem1<=C011

	C011_w = S.Task('C011_w', length=1, delay_cost=1)
	C011_w += alt(INPUT_mem_w)
	S += 0 < C011_w
	S += C011-1 <= C011_w

	C100 = S.Task('C100', length=1, delay_cost=1)
	C100 += alt(ADD)

	C100_mem0 = S.Task('C100_mem0', length=1, delay_cost=1)
	C100_mem0 += INPUT_mem_r
	S += C100_mem0<=C100

	C100_mem1 = S.Task('C100_mem1', length=1, delay_cost=1)
	C100_mem1 += INPUT_mem_r
	S += C100_mem1<=C100

	C100_w = S.Task('C100_w', length=1, delay_cost=1)
	C100_w += alt(INPUT_mem_w)
	S += 0 < C100_w
	S += C100-1 <= C100_w

	C101 = S.Task('C101', length=1, delay_cost=1)
	C101 += alt(ADD)

	C101_mem0 = S.Task('C101_mem0', length=1, delay_cost=1)
	C101_mem0 += INPUT_mem_r
	S += C101_mem0<=C101

	C101_mem1 = S.Task('C101_mem1', length=1, delay_cost=1)
	C101_mem1 += INPUT_mem_r
	S += C101_mem1<=C101

	C101_w = S.Task('C101_w', length=1, delay_cost=1)
	C101_w += alt(INPUT_mem_w)
	S += 0 < C101_w
	S += C101-1 <= C101_w

	C110 = S.Task('C110', length=1, delay_cost=1)
	C110 += alt(ADD)

	C110_mem0 = S.Task('C110_mem0', length=1, delay_cost=1)
	C110_mem0 += INPUT_mem_r
	S += C110_mem0<=C110

	C110_mem1 = S.Task('C110_mem1', length=1, delay_cost=1)
	C110_mem1 += INPUT_mem_r
	S += C110_mem1<=C110

	C110_w = S.Task('C110_w', length=1, delay_cost=1)
	C110_w += alt(INPUT_mem_w)
	S += 0 < C110_w
	S += C110-1 <= C110_w

	C111 = S.Task('C111', length=1, delay_cost=1)
	C111 += alt(ADD)

	C111_mem0 = S.Task('C111_mem0', length=1, delay_cost=1)
	C111_mem0 += INPUT_mem_r
	S += C111_mem0<=C111

	C111_mem1 = S.Task('C111_mem1', length=1, delay_cost=1)
	C111_mem1 += INPUT_mem_r
	S += C111_mem1<=C111

	C111_w = S.Task('C111_w', length=1, delay_cost=1)
	C111_w += alt(INPUT_mem_w)
	S += 0 < C111_w
	S += C111-1 <= C111_w

	C200 = S.Task('C200', length=1, delay_cost=1)
	C200 += alt(ADD)

	C200_mem0 = S.Task('C200_mem0', length=1, delay_cost=1)
	C200_mem0 += INPUT_mem_r
	S += C200_mem0<=C200

	C200_mem1 = S.Task('C200_mem1', length=1, delay_cost=1)
	C200_mem1 += INPUT_mem_r
	S += C200_mem1<=C200

	C200_w = S.Task('C200_w', length=1, delay_cost=1)
	C200_w += alt(INPUT_mem_w)
	S += 0 < C200_w
	S += C200-1 <= C200_w

	C201 = S.Task('C201', length=1, delay_cost=1)
	C201 += alt(ADD)

	C201_mem0 = S.Task('C201_mem0', length=1, delay_cost=1)
	C201_mem0 += INPUT_mem_r
	S += C201_mem0<=C201

	C201_mem1 = S.Task('C201_mem1', length=1, delay_cost=1)
	C201_mem1 += INPUT_mem_r
	S += C201_mem1<=C201

	C201_w = S.Task('C201_w', length=1, delay_cost=1)
	C201_w += alt(INPUT_mem_w)
	S += 0 < C201_w
	S += C201-1 <= C201_w

	C210 = S.Task('C210', length=1, delay_cost=1)
	C210 += alt(ADD)

	C210_mem0 = S.Task('C210_mem0', length=1, delay_cost=1)
	C210_mem0 += INPUT_mem_r
	S += C210_mem0<=C210

	C210_mem1 = S.Task('C210_mem1', length=1, delay_cost=1)
	C210_mem1 += INPUT_mem_r
	S += C210_mem1<=C210

	C210_w = S.Task('C210_w', length=1, delay_cost=1)
	C210_w += alt(INPUT_mem_w)
	S += 0 < C210_w
	S += C210-1 <= C210_w

	C211 = S.Task('C211', length=1, delay_cost=1)
	C211 += alt(ADD)

	C211_mem0 = S.Task('C211_mem0', length=1, delay_cost=1)
	C211_mem0 += INPUT_mem_r
	S += C211_mem0<=C211

	C211_mem1 = S.Task('C211_mem1', length=1, delay_cost=1)
	C211_mem1 += INPUT_mem_r
	S += C211_mem1<=C211

	C211_w = S.Task('C211_w', length=1, delay_cost=1)
	C211_w += alt(INPUT_mem_w)
	S += 0 < C211_w
	S += C211-1 <= C211_w

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "conj_mul1_add4/conj_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_conj_mul1_add4_0(0, 0)