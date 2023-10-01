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
	C0000 = S.Task('C0000', length=1, delay_cost=1)
	C0000 += alt(ADD)

	C0000_mem0 = S.Task('C0000_mem0', length=1, delay_cost=1)
	C0000_mem0 += INPUT_mem_r
	S += C0000_mem0<=C0000

	C0000_mem1 = S.Task('C0000_mem1', length=1, delay_cost=1)
	C0000_mem1 += INPUT_mem_r
	S += C0000_mem1<=C0000

	C0000_w = S.Task('C0000_w', length=1, delay_cost=1)
	C0000_w += alt(INPUT_mem_w)
	S += C0000-1 <= C0000_w

	C0001 = S.Task('C0001', length=1, delay_cost=1)
	C0001 += alt(ADD)

	C0001_mem0 = S.Task('C0001_mem0', length=1, delay_cost=1)
	C0001_mem0 += INPUT_mem_r
	S += C0001_mem0<=C0001

	C0001_mem1 = S.Task('C0001_mem1', length=1, delay_cost=1)
	C0001_mem1 += INPUT_mem_r
	S += C0001_mem1<=C0001

	C0001_w = S.Task('C0001_w', length=1, delay_cost=1)
	C0001_w += alt(INPUT_mem_w)
	S += C0001-1 <= C0001_w

	C0010 = S.Task('C0010', length=1, delay_cost=1)
	C0010 += alt(ADD)

	C0010_mem0 = S.Task('C0010_mem0', length=1, delay_cost=1)
	C0010_mem0 += INPUT_mem_r
	S += C0010_mem0<=C0010

	C0010_mem1 = S.Task('C0010_mem1', length=1, delay_cost=1)
	C0010_mem1 += INPUT_mem_r
	S += C0010_mem1<=C0010

	C0010_w = S.Task('C0010_w', length=1, delay_cost=1)
	C0010_w += alt(INPUT_mem_w)
	S += C0010-1 <= C0010_w

	C0011 = S.Task('C0011', length=1, delay_cost=1)
	C0011 += alt(ADD)

	C0011_mem0 = S.Task('C0011_mem0', length=1, delay_cost=1)
	C0011_mem0 += INPUT_mem_r
	S += C0011_mem0<=C0011

	C0011_mem1 = S.Task('C0011_mem1', length=1, delay_cost=1)
	C0011_mem1 += INPUT_mem_r
	S += C0011_mem1<=C0011

	C0011_w = S.Task('C0011_w', length=1, delay_cost=1)
	C0011_w += alt(INPUT_mem_w)
	S += C0011-1 <= C0011_w

	C0100 = S.Task('C0100', length=1, delay_cost=1)
	C0100 += alt(ADD)

	C0100_mem0 = S.Task('C0100_mem0', length=1, delay_cost=1)
	C0100_mem0 += INPUT_mem_r
	S += C0100_mem0<=C0100

	C0100_mem1 = S.Task('C0100_mem1', length=1, delay_cost=1)
	C0100_mem1 += INPUT_mem_r
	S += C0100_mem1<=C0100

	C0100_w = S.Task('C0100_w', length=1, delay_cost=1)
	C0100_w += alt(INPUT_mem_w)
	S += C0100-1 <= C0100_w

	C0101 = S.Task('C0101', length=1, delay_cost=1)
	C0101 += alt(ADD)

	C0101_mem0 = S.Task('C0101_mem0', length=1, delay_cost=1)
	C0101_mem0 += INPUT_mem_r
	S += C0101_mem0<=C0101

	C0101_mem1 = S.Task('C0101_mem1', length=1, delay_cost=1)
	C0101_mem1 += INPUT_mem_r
	S += C0101_mem1<=C0101

	C0101_w = S.Task('C0101_w', length=1, delay_cost=1)
	C0101_w += alt(INPUT_mem_w)
	S += C0101-1 <= C0101_w

	C0110 = S.Task('C0110', length=1, delay_cost=1)
	C0110 += alt(ADD)

	C0110_mem0 = S.Task('C0110_mem0', length=1, delay_cost=1)
	C0110_mem0 += INPUT_mem_r
	S += C0110_mem0<=C0110

	C0110_mem1 = S.Task('C0110_mem1', length=1, delay_cost=1)
	C0110_mem1 += INPUT_mem_r
	S += C0110_mem1<=C0110

	C0110_w = S.Task('C0110_w', length=1, delay_cost=1)
	C0110_w += alt(INPUT_mem_w)
	S += C0110-1 <= C0110_w

	C0111 = S.Task('C0111', length=1, delay_cost=1)
	C0111 += alt(ADD)

	C0111_mem0 = S.Task('C0111_mem0', length=1, delay_cost=1)
	C0111_mem0 += INPUT_mem_r
	S += C0111_mem0<=C0111

	C0111_mem1 = S.Task('C0111_mem1', length=1, delay_cost=1)
	C0111_mem1 += INPUT_mem_r
	S += C0111_mem1<=C0111

	C0111_w = S.Task('C0111_w', length=1, delay_cost=1)
	C0111_w += alt(INPUT_mem_w)
	S += C0111-1 <= C0111_w

	C0200 = S.Task('C0200', length=1, delay_cost=1)
	C0200 += alt(ADD)

	C0200_mem0 = S.Task('C0200_mem0', length=1, delay_cost=1)
	C0200_mem0 += INPUT_mem_r
	S += C0200_mem0<=C0200

	C0200_mem1 = S.Task('C0200_mem1', length=1, delay_cost=1)
	C0200_mem1 += INPUT_mem_r
	S += C0200_mem1<=C0200

	C0200_w = S.Task('C0200_w', length=1, delay_cost=1)
	C0200_w += alt(INPUT_mem_w)
	S += C0200-1 <= C0200_w

	C0201 = S.Task('C0201', length=1, delay_cost=1)
	C0201 += alt(ADD)

	C0201_mem0 = S.Task('C0201_mem0', length=1, delay_cost=1)
	C0201_mem0 += INPUT_mem_r
	S += C0201_mem0<=C0201

	C0201_mem1 = S.Task('C0201_mem1', length=1, delay_cost=1)
	C0201_mem1 += INPUT_mem_r
	S += C0201_mem1<=C0201

	C0201_w = S.Task('C0201_w', length=1, delay_cost=1)
	C0201_w += alt(INPUT_mem_w)
	S += C0201-1 <= C0201_w

	C0210 = S.Task('C0210', length=1, delay_cost=1)
	C0210 += alt(ADD)

	C0210_mem0 = S.Task('C0210_mem0', length=1, delay_cost=1)
	C0210_mem0 += INPUT_mem_r
	S += C0210_mem0<=C0210

	C0210_mem1 = S.Task('C0210_mem1', length=1, delay_cost=1)
	C0210_mem1 += INPUT_mem_r
	S += C0210_mem1<=C0210

	C0210_w = S.Task('C0210_w', length=1, delay_cost=1)
	C0210_w += alt(INPUT_mem_w)
	S += C0210-1 <= C0210_w

	C0211 = S.Task('C0211', length=1, delay_cost=1)
	C0211 += alt(ADD)

	C0211_mem0 = S.Task('C0211_mem0', length=1, delay_cost=1)
	C0211_mem0 += INPUT_mem_r
	S += C0211_mem0<=C0211

	C0211_mem1 = S.Task('C0211_mem1', length=1, delay_cost=1)
	C0211_mem1 += INPUT_mem_r
	S += C0211_mem1<=C0211

	C0211_w = S.Task('C0211_w', length=1, delay_cost=1)
	C0211_w += alt(INPUT_mem_w)
	S += C0211-1 <= C0211_w

	C1000 = S.Task('C1000', length=1, delay_cost=1)
	C1000 += alt(ADD)

	C1000_mem0 = S.Task('C1000_mem0', length=1, delay_cost=1)
	C1000_mem0 += INPUT_mem_r
	S += C1000_mem0<=C1000

	C1000_mem1 = S.Task('C1000_mem1', length=1, delay_cost=1)
	C1000_mem1 += INPUT_mem_r
	S += C1000_mem1<=C1000

	C1000_w = S.Task('C1000_w', length=1, delay_cost=1)
	C1000_w += alt(INPUT_mem_w)
	S += C1000-1 <= C1000_w

	C1001 = S.Task('C1001', length=1, delay_cost=1)
	C1001 += alt(ADD)

	C1001_mem0 = S.Task('C1001_mem0', length=1, delay_cost=1)
	C1001_mem0 += INPUT_mem_r
	S += C1001_mem0<=C1001

	C1001_mem1 = S.Task('C1001_mem1', length=1, delay_cost=1)
	C1001_mem1 += INPUT_mem_r
	S += C1001_mem1<=C1001

	C1001_w = S.Task('C1001_w', length=1, delay_cost=1)
	C1001_w += alt(INPUT_mem_w)
	S += C1001-1 <= C1001_w

	C1010 = S.Task('C1010', length=1, delay_cost=1)
	C1010 += alt(ADD)

	C1010_mem0 = S.Task('C1010_mem0', length=1, delay_cost=1)
	C1010_mem0 += INPUT_mem_r
	S += C1010_mem0<=C1010

	C1010_mem1 = S.Task('C1010_mem1', length=1, delay_cost=1)
	C1010_mem1 += INPUT_mem_r
	S += C1010_mem1<=C1010

	C1010_w = S.Task('C1010_w', length=1, delay_cost=1)
	C1010_w += alt(INPUT_mem_w)
	S += C1010-1 <= C1010_w

	C1011 = S.Task('C1011', length=1, delay_cost=1)
	C1011 += alt(ADD)

	C1011_mem0 = S.Task('C1011_mem0', length=1, delay_cost=1)
	C1011_mem0 += INPUT_mem_r
	S += C1011_mem0<=C1011

	C1011_mem1 = S.Task('C1011_mem1', length=1, delay_cost=1)
	C1011_mem1 += INPUT_mem_r
	S += C1011_mem1<=C1011

	C1011_w = S.Task('C1011_w', length=1, delay_cost=1)
	C1011_w += alt(INPUT_mem_w)
	S += C1011-1 <= C1011_w

	C1100 = S.Task('C1100', length=1, delay_cost=1)
	C1100 += alt(ADD)

	C1100_mem0 = S.Task('C1100_mem0', length=1, delay_cost=1)
	C1100_mem0 += INPUT_mem_r
	S += C1100_mem0<=C1100

	C1100_mem1 = S.Task('C1100_mem1', length=1, delay_cost=1)
	C1100_mem1 += INPUT_mem_r
	S += C1100_mem1<=C1100

	C1100_w = S.Task('C1100_w', length=1, delay_cost=1)
	C1100_w += alt(INPUT_mem_w)
	S += C1100-1 <= C1100_w

	C1101 = S.Task('C1101', length=1, delay_cost=1)
	C1101 += alt(ADD)

	C1101_mem0 = S.Task('C1101_mem0', length=1, delay_cost=1)
	C1101_mem0 += INPUT_mem_r
	S += C1101_mem0<=C1101

	C1101_mem1 = S.Task('C1101_mem1', length=1, delay_cost=1)
	C1101_mem1 += INPUT_mem_r
	S += C1101_mem1<=C1101

	C1101_w = S.Task('C1101_w', length=1, delay_cost=1)
	C1101_w += alt(INPUT_mem_w)
	S += C1101-1 <= C1101_w

	C1110 = S.Task('C1110', length=1, delay_cost=1)
	C1110 += alt(ADD)

	C1110_mem0 = S.Task('C1110_mem0', length=1, delay_cost=1)
	C1110_mem0 += INPUT_mem_r
	S += C1110_mem0<=C1110

	C1110_mem1 = S.Task('C1110_mem1', length=1, delay_cost=1)
	C1110_mem1 += INPUT_mem_r
	S += C1110_mem1<=C1110

	C1110_w = S.Task('C1110_w', length=1, delay_cost=1)
	C1110_w += alt(INPUT_mem_w)
	S += C1110-1 <= C1110_w

	C1111 = S.Task('C1111', length=1, delay_cost=1)
	C1111 += alt(ADD)

	C1111_mem0 = S.Task('C1111_mem0', length=1, delay_cost=1)
	C1111_mem0 += INPUT_mem_r
	S += C1111_mem0<=C1111

	C1111_mem1 = S.Task('C1111_mem1', length=1, delay_cost=1)
	C1111_mem1 += INPUT_mem_r
	S += C1111_mem1<=C1111

	C1111_w = S.Task('C1111_w', length=1, delay_cost=1)
	C1111_w += alt(INPUT_mem_w)
	S += C1111-1 <= C1111_w

	C1200 = S.Task('C1200', length=1, delay_cost=1)
	C1200 += alt(ADD)

	C1200_mem0 = S.Task('C1200_mem0', length=1, delay_cost=1)
	C1200_mem0 += INPUT_mem_r
	S += C1200_mem0<=C1200

	C1200_mem1 = S.Task('C1200_mem1', length=1, delay_cost=1)
	C1200_mem1 += INPUT_mem_r
	S += C1200_mem1<=C1200

	C1200_w = S.Task('C1200_w', length=1, delay_cost=1)
	C1200_w += alt(INPUT_mem_w)
	S += C1200-1 <= C1200_w

	C1201 = S.Task('C1201', length=1, delay_cost=1)
	C1201 += alt(ADD)

	C1201_mem0 = S.Task('C1201_mem0', length=1, delay_cost=1)
	C1201_mem0 += INPUT_mem_r
	S += C1201_mem0<=C1201

	C1201_mem1 = S.Task('C1201_mem1', length=1, delay_cost=1)
	C1201_mem1 += INPUT_mem_r
	S += C1201_mem1<=C1201

	C1201_w = S.Task('C1201_w', length=1, delay_cost=1)
	C1201_w += alt(INPUT_mem_w)
	S += C1201-1 <= C1201_w

	C1210 = S.Task('C1210', length=1, delay_cost=1)
	C1210 += alt(ADD)

	C1210_mem0 = S.Task('C1210_mem0', length=1, delay_cost=1)
	C1210_mem0 += INPUT_mem_r
	S += C1210_mem0<=C1210

	C1210_mem1 = S.Task('C1210_mem1', length=1, delay_cost=1)
	C1210_mem1 += INPUT_mem_r
	S += C1210_mem1<=C1210

	C1210_w = S.Task('C1210_w', length=1, delay_cost=1)
	C1210_w += alt(INPUT_mem_w)
	S += C1210-1 <= C1210_w

	C1211 = S.Task('C1211', length=1, delay_cost=1)
	C1211 += alt(ADD)

	C1211_mem0 = S.Task('C1211_mem0', length=1, delay_cost=1)
	C1211_mem0 += INPUT_mem_r
	S += C1211_mem0<=C1211

	C1211_mem1 = S.Task('C1211_mem1', length=1, delay_cost=1)
	C1211_mem1 += INPUT_mem_r
	S += C1211_mem1<=C1211

	C1211_w = S.Task('C1211_w', length=1, delay_cost=1)
	C1211_w += alt(INPUT_mem_w)
	S += C1211-1 <= C1211_w

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