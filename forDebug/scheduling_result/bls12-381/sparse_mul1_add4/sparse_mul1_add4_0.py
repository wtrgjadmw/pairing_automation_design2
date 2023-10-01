from pyschedule import Scenario, solvers, plotters, alt

def solve_sparse_mul1_add4_0(ConstStep, ExpStep):
	horizon = 95
	S=Scenario("sparse_mul1_add4_0",horizon = horizon)

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
	T1T0_in = S.Task('T1T0_in', length=1, delay_cost=1)
	T1T0_in += alt(MUL_in)
	T1T0 = S.Task('T1T0', length=7, delay_cost=1)
	T1T0 += alt(MUL)
	S+=T1T0>=T1T0_in

	T1T0_mem0 = S.Task('T1T0_mem0', length=1, delay_cost=1)
	T1T0_mem0 += INPUT_mem_r
	S += T1T0_mem0<=T1T0

	T1T0_mem1 = S.Task('T1T0_mem1', length=1, delay_cost=1)
	T1T0_mem1 += INPUT_mem_r
	S += T1T0_mem1<=T1T0

	T1T1_in = S.Task('T1T1_in', length=1, delay_cost=1)
	T1T1_in += alt(MUL_in)
	T1T1 = S.Task('T1T1', length=7, delay_cost=1)
	T1T1 += alt(MUL)
	S+=T1T1>=T1T1_in

	T1T1_mem0 = S.Task('T1T1_mem0', length=1, delay_cost=1)
	T1T1_mem0 += INPUT_mem_r
	S += T1T1_mem0<=T1T1

	T1T1_mem1 = S.Task('T1T1_mem1', length=1, delay_cost=1)
	T1T1_mem1 += INPUT_mem_r
	S += T1T1_mem1<=T1T1

	T1T2 = S.Task('T1T2', length=1, delay_cost=1)
	T1T2 += alt(ADD)

	T1T2_mem0 = S.Task('T1T2_mem0', length=1, delay_cost=1)
	T1T2_mem0 += INPUT_mem_r
	S += T1T2_mem0<=T1T2

	T1T2_mem1 = S.Task('T1T2_mem1', length=1, delay_cost=1)
	T1T2_mem1 += INPUT_mem_r
	S += T1T2_mem1<=T1T2

	T1T3 = S.Task('T1T3', length=1, delay_cost=1)
	T1T3 += alt(ADD)

	T1T3_mem0 = S.Task('T1T3_mem0', length=1, delay_cost=1)
	T1T3_mem0 += INPUT_mem_r
	S += T1T3_mem0<=T1T3

	T1T3_mem1 = S.Task('T1T3_mem1', length=1, delay_cost=1)
	T1T3_mem1 += INPUT_mem_r
	S += T1T3_mem1<=T1T3

	T2T0_in = S.Task('T2T0_in', length=1, delay_cost=1)
	T2T0_in += alt(MUL_in)
	T2T0 = S.Task('T2T0', length=7, delay_cost=1)
	T2T0 += alt(MUL)
	S+=T2T0>=T2T0_in

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	T2T0_mem0 += INPUT_mem_r
	S += T2T0_mem0<=T2T0

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	T2T0_mem1 += INPUT_mem_r
	S += T2T0_mem1<=T2T0

	T2T1_in = S.Task('T2T1_in', length=1, delay_cost=1)
	T2T1_in += alt(MUL_in)
	T2T1 = S.Task('T2T1', length=7, delay_cost=1)
	T2T1 += alt(MUL)
	S+=T2T1>=T2T1_in

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	T2T1_mem0 += INPUT_mem_r
	S += T2T1_mem0<=T2T1

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	T2T1_mem1 += INPUT_mem_r
	S += T2T1_mem1<=T2T1

	T2T2 = S.Task('T2T2', length=1, delay_cost=1)
	T2T2 += alt(ADD)

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	T2T2_mem0 += INPUT_mem_r
	S += T2T2_mem0<=T2T2

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	T2T2_mem1 += INPUT_mem_r
	S += T2T2_mem1<=T2T2

	T2T3 = S.Task('T2T3', length=1, delay_cost=1)
	T2T3 += alt(ADD)

	T2T3_mem0 = S.Task('T2T3_mem0', length=1, delay_cost=1)
	T2T3_mem0 += INPUT_mem_r
	S += T2T3_mem0<=T2T3

	T2T3_mem1 = S.Task('T2T3_mem1', length=1, delay_cost=1)
	T2T3_mem1 += INPUT_mem_r
	S += T2T3_mem1<=T2T3

	T0T0_in = S.Task('T0T0_in', length=1, delay_cost=1)
	T0T0_in += alt(MUL_in)
	T0T0 = S.Task('T0T0', length=7, delay_cost=1)
	T0T0 += alt(MUL)
	S+=T0T0>=T0T0_in

	T0T0_mem0 = S.Task('T0T0_mem0', length=1, delay_cost=1)
	T0T0_mem0 += INPUT_mem_r
	S += T0T0_mem0<=T0T0

	T0T0_mem1 = S.Task('T0T0_mem1', length=1, delay_cost=1)
	T0T0_mem1 += INPUT_mem_r
	S += T0T0_mem1<=T0T0

	T0T1_in = S.Task('T0T1_in', length=1, delay_cost=1)
	T0T1_in += alt(MUL_in)
	T0T1 = S.Task('T0T1', length=7, delay_cost=1)
	T0T1 += alt(MUL)
	S+=T0T1>=T0T1_in

	T0T1_mem0 = S.Task('T0T1_mem0', length=1, delay_cost=1)
	T0T1_mem0 += INPUT_mem_r
	S += T0T1_mem0<=T0T1

	T0T1_mem1 = S.Task('T0T1_mem1', length=1, delay_cost=1)
	T0T1_mem1 += INPUT_mem_r
	S += T0T1_mem1<=T0T1

	T0T2 = S.Task('T0T2', length=1, delay_cost=1)
	T0T2 += alt(ADD)

	T0T2_mem0 = S.Task('T0T2_mem0', length=1, delay_cost=1)
	T0T2_mem0 += INPUT_mem_r
	S += T0T2_mem0<=T0T2

	T0T2_mem1 = S.Task('T0T2_mem1', length=1, delay_cost=1)
	T0T2_mem1 += INPUT_mem_r
	S += T0T2_mem1<=T0T2

	T0T3 = S.Task('T0T3', length=1, delay_cost=1)
	T0T3 += alt(ADD)

	T0T3_mem0 = S.Task('T0T3_mem0', length=1, delay_cost=1)
	T0T3_mem0 += INPUT_mem_r
	S += T0T3_mem0<=T0T3

	T0T3_mem1 = S.Task('T0T3_mem1', length=1, delay_cost=1)
	T0T3_mem1 += INPUT_mem_r
	S += T0T3_mem1<=T0T3

	T3T0_in = S.Task('T3T0_in', length=1, delay_cost=1)
	T3T0_in += alt(MUL_in)
	T3T0 = S.Task('T3T0', length=7, delay_cost=1)
	T3T0 += alt(MUL)
	S+=T3T0>=T3T0_in

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	T3T0_mem0 += INPUT_mem_r
	S += T3T0_mem0<=T3T0

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	T3T0_mem1 += INPUT_mem_r
	S += T3T0_mem1<=T3T0

	T3T1_in = S.Task('T3T1_in', length=1, delay_cost=1)
	T3T1_in += alt(MUL_in)
	T3T1 = S.Task('T3T1', length=7, delay_cost=1)
	T3T1 += alt(MUL)
	S+=T3T1>=T3T1_in

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	T3T1_mem0 += INPUT_mem_r
	S += T3T1_mem0<=T3T1

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	T3T1_mem1 += INPUT_mem_r
	S += T3T1_mem1<=T3T1

	T3T2 = S.Task('T3T2', length=1, delay_cost=1)
	T3T2 += alt(ADD)

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	T3T2_mem0 += INPUT_mem_r
	S += T3T2_mem0<=T3T2

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	T3T2_mem1 += INPUT_mem_r
	S += T3T2_mem1<=T3T2

	T3T3 = S.Task('T3T3', length=1, delay_cost=1)
	T3T3 += alt(ADD)

	T3T3_mem0 = S.Task('T3T3_mem0', length=1, delay_cost=1)
	T3T3_mem0 += INPUT_mem_r
	S += T3T3_mem0<=T3T3

	T3T3_mem1 = S.Task('T3T3_mem1', length=1, delay_cost=1)
	T3T3_mem1 += INPUT_mem_r
	S += T3T3_mem1<=T3T3

	T4T0_in = S.Task('T4T0_in', length=1, delay_cost=1)
	T4T0_in += alt(MUL_in)
	T4T0 = S.Task('T4T0', length=7, delay_cost=1)
	T4T0 += alt(MUL)
	S+=T4T0>=T4T0_in

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	T4T0_mem0 += INPUT_mem_r
	S += T4T0_mem0<=T4T0

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	T4T0_mem1 += INPUT_mem_r
	S += T4T0_mem1<=T4T0

	T4T1_in = S.Task('T4T1_in', length=1, delay_cost=1)
	T4T1_in += alt(MUL_in)
	T4T1 = S.Task('T4T1', length=7, delay_cost=1)
	T4T1 += alt(MUL)
	S+=T4T1>=T4T1_in

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	T4T1_mem0 += INPUT_mem_r
	S += T4T1_mem0<=T4T1

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	T4T1_mem1 += INPUT_mem_r
	S += T4T1_mem1<=T4T1

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	T4T2 += alt(ADD)

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	T4T2_mem0 += INPUT_mem_r
	S += T4T2_mem0<=T4T2

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	T4T2_mem1 += INPUT_mem_r
	S += T4T2_mem1<=T4T2

	T4T3 = S.Task('T4T3', length=1, delay_cost=1)
	T4T3 += alt(ADD)

	T4T3_mem0 = S.Task('T4T3_mem0', length=1, delay_cost=1)
	T4T3_mem0 += INPUT_mem_r
	S += T4T3_mem0<=T4T3

	T4T3_mem1 = S.Task('T4T3_mem1', length=1, delay_cost=1)
	T4T3_mem1 += INPUT_mem_r
	S += T4T3_mem1<=T4T3

	T5T0_in = S.Task('T5T0_in', length=1, delay_cost=1)
	T5T0_in += alt(MUL_in)
	T5T0 = S.Task('T5T0', length=7, delay_cost=1)
	T5T0 += alt(MUL)
	S+=T5T0>=T5T0_in

	T5T0_mem0 = S.Task('T5T0_mem0', length=1, delay_cost=1)
	T5T0_mem0 += INPUT_mem_r
	S += T5T0_mem0<=T5T0

	T5T0_mem1 = S.Task('T5T0_mem1', length=1, delay_cost=1)
	T5T0_mem1 += INPUT_mem_r
	S += T5T0_mem1<=T5T0

	T5T1_in = S.Task('T5T1_in', length=1, delay_cost=1)
	T5T1_in += alt(MUL_in)
	T5T1 = S.Task('T5T1', length=7, delay_cost=1)
	T5T1 += alt(MUL)
	S+=T5T1>=T5T1_in

	T5T1_mem0 = S.Task('T5T1_mem0', length=1, delay_cost=1)
	T5T1_mem0 += INPUT_mem_r
	S += T5T1_mem0<=T5T1

	T5T1_mem1 = S.Task('T5T1_mem1', length=1, delay_cost=1)
	T5T1_mem1 += INPUT_mem_r
	S += T5T1_mem1<=T5T1

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	T5T2 += alt(ADD)

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	T5T2_mem0 += INPUT_mem_r
	S += T5T2_mem0<=T5T2

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	T5T2_mem1 += INPUT_mem_r
	S += T5T2_mem1<=T5T2

	T5T3 = S.Task('T5T3', length=1, delay_cost=1)
	T5T3 += alt(ADD)

	T5T3_mem0 = S.Task('T5T3_mem0', length=1, delay_cost=1)
	T5T3_mem0 += INPUT_mem_r
	S += T5T3_mem0<=T5T3

	T5T3_mem1 = S.Task('T5T3_mem1', length=1, delay_cost=1)
	T5T3_mem1 += INPUT_mem_r
	S += T5T3_mem1<=T5T3

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += INPUT_mem_r
	S += T60_mem0<=T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += INPUT_mem_r
	S += T60_mem1<=T60

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += INPUT_mem_r
	S += T61_mem0<=T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += INPUT_mem_r
	S += T61_mem1<=T61

	T70 = S.Task('T70', length=1, delay_cost=1)
	T70 += alt(ADD)

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	T70_mem0 += INPUT_mem_r
	S += T70_mem0<=T70

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	T70_mem1 += INPUT_mem_r
	S += T70_mem1<=T70

	T71 = S.Task('T71', length=1, delay_cost=1)
	T71 += alt(ADD)

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	T71_mem0 += INPUT_mem_r
	S += T71_mem0<=T71

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	T71_mem1 += INPUT_mem_r
	S += T71_mem1<=T71

	T6_1T0_in = S.Task('T6_1T0_in', length=1, delay_cost=1)
	T6_1T0_in += alt(MUL_in)
	T6_1T0 = S.Task('T6_1T0', length=7, delay_cost=1)
	T6_1T0 += alt(MUL)
	S+=T6_1T0>=T6_1T0_in

	T6_1T0_mem0 = S.Task('T6_1T0_mem0', length=1, delay_cost=1)
	T6_1T0_mem0 += INPUT_mem_r
	S += T6_1T0_mem0<=T6_1T0

	T6_1T0_mem1 = S.Task('T6_1T0_mem1', length=1, delay_cost=1)
	T6_1T0_mem1 += INPUT_mem_r
	S += T6_1T0_mem1<=T6_1T0

	T6_1T1_in = S.Task('T6_1T1_in', length=1, delay_cost=1)
	T6_1T1_in += alt(MUL_in)
	T6_1T1 = S.Task('T6_1T1', length=7, delay_cost=1)
	T6_1T1 += alt(MUL)
	S+=T6_1T1>=T6_1T1_in

	T6_1T1_mem0 = S.Task('T6_1T1_mem0', length=1, delay_cost=1)
	T6_1T1_mem0 += INPUT_mem_r
	S += T6_1T1_mem0<=T6_1T1

	T6_1T1_mem1 = S.Task('T6_1T1_mem1', length=1, delay_cost=1)
	T6_1T1_mem1 += INPUT_mem_r
	S += T6_1T1_mem1<=T6_1T1

	T6_1T2 = S.Task('T6_1T2', length=1, delay_cost=1)
	T6_1T2 += alt(ADD)

	T6_1T2_mem0 = S.Task('T6_1T2_mem0', length=1, delay_cost=1)
	T6_1T2_mem0 += INPUT_mem_r
	S += T6_1T2_mem0<=T6_1T2

	T6_1T2_mem1 = S.Task('T6_1T2_mem1', length=1, delay_cost=1)
	T6_1T2_mem1 += INPUT_mem_r
	S += T6_1T2_mem1<=T6_1T2

	T6_1T3 = S.Task('T6_1T3', length=1, delay_cost=1)
	T6_1T3 += alt(ADD)

	T6_1T3_mem0 = S.Task('T6_1T3_mem0', length=1, delay_cost=1)
	T6_1T3_mem0 += INPUT_mem_r
	S += T6_1T3_mem0<=T6_1T3

	T6_1T3_mem1 = S.Task('T6_1T3_mem1', length=1, delay_cost=1)
	T6_1T3_mem1 += INPUT_mem_r
	S += T6_1T3_mem1<=T6_1T3

	T130 = S.Task('T130', length=1, delay_cost=1)
	T130 += alt(ADD)

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	T130_mem0 += INPUT_mem_r
	S += T130_mem0<=T130

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	T130_mem1 += INPUT_mem_r
	S += T130_mem1<=T130

	T131 = S.Task('T131', length=1, delay_cost=1)
	T131 += alt(ADD)

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	T131_mem0 += INPUT_mem_r
	S += T131_mem0<=T131

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	T131_mem1 += INPUT_mem_r
	S += T131_mem1<=T131

	T140 = S.Task('T140', length=1, delay_cost=1)
	T140 += alt(ADD)

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	T140_mem0 += INPUT_mem_r
	S += T140_mem0<=T140

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	T140_mem1 += INPUT_mem_r
	S += T140_mem1<=T140

	T141 = S.Task('T141', length=1, delay_cost=1)
	T141 += alt(ADD)

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	T141_mem0 += INPUT_mem_r
	S += T141_mem0<=T141

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	T141_mem1 += INPUT_mem_r
	S += T141_mem1<=T141

	T150 = S.Task('T150', length=1, delay_cost=1)
	T150 += alt(ADD)

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	T150_mem0 += INPUT_mem_r
	S += T150_mem0<=T150

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	T150_mem1 += INPUT_mem_r
	S += T150_mem1<=T150

	T151 = S.Task('T151', length=1, delay_cost=1)
	T151 += alt(ADD)

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	T151_mem0 += INPUT_mem_r
	S += T151_mem0<=T151

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	T151_mem1 += INPUT_mem_r
	S += T151_mem1<=T151

	T160 = S.Task('T160', length=1, delay_cost=1)
	T160 += alt(ADD)

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	T160_mem0 += INPUT_mem_r
	S += T160_mem0<=T160

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	T160_mem1 += INPUT_mem_r
	S += T160_mem1<=T160

	T161 = S.Task('T161', length=1, delay_cost=1)
	T161 += alt(ADD)

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	T161_mem0 += INPUT_mem_r
	S += T161_mem0<=T161

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	T161_mem1 += INPUT_mem_r
	S += T161_mem1<=T161

	T3_T2 = S.Task('T3_T2', length=1, delay_cost=1)
	T3_T2 += alt(ADD)

	T3_T2_mem0 = S.Task('T3_T2_mem0', length=1, delay_cost=1)
	T3_T2_mem0 += INPUT_mem_r
	S += T3_T2_mem0<=T3_T2

	T3_T2_mem1 = S.Task('T3_T2_mem1', length=1, delay_cost=1)
	T3_T2_mem1 += INPUT_mem_r
	S += T3_T2_mem1<=T3_T2

	T9_1T2 = S.Task('T9_1T2', length=1, delay_cost=1)
	T9_1T2 += alt(ADD)

	T9_1T2_mem0 = S.Task('T9_1T2_mem0', length=1, delay_cost=1)
	T9_1T2_mem0 += INPUT_mem_r
	S += T9_1T2_mem0<=T9_1T2

	T9_1T2_mem1 = S.Task('T9_1T2_mem1', length=1, delay_cost=1)
	T9_1T2_mem1 += INPUT_mem_r
	S += T9_1T2_mem1<=T9_1T2

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "sparse_mul1_add4/sparse_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_sparse_mul1_add4_0(0, 0)