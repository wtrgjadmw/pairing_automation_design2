from pyschedule import Scenario, solvers, plotters, alt

def solve_inv_mul1_add4_0(ConstStep, ExpStep):
	horizon = 92
	S=Scenario("inv_mul1_add4_0",horizon = horizon)

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
	T0T0 = S.Task('T0T0', length=1, delay_cost=1)
	T0T0 += alt(ADD)

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	T0T0_mem0 += INPUT_mem_r
	S += T0T0_mem0<=T0T0

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	T0T0_mem1 += INPUT_mem_r
	S += T0T0_mem1<=T0T0

	T0T1 = S.Task('T0T1', length=1, delay_cost=1)
	T0T1 += alt(ADD)

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	T0T1_mem0 += INPUT_mem_r
	S += T0T1_mem0<=T0T1

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	T0T1_mem1 += INPUT_mem_r
	S += T0T1_mem1<=T0T1

	T0T2_in = S.Task('T0T2_in', length=1, delay_cost=1)
	T0T2_in += alt(MUL_in)
	T0T2 = S.Task('T0T2', length=7, delay_cost=1)
	T0T2 += alt(MUL)
	S+=T0T2>=T0T2_in

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	T0T2_mem0 += INPUT_mem_r
	S += T0T2_mem0<=T0T2

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	T0T2_mem1 += INPUT_mem_r
	S += T0T2_mem1<=T0T2

	T1T0 = S.Task('T1T0', length=1, delay_cost=1)
	T1T0 += alt(ADD)

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	T1T0_mem0 += INPUT_mem_r
	S += T1T0_mem0<=T1T0

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	T1T0_mem1 += INPUT_mem_r
	S += T1T0_mem1<=T1T0

	T1T1 = S.Task('T1T1', length=1, delay_cost=1)
	T1T1 += alt(ADD)

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	T1T1_mem0 += INPUT_mem_r
	S += T1T1_mem0<=T1T1

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	T1T1_mem1 += INPUT_mem_r
	S += T1T1_mem1<=T1T1

	T1T2_in = S.Task('T1T2_in', length=1, delay_cost=1)
	T1T2_in += alt(MUL_in)
	T1T2 = S.Task('T1T2', length=7, delay_cost=1)
	T1T2 += alt(MUL)
	S+=T1T2>=T1T2_in

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	T1T2_mem0 += INPUT_mem_r
	S += T1T2_mem0<=T1T2

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	T1T2_mem1 += INPUT_mem_r
	S += T1T2_mem1<=T1T2

	T2T0 = S.Task('T2T0', length=1, delay_cost=1)
	T2T0 += alt(ADD)

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	T2T0_mem0 += INPUT_mem_r
	S += T2T0_mem0<=T2T0

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	T2T0_mem1 += INPUT_mem_r
	S += T2T0_mem1<=T2T0

	T2T1 = S.Task('T2T1', length=1, delay_cost=1)
	T2T1 += alt(ADD)

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	T2T1_mem0 += INPUT_mem_r
	S += T2T1_mem0<=T2T1

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	T2T1_mem1 += INPUT_mem_r
	S += T2T1_mem1<=T2T1

	T2T2_in = S.Task('T2T2_in', length=1, delay_cost=1)
	T2T2_in += alt(MUL_in)
	T2T2 = S.Task('T2T2', length=7, delay_cost=1)
	T2T2 += alt(MUL)
	S+=T2T2>=T2T2_in

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	T2T2_mem0 += INPUT_mem_r
	S += T2T2_mem0<=T2T2

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	T2T2_mem1 += INPUT_mem_r
	S += T2T2_mem1<=T2T2

	NEW_A000 = S.Task('NEW_A000', length=1, delay_cost=1)
	NEW_A000 += alt(ADD)

	NEW_A000_mem0 = S.Task('NEW_A000_mem0', length=1, delay_cost=1)
	NEW_A000_mem0 += INPUT_mem_r
	S += NEW_A000_mem0<=NEW_A000

	NEW_A000_mem1 = S.Task('NEW_A000_mem1', length=1, delay_cost=1)
	NEW_A000_mem1 += INPUT_mem_r
	S += NEW_A000_mem1<=NEW_A000

	NEW_A001 = S.Task('NEW_A001', length=1, delay_cost=1)
	NEW_A001 += alt(ADD)

	NEW_A001_mem0 = S.Task('NEW_A001_mem0', length=1, delay_cost=1)
	NEW_A001_mem0 += INPUT_mem_r
	S += NEW_A001_mem0<=NEW_A001

	NEW_A001_mem1 = S.Task('NEW_A001_mem1', length=1, delay_cost=1)
	NEW_A001_mem1 += INPUT_mem_r
	S += NEW_A001_mem1<=NEW_A001

	NEW_A010 = S.Task('NEW_A010', length=1, delay_cost=1)
	NEW_A010 += alt(ADD)

	NEW_A010_mem0 = S.Task('NEW_A010_mem0', length=1, delay_cost=1)
	NEW_A010_mem0 += INPUT_mem_r
	S += NEW_A010_mem0<=NEW_A010

	NEW_A010_mem1 = S.Task('NEW_A010_mem1', length=1, delay_cost=1)
	NEW_A010_mem1 += INPUT_mem_r
	S += NEW_A010_mem1<=NEW_A010

	NEW_A011 = S.Task('NEW_A011', length=1, delay_cost=1)
	NEW_A011 += alt(ADD)

	NEW_A011_mem0 = S.Task('NEW_A011_mem0', length=1, delay_cost=1)
	NEW_A011_mem0 += INPUT_mem_r
	S += NEW_A011_mem0<=NEW_A011

	NEW_A011_mem1 = S.Task('NEW_A011_mem1', length=1, delay_cost=1)
	NEW_A011_mem1 += INPUT_mem_r
	S += NEW_A011_mem1<=NEW_A011

	NEW_A020 = S.Task('NEW_A020', length=1, delay_cost=1)
	NEW_A020 += alt(ADD)

	NEW_A020_mem0 = S.Task('NEW_A020_mem0', length=1, delay_cost=1)
	NEW_A020_mem0 += INPUT_mem_r
	S += NEW_A020_mem0<=NEW_A020

	NEW_A020_mem1 = S.Task('NEW_A020_mem1', length=1, delay_cost=1)
	NEW_A020_mem1 += INPUT_mem_r
	S += NEW_A020_mem1<=NEW_A020

	NEW_A021 = S.Task('NEW_A021', length=1, delay_cost=1)
	NEW_A021 += alt(ADD)

	NEW_A021_mem0 = S.Task('NEW_A021_mem0', length=1, delay_cost=1)
	NEW_A021_mem0 += INPUT_mem_r
	S += NEW_A021_mem0<=NEW_A021

	NEW_A021_mem1 = S.Task('NEW_A021_mem1', length=1, delay_cost=1)
	NEW_A021_mem1 += INPUT_mem_r
	S += NEW_A021_mem1<=NEW_A021

	T0_T0 = S.Task('T0_T0', length=1, delay_cost=1)
	T0_T0 += alt(ADD)

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	T0_T0_mem0 += INPUT_mem_r
	S += T0_T0_mem0<=T0_T0

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	T0_T0_mem1 += INPUT_mem_r
	S += T0_T0_mem1<=T0_T0

	T0_T1 = S.Task('T0_T1', length=1, delay_cost=1)
	T0_T1 += alt(ADD)

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	T0_T1_mem0 += INPUT_mem_r
	S += T0_T1_mem0<=T0_T1

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	T0_T1_mem1 += INPUT_mem_r
	S += T0_T1_mem1<=T0_T1

	T0_T2_in = S.Task('T0_T2_in', length=1, delay_cost=1)
	T0_T2_in += alt(MUL_in)
	T0_T2 = S.Task('T0_T2', length=7, delay_cost=1)
	T0_T2 += alt(MUL)
	S+=T0_T2>=T0_T2_in

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	T0_T2_mem0 += INPUT_mem_r
	S += T0_T2_mem0<=T0_T2

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	T0_T2_mem1 += INPUT_mem_r
	S += T0_T2_mem1<=T0_T2

	T1_T0 = S.Task('T1_T0', length=1, delay_cost=1)
	T1_T0 += alt(ADD)

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	T1_T0_mem0 += INPUT_mem_r
	S += T1_T0_mem0<=T1_T0

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	T1_T0_mem1 += INPUT_mem_r
	S += T1_T0_mem1<=T1_T0

	T1_T1 = S.Task('T1_T1', length=1, delay_cost=1)
	T1_T1 += alt(ADD)

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	T1_T1_mem0 += INPUT_mem_r
	S += T1_T1_mem0<=T1_T1

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	T1_T1_mem1 += INPUT_mem_r
	S += T1_T1_mem1<=T1_T1

	T1_T2_in = S.Task('T1_T2_in', length=1, delay_cost=1)
	T1_T2_in += alt(MUL_in)
	T1_T2 = S.Task('T1_T2', length=7, delay_cost=1)
	T1_T2 += alt(MUL)
	S+=T1_T2>=T1_T2_in

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	T1_T2_mem0 += INPUT_mem_r
	S += T1_T2_mem0<=T1_T2

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	T1_T2_mem1 += INPUT_mem_r
	S += T1_T2_mem1<=T1_T2

	T2_1T0 = S.Task('T2_1T0', length=1, delay_cost=1)
	T2_1T0 += alt(ADD)

	T2_1T0_mem0 = S.Task('T2_1T0_mem0', length=1, delay_cost=1)
	T2_1T0_mem0 += INPUT_mem_r
	S += T2_1T0_mem0<=T2_1T0

	T2_1T0_mem1 = S.Task('T2_1T0_mem1', length=1, delay_cost=1)
	T2_1T0_mem1 += INPUT_mem_r
	S += T2_1T0_mem1<=T2_1T0

	T2_1T1 = S.Task('T2_1T1', length=1, delay_cost=1)
	T2_1T1 += alt(ADD)

	T2_1T1_mem0 = S.Task('T2_1T1_mem0', length=1, delay_cost=1)
	T2_1T1_mem0 += INPUT_mem_r
	S += T2_1T1_mem0<=T2_1T1

	T2_1T1_mem1 = S.Task('T2_1T1_mem1', length=1, delay_cost=1)
	T2_1T1_mem1 += INPUT_mem_r
	S += T2_1T1_mem1<=T2_1T1

	T2_1T2_in = S.Task('T2_1T2_in', length=1, delay_cost=1)
	T2_1T2_in += alt(MUL_in)
	T2_1T2 = S.Task('T2_1T2', length=7, delay_cost=1)
	T2_1T2 += alt(MUL)
	S+=T2_1T2>=T2_1T2_in

	T2_1T2_mem0 = S.Task('T2_1T2_mem0', length=1, delay_cost=1)
	T2_1T2_mem0 += INPUT_mem_r
	S += T2_1T2_mem0<=T2_1T2

	T2_1T2_mem1 = S.Task('T2_1T2_mem1', length=1, delay_cost=1)
	T2_1T2_mem1 += INPUT_mem_r
	S += T2_1T2_mem1<=T2_1T2

	NEW_A100 = S.Task('NEW_A100', length=1, delay_cost=1)
	NEW_A100 += alt(ADD)

	NEW_A100_mem0 = S.Task('NEW_A100_mem0', length=1, delay_cost=1)
	NEW_A100_mem0 += INPUT_mem_r
	S += NEW_A100_mem0<=NEW_A100

	NEW_A100_mem1 = S.Task('NEW_A100_mem1', length=1, delay_cost=1)
	NEW_A100_mem1 += INPUT_mem_r
	S += NEW_A100_mem1<=NEW_A100

	NEW_A101 = S.Task('NEW_A101', length=1, delay_cost=1)
	NEW_A101 += alt(ADD)

	NEW_A101_mem0 = S.Task('NEW_A101_mem0', length=1, delay_cost=1)
	NEW_A101_mem0 += INPUT_mem_r
	S += NEW_A101_mem0<=NEW_A101

	NEW_A101_mem1 = S.Task('NEW_A101_mem1', length=1, delay_cost=1)
	NEW_A101_mem1 += INPUT_mem_r
	S += NEW_A101_mem1<=NEW_A101

	NEW_A110 = S.Task('NEW_A110', length=1, delay_cost=1)
	NEW_A110 += alt(ADD)

	NEW_A110_mem0 = S.Task('NEW_A110_mem0', length=1, delay_cost=1)
	NEW_A110_mem0 += INPUT_mem_r
	S += NEW_A110_mem0<=NEW_A110

	NEW_A110_mem1 = S.Task('NEW_A110_mem1', length=1, delay_cost=1)
	NEW_A110_mem1 += INPUT_mem_r
	S += NEW_A110_mem1<=NEW_A110

	NEW_A111 = S.Task('NEW_A111', length=1, delay_cost=1)
	NEW_A111 += alt(ADD)

	NEW_A111_mem0 = S.Task('NEW_A111_mem0', length=1, delay_cost=1)
	NEW_A111_mem0 += INPUT_mem_r
	S += NEW_A111_mem0<=NEW_A111

	NEW_A111_mem1 = S.Task('NEW_A111_mem1', length=1, delay_cost=1)
	NEW_A111_mem1 += INPUT_mem_r
	S += NEW_A111_mem1<=NEW_A111

	NEW_A120 = S.Task('NEW_A120', length=1, delay_cost=1)
	NEW_A120 += alt(ADD)

	NEW_A120_mem0 = S.Task('NEW_A120_mem0', length=1, delay_cost=1)
	NEW_A120_mem0 += INPUT_mem_r
	S += NEW_A120_mem0<=NEW_A120

	NEW_A120_mem1 = S.Task('NEW_A120_mem1', length=1, delay_cost=1)
	NEW_A120_mem1 += INPUT_mem_r
	S += NEW_A120_mem1<=NEW_A120

	NEW_A121 = S.Task('NEW_A121', length=1, delay_cost=1)
	NEW_A121 += alt(ADD)

	NEW_A121_mem0 = S.Task('NEW_A121_mem0', length=1, delay_cost=1)
	NEW_A121_mem0 += INPUT_mem_r
	S += NEW_A121_mem0<=NEW_A121

	NEW_A121_mem1 = S.Task('NEW_A121_mem1', length=1, delay_cost=1)
	NEW_A121_mem1 += INPUT_mem_r
	S += NEW_A121_mem1<=NEW_A121

	T0_3T2 = S.Task('T0_3T2', length=1, delay_cost=1)
	T0_3T2 += alt(ADD)

	T0_3T2_mem0 = S.Task('T0_3T2_mem0', length=1, delay_cost=1)
	T0_3T2_mem0 += INPUT_mem_r
	S += T0_3T2_mem0<=T0_3T2

	T0_3T2_mem1 = S.Task('T0_3T2_mem1', length=1, delay_cost=1)
	T0_3T2_mem1 += INPUT_mem_r
	S += T0_3T2_mem1<=T0_3T2

	T1_3T2 = S.Task('T1_3T2', length=1, delay_cost=1)
	T1_3T2 += alt(ADD)

	T1_3T2_mem0 = S.Task('T1_3T2_mem0', length=1, delay_cost=1)
	T1_3T2_mem0 += INPUT_mem_r
	S += T1_3T2_mem0<=T1_3T2

	T1_3T2_mem1 = S.Task('T1_3T2_mem1', length=1, delay_cost=1)
	T1_3T2_mem1 += INPUT_mem_r
	S += T1_3T2_mem1<=T1_3T2

	T2_6T2 = S.Task('T2_6T2', length=1, delay_cost=1)
	T2_6T2 += alt(ADD)

	T2_6T2_mem0 = S.Task('T2_6T2_mem0', length=1, delay_cost=1)
	T2_6T2_mem0 += INPUT_mem_r
	S += T2_6T2_mem0<=T2_6T2

	T2_6T2_mem1 = S.Task('T2_6T2_mem1', length=1, delay_cost=1)
	T2_6T2_mem1 += INPUT_mem_r
	S += T2_6T2_mem1<=T2_6T2

	T0_4T2 = S.Task('T0_4T2', length=1, delay_cost=1)
	T0_4T2 += alt(ADD)

	T0_4T2_mem0 = S.Task('T0_4T2_mem0', length=1, delay_cost=1)
	T0_4T2_mem0 += INPUT_mem_r
	S += T0_4T2_mem0<=T0_4T2

	T0_4T2_mem1 = S.Task('T0_4T2_mem1', length=1, delay_cost=1)
	T0_4T2_mem1 += INPUT_mem_r
	S += T0_4T2_mem1<=T0_4T2

	T1_4T2 = S.Task('T1_4T2', length=1, delay_cost=1)
	T1_4T2 += alt(ADD)

	T1_4T2_mem0 = S.Task('T1_4T2_mem0', length=1, delay_cost=1)
	T1_4T2_mem0 += INPUT_mem_r
	S += T1_4T2_mem0<=T1_4T2

	T1_4T2_mem1 = S.Task('T1_4T2_mem1', length=1, delay_cost=1)
	T1_4T2_mem1 += INPUT_mem_r
	S += T1_4T2_mem1<=T1_4T2

	T2_8T2 = S.Task('T2_8T2', length=1, delay_cost=1)
	T2_8T2 += alt(ADD)

	T2_8T2_mem0 = S.Task('T2_8T2_mem0', length=1, delay_cost=1)
	T2_8T2_mem0 += INPUT_mem_r
	S += T2_8T2_mem0<=T2_8T2

	T2_8T2_mem1 = S.Task('T2_8T2_mem1', length=1, delay_cost=1)
	T2_8T2_mem1 += INPUT_mem_r
	S += T2_8T2_mem1<=T2_8T2

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "inv_mul1_add4/inv_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_inv_mul1_add4_0(0, 0)