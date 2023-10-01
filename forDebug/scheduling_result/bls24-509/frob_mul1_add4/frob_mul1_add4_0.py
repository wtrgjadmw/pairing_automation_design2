from pyschedule import Scenario, solvers, plotters, alt

def solve_frob_mul1_add4_0(ConstStep, ExpStep):
	horizon = 621
	S=Scenario("frob_mul1_add4_0",horizon = horizon)

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
	T001 = S.Task('T001', length=1, delay_cost=1)
	T001 += alt(ADD)

	T0t0_in = S.Task('T0t0_in', length=1, delay_cost=1)
	T0t0_in += alt(MUL_in)
	T0t0 = S.Task('T0t0', length=7, delay_cost=1)
	T0t0 += alt(MUL)
	S+=T0t0>=T0t0_in

	T0t1_in = S.Task('T0t1_in', length=1, delay_cost=1)
	T0t1_in += alt(MUL_in)
	T0t1 = S.Task('T0t1', length=7, delay_cost=1)
	T0t1 += alt(MUL)
	S+=T0t1>=T0t1_in

	T0t2 = S.Task('T0t2', length=1, delay_cost=1)
	T0t2 += alt(ADD)

	T0t3 = S.Task('T0t3', length=1, delay_cost=1)
	T0t3 += alt(ADD)

	T101 = S.Task('T101', length=1, delay_cost=1)
	T101 += alt(ADD)

	T1t0_in = S.Task('T1t0_in', length=1, delay_cost=1)
	T1t0_in += alt(MUL_in)
	T1t0 = S.Task('T1t0', length=7, delay_cost=1)
	T1t0 += alt(MUL)
	S+=T1t0>=T1t0_in

	T1t1_in = S.Task('T1t1_in', length=1, delay_cost=1)
	T1t1_in += alt(MUL_in)
	T1t1 = S.Task('T1t1', length=7, delay_cost=1)
	T1t1 += alt(MUL)
	S+=T1t1>=T1t1_in

	T1t2 = S.Task('T1t2', length=1, delay_cost=1)
	T1t2 += alt(ADD)

	T201 = S.Task('T201', length=1, delay_cost=1)
	T201 += alt(ADD)

	T2t0_in = S.Task('T2t0_in', length=1, delay_cost=1)
	T2t0_in += alt(MUL_in)
	T2t0 = S.Task('T2t0', length=7, delay_cost=1)
	T2t0 += alt(MUL)
	S+=T2t0>=T2t0_in

	T2t1_in = S.Task('T2t1_in', length=1, delay_cost=1)
	T2t1_in += alt(MUL_in)
	T2t1 = S.Task('T2t1', length=7, delay_cost=1)
	T2t1 += alt(MUL)
	S+=T2t1>=T2t1_in

	T2t2 = S.Task('T2t2', length=1, delay_cost=1)
	T2t2 += alt(ADD)

	T301 = S.Task('T301', length=1, delay_cost=1)
	T301 += alt(ADD)

	T3t0_in = S.Task('T3t0_in', length=1, delay_cost=1)
	T3t0_in += alt(MUL_in)
	T3t0 = S.Task('T3t0', length=7, delay_cost=1)
	T3t0 += alt(MUL)
	S+=T3t0>=T3t0_in

	T3t1_in = S.Task('T3t1_in', length=1, delay_cost=1)
	T3t1_in += alt(MUL_in)
	T3t1 = S.Task('T3t1', length=7, delay_cost=1)
	T3t1 += alt(MUL)
	S+=T3t1>=T3t1_in

	T3t2 = S.Task('T3t2', length=1, delay_cost=1)
	T3t2 += alt(ADD)

	T401 = S.Task('T401', length=1, delay_cost=1)
	T401 += alt(ADD)

	T4t0_in = S.Task('T4t0_in', length=1, delay_cost=1)
	T4t0_in += alt(MUL_in)
	T4t0 = S.Task('T4t0', length=7, delay_cost=1)
	T4t0 += alt(MUL)
	S+=T4t0>=T4t0_in

	T4t1_in = S.Task('T4t1_in', length=1, delay_cost=1)
	T4t1_in += alt(MUL_in)
	T4t1 = S.Task('T4t1', length=7, delay_cost=1)
	T4t1 += alt(MUL)
	S+=T4t1>=T4t1_in

	T4t2 = S.Task('T4t2', length=1, delay_cost=1)
	T4t2 += alt(ADD)

	C00t0_in = S.Task('C00t0_in', length=1, delay_cost=1)
	C00t0_in += alt(MUL_in)
	C00t0 = S.Task('C00t0', length=7, delay_cost=1)
	C00t0 += alt(MUL)
	S+=C00t0>=C00t0_in

	C00t1_in = S.Task('C00t1_in', length=1, delay_cost=1)
	C00t1_in += alt(MUL_in)
	C00t1 = S.Task('C00t1', length=7, delay_cost=1)
	C00t1 += alt(MUL)
	S+=C00t1>=C00t1_in

	C00t2 = S.Task('C00t2', length=1, delay_cost=1)
	C00t2 += alt(ADD)

	C10t3_0 = S.Task('C10t3_0', length=1, delay_cost=1)
	C10t3_0 += alt(ADD)

	C10t3_1 = S.Task('C10t3_1', length=1, delay_cost=1)
	C10t3_1 += alt(ADD)

	C10t0_a0b0_in = S.Task('C10t0_a0b0_in', length=1, delay_cost=1)
	C10t0_a0b0_in += alt(MUL_in)
	C10t0_a0b0 = S.Task('C10t0_a0b0', length=7, delay_cost=1)
	C10t0_a0b0 += alt(MUL)
	S+=C10t0_a0b0>=C10t0_a0b0_in

	C10t3_a0b0 = S.Task('C10t3_a0b0', length=1, delay_cost=1)
	C10t3_a0b0 += alt(ADD)

	C10t3_a1b1 = S.Task('C10t3_a1b1', length=1, delay_cost=1)
	C10t3_a1b1 += alt(ADD)

	C01t3_0 = S.Task('C01t3_0', length=1, delay_cost=1)
	C01t3_0 += alt(ADD)

	C01t3_1 = S.Task('C01t3_1', length=1, delay_cost=1)
	C01t3_1 += alt(ADD)

	C01t0_a0b0_in = S.Task('C01t0_a0b0_in', length=1, delay_cost=1)
	C01t0_a0b0_in += alt(MUL_in)
	C01t0_a0b0 = S.Task('C01t0_a0b0', length=7, delay_cost=1)
	C01t0_a0b0 += alt(MUL)
	S+=C01t0_a0b0>=C01t0_a0b0_in

	C01t3_a0b0 = S.Task('C01t3_a0b0', length=1, delay_cost=1)
	C01t3_a0b0 += alt(ADD)

	C01t3_a1b1 = S.Task('C01t3_a1b1', length=1, delay_cost=1)
	C01t3_a1b1 += alt(ADD)

	C11t3_0 = S.Task('C11t3_0', length=1, delay_cost=1)
	C11t3_0 += alt(ADD)

	C11t3_1 = S.Task('C11t3_1', length=1, delay_cost=1)
	C11t3_1 += alt(ADD)

	C11t0_a0b0_in = S.Task('C11t0_a0b0_in', length=1, delay_cost=1)
	C11t0_a0b0_in += alt(MUL_in)
	C11t0_a0b0 = S.Task('C11t0_a0b0', length=7, delay_cost=1)
	C11t0_a0b0 += alt(MUL)
	S+=C11t0_a0b0>=C11t0_a0b0_in

	C11t3_a0b0 = S.Task('C11t3_a0b0', length=1, delay_cost=1)
	C11t3_a0b0 += alt(ADD)

	C11t3_a1b1 = S.Task('C11t3_a1b1', length=1, delay_cost=1)
	C11t3_a1b1 += alt(ADD)

	C02t3_0 = S.Task('C02t3_0', length=1, delay_cost=1)
	C02t3_0 += alt(ADD)

	C02t3_1 = S.Task('C02t3_1', length=1, delay_cost=1)
	C02t3_1 += alt(ADD)

	C02t0_a0b0_in = S.Task('C02t0_a0b0_in', length=1, delay_cost=1)
	C02t0_a0b0_in += alt(MUL_in)
	C02t0_a0b0 = S.Task('C02t0_a0b0', length=7, delay_cost=1)
	C02t0_a0b0 += alt(MUL)
	S+=C02t0_a0b0>=C02t0_a0b0_in

	C02t3_a0b0 = S.Task('C02t3_a0b0', length=1, delay_cost=1)
	C02t3_a0b0 += alt(ADD)

	C02t3_a1b1 = S.Task('C02t3_a1b1', length=1, delay_cost=1)
	C02t3_a1b1 += alt(ADD)

	C12t3_0 = S.Task('C12t3_0', length=1, delay_cost=1)
	C12t3_0 += alt(ADD)

	C12t3_1 = S.Task('C12t3_1', length=1, delay_cost=1)
	C12t3_1 += alt(ADD)

	C12t0_a0b0_in = S.Task('C12t0_a0b0_in', length=1, delay_cost=1)
	C12t0_a0b0_in += alt(MUL_in)
	C12t0_a0b0 = S.Task('C12t0_a0b0', length=7, delay_cost=1)
	C12t0_a0b0 += alt(MUL)
	S+=C12t0_a0b0>=C12t0_a0b0_in

	C12t3_a0b0 = S.Task('C12t3_a0b0', length=1, delay_cost=1)
	C12t3_a0b0 += alt(ADD)

	C12t3_a1b1 = S.Task('C12t3_a1b1', length=1, delay_cost=1)
	C12t3_a1b1 += alt(ADD)

	T001_mem0 = S.Task('T001_mem0', length=1, delay_cost=1)
	T001_mem0 += INPUT_mem_r
	S += T001_mem0<=T001

	T001_mem1 = S.Task('T001_mem1', length=1, delay_cost=1)
	T001_mem1 += INPUT_mem_r
	S += T001_mem1<=T001

	T0t0_mem0 = S.Task('T0t0_mem0', length=1, delay_cost=1)
	T0t0_mem0 += INPUT_mem_r
	S += T0t0_mem0<=T0t0

	T0t0_mem1 = S.Task('T0t0_mem1', length=1, delay_cost=1)
	T0t0_mem1 += INPUT_mem_r
	S += T0t0_mem1<=T0t0

	T0t1_mem0 = S.Task('T0t1_mem0', length=1, delay_cost=1)
	T0t1_mem0 += INPUT_mem_r
	S += T0t1_mem0<=T0t1

	T0t1_mem1 = S.Task('T0t1_mem1', length=1, delay_cost=1)
	T0t1_mem1 += INPUT_mem_r
	S += T0t1_mem1<=T0t1

	T0t2_mem0 = S.Task('T0t2_mem0', length=1, delay_cost=1)
	T0t2_mem0 += INPUT_mem_r
	S += T0t2_mem0<=T0t2

	T0t2_mem1 = S.Task('T0t2_mem1', length=1, delay_cost=1)
	T0t2_mem1 += INPUT_mem_r
	S += T0t2_mem1<=T0t2

	T0t3_mem0 = S.Task('T0t3_mem0', length=1, delay_cost=1)
	T0t3_mem0 += INPUT_mem_r
	S += T0t3_mem0<=T0t3

	T0t3_mem1 = S.Task('T0t3_mem1', length=1, delay_cost=1)
	T0t3_mem1 += INPUT_mem_r
	S += T0t3_mem1<=T0t3

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	T101_mem0 += INPUT_mem_r
	S += T101_mem0<=T101

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	T101_mem1 += INPUT_mem_r
	S += T101_mem1<=T101

	T1t0_mem0 = S.Task('T1t0_mem0', length=1, delay_cost=1)
	T1t0_mem0 += INPUT_mem_r
	S += T1t0_mem0<=T1t0

	T1t0_mem1 = S.Task('T1t0_mem1', length=1, delay_cost=1)
	T1t0_mem1 += INPUT_mem_r
	S += T1t0_mem1<=T1t0

	T1t1_mem0 = S.Task('T1t1_mem0', length=1, delay_cost=1)
	T1t1_mem0 += INPUT_mem_r
	S += T1t1_mem0<=T1t1

	T1t1_mem1 = S.Task('T1t1_mem1', length=1, delay_cost=1)
	T1t1_mem1 += INPUT_mem_r
	S += T1t1_mem1<=T1t1

	T1t2_mem0 = S.Task('T1t2_mem0', length=1, delay_cost=1)
	T1t2_mem0 += INPUT_mem_r
	S += T1t2_mem0<=T1t2

	T1t2_mem1 = S.Task('T1t2_mem1', length=1, delay_cost=1)
	T1t2_mem1 += INPUT_mem_r
	S += T1t2_mem1<=T1t2

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	T201_mem0 += INPUT_mem_r
	S += T201_mem0<=T201

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	T201_mem1 += INPUT_mem_r
	S += T201_mem1<=T201

	T2t0_mem0 = S.Task('T2t0_mem0', length=1, delay_cost=1)
	T2t0_mem0 += INPUT_mem_r
	S += T2t0_mem0<=T2t0

	T2t0_mem1 = S.Task('T2t0_mem1', length=1, delay_cost=1)
	T2t0_mem1 += INPUT_mem_r
	S += T2t0_mem1<=T2t0

	T2t1_mem0 = S.Task('T2t1_mem0', length=1, delay_cost=1)
	T2t1_mem0 += INPUT_mem_r
	S += T2t1_mem0<=T2t1

	T2t1_mem1 = S.Task('T2t1_mem1', length=1, delay_cost=1)
	T2t1_mem1 += INPUT_mem_r
	S += T2t1_mem1<=T2t1

	T2t2_mem0 = S.Task('T2t2_mem0', length=1, delay_cost=1)
	T2t2_mem0 += INPUT_mem_r
	S += T2t2_mem0<=T2t2

	T2t2_mem1 = S.Task('T2t2_mem1', length=1, delay_cost=1)
	T2t2_mem1 += INPUT_mem_r
	S += T2t2_mem1<=T2t2

	T301_mem0 = S.Task('T301_mem0', length=1, delay_cost=1)
	T301_mem0 += INPUT_mem_r
	S += T301_mem0<=T301

	T301_mem1 = S.Task('T301_mem1', length=1, delay_cost=1)
	T301_mem1 += INPUT_mem_r
	S += T301_mem1<=T301

	T3t0_mem0 = S.Task('T3t0_mem0', length=1, delay_cost=1)
	T3t0_mem0 += INPUT_mem_r
	S += T3t0_mem0<=T3t0

	T3t0_mem1 = S.Task('T3t0_mem1', length=1, delay_cost=1)
	T3t0_mem1 += INPUT_mem_r
	S += T3t0_mem1<=T3t0

	T3t1_mem0 = S.Task('T3t1_mem0', length=1, delay_cost=1)
	T3t1_mem0 += INPUT_mem_r
	S += T3t1_mem0<=T3t1

	T3t1_mem1 = S.Task('T3t1_mem1', length=1, delay_cost=1)
	T3t1_mem1 += INPUT_mem_r
	S += T3t1_mem1<=T3t1

	T3t2_mem0 = S.Task('T3t2_mem0', length=1, delay_cost=1)
	T3t2_mem0 += INPUT_mem_r
	S += T3t2_mem0<=T3t2

	T3t2_mem1 = S.Task('T3t2_mem1', length=1, delay_cost=1)
	T3t2_mem1 += INPUT_mem_r
	S += T3t2_mem1<=T3t2

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	T401_mem0 += INPUT_mem_r
	S += T401_mem0<=T401

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	T401_mem1 += INPUT_mem_r
	S += T401_mem1<=T401

	T4t0_mem0 = S.Task('T4t0_mem0', length=1, delay_cost=1)
	T4t0_mem0 += INPUT_mem_r
	S += T4t0_mem0<=T4t0

	T4t0_mem1 = S.Task('T4t0_mem1', length=1, delay_cost=1)
	T4t0_mem1 += INPUT_mem_r
	S += T4t0_mem1<=T4t0

	T4t1_mem0 = S.Task('T4t1_mem0', length=1, delay_cost=1)
	T4t1_mem0 += INPUT_mem_r
	S += T4t1_mem0<=T4t1

	T4t1_mem1 = S.Task('T4t1_mem1', length=1, delay_cost=1)
	T4t1_mem1 += INPUT_mem_r
	S += T4t1_mem1<=T4t1

	T4t2_mem0 = S.Task('T4t2_mem0', length=1, delay_cost=1)
	T4t2_mem0 += INPUT_mem_r
	S += T4t2_mem0<=T4t2

	T4t2_mem1 = S.Task('T4t2_mem1', length=1, delay_cost=1)
	T4t2_mem1 += INPUT_mem_r
	S += T4t2_mem1<=T4t2

	C00t0_mem0 = S.Task('C00t0_mem0', length=1, delay_cost=1)
	C00t0_mem0 += INPUT_mem_r
	S += C00t0_mem0<=C00t0

	C00t0_mem1 = S.Task('C00t0_mem1', length=1, delay_cost=1)
	C00t0_mem1 += INPUT_mem_r
	S += C00t0_mem1<=C00t0

	C00t1_mem0 = S.Task('C00t1_mem0', length=1, delay_cost=1)
	C00t1_mem0 += INPUT_mem_r
	S += C00t1_mem0<=C00t1

	C00t1_mem1 = S.Task('C00t1_mem1', length=1, delay_cost=1)
	C00t1_mem1 += INPUT_mem_r
	S += C00t1_mem1<=C00t1

	C00t2_mem0 = S.Task('C00t2_mem0', length=1, delay_cost=1)
	C00t2_mem0 += INPUT_mem_r
	S += C00t2_mem0<=C00t2

	C00t2_mem1 = S.Task('C00t2_mem1', length=1, delay_cost=1)
	C00t2_mem1 += INPUT_mem_r
	S += C00t2_mem1<=C00t2

	C10t3_0_mem0 = S.Task('C10t3_0_mem0', length=1, delay_cost=1)
	C10t3_0_mem0 += INPUT_mem_r
	S += C10t3_0_mem0<=C10t3_0

	C10t3_0_mem1 = S.Task('C10t3_0_mem1', length=1, delay_cost=1)
	C10t3_0_mem1 += INPUT_mem_r
	S += C10t3_0_mem1<=C10t3_0

	C10t3_1_mem0 = S.Task('C10t3_1_mem0', length=1, delay_cost=1)
	C10t3_1_mem0 += INPUT_mem_r
	S += C10t3_1_mem0<=C10t3_1

	C10t3_1_mem1 = S.Task('C10t3_1_mem1', length=1, delay_cost=1)
	C10t3_1_mem1 += INPUT_mem_r
	S += C10t3_1_mem1<=C10t3_1

	C10t0_a0b0_mem0 = S.Task('C10t0_a0b0_mem0', length=1, delay_cost=1)
	C10t0_a0b0_mem0 += INPUT_mem_r
	S += C10t0_a0b0_mem0<=C10t0_a0b0

	C10t0_a0b0_mem1 = S.Task('C10t0_a0b0_mem1', length=1, delay_cost=1)
	C10t0_a0b0_mem1 += INPUT_mem_r
	S += C10t0_a0b0_mem1<=C10t0_a0b0

	C10t3_a0b0_mem0 = S.Task('C10t3_a0b0_mem0', length=1, delay_cost=1)
	C10t3_a0b0_mem0 += INPUT_mem_r
	S += C10t3_a0b0_mem0<=C10t3_a0b0

	C10t3_a0b0_mem1 = S.Task('C10t3_a0b0_mem1', length=1, delay_cost=1)
	C10t3_a0b0_mem1 += INPUT_mem_r
	S += C10t3_a0b0_mem1<=C10t3_a0b0

	C10t3_a1b1_mem0 = S.Task('C10t3_a1b1_mem0', length=1, delay_cost=1)
	C10t3_a1b1_mem0 += INPUT_mem_r
	S += C10t3_a1b1_mem0<=C10t3_a1b1

	C10t3_a1b1_mem1 = S.Task('C10t3_a1b1_mem1', length=1, delay_cost=1)
	C10t3_a1b1_mem1 += INPUT_mem_r
	S += C10t3_a1b1_mem1<=C10t3_a1b1

	C01t3_0_mem0 = S.Task('C01t3_0_mem0', length=1, delay_cost=1)
	C01t3_0_mem0 += INPUT_mem_r
	S += C01t3_0_mem0<=C01t3_0

	C01t3_0_mem1 = S.Task('C01t3_0_mem1', length=1, delay_cost=1)
	C01t3_0_mem1 += INPUT_mem_r
	S += C01t3_0_mem1<=C01t3_0

	C01t3_1_mem0 = S.Task('C01t3_1_mem0', length=1, delay_cost=1)
	C01t3_1_mem0 += INPUT_mem_r
	S += C01t3_1_mem0<=C01t3_1

	C01t3_1_mem1 = S.Task('C01t3_1_mem1', length=1, delay_cost=1)
	C01t3_1_mem1 += INPUT_mem_r
	S += C01t3_1_mem1<=C01t3_1

	C01t0_a0b0_mem0 = S.Task('C01t0_a0b0_mem0', length=1, delay_cost=1)
	C01t0_a0b0_mem0 += INPUT_mem_r
	S += C01t0_a0b0_mem0<=C01t0_a0b0

	C01t0_a0b0_mem1 = S.Task('C01t0_a0b0_mem1', length=1, delay_cost=1)
	C01t0_a0b0_mem1 += INPUT_mem_r
	S += C01t0_a0b0_mem1<=C01t0_a0b0

	C01t3_a0b0_mem0 = S.Task('C01t3_a0b0_mem0', length=1, delay_cost=1)
	C01t3_a0b0_mem0 += INPUT_mem_r
	S += C01t3_a0b0_mem0<=C01t3_a0b0

	C01t3_a0b0_mem1 = S.Task('C01t3_a0b0_mem1', length=1, delay_cost=1)
	C01t3_a0b0_mem1 += INPUT_mem_r
	S += C01t3_a0b0_mem1<=C01t3_a0b0

	C01t3_a1b1_mem0 = S.Task('C01t3_a1b1_mem0', length=1, delay_cost=1)
	C01t3_a1b1_mem0 += INPUT_mem_r
	S += C01t3_a1b1_mem0<=C01t3_a1b1

	C01t3_a1b1_mem1 = S.Task('C01t3_a1b1_mem1', length=1, delay_cost=1)
	C01t3_a1b1_mem1 += INPUT_mem_r
	S += C01t3_a1b1_mem1<=C01t3_a1b1

	C11t3_0_mem0 = S.Task('C11t3_0_mem0', length=1, delay_cost=1)
	C11t3_0_mem0 += INPUT_mem_r
	S += C11t3_0_mem0<=C11t3_0

	C11t3_0_mem1 = S.Task('C11t3_0_mem1', length=1, delay_cost=1)
	C11t3_0_mem1 += INPUT_mem_r
	S += C11t3_0_mem1<=C11t3_0

	C11t3_1_mem0 = S.Task('C11t3_1_mem0', length=1, delay_cost=1)
	C11t3_1_mem0 += INPUT_mem_r
	S += C11t3_1_mem0<=C11t3_1

	C11t3_1_mem1 = S.Task('C11t3_1_mem1', length=1, delay_cost=1)
	C11t3_1_mem1 += INPUT_mem_r
	S += C11t3_1_mem1<=C11t3_1

	C11t0_a0b0_mem0 = S.Task('C11t0_a0b0_mem0', length=1, delay_cost=1)
	C11t0_a0b0_mem0 += INPUT_mem_r
	S += C11t0_a0b0_mem0<=C11t0_a0b0

	C11t0_a0b0_mem1 = S.Task('C11t0_a0b0_mem1', length=1, delay_cost=1)
	C11t0_a0b0_mem1 += INPUT_mem_r
	S += C11t0_a0b0_mem1<=C11t0_a0b0

	C11t3_a0b0_mem0 = S.Task('C11t3_a0b0_mem0', length=1, delay_cost=1)
	C11t3_a0b0_mem0 += INPUT_mem_r
	S += C11t3_a0b0_mem0<=C11t3_a0b0

	C11t3_a0b0_mem1 = S.Task('C11t3_a0b0_mem1', length=1, delay_cost=1)
	C11t3_a0b0_mem1 += INPUT_mem_r
	S += C11t3_a0b0_mem1<=C11t3_a0b0

	C11t3_a1b1_mem0 = S.Task('C11t3_a1b1_mem0', length=1, delay_cost=1)
	C11t3_a1b1_mem0 += INPUT_mem_r
	S += C11t3_a1b1_mem0<=C11t3_a1b1

	C11t3_a1b1_mem1 = S.Task('C11t3_a1b1_mem1', length=1, delay_cost=1)
	C11t3_a1b1_mem1 += INPUT_mem_r
	S += C11t3_a1b1_mem1<=C11t3_a1b1

	C02t3_0_mem0 = S.Task('C02t3_0_mem0', length=1, delay_cost=1)
	C02t3_0_mem0 += INPUT_mem_r
	S += C02t3_0_mem0<=C02t3_0

	C02t3_0_mem1 = S.Task('C02t3_0_mem1', length=1, delay_cost=1)
	C02t3_0_mem1 += INPUT_mem_r
	S += C02t3_0_mem1<=C02t3_0

	C02t3_1_mem0 = S.Task('C02t3_1_mem0', length=1, delay_cost=1)
	C02t3_1_mem0 += INPUT_mem_r
	S += C02t3_1_mem0<=C02t3_1

	C02t3_1_mem1 = S.Task('C02t3_1_mem1', length=1, delay_cost=1)
	C02t3_1_mem1 += INPUT_mem_r
	S += C02t3_1_mem1<=C02t3_1

	C02t0_a0b0_mem0 = S.Task('C02t0_a0b0_mem0', length=1, delay_cost=1)
	C02t0_a0b0_mem0 += INPUT_mem_r
	S += C02t0_a0b0_mem0<=C02t0_a0b0

	C02t0_a0b0_mem1 = S.Task('C02t0_a0b0_mem1', length=1, delay_cost=1)
	C02t0_a0b0_mem1 += INPUT_mem_r
	S += C02t0_a0b0_mem1<=C02t0_a0b0

	C02t3_a0b0_mem0 = S.Task('C02t3_a0b0_mem0', length=1, delay_cost=1)
	C02t3_a0b0_mem0 += INPUT_mem_r
	S += C02t3_a0b0_mem0<=C02t3_a0b0

	C02t3_a0b0_mem1 = S.Task('C02t3_a0b0_mem1', length=1, delay_cost=1)
	C02t3_a0b0_mem1 += INPUT_mem_r
	S += C02t3_a0b0_mem1<=C02t3_a0b0

	C02t3_a1b1_mem0 = S.Task('C02t3_a1b1_mem0', length=1, delay_cost=1)
	C02t3_a1b1_mem0 += INPUT_mem_r
	S += C02t3_a1b1_mem0<=C02t3_a1b1

	C02t3_a1b1_mem1 = S.Task('C02t3_a1b1_mem1', length=1, delay_cost=1)
	C02t3_a1b1_mem1 += INPUT_mem_r
	S += C02t3_a1b1_mem1<=C02t3_a1b1

	C12t3_0_mem0 = S.Task('C12t3_0_mem0', length=1, delay_cost=1)
	C12t3_0_mem0 += INPUT_mem_r
	S += C12t3_0_mem0<=C12t3_0

	C12t3_0_mem1 = S.Task('C12t3_0_mem1', length=1, delay_cost=1)
	C12t3_0_mem1 += INPUT_mem_r
	S += C12t3_0_mem1<=C12t3_0

	C12t3_1_mem0 = S.Task('C12t3_1_mem0', length=1, delay_cost=1)
	C12t3_1_mem0 += INPUT_mem_r
	S += C12t3_1_mem0<=C12t3_1

	C12t3_1_mem1 = S.Task('C12t3_1_mem1', length=1, delay_cost=1)
	C12t3_1_mem1 += INPUT_mem_r
	S += C12t3_1_mem1<=C12t3_1

	C12t0_a0b0_mem0 = S.Task('C12t0_a0b0_mem0', length=1, delay_cost=1)
	C12t0_a0b0_mem0 += INPUT_mem_r
	S += C12t0_a0b0_mem0<=C12t0_a0b0

	C12t0_a0b0_mem1 = S.Task('C12t0_a0b0_mem1', length=1, delay_cost=1)
	C12t0_a0b0_mem1 += INPUT_mem_r
	S += C12t0_a0b0_mem1<=C12t0_a0b0

	C12t3_a0b0_mem0 = S.Task('C12t3_a0b0_mem0', length=1, delay_cost=1)
	C12t3_a0b0_mem0 += INPUT_mem_r
	S += C12t3_a0b0_mem0<=C12t3_a0b0

	C12t3_a0b0_mem1 = S.Task('C12t3_a0b0_mem1', length=1, delay_cost=1)
	C12t3_a0b0_mem1 += INPUT_mem_r
	S += C12t3_a0b0_mem1<=C12t3_a0b0

	C12t3_a1b1_mem0 = S.Task('C12t3_a1b1_mem0', length=1, delay_cost=1)
	C12t3_a1b1_mem0 += INPUT_mem_r
	S += C12t3_a1b1_mem0<=C12t3_a1b1

	C12t3_a1b1_mem1 = S.Task('C12t3_a1b1_mem1', length=1, delay_cost=1)
	C12t3_a1b1_mem1 += INPUT_mem_r
	S += C12t3_a1b1_mem1<=C12t3_a1b1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "frob_mul1_add4/frob_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_frob_mul1_add4_0(0, 0)