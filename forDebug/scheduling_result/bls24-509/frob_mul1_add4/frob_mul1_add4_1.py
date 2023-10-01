from pyschedule import Scenario, solvers, plotters, alt

def solve_frob_mul1_add4_1(ConstStep, ExpStep):
	horizon = 621
	S=Scenario("frob_mul1_add4_1",horizon = horizon)

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
	T1t0_in = S.Task('T1t0_in', length=1, delay_cost=1)
	S += T1t0_in >= 0
	T1t0_in += MUL_in[0]

	T1t0_mem0 = S.Task('T1t0_mem0', length=1, delay_cost=1)
	S += T1t0_mem0 >= 0
	T1t0_mem0 += INPUT_mem_r

	T1t0_mem1 = S.Task('T1t0_mem1', length=1, delay_cost=1)
	S += T1t0_mem1 >= 0
	T1t0_mem1 += INPUT_mem_r

	T1t0 = S.Task('T1t0', length=7, delay_cost=1)
	S += T1t0 >= 1
	T1t0 += MUL[0]

	T2t0_in = S.Task('T2t0_in', length=1, delay_cost=1)
	S += T2t0_in >= 1
	T2t0_in += MUL_in[0]

	T2t0_mem0 = S.Task('T2t0_mem0', length=1, delay_cost=1)
	S += T2t0_mem0 >= 1
	T2t0_mem0 += INPUT_mem_r

	T2t0_mem1 = S.Task('T2t0_mem1', length=1, delay_cost=1)
	S += T2t0_mem1 >= 1
	T2t0_mem1 += INPUT_mem_r

	T2t0 = S.Task('T2t0', length=7, delay_cost=1)
	S += T2t0 >= 2
	T2t0 += MUL[0]

	T2t1_in = S.Task('T2t1_in', length=1, delay_cost=1)
	S += T2t1_in >= 2
	T2t1_in += MUL_in[0]

	T2t1_mem0 = S.Task('T2t1_mem0', length=1, delay_cost=1)
	S += T2t1_mem0 >= 2
	T2t1_mem0 += INPUT_mem_r

	T2t1_mem1 = S.Task('T2t1_mem1', length=1, delay_cost=1)
	S += T2t1_mem1 >= 2
	T2t1_mem1 += INPUT_mem_r

	T0t0_in = S.Task('T0t0_in', length=1, delay_cost=1)
	S += T0t0_in >= 3
	T0t0_in += MUL_in[0]

	T0t0_mem0 = S.Task('T0t0_mem0', length=1, delay_cost=1)
	S += T0t0_mem0 >= 3
	T0t0_mem0 += INPUT_mem_r

	T0t0_mem1 = S.Task('T0t0_mem1', length=1, delay_cost=1)
	S += T0t0_mem1 >= 3
	T0t0_mem1 += INPUT_mem_r

	T2t1 = S.Task('T2t1', length=7, delay_cost=1)
	S += T2t1 >= 3
	T2t1 += MUL[0]

	C00t1_in = S.Task('C00t1_in', length=1, delay_cost=1)
	S += C00t1_in >= 4
	C00t1_in += MUL_in[0]

	C00t1_mem0 = S.Task('C00t1_mem0', length=1, delay_cost=1)
	S += C00t1_mem0 >= 4
	C00t1_mem0 += INPUT_mem_r

	C00t1_mem1 = S.Task('C00t1_mem1', length=1, delay_cost=1)
	S += C00t1_mem1 >= 4
	C00t1_mem1 += INPUT_mem_r

	T0t0 = S.Task('T0t0', length=7, delay_cost=1)
	S += T0t0 >= 4
	T0t0 += MUL[0]

	C00t1 = S.Task('C00t1', length=7, delay_cost=1)
	S += C00t1 >= 5
	C00t1 += MUL[0]

	T4t0_in = S.Task('T4t0_in', length=1, delay_cost=1)
	S += T4t0_in >= 5
	T4t0_in += MUL_in[0]

	T4t0_mem0 = S.Task('T4t0_mem0', length=1, delay_cost=1)
	S += T4t0_mem0 >= 5
	T4t0_mem0 += INPUT_mem_r

	T4t0_mem1 = S.Task('T4t0_mem1', length=1, delay_cost=1)
	S += T4t0_mem1 >= 5
	T4t0_mem1 += INPUT_mem_r

	C02t0_a0b0_in = S.Task('C02t0_a0b0_in', length=1, delay_cost=1)
	S += C02t0_a0b0_in >= 6
	C02t0_a0b0_in += MUL_in[0]

	C02t0_a0b0_mem0 = S.Task('C02t0_a0b0_mem0', length=1, delay_cost=1)
	S += C02t0_a0b0_mem0 >= 6
	C02t0_a0b0_mem0 += INPUT_mem_r

	C02t0_a0b0_mem1 = S.Task('C02t0_a0b0_mem1', length=1, delay_cost=1)
	S += C02t0_a0b0_mem1 >= 6
	C02t0_a0b0_mem1 += INPUT_mem_r

	T4t0 = S.Task('T4t0', length=7, delay_cost=1)
	S += T4t0 >= 6
	T4t0 += MUL[0]

	C02t0_a0b0 = S.Task('C02t0_a0b0', length=7, delay_cost=1)
	S += C02t0_a0b0 >= 7
	C02t0_a0b0 += MUL[0]

	C10t0_a0b0_in = S.Task('C10t0_a0b0_in', length=1, delay_cost=1)
	S += C10t0_a0b0_in >= 7
	C10t0_a0b0_in += MUL_in[0]

	C10t0_a0b0_mem0 = S.Task('C10t0_a0b0_mem0', length=1, delay_cost=1)
	S += C10t0_a0b0_mem0 >= 7
	C10t0_a0b0_mem0 += INPUT_mem_r

	C10t0_a0b0_mem1 = S.Task('C10t0_a0b0_mem1', length=1, delay_cost=1)
	S += C10t0_a0b0_mem1 >= 7
	C10t0_a0b0_mem1 += INPUT_mem_r

	C10t0_a0b0 = S.Task('C10t0_a0b0', length=7, delay_cost=1)
	S += C10t0_a0b0 >= 8
	C10t0_a0b0 += MUL[0]

	T1t1_in = S.Task('T1t1_in', length=1, delay_cost=1)
	S += T1t1_in >= 8
	T1t1_in += MUL_in[0]

	T1t1_mem0 = S.Task('T1t1_mem0', length=1, delay_cost=1)
	S += T1t1_mem0 >= 8
	T1t1_mem0 += INPUT_mem_r

	T1t1_mem1 = S.Task('T1t1_mem1', length=1, delay_cost=1)
	S += T1t1_mem1 >= 8
	T1t1_mem1 += INPUT_mem_r

	T1t1 = S.Task('T1t1', length=7, delay_cost=1)
	S += T1t1 >= 9
	T1t1 += MUL[0]

	T3t1_in = S.Task('T3t1_in', length=1, delay_cost=1)
	S += T3t1_in >= 9
	T3t1_in += MUL_in[0]

	T3t1_mem0 = S.Task('T3t1_mem0', length=1, delay_cost=1)
	S += T3t1_mem0 >= 9
	T3t1_mem0 += INPUT_mem_r

	T3t1_mem1 = S.Task('T3t1_mem1', length=1, delay_cost=1)
	S += T3t1_mem1 >= 9
	T3t1_mem1 += INPUT_mem_r

	T0t1_in = S.Task('T0t1_in', length=1, delay_cost=1)
	S += T0t1_in >= 10
	T0t1_in += MUL_in[0]

	T0t1_mem0 = S.Task('T0t1_mem0', length=1, delay_cost=1)
	S += T0t1_mem0 >= 10
	T0t1_mem0 += INPUT_mem_r

	T0t1_mem1 = S.Task('T0t1_mem1', length=1, delay_cost=1)
	S += T0t1_mem1 >= 10
	T0t1_mem1 += INPUT_mem_r

	T3t1 = S.Task('T3t1', length=7, delay_cost=1)
	S += T3t1 >= 10
	T3t1 += MUL[0]

	C01t0_a0b0_in = S.Task('C01t0_a0b0_in', length=1, delay_cost=1)
	S += C01t0_a0b0_in >= 11
	C01t0_a0b0_in += MUL_in[0]

	C01t0_a0b0_mem0 = S.Task('C01t0_a0b0_mem0', length=1, delay_cost=1)
	S += C01t0_a0b0_mem0 >= 11
	C01t0_a0b0_mem0 += INPUT_mem_r

	C01t0_a0b0_mem1 = S.Task('C01t0_a0b0_mem1', length=1, delay_cost=1)
	S += C01t0_a0b0_mem1 >= 11
	C01t0_a0b0_mem1 += INPUT_mem_r

	T0t1 = S.Task('T0t1', length=7, delay_cost=1)
	S += T0t1 >= 11
	T0t1 += MUL[0]

	C01t0_a0b0 = S.Task('C01t0_a0b0', length=7, delay_cost=1)
	S += C01t0_a0b0 >= 12
	C01t0_a0b0 += MUL[0]

	C12t0_a0b0_in = S.Task('C12t0_a0b0_in', length=1, delay_cost=1)
	S += C12t0_a0b0_in >= 12
	C12t0_a0b0_in += MUL_in[0]

	C12t0_a0b0_mem0 = S.Task('C12t0_a0b0_mem0', length=1, delay_cost=1)
	S += C12t0_a0b0_mem0 >= 12
	C12t0_a0b0_mem0 += INPUT_mem_r

	C12t0_a0b0_mem1 = S.Task('C12t0_a0b0_mem1', length=1, delay_cost=1)
	S += C12t0_a0b0_mem1 >= 12
	C12t0_a0b0_mem1 += INPUT_mem_r

	C12t0_a0b0 = S.Task('C12t0_a0b0', length=7, delay_cost=1)
	S += C12t0_a0b0 >= 13
	C12t0_a0b0 += MUL[0]

	T3t0_in = S.Task('T3t0_in', length=1, delay_cost=1)
	S += T3t0_in >= 13
	T3t0_in += MUL_in[0]

	T3t0_mem0 = S.Task('T3t0_mem0', length=1, delay_cost=1)
	S += T3t0_mem0 >= 13
	T3t0_mem0 += INPUT_mem_r

	T3t0_mem1 = S.Task('T3t0_mem1', length=1, delay_cost=1)
	S += T3t0_mem1 >= 13
	T3t0_mem1 += INPUT_mem_r

	C11t0_a0b0_in = S.Task('C11t0_a0b0_in', length=1, delay_cost=1)
	S += C11t0_a0b0_in >= 14
	C11t0_a0b0_in += MUL_in[0]

	C11t0_a0b0_mem0 = S.Task('C11t0_a0b0_mem0', length=1, delay_cost=1)
	S += C11t0_a0b0_mem0 >= 14
	C11t0_a0b0_mem0 += INPUT_mem_r

	C11t0_a0b0_mem1 = S.Task('C11t0_a0b0_mem1', length=1, delay_cost=1)
	S += C11t0_a0b0_mem1 >= 14
	C11t0_a0b0_mem1 += INPUT_mem_r

	T3t0 = S.Task('T3t0', length=7, delay_cost=1)
	S += T3t0 >= 14
	T3t0 += MUL[0]

	C11t0_a0b0 = S.Task('C11t0_a0b0', length=7, delay_cost=1)
	S += C11t0_a0b0 >= 15
	C11t0_a0b0 += MUL[0]

	T4t1_in = S.Task('T4t1_in', length=1, delay_cost=1)
	S += T4t1_in >= 15
	T4t1_in += MUL_in[0]

	T4t1_mem0 = S.Task('T4t1_mem0', length=1, delay_cost=1)
	S += T4t1_mem0 >= 15
	T4t1_mem0 += INPUT_mem_r

	T4t1_mem1 = S.Task('T4t1_mem1', length=1, delay_cost=1)
	S += T4t1_mem1 >= 15
	T4t1_mem1 += INPUT_mem_r

	C00t0_in = S.Task('C00t0_in', length=1, delay_cost=1)
	S += C00t0_in >= 16
	C00t0_in += MUL_in[0]

	C00t0_mem0 = S.Task('C00t0_mem0', length=1, delay_cost=1)
	S += C00t0_mem0 >= 16
	C00t0_mem0 += INPUT_mem_r

	C00t0_mem1 = S.Task('C00t0_mem1', length=1, delay_cost=1)
	S += C00t0_mem1 >= 16
	C00t0_mem1 += INPUT_mem_r

	T4t1 = S.Task('T4t1', length=7, delay_cost=1)
	S += T4t1 >= 16
	T4t1 += MUL[0]

	C00t0 = S.Task('C00t0', length=7, delay_cost=1)
	S += C00t0 >= 17
	C00t0 += MUL[0]

	C10t3_0_mem0 = S.Task('C10t3_0_mem0', length=1, delay_cost=1)
	S += C10t3_0_mem0 >= 17
	C10t3_0_mem0 += INPUT_mem_r

	C10t3_0_mem1 = S.Task('C10t3_0_mem1', length=1, delay_cost=1)
	S += C10t3_0_mem1 >= 17
	C10t3_0_mem1 += INPUT_mem_r

	C10t3_0 = S.Task('C10t3_0', length=1, delay_cost=1)
	S += C10t3_0 >= 18
	C10t3_0 += ADD[0]

	T301_mem0 = S.Task('T301_mem0', length=1, delay_cost=1)
	S += T301_mem0 >= 18
	T301_mem0 += INPUT_mem_r

	T301_mem1 = S.Task('T301_mem1', length=1, delay_cost=1)
	S += T301_mem1 >= 18
	T301_mem1 += INPUT_mem_r

	T301 = S.Task('T301', length=1, delay_cost=1)
	S += T301 >= 19
	T301 += ADD[1]

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	S += T401_mem0 >= 19
	T401_mem0 += INPUT_mem_r

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	S += T401_mem1 >= 19
	T401_mem1 += INPUT_mem_r

	C12t3_0_mem0 = S.Task('C12t3_0_mem0', length=1, delay_cost=1)
	S += C12t3_0_mem0 >= 20
	C12t3_0_mem0 += INPUT_mem_r

	C12t3_0_mem1 = S.Task('C12t3_0_mem1', length=1, delay_cost=1)
	S += C12t3_0_mem1 >= 20
	C12t3_0_mem1 += INPUT_mem_r

	T401 = S.Task('T401', length=1, delay_cost=1)
	S += T401 >= 20
	T401 += ADD[2]

	C02t3_1_mem0 = S.Task('C02t3_1_mem0', length=1, delay_cost=1)
	S += C02t3_1_mem0 >= 21
	C02t3_1_mem0 += INPUT_mem_r

	C02t3_1_mem1 = S.Task('C02t3_1_mem1', length=1, delay_cost=1)
	S += C02t3_1_mem1 >= 21
	C02t3_1_mem1 += INPUT_mem_r

	C12t3_0 = S.Task('C12t3_0', length=1, delay_cost=1)
	S += C12t3_0 >= 21
	C12t3_0 += ADD[0]

	C02t3_1 = S.Task('C02t3_1', length=1, delay_cost=1)
	S += C02t3_1 >= 22
	C02t3_1 += ADD[1]

	C12t3_1_mem0 = S.Task('C12t3_1_mem0', length=1, delay_cost=1)
	S += C12t3_1_mem0 >= 22
	C12t3_1_mem0 += INPUT_mem_r

	C12t3_1_mem1 = S.Task('C12t3_1_mem1', length=1, delay_cost=1)
	S += C12t3_1_mem1 >= 22
	C12t3_1_mem1 += INPUT_mem_r

	C12t3_1 = S.Task('C12t3_1', length=1, delay_cost=1)
	S += C12t3_1 >= 23
	C12t3_1 += ADD[1]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 23
	T101_mem0 += INPUT_mem_r

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 23
	T101_mem1 += INPUT_mem_r

	C12t3_a1b1_mem0 = S.Task('C12t3_a1b1_mem0', length=1, delay_cost=1)
	S += C12t3_a1b1_mem0 >= 24
	C12t3_a1b1_mem0 += INPUT_mem_r

	C12t3_a1b1_mem1 = S.Task('C12t3_a1b1_mem1', length=1, delay_cost=1)
	S += C12t3_a1b1_mem1 >= 24
	C12t3_a1b1_mem1 += INPUT_mem_r

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 24
	T101 += ADD[1]

	C02t3_0_mem0 = S.Task('C02t3_0_mem0', length=1, delay_cost=1)
	S += C02t3_0_mem0 >= 25
	C02t3_0_mem0 += INPUT_mem_r

	C02t3_0_mem1 = S.Task('C02t3_0_mem1', length=1, delay_cost=1)
	S += C02t3_0_mem1 >= 25
	C02t3_0_mem1 += INPUT_mem_r

	C12t3_a1b1 = S.Task('C12t3_a1b1', length=1, delay_cost=1)
	S += C12t3_a1b1 >= 25
	C12t3_a1b1 += ADD[3]

	C02t3_0 = S.Task('C02t3_0', length=1, delay_cost=1)
	S += C02t3_0 >= 26
	C02t3_0 += ADD[1]

	T001_mem0 = S.Task('T001_mem0', length=1, delay_cost=1)
	S += T001_mem0 >= 26
	T001_mem0 += INPUT_mem_r

	T001_mem1 = S.Task('T001_mem1', length=1, delay_cost=1)
	S += T001_mem1 >= 26
	T001_mem1 += INPUT_mem_r

	T001 = S.Task('T001', length=1, delay_cost=1)
	S += T001 >= 27
	T001 += ADD[1]

	T1t2_mem0 = S.Task('T1t2_mem0', length=1, delay_cost=1)
	S += T1t2_mem0 >= 27
	T1t2_mem0 += INPUT_mem_r

	T1t2_mem1 = S.Task('T1t2_mem1', length=1, delay_cost=1)
	S += T1t2_mem1 >= 27
	T1t2_mem1 += INPUT_mem_r

	T1t2 = S.Task('T1t2', length=1, delay_cost=1)
	S += T1t2 >= 28
	T1t2 += ADD[3]

	T4t2_mem0 = S.Task('T4t2_mem0', length=1, delay_cost=1)
	S += T4t2_mem0 >= 28
	T4t2_mem0 += INPUT_mem_r

	T4t2_mem1 = S.Task('T4t2_mem1', length=1, delay_cost=1)
	S += T4t2_mem1 >= 28
	T4t2_mem1 += INPUT_mem_r

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	S += T201_mem0 >= 29
	T201_mem0 += INPUT_mem_r

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	S += T201_mem1 >= 29
	T201_mem1 += INPUT_mem_r

	T4t2 = S.Task('T4t2', length=1, delay_cost=1)
	S += T4t2 >= 29
	T4t2 += ADD[0]

	C10t3_a1b1_mem0 = S.Task('C10t3_a1b1_mem0', length=1, delay_cost=1)
	S += C10t3_a1b1_mem0 >= 30
	C10t3_a1b1_mem0 += INPUT_mem_r

	C10t3_a1b1_mem1 = S.Task('C10t3_a1b1_mem1', length=1, delay_cost=1)
	S += C10t3_a1b1_mem1 >= 30
	C10t3_a1b1_mem1 += INPUT_mem_r

	T201 = S.Task('T201', length=1, delay_cost=1)
	S += T201 >= 30
	T201 += ADD[1]

	C10t3_a1b1 = S.Task('C10t3_a1b1', length=1, delay_cost=1)
	S += C10t3_a1b1 >= 31
	C10t3_a1b1 += ADD[1]

	C11t3_a1b1_mem0 = S.Task('C11t3_a1b1_mem0', length=1, delay_cost=1)
	S += C11t3_a1b1_mem0 >= 31
	C11t3_a1b1_mem0 += INPUT_mem_r

	C11t3_a1b1_mem1 = S.Task('C11t3_a1b1_mem1', length=1, delay_cost=1)
	S += C11t3_a1b1_mem1 >= 31
	C11t3_a1b1_mem1 += INPUT_mem_r

	C11t3_a1b1 = S.Task('C11t3_a1b1', length=1, delay_cost=1)
	S += C11t3_a1b1 >= 32
	C11t3_a1b1 += ADD[2]

	T3t2_mem0 = S.Task('T3t2_mem0', length=1, delay_cost=1)
	S += T3t2_mem0 >= 32
	T3t2_mem0 += INPUT_mem_r

	T3t2_mem1 = S.Task('T3t2_mem1', length=1, delay_cost=1)
	S += T3t2_mem1 >= 32
	T3t2_mem1 += INPUT_mem_r

	C12t3_a0b0_mem0 = S.Task('C12t3_a0b0_mem0', length=1, delay_cost=1)
	S += C12t3_a0b0_mem0 >= 33
	C12t3_a0b0_mem0 += INPUT_mem_r

	C12t3_a0b0_mem1 = S.Task('C12t3_a0b0_mem1', length=1, delay_cost=1)
	S += C12t3_a0b0_mem1 >= 33
	C12t3_a0b0_mem1 += INPUT_mem_r

	T3t2 = S.Task('T3t2', length=1, delay_cost=1)
	S += T3t2 >= 33
	T3t2 += ADD[2]

	C10t3_1_mem0 = S.Task('C10t3_1_mem0', length=1, delay_cost=1)
	S += C10t3_1_mem0 >= 34
	C10t3_1_mem0 += INPUT_mem_r

	C10t3_1_mem1 = S.Task('C10t3_1_mem1', length=1, delay_cost=1)
	S += C10t3_1_mem1 >= 34
	C10t3_1_mem1 += INPUT_mem_r

	C12t3_a0b0 = S.Task('C12t3_a0b0', length=1, delay_cost=1)
	S += C12t3_a0b0 >= 34
	C12t3_a0b0 += ADD[2]

	C10t3_1 = S.Task('C10t3_1', length=1, delay_cost=1)
	S += C10t3_1 >= 35
	C10t3_1 += ADD[3]

	T0t3_mem0 = S.Task('T0t3_mem0', length=1, delay_cost=1)
	S += T0t3_mem0 >= 35
	T0t3_mem0 += INPUT_mem_r

	T0t3_mem1 = S.Task('T0t3_mem1', length=1, delay_cost=1)
	S += T0t3_mem1 >= 35
	T0t3_mem1 += INPUT_mem_r

	C00t2_mem0 = S.Task('C00t2_mem0', length=1, delay_cost=1)
	S += C00t2_mem0 >= 36
	C00t2_mem0 += INPUT_mem_r

	C00t2_mem1 = S.Task('C00t2_mem1', length=1, delay_cost=1)
	S += C00t2_mem1 >= 36
	C00t2_mem1 += INPUT_mem_r

	T0t3 = S.Task('T0t3', length=1, delay_cost=1)
	S += T0t3 >= 36
	T0t3 += ADD[0]

	C00t2 = S.Task('C00t2', length=1, delay_cost=1)
	S += C00t2 >= 37
	C00t2 += ADD[1]

	C11t3_0_mem0 = S.Task('C11t3_0_mem0', length=1, delay_cost=1)
	S += C11t3_0_mem0 >= 37
	C11t3_0_mem0 += INPUT_mem_r

	C11t3_0_mem1 = S.Task('C11t3_0_mem1', length=1, delay_cost=1)
	S += C11t3_0_mem1 >= 37
	C11t3_0_mem1 += INPUT_mem_r

	C10t3_a0b0_mem0 = S.Task('C10t3_a0b0_mem0', length=1, delay_cost=1)
	S += C10t3_a0b0_mem0 >= 38
	C10t3_a0b0_mem0 += INPUT_mem_r

	C10t3_a0b0_mem1 = S.Task('C10t3_a0b0_mem1', length=1, delay_cost=1)
	S += C10t3_a0b0_mem1 >= 38
	C10t3_a0b0_mem1 += INPUT_mem_r

	C11t3_0 = S.Task('C11t3_0', length=1, delay_cost=1)
	S += C11t3_0 >= 38
	C11t3_0 += ADD[3]

	C02t3_a0b0_mem0 = S.Task('C02t3_a0b0_mem0', length=1, delay_cost=1)
	S += C02t3_a0b0_mem0 >= 39
	C02t3_a0b0_mem0 += INPUT_mem_r

	C02t3_a0b0_mem1 = S.Task('C02t3_a0b0_mem1', length=1, delay_cost=1)
	S += C02t3_a0b0_mem1 >= 39
	C02t3_a0b0_mem1 += INPUT_mem_r

	C10t3_a0b0 = S.Task('C10t3_a0b0', length=1, delay_cost=1)
	S += C10t3_a0b0 >= 39
	C10t3_a0b0 += ADD[1]

	C01t3_a1b1_mem0 = S.Task('C01t3_a1b1_mem0', length=1, delay_cost=1)
	S += C01t3_a1b1_mem0 >= 40
	C01t3_a1b1_mem0 += INPUT_mem_r

	C01t3_a1b1_mem1 = S.Task('C01t3_a1b1_mem1', length=1, delay_cost=1)
	S += C01t3_a1b1_mem1 >= 40
	C01t3_a1b1_mem1 += INPUT_mem_r

	C02t3_a0b0 = S.Task('C02t3_a0b0', length=1, delay_cost=1)
	S += C02t3_a0b0 >= 40
	C02t3_a0b0 += ADD[0]

	C01t3_a1b1 = S.Task('C01t3_a1b1', length=1, delay_cost=1)
	S += C01t3_a1b1 >= 41
	C01t3_a1b1 += ADD[0]

	C02t3_a1b1_mem0 = S.Task('C02t3_a1b1_mem0', length=1, delay_cost=1)
	S += C02t3_a1b1_mem0 >= 41
	C02t3_a1b1_mem0 += INPUT_mem_r

	C02t3_a1b1_mem1 = S.Task('C02t3_a1b1_mem1', length=1, delay_cost=1)
	S += C02t3_a1b1_mem1 >= 41
	C02t3_a1b1_mem1 += INPUT_mem_r

	C02t3_a1b1 = S.Task('C02t3_a1b1', length=1, delay_cost=1)
	S += C02t3_a1b1 >= 42
	C02t3_a1b1 += ADD[0]

	T0t2_mem0 = S.Task('T0t2_mem0', length=1, delay_cost=1)
	S += T0t2_mem0 >= 42
	T0t2_mem0 += INPUT_mem_r

	T0t2_mem1 = S.Task('T0t2_mem1', length=1, delay_cost=1)
	S += T0t2_mem1 >= 42
	T0t2_mem1 += INPUT_mem_r

	C11t3_a0b0_mem0 = S.Task('C11t3_a0b0_mem0', length=1, delay_cost=1)
	S += C11t3_a0b0_mem0 >= 43
	C11t3_a0b0_mem0 += INPUT_mem_r

	C11t3_a0b0_mem1 = S.Task('C11t3_a0b0_mem1', length=1, delay_cost=1)
	S += C11t3_a0b0_mem1 >= 43
	C11t3_a0b0_mem1 += INPUT_mem_r

	T0t2 = S.Task('T0t2', length=1, delay_cost=1)
	S += T0t2 >= 43
	T0t2 += ADD[3]

	C11t3_1_mem0 = S.Task('C11t3_1_mem0', length=1, delay_cost=1)
	S += C11t3_1_mem0 >= 44
	C11t3_1_mem0 += INPUT_mem_r

	C11t3_1_mem1 = S.Task('C11t3_1_mem1', length=1, delay_cost=1)
	S += C11t3_1_mem1 >= 44
	C11t3_1_mem1 += INPUT_mem_r

	C11t3_a0b0 = S.Task('C11t3_a0b0', length=1, delay_cost=1)
	S += C11t3_a0b0 >= 44
	C11t3_a0b0 += ADD[0]

	C11t3_1 = S.Task('C11t3_1', length=1, delay_cost=1)
	S += C11t3_1 >= 45
	C11t3_1 += ADD[0]

	T2t2_mem0 = S.Task('T2t2_mem0', length=1, delay_cost=1)
	S += T2t2_mem0 >= 45
	T2t2_mem0 += INPUT_mem_r

	T2t2_mem1 = S.Task('T2t2_mem1', length=1, delay_cost=1)
	S += T2t2_mem1 >= 45
	T2t2_mem1 += INPUT_mem_r

	C01t3_a0b0_mem0 = S.Task('C01t3_a0b0_mem0', length=1, delay_cost=1)
	S += C01t3_a0b0_mem0 >= 46
	C01t3_a0b0_mem0 += INPUT_mem_r

	C01t3_a0b0_mem1 = S.Task('C01t3_a0b0_mem1', length=1, delay_cost=1)
	S += C01t3_a0b0_mem1 >= 46
	C01t3_a0b0_mem1 += INPUT_mem_r

	T2t2 = S.Task('T2t2', length=1, delay_cost=1)
	S += T2t2 >= 46
	T2t2 += ADD[0]

	C01t3_1_mem0 = S.Task('C01t3_1_mem0', length=1, delay_cost=1)
	S += C01t3_1_mem0 >= 47
	C01t3_1_mem0 += INPUT_mem_r

	C01t3_1_mem1 = S.Task('C01t3_1_mem1', length=1, delay_cost=1)
	S += C01t3_1_mem1 >= 47
	C01t3_1_mem1 += INPUT_mem_r

	C01t3_a0b0 = S.Task('C01t3_a0b0', length=1, delay_cost=1)
	S += C01t3_a0b0 >= 47
	C01t3_a0b0 += ADD[1]

	C01t3_0_mem0 = S.Task('C01t3_0_mem0', length=1, delay_cost=1)
	S += C01t3_0_mem0 >= 48
	C01t3_0_mem0 += INPUT_mem_r

	C01t3_0_mem1 = S.Task('C01t3_0_mem1', length=1, delay_cost=1)
	S += C01t3_0_mem1 >= 48
	C01t3_0_mem1 += INPUT_mem_r

	C01t3_1 = S.Task('C01t3_1', length=1, delay_cost=1)
	S += C01t3_1 >= 48
	C01t3_1 += ADD[3]

	C01t3_0 = S.Task('C01t3_0', length=1, delay_cost=1)
	S += C01t3_0 >= 49
	C01t3_0 += ADD[1]



	# new tasks
	T0t4_in = S.Task('T0t4_in', length=1, delay_cost=1)
	T0t4_in += alt(MUL_in)
	T0t4 = S.Task('T0t4', length=7, delay_cost=1)
	T0t4 += alt(MUL)
	S+=T0t4>=T0t4_in

	T010 = S.Task('T010', length=1, delay_cost=1)
	T010 += alt(ADD)

	T1t4_in = S.Task('T1t4_in', length=1, delay_cost=1)
	T1t4_in += alt(MUL_in)
	T1t4 = S.Task('T1t4', length=7, delay_cost=1)
	T1t4 += alt(MUL)
	S+=T1t4>=T1t4_in

	T110 = S.Task('T110', length=1, delay_cost=1)
	T110 += alt(ADD)

	T2t4_in = S.Task('T2t4_in', length=1, delay_cost=1)
	T2t4_in += alt(MUL_in)
	T2t4 = S.Task('T2t4', length=7, delay_cost=1)
	T2t4 += alt(MUL)
	S+=T2t4>=T2t4_in

	T210 = S.Task('T210', length=1, delay_cost=1)
	T210 += alt(ADD)

	T3t4_in = S.Task('T3t4_in', length=1, delay_cost=1)
	T3t4_in += alt(MUL_in)
	T3t4 = S.Task('T3t4', length=7, delay_cost=1)
	T3t4 += alt(MUL)
	S+=T3t4>=T3t4_in

	T310 = S.Task('T310', length=1, delay_cost=1)
	T310 += alt(ADD)

	T4t4_in = S.Task('T4t4_in', length=1, delay_cost=1)
	T4t4_in += alt(MUL_in)
	T4t4 = S.Task('T4t4', length=7, delay_cost=1)
	T4t4 += alt(MUL)
	S+=T4t4>=T4t4_in

	T410 = S.Task('T410', length=1, delay_cost=1)
	T410 += alt(ADD)

	C00t4_in = S.Task('C00t4_in', length=1, delay_cost=1)
	C00t4_in += alt(MUL_in)
	C00t4 = S.Task('C00t4', length=7, delay_cost=1)
	C00t4 += alt(MUL)
	S+=C00t4>=C00t4_in

	C10t1_a0b0_in = S.Task('C10t1_a0b0_in', length=1, delay_cost=1)
	C10t1_a0b0_in += alt(MUL_in)
	C10t1_a0b0 = S.Task('C10t1_a0b0', length=7, delay_cost=1)
	C10t1_a0b0 += alt(MUL)
	S+=C10t1_a0b0>=C10t1_a0b0_in

	C10t2_a0b0 = S.Task('C10t2_a0b0', length=1, delay_cost=1)
	C10t2_a0b0 += alt(ADD)

	C10t3_t2t3 = S.Task('C10t3_t2t3', length=1, delay_cost=1)
	C10t3_t2t3 += alt(ADD)

	C01t1_a0b0_in = S.Task('C01t1_a0b0_in', length=1, delay_cost=1)
	C01t1_a0b0_in += alt(MUL_in)
	C01t1_a0b0 = S.Task('C01t1_a0b0', length=7, delay_cost=1)
	C01t1_a0b0 += alt(MUL)
	S+=C01t1_a0b0>=C01t1_a0b0_in

	C01t2_a0b0 = S.Task('C01t2_a0b0', length=1, delay_cost=1)
	C01t2_a0b0 += alt(ADD)

	C01t3_t2t3 = S.Task('C01t3_t2t3', length=1, delay_cost=1)
	C01t3_t2t3 += alt(ADD)

	C11t1_a0b0_in = S.Task('C11t1_a0b0_in', length=1, delay_cost=1)
	C11t1_a0b0_in += alt(MUL_in)
	C11t1_a0b0 = S.Task('C11t1_a0b0', length=7, delay_cost=1)
	C11t1_a0b0 += alt(MUL)
	S+=C11t1_a0b0>=C11t1_a0b0_in

	C11t2_a0b0 = S.Task('C11t2_a0b0', length=1, delay_cost=1)
	C11t2_a0b0 += alt(ADD)

	C11t3_t2t3 = S.Task('C11t3_t2t3', length=1, delay_cost=1)
	C11t3_t2t3 += alt(ADD)

	C02t1_a0b0_in = S.Task('C02t1_a0b0_in', length=1, delay_cost=1)
	C02t1_a0b0_in += alt(MUL_in)
	C02t1_a0b0 = S.Task('C02t1_a0b0', length=7, delay_cost=1)
	C02t1_a0b0 += alt(MUL)
	S+=C02t1_a0b0>=C02t1_a0b0_in

	C02t2_a0b0 = S.Task('C02t2_a0b0', length=1, delay_cost=1)
	C02t2_a0b0 += alt(ADD)

	C02t3_t2t3 = S.Task('C02t3_t2t3', length=1, delay_cost=1)
	C02t3_t2t3 += alt(ADD)

	C12t1_a0b0_in = S.Task('C12t1_a0b0_in', length=1, delay_cost=1)
	C12t1_a0b0_in += alt(MUL_in)
	C12t1_a0b0 = S.Task('C12t1_a0b0', length=7, delay_cost=1)
	C12t1_a0b0 += alt(MUL)
	S+=C12t1_a0b0>=C12t1_a0b0_in

	C12t2_a0b0 = S.Task('C12t2_a0b0', length=1, delay_cost=1)
	C12t2_a0b0 += alt(ADD)

	C12t3_t2t3 = S.Task('C12t3_t2t3', length=1, delay_cost=1)
	C12t3_t2t3 += alt(ADD)

	T0t4_mem0 = S.Task('T0t4_mem0', length=1, delay_cost=1)
	T0t4_mem0 += ADD_mem[3]
	S += 43<T0t4_mem0
	S += T0t4_mem0<=T0t4

	T0t4_mem1 = S.Task('T0t4_mem1', length=1, delay_cost=1)
	T0t4_mem1 += ADD_mem[0]
	S += 36<T0t4_mem1
	S += T0t4_mem1<=T0t4

	T010_mem0 = S.Task('T010_mem0', length=1, delay_cost=1)
	T010_mem0 += MUL_mem[0]
	S += 10<T010_mem0
	S += T010_mem0<=T010

	T010_mem1 = S.Task('T010_mem1', length=1, delay_cost=1)
	T010_mem1 += MUL_mem[0]
	S += 17<T010_mem1
	S += T010_mem1<=T010

	T1t4_mem0 = S.Task('T1t4_mem0', length=1, delay_cost=1)
	T1t4_mem0 += ADD_mem[3]
	S += 28<T1t4_mem0
	S += T1t4_mem0<=T1t4

	T1t4_mem1 = S.Task('T1t4_mem1', length=1, delay_cost=1)
	T1t4_mem1 += ADD_mem[0]
	S += 36<T1t4_mem1
	S += T1t4_mem1<=T1t4

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	T110_mem0 += MUL_mem[0]
	S += 7<T110_mem0
	S += T110_mem0<=T110

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	T110_mem1 += MUL_mem[0]
	S += 15<T110_mem1
	S += T110_mem1<=T110

	T2t4_mem0 = S.Task('T2t4_mem0', length=1, delay_cost=1)
	T2t4_mem0 += ADD_mem[0]
	S += 46<T2t4_mem0
	S += T2t4_mem0<=T2t4

	T2t4_mem1 = S.Task('T2t4_mem1', length=1, delay_cost=1)
	T2t4_mem1 += ADD_mem[0]
	S += 36<T2t4_mem1
	S += T2t4_mem1<=T2t4

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	T210_mem0 += MUL_mem[0]
	S += 8<T210_mem0
	S += T210_mem0<=T210

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	T210_mem1 += MUL_mem[0]
	S += 9<T210_mem1
	S += T210_mem1<=T210

	T3t4_mem0 = S.Task('T3t4_mem0', length=1, delay_cost=1)
	T3t4_mem0 += ADD_mem[2]
	S += 33<T3t4_mem0
	S += T3t4_mem0<=T3t4

	T3t4_mem1 = S.Task('T3t4_mem1', length=1, delay_cost=1)
	T3t4_mem1 += ADD_mem[0]
	S += 36<T3t4_mem1
	S += T3t4_mem1<=T3t4

	T310_mem0 = S.Task('T310_mem0', length=1, delay_cost=1)
	T310_mem0 += MUL_mem[0]
	S += 20<T310_mem0
	S += T310_mem0<=T310

	T310_mem1 = S.Task('T310_mem1', length=1, delay_cost=1)
	T310_mem1 += MUL_mem[0]
	S += 16<T310_mem1
	S += T310_mem1<=T310

	T4t4_mem0 = S.Task('T4t4_mem0', length=1, delay_cost=1)
	T4t4_mem0 += ADD_mem[0]
	S += 29<T4t4_mem0
	S += T4t4_mem0<=T4t4

	T4t4_mem1 = S.Task('T4t4_mem1', length=1, delay_cost=1)
	T4t4_mem1 += ADD_mem[0]
	S += 36<T4t4_mem1
	S += T4t4_mem1<=T4t4

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	T410_mem0 += MUL_mem[0]
	S += 12<T410_mem0
	S += T410_mem0<=T410

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	T410_mem1 += MUL_mem[0]
	S += 22<T410_mem1
	S += T410_mem1<=T410

	C00t4_mem0 = S.Task('C00t4_mem0', length=1, delay_cost=1)
	C00t4_mem0 += ADD_mem[1]
	S += 37<C00t4_mem0
	S += C00t4_mem0<=C00t4

	C00t4_mem1 = S.Task('C00t4_mem1', length=1, delay_cost=1)
	C00t4_mem1 += ADD_mem[0]
	S += 36<C00t4_mem1
	S += C00t4_mem1<=C00t4

	C10t1_a0b0_mem0 = S.Task('C10t1_a0b0_mem0', length=1, delay_cost=1)
	C10t1_a0b0_mem0 += ADD_mem[1]
	S += 27<C10t1_a0b0_mem0
	S += C10t1_a0b0_mem0<=C10t1_a0b0

	C10t1_a0b0_mem1 = S.Task('C10t1_a0b0_mem1', length=1, delay_cost=1)
	C10t1_a0b0_mem1 += INPUT_mem_r
	S += C10t1_a0b0_mem1<=C10t1_a0b0

	C10t2_a0b0_mem0 = S.Task('C10t2_a0b0_mem0', length=1, delay_cost=1)
	C10t2_a0b0_mem0 += INPUT_mem_r
	S += C10t2_a0b0_mem0<=C10t2_a0b0

	C10t2_a0b0_mem1 = S.Task('C10t2_a0b0_mem1', length=1, delay_cost=1)
	C10t2_a0b0_mem1 += ADD_mem[1]
	S += 27<C10t2_a0b0_mem1
	S += C10t2_a0b0_mem1<=C10t2_a0b0

	C10t3_t2t3_mem0 = S.Task('C10t3_t2t3_mem0', length=1, delay_cost=1)
	C10t3_t2t3_mem0 += ADD_mem[0]
	S += 18<C10t3_t2t3_mem0
	S += C10t3_t2t3_mem0<=C10t3_t2t3

	C10t3_t2t3_mem1 = S.Task('C10t3_t2t3_mem1', length=1, delay_cost=1)
	C10t3_t2t3_mem1 += ADD_mem[3]
	S += 35<C10t3_t2t3_mem1
	S += C10t3_t2t3_mem1<=C10t3_t2t3

	C01t1_a0b0_mem0 = S.Task('C01t1_a0b0_mem0', length=1, delay_cost=1)
	C01t1_a0b0_mem0 += ADD_mem[1]
	S += 24<C01t1_a0b0_mem0
	S += C01t1_a0b0_mem0<=C01t1_a0b0

	C01t1_a0b0_mem1 = S.Task('C01t1_a0b0_mem1', length=1, delay_cost=1)
	C01t1_a0b0_mem1 += INPUT_mem_r
	S += C01t1_a0b0_mem1<=C01t1_a0b0

	C01t2_a0b0_mem0 = S.Task('C01t2_a0b0_mem0', length=1, delay_cost=1)
	C01t2_a0b0_mem0 += INPUT_mem_r
	S += C01t2_a0b0_mem0<=C01t2_a0b0

	C01t2_a0b0_mem1 = S.Task('C01t2_a0b0_mem1', length=1, delay_cost=1)
	C01t2_a0b0_mem1 += ADD_mem[1]
	S += 24<C01t2_a0b0_mem1
	S += C01t2_a0b0_mem1<=C01t2_a0b0

	C01t3_t2t3_mem0 = S.Task('C01t3_t2t3_mem0', length=1, delay_cost=1)
	C01t3_t2t3_mem0 += ADD_mem[1]
	S += 49<C01t3_t2t3_mem0
	S += C01t3_t2t3_mem0<=C01t3_t2t3

	C01t3_t2t3_mem1 = S.Task('C01t3_t2t3_mem1', length=1, delay_cost=1)
	C01t3_t2t3_mem1 += ADD_mem[3]
	S += 48<C01t3_t2t3_mem1
	S += C01t3_t2t3_mem1<=C01t3_t2t3

	C11t1_a0b0_mem0 = S.Task('C11t1_a0b0_mem0', length=1, delay_cost=1)
	C11t1_a0b0_mem0 += ADD_mem[1]
	S += 30<C11t1_a0b0_mem0
	S += C11t1_a0b0_mem0<=C11t1_a0b0

	C11t1_a0b0_mem1 = S.Task('C11t1_a0b0_mem1', length=1, delay_cost=1)
	C11t1_a0b0_mem1 += INPUT_mem_r
	S += C11t1_a0b0_mem1<=C11t1_a0b0

	C11t2_a0b0_mem0 = S.Task('C11t2_a0b0_mem0', length=1, delay_cost=1)
	C11t2_a0b0_mem0 += INPUT_mem_r
	S += C11t2_a0b0_mem0<=C11t2_a0b0

	C11t2_a0b0_mem1 = S.Task('C11t2_a0b0_mem1', length=1, delay_cost=1)
	C11t2_a0b0_mem1 += ADD_mem[1]
	S += 30<C11t2_a0b0_mem1
	S += C11t2_a0b0_mem1<=C11t2_a0b0

	C11t3_t2t3_mem0 = S.Task('C11t3_t2t3_mem0', length=1, delay_cost=1)
	C11t3_t2t3_mem0 += ADD_mem[3]
	S += 38<C11t3_t2t3_mem0
	S += C11t3_t2t3_mem0<=C11t3_t2t3

	C11t3_t2t3_mem1 = S.Task('C11t3_t2t3_mem1', length=1, delay_cost=1)
	C11t3_t2t3_mem1 += ADD_mem[0]
	S += 45<C11t3_t2t3_mem1
	S += C11t3_t2t3_mem1<=C11t3_t2t3

	C02t1_a0b0_mem0 = S.Task('C02t1_a0b0_mem0', length=1, delay_cost=1)
	C02t1_a0b0_mem0 += ADD_mem[1]
	S += 19<C02t1_a0b0_mem0
	S += C02t1_a0b0_mem0<=C02t1_a0b0

	C02t1_a0b0_mem1 = S.Task('C02t1_a0b0_mem1', length=1, delay_cost=1)
	C02t1_a0b0_mem1 += INPUT_mem_r
	S += C02t1_a0b0_mem1<=C02t1_a0b0

	C02t2_a0b0_mem0 = S.Task('C02t2_a0b0_mem0', length=1, delay_cost=1)
	C02t2_a0b0_mem0 += INPUT_mem_r
	S += C02t2_a0b0_mem0<=C02t2_a0b0

	C02t2_a0b0_mem1 = S.Task('C02t2_a0b0_mem1', length=1, delay_cost=1)
	C02t2_a0b0_mem1 += ADD_mem[1]
	S += 19<C02t2_a0b0_mem1
	S += C02t2_a0b0_mem1<=C02t2_a0b0

	C02t3_t2t3_mem0 = S.Task('C02t3_t2t3_mem0', length=1, delay_cost=1)
	C02t3_t2t3_mem0 += ADD_mem[1]
	S += 26<C02t3_t2t3_mem0
	S += C02t3_t2t3_mem0<=C02t3_t2t3

	C02t3_t2t3_mem1 = S.Task('C02t3_t2t3_mem1', length=1, delay_cost=1)
	C02t3_t2t3_mem1 += ADD_mem[1]
	S += 22<C02t3_t2t3_mem1
	S += C02t3_t2t3_mem1<=C02t3_t2t3

	C12t1_a0b0_mem0 = S.Task('C12t1_a0b0_mem0', length=1, delay_cost=1)
	C12t1_a0b0_mem0 += ADD_mem[2]
	S += 20<C12t1_a0b0_mem0
	S += C12t1_a0b0_mem0<=C12t1_a0b0

	C12t1_a0b0_mem1 = S.Task('C12t1_a0b0_mem1', length=1, delay_cost=1)
	C12t1_a0b0_mem1 += INPUT_mem_r
	S += C12t1_a0b0_mem1<=C12t1_a0b0

	C12t2_a0b0_mem0 = S.Task('C12t2_a0b0_mem0', length=1, delay_cost=1)
	C12t2_a0b0_mem0 += INPUT_mem_r
	S += C12t2_a0b0_mem0<=C12t2_a0b0

	C12t2_a0b0_mem1 = S.Task('C12t2_a0b0_mem1', length=1, delay_cost=1)
	C12t2_a0b0_mem1 += ADD_mem[2]
	S += 20<C12t2_a0b0_mem1
	S += C12t2_a0b0_mem1<=C12t2_a0b0

	C12t3_t2t3_mem0 = S.Task('C12t3_t2t3_mem0', length=1, delay_cost=1)
	C12t3_t2t3_mem0 += ADD_mem[0]
	S += 21<C12t3_t2t3_mem0
	S += C12t3_t2t3_mem0<=C12t3_t2t3

	C12t3_t2t3_mem1 = S.Task('C12t3_t2t3_mem1', length=1, delay_cost=1)
	C12t3_t2t3_mem1 += ADD_mem[1]
	S += 23<C12t3_t2t3_mem1
	S += C12t3_t2t3_mem1<=C12t3_t2t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "frob_mul1_add4/frob_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_frob_mul1_add4_1(0, 0)