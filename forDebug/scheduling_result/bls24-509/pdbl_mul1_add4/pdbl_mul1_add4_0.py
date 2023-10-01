from pyschedule import Scenario, solvers, plotters, alt

def solve_pdbl_mul1_add4_0(ConstStep, ExpStep):
	horizon = 92
	S=Scenario("pdbl_mul1_add4_0",horizon = horizon)

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
	T0a10_new = S.Task('T0a10_new', length=1, delay_cost=1)
	T0a10_new += alt(ADD)

	T0a11_new = S.Task('T0a11_new', length=1, delay_cost=1)
	T0a11_new += alt(ADD)

	T0t10 = S.Task('T0t10', length=1, delay_cost=1)
	T0t10 += alt(ADD)

	T0t11 = S.Task('T0t11', length=1, delay_cost=1)
	T0t11 += alt(ADD)

	T0t0_a0a1_in = S.Task('T0t0_a0a1_in', length=1, delay_cost=1)
	T0t0_a0a1_in += alt(MUL_in)
	T0t0_a0a1 = S.Task('T0t0_a0a1', length=7, delay_cost=1)
	T0t0_a0a1 += alt(MUL)
	S+=T0t0_a0a1>=T0t0_a0a1_in

	T0t1_a0a1_in = S.Task('T0t1_a0a1_in', length=1, delay_cost=1)
	T0t1_a0a1_in += alt(MUL_in)
	T0t1_a0a1 = S.Task('T0t1_a0a1', length=7, delay_cost=1)
	T0t1_a0a1 += alt(MUL)
	S+=T0t1_a0a1>=T0t1_a0a1_in

	T0t2_a0a1 = S.Task('T0t2_a0a1', length=1, delay_cost=1)
	T0t2_a0a1 += alt(ADD)

	T1a10_new = S.Task('T1a10_new', length=1, delay_cost=1)
	T1a10_new += alt(ADD)

	T1a11_new = S.Task('T1a11_new', length=1, delay_cost=1)
	T1a11_new += alt(ADD)

	T1t10 = S.Task('T1t10', length=1, delay_cost=1)
	T1t10 += alt(ADD)

	T1t11 = S.Task('T1t11', length=1, delay_cost=1)
	T1t11 += alt(ADD)

	T1t0_a0a1_in = S.Task('T1t0_a0a1_in', length=1, delay_cost=1)
	T1t0_a0a1_in += alt(MUL_in)
	T1t0_a0a1 = S.Task('T1t0_a0a1', length=7, delay_cost=1)
	T1t0_a0a1 += alt(MUL)
	S+=T1t0_a0a1>=T1t0_a0a1_in

	T1t1_a0a1_in = S.Task('T1t1_a0a1_in', length=1, delay_cost=1)
	T1t1_a0a1_in += alt(MUL_in)
	T1t1_a0a1 = S.Task('T1t1_a0a1', length=7, delay_cost=1)
	T1t1_a0a1 += alt(MUL)
	S+=T1t1_a0a1>=T1t1_a0a1_in

	T1t2_a0a1 = S.Task('T1t2_a0a1', length=1, delay_cost=1)
	T1t2_a0a1 += alt(ADD)

	T2a10_new = S.Task('T2a10_new', length=1, delay_cost=1)
	T2a10_new += alt(ADD)

	T2a11_new = S.Task('T2a11_new', length=1, delay_cost=1)
	T2a11_new += alt(ADD)

	T2t10 = S.Task('T2t10', length=1, delay_cost=1)
	T2t10 += alt(ADD)

	T2t11 = S.Task('T2t11', length=1, delay_cost=1)
	T2t11 += alt(ADD)

	T2t0_a0a1_in = S.Task('T2t0_a0a1_in', length=1, delay_cost=1)
	T2t0_a0a1_in += alt(MUL_in)
	T2t0_a0a1 = S.Task('T2t0_a0a1', length=7, delay_cost=1)
	T2t0_a0a1 += alt(MUL)
	S+=T2t0_a0a1>=T2t0_a0a1_in

	T2t1_a0a1_in = S.Task('T2t1_a0a1_in', length=1, delay_cost=1)
	T2t1_a0a1_in += alt(MUL_in)
	T2t1_a0a1 = S.Task('T2t1_a0a1', length=7, delay_cost=1)
	T2t1_a0a1 += alt(MUL)
	S+=T2t1_a0a1>=T2t1_a0a1_in

	T2t2_a0a1 = S.Task('T2t2_a0a1', length=1, delay_cost=1)
	T2t2_a0a1 += alt(ADD)

	T3_2t3_0 = S.Task('T3_2t3_0', length=1, delay_cost=1)
	T3_2t3_0 += alt(ADD)

	T3_2t3_1 = S.Task('T3_2t3_1', length=1, delay_cost=1)
	T3_2t3_1 += alt(ADD)

	T3_2t3_a0b0 = S.Task('T3_2t3_a0b0', length=1, delay_cost=1)
	T3_2t3_a0b0 += alt(ADD)

	T3_2t3_a1b1 = S.Task('T3_2t3_a1b1', length=1, delay_cost=1)
	T3_2t3_a1b1 += alt(ADD)

	T400 = S.Task('T400', length=1, delay_cost=1)
	T400 += alt(ADD)

	T401 = S.Task('T401', length=1, delay_cost=1)
	T401 += alt(ADD)

	T410 = S.Task('T410', length=1, delay_cost=1)
	T410 += alt(ADD)

	T411 = S.Task('T411', length=1, delay_cost=1)
	T411 += alt(ADD)

	T500 = S.Task('T500', length=1, delay_cost=1)
	T500 += alt(ADD)

	T501 = S.Task('T501', length=1, delay_cost=1)
	T501 += alt(ADD)

	T510 = S.Task('T510', length=1, delay_cost=1)
	T510 += alt(ADD)

	T511 = S.Task('T511', length=1, delay_cost=1)
	T511 += alt(ADD)

	T0a10_new_mem0 = S.Task('T0a10_new_mem0', length=1, delay_cost=1)
	T0a10_new_mem0 += INPUT_mem_r
	S += T0a10_new_mem0<=T0a10_new

	T0a10_new_mem1 = S.Task('T0a10_new_mem1', length=1, delay_cost=1)
	T0a10_new_mem1 += INPUT_mem_r
	S += T0a10_new_mem1<=T0a10_new

	T0a11_new_mem0 = S.Task('T0a11_new_mem0', length=1, delay_cost=1)
	T0a11_new_mem0 += INPUT_mem_r
	S += T0a11_new_mem0<=T0a11_new

	T0a11_new_mem1 = S.Task('T0a11_new_mem1', length=1, delay_cost=1)
	T0a11_new_mem1 += INPUT_mem_r
	S += T0a11_new_mem1<=T0a11_new

	T0t10_mem0 = S.Task('T0t10_mem0', length=1, delay_cost=1)
	T0t10_mem0 += INPUT_mem_r
	S += T0t10_mem0<=T0t10

	T0t10_mem1 = S.Task('T0t10_mem1', length=1, delay_cost=1)
	T0t10_mem1 += INPUT_mem_r
	S += T0t10_mem1<=T0t10

	T0t11_mem0 = S.Task('T0t11_mem0', length=1, delay_cost=1)
	T0t11_mem0 += INPUT_mem_r
	S += T0t11_mem0<=T0t11

	T0t11_mem1 = S.Task('T0t11_mem1', length=1, delay_cost=1)
	T0t11_mem1 += INPUT_mem_r
	S += T0t11_mem1<=T0t11

	T0t0_a0a1_mem0 = S.Task('T0t0_a0a1_mem0', length=1, delay_cost=1)
	T0t0_a0a1_mem0 += INPUT_mem_r
	S += T0t0_a0a1_mem0<=T0t0_a0a1

	T0t0_a0a1_mem1 = S.Task('T0t0_a0a1_mem1', length=1, delay_cost=1)
	T0t0_a0a1_mem1 += INPUT_mem_r
	S += T0t0_a0a1_mem1<=T0t0_a0a1

	T0t1_a0a1_mem0 = S.Task('T0t1_a0a1_mem0', length=1, delay_cost=1)
	T0t1_a0a1_mem0 += INPUT_mem_r
	S += T0t1_a0a1_mem0<=T0t1_a0a1

	T0t1_a0a1_mem1 = S.Task('T0t1_a0a1_mem1', length=1, delay_cost=1)
	T0t1_a0a1_mem1 += INPUT_mem_r
	S += T0t1_a0a1_mem1<=T0t1_a0a1

	T0t2_a0a1_mem0 = S.Task('T0t2_a0a1_mem0', length=1, delay_cost=1)
	T0t2_a0a1_mem0 += INPUT_mem_r
	S += T0t2_a0a1_mem0<=T0t2_a0a1

	T0t2_a0a1_mem1 = S.Task('T0t2_a0a1_mem1', length=1, delay_cost=1)
	T0t2_a0a1_mem1 += INPUT_mem_r
	S += T0t2_a0a1_mem1<=T0t2_a0a1

	T1a10_new_mem0 = S.Task('T1a10_new_mem0', length=1, delay_cost=1)
	T1a10_new_mem0 += INPUT_mem_r
	S += T1a10_new_mem0<=T1a10_new

	T1a10_new_mem1 = S.Task('T1a10_new_mem1', length=1, delay_cost=1)
	T1a10_new_mem1 += INPUT_mem_r
	S += T1a10_new_mem1<=T1a10_new

	T1a11_new_mem0 = S.Task('T1a11_new_mem0', length=1, delay_cost=1)
	T1a11_new_mem0 += INPUT_mem_r
	S += T1a11_new_mem0<=T1a11_new

	T1a11_new_mem1 = S.Task('T1a11_new_mem1', length=1, delay_cost=1)
	T1a11_new_mem1 += INPUT_mem_r
	S += T1a11_new_mem1<=T1a11_new

	T1t10_mem0 = S.Task('T1t10_mem0', length=1, delay_cost=1)
	T1t10_mem0 += INPUT_mem_r
	S += T1t10_mem0<=T1t10

	T1t10_mem1 = S.Task('T1t10_mem1', length=1, delay_cost=1)
	T1t10_mem1 += INPUT_mem_r
	S += T1t10_mem1<=T1t10

	T1t11_mem0 = S.Task('T1t11_mem0', length=1, delay_cost=1)
	T1t11_mem0 += INPUT_mem_r
	S += T1t11_mem0<=T1t11

	T1t11_mem1 = S.Task('T1t11_mem1', length=1, delay_cost=1)
	T1t11_mem1 += INPUT_mem_r
	S += T1t11_mem1<=T1t11

	T1t0_a0a1_mem0 = S.Task('T1t0_a0a1_mem0', length=1, delay_cost=1)
	T1t0_a0a1_mem0 += INPUT_mem_r
	S += T1t0_a0a1_mem0<=T1t0_a0a1

	T1t0_a0a1_mem1 = S.Task('T1t0_a0a1_mem1', length=1, delay_cost=1)
	T1t0_a0a1_mem1 += INPUT_mem_r
	S += T1t0_a0a1_mem1<=T1t0_a0a1

	T1t1_a0a1_mem0 = S.Task('T1t1_a0a1_mem0', length=1, delay_cost=1)
	T1t1_a0a1_mem0 += INPUT_mem_r
	S += T1t1_a0a1_mem0<=T1t1_a0a1

	T1t1_a0a1_mem1 = S.Task('T1t1_a0a1_mem1', length=1, delay_cost=1)
	T1t1_a0a1_mem1 += INPUT_mem_r
	S += T1t1_a0a1_mem1<=T1t1_a0a1

	T1t2_a0a1_mem0 = S.Task('T1t2_a0a1_mem0', length=1, delay_cost=1)
	T1t2_a0a1_mem0 += INPUT_mem_r
	S += T1t2_a0a1_mem0<=T1t2_a0a1

	T1t2_a0a1_mem1 = S.Task('T1t2_a0a1_mem1', length=1, delay_cost=1)
	T1t2_a0a1_mem1 += INPUT_mem_r
	S += T1t2_a0a1_mem1<=T1t2_a0a1

	T2a10_new_mem0 = S.Task('T2a10_new_mem0', length=1, delay_cost=1)
	T2a10_new_mem0 += INPUT_mem_r
	S += T2a10_new_mem0<=T2a10_new

	T2a10_new_mem1 = S.Task('T2a10_new_mem1', length=1, delay_cost=1)
	T2a10_new_mem1 += INPUT_mem_r
	S += T2a10_new_mem1<=T2a10_new

	T2a11_new_mem0 = S.Task('T2a11_new_mem0', length=1, delay_cost=1)
	T2a11_new_mem0 += INPUT_mem_r
	S += T2a11_new_mem0<=T2a11_new

	T2a11_new_mem1 = S.Task('T2a11_new_mem1', length=1, delay_cost=1)
	T2a11_new_mem1 += INPUT_mem_r
	S += T2a11_new_mem1<=T2a11_new

	T2t10_mem0 = S.Task('T2t10_mem0', length=1, delay_cost=1)
	T2t10_mem0 += INPUT_mem_r
	S += T2t10_mem0<=T2t10

	T2t10_mem1 = S.Task('T2t10_mem1', length=1, delay_cost=1)
	T2t10_mem1 += INPUT_mem_r
	S += T2t10_mem1<=T2t10

	T2t11_mem0 = S.Task('T2t11_mem0', length=1, delay_cost=1)
	T2t11_mem0 += INPUT_mem_r
	S += T2t11_mem0<=T2t11

	T2t11_mem1 = S.Task('T2t11_mem1', length=1, delay_cost=1)
	T2t11_mem1 += INPUT_mem_r
	S += T2t11_mem1<=T2t11

	T2t0_a0a1_mem0 = S.Task('T2t0_a0a1_mem0', length=1, delay_cost=1)
	T2t0_a0a1_mem0 += INPUT_mem_r
	S += T2t0_a0a1_mem0<=T2t0_a0a1

	T2t0_a0a1_mem1 = S.Task('T2t0_a0a1_mem1', length=1, delay_cost=1)
	T2t0_a0a1_mem1 += INPUT_mem_r
	S += T2t0_a0a1_mem1<=T2t0_a0a1

	T2t1_a0a1_mem0 = S.Task('T2t1_a0a1_mem0', length=1, delay_cost=1)
	T2t1_a0a1_mem0 += INPUT_mem_r
	S += T2t1_a0a1_mem0<=T2t1_a0a1

	T2t1_a0a1_mem1 = S.Task('T2t1_a0a1_mem1', length=1, delay_cost=1)
	T2t1_a0a1_mem1 += INPUT_mem_r
	S += T2t1_a0a1_mem1<=T2t1_a0a1

	T2t2_a0a1_mem0 = S.Task('T2t2_a0a1_mem0', length=1, delay_cost=1)
	T2t2_a0a1_mem0 += INPUT_mem_r
	S += T2t2_a0a1_mem0<=T2t2_a0a1

	T2t2_a0a1_mem1 = S.Task('T2t2_a0a1_mem1', length=1, delay_cost=1)
	T2t2_a0a1_mem1 += INPUT_mem_r
	S += T2t2_a0a1_mem1<=T2t2_a0a1

	T3_2t3_0_mem0 = S.Task('T3_2t3_0_mem0', length=1, delay_cost=1)
	T3_2t3_0_mem0 += INPUT_mem_r
	S += T3_2t3_0_mem0<=T3_2t3_0

	T3_2t3_0_mem1 = S.Task('T3_2t3_0_mem1', length=1, delay_cost=1)
	T3_2t3_0_mem1 += INPUT_mem_r
	S += T3_2t3_0_mem1<=T3_2t3_0

	T3_2t3_1_mem0 = S.Task('T3_2t3_1_mem0', length=1, delay_cost=1)
	T3_2t3_1_mem0 += INPUT_mem_r
	S += T3_2t3_1_mem0<=T3_2t3_1

	T3_2t3_1_mem1 = S.Task('T3_2t3_1_mem1', length=1, delay_cost=1)
	T3_2t3_1_mem1 += INPUT_mem_r
	S += T3_2t3_1_mem1<=T3_2t3_1

	T3_2t3_a0b0_mem0 = S.Task('T3_2t3_a0b0_mem0', length=1, delay_cost=1)
	T3_2t3_a0b0_mem0 += INPUT_mem_r
	S += T3_2t3_a0b0_mem0<=T3_2t3_a0b0

	T3_2t3_a0b0_mem1 = S.Task('T3_2t3_a0b0_mem1', length=1, delay_cost=1)
	T3_2t3_a0b0_mem1 += INPUT_mem_r
	S += T3_2t3_a0b0_mem1<=T3_2t3_a0b0

	T3_2t3_a1b1_mem0 = S.Task('T3_2t3_a1b1_mem0', length=1, delay_cost=1)
	T3_2t3_a1b1_mem0 += INPUT_mem_r
	S += T3_2t3_a1b1_mem0<=T3_2t3_a1b1

	T3_2t3_a1b1_mem1 = S.Task('T3_2t3_a1b1_mem1', length=1, delay_cost=1)
	T3_2t3_a1b1_mem1 += INPUT_mem_r
	S += T3_2t3_a1b1_mem1<=T3_2t3_a1b1

	T400_mem0 = S.Task('T400_mem0', length=1, delay_cost=1)
	T400_mem0 += INPUT_mem_r
	S += T400_mem0<=T400

	T400_mem1 = S.Task('T400_mem1', length=1, delay_cost=1)
	T400_mem1 += INPUT_mem_r
	S += T400_mem1<=T400

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	T401_mem0 += INPUT_mem_r
	S += T401_mem0<=T401

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	T401_mem1 += INPUT_mem_r
	S += T401_mem1<=T401

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	T410_mem0 += INPUT_mem_r
	S += T410_mem0<=T410

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	T410_mem1 += INPUT_mem_r
	S += T410_mem1<=T410

	T411_mem0 = S.Task('T411_mem0', length=1, delay_cost=1)
	T411_mem0 += INPUT_mem_r
	S += T411_mem0<=T411

	T411_mem1 = S.Task('T411_mem1', length=1, delay_cost=1)
	T411_mem1 += INPUT_mem_r
	S += T411_mem1<=T411

	T500_mem0 = S.Task('T500_mem0', length=1, delay_cost=1)
	T500_mem0 += INPUT_mem_r
	S += T500_mem0<=T500

	T500_mem1 = S.Task('T500_mem1', length=1, delay_cost=1)
	T500_mem1 += INPUT_mem_r
	S += T500_mem1<=T500

	T501_mem0 = S.Task('T501_mem0', length=1, delay_cost=1)
	T501_mem0 += INPUT_mem_r
	S += T501_mem0<=T501

	T501_mem1 = S.Task('T501_mem1', length=1, delay_cost=1)
	T501_mem1 += INPUT_mem_r
	S += T501_mem1<=T501

	T510_mem0 = S.Task('T510_mem0', length=1, delay_cost=1)
	T510_mem0 += INPUT_mem_r
	S += T510_mem0<=T510

	T510_mem1 = S.Task('T510_mem1', length=1, delay_cost=1)
	T510_mem1 += INPUT_mem_r
	S += T510_mem1<=T510

	T511_mem0 = S.Task('T511_mem0', length=1, delay_cost=1)
	T511_mem0 += INPUT_mem_r
	S += T511_mem0<=T511

	T511_mem1 = S.Task('T511_mem1', length=1, delay_cost=1)
	T511_mem1 += INPUT_mem_r
	S += T511_mem1<=T511

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "pdbl_mul1_add4/pdbl_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_pdbl_mul1_add4_0(0, 0)