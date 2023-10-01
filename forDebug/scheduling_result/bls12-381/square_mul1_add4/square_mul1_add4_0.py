from pyschedule import Scenario, solvers, plotters, alt

def solve_square_mul1_add4_0(ConstStep, ExpStep):
	horizon = 90
	S=Scenario("square_mul1_add4_0",horizon = horizon)

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
	T00 = S.Task('T00', length=1, delay_cost=1)
	T00 += alt(ADD)

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	T00_mem0 += INPUT_mem_r
	S += T00_mem0<=T00

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	T00_mem1 += INPUT_mem_r
	S += T00_mem1<=T00

	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += INPUT_mem_r
	S += T01_mem0<=T01

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	T01_mem1 += INPUT_mem_r
	S += T01_mem1<=T01

	T10 = S.Task('T10', length=1, delay_cost=1)
	T10 += alt(ADD)

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += INPUT_mem_r
	S += T10_mem0<=T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += INPUT_mem_r
	S += T10_mem1<=T10

	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(ADD)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += INPUT_mem_r
	S += T11_mem0<=T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += INPUT_mem_r
	S += T11_mem1<=T11

	T20 = S.Task('T20', length=1, delay_cost=1)
	T20 += alt(ADD)

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += INPUT_mem_r
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += INPUT_mem_r
	S += T20_mem1<=T20

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(ADD)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += INPUT_mem_r
	S += T21_mem0<=T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += INPUT_mem_r
	S += T21_mem1<=T21

	T30 = S.Task('T30', length=1, delay_cost=1)
	T30 += alt(ADD)

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += INPUT_mem_r
	S += T30_mem0<=T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += INPUT_mem_r
	S += T30_mem1<=T30

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += INPUT_mem_r
	S += T31_mem0<=T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += INPUT_mem_r
	S += T31_mem1<=T31

	T40 = S.Task('T40', length=1, delay_cost=1)
	T40 += alt(ADD)

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += INPUT_mem_r
	S += T40_mem0<=T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += INPUT_mem_r
	S += T40_mem1<=T40

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += INPUT_mem_r
	S += T41_mem0<=T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += INPUT_mem_r
	S += T41_mem1<=T41

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(ADD)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += INPUT_mem_r
	S += T50_mem0<=T50

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	T50_mem1 += INPUT_mem_r
	S += T50_mem1<=T50

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(ADD)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += INPUT_mem_r
	S += T51_mem0<=T51

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	T51_mem1 += INPUT_mem_r
	S += T51_mem1<=T51

	T6_T0_in = S.Task('T6_T0_in', length=1, delay_cost=1)
	T6_T0_in += alt(MUL_in)
	T6_T0 = S.Task('T6_T0', length=7, delay_cost=1)
	T6_T0 += alt(MUL)
	S+=T6_T0>=T6_T0_in

	T6_T0_mem0 = S.Task('T6_T0_mem0', length=1, delay_cost=1)
	T6_T0_mem0 += INPUT_mem_r
	S += T6_T0_mem0<=T6_T0

	T6_T0_mem1 = S.Task('T6_T0_mem1', length=1, delay_cost=1)
	T6_T0_mem1 += INPUT_mem_r
	S += T6_T0_mem1<=T6_T0

	T6_T1_in = S.Task('T6_T1_in', length=1, delay_cost=1)
	T6_T1_in += alt(MUL_in)
	T6_T1 = S.Task('T6_T1', length=7, delay_cost=1)
	T6_T1 += alt(MUL)
	S+=T6_T1>=T6_T1_in

	T6_T1_mem0 = S.Task('T6_T1_mem0', length=1, delay_cost=1)
	T6_T1_mem0 += INPUT_mem_r
	S += T6_T1_mem0<=T6_T1

	T6_T1_mem1 = S.Task('T6_T1_mem1', length=1, delay_cost=1)
	T6_T1_mem1 += INPUT_mem_r
	S += T6_T1_mem1<=T6_T1

	T6_T2 = S.Task('T6_T2', length=1, delay_cost=1)
	T6_T2 += alt(ADD)

	T6_T2_mem0 = S.Task('T6_T2_mem0', length=1, delay_cost=1)
	T6_T2_mem0 += INPUT_mem_r
	S += T6_T2_mem0<=T6_T2

	T6_T2_mem1 = S.Task('T6_T2_mem1', length=1, delay_cost=1)
	T6_T2_mem1 += INPUT_mem_r
	S += T6_T2_mem1<=T6_T2

	T6_T3 = S.Task('T6_T3', length=1, delay_cost=1)
	T6_T3 += alt(ADD)

	T6_T3_mem0 = S.Task('T6_T3_mem0', length=1, delay_cost=1)
	T6_T3_mem0 += INPUT_mem_r
	S += T6_T3_mem0<=T6_T3

	T6_T3_mem1 = S.Task('T6_T3_mem1', length=1, delay_cost=1)
	T6_T3_mem1 += INPUT_mem_r
	S += T6_T3_mem1<=T6_T3

	T7_T0_in = S.Task('T7_T0_in', length=1, delay_cost=1)
	T7_T0_in += alt(MUL_in)
	T7_T0 = S.Task('T7_T0', length=7, delay_cost=1)
	T7_T0 += alt(MUL)
	S+=T7_T0>=T7_T0_in

	T7_T0_mem0 = S.Task('T7_T0_mem0', length=1, delay_cost=1)
	T7_T0_mem0 += INPUT_mem_r
	S += T7_T0_mem0<=T7_T0

	T7_T0_mem1 = S.Task('T7_T0_mem1', length=1, delay_cost=1)
	T7_T0_mem1 += INPUT_mem_r
	S += T7_T0_mem1<=T7_T0

	T7_T1_in = S.Task('T7_T1_in', length=1, delay_cost=1)
	T7_T1_in += alt(MUL_in)
	T7_T1 = S.Task('T7_T1', length=7, delay_cost=1)
	T7_T1 += alt(MUL)
	S+=T7_T1>=T7_T1_in

	T7_T1_mem0 = S.Task('T7_T1_mem0', length=1, delay_cost=1)
	T7_T1_mem0 += INPUT_mem_r
	S += T7_T1_mem0<=T7_T1

	T7_T1_mem1 = S.Task('T7_T1_mem1', length=1, delay_cost=1)
	T7_T1_mem1 += INPUT_mem_r
	S += T7_T1_mem1<=T7_T1

	T7_T2 = S.Task('T7_T2', length=1, delay_cost=1)
	T7_T2 += alt(ADD)

	T7_T2_mem0 = S.Task('T7_T2_mem0', length=1, delay_cost=1)
	T7_T2_mem0 += INPUT_mem_r
	S += T7_T2_mem0<=T7_T2

	T7_T2_mem1 = S.Task('T7_T2_mem1', length=1, delay_cost=1)
	T7_T2_mem1 += INPUT_mem_r
	S += T7_T2_mem1<=T7_T2

	T7_T3 = S.Task('T7_T3', length=1, delay_cost=1)
	T7_T3 += alt(ADD)

	T7_T3_mem0 = S.Task('T7_T3_mem0', length=1, delay_cost=1)
	T7_T3_mem0 += INPUT_mem_r
	S += T7_T3_mem0<=T7_T3

	T7_T3_mem1 = S.Task('T7_T3_mem1', length=1, delay_cost=1)
	T7_T3_mem1 += INPUT_mem_r
	S += T7_T3_mem1<=T7_T3

	T8_1T0_in = S.Task('T8_1T0_in', length=1, delay_cost=1)
	T8_1T0_in += alt(MUL_in)
	T8_1T0 = S.Task('T8_1T0', length=7, delay_cost=1)
	T8_1T0 += alt(MUL)
	S+=T8_1T0>=T8_1T0_in

	T8_1T0_mem0 = S.Task('T8_1T0_mem0', length=1, delay_cost=1)
	T8_1T0_mem0 += INPUT_mem_r
	S += T8_1T0_mem0<=T8_1T0

	T8_1T0_mem1 = S.Task('T8_1T0_mem1', length=1, delay_cost=1)
	T8_1T0_mem1 += INPUT_mem_r
	S += T8_1T0_mem1<=T8_1T0

	T8_1T1_in = S.Task('T8_1T1_in', length=1, delay_cost=1)
	T8_1T1_in += alt(MUL_in)
	T8_1T1 = S.Task('T8_1T1', length=7, delay_cost=1)
	T8_1T1 += alt(MUL)
	S+=T8_1T1>=T8_1T1_in

	T8_1T1_mem0 = S.Task('T8_1T1_mem0', length=1, delay_cost=1)
	T8_1T1_mem0 += INPUT_mem_r
	S += T8_1T1_mem0<=T8_1T1

	T8_1T1_mem1 = S.Task('T8_1T1_mem1', length=1, delay_cost=1)
	T8_1T1_mem1 += INPUT_mem_r
	S += T8_1T1_mem1<=T8_1T1

	T8_1T2 = S.Task('T8_1T2', length=1, delay_cost=1)
	T8_1T2 += alt(ADD)

	T8_1T2_mem0 = S.Task('T8_1T2_mem0', length=1, delay_cost=1)
	T8_1T2_mem0 += INPUT_mem_r
	S += T8_1T2_mem0<=T8_1T2

	T8_1T2_mem1 = S.Task('T8_1T2_mem1', length=1, delay_cost=1)
	T8_1T2_mem1 += INPUT_mem_r
	S += T8_1T2_mem1<=T8_1T2

	T8_1T3 = S.Task('T8_1T3', length=1, delay_cost=1)
	T8_1T3 += alt(ADD)

	T8_1T3_mem0 = S.Task('T8_1T3_mem0', length=1, delay_cost=1)
	T8_1T3_mem0 += INPUT_mem_r
	S += T8_1T3_mem0<=T8_1T3

	T8_1T3_mem1 = S.Task('T8_1T3_mem1', length=1, delay_cost=1)
	T8_1T3_mem1 += INPUT_mem_r
	S += T8_1T3_mem1<=T8_1T3

	T9_30 = S.Task('T9_30', length=1, delay_cost=1)
	T9_30 += alt(ADD)

	T9_30_mem0 = S.Task('T9_30_mem0', length=1, delay_cost=1)
	T9_30_mem0 += INPUT_mem_r
	S += T9_30_mem0<=T9_30

	T9_30_mem1 = S.Task('T9_30_mem1', length=1, delay_cost=1)
	T9_30_mem1 += INPUT_mem_r
	S += T9_30_mem1<=T9_30

	T9_31 = S.Task('T9_31', length=1, delay_cost=1)
	T9_31 += alt(ADD)

	T9_31_mem0 = S.Task('T9_31_mem0', length=1, delay_cost=1)
	T9_31_mem0 += INPUT_mem_r
	S += T9_31_mem0<=T9_31

	T9_31_mem1 = S.Task('T9_31_mem1', length=1, delay_cost=1)
	T9_31_mem1 += INPUT_mem_r
	S += T9_31_mem1<=T9_31

	T10_0 = S.Task('T10_0', length=1, delay_cost=1)
	T10_0 += alt(ADD)

	T10_0_mem0 = S.Task('T10_0_mem0', length=1, delay_cost=1)
	T10_0_mem0 += INPUT_mem_r
	S += T10_0_mem0<=T10_0

	T10_0_mem1 = S.Task('T10_0_mem1', length=1, delay_cost=1)
	T10_0_mem1 += INPUT_mem_r
	S += T10_0_mem1<=T10_0

	T10_1 = S.Task('T10_1', length=1, delay_cost=1)
	T10_1 += alt(ADD)

	T10_1_mem0 = S.Task('T10_1_mem0', length=1, delay_cost=1)
	T10_1_mem0 += INPUT_mem_r
	S += T10_1_mem0<=T10_1

	T10_1_mem1 = S.Task('T10_1_mem1', length=1, delay_cost=1)
	T10_1_mem1 += INPUT_mem_r
	S += T10_1_mem1<=T10_1

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	T3_0 += alt(ADD)

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	T3_0_mem0 += INPUT_mem_r
	S += T3_0_mem0<=T3_0

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	T3_0_mem1 += INPUT_mem_r
	S += T3_0_mem1<=T3_0

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	T3_1 += alt(ADD)

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	T3_1_mem0 += INPUT_mem_r
	S += T3_1_mem0<=T3_1

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	T3_1_mem1 += INPUT_mem_r
	S += T3_1_mem1<=T3_1

	T4_10 = S.Task('T4_10', length=1, delay_cost=1)
	T4_10 += alt(ADD)

	T4_10_mem0 = S.Task('T4_10_mem0', length=1, delay_cost=1)
	T4_10_mem0 += INPUT_mem_r
	S += T4_10_mem0<=T4_10

	T4_10_mem1 = S.Task('T4_10_mem1', length=1, delay_cost=1)
	T4_10_mem1 += INPUT_mem_r
	S += T4_10_mem1<=T4_10

	T4_11 = S.Task('T4_11', length=1, delay_cost=1)
	T4_11 += alt(ADD)

	T4_11_mem0 = S.Task('T4_11_mem0', length=1, delay_cost=1)
	T4_11_mem0 += INPUT_mem_r
	S += T4_11_mem0<=T4_11

	T4_11_mem1 = S.Task('T4_11_mem1', length=1, delay_cost=1)
	T4_11_mem1 += INPUT_mem_r
	S += T4_11_mem1<=T4_11

	T4_20 = S.Task('T4_20', length=1, delay_cost=1)
	T4_20 += alt(ADD)

	T4_20_mem0 = S.Task('T4_20_mem0', length=1, delay_cost=1)
	T4_20_mem0 += INPUT_mem_r
	S += T4_20_mem0<=T4_20

	T4_20_mem1 = S.Task('T4_20_mem1', length=1, delay_cost=1)
	T4_20_mem1 += INPUT_mem_r
	S += T4_20_mem1<=T4_20

	T4_21 = S.Task('T4_21', length=1, delay_cost=1)
	T4_21 += alt(ADD)

	T4_21_mem0 = S.Task('T4_21_mem0', length=1, delay_cost=1)
	T4_21_mem0 += INPUT_mem_r
	S += T4_21_mem0<=T4_21

	T4_21_mem1 = S.Task('T4_21_mem1', length=1, delay_cost=1)
	T4_21_mem1 += INPUT_mem_r
	S += T4_21_mem1<=T4_21

	T5_10 = S.Task('T5_10', length=1, delay_cost=1)
	T5_10 += alt(ADD)

	T5_10_mem0 = S.Task('T5_10_mem0', length=1, delay_cost=1)
	T5_10_mem0 += INPUT_mem_r
	S += T5_10_mem0<=T5_10

	T5_10_mem1 = S.Task('T5_10_mem1', length=1, delay_cost=1)
	T5_10_mem1 += INPUT_mem_r
	S += T5_10_mem1<=T5_10

	T5_11 = S.Task('T5_11', length=1, delay_cost=1)
	T5_11 += alt(ADD)

	T5_11_mem0 = S.Task('T5_11_mem0', length=1, delay_cost=1)
	T5_11_mem0 += INPUT_mem_r
	S += T5_11_mem0<=T5_11

	T5_11_mem1 = S.Task('T5_11_mem1', length=1, delay_cost=1)
	T5_11_mem1 += INPUT_mem_r
	S += T5_11_mem1<=T5_11

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "square_mul1_add4/square_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_square_mul1_add4_0(0, 0)