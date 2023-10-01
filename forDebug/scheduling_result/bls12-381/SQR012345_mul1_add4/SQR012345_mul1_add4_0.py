from pyschedule import Scenario, solvers, plotters, alt

def solve_SQR012345_mul1_add4_0(ConstStep, ExpStep):
	horizon = 90
	S=Scenario("SQR012345_mul1_add4_0",horizon = horizon)

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

	T4T0 = S.Task('T4T0', length=1, delay_cost=1)
	T4T0 += alt(ADD)

	T4T0_mem0 = S.Task('T4T0_mem0', length=1, delay_cost=1)
	T4T0_mem0 += INPUT_mem_r
	S += T4T0_mem0<=T4T0

	T4T0_mem1 = S.Task('T4T0_mem1', length=1, delay_cost=1)
	T4T0_mem1 += INPUT_mem_r
	S += T4T0_mem1<=T4T0

	T4T1 = S.Task('T4T1', length=1, delay_cost=1)
	T4T1 += alt(ADD)

	T4T1_mem0 = S.Task('T4T1_mem0', length=1, delay_cost=1)
	T4T1_mem0 += INPUT_mem_r
	S += T4T1_mem0<=T4T1

	T4T1_mem1 = S.Task('T4T1_mem1', length=1, delay_cost=1)
	T4T1_mem1 += INPUT_mem_r
	S += T4T1_mem1<=T4T1

	T4T2_in = S.Task('T4T2_in', length=1, delay_cost=1)
	T4T2_in += alt(MUL_in)
	T4T2 = S.Task('T4T2', length=7, delay_cost=1)
	T4T2 += alt(MUL)
	S+=T4T2>=T4T2_in

	T4T2_mem0 = S.Task('T4T2_mem0', length=1, delay_cost=1)
	T4T2_mem0 += INPUT_mem_r
	S += T4T2_mem0<=T4T2

	T4T2_mem1 = S.Task('T4T2_mem1', length=1, delay_cost=1)
	T4T2_mem1 += INPUT_mem_r
	S += T4T2_mem1<=T4T2

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

	T6T0_in = S.Task('T6T0_in', length=1, delay_cost=1)
	T6T0_in += alt(MUL_in)
	T6T0 = S.Task('T6T0', length=7, delay_cost=1)
	T6T0 += alt(MUL)
	S+=T6T0>=T6T0_in

	T6T0_mem0 = S.Task('T6T0_mem0', length=1, delay_cost=1)
	T6T0_mem0 += INPUT_mem_r
	S += T6T0_mem0<=T6T0

	T6T0_mem1 = S.Task('T6T0_mem1', length=1, delay_cost=1)
	T6T0_mem1 += INPUT_mem_r
	S += T6T0_mem1<=T6T0

	T6T1_in = S.Task('T6T1_in', length=1, delay_cost=1)
	T6T1_in += alt(MUL_in)
	T6T1 = S.Task('T6T1', length=7, delay_cost=1)
	T6T1 += alt(MUL)
	S+=T6T1>=T6T1_in

	T6T1_mem0 = S.Task('T6T1_mem0', length=1, delay_cost=1)
	T6T1_mem0 += INPUT_mem_r
	S += T6T1_mem0<=T6T1

	T6T1_mem1 = S.Task('T6T1_mem1', length=1, delay_cost=1)
	T6T1_mem1 += INPUT_mem_r
	S += T6T1_mem1<=T6T1

	T6T2 = S.Task('T6T2', length=1, delay_cost=1)
	T6T2 += alt(ADD)

	T6T2_mem0 = S.Task('T6T2_mem0', length=1, delay_cost=1)
	T6T2_mem0 += INPUT_mem_r
	S += T6T2_mem0<=T6T2

	T6T2_mem1 = S.Task('T6T2_mem1', length=1, delay_cost=1)
	T6T2_mem1 += INPUT_mem_r
	S += T6T2_mem1<=T6T2

	T6T3 = S.Task('T6T3', length=1, delay_cost=1)
	T6T3 += alt(ADD)

	T6T3_mem0 = S.Task('T6T3_mem0', length=1, delay_cost=1)
	T6T3_mem0 += INPUT_mem_r
	S += T6T3_mem0<=T6T3

	T6T3_mem1 = S.Task('T6T3_mem1', length=1, delay_cost=1)
	T6T3_mem1 += INPUT_mem_r
	S += T6T3_mem1<=T6T3

	T7T0_in = S.Task('T7T0_in', length=1, delay_cost=1)
	T7T0_in += alt(MUL_in)
	T7T0 = S.Task('T7T0', length=7, delay_cost=1)
	T7T0 += alt(MUL)
	S+=T7T0>=T7T0_in

	T7T0_mem0 = S.Task('T7T0_mem0', length=1, delay_cost=1)
	T7T0_mem0 += INPUT_mem_r
	S += T7T0_mem0<=T7T0

	T7T0_mem1 = S.Task('T7T0_mem1', length=1, delay_cost=1)
	T7T0_mem1 += INPUT_mem_r
	S += T7T0_mem1<=T7T0

	T7T1_in = S.Task('T7T1_in', length=1, delay_cost=1)
	T7T1_in += alt(MUL_in)
	T7T1 = S.Task('T7T1', length=7, delay_cost=1)
	T7T1 += alt(MUL)
	S+=T7T1>=T7T1_in

	T7T1_mem0 = S.Task('T7T1_mem0', length=1, delay_cost=1)
	T7T1_mem0 += INPUT_mem_r
	S += T7T1_mem0<=T7T1

	T7T1_mem1 = S.Task('T7T1_mem1', length=1, delay_cost=1)
	T7T1_mem1 += INPUT_mem_r
	S += T7T1_mem1<=T7T1

	T7T2 = S.Task('T7T2', length=1, delay_cost=1)
	T7T2 += alt(ADD)

	T7T2_mem0 = S.Task('T7T2_mem0', length=1, delay_cost=1)
	T7T2_mem0 += INPUT_mem_r
	S += T7T2_mem0<=T7T2

	T7T2_mem1 = S.Task('T7T2_mem1', length=1, delay_cost=1)
	T7T2_mem1 += INPUT_mem_r
	S += T7T2_mem1<=T7T2

	T7T3 = S.Task('T7T3', length=1, delay_cost=1)
	T7T3 += alt(ADD)

	T7T3_mem0 = S.Task('T7T3_mem0', length=1, delay_cost=1)
	T7T3_mem0 += INPUT_mem_r
	S += T7T3_mem0<=T7T3

	T7T3_mem1 = S.Task('T7T3_mem1', length=1, delay_cost=1)
	T7T3_mem1 += INPUT_mem_r
	S += T7T3_mem1<=T7T3

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

	T20 = S.Task('T20', length=1, delay_cost=1)
	T20 += alt(ADD)

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += alt(ADD_mem)
	S += (T10*ADD[0])-1<T20_mem0*ADD_mem[0]
	S += (T10*ADD[1])-1<T20_mem0*ADD_mem[1]
	S += (T10*ADD[2])-1<T20_mem0*ADD_mem[2]
	S += (T10*ADD[3])-1<T20_mem0*ADD_mem[3]
	S += T20_mem0<=T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += INPUT_mem_r
	S += T20_mem1<=T20

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(ADD)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += alt(ADD_mem)
	S += (T11*ADD[0])-1<T21_mem0*ADD_mem[0]
	S += (T11*ADD[1])-1<T21_mem0*ADD_mem[1]
	S += (T11*ADD[2])-1<T21_mem0*ADD_mem[2]
	S += (T11*ADD[3])-1<T21_mem0*ADD_mem[3]
	S += T21_mem0<=T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += INPUT_mem_r
	S += T21_mem1<=T21

	T1_0 = S.Task('T1_0', length=1, delay_cost=1)
	T1_0 += alt(ADD)

	T1_0_mem0 = S.Task('T1_0_mem0', length=1, delay_cost=1)
	T1_0_mem0 += alt(ADD_mem)
	S += (T10*ADD[0])-1<T1_0_mem0*ADD_mem[0]
	S += (T10*ADD[1])-1<T1_0_mem0*ADD_mem[1]
	S += (T10*ADD[2])-1<T1_0_mem0*ADD_mem[2]
	S += (T10*ADD[3])-1<T1_0_mem0*ADD_mem[3]
	S += T1_0_mem0<=T1_0

	T1_0_mem1 = S.Task('T1_0_mem1', length=1, delay_cost=1)
	T1_0_mem1 += INPUT_mem_r
	S += T1_0_mem1<=T1_0

	T1_1 = S.Task('T1_1', length=1, delay_cost=1)
	T1_1 += alt(ADD)

	T1_1_mem0 = S.Task('T1_1_mem0', length=1, delay_cost=1)
	T1_1_mem0 += alt(ADD_mem)
	S += (T11*ADD[0])-1<T1_1_mem0*ADD_mem[0]
	S += (T11*ADD[1])-1<T1_1_mem0*ADD_mem[1]
	S += (T11*ADD[2])-1<T1_1_mem0*ADD_mem[2]
	S += (T11*ADD[3])-1<T1_1_mem0*ADD_mem[3]
	S += T1_1_mem0<=T1_1

	T1_1_mem1 = S.Task('T1_1_mem1', length=1, delay_cost=1)
	T1_1_mem1 += INPUT_mem_r
	S += T1_1_mem1<=T1_1

	T3T4_in = S.Task('T3T4_in', length=1, delay_cost=1)
	T3T4_in += alt(MUL_in)
	T3T4 = S.Task('T3T4', length=7, delay_cost=1)
	T3T4 += alt(MUL)
	S+=T3T4>=T3T4_in

	T3T4_mem0 = S.Task('T3T4_mem0', length=1, delay_cost=1)
	T3T4_mem0 += alt(ADD_mem)
	S += (T3T2*ADD[0])-1<T3T4_mem0*ADD_mem[0]
	S += (T3T2*ADD[1])-1<T3T4_mem0*ADD_mem[1]
	S += (T3T2*ADD[2])-1<T3T4_mem0*ADD_mem[2]
	S += (T3T2*ADD[3])-1<T3T4_mem0*ADD_mem[3]
	S += T3T4_mem0<=T3T4

	T3T4_mem1 = S.Task('T3T4_mem1', length=1, delay_cost=1)
	T3T4_mem1 += alt(ADD_mem)
	S += (T3T3*ADD[0])-1<T3T4_mem1*ADD_mem[0]
	S += (T3T3*ADD[1])-1<T3T4_mem1*ADD_mem[1]
	S += (T3T3*ADD[2])-1<T3T4_mem1*ADD_mem[2]
	S += (T3T3*ADD[3])-1<T3T4_mem1*ADD_mem[3]
	S += T3T4_mem1<=T3T4

	T3T5 = S.Task('T3T5', length=1, delay_cost=1)
	T3T5 += alt(ADD)

	T3T5_mem0 = S.Task('T3T5_mem0', length=1, delay_cost=1)
	T3T5_mem0 += alt(MUL_mem)
	S += (T3T0*MUL[0])-1<T3T5_mem0*MUL_mem[0]
	S += T3T5_mem0<=T3T5

	T3T5_mem1 = S.Task('T3T5_mem1', length=1, delay_cost=1)
	T3T5_mem1 += alt(MUL_mem)
	S += (T3T1*MUL[0])-1<T3T5_mem1*MUL_mem[0]
	S += T3T5_mem1<=T3T5

	T30 = S.Task('T30', length=1, delay_cost=1)
	T30 += alt(ADD)

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += alt(MUL_mem)
	S += (T3T0*MUL[0])-1<T30_mem0*MUL_mem[0]
	S += T30_mem0<=T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += alt(MUL_mem)
	S += (T3T1*MUL[0])-1<T30_mem1*MUL_mem[0]
	S += T30_mem1<=T30

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	T40_in += alt(MUL_in)
	T40 = S.Task('T40', length=7, delay_cost=1)
	T40 += alt(MUL)
	S+=T40>=T40_in

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += alt(ADD_mem)
	S += (T4T0*ADD[0])-1<T40_mem0*ADD_mem[0]
	S += (T4T0*ADD[1])-1<T40_mem0*ADD_mem[1]
	S += (T4T0*ADD[2])-1<T40_mem0*ADD_mem[2]
	S += (T4T0*ADD[3])-1<T40_mem0*ADD_mem[3]
	S += T40_mem0<=T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += alt(ADD_mem)
	S += (T4T1*ADD[0])-1<T40_mem1*ADD_mem[0]
	S += (T4T1*ADD[1])-1<T40_mem1*ADD_mem[1]
	S += (T4T1*ADD[2])-1<T40_mem1*ADD_mem[2]
	S += (T4T1*ADD[3])-1<T40_mem1*ADD_mem[3]
	S += T40_mem1<=T40

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(ADD)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += alt(MUL_mem)
	S += (T4T2*MUL[0])-1<T41_mem0*MUL_mem[0]
	S += T41_mem0<=T41

	T5T4_in = S.Task('T5T4_in', length=1, delay_cost=1)
	T5T4_in += alt(MUL_in)
	T5T4 = S.Task('T5T4', length=7, delay_cost=1)
	T5T4 += alt(MUL)
	S+=T5T4>=T5T4_in

	T5T4_mem0 = S.Task('T5T4_mem0', length=1, delay_cost=1)
	T5T4_mem0 += alt(ADD_mem)
	S += (T5T2*ADD[0])-1<T5T4_mem0*ADD_mem[0]
	S += (T5T2*ADD[1])-1<T5T4_mem0*ADD_mem[1]
	S += (T5T2*ADD[2])-1<T5T4_mem0*ADD_mem[2]
	S += (T5T2*ADD[3])-1<T5T4_mem0*ADD_mem[3]
	S += T5T4_mem0<=T5T4

	T5T4_mem1 = S.Task('T5T4_mem1', length=1, delay_cost=1)
	T5T4_mem1 += alt(ADD_mem)
	S += (T5T3*ADD[0])-1<T5T4_mem1*ADD_mem[0]
	S += (T5T3*ADD[1])-1<T5T4_mem1*ADD_mem[1]
	S += (T5T3*ADD[2])-1<T5T4_mem1*ADD_mem[2]
	S += (T5T3*ADD[3])-1<T5T4_mem1*ADD_mem[3]
	S += T5T4_mem1<=T5T4

	T5T5 = S.Task('T5T5', length=1, delay_cost=1)
	T5T5 += alt(ADD)

	T5T5_mem0 = S.Task('T5T5_mem0', length=1, delay_cost=1)
	T5T5_mem0 += alt(MUL_mem)
	S += (T5T0*MUL[0])-1<T5T5_mem0*MUL_mem[0]
	S += T5T5_mem0<=T5T5

	T5T5_mem1 = S.Task('T5T5_mem1', length=1, delay_cost=1)
	T5T5_mem1 += alt(MUL_mem)
	S += (T5T1*MUL[0])-1<T5T5_mem1*MUL_mem[0]
	S += T5T5_mem1<=T5T5

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(ADD)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += alt(MUL_mem)
	S += (T5T0*MUL[0])-1<T50_mem0*MUL_mem[0]
	S += T50_mem0<=T50

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	T50_mem1 += alt(MUL_mem)
	S += (T5T1*MUL[0])-1<T50_mem1*MUL_mem[0]
	S += T50_mem1<=T50

	T6T4_in = S.Task('T6T4_in', length=1, delay_cost=1)
	T6T4_in += alt(MUL_in)
	T6T4 = S.Task('T6T4', length=7, delay_cost=1)
	T6T4 += alt(MUL)
	S+=T6T4>=T6T4_in

	T6T4_mem0 = S.Task('T6T4_mem0', length=1, delay_cost=1)
	T6T4_mem0 += alt(ADD_mem)
	S += (T6T2*ADD[0])-1<T6T4_mem0*ADD_mem[0]
	S += (T6T2*ADD[1])-1<T6T4_mem0*ADD_mem[1]
	S += (T6T2*ADD[2])-1<T6T4_mem0*ADD_mem[2]
	S += (T6T2*ADD[3])-1<T6T4_mem0*ADD_mem[3]
	S += T6T4_mem0<=T6T4

	T6T4_mem1 = S.Task('T6T4_mem1', length=1, delay_cost=1)
	T6T4_mem1 += alt(ADD_mem)
	S += (T6T3*ADD[0])-1<T6T4_mem1*ADD_mem[0]
	S += (T6T3*ADD[1])-1<T6T4_mem1*ADD_mem[1]
	S += (T6T3*ADD[2])-1<T6T4_mem1*ADD_mem[2]
	S += (T6T3*ADD[3])-1<T6T4_mem1*ADD_mem[3]
	S += T6T4_mem1<=T6T4

	T6T5 = S.Task('T6T5', length=1, delay_cost=1)
	T6T5 += alt(ADD)

	T6T5_mem0 = S.Task('T6T5_mem0', length=1, delay_cost=1)
	T6T5_mem0 += alt(MUL_mem)
	S += (T6T0*MUL[0])-1<T6T5_mem0*MUL_mem[0]
	S += T6T5_mem0<=T6T5

	T6T5_mem1 = S.Task('T6T5_mem1', length=1, delay_cost=1)
	T6T5_mem1 += alt(MUL_mem)
	S += (T6T1*MUL[0])-1<T6T5_mem1*MUL_mem[0]
	S += T6T5_mem1<=T6T5

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(ADD)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += alt(MUL_mem)
	S += (T6T0*MUL[0])-1<T60_mem0*MUL_mem[0]
	S += T60_mem0<=T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += alt(MUL_mem)
	S += (T6T1*MUL[0])-1<T60_mem1*MUL_mem[0]
	S += T60_mem1<=T60

	T7T4_in = S.Task('T7T4_in', length=1, delay_cost=1)
	T7T4_in += alt(MUL_in)
	T7T4 = S.Task('T7T4', length=7, delay_cost=1)
	T7T4 += alt(MUL)
	S+=T7T4>=T7T4_in

	T7T4_mem0 = S.Task('T7T4_mem0', length=1, delay_cost=1)
	T7T4_mem0 += alt(ADD_mem)
	S += (T7T2*ADD[0])-1<T7T4_mem0*ADD_mem[0]
	S += (T7T2*ADD[1])-1<T7T4_mem0*ADD_mem[1]
	S += (T7T2*ADD[2])-1<T7T4_mem0*ADD_mem[2]
	S += (T7T2*ADD[3])-1<T7T4_mem0*ADD_mem[3]
	S += T7T4_mem0<=T7T4

	T7T4_mem1 = S.Task('T7T4_mem1', length=1, delay_cost=1)
	T7T4_mem1 += alt(ADD_mem)
	S += (T7T3*ADD[0])-1<T7T4_mem1*ADD_mem[0]
	S += (T7T3*ADD[1])-1<T7T4_mem1*ADD_mem[1]
	S += (T7T3*ADD[2])-1<T7T4_mem1*ADD_mem[2]
	S += (T7T3*ADD[3])-1<T7T4_mem1*ADD_mem[3]
	S += T7T4_mem1<=T7T4

	T7T5 = S.Task('T7T5', length=1, delay_cost=1)
	T7T5 += alt(ADD)

	T7T5_mem0 = S.Task('T7T5_mem0', length=1, delay_cost=1)
	T7T5_mem0 += alt(MUL_mem)
	S += (T7T0*MUL[0])-1<T7T5_mem0*MUL_mem[0]
	S += T7T5_mem0<=T7T5

	T7T5_mem1 = S.Task('T7T5_mem1', length=1, delay_cost=1)
	T7T5_mem1 += alt(MUL_mem)
	S += (T7T1*MUL[0])-1<T7T5_mem1*MUL_mem[0]
	S += T7T5_mem1<=T7T5

	T70 = S.Task('T70', length=1, delay_cost=1)
	T70 += alt(ADD)

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	T70_mem0 += alt(MUL_mem)
	S += (T7T0*MUL[0])-1<T70_mem0*MUL_mem[0]
	S += T70_mem0<=T70

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	T70_mem1 += alt(MUL_mem)
	S += (T7T1*MUL[0])-1<T70_mem1*MUL_mem[0]
	S += T70_mem1<=T70

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "SQR012345_mul1_add4/SQR012345_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_SQR012345_mul1_add4_0(0, 0)