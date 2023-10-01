from pyschedule import Scenario, solvers, plotters, alt

def solve_padd_mul1_add4_0(ConstStep, ExpStep):
	horizon = 90
	S=Scenario("padd_mul1_add4_0",horizon = horizon)

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

	T5T2 = S.Task('T5T2', length=1, delay_cost=1)
	T5T2 += alt(ADD)

	T5T2_mem0 = S.Task('T5T2_mem0', length=1, delay_cost=1)
	T5T2_mem0 += INPUT_mem_r
	S += T5T2_mem0<=T5T2

	T5T2_mem1 = S.Task('T5T2_mem1', length=1, delay_cost=1)
	T5T2_mem1 += INPUT_mem_r
	S += T5T2_mem1<=T5T2

	T3_T2 = S.Task('T3_T2', length=1, delay_cost=1)
	T3_T2 += alt(ADD)

	T3_T2_mem0 = S.Task('T3_T2_mem0', length=1, delay_cost=1)
	T3_T2_mem0 += INPUT_mem_r
	S += T3_T2_mem0<=T3_T2

	T3_T2_mem1 = S.Task('T3_T2_mem1', length=1, delay_cost=1)
	T3_T2_mem1 += INPUT_mem_r
	S += T3_T2_mem1<=T3_T2

	T8T2 = S.Task('T8T2', length=1, delay_cost=1)
	T8T2 += alt(ADD)

	T8T2_mem0 = S.Task('T8T2_mem0', length=1, delay_cost=1)
	T8T2_mem0 += INPUT_mem_r
	S += T8T2_mem0<=T8T2

	T8T2_mem1 = S.Task('T8T2_mem1', length=1, delay_cost=1)
	T8T2_mem1 += INPUT_mem_r
	S += T8T2_mem1<=T8T2

	NEW_TZT2 = S.Task('NEW_TZT2', length=1, delay_cost=1)
	NEW_TZT2 += alt(ADD)

	NEW_TZT2_mem0 = S.Task('NEW_TZT2_mem0', length=1, delay_cost=1)
	NEW_TZT2_mem0 += INPUT_mem_r
	S += NEW_TZT2_mem0<=NEW_TZT2

	NEW_TZT2_mem1 = S.Task('NEW_TZT2_mem1', length=1, delay_cost=1)
	NEW_TZT2_mem1 += INPUT_mem_r
	S += NEW_TZT2_mem1<=NEW_TZT2

	C00T2 = S.Task('C00T2', length=1, delay_cost=1)
	C00T2 += alt(ADD)

	C00T2_mem0 = S.Task('C00T2_mem0', length=1, delay_cost=1)
	C00T2_mem0 += INPUT_mem_r
	S += C00T2_mem0<=C00T2

	C00T2_mem1 = S.Task('C00T2_mem1', length=1, delay_cost=1)
	C00T2_mem1 += INPUT_mem_r
	S += C00T2_mem1<=C00T2

	T0_1T2 = S.Task('T0_1T2', length=1, delay_cost=1)
	T0_1T2 += alt(ADD)

	T0_1T2_mem0 = S.Task('T0_1T2_mem0', length=1, delay_cost=1)
	T0_1T2_mem0 += INPUT_mem_r
	S += T0_1T2_mem0<=T0_1T2

	T0_1T2_mem1 = S.Task('T0_1T2_mem1', length=1, delay_cost=1)
	T0_1T2_mem1 += INPUT_mem_r
	S += T0_1T2_mem1<=T0_1T2

	T0T4_in = S.Task('T0T4_in', length=1, delay_cost=1)
	T0T4_in += alt(MUL_in)
	T0T4 = S.Task('T0T4', length=7, delay_cost=1)
	T0T4 += alt(MUL)
	S+=T0T4>=T0T4_in

	T0T4_mem0 = S.Task('T0T4_mem0', length=1, delay_cost=1)
	T0T4_mem0 += alt(ADD_mem)
	S += (T0T2*ADD[0])-1<T0T4_mem0*ADD_mem[0]
	S += (T0T2*ADD[1])-1<T0T4_mem0*ADD_mem[1]
	S += (T0T2*ADD[2])-1<T0T4_mem0*ADD_mem[2]
	S += (T0T2*ADD[3])-1<T0T4_mem0*ADD_mem[3]
	S += T0T4_mem0<=T0T4

	T0T4_mem1 = S.Task('T0T4_mem1', length=1, delay_cost=1)
	T0T4_mem1 += alt(ADD_mem)
	S += (T0T3*ADD[0])-1<T0T4_mem1*ADD_mem[0]
	S += (T0T3*ADD[1])-1<T0T4_mem1*ADD_mem[1]
	S += (T0T3*ADD[2])-1<T0T4_mem1*ADD_mem[2]
	S += (T0T3*ADD[3])-1<T0T4_mem1*ADD_mem[3]
	S += T0T4_mem1<=T0T4

	T0T5 = S.Task('T0T5', length=1, delay_cost=1)
	T0T5 += alt(ADD)

	T0T5_mem0 = S.Task('T0T5_mem0', length=1, delay_cost=1)
	T0T5_mem0 += alt(MUL_mem)
	S += (T0T0*MUL[0])-1<T0T5_mem0*MUL_mem[0]
	S += T0T5_mem0<=T0T5

	T0T5_mem1 = S.Task('T0T5_mem1', length=1, delay_cost=1)
	T0T5_mem1 += alt(MUL_mem)
	S += (T0T1*MUL[0])-1<T0T5_mem1*MUL_mem[0]
	S += T0T5_mem1<=T0T5

	T00 = S.Task('T00', length=1, delay_cost=1)
	T00 += alt(ADD)

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	T00_mem0 += alt(MUL_mem)
	S += (T0T0*MUL[0])-1<T00_mem0*MUL_mem[0]
	S += T00_mem0<=T00

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	T00_mem1 += alt(MUL_mem)
	S += (T0T1*MUL[0])-1<T00_mem1*MUL_mem[0]
	S += T00_mem1<=T00

	T1T4_in = S.Task('T1T4_in', length=1, delay_cost=1)
	T1T4_in += alt(MUL_in)
	T1T4 = S.Task('T1T4', length=7, delay_cost=1)
	T1T4 += alt(MUL)
	S+=T1T4>=T1T4_in

	T1T4_mem0 = S.Task('T1T4_mem0', length=1, delay_cost=1)
	T1T4_mem0 += alt(ADD_mem)
	S += (T1T2*ADD[0])-1<T1T4_mem0*ADD_mem[0]
	S += (T1T2*ADD[1])-1<T1T4_mem0*ADD_mem[1]
	S += (T1T2*ADD[2])-1<T1T4_mem0*ADD_mem[2]
	S += (T1T2*ADD[3])-1<T1T4_mem0*ADD_mem[3]
	S += T1T4_mem0<=T1T4

	T1T4_mem1 = S.Task('T1T4_mem1', length=1, delay_cost=1)
	T1T4_mem1 += alt(ADD_mem)
	S += (T1T3*ADD[0])-1<T1T4_mem1*ADD_mem[0]
	S += (T1T3*ADD[1])-1<T1T4_mem1*ADD_mem[1]
	S += (T1T3*ADD[2])-1<T1T4_mem1*ADD_mem[2]
	S += (T1T3*ADD[3])-1<T1T4_mem1*ADD_mem[3]
	S += T1T4_mem1<=T1T4

	T1T5 = S.Task('T1T5', length=1, delay_cost=1)
	T1T5 += alt(ADD)

	T1T5_mem0 = S.Task('T1T5_mem0', length=1, delay_cost=1)
	T1T5_mem0 += alt(MUL_mem)
	S += (T1T0*MUL[0])-1<T1T5_mem0*MUL_mem[0]
	S += T1T5_mem0<=T1T5

	T1T5_mem1 = S.Task('T1T5_mem1', length=1, delay_cost=1)
	T1T5_mem1 += alt(MUL_mem)
	S += (T1T1*MUL[0])-1<T1T5_mem1*MUL_mem[0]
	S += T1T5_mem1<=T1T5

	T10 = S.Task('T10', length=1, delay_cost=1)
	T10 += alt(ADD)

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += alt(MUL_mem)
	S += (T1T0*MUL[0])-1<T10_mem0*MUL_mem[0]
	S += T10_mem0<=T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += alt(MUL_mem)
	S += (T1T1*MUL[0])-1<T10_mem1*MUL_mem[0]
	S += T10_mem1<=T10

	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += alt(MUL_mem)
	S += (T0T4*MUL[0])-1<T01_mem0*MUL_mem[0]
	S += T01_mem0<=T01

	T01_mem1 = S.Task('T01_mem1', length=1, delay_cost=1)
	T01_mem1 += alt(ADD_mem)
	S += (T0T5*ADD[0])-1<T01_mem1*ADD_mem[0]
	S += (T0T5*ADD[1])-1<T01_mem1*ADD_mem[1]
	S += (T0T5*ADD[2])-1<T01_mem1*ADD_mem[2]
	S += (T0T5*ADD[3])-1<T01_mem1*ADD_mem[3]
	S += T01_mem1<=T01

	T0_0 = S.Task('T0_0', length=1, delay_cost=1)
	T0_0 += alt(ADD)

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	T0_0_mem0 += INPUT_mem_r
	S += T0_0_mem0<=T0_0

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	T0_0_mem1 += alt(ADD_mem)
	S += (T00*ADD[0])-1<T0_0_mem1*ADD_mem[0]
	S += (T00*ADD[1])-1<T0_0_mem1*ADD_mem[1]
	S += (T00*ADD[2])-1<T0_0_mem1*ADD_mem[2]
	S += (T00*ADD[3])-1<T0_0_mem1*ADD_mem[3]
	S += T0_0_mem1<=T0_0

	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(ADD)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += alt(MUL_mem)
	S += (T1T4*MUL[0])-1<T11_mem0*MUL_mem[0]
	S += T11_mem0<=T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += alt(ADD_mem)
	S += (T1T5*ADD[0])-1<T11_mem1*ADD_mem[0]
	S += (T1T5*ADD[1])-1<T11_mem1*ADD_mem[1]
	S += (T1T5*ADD[2])-1<T11_mem1*ADD_mem[2]
	S += (T1T5*ADD[3])-1<T11_mem1*ADD_mem[3]
	S += T11_mem1<=T11

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	T1_0 += alt(ADD)

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	T1_0_mem0 += INPUT_mem_r
	S += T1_0_mem0<=T1_0

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	T1_0_mem1 += alt(ADD_mem)
	S += (T10*ADD[0])-1<T1_0_mem1*ADD_mem[0]
	S += (T10*ADD[1])-1<T1_0_mem1*ADD_mem[1]
	S += (T10*ADD[2])-1<T1_0_mem1*ADD_mem[2]
	S += (T10*ADD[3])-1<T1_0_mem1*ADD_mem[3]
	S += T1_0_mem1<=T1_0

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	T0_1 += alt(ADD)

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	T0_1_mem0 += INPUT_mem_r
	S += T0_1_mem0<=T0_1

	T0_1_mem1 = S.Task('T0_1_mem1', length=1, delay_cost=1)
	T0_1_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<T0_1_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<T0_1_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<T0_1_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<T0_1_mem1*ADD_mem[3]
	S += T0_1_mem1<=T0_1

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	T1_1 += alt(ADD)

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	T1_1_mem0 += INPUT_mem_r
	S += T1_1_mem0<=T1_1

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	T1_1_mem1 += alt(ADD_mem)
	S += (T11*ADD[0])-1<T1_1_mem1*ADD_mem[0]
	S += (T11*ADD[1])-1<T1_1_mem1*ADD_mem[1]
	S += (T11*ADD[2])-1<T1_1_mem1*ADD_mem[2]
	S += (T11*ADD[3])-1<T1_1_mem1*ADD_mem[3]
	S += T1_1_mem1<=T1_1

	C00T0_in = S.Task('C00T0_in', length=1, delay_cost=1)
	C00T0_in += alt(MUL_in)
	C00T0 = S.Task('C00T0', length=7, delay_cost=1)
	C00T0 += alt(MUL)
	S+=C00T0>=C00T0_in

	C00T0_mem0 = S.Task('C00T0_mem0', length=1, delay_cost=1)
	C00T0_mem0 += INPUT_mem_r
	S += C00T0_mem0<=C00T0

	C00T0_mem1 = S.Task('C00T0_mem1', length=1, delay_cost=1)
	C00T0_mem1 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<C00T0_mem1*ADD_mem[0]
	S += (T1_0*ADD[1])-1<C00T0_mem1*ADD_mem[1]
	S += (T1_0*ADD[2])-1<C00T0_mem1*ADD_mem[2]
	S += (T1_0*ADD[3])-1<C00T0_mem1*ADD_mem[3]
	S += C00T0_mem1<=C00T0

	T0_1T0_in = S.Task('T0_1T0_in', length=1, delay_cost=1)
	T0_1T0_in += alt(MUL_in)
	T0_1T0 = S.Task('T0_1T0', length=7, delay_cost=1)
	T0_1T0 += alt(MUL)
	S+=T0_1T0>=T0_1T0_in

	T0_1T0_mem0 = S.Task('T0_1T0_mem0', length=1, delay_cost=1)
	T0_1T0_mem0 += INPUT_mem_r
	S += T0_1T0_mem0<=T0_1T0

	T0_1T0_mem1 = S.Task('T0_1T0_mem1', length=1, delay_cost=1)
	T0_1T0_mem1 += alt(ADD_mem)
	S += (T0_0*ADD[0])-1<T0_1T0_mem1*ADD_mem[0]
	S += (T0_0*ADD[1])-1<T0_1T0_mem1*ADD_mem[1]
	S += (T0_0*ADD[2])-1<T0_1T0_mem1*ADD_mem[2]
	S += (T0_0*ADD[3])-1<T0_1T0_mem1*ADD_mem[3]
	S += T0_1T0_mem1<=T0_1T0

	T2T0 = S.Task('T2T0', length=1, delay_cost=1)
	T2T0 += alt(ADD)

	T2T0_mem0 = S.Task('T2T0_mem0', length=1, delay_cost=1)
	T2T0_mem0 += alt(ADD_mem)
	S += (T0_0*ADD[0])-1<T2T0_mem0*ADD_mem[0]
	S += (T0_0*ADD[1])-1<T2T0_mem0*ADD_mem[1]
	S += (T0_0*ADD[2])-1<T2T0_mem0*ADD_mem[2]
	S += (T0_0*ADD[3])-1<T2T0_mem0*ADD_mem[3]
	S += T2T0_mem0<=T2T0

	T2T0_mem1 = S.Task('T2T0_mem1', length=1, delay_cost=1)
	T2T0_mem1 += alt(ADD_mem)
	S += (T0_1*ADD[0])-1<T2T0_mem1*ADD_mem[0]
	S += (T0_1*ADD[1])-1<T2T0_mem1*ADD_mem[1]
	S += (T0_1*ADD[2])-1<T2T0_mem1*ADD_mem[2]
	S += (T0_1*ADD[3])-1<T2T0_mem1*ADD_mem[3]
	S += T2T0_mem1<=T2T0

	T2T1 = S.Task('T2T1', length=1, delay_cost=1)
	T2T1 += alt(ADD)

	T2T1_mem0 = S.Task('T2T1_mem0', length=1, delay_cost=1)
	T2T1_mem0 += alt(ADD_mem)
	S += (T0_0*ADD[0])-1<T2T1_mem0*ADD_mem[0]
	S += (T0_0*ADD[1])-1<T2T1_mem0*ADD_mem[1]
	S += (T0_0*ADD[2])-1<T2T1_mem0*ADD_mem[2]
	S += (T0_0*ADD[3])-1<T2T1_mem0*ADD_mem[3]
	S += T2T1_mem0<=T2T1

	T2T1_mem1 = S.Task('T2T1_mem1', length=1, delay_cost=1)
	T2T1_mem1 += alt(ADD_mem)
	S += (T0_1*ADD[0])-1<T2T1_mem1*ADD_mem[0]
	S += (T0_1*ADD[1])-1<T2T1_mem1*ADD_mem[1]
	S += (T0_1*ADD[2])-1<T2T1_mem1*ADD_mem[2]
	S += (T0_1*ADD[3])-1<T2T1_mem1*ADD_mem[3]
	S += T2T1_mem1<=T2T1

	T2T2_in = S.Task('T2T2_in', length=1, delay_cost=1)
	T2T2_in += alt(MUL_in)
	T2T2 = S.Task('T2T2', length=7, delay_cost=1)
	T2T2 += alt(MUL)
	S+=T2T2>=T2T2_in

	T2T2_mem0 = S.Task('T2T2_mem0', length=1, delay_cost=1)
	T2T2_mem0 += alt(ADD_mem)
	S += (T0_0*ADD[0])-1<T2T2_mem0*ADD_mem[0]
	S += (T0_0*ADD[1])-1<T2T2_mem0*ADD_mem[1]
	S += (T0_0*ADD[2])-1<T2T2_mem0*ADD_mem[2]
	S += (T0_0*ADD[3])-1<T2T2_mem0*ADD_mem[3]
	S += T2T2_mem0<=T2T2

	T2T2_mem1 = S.Task('T2T2_mem1', length=1, delay_cost=1)
	T2T2_mem1 += alt(ADD_mem)
	S += (T0_1*ADD[0])-1<T2T2_mem1*ADD_mem[0]
	S += (T0_1*ADD[1])-1<T2T2_mem1*ADD_mem[1]
	S += (T0_1*ADD[2])-1<T2T2_mem1*ADD_mem[2]
	S += (T0_1*ADD[3])-1<T2T2_mem1*ADD_mem[3]
	S += T2T2_mem1<=T2T2

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	T3T0 += alt(ADD)

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	T3T0_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<T3T0_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<T3T0_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<T3T0_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<T3T0_mem0*ADD_mem[3]
	S += T3T0_mem0<=T3T0

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	T3T0_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<T3T0_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<T3T0_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<T3T0_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<T3T0_mem1*ADD_mem[3]
	S += T3T0_mem1<=T3T0

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	T3T1 += alt(ADD)

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	T3T1_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<T3T1_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<T3T1_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<T3T1_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<T3T1_mem0*ADD_mem[3]
	S += T3T1_mem0<=T3T1

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	T3T1_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<T3T1_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<T3T1_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<T3T1_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<T3T1_mem1*ADD_mem[3]
	S += T3T1_mem1<=T3T1

	T3T2_in = S.Task('T3T2_in', length=1, delay_cost=1)
	T3T2_in += alt(MUL_in)
	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	T3T2 += alt(MUL)
	S+=T3T2>=T3T2_in

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	T3T2_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<T3T2_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<T3T2_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<T3T2_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<T3T2_mem0*ADD_mem[3]
	S += T3T2_mem0<=T3T2

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	T3T2_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<T3T2_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<T3T2_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<T3T2_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<T3T2_mem1*ADD_mem[3]
	S += T3T2_mem1<=T3T2

	T4T2 = S.Task('T4T2', length=1, delay_cost=1)
	T4T2 += alt(ADD)

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	T4T2_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<T4T2_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<T4T2_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<T4T2_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<T4T2_mem0*ADD_mem[3]
	S += T4T2_mem0<=T4T2

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	T4T2_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<T4T2_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<T4T2_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<T4T2_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<T4T2_mem1*ADD_mem[3]
	S += T4T2_mem1<=T4T2

	NEW_TXT2 = S.Task('NEW_TXT2', length=1, delay_cost=1)
	NEW_TXT2 += alt(ADD)

	NEW_TXT2_mem0 = S.Task('NEW_TXT2_mem0', length=1, delay_cost=1)
	NEW_TXT2_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<NEW_TXT2_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<NEW_TXT2_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<NEW_TXT2_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<NEW_TXT2_mem0*ADD_mem[3]
	S += NEW_TXT2_mem0<=NEW_TXT2

	NEW_TXT2_mem1 = S.Task('NEW_TXT2_mem1', length=1, delay_cost=1)
	NEW_TXT2_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<NEW_TXT2_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<NEW_TXT2_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<NEW_TXT2_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<NEW_TXT2_mem1*ADD_mem[3]
	S += NEW_TXT2_mem1<=NEW_TXT2

	T7_T2 = S.Task('T7_T2', length=1, delay_cost=1)
	T7_T2 += alt(ADD)

	T7_T2_mem0 = S.Task('T7_T2_mem0', length=1, delay_cost=1)
	T7_T2_mem0 += alt(ADD_mem)
	S += (T0_0*ADD[0])-1<T7_T2_mem0*ADD_mem[0]
	S += (T0_0*ADD[1])-1<T7_T2_mem0*ADD_mem[1]
	S += (T0_0*ADD[2])-1<T7_T2_mem0*ADD_mem[2]
	S += (T0_0*ADD[3])-1<T7_T2_mem0*ADD_mem[3]
	S += T7_T2_mem0<=T7_T2

	T7_T2_mem1 = S.Task('T7_T2_mem1', length=1, delay_cost=1)
	T7_T2_mem1 += alt(ADD_mem)
	S += (T0_1*ADD[0])-1<T7_T2_mem1*ADD_mem[0]
	S += (T0_1*ADD[1])-1<T7_T2_mem1*ADD_mem[1]
	S += (T0_1*ADD[2])-1<T7_T2_mem1*ADD_mem[2]
	S += (T0_1*ADD[3])-1<T7_T2_mem1*ADD_mem[3]
	S += T7_T2_mem1<=T7_T2

	C00T1_in = S.Task('C00T1_in', length=1, delay_cost=1)
	C00T1_in += alt(MUL_in)
	C00T1 = S.Task('C00T1', length=7, delay_cost=1)
	C00T1 += alt(MUL)
	S+=C00T1>=C00T1_in

	C00T1_mem0 = S.Task('C00T1_mem0', length=1, delay_cost=1)
	C00T1_mem0 += INPUT_mem_r
	S += C00T1_mem0<=C00T1

	C00T1_mem1 = S.Task('C00T1_mem1', length=1, delay_cost=1)
	C00T1_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<C00T1_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<C00T1_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<C00T1_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<C00T1_mem1*ADD_mem[3]
	S += C00T1_mem1<=C00T1

	C00T3 = S.Task('C00T3', length=1, delay_cost=1)
	C00T3 += alt(ADD)

	C00T3_mem0 = S.Task('C00T3_mem0', length=1, delay_cost=1)
	C00T3_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<C00T3_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<C00T3_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<C00T3_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<C00T3_mem0*ADD_mem[3]
	S += C00T3_mem0<=C00T3

	C00T3_mem1 = S.Task('C00T3_mem1', length=1, delay_cost=1)
	C00T3_mem1 += alt(ADD_mem)
	S += (T1_1*ADD[0])-1<C00T3_mem1*ADD_mem[0]
	S += (T1_1*ADD[1])-1<C00T3_mem1*ADD_mem[1]
	S += (T1_1*ADD[2])-1<C00T3_mem1*ADD_mem[2]
	S += (T1_1*ADD[3])-1<C00T3_mem1*ADD_mem[3]
	S += C00T3_mem1<=C00T3

	T0_1T1_in = S.Task('T0_1T1_in', length=1, delay_cost=1)
	T0_1T1_in += alt(MUL_in)
	T0_1T1 = S.Task('T0_1T1', length=7, delay_cost=1)
	T0_1T1 += alt(MUL)
	S+=T0_1T1>=T0_1T1_in

	T0_1T1_mem0 = S.Task('T0_1T1_mem0', length=1, delay_cost=1)
	T0_1T1_mem0 += INPUT_mem_r
	S += T0_1T1_mem0<=T0_1T1

	T0_1T1_mem1 = S.Task('T0_1T1_mem1', length=1, delay_cost=1)
	T0_1T1_mem1 += alt(ADD_mem)
	S += (T0_1*ADD[0])-1<T0_1T1_mem1*ADD_mem[0]
	S += (T0_1*ADD[1])-1<T0_1T1_mem1*ADD_mem[1]
	S += (T0_1*ADD[2])-1<T0_1T1_mem1*ADD_mem[2]
	S += (T0_1*ADD[3])-1<T0_1T1_mem1*ADD_mem[3]
	S += T0_1T1_mem1<=T0_1T1

	T0_1T3 = S.Task('T0_1T3', length=1, delay_cost=1)
	T0_1T3 += alt(ADD)

	T0_1T3_mem0 = S.Task('T0_1T3_mem0', length=1, delay_cost=1)
	T0_1T3_mem0 += alt(ADD_mem)
	S += (T0_0*ADD[0])-1<T0_1T3_mem0*ADD_mem[0]
	S += (T0_0*ADD[1])-1<T0_1T3_mem0*ADD_mem[1]
	S += (T0_0*ADD[2])-1<T0_1T3_mem0*ADD_mem[2]
	S += (T0_0*ADD[3])-1<T0_1T3_mem0*ADD_mem[3]
	S += T0_1T3_mem0<=T0_1T3

	T0_1T3_mem1 = S.Task('T0_1T3_mem1', length=1, delay_cost=1)
	T0_1T3_mem1 += alt(ADD_mem)
	S += (T0_1*ADD[0])-1<T0_1T3_mem1*ADD_mem[0]
	S += (T0_1*ADD[1])-1<T0_1T3_mem1*ADD_mem[1]
	S += (T0_1*ADD[2])-1<T0_1T3_mem1*ADD_mem[2]
	S += (T0_1*ADD[3])-1<T0_1T3_mem1*ADD_mem[3]
	S += T0_1T3_mem1<=T0_1T3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01, time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "padd_mul1_add4/padd_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_padd_mul1_add4_0(0, 0)