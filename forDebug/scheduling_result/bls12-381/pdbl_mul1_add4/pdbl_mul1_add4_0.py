from pyschedule import Scenario, solvers, plotters, alt

def solve_pdbl_mul1_add4_0(ConstStep, ExpStep):
	horizon = 90
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

	T1_T2 = S.Task('T1_T2', length=1, delay_cost=1)
	T1_T2 += alt(ADD)

	T1_T2_mem0 = S.Task('T1_T2_mem0', length=1, delay_cost=1)
	T1_T2_mem0 += INPUT_mem_r
	S += T1_T2_mem0<=T1_T2

	T1_T2_mem1 = S.Task('T1_T2_mem1', length=1, delay_cost=1)
	T1_T2_mem1 += INPUT_mem_r
	S += T1_T2_mem1<=T1_T2

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

	T3T0 = S.Task('T3T0', length=1, delay_cost=1)
	T3T0 += alt(ADD)

	T3T0_mem0 = S.Task('T3T0_mem0', length=1, delay_cost=1)
	T3T0_mem0 += INPUT_mem_r
	S += T3T0_mem0<=T3T0

	T3T0_mem1 = S.Task('T3T0_mem1', length=1, delay_cost=1)
	T3T0_mem1 += INPUT_mem_r
	S += T3T0_mem1<=T3T0

	T3T1 = S.Task('T3T1', length=1, delay_cost=1)
	T3T1 += alt(ADD)

	T3T1_mem0 = S.Task('T3T1_mem0', length=1, delay_cost=1)
	T3T1_mem0 += INPUT_mem_r
	S += T3T1_mem0<=T3T1

	T3T1_mem1 = S.Task('T3T1_mem1', length=1, delay_cost=1)
	T3T1_mem1 += INPUT_mem_r
	S += T3T1_mem1<=T3T1

	T3T2_in = S.Task('T3T2_in', length=1, delay_cost=1)
	T3T2_in += alt(MUL_in)
	T3T2 = S.Task('T3T2', length=7, delay_cost=1)
	T3T2 += alt(MUL)
	S+=T3T2>=T3T2_in

	T3T2_mem0 = S.Task('T3T2_mem0', length=1, delay_cost=1)
	T3T2_mem0 += INPUT_mem_r
	S += T3T2_mem0<=T3T2

	T3T2_mem1 = S.Task('T3T2_mem1', length=1, delay_cost=1)
	T3T2_mem1 += INPUT_mem_r
	S += T3T2_mem1<=T3T2

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

	T00_in = S.Task('T00_in', length=1, delay_cost=1)
	T00_in += alt(MUL_in)
	T00 = S.Task('T00', length=7, delay_cost=1)
	T00 += alt(MUL)
	S+=T00>=T00_in

	T00_mem0 = S.Task('T00_mem0', length=1, delay_cost=1)
	T00_mem0 += alt(ADD_mem)
	S += (T0T0*ADD[0])-1<T00_mem0*ADD_mem[0]
	S += (T0T0*ADD[1])-1<T00_mem0*ADD_mem[1]
	S += (T0T0*ADD[2])-1<T00_mem0*ADD_mem[2]
	S += (T0T0*ADD[3])-1<T00_mem0*ADD_mem[3]
	S += T00_mem0<=T00

	T00_mem1 = S.Task('T00_mem1', length=1, delay_cost=1)
	T00_mem1 += alt(ADD_mem)
	S += (T0T1*ADD[0])-1<T00_mem1*ADD_mem[0]
	S += (T0T1*ADD[1])-1<T00_mem1*ADD_mem[1]
	S += (T0T1*ADD[2])-1<T00_mem1*ADD_mem[2]
	S += (T0T1*ADD[3])-1<T00_mem1*ADD_mem[3]
	S += T00_mem1<=T00

	T01 = S.Task('T01', length=1, delay_cost=1)
	T01 += alt(ADD)

	T01_mem0 = S.Task('T01_mem0', length=1, delay_cost=1)
	T01_mem0 += alt(MUL_mem)
	S += (T0T2*MUL[0])-1<T01_mem0*MUL_mem[0]
	S += T01_mem0<=T01

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	T10_in += alt(MUL_in)
	T10 = S.Task('T10', length=7, delay_cost=1)
	T10 += alt(MUL)
	S+=T10>=T10_in

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += alt(ADD_mem)
	S += (T1T0*ADD[0])-1<T10_mem0*ADD_mem[0]
	S += (T1T0*ADD[1])-1<T10_mem0*ADD_mem[1]
	S += (T1T0*ADD[2])-1<T10_mem0*ADD_mem[2]
	S += (T1T0*ADD[3])-1<T10_mem0*ADD_mem[3]
	S += T10_mem0<=T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += alt(ADD_mem)
	S += (T1T1*ADD[0])-1<T10_mem1*ADD_mem[0]
	S += (T1T1*ADD[1])-1<T10_mem1*ADD_mem[1]
	S += (T1T1*ADD[2])-1<T10_mem1*ADD_mem[2]
	S += (T1T1*ADD[3])-1<T10_mem1*ADD_mem[3]
	S += T10_mem1<=T10

	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(ADD)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += alt(MUL_mem)
	S += (T1T2*MUL[0])-1<T11_mem0*MUL_mem[0]
	S += T11_mem0<=T11

	T2T4_in = S.Task('T2T4_in', length=1, delay_cost=1)
	T2T4_in += alt(MUL_in)
	T2T4 = S.Task('T2T4', length=7, delay_cost=1)
	T2T4 += alt(MUL)
	S+=T2T4>=T2T4_in

	T2T4_mem0 = S.Task('T2T4_mem0', length=1, delay_cost=1)
	T2T4_mem0 += alt(ADD_mem)
	S += (T2T2*ADD[0])-1<T2T4_mem0*ADD_mem[0]
	S += (T2T2*ADD[1])-1<T2T4_mem0*ADD_mem[1]
	S += (T2T2*ADD[2])-1<T2T4_mem0*ADD_mem[2]
	S += (T2T2*ADD[3])-1<T2T4_mem0*ADD_mem[3]
	S += T2T4_mem0<=T2T4

	T2T4_mem1 = S.Task('T2T4_mem1', length=1, delay_cost=1)
	T2T4_mem1 += alt(ADD_mem)
	S += (T2T3*ADD[0])-1<T2T4_mem1*ADD_mem[0]
	S += (T2T3*ADD[1])-1<T2T4_mem1*ADD_mem[1]
	S += (T2T3*ADD[2])-1<T2T4_mem1*ADD_mem[2]
	S += (T2T3*ADD[3])-1<T2T4_mem1*ADD_mem[3]
	S += T2T4_mem1<=T2T4

	T2T5 = S.Task('T2T5', length=1, delay_cost=1)
	T2T5 += alt(ADD)

	T2T5_mem0 = S.Task('T2T5_mem0', length=1, delay_cost=1)
	T2T5_mem0 += alt(MUL_mem)
	S += (T2T0*MUL[0])-1<T2T5_mem0*MUL_mem[0]
	S += T2T5_mem0<=T2T5

	T2T5_mem1 = S.Task('T2T5_mem1', length=1, delay_cost=1)
	T2T5_mem1 += alt(MUL_mem)
	S += (T2T1*MUL[0])-1<T2T5_mem1*MUL_mem[0]
	S += T2T5_mem1<=T2T5

	T20 = S.Task('T20', length=1, delay_cost=1)
	T20 += alt(ADD)

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += alt(MUL_mem)
	S += (T2T0*MUL[0])-1<T20_mem0*MUL_mem[0]
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += alt(MUL_mem)
	S += (T2T1*MUL[0])-1<T20_mem1*MUL_mem[0]
	S += T20_mem1<=T20

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	T30_in += alt(MUL_in)
	T30 = S.Task('T30', length=7, delay_cost=1)
	T30 += alt(MUL)
	S+=T30>=T30_in

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += alt(ADD_mem)
	S += (T3T0*ADD[0])-1<T30_mem0*ADD_mem[0]
	S += (T3T0*ADD[1])-1<T30_mem0*ADD_mem[1]
	S += (T3T0*ADD[2])-1<T30_mem0*ADD_mem[2]
	S += (T3T0*ADD[3])-1<T30_mem0*ADD_mem[3]
	S += T30_mem0<=T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += alt(ADD_mem)
	S += (T3T1*ADD[0])-1<T30_mem1*ADD_mem[0]
	S += (T3T1*ADD[1])-1<T30_mem1*ADD_mem[1]
	S += (T3T1*ADD[2])-1<T30_mem1*ADD_mem[2]
	S += (T3T1*ADD[3])-1<T30_mem1*ADD_mem[3]
	S += T30_mem1<=T30

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(ADD)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += alt(MUL_mem)
	S += (T3T2*MUL[0])-1<T31_mem0*MUL_mem[0]
	S += T31_mem0<=T31

	T4T4_in = S.Task('T4T4_in', length=1, delay_cost=1)
	T4T4_in += alt(MUL_in)
	T4T4 = S.Task('T4T4', length=7, delay_cost=1)
	T4T4 += alt(MUL)
	S+=T4T4>=T4T4_in

	T4T4_mem0 = S.Task('T4T4_mem0', length=1, delay_cost=1)
	T4T4_mem0 += alt(ADD_mem)
	S += (T4T2*ADD[0])-1<T4T4_mem0*ADD_mem[0]
	S += (T4T2*ADD[1])-1<T4T4_mem0*ADD_mem[1]
	S += (T4T2*ADD[2])-1<T4T4_mem0*ADD_mem[2]
	S += (T4T2*ADD[3])-1<T4T4_mem0*ADD_mem[3]
	S += T4T4_mem0<=T4T4

	T4T4_mem1 = S.Task('T4T4_mem1', length=1, delay_cost=1)
	T4T4_mem1 += alt(ADD_mem)
	S += (T4T3*ADD[0])-1<T4T4_mem1*ADD_mem[0]
	S += (T4T3*ADD[1])-1<T4T4_mem1*ADD_mem[1]
	S += (T4T3*ADD[2])-1<T4T4_mem1*ADD_mem[2]
	S += (T4T3*ADD[3])-1<T4T4_mem1*ADD_mem[3]
	S += T4T4_mem1<=T4T4

	T4T5 = S.Task('T4T5', length=1, delay_cost=1)
	T4T5 += alt(ADD)

	T4T5_mem0 = S.Task('T4T5_mem0', length=1, delay_cost=1)
	T4T5_mem0 += alt(MUL_mem)
	S += (T4T0*MUL[0])-1<T4T5_mem0*MUL_mem[0]
	S += T4T5_mem0<=T4T5

	T4T5_mem1 = S.Task('T4T5_mem1', length=1, delay_cost=1)
	T4T5_mem1 += alt(MUL_mem)
	S += (T4T1*MUL[0])-1<T4T5_mem1*MUL_mem[0]
	S += T4T5_mem1<=T4T5

	T40 = S.Task('T40', length=1, delay_cost=1)
	T40 += alt(ADD)

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += alt(MUL_mem)
	S += (T4T0*MUL[0])-1<T40_mem0*MUL_mem[0]
	S += T40_mem0<=T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += alt(MUL_mem)
	S += (T4T1*MUL[0])-1<T40_mem1*MUL_mem[0]
	S += T40_mem1<=T40

	T1_T0_in = S.Task('T1_T0_in', length=1, delay_cost=1)
	T1_T0_in += alt(MUL_in)
	T1_T0 = S.Task('T1_T0', length=7, delay_cost=1)
	T1_T0 += alt(MUL)
	S+=T1_T0>=T1_T0_in

	T1_T0_mem0 = S.Task('T1_T0_mem0', length=1, delay_cost=1)
	T1_T0_mem0 += INPUT_mem_r
	S += T1_T0_mem0<=T1_T0

	T1_T0_mem1 = S.Task('T1_T0_mem1', length=1, delay_cost=1)
	T1_T0_mem1 += alt(MUL_mem)
	S += (T10*MUL[0])-1<T1_T0_mem1*MUL_mem[0]
	S += T1_T0_mem1<=T1_T0

	T1_T1_in = S.Task('T1_T1_in', length=1, delay_cost=1)
	T1_T1_in += alt(MUL_in)
	T1_T1 = S.Task('T1_T1', length=7, delay_cost=1)
	T1_T1 += alt(MUL)
	S+=T1_T1>=T1_T1_in

	T1_T1_mem0 = S.Task('T1_T1_mem0', length=1, delay_cost=1)
	T1_T1_mem0 += INPUT_mem_r
	S += T1_T1_mem0<=T1_T1

	T1_T1_mem1 = S.Task('T1_T1_mem1', length=1, delay_cost=1)
	T1_T1_mem1 += alt(ADD_mem)
	S += (T11*ADD[0])-1<T1_T1_mem1*ADD_mem[0]
	S += (T11*ADD[1])-1<T1_T1_mem1*ADD_mem[1]
	S += (T11*ADD[2])-1<T1_T1_mem1*ADD_mem[2]
	S += (T11*ADD[3])-1<T1_T1_mem1*ADD_mem[3]
	S += T1_T1_mem1<=T1_T1

	T1_T3 = S.Task('T1_T3', length=1, delay_cost=1)
	T1_T3 += alt(ADD)

	T1_T3_mem0 = S.Task('T1_T3_mem0', length=1, delay_cost=1)
	T1_T3_mem0 += alt(MUL_mem)
	S += (T10*MUL[0])-1<T1_T3_mem0*MUL_mem[0]
	S += T1_T3_mem0<=T1_T3

	T1_T3_mem1 = S.Task('T1_T3_mem1', length=1, delay_cost=1)
	T1_T3_mem1 += alt(ADD_mem)
	S += (T11*ADD[0])-1<T1_T3_mem1*ADD_mem[0]
	S += (T11*ADD[1])-1<T1_T3_mem1*ADD_mem[1]
	S += (T11*ADD[2])-1<T1_T3_mem1*ADD_mem[2]
	S += (T11*ADD[3])-1<T1_T3_mem1*ADD_mem[3]
	S += T1_T3_mem1<=T1_T3

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(ADD)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += alt(MUL_mem)
	S += (T2T4*MUL[0])-1<T21_mem0*MUL_mem[0]
	S += T21_mem0<=T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += alt(ADD_mem)
	S += (T2T5*ADD[0])-1<T21_mem1*ADD_mem[0]
	S += (T2T5*ADD[1])-1<T21_mem1*ADD_mem[1]
	S += (T2T5*ADD[2])-1<T21_mem1*ADD_mem[2]
	S += (T2T5*ADD[3])-1<T21_mem1*ADD_mem[3]
	S += T21_mem1<=T21

	T2_0 = S.Task('T2_0', length=1, delay_cost=1)
	T2_0 += alt(ADD)

	T2_0_mem0 = S.Task('T2_0_mem0', length=1, delay_cost=1)
	T2_0_mem0 += alt(ADD_mem)
	S += (T20*ADD[0])-1<T2_0_mem0*ADD_mem[0]
	S += (T20*ADD[1])-1<T2_0_mem0*ADD_mem[1]
	S += (T20*ADD[2])-1<T2_0_mem0*ADD_mem[2]
	S += (T20*ADD[3])-1<T2_0_mem0*ADD_mem[3]
	S += T2_0_mem0<=T2_0

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += alt(MUL_mem)
	S += (T30*MUL[0])-1<T60_mem0*MUL_mem[0]
	S += T60_mem0<=T60

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(ADD)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T61_mem0*ADD_mem[0]
	S += (T31*ADD[1])-1<T61_mem0*ADD_mem[1]
	S += (T31*ADD[2])-1<T61_mem0*ADD_mem[2]
	S += (T31*ADD[3])-1<T61_mem0*ADD_mem[3]
	S += T61_mem0<=T61

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += alt(MUL_mem)
	S += (T4T4*MUL[0])-1<T41_mem0*MUL_mem[0]
	S += T41_mem0<=T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += alt(ADD_mem)
	S += (T4T5*ADD[0])-1<T41_mem1*ADD_mem[0]
	S += (T4T5*ADD[1])-1<T41_mem1*ADD_mem[1]
	S += (T4T5*ADD[2])-1<T41_mem1*ADD_mem[2]
	S += (T4T5*ADD[3])-1<T41_mem1*ADD_mem[3]
	S += T41_mem1<=T41

	T4_0 = S.Task('T4_0', length=1, delay_cost=1)
	T4_0 += alt(ADD)

	T4_0_mem0 = S.Task('T4_0_mem0', length=1, delay_cost=1)
	T4_0_mem0 += alt(ADD_mem)
	S += (T40*ADD[0])-1<T4_0_mem0*ADD_mem[0]
	S += (T40*ADD[1])-1<T4_0_mem0*ADD_mem[1]
	S += (T40*ADD[2])-1<T4_0_mem0*ADD_mem[2]
	S += (T40*ADD[3])-1<T4_0_mem0*ADD_mem[3]
	S += T4_0_mem0<=T4_0

	NEW_TZT2 = S.Task('NEW_TZT2', length=1, delay_cost=1)
	NEW_TZT2 += alt(ADD)

	NEW_TZT2_mem0 = S.Task('NEW_TZT2_mem0', length=1, delay_cost=1)
	NEW_TZT2_mem0 += alt(MUL_mem)
	S += (T00*MUL[0])-1<NEW_TZT2_mem0*MUL_mem[0]
	S += NEW_TZT2_mem0<=NEW_TZT2

	NEW_TZT2_mem1 = S.Task('NEW_TZT2_mem1', length=1, delay_cost=1)
	NEW_TZT2_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<NEW_TZT2_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<NEW_TZT2_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<NEW_TZT2_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<NEW_TZT2_mem1*ADD_mem[3]
	S += NEW_TZT2_mem1<=NEW_TZT2

	T0_T0 = S.Task('T0_T0', length=1, delay_cost=1)
	T0_T0 += alt(ADD)

	T0_T0_mem0 = S.Task('T0_T0_mem0', length=1, delay_cost=1)
	T0_T0_mem0 += alt(MUL_mem)
	S += (T00*MUL[0])-1<T0_T0_mem0*MUL_mem[0]
	S += T0_T0_mem0<=T0_T0

	T0_T0_mem1 = S.Task('T0_T0_mem1', length=1, delay_cost=1)
	T0_T0_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<T0_T0_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<T0_T0_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<T0_T0_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<T0_T0_mem1*ADD_mem[3]
	S += T0_T0_mem1<=T0_T0

	T0_T1 = S.Task('T0_T1', length=1, delay_cost=1)
	T0_T1 += alt(ADD)

	T0_T1_mem0 = S.Task('T0_T1_mem0', length=1, delay_cost=1)
	T0_T1_mem0 += alt(MUL_mem)
	S += (T00*MUL[0])-1<T0_T1_mem0*MUL_mem[0]
	S += T0_T1_mem0<=T0_T1

	T0_T1_mem1 = S.Task('T0_T1_mem1', length=1, delay_cost=1)
	T0_T1_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<T0_T1_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<T0_T1_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<T0_T1_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<T0_T1_mem1*ADD_mem[3]
	S += T0_T1_mem1<=T0_T1

	T0_T2_in = S.Task('T0_T2_in', length=1, delay_cost=1)
	T0_T2_in += alt(MUL_in)
	T0_T2 = S.Task('T0_T2', length=7, delay_cost=1)
	T0_T2 += alt(MUL)
	S+=T0_T2>=T0_T2_in

	T0_T2_mem0 = S.Task('T0_T2_mem0', length=1, delay_cost=1)
	T0_T2_mem0 += alt(MUL_mem)
	S += (T00*MUL[0])-1<T0_T2_mem0*MUL_mem[0]
	S += T0_T2_mem0<=T0_T2

	T0_T2_mem1 = S.Task('T0_T2_mem1', length=1, delay_cost=1)
	T0_T2_mem1 += alt(ADD_mem)
	S += (T01*ADD[0])-1<T0_T2_mem1*ADD_mem[0]
	S += (T01*ADD[1])-1<T0_T2_mem1*ADD_mem[1]
	S += (T01*ADD[2])-1<T0_T2_mem1*ADD_mem[2]
	S += (T01*ADD[3])-1<T0_T2_mem1*ADD_mem[3]
	S += T0_T2_mem1<=T0_T2

	T1_T4_in = S.Task('T1_T4_in', length=1, delay_cost=1)
	T1_T4_in += alt(MUL_in)
	T1_T4 = S.Task('T1_T4', length=7, delay_cost=1)
	T1_T4 += alt(MUL)
	S+=T1_T4>=T1_T4_in

	T1_T4_mem0 = S.Task('T1_T4_mem0', length=1, delay_cost=1)
	T1_T4_mem0 += alt(ADD_mem)
	S += (T1_T2*ADD[0])-1<T1_T4_mem0*ADD_mem[0]
	S += (T1_T2*ADD[1])-1<T1_T4_mem0*ADD_mem[1]
	S += (T1_T2*ADD[2])-1<T1_T4_mem0*ADD_mem[2]
	S += (T1_T2*ADD[3])-1<T1_T4_mem0*ADD_mem[3]
	S += T1_T4_mem0<=T1_T4

	T1_T4_mem1 = S.Task('T1_T4_mem1', length=1, delay_cost=1)
	T1_T4_mem1 += alt(ADD_mem)
	S += (T1_T3*ADD[0])-1<T1_T4_mem1*ADD_mem[0]
	S += (T1_T3*ADD[1])-1<T1_T4_mem1*ADD_mem[1]
	S += (T1_T3*ADD[2])-1<T1_T4_mem1*ADD_mem[2]
	S += (T1_T3*ADD[3])-1<T1_T4_mem1*ADD_mem[3]
	S += T1_T4_mem1<=T1_T4

	T1_T5 = S.Task('T1_T5', length=1, delay_cost=1)
	T1_T5 += alt(ADD)

	T1_T5_mem0 = S.Task('T1_T5_mem0', length=1, delay_cost=1)
	T1_T5_mem0 += alt(MUL_mem)
	S += (T1_T0*MUL[0])-1<T1_T5_mem0*MUL_mem[0]
	S += T1_T5_mem0<=T1_T5

	T1_T5_mem1 = S.Task('T1_T5_mem1', length=1, delay_cost=1)
	T1_T5_mem1 += alt(MUL_mem)
	S += (T1_T1*MUL[0])-1<T1_T5_mem1*MUL_mem[0]
	S += T1_T5_mem1<=T1_T5

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	T1_0 += alt(ADD)

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	T1_0_mem0 += alt(MUL_mem)
	S += (T1_T0*MUL[0])-1<T1_0_mem0*MUL_mem[0]
	S += T1_0_mem0<=T1_0

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	T1_0_mem1 += alt(MUL_mem)
	S += (T1_T1*MUL[0])-1<T1_0_mem1*MUL_mem[0]
	S += T1_0_mem1<=T1_0

	T2_1 = S.Task('T2_1', length=1, delay_cost=1)
	T2_1 += alt(ADD)

	T2_1_mem0 = S.Task('T2_1_mem0', length=1, delay_cost=1)
	T2_1_mem0 += alt(ADD_mem)
	S += (T21*ADD[0])-1<T2_1_mem0*ADD_mem[0]
	S += (T21*ADD[1])-1<T2_1_mem0*ADD_mem[1]
	S += (T21*ADD[2])-1<T2_1_mem0*ADD_mem[2]
	S += (T21*ADD[3])-1<T2_1_mem0*ADD_mem[3]
	S += T2_1_mem0<=T2_1

	T3_0 = S.Task('T3_0', length=1, delay_cost=1)
	T3_0 += alt(ADD)

	T3_0_mem0 = S.Task('T3_0_mem0', length=1, delay_cost=1)
	T3_0_mem0 += alt(ADD_mem)
	S += (T60*ADD[0])-1<T3_0_mem0*ADD_mem[0]
	S += (T60*ADD[1])-1<T3_0_mem0*ADD_mem[1]
	S += (T60*ADD[2])-1<T3_0_mem0*ADD_mem[2]
	S += (T60*ADD[3])-1<T3_0_mem0*ADD_mem[3]
	S += T3_0_mem0<=T3_0

	T3_0_mem1 = S.Task('T3_0_mem1', length=1, delay_cost=1)
	T3_0_mem1 += alt(MUL_mem)
	S += (T30*MUL[0])-1<T3_0_mem1*MUL_mem[0]
	S += T3_0_mem1<=T3_0

	T3_1 = S.Task('T3_1', length=1, delay_cost=1)
	T3_1 += alt(ADD)

	T3_1_mem0 = S.Task('T3_1_mem0', length=1, delay_cost=1)
	T3_1_mem0 += alt(ADD_mem)
	S += (T61*ADD[0])-1<T3_1_mem0*ADD_mem[0]
	S += (T61*ADD[1])-1<T3_1_mem0*ADD_mem[1]
	S += (T61*ADD[2])-1<T3_1_mem0*ADD_mem[2]
	S += (T61*ADD[3])-1<T3_1_mem0*ADD_mem[3]
	S += T3_1_mem0<=T3_1

	T3_1_mem1 = S.Task('T3_1_mem1', length=1, delay_cost=1)
	T3_1_mem1 += alt(ADD_mem)
	S += (T31*ADD[0])-1<T3_1_mem1*ADD_mem[0]
	S += (T31*ADD[1])-1<T3_1_mem1*ADD_mem[1]
	S += (T31*ADD[2])-1<T3_1_mem1*ADD_mem[2]
	S += (T31*ADD[3])-1<T3_1_mem1*ADD_mem[3]
	S += T3_1_mem1<=T3_1

	T4_1 = S.Task('T4_1', length=1, delay_cost=1)
	T4_1 += alt(ADD)

	T4_1_mem0 = S.Task('T4_1_mem0', length=1, delay_cost=1)
	T4_1_mem0 += alt(ADD_mem)
	S += (T41*ADD[0])-1<T4_1_mem0*ADD_mem[0]
	S += (T41*ADD[1])-1<T4_1_mem0*ADD_mem[1]
	S += (T41*ADD[2])-1<T4_1_mem0*ADD_mem[2]
	S += (T41*ADD[3])-1<T4_1_mem0*ADD_mem[3]
	S += T4_1_mem0<=T4_1

	NEW_TZT0_in = S.Task('NEW_TZT0_in', length=1, delay_cost=1)
	NEW_TZT0_in += alt(MUL_in)
	NEW_TZT0 = S.Task('NEW_TZT0', length=7, delay_cost=1)
	NEW_TZT0 += alt(MUL)
	S+=NEW_TZT0>=NEW_TZT0_in

	NEW_TZT0_mem0 = S.Task('NEW_TZT0_mem0', length=1, delay_cost=1)
	NEW_TZT0_mem0 += alt(MUL_mem)
	S += (T00*MUL[0])-1<NEW_TZT0_mem0*MUL_mem[0]
	S += NEW_TZT0_mem0<=NEW_TZT0

	NEW_TZT0_mem1 = S.Task('NEW_TZT0_mem1', length=1, delay_cost=1)
	NEW_TZT0_mem1 += alt(ADD_mem)
	S += (T4_0*ADD[0])-1<NEW_TZT0_mem1*ADD_mem[0]
	S += (T4_0*ADD[1])-1<NEW_TZT0_mem1*ADD_mem[1]
	S += (T4_0*ADD[2])-1<NEW_TZT0_mem1*ADD_mem[2]
	S += (T4_0*ADD[3])-1<NEW_TZT0_mem1*ADD_mem[3]
	S += NEW_TZT0_mem1<=NEW_TZT0

	T0_0_in = S.Task('T0_0_in', length=1, delay_cost=1)
	T0_0_in += alt(MUL_in)
	T0_0 = S.Task('T0_0', length=7, delay_cost=1)
	T0_0 += alt(MUL)
	S+=T0_0>=T0_0_in

	T0_0_mem0 = S.Task('T0_0_mem0', length=1, delay_cost=1)
	T0_0_mem0 += alt(ADD_mem)
	S += (T0_T0*ADD[0])-1<T0_0_mem0*ADD_mem[0]
	S += (T0_T0*ADD[1])-1<T0_0_mem0*ADD_mem[1]
	S += (T0_T0*ADD[2])-1<T0_0_mem0*ADD_mem[2]
	S += (T0_T0*ADD[3])-1<T0_0_mem0*ADD_mem[3]
	S += T0_0_mem0<=T0_0

	T0_0_mem1 = S.Task('T0_0_mem1', length=1, delay_cost=1)
	T0_0_mem1 += alt(ADD_mem)
	S += (T0_T1*ADD[0])-1<T0_0_mem1*ADD_mem[0]
	S += (T0_T1*ADD[1])-1<T0_0_mem1*ADD_mem[1]
	S += (T0_T1*ADD[2])-1<T0_0_mem1*ADD_mem[2]
	S += (T0_T1*ADD[3])-1<T0_0_mem1*ADD_mem[3]
	S += T0_0_mem1<=T0_0

	T0_1 = S.Task('T0_1', length=1, delay_cost=1)
	T0_1 += alt(ADD)

	T0_1_mem0 = S.Task('T0_1_mem0', length=1, delay_cost=1)
	T0_1_mem0 += alt(MUL_mem)
	S += (T0_T2*MUL[0])-1<T0_1_mem0*MUL_mem[0]
	S += T0_1_mem0<=T0_1

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	T1_1 += alt(ADD)

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	T1_1_mem0 += alt(MUL_mem)
	S += (T1_T4*MUL[0])-1<T1_1_mem0*MUL_mem[0]
	S += T1_1_mem0<=T1_1

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	T1_1_mem1 += alt(ADD_mem)
	S += (T1_T5*ADD[0])-1<T1_1_mem1*ADD_mem[0]
	S += (T1_T5*ADD[1])-1<T1_1_mem1*ADD_mem[1]
	S += (T1_T5*ADD[2])-1<T1_1_mem1*ADD_mem[2]
	S += (T1_T5*ADD[3])-1<T1_1_mem1*ADD_mem[3]
	S += T1_1_mem1<=T1_1

	B_0 = S.Task('B_0', length=1, delay_cost=1)
	B_0 += alt(ADD)

	B_0_mem0 = S.Task('B_0_mem0', length=1, delay_cost=1)
	B_0_mem0 += alt(ADD_mem)
	S += (T1_0*ADD[0])-1<B_0_mem0*ADD_mem[0]
	S += (T1_0*ADD[1])-1<B_0_mem0*ADD_mem[1]
	S += (T1_0*ADD[2])-1<B_0_mem0*ADD_mem[2]
	S += (T1_0*ADD[3])-1<B_0_mem0*ADD_mem[3]
	S += B_0_mem0<=B_0

	NEW_TZT1_in = S.Task('NEW_TZT1_in', length=1, delay_cost=1)
	NEW_TZT1_in += alt(MUL_in)
	NEW_TZT1 = S.Task('NEW_TZT1', length=7, delay_cost=1)
	NEW_TZT1 += alt(MUL)
	S+=NEW_TZT1>=NEW_TZT1_in

	NEW_TZT1_mem0 = S.Task('NEW_TZT1_mem0', length=1, delay_cost=1)
	NEW_TZT1_mem0 += alt(ADD_mem)
	S += (T01*ADD[0])-1<NEW_TZT1_mem0*ADD_mem[0]
	S += (T01*ADD[1])-1<NEW_TZT1_mem0*ADD_mem[1]
	S += (T01*ADD[2])-1<NEW_TZT1_mem0*ADD_mem[2]
	S += (T01*ADD[3])-1<NEW_TZT1_mem0*ADD_mem[3]
	S += NEW_TZT1_mem0<=NEW_TZT1

	NEW_TZT1_mem1 = S.Task('NEW_TZT1_mem1', length=1, delay_cost=1)
	NEW_TZT1_mem1 += alt(ADD_mem)
	S += (T4_1*ADD[0])-1<NEW_TZT1_mem1*ADD_mem[0]
	S += (T4_1*ADD[1])-1<NEW_TZT1_mem1*ADD_mem[1]
	S += (T4_1*ADD[2])-1<NEW_TZT1_mem1*ADD_mem[2]
	S += (T4_1*ADD[3])-1<NEW_TZT1_mem1*ADD_mem[3]
	S += NEW_TZT1_mem1<=NEW_TZT1

	NEW_TZT3 = S.Task('NEW_TZT3', length=1, delay_cost=1)
	NEW_TZT3 += alt(ADD)

	NEW_TZT3_mem0 = S.Task('NEW_TZT3_mem0', length=1, delay_cost=1)
	NEW_TZT3_mem0 += alt(ADD_mem)
	S += (T4_0*ADD[0])-1<NEW_TZT3_mem0*ADD_mem[0]
	S += (T4_0*ADD[1])-1<NEW_TZT3_mem0*ADD_mem[1]
	S += (T4_0*ADD[2])-1<NEW_TZT3_mem0*ADD_mem[2]
	S += (T4_0*ADD[3])-1<NEW_TZT3_mem0*ADD_mem[3]
	S += NEW_TZT3_mem0<=NEW_TZT3

	NEW_TZT3_mem1 = S.Task('NEW_TZT3_mem1', length=1, delay_cost=1)
	NEW_TZT3_mem1 += alt(ADD_mem)
	S += (T4_1*ADD[0])-1<NEW_TZT3_mem1*ADD_mem[0]
	S += (T4_1*ADD[1])-1<NEW_TZT3_mem1*ADD_mem[1]
	S += (T4_1*ADD[2])-1<NEW_TZT3_mem1*ADD_mem[2]
	S += (T4_1*ADD[3])-1<NEW_TZT3_mem1*ADD_mem[3]
	S += NEW_TZT3_mem1<=NEW_TZT3

	NEW_TX_T3 = S.Task('NEW_TX_T3', length=1, delay_cost=1)
	NEW_TX_T3 += alt(ADD)

	NEW_TX_T3_mem0 = S.Task('NEW_TX_T3_mem0', length=1, delay_cost=1)
	NEW_TX_T3_mem0 += alt(ADD_mem)
	S += (T2_0*ADD[0])-1<NEW_TX_T3_mem0*ADD_mem[0]
	S += (T2_0*ADD[1])-1<NEW_TX_T3_mem0*ADD_mem[1]
	S += (T2_0*ADD[2])-1<NEW_TX_T3_mem0*ADD_mem[2]
	S += (T2_0*ADD[3])-1<NEW_TX_T3_mem0*ADD_mem[3]
	S += NEW_TX_T3_mem0<=NEW_TX_T3

	NEW_TX_T3_mem1 = S.Task('NEW_TX_T3_mem1', length=1, delay_cost=1)
	NEW_TX_T3_mem1 += alt(ADD_mem)
	S += (T2_1*ADD[0])-1<NEW_TX_T3_mem1*ADD_mem[0]
	S += (T2_1*ADD[1])-1<NEW_TX_T3_mem1*ADD_mem[1]
	S += (T2_1*ADD[2])-1<NEW_TX_T3_mem1*ADD_mem[2]
	S += (T2_1*ADD[3])-1<NEW_TX_T3_mem1*ADD_mem[3]
	S += NEW_TX_T3_mem1<=NEW_TX_T3

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

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