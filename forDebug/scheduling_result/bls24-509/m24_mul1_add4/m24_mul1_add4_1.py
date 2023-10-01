from pyschedule import Scenario, solvers, plotters, alt

def solve_m24_mul1_add4_1(ConstStep, ExpStep):
	horizon = 194
	S=Scenario("m24_mul1_add4_1",horizon = horizon)

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
	T2t0_a1b1_in = S.Task('T2t0_a1b1_in', length=1, delay_cost=1)
	S += T2t0_a1b1_in >= 0
	T2t0_a1b1_in += MUL_in[0]

	T2t0_a1b1_mem0 = S.Task('T2t0_a1b1_mem0', length=1, delay_cost=1)
	S += T2t0_a1b1_mem0 >= 0
	T2t0_a1b1_mem0 += INPUT_mem_r

	T2t0_a1b1_mem1 = S.Task('T2t0_a1b1_mem1', length=1, delay_cost=1)
	S += T2t0_a1b1_mem1 >= 0
	T2t0_a1b1_mem1 += INPUT_mem_r

	T2t0_a0b0_in = S.Task('T2t0_a0b0_in', length=1, delay_cost=1)
	S += T2t0_a0b0_in >= 1
	T2t0_a0b0_in += MUL_in[0]

	T2t0_a0b0_mem0 = S.Task('T2t0_a0b0_mem0', length=1, delay_cost=1)
	S += T2t0_a0b0_mem0 >= 1
	T2t0_a0b0_mem0 += INPUT_mem_r

	T2t0_a0b0_mem1 = S.Task('T2t0_a0b0_mem1', length=1, delay_cost=1)
	S += T2t0_a0b0_mem1 >= 1
	T2t0_a0b0_mem1 += INPUT_mem_r

	T2t0_a1b1 = S.Task('T2t0_a1b1', length=7, delay_cost=1)
	S += T2t0_a1b1 >= 1
	T2t0_a1b1 += MUL[0]

	T1t1_a1b1_in = S.Task('T1t1_a1b1_in', length=1, delay_cost=1)
	S += T1t1_a1b1_in >= 2
	T1t1_a1b1_in += MUL_in[0]

	T1t1_a1b1_mem0 = S.Task('T1t1_a1b1_mem0', length=1, delay_cost=1)
	S += T1t1_a1b1_mem0 >= 2
	T1t1_a1b1_mem0 += INPUT_mem_r

	T1t1_a1b1_mem1 = S.Task('T1t1_a1b1_mem1', length=1, delay_cost=1)
	S += T1t1_a1b1_mem1 >= 2
	T1t1_a1b1_mem1 += INPUT_mem_r

	T2t0_a0b0 = S.Task('T2t0_a0b0', length=7, delay_cost=1)
	S += T2t0_a0b0 >= 2
	T2t0_a0b0 += MUL[0]

	T1t1_a0b0_in = S.Task('T1t1_a0b0_in', length=1, delay_cost=1)
	S += T1t1_a0b0_in >= 3
	T1t1_a0b0_in += MUL_in[0]

	T1t1_a0b0_mem0 = S.Task('T1t1_a0b0_mem0', length=1, delay_cost=1)
	S += T1t1_a0b0_mem0 >= 3
	T1t1_a0b0_mem0 += INPUT_mem_r

	T1t1_a0b0_mem1 = S.Task('T1t1_a0b0_mem1', length=1, delay_cost=1)
	S += T1t1_a0b0_mem1 >= 3
	T1t1_a0b0_mem1 += INPUT_mem_r

	T1t1_a1b1 = S.Task('T1t1_a1b1', length=7, delay_cost=1)
	S += T1t1_a1b1 >= 3
	T1t1_a1b1 += MUL[0]

	T1t0_a1b1_in = S.Task('T1t0_a1b1_in', length=1, delay_cost=1)
	S += T1t0_a1b1_in >= 4
	T1t0_a1b1_in += MUL_in[0]

	T1t0_a1b1_mem0 = S.Task('T1t0_a1b1_mem0', length=1, delay_cost=1)
	S += T1t0_a1b1_mem0 >= 4
	T1t0_a1b1_mem0 += INPUT_mem_r

	T1t0_a1b1_mem1 = S.Task('T1t0_a1b1_mem1', length=1, delay_cost=1)
	S += T1t0_a1b1_mem1 >= 4
	T1t0_a1b1_mem1 += INPUT_mem_r

	T1t1_a0b0 = S.Task('T1t1_a0b0', length=7, delay_cost=1)
	S += T1t1_a0b0 >= 4
	T1t1_a0b0 += MUL[0]

	T0t1_a1b1_in = S.Task('T0t1_a1b1_in', length=1, delay_cost=1)
	S += T0t1_a1b1_in >= 5
	T0t1_a1b1_in += MUL_in[0]

	T0t1_a1b1_mem0 = S.Task('T0t1_a1b1_mem0', length=1, delay_cost=1)
	S += T0t1_a1b1_mem0 >= 5
	T0t1_a1b1_mem0 += INPUT_mem_r

	T0t1_a1b1_mem1 = S.Task('T0t1_a1b1_mem1', length=1, delay_cost=1)
	S += T0t1_a1b1_mem1 >= 5
	T0t1_a1b1_mem1 += INPUT_mem_r

	T1t0_a1b1 = S.Task('T1t0_a1b1', length=7, delay_cost=1)
	S += T1t0_a1b1 >= 5
	T1t0_a1b1 += MUL[0]

	T0t1_a0b0_in = S.Task('T0t1_a0b0_in', length=1, delay_cost=1)
	S += T0t1_a0b0_in >= 6
	T0t1_a0b0_in += MUL_in[0]

	T0t1_a0b0_mem0 = S.Task('T0t1_a0b0_mem0', length=1, delay_cost=1)
	S += T0t1_a0b0_mem0 >= 6
	T0t1_a0b0_mem0 += INPUT_mem_r

	T0t1_a0b0_mem1 = S.Task('T0t1_a0b0_mem1', length=1, delay_cost=1)
	S += T0t1_a0b0_mem1 >= 6
	T0t1_a0b0_mem1 += INPUT_mem_r

	T0t1_a1b1 = S.Task('T0t1_a1b1', length=7, delay_cost=1)
	S += T0t1_a1b1 >= 6
	T0t1_a1b1 += MUL[0]

	T0t0_a1b1_in = S.Task('T0t0_a1b1_in', length=1, delay_cost=1)
	S += T0t0_a1b1_in >= 7
	T0t0_a1b1_in += MUL_in[0]

	T0t0_a1b1_mem0 = S.Task('T0t0_a1b1_mem0', length=1, delay_cost=1)
	S += T0t0_a1b1_mem0 >= 7
	T0t0_a1b1_mem0 += INPUT_mem_r

	T0t0_a1b1_mem1 = S.Task('T0t0_a1b1_mem1', length=1, delay_cost=1)
	S += T0t0_a1b1_mem1 >= 7
	T0t0_a1b1_mem1 += INPUT_mem_r

	T0t1_a0b0 = S.Task('T0t1_a0b0', length=7, delay_cost=1)
	S += T0t1_a0b0 >= 7
	T0t1_a0b0 += MUL[0]

	T0t0_a0b0_in = S.Task('T0t0_a0b0_in', length=1, delay_cost=1)
	S += T0t0_a0b0_in >= 8
	T0t0_a0b0_in += MUL_in[0]

	T0t0_a0b0_mem0 = S.Task('T0t0_a0b0_mem0', length=1, delay_cost=1)
	S += T0t0_a0b0_mem0 >= 8
	T0t0_a0b0_mem0 += INPUT_mem_r

	T0t0_a0b0_mem1 = S.Task('T0t0_a0b0_mem1', length=1, delay_cost=1)
	S += T0t0_a0b0_mem1 >= 8
	T0t0_a0b0_mem1 += INPUT_mem_r

	T0t0_a1b1 = S.Task('T0t0_a1b1', length=7, delay_cost=1)
	S += T0t0_a1b1 >= 8
	T0t0_a1b1 += MUL[0]

	T0t0_a0b0 = S.Task('T0t0_a0b0', length=7, delay_cost=1)
	S += T0t0_a0b0 >= 9
	T0t0_a0b0 += MUL[0]

	T2t1_a1b1_in = S.Task('T2t1_a1b1_in', length=1, delay_cost=1)
	S += T2t1_a1b1_in >= 9
	T2t1_a1b1_in += MUL_in[0]

	T2t1_a1b1_mem0 = S.Task('T2t1_a1b1_mem0', length=1, delay_cost=1)
	S += T2t1_a1b1_mem0 >= 9
	T2t1_a1b1_mem0 += INPUT_mem_r

	T2t1_a1b1_mem1 = S.Task('T2t1_a1b1_mem1', length=1, delay_cost=1)
	S += T2t1_a1b1_mem1 >= 9
	T2t1_a1b1_mem1 += INPUT_mem_r

	T2t1_a0b0_in = S.Task('T2t1_a0b0_in', length=1, delay_cost=1)
	S += T2t1_a0b0_in >= 10
	T2t1_a0b0_in += MUL_in[0]

	T2t1_a0b0_mem0 = S.Task('T2t1_a0b0_mem0', length=1, delay_cost=1)
	S += T2t1_a0b0_mem0 >= 10
	T2t1_a0b0_mem0 += INPUT_mem_r

	T2t1_a0b0_mem1 = S.Task('T2t1_a0b0_mem1', length=1, delay_cost=1)
	S += T2t1_a0b0_mem1 >= 10
	T2t1_a0b0_mem1 += INPUT_mem_r

	T2t1_a1b1 = S.Task('T2t1_a1b1', length=7, delay_cost=1)
	S += T2t1_a1b1 >= 10
	T2t1_a1b1 += MUL[0]

	T1t0_a0b0_in = S.Task('T1t0_a0b0_in', length=1, delay_cost=1)
	S += T1t0_a0b0_in >= 11
	T1t0_a0b0_in += MUL_in[0]

	T1t0_a0b0_mem0 = S.Task('T1t0_a0b0_mem0', length=1, delay_cost=1)
	S += T1t0_a0b0_mem0 >= 11
	T1t0_a0b0_mem0 += INPUT_mem_r

	T1t0_a0b0_mem1 = S.Task('T1t0_a0b0_mem1', length=1, delay_cost=1)
	S += T1t0_a0b0_mem1 >= 11
	T1t0_a0b0_mem1 += INPUT_mem_r

	T2t1_a0b0 = S.Task('T2t1_a0b0', length=7, delay_cost=1)
	S += T2t1_a0b0 >= 11
	T2t1_a0b0 += MUL[0]

	T1t0_a0b0 = S.Task('T1t0_a0b0', length=7, delay_cost=1)
	S += T1t0_a0b0 >= 12
	T1t0_a0b0 += MUL[0]

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	S += T410_mem0 >= 12
	T410_mem0 += INPUT_mem_r

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	S += T410_mem1 >= 12
	T410_mem1 += INPUT_mem_r

	T410 = S.Task('T410', length=1, delay_cost=1)
	S += T410 >= 13
	T410 += ADD[0]

	T601_mem0 = S.Task('T601_mem0', length=1, delay_cost=1)
	S += T601_mem0 >= 13
	T601_mem0 += INPUT_mem_r

	T601_mem1 = S.Task('T601_mem1', length=1, delay_cost=1)
	S += T601_mem1 >= 13
	T601_mem1 += INPUT_mem_r

	T300_mem0 = S.Task('T300_mem0', length=1, delay_cost=1)
	S += T300_mem0 >= 14
	T300_mem0 += INPUT_mem_r

	T300_mem1 = S.Task('T300_mem1', length=1, delay_cost=1)
	S += T300_mem1 >= 14
	T300_mem1 += INPUT_mem_r

	T601 = S.Task('T601', length=1, delay_cost=1)
	S += T601 >= 14
	T601 += ADD[0]

	T300 = S.Task('T300', length=1, delay_cost=1)
	S += T300 >= 15
	T300 += ADD[0]

	T4_110_mem0 = S.Task('T4_110_mem0', length=1, delay_cost=1)
	S += T4_110_mem0 >= 15
	T4_110_mem0 += INPUT_mem_r

	T4_110_mem1 = S.Task('T4_110_mem1', length=1, delay_cost=1)
	S += T4_110_mem1 >= 15
	T4_110_mem1 += INPUT_mem_r

	T4_110 = S.Task('T4_110', length=1, delay_cost=1)
	S += T4_110 >= 16
	T4_110 += ADD[0]

	T5_111_mem0 = S.Task('T5_111_mem0', length=1, delay_cost=1)
	S += T5_111_mem0 >= 16
	T5_111_mem0 += INPUT_mem_r

	T5_111_mem1 = S.Task('T5_111_mem1', length=1, delay_cost=1)
	S += T5_111_mem1 >= 16
	T5_111_mem1 += INPUT_mem_r

	T500_mem0 = S.Task('T500_mem0', length=1, delay_cost=1)
	S += T500_mem0 >= 17
	T500_mem0 += INPUT_mem_r

	T500_mem1 = S.Task('T500_mem1', length=1, delay_cost=1)
	S += T500_mem1 >= 17
	T500_mem1 += INPUT_mem_r

	T5_111 = S.Task('T5_111', length=1, delay_cost=1)
	S += T5_111 >= 17
	T5_111 += ADD[2]

	T4_100_mem0 = S.Task('T4_100_mem0', length=1, delay_cost=1)
	S += T4_100_mem0 >= 18
	T4_100_mem0 += INPUT_mem_r

	T4_100_mem1 = S.Task('T4_100_mem1', length=1, delay_cost=1)
	S += T4_100_mem1 >= 18
	T4_100_mem1 += INPUT_mem_r

	T500 = S.Task('T500', length=1, delay_cost=1)
	S += T500 >= 18
	T500 += ADD[0]

	T4_100 = S.Task('T4_100', length=1, delay_cost=1)
	S += T4_100 >= 19
	T4_100 += ADD[0]

	T511_mem0 = S.Task('T511_mem0', length=1, delay_cost=1)
	S += T511_mem0 >= 19
	T511_mem0 += INPUT_mem_r

	T511_mem1 = S.Task('T511_mem1', length=1, delay_cost=1)
	S += T511_mem1 >= 19
	T511_mem1 += INPUT_mem_r

	T511 = S.Task('T511', length=1, delay_cost=1)
	S += T511 >= 20
	T511 += ADD[0]

	T611_mem0 = S.Task('T611_mem0', length=1, delay_cost=1)
	S += T611_mem0 >= 20
	T611_mem0 += INPUT_mem_r

	T611_mem1 = S.Task('T611_mem1', length=1, delay_cost=1)
	S += T611_mem1 >= 20
	T611_mem1 += INPUT_mem_r

	T0t3_a0b0_mem0 = S.Task('T0t3_a0b0_mem0', length=1, delay_cost=1)
	S += T0t3_a0b0_mem0 >= 21
	T0t3_a0b0_mem0 += INPUT_mem_r

	T0t3_a0b0_mem1 = S.Task('T0t3_a0b0_mem1', length=1, delay_cost=1)
	S += T0t3_a0b0_mem1 >= 21
	T0t3_a0b0_mem1 += INPUT_mem_r

	T611 = S.Task('T611', length=1, delay_cost=1)
	S += T611 >= 21
	T611 += ADD[1]

	T0t3_a0b0 = S.Task('T0t3_a0b0', length=1, delay_cost=1)
	S += T0t3_a0b0 >= 22
	T0t3_a0b0 += ADD[3]

	T5_101_mem0 = S.Task('T5_101_mem0', length=1, delay_cost=1)
	S += T5_101_mem0 >= 22
	T5_101_mem0 += INPUT_mem_r

	T5_101_mem1 = S.Task('T5_101_mem1', length=1, delay_cost=1)
	S += T5_101_mem1 >= 22
	T5_101_mem1 += INPUT_mem_r

	T2t2_a0b0_mem0 = S.Task('T2t2_a0b0_mem0', length=1, delay_cost=1)
	S += T2t2_a0b0_mem0 >= 23
	T2t2_a0b0_mem0 += INPUT_mem_r

	T2t2_a0b0_mem1 = S.Task('T2t2_a0b0_mem1', length=1, delay_cost=1)
	S += T2t2_a0b0_mem1 >= 23
	T2t2_a0b0_mem1 += INPUT_mem_r

	T5_101 = S.Task('T5_101', length=1, delay_cost=1)
	S += T5_101 >= 23
	T5_101 += ADD[1]

	T0t2_0_mem0 = S.Task('T0t2_0_mem0', length=1, delay_cost=1)
	S += T0t2_0_mem0 >= 24
	T0t2_0_mem0 += INPUT_mem_r

	T0t2_0_mem1 = S.Task('T0t2_0_mem1', length=1, delay_cost=1)
	S += T0t2_0_mem1 >= 24
	T0t2_0_mem1 += INPUT_mem_r

	T2t2_a0b0 = S.Task('T2t2_a0b0', length=1, delay_cost=1)
	S += T2t2_a0b0 >= 24
	T2t2_a0b0 += ADD[1]

	T0t2_0 = S.Task('T0t2_0', length=1, delay_cost=1)
	S += T0t2_0 >= 25
	T0t2_0 += ADD[2]

	T1t3_a0b0_mem0 = S.Task('T1t3_a0b0_mem0', length=1, delay_cost=1)
	S += T1t3_a0b0_mem0 >= 25
	T1t3_a0b0_mem0 += INPUT_mem_r

	T1t3_a0b0_mem1 = S.Task('T1t3_a0b0_mem1', length=1, delay_cost=1)
	S += T1t3_a0b0_mem1 >= 25
	T1t3_a0b0_mem1 += INPUT_mem_r

	T0t2_1_mem0 = S.Task('T0t2_1_mem0', length=1, delay_cost=1)
	S += T0t2_1_mem0 >= 26
	T0t2_1_mem0 += INPUT_mem_r

	T0t2_1_mem1 = S.Task('T0t2_1_mem1', length=1, delay_cost=1)
	S += T0t2_1_mem1 >= 26
	T0t2_1_mem1 += INPUT_mem_r

	T1t3_a0b0 = S.Task('T1t3_a0b0', length=1, delay_cost=1)
	S += T1t3_a0b0 >= 26
	T1t3_a0b0 += ADD[1]

	T0t2_1 = S.Task('T0t2_1', length=1, delay_cost=1)
	S += T0t2_1 >= 27
	T0t2_1 += ADD[0]

	T501_mem0 = S.Task('T501_mem0', length=1, delay_cost=1)
	S += T501_mem0 >= 27
	T501_mem0 += INPUT_mem_r

	T501_mem1 = S.Task('T501_mem1', length=1, delay_cost=1)
	S += T501_mem1 >= 27
	T501_mem1 += INPUT_mem_r

	T1t2_0_mem0 = S.Task('T1t2_0_mem0', length=1, delay_cost=1)
	S += T1t2_0_mem0 >= 28
	T1t2_0_mem0 += INPUT_mem_r

	T1t2_0_mem1 = S.Task('T1t2_0_mem1', length=1, delay_cost=1)
	S += T1t2_0_mem1 >= 28
	T1t2_0_mem1 += INPUT_mem_r

	T501 = S.Task('T501', length=1, delay_cost=1)
	S += T501 >= 28
	T501 += ADD[3]

	T1t2_0 = S.Task('T1t2_0', length=1, delay_cost=1)
	S += T1t2_0 >= 29
	T1t2_0 += ADD[1]

	T510_mem0 = S.Task('T510_mem0', length=1, delay_cost=1)
	S += T510_mem0 >= 29
	T510_mem0 += INPUT_mem_r

	T510_mem1 = S.Task('T510_mem1', length=1, delay_cost=1)
	S += T510_mem1 >= 29
	T510_mem1 += INPUT_mem_r

	T2t2_0_mem0 = S.Task('T2t2_0_mem0', length=1, delay_cost=1)
	S += T2t2_0_mem0 >= 30
	T2t2_0_mem0 += INPUT_mem_r

	T2t2_0_mem1 = S.Task('T2t2_0_mem1', length=1, delay_cost=1)
	S += T2t2_0_mem1 >= 30
	T2t2_0_mem1 += INPUT_mem_r

	T510 = S.Task('T510', length=1, delay_cost=1)
	S += T510 >= 30
	T510 += ADD[1]

	T2t2_0 = S.Task('T2t2_0', length=1, delay_cost=1)
	S += T2t2_0 >= 31
	T2t2_0 += ADD[3]

	T2t2_1_mem0 = S.Task('T2t2_1_mem0', length=1, delay_cost=1)
	S += T2t2_1_mem0 >= 31
	T2t2_1_mem0 += INPUT_mem_r

	T2t2_1_mem1 = S.Task('T2t2_1_mem1', length=1, delay_cost=1)
	S += T2t2_1_mem1 >= 31
	T2t2_1_mem1 += INPUT_mem_r

	T0t2_a0b0_mem0 = S.Task('T0t2_a0b0_mem0', length=1, delay_cost=1)
	S += T0t2_a0b0_mem0 >= 32
	T0t2_a0b0_mem0 += INPUT_mem_r

	T0t2_a0b0_mem1 = S.Task('T0t2_a0b0_mem1', length=1, delay_cost=1)
	S += T0t2_a0b0_mem1 >= 32
	T0t2_a0b0_mem1 += INPUT_mem_r

	T2t2_1 = S.Task('T2t2_1', length=1, delay_cost=1)
	S += T2t2_1 >= 32
	T2t2_1 += ADD[1]

	T0t2_a0b0 = S.Task('T0t2_a0b0', length=1, delay_cost=1)
	S += T0t2_a0b0 >= 33
	T0t2_a0b0 += ADD[2]

	T1t3_1_mem0 = S.Task('T1t3_1_mem0', length=1, delay_cost=1)
	S += T1t3_1_mem0 >= 33
	T1t3_1_mem0 += INPUT_mem_r

	T1t3_1_mem1 = S.Task('T1t3_1_mem1', length=1, delay_cost=1)
	S += T1t3_1_mem1 >= 33
	T1t3_1_mem1 += INPUT_mem_r

	T1t3_1 = S.Task('T1t3_1', length=1, delay_cost=1)
	S += T1t3_1 >= 34
	T1t3_1 += ADD[0]

	T4_111_mem0 = S.Task('T4_111_mem0', length=1, delay_cost=1)
	S += T4_111_mem0 >= 34
	T4_111_mem0 += INPUT_mem_r

	T4_111_mem1 = S.Task('T4_111_mem1', length=1, delay_cost=1)
	S += T4_111_mem1 >= 34
	T4_111_mem1 += INPUT_mem_r

	T310_mem0 = S.Task('T310_mem0', length=1, delay_cost=1)
	S += T310_mem0 >= 35
	T310_mem0 += INPUT_mem_r

	T310_mem1 = S.Task('T310_mem1', length=1, delay_cost=1)
	S += T310_mem1 >= 35
	T310_mem1 += INPUT_mem_r

	T4_111 = S.Task('T4_111', length=1, delay_cost=1)
	S += T4_111 >= 35
	T4_111 += ADD[2]

	T0t3_1_mem0 = S.Task('T0t3_1_mem0', length=1, delay_cost=1)
	S += T0t3_1_mem0 >= 36
	T0t3_1_mem0 += INPUT_mem_r

	T0t3_1_mem1 = S.Task('T0t3_1_mem1', length=1, delay_cost=1)
	S += T0t3_1_mem1 >= 36
	T0t3_1_mem1 += INPUT_mem_r

	T310 = S.Task('T310', length=1, delay_cost=1)
	S += T310 >= 36
	T310 += ADD[1]

	T0t3_1 = S.Task('T0t3_1', length=1, delay_cost=1)
	S += T0t3_1 >= 37
	T0t3_1 += ADD[1]

	T1t2_1_mem0 = S.Task('T1t2_1_mem0', length=1, delay_cost=1)
	S += T1t2_1_mem0 >= 37
	T1t2_1_mem0 += INPUT_mem_r

	T1t2_1_mem1 = S.Task('T1t2_1_mem1', length=1, delay_cost=1)
	S += T1t2_1_mem1 >= 37
	T1t2_1_mem1 += INPUT_mem_r

	T1t2_1 = S.Task('T1t2_1', length=1, delay_cost=1)
	S += T1t2_1 >= 38
	T1t2_1 += ADD[1]

	T2t3_0_mem0 = S.Task('T2t3_0_mem0', length=1, delay_cost=1)
	S += T2t3_0_mem0 >= 38
	T2t3_0_mem0 += INPUT_mem_r

	T2t3_0_mem1 = S.Task('T2t3_0_mem1', length=1, delay_cost=1)
	S += T2t3_0_mem1 >= 38
	T2t3_0_mem1 += INPUT_mem_r

	T2t3_0 = S.Task('T2t3_0', length=1, delay_cost=1)
	S += T2t3_0 >= 39
	T2t3_0 += ADD[0]

	T311_mem0 = S.Task('T311_mem0', length=1, delay_cost=1)
	S += T311_mem0 >= 39
	T311_mem0 += INPUT_mem_r

	T311_mem1 = S.Task('T311_mem1', length=1, delay_cost=1)
	S += T311_mem1 >= 39
	T311_mem1 += INPUT_mem_r

	T0t3_0_mem0 = S.Task('T0t3_0_mem0', length=1, delay_cost=1)
	S += T0t3_0_mem0 >= 40
	T0t3_0_mem0 += INPUT_mem_r

	T0t3_0_mem1 = S.Task('T0t3_0_mem1', length=1, delay_cost=1)
	S += T0t3_0_mem1 >= 40
	T0t3_0_mem1 += INPUT_mem_r

	T311 = S.Task('T311', length=1, delay_cost=1)
	S += T311 >= 40
	T311 += ADD[2]

	T0t3_0 = S.Task('T0t3_0', length=1, delay_cost=1)
	S += T0t3_0 >= 41
	T0t3_0 += ADD[3]

	T2t3_a1b1_mem0 = S.Task('T2t3_a1b1_mem0', length=1, delay_cost=1)
	S += T2t3_a1b1_mem0 >= 41
	T2t3_a1b1_mem0 += INPUT_mem_r

	T2t3_a1b1_mem1 = S.Task('T2t3_a1b1_mem1', length=1, delay_cost=1)
	S += T2t3_a1b1_mem1 >= 41
	T2t3_a1b1_mem1 += INPUT_mem_r

	T2t3_a1b1 = S.Task('T2t3_a1b1', length=1, delay_cost=1)
	S += T2t3_a1b1 >= 42
	T2t3_a1b1 += ADD[2]

	T600_mem0 = S.Task('T600_mem0', length=1, delay_cost=1)
	S += T600_mem0 >= 42
	T600_mem0 += INPUT_mem_r

	T600_mem1 = S.Task('T600_mem1', length=1, delay_cost=1)
	S += T600_mem1 >= 42
	T600_mem1 += INPUT_mem_r

	T411_mem0 = S.Task('T411_mem0', length=1, delay_cost=1)
	S += T411_mem0 >= 43
	T411_mem0 += INPUT_mem_r

	T411_mem1 = S.Task('T411_mem1', length=1, delay_cost=1)
	S += T411_mem1 >= 43
	T411_mem1 += INPUT_mem_r

	T600 = S.Task('T600', length=1, delay_cost=1)
	S += T600 >= 43
	T600 += ADD[1]

	T411 = S.Task('T411', length=1, delay_cost=1)
	S += T411 >= 44
	T411 += ADD[0]

	T5_110_mem0 = S.Task('T5_110_mem0', length=1, delay_cost=1)
	S += T5_110_mem0 >= 44
	T5_110_mem0 += INPUT_mem_r

	T5_110_mem1 = S.Task('T5_110_mem1', length=1, delay_cost=1)
	S += T5_110_mem1 >= 44
	T5_110_mem1 += INPUT_mem_r

	T400_mem0 = S.Task('T400_mem0', length=1, delay_cost=1)
	S += T400_mem0 >= 45
	T400_mem0 += INPUT_mem_r

	T400_mem1 = S.Task('T400_mem1', length=1, delay_cost=1)
	S += T400_mem1 >= 45
	T400_mem1 += INPUT_mem_r

	T5_110 = S.Task('T5_110', length=1, delay_cost=1)
	S += T5_110 >= 45
	T5_110 += ADD[2]

	T0t3_a1b1_mem0 = S.Task('T0t3_a1b1_mem0', length=1, delay_cost=1)
	S += T0t3_a1b1_mem0 >= 46
	T0t3_a1b1_mem0 += INPUT_mem_r

	T0t3_a1b1_mem1 = S.Task('T0t3_a1b1_mem1', length=1, delay_cost=1)
	S += T0t3_a1b1_mem1 >= 46
	T0t3_a1b1_mem1 += INPUT_mem_r

	T400 = S.Task('T400', length=1, delay_cost=1)
	S += T400 >= 46
	T400 += ADD[0]

	T0t3_a1b1 = S.Task('T0t3_a1b1', length=1, delay_cost=1)
	S += T0t3_a1b1 >= 47
	T0t3_a1b1 += ADD[3]

	T610_mem0 = S.Task('T610_mem0', length=1, delay_cost=1)
	S += T610_mem0 >= 47
	T610_mem0 += INPUT_mem_r

	T610_mem1 = S.Task('T610_mem1', length=1, delay_cost=1)
	S += T610_mem1 >= 47
	T610_mem1 += INPUT_mem_r

	T301_mem0 = S.Task('T301_mem0', length=1, delay_cost=1)
	S += T301_mem0 >= 48
	T301_mem0 += INPUT_mem_r

	T301_mem1 = S.Task('T301_mem1', length=1, delay_cost=1)
	S += T301_mem1 >= 48
	T301_mem1 += INPUT_mem_r

	T610 = S.Task('T610', length=1, delay_cost=1)
	S += T610 >= 48
	T610 += ADD[1]

	T1t2_a1b1_mem0 = S.Task('T1t2_a1b1_mem0', length=1, delay_cost=1)
	S += T1t2_a1b1_mem0 >= 49
	T1t2_a1b1_mem0 += INPUT_mem_r

	T1t2_a1b1_mem1 = S.Task('T1t2_a1b1_mem1', length=1, delay_cost=1)
	S += T1t2_a1b1_mem1 >= 49
	T1t2_a1b1_mem1 += INPUT_mem_r

	T301 = S.Task('T301', length=1, delay_cost=1)
	S += T301 >= 49
	T301 += ADD[0]

	T1t2_a1b1 = S.Task('T1t2_a1b1', length=1, delay_cost=1)
	S += T1t2_a1b1 >= 50
	T1t2_a1b1 += ADD[3]

	T2t3_a0b0_mem0 = S.Task('T2t3_a0b0_mem0', length=1, delay_cost=1)
	S += T2t3_a0b0_mem0 >= 50
	T2t3_a0b0_mem0 += INPUT_mem_r

	T2t3_a0b0_mem1 = S.Task('T2t3_a0b0_mem1', length=1, delay_cost=1)
	S += T2t3_a0b0_mem1 >= 50
	T2t3_a0b0_mem1 += INPUT_mem_r

	T2t2_a1b1_mem0 = S.Task('T2t2_a1b1_mem0', length=1, delay_cost=1)
	S += T2t2_a1b1_mem0 >= 51
	T2t2_a1b1_mem0 += INPUT_mem_r

	T2t2_a1b1_mem1 = S.Task('T2t2_a1b1_mem1', length=1, delay_cost=1)
	S += T2t2_a1b1_mem1 >= 51
	T2t2_a1b1_mem1 += INPUT_mem_r

	T2t3_a0b0 = S.Task('T2t3_a0b0', length=1, delay_cost=1)
	S += T2t3_a0b0 >= 51
	T2t3_a0b0 += ADD[0]

	T1t2_a0b0_mem0 = S.Task('T1t2_a0b0_mem0', length=1, delay_cost=1)
	S += T1t2_a0b0_mem0 >= 52
	T1t2_a0b0_mem0 += INPUT_mem_r

	T1t2_a0b0_mem1 = S.Task('T1t2_a0b0_mem1', length=1, delay_cost=1)
	S += T1t2_a0b0_mem1 >= 52
	T1t2_a0b0_mem1 += INPUT_mem_r

	T2t2_a1b1 = S.Task('T2t2_a1b1', length=1, delay_cost=1)
	S += T2t2_a1b1 >= 52
	T2t2_a1b1 += ADD[0]

	T1t2_a0b0 = S.Task('T1t2_a0b0', length=1, delay_cost=1)
	S += T1t2_a0b0 >= 53
	T1t2_a0b0 += ADD[0]

	T2t3_1_mem0 = S.Task('T2t3_1_mem0', length=1, delay_cost=1)
	S += T2t3_1_mem0 >= 53
	T2t3_1_mem0 += INPUT_mem_r

	T2t3_1_mem1 = S.Task('T2t3_1_mem1', length=1, delay_cost=1)
	S += T2t3_1_mem1 >= 53
	T2t3_1_mem1 += INPUT_mem_r

	T2t3_1 = S.Task('T2t3_1', length=1, delay_cost=1)
	S += T2t3_1 >= 54
	T2t3_1 += ADD[0]

	T4_101_mem0 = S.Task('T4_101_mem0', length=1, delay_cost=1)
	S += T4_101_mem0 >= 54
	T4_101_mem0 += INPUT_mem_r

	T4_101_mem1 = S.Task('T4_101_mem1', length=1, delay_cost=1)
	S += T4_101_mem1 >= 54
	T4_101_mem1 += INPUT_mem_r

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	S += T401_mem0 >= 55
	T401_mem0 += INPUT_mem_r

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	S += T401_mem1 >= 55
	T401_mem1 += INPUT_mem_r

	T4_101 = S.Task('T4_101', length=1, delay_cost=1)
	S += T4_101 >= 55
	T4_101 += ADD[0]

	T1t3_a1b1_mem0 = S.Task('T1t3_a1b1_mem0', length=1, delay_cost=1)
	S += T1t3_a1b1_mem0 >= 56
	T1t3_a1b1_mem0 += INPUT_mem_r

	T1t3_a1b1_mem1 = S.Task('T1t3_a1b1_mem1', length=1, delay_cost=1)
	S += T1t3_a1b1_mem1 >= 56
	T1t3_a1b1_mem1 += INPUT_mem_r

	T401 = S.Task('T401', length=1, delay_cost=1)
	S += T401 >= 56
	T401 += ADD[0]

	T1t3_0_mem0 = S.Task('T1t3_0_mem0', length=1, delay_cost=1)
	S += T1t3_0_mem0 >= 57
	T1t3_0_mem0 += INPUT_mem_r

	T1t3_0_mem1 = S.Task('T1t3_0_mem1', length=1, delay_cost=1)
	S += T1t3_0_mem1 >= 57
	T1t3_0_mem1 += INPUT_mem_r

	T1t3_a1b1 = S.Task('T1t3_a1b1', length=1, delay_cost=1)
	S += T1t3_a1b1 >= 57
	T1t3_a1b1 += ADD[0]

	T1t3_0 = S.Task('T1t3_0', length=1, delay_cost=1)
	S += T1t3_0 >= 58
	T1t3_0 += ADD[0]

	T5_100_mem0 = S.Task('T5_100_mem0', length=1, delay_cost=1)
	S += T5_100_mem0 >= 58
	T5_100_mem0 += INPUT_mem_r

	T5_100_mem1 = S.Task('T5_100_mem1', length=1, delay_cost=1)
	S += T5_100_mem1 >= 58
	T5_100_mem1 += INPUT_mem_r

	T0t2_a1b1_mem0 = S.Task('T0t2_a1b1_mem0', length=1, delay_cost=1)
	S += T0t2_a1b1_mem0 >= 59
	T0t2_a1b1_mem0 += INPUT_mem_r

	T0t2_a1b1_mem1 = S.Task('T0t2_a1b1_mem1', length=1, delay_cost=1)
	S += T0t2_a1b1_mem1 >= 59
	T0t2_a1b1_mem1 += INPUT_mem_r

	T5_100 = S.Task('T5_100', length=1, delay_cost=1)
	S += T5_100 >= 59
	T5_100 += ADD[0]

	T0t2_a1b1 = S.Task('T0t2_a1b1', length=1, delay_cost=1)
	S += T0t2_a1b1 >= 60
	T0t2_a1b1 += ADD[0]


	# new tasks
	T0_1t2_0 = S.Task('T0_1t2_0', length=1, delay_cost=1)
	T0_1t2_0 += alt(ADD)

	T0_1t2_0_mem0 = S.Task('T0_1t2_0_mem0', length=1, delay_cost=1)
	T0_1t2_0_mem0 += INPUT_mem_r
	S += T0_1t2_0_mem0<=T0_1t2_0

	T0_1t2_0_mem1 = S.Task('T0_1t2_0_mem1', length=1, delay_cost=1)
	T0_1t2_0_mem1 += INPUT_mem_r
	S += T0_1t2_0_mem1<=T0_1t2_0

	T0_1t2_1 = S.Task('T0_1t2_1', length=1, delay_cost=1)
	T0_1t2_1 += alt(ADD)

	T0_1t2_1_mem0 = S.Task('T0_1t2_1_mem0', length=1, delay_cost=1)
	T0_1t2_1_mem0 += INPUT_mem_r
	S += T0_1t2_1_mem0<=T0_1t2_1

	T0_1t2_1_mem1 = S.Task('T0_1t2_1_mem1', length=1, delay_cost=1)
	T0_1t2_1_mem1 += INPUT_mem_r
	S += T0_1t2_1_mem1<=T0_1t2_1

	T0_1t3_0 = S.Task('T0_1t3_0', length=1, delay_cost=1)
	T0_1t3_0 += alt(ADD)

	T0_1t3_0_mem0 = S.Task('T0_1t3_0_mem0', length=1, delay_cost=1)
	T0_1t3_0_mem0 += INPUT_mem_r
	S += T0_1t3_0_mem0<=T0_1t3_0

	T0_1t3_0_mem1 = S.Task('T0_1t3_0_mem1', length=1, delay_cost=1)
	T0_1t3_0_mem1 += INPUT_mem_r
	S += T0_1t3_0_mem1<=T0_1t3_0

	T0_1t3_1 = S.Task('T0_1t3_1', length=1, delay_cost=1)
	T0_1t3_1 += alt(ADD)

	T0_1t3_1_mem0 = S.Task('T0_1t3_1_mem0', length=1, delay_cost=1)
	T0_1t3_1_mem0 += INPUT_mem_r
	S += T0_1t3_1_mem0<=T0_1t3_1

	T0_1t3_1_mem1 = S.Task('T0_1t3_1_mem1', length=1, delay_cost=1)
	T0_1t3_1_mem1 += INPUT_mem_r
	S += T0_1t3_1_mem1<=T0_1t3_1

	T0_1t0_a0b0_in = S.Task('T0_1t0_a0b0_in', length=1, delay_cost=1)
	T0_1t0_a0b0_in += alt(MUL_in)
	T0_1t0_a0b0 = S.Task('T0_1t0_a0b0', length=7, delay_cost=1)
	T0_1t0_a0b0 += alt(MUL)
	S+=T0_1t0_a0b0>=T0_1t0_a0b0_in

	T0_1t0_a0b0_mem0 = S.Task('T0_1t0_a0b0_mem0', length=1, delay_cost=1)
	T0_1t0_a0b0_mem0 += INPUT_mem_r
	S += T0_1t0_a0b0_mem0<=T0_1t0_a0b0

	T0_1t0_a0b0_mem1 = S.Task('T0_1t0_a0b0_mem1', length=1, delay_cost=1)
	T0_1t0_a0b0_mem1 += INPUT_mem_r
	S += T0_1t0_a0b0_mem1<=T0_1t0_a0b0

	T0_1t1_a0b0_in = S.Task('T0_1t1_a0b0_in', length=1, delay_cost=1)
	T0_1t1_a0b0_in += alt(MUL_in)
	T0_1t1_a0b0 = S.Task('T0_1t1_a0b0', length=7, delay_cost=1)
	T0_1t1_a0b0 += alt(MUL)
	S+=T0_1t1_a0b0>=T0_1t1_a0b0_in

	T0_1t1_a0b0_mem0 = S.Task('T0_1t1_a0b0_mem0', length=1, delay_cost=1)
	T0_1t1_a0b0_mem0 += INPUT_mem_r
	S += T0_1t1_a0b0_mem0<=T0_1t1_a0b0

	T0_1t1_a0b0_mem1 = S.Task('T0_1t1_a0b0_mem1', length=1, delay_cost=1)
	T0_1t1_a0b0_mem1 += INPUT_mem_r
	S += T0_1t1_a0b0_mem1<=T0_1t1_a0b0

	T0_1t2_a0b0 = S.Task('T0_1t2_a0b0', length=1, delay_cost=1)
	T0_1t2_a0b0 += alt(ADD)

	T0_1t2_a0b0_mem0 = S.Task('T0_1t2_a0b0_mem0', length=1, delay_cost=1)
	T0_1t2_a0b0_mem0 += INPUT_mem_r
	S += T0_1t2_a0b0_mem0<=T0_1t2_a0b0

	T0_1t2_a0b0_mem1 = S.Task('T0_1t2_a0b0_mem1', length=1, delay_cost=1)
	T0_1t2_a0b0_mem1 += INPUT_mem_r
	S += T0_1t2_a0b0_mem1<=T0_1t2_a0b0

	T0_1t3_a0b0 = S.Task('T0_1t3_a0b0', length=1, delay_cost=1)
	T0_1t3_a0b0 += alt(ADD)

	T0_1t3_a0b0_mem0 = S.Task('T0_1t3_a0b0_mem0', length=1, delay_cost=1)
	T0_1t3_a0b0_mem0 += INPUT_mem_r
	S += T0_1t3_a0b0_mem0<=T0_1t3_a0b0

	T0_1t3_a0b0_mem1 = S.Task('T0_1t3_a0b0_mem1', length=1, delay_cost=1)
	T0_1t3_a0b0_mem1 += INPUT_mem_r
	S += T0_1t3_a0b0_mem1<=T0_1t3_a0b0

	T0_1t0_a1b1_in = S.Task('T0_1t0_a1b1_in', length=1, delay_cost=1)
	T0_1t0_a1b1_in += alt(MUL_in)
	T0_1t0_a1b1 = S.Task('T0_1t0_a1b1', length=7, delay_cost=1)
	T0_1t0_a1b1 += alt(MUL)
	S+=T0_1t0_a1b1>=T0_1t0_a1b1_in

	T0_1t0_a1b1_mem0 = S.Task('T0_1t0_a1b1_mem0', length=1, delay_cost=1)
	T0_1t0_a1b1_mem0 += INPUT_mem_r
	S += T0_1t0_a1b1_mem0<=T0_1t0_a1b1

	T0_1t0_a1b1_mem1 = S.Task('T0_1t0_a1b1_mem1', length=1, delay_cost=1)
	T0_1t0_a1b1_mem1 += INPUT_mem_r
	S += T0_1t0_a1b1_mem1<=T0_1t0_a1b1

	T0_1t1_a1b1_in = S.Task('T0_1t1_a1b1_in', length=1, delay_cost=1)
	T0_1t1_a1b1_in += alt(MUL_in)
	T0_1t1_a1b1 = S.Task('T0_1t1_a1b1', length=7, delay_cost=1)
	T0_1t1_a1b1 += alt(MUL)
	S+=T0_1t1_a1b1>=T0_1t1_a1b1_in

	T0_1t1_a1b1_mem0 = S.Task('T0_1t1_a1b1_mem0', length=1, delay_cost=1)
	T0_1t1_a1b1_mem0 += INPUT_mem_r
	S += T0_1t1_a1b1_mem0<=T0_1t1_a1b1

	T0_1t1_a1b1_mem1 = S.Task('T0_1t1_a1b1_mem1', length=1, delay_cost=1)
	T0_1t1_a1b1_mem1 += INPUT_mem_r
	S += T0_1t1_a1b1_mem1<=T0_1t1_a1b1

	T0_1t2_a1b1 = S.Task('T0_1t2_a1b1', length=1, delay_cost=1)
	T0_1t2_a1b1 += alt(ADD)

	T0_1t2_a1b1_mem0 = S.Task('T0_1t2_a1b1_mem0', length=1, delay_cost=1)
	T0_1t2_a1b1_mem0 += INPUT_mem_r
	S += T0_1t2_a1b1_mem0<=T0_1t2_a1b1

	T0_1t2_a1b1_mem1 = S.Task('T0_1t2_a1b1_mem1', length=1, delay_cost=1)
	T0_1t2_a1b1_mem1 += INPUT_mem_r
	S += T0_1t2_a1b1_mem1<=T0_1t2_a1b1

	T0_1t3_a1b1 = S.Task('T0_1t3_a1b1', length=1, delay_cost=1)
	T0_1t3_a1b1 += alt(ADD)

	T0_1t3_a1b1_mem0 = S.Task('T0_1t3_a1b1_mem0', length=1, delay_cost=1)
	T0_1t3_a1b1_mem0 += INPUT_mem_r
	S += T0_1t3_a1b1_mem0<=T0_1t3_a1b1

	T0_1t3_a1b1_mem1 = S.Task('T0_1t3_a1b1_mem1', length=1, delay_cost=1)
	T0_1t3_a1b1_mem1 += INPUT_mem_r
	S += T0_1t3_a1b1_mem1<=T0_1t3_a1b1

	T1_1t2_0 = S.Task('T1_1t2_0', length=1, delay_cost=1)
	T1_1t2_0 += alt(ADD)

	T1_1t2_0_mem0 = S.Task('T1_1t2_0_mem0', length=1, delay_cost=1)
	T1_1t2_0_mem0 += INPUT_mem_r
	S += T1_1t2_0_mem0<=T1_1t2_0

	T1_1t2_0_mem1 = S.Task('T1_1t2_0_mem1', length=1, delay_cost=1)
	T1_1t2_0_mem1 += INPUT_mem_r
	S += T1_1t2_0_mem1<=T1_1t2_0

	T1_1t2_1 = S.Task('T1_1t2_1', length=1, delay_cost=1)
	T1_1t2_1 += alt(ADD)

	T1_1t2_1_mem0 = S.Task('T1_1t2_1_mem0', length=1, delay_cost=1)
	T1_1t2_1_mem0 += INPUT_mem_r
	S += T1_1t2_1_mem0<=T1_1t2_1

	T1_1t2_1_mem1 = S.Task('T1_1t2_1_mem1', length=1, delay_cost=1)
	T1_1t2_1_mem1 += INPUT_mem_r
	S += T1_1t2_1_mem1<=T1_1t2_1

	T1_1t3_0 = S.Task('T1_1t3_0', length=1, delay_cost=1)
	T1_1t3_0 += alt(ADD)

	T1_1t3_0_mem0 = S.Task('T1_1t3_0_mem0', length=1, delay_cost=1)
	T1_1t3_0_mem0 += INPUT_mem_r
	S += T1_1t3_0_mem0<=T1_1t3_0

	T1_1t3_0_mem1 = S.Task('T1_1t3_0_mem1', length=1, delay_cost=1)
	T1_1t3_0_mem1 += INPUT_mem_r
	S += T1_1t3_0_mem1<=T1_1t3_0

	T1_1t3_1 = S.Task('T1_1t3_1', length=1, delay_cost=1)
	T1_1t3_1 += alt(ADD)

	T1_1t3_1_mem0 = S.Task('T1_1t3_1_mem0', length=1, delay_cost=1)
	T1_1t3_1_mem0 += INPUT_mem_r
	S += T1_1t3_1_mem0<=T1_1t3_1

	T1_1t3_1_mem1 = S.Task('T1_1t3_1_mem1', length=1, delay_cost=1)
	T1_1t3_1_mem1 += INPUT_mem_r
	S += T1_1t3_1_mem1<=T1_1t3_1

	T1_1t0_a0b0_in = S.Task('T1_1t0_a0b0_in', length=1, delay_cost=1)
	T1_1t0_a0b0_in += alt(MUL_in)
	T1_1t0_a0b0 = S.Task('T1_1t0_a0b0', length=7, delay_cost=1)
	T1_1t0_a0b0 += alt(MUL)
	S+=T1_1t0_a0b0>=T1_1t0_a0b0_in

	T1_1t0_a0b0_mem0 = S.Task('T1_1t0_a0b0_mem0', length=1, delay_cost=1)
	T1_1t0_a0b0_mem0 += INPUT_mem_r
	S += T1_1t0_a0b0_mem0<=T1_1t0_a0b0

	T1_1t0_a0b0_mem1 = S.Task('T1_1t0_a0b0_mem1', length=1, delay_cost=1)
	T1_1t0_a0b0_mem1 += INPUT_mem_r
	S += T1_1t0_a0b0_mem1<=T1_1t0_a0b0

	T1_1t1_a0b0_in = S.Task('T1_1t1_a0b0_in', length=1, delay_cost=1)
	T1_1t1_a0b0_in += alt(MUL_in)
	T1_1t1_a0b0 = S.Task('T1_1t1_a0b0', length=7, delay_cost=1)
	T1_1t1_a0b0 += alt(MUL)
	S+=T1_1t1_a0b0>=T1_1t1_a0b0_in

	T1_1t1_a0b0_mem0 = S.Task('T1_1t1_a0b0_mem0', length=1, delay_cost=1)
	T1_1t1_a0b0_mem0 += INPUT_mem_r
	S += T1_1t1_a0b0_mem0<=T1_1t1_a0b0

	T1_1t1_a0b0_mem1 = S.Task('T1_1t1_a0b0_mem1', length=1, delay_cost=1)
	T1_1t1_a0b0_mem1 += INPUT_mem_r
	S += T1_1t1_a0b0_mem1<=T1_1t1_a0b0

	T1_1t2_a0b0 = S.Task('T1_1t2_a0b0', length=1, delay_cost=1)
	T1_1t2_a0b0 += alt(ADD)

	T1_1t2_a0b0_mem0 = S.Task('T1_1t2_a0b0_mem0', length=1, delay_cost=1)
	T1_1t2_a0b0_mem0 += INPUT_mem_r
	S += T1_1t2_a0b0_mem0<=T1_1t2_a0b0

	T1_1t2_a0b0_mem1 = S.Task('T1_1t2_a0b0_mem1', length=1, delay_cost=1)
	T1_1t2_a0b0_mem1 += INPUT_mem_r
	S += T1_1t2_a0b0_mem1<=T1_1t2_a0b0

	T1_1t3_a0b0 = S.Task('T1_1t3_a0b0', length=1, delay_cost=1)
	T1_1t3_a0b0 += alt(ADD)

	T1_1t3_a0b0_mem0 = S.Task('T1_1t3_a0b0_mem0', length=1, delay_cost=1)
	T1_1t3_a0b0_mem0 += INPUT_mem_r
	S += T1_1t3_a0b0_mem0<=T1_1t3_a0b0

	T1_1t3_a0b0_mem1 = S.Task('T1_1t3_a0b0_mem1', length=1, delay_cost=1)
	T1_1t3_a0b0_mem1 += INPUT_mem_r
	S += T1_1t3_a0b0_mem1<=T1_1t3_a0b0

	T1_1t0_a1b1_in = S.Task('T1_1t0_a1b1_in', length=1, delay_cost=1)
	T1_1t0_a1b1_in += alt(MUL_in)
	T1_1t0_a1b1 = S.Task('T1_1t0_a1b1', length=7, delay_cost=1)
	T1_1t0_a1b1 += alt(MUL)
	S+=T1_1t0_a1b1>=T1_1t0_a1b1_in

	T1_1t0_a1b1_mem0 = S.Task('T1_1t0_a1b1_mem0', length=1, delay_cost=1)
	T1_1t0_a1b1_mem0 += INPUT_mem_r
	S += T1_1t0_a1b1_mem0<=T1_1t0_a1b1

	T1_1t0_a1b1_mem1 = S.Task('T1_1t0_a1b1_mem1', length=1, delay_cost=1)
	T1_1t0_a1b1_mem1 += INPUT_mem_r
	S += T1_1t0_a1b1_mem1<=T1_1t0_a1b1

	T1_1t1_a1b1_in = S.Task('T1_1t1_a1b1_in', length=1, delay_cost=1)
	T1_1t1_a1b1_in += alt(MUL_in)
	T1_1t1_a1b1 = S.Task('T1_1t1_a1b1', length=7, delay_cost=1)
	T1_1t1_a1b1 += alt(MUL)
	S+=T1_1t1_a1b1>=T1_1t1_a1b1_in

	T1_1t1_a1b1_mem0 = S.Task('T1_1t1_a1b1_mem0', length=1, delay_cost=1)
	T1_1t1_a1b1_mem0 += INPUT_mem_r
	S += T1_1t1_a1b1_mem0<=T1_1t1_a1b1

	T1_1t1_a1b1_mem1 = S.Task('T1_1t1_a1b1_mem1', length=1, delay_cost=1)
	T1_1t1_a1b1_mem1 += INPUT_mem_r
	S += T1_1t1_a1b1_mem1<=T1_1t1_a1b1

	T1_1t2_a1b1 = S.Task('T1_1t2_a1b1', length=1, delay_cost=1)
	T1_1t2_a1b1 += alt(ADD)

	T1_1t2_a1b1_mem0 = S.Task('T1_1t2_a1b1_mem0', length=1, delay_cost=1)
	T1_1t2_a1b1_mem0 += INPUT_mem_r
	S += T1_1t2_a1b1_mem0<=T1_1t2_a1b1

	T1_1t2_a1b1_mem1 = S.Task('T1_1t2_a1b1_mem1', length=1, delay_cost=1)
	T1_1t2_a1b1_mem1 += INPUT_mem_r
	S += T1_1t2_a1b1_mem1<=T1_1t2_a1b1

	T1_1t3_a1b1 = S.Task('T1_1t3_a1b1', length=1, delay_cost=1)
	T1_1t3_a1b1 += alt(ADD)

	T1_1t3_a1b1_mem0 = S.Task('T1_1t3_a1b1_mem0', length=1, delay_cost=1)
	T1_1t3_a1b1_mem0 += INPUT_mem_r
	S += T1_1t3_a1b1_mem0<=T1_1t3_a1b1

	T1_1t3_a1b1_mem1 = S.Task('T1_1t3_a1b1_mem1', length=1, delay_cost=1)
	T1_1t3_a1b1_mem1 += INPUT_mem_r
	S += T1_1t3_a1b1_mem1<=T1_1t3_a1b1

	T2_2t2_0 = S.Task('T2_2t2_0', length=1, delay_cost=1)
	T2_2t2_0 += alt(ADD)

	T2_2t2_0_mem0 = S.Task('T2_2t2_0_mem0', length=1, delay_cost=1)
	T2_2t2_0_mem0 += INPUT_mem_r
	S += T2_2t2_0_mem0<=T2_2t2_0

	T2_2t2_0_mem1 = S.Task('T2_2t2_0_mem1', length=1, delay_cost=1)
	T2_2t2_0_mem1 += INPUT_mem_r
	S += T2_2t2_0_mem1<=T2_2t2_0

	T2_2t2_1 = S.Task('T2_2t2_1', length=1, delay_cost=1)
	T2_2t2_1 += alt(ADD)

	T2_2t2_1_mem0 = S.Task('T2_2t2_1_mem0', length=1, delay_cost=1)
	T2_2t2_1_mem0 += INPUT_mem_r
	S += T2_2t2_1_mem0<=T2_2t2_1

	T2_2t2_1_mem1 = S.Task('T2_2t2_1_mem1', length=1, delay_cost=1)
	T2_2t2_1_mem1 += INPUT_mem_r
	S += T2_2t2_1_mem1<=T2_2t2_1

	T2_2t3_0 = S.Task('T2_2t3_0', length=1, delay_cost=1)
	T2_2t3_0 += alt(ADD)

	T2_2t3_0_mem0 = S.Task('T2_2t3_0_mem0', length=1, delay_cost=1)
	T2_2t3_0_mem0 += INPUT_mem_r
	S += T2_2t3_0_mem0<=T2_2t3_0

	T2_2t3_0_mem1 = S.Task('T2_2t3_0_mem1', length=1, delay_cost=1)
	T2_2t3_0_mem1 += INPUT_mem_r
	S += T2_2t3_0_mem1<=T2_2t3_0

	T2_2t3_1 = S.Task('T2_2t3_1', length=1, delay_cost=1)
	T2_2t3_1 += alt(ADD)

	T2_2t3_1_mem0 = S.Task('T2_2t3_1_mem0', length=1, delay_cost=1)
	T2_2t3_1_mem0 += INPUT_mem_r
	S += T2_2t3_1_mem0<=T2_2t3_1

	T2_2t3_1_mem1 = S.Task('T2_2t3_1_mem1', length=1, delay_cost=1)
	T2_2t3_1_mem1 += INPUT_mem_r
	S += T2_2t3_1_mem1<=T2_2t3_1

	T2_2t0_a0b0_in = S.Task('T2_2t0_a0b0_in', length=1, delay_cost=1)
	T2_2t0_a0b0_in += alt(MUL_in)
	T2_2t0_a0b0 = S.Task('T2_2t0_a0b0', length=7, delay_cost=1)
	T2_2t0_a0b0 += alt(MUL)
	S+=T2_2t0_a0b0>=T2_2t0_a0b0_in

	T2_2t0_a0b0_mem0 = S.Task('T2_2t0_a0b0_mem0', length=1, delay_cost=1)
	T2_2t0_a0b0_mem0 += INPUT_mem_r
	S += T2_2t0_a0b0_mem0<=T2_2t0_a0b0

	T2_2t0_a0b0_mem1 = S.Task('T2_2t0_a0b0_mem1', length=1, delay_cost=1)
	T2_2t0_a0b0_mem1 += INPUT_mem_r
	S += T2_2t0_a0b0_mem1<=T2_2t0_a0b0

	T2_2t1_a0b0_in = S.Task('T2_2t1_a0b0_in', length=1, delay_cost=1)
	T2_2t1_a0b0_in += alt(MUL_in)
	T2_2t1_a0b0 = S.Task('T2_2t1_a0b0', length=7, delay_cost=1)
	T2_2t1_a0b0 += alt(MUL)
	S+=T2_2t1_a0b0>=T2_2t1_a0b0_in

	T2_2t1_a0b0_mem0 = S.Task('T2_2t1_a0b0_mem0', length=1, delay_cost=1)
	T2_2t1_a0b0_mem0 += INPUT_mem_r
	S += T2_2t1_a0b0_mem0<=T2_2t1_a0b0

	T2_2t1_a0b0_mem1 = S.Task('T2_2t1_a0b0_mem1', length=1, delay_cost=1)
	T2_2t1_a0b0_mem1 += INPUT_mem_r
	S += T2_2t1_a0b0_mem1<=T2_2t1_a0b0

	T2_2t2_a0b0 = S.Task('T2_2t2_a0b0', length=1, delay_cost=1)
	T2_2t2_a0b0 += alt(ADD)

	T2_2t2_a0b0_mem0 = S.Task('T2_2t2_a0b0_mem0', length=1, delay_cost=1)
	T2_2t2_a0b0_mem0 += INPUT_mem_r
	S += T2_2t2_a0b0_mem0<=T2_2t2_a0b0

	T2_2t2_a0b0_mem1 = S.Task('T2_2t2_a0b0_mem1', length=1, delay_cost=1)
	T2_2t2_a0b0_mem1 += INPUT_mem_r
	S += T2_2t2_a0b0_mem1<=T2_2t2_a0b0

	T2_2t3_a0b0 = S.Task('T2_2t3_a0b0', length=1, delay_cost=1)
	T2_2t3_a0b0 += alt(ADD)

	T2_2t3_a0b0_mem0 = S.Task('T2_2t3_a0b0_mem0', length=1, delay_cost=1)
	T2_2t3_a0b0_mem0 += INPUT_mem_r
	S += T2_2t3_a0b0_mem0<=T2_2t3_a0b0

	T2_2t3_a0b0_mem1 = S.Task('T2_2t3_a0b0_mem1', length=1, delay_cost=1)
	T2_2t3_a0b0_mem1 += INPUT_mem_r
	S += T2_2t3_a0b0_mem1<=T2_2t3_a0b0

	T2_2t0_a1b1_in = S.Task('T2_2t0_a1b1_in', length=1, delay_cost=1)
	T2_2t0_a1b1_in += alt(MUL_in)
	T2_2t0_a1b1 = S.Task('T2_2t0_a1b1', length=7, delay_cost=1)
	T2_2t0_a1b1 += alt(MUL)
	S+=T2_2t0_a1b1>=T2_2t0_a1b1_in

	T2_2t0_a1b1_mem0 = S.Task('T2_2t0_a1b1_mem0', length=1, delay_cost=1)
	T2_2t0_a1b1_mem0 += INPUT_mem_r
	S += T2_2t0_a1b1_mem0<=T2_2t0_a1b1

	T2_2t0_a1b1_mem1 = S.Task('T2_2t0_a1b1_mem1', length=1, delay_cost=1)
	T2_2t0_a1b1_mem1 += INPUT_mem_r
	S += T2_2t0_a1b1_mem1<=T2_2t0_a1b1

	T2_2t1_a1b1_in = S.Task('T2_2t1_a1b1_in', length=1, delay_cost=1)
	T2_2t1_a1b1_in += alt(MUL_in)
	T2_2t1_a1b1 = S.Task('T2_2t1_a1b1', length=7, delay_cost=1)
	T2_2t1_a1b1 += alt(MUL)
	S+=T2_2t1_a1b1>=T2_2t1_a1b1_in

	T2_2t1_a1b1_mem0 = S.Task('T2_2t1_a1b1_mem0', length=1, delay_cost=1)
	T2_2t1_a1b1_mem0 += INPUT_mem_r
	S += T2_2t1_a1b1_mem0<=T2_2t1_a1b1

	T2_2t1_a1b1_mem1 = S.Task('T2_2t1_a1b1_mem1', length=1, delay_cost=1)
	T2_2t1_a1b1_mem1 += INPUT_mem_r
	S += T2_2t1_a1b1_mem1<=T2_2t1_a1b1

	T2_2t2_a1b1 = S.Task('T2_2t2_a1b1', length=1, delay_cost=1)
	T2_2t2_a1b1 += alt(ADD)

	T2_2t2_a1b1_mem0 = S.Task('T2_2t2_a1b1_mem0', length=1, delay_cost=1)
	T2_2t2_a1b1_mem0 += INPUT_mem_r
	S += T2_2t2_a1b1_mem0<=T2_2t2_a1b1

	T2_2t2_a1b1_mem1 = S.Task('T2_2t2_a1b1_mem1', length=1, delay_cost=1)
	T2_2t2_a1b1_mem1 += INPUT_mem_r
	S += T2_2t2_a1b1_mem1<=T2_2t2_a1b1

	T2_2t3_a1b1 = S.Task('T2_2t3_a1b1', length=1, delay_cost=1)
	T2_2t3_a1b1 += alt(ADD)

	T2_2t3_a1b1_mem0 = S.Task('T2_2t3_a1b1_mem0', length=1, delay_cost=1)
	T2_2t3_a1b1_mem0 += INPUT_mem_r
	S += T2_2t3_a1b1_mem0<=T2_2t3_a1b1

	T2_2t3_a1b1_mem1 = S.Task('T2_2t3_a1b1_mem1', length=1, delay_cost=1)
	T2_2t3_a1b1_mem1 += INPUT_mem_r
	S += T2_2t3_a1b1_mem1<=T2_2t3_a1b1

	T3_400 = S.Task('T3_400', length=1, delay_cost=1)
	T3_400 += alt(ADD)

	T3_400_mem0 = S.Task('T3_400_mem0', length=1, delay_cost=1)
	T3_400_mem0 += INPUT_mem_r
	S += T3_400_mem0<=T3_400

	T3_400_mem1 = S.Task('T3_400_mem1', length=1, delay_cost=1)
	T3_400_mem1 += INPUT_mem_r
	S += T3_400_mem1<=T3_400

	T3_401 = S.Task('T3_401', length=1, delay_cost=1)
	T3_401 += alt(ADD)

	T3_401_mem0 = S.Task('T3_401_mem0', length=1, delay_cost=1)
	T3_401_mem0 += INPUT_mem_r
	S += T3_401_mem0<=T3_401

	T3_401_mem1 = S.Task('T3_401_mem1', length=1, delay_cost=1)
	T3_401_mem1 += INPUT_mem_r
	S += T3_401_mem1<=T3_401

	T3_410 = S.Task('T3_410', length=1, delay_cost=1)
	T3_410 += alt(ADD)

	T3_410_mem0 = S.Task('T3_410_mem0', length=1, delay_cost=1)
	T3_410_mem0 += INPUT_mem_r
	S += T3_410_mem0<=T3_410

	T3_410_mem1 = S.Task('T3_410_mem1', length=1, delay_cost=1)
	T3_410_mem1 += INPUT_mem_r
	S += T3_410_mem1<=T3_410

	T3_411 = S.Task('T3_411', length=1, delay_cost=1)
	T3_411 += alt(ADD)

	T3_411_mem0 = S.Task('T3_411_mem0', length=1, delay_cost=1)
	T3_411_mem0 += INPUT_mem_r
	S += T3_411_mem0<=T3_411

	T3_411_mem1 = S.Task('T3_411_mem1', length=1, delay_cost=1)
	T3_411_mem1 += INPUT_mem_r
	S += T3_411_mem1<=T3_411

	T4_600 = S.Task('T4_600', length=1, delay_cost=1)
	T4_600 += alt(ADD)

	T4_600_mem0 = S.Task('T4_600_mem0', length=1, delay_cost=1)
	T4_600_mem0 += INPUT_mem_r
	S += T4_600_mem0<=T4_600

	T4_600_mem1 = S.Task('T4_600_mem1', length=1, delay_cost=1)
	T4_600_mem1 += INPUT_mem_r
	S += T4_600_mem1<=T4_600

	T4_601 = S.Task('T4_601', length=1, delay_cost=1)
	T4_601 += alt(ADD)

	T4_601_mem0 = S.Task('T4_601_mem0', length=1, delay_cost=1)
	T4_601_mem0 += INPUT_mem_r
	S += T4_601_mem0<=T4_601

	T4_601_mem1 = S.Task('T4_601_mem1', length=1, delay_cost=1)
	T4_601_mem1 += INPUT_mem_r
	S += T4_601_mem1<=T4_601

	T4_610 = S.Task('T4_610', length=1, delay_cost=1)
	T4_610 += alt(ADD)

	T4_610_mem0 = S.Task('T4_610_mem0', length=1, delay_cost=1)
	T4_610_mem0 += INPUT_mem_r
	S += T4_610_mem0<=T4_610

	T4_610_mem1 = S.Task('T4_610_mem1', length=1, delay_cost=1)
	T4_610_mem1 += INPUT_mem_r
	S += T4_610_mem1<=T4_610

	T4_611 = S.Task('T4_611', length=1, delay_cost=1)
	T4_611 += alt(ADD)

	T4_611_mem0 = S.Task('T4_611_mem0', length=1, delay_cost=1)
	T4_611_mem0 += INPUT_mem_r
	S += T4_611_mem0<=T4_611

	T4_611_mem1 = S.Task('T4_611_mem1', length=1, delay_cost=1)
	T4_611_mem1 += INPUT_mem_r
	S += T4_611_mem1<=T4_611

	T4_700 = S.Task('T4_700', length=1, delay_cost=1)
	T4_700 += alt(ADD)

	T4_700_mem0 = S.Task('T4_700_mem0', length=1, delay_cost=1)
	T4_700_mem0 += INPUT_mem_r
	S += T4_700_mem0<=T4_700

	T4_700_mem1 = S.Task('T4_700_mem1', length=1, delay_cost=1)
	T4_700_mem1 += INPUT_mem_r
	S += T4_700_mem1<=T4_700

	T4_701 = S.Task('T4_701', length=1, delay_cost=1)
	T4_701 += alt(ADD)

	T4_701_mem0 = S.Task('T4_701_mem0', length=1, delay_cost=1)
	T4_701_mem0 += INPUT_mem_r
	S += T4_701_mem0<=T4_701

	T4_701_mem1 = S.Task('T4_701_mem1', length=1, delay_cost=1)
	T4_701_mem1 += INPUT_mem_r
	S += T4_701_mem1<=T4_701

	T4_710 = S.Task('T4_710', length=1, delay_cost=1)
	T4_710 += alt(ADD)

	T4_710_mem0 = S.Task('T4_710_mem0', length=1, delay_cost=1)
	T4_710_mem0 += INPUT_mem_r
	S += T4_710_mem0<=T4_710

	T4_710_mem1 = S.Task('T4_710_mem1', length=1, delay_cost=1)
	T4_710_mem1 += INPUT_mem_r
	S += T4_710_mem1<=T4_710

	T4_711 = S.Task('T4_711', length=1, delay_cost=1)
	T4_711 += alt(ADD)

	T4_711_mem0 = S.Task('T4_711_mem0', length=1, delay_cost=1)
	T4_711_mem0 += INPUT_mem_r
	S += T4_711_mem0<=T4_711

	T4_711_mem1 = S.Task('T4_711_mem1', length=1, delay_cost=1)
	T4_711_mem1 += INPUT_mem_r
	S += T4_711_mem1<=T4_711

	T5_500 = S.Task('T5_500', length=1, delay_cost=1)
	T5_500 += alt(ADD)

	T5_500_mem0 = S.Task('T5_500_mem0', length=1, delay_cost=1)
	T5_500_mem0 += INPUT_mem_r
	S += T5_500_mem0<=T5_500

	T5_500_mem1 = S.Task('T5_500_mem1', length=1, delay_cost=1)
	T5_500_mem1 += INPUT_mem_r
	S += T5_500_mem1<=T5_500

	T5_501 = S.Task('T5_501', length=1, delay_cost=1)
	T5_501 += alt(ADD)

	T5_501_mem0 = S.Task('T5_501_mem0', length=1, delay_cost=1)
	T5_501_mem0 += INPUT_mem_r
	S += T5_501_mem0<=T5_501

	T5_501_mem1 = S.Task('T5_501_mem1', length=1, delay_cost=1)
	T5_501_mem1 += INPUT_mem_r
	S += T5_501_mem1<=T5_501

	T5_510 = S.Task('T5_510', length=1, delay_cost=1)
	T5_510 += alt(ADD)

	T5_510_mem0 = S.Task('T5_510_mem0', length=1, delay_cost=1)
	T5_510_mem0 += INPUT_mem_r
	S += T5_510_mem0<=T5_510

	T5_510_mem1 = S.Task('T5_510_mem1', length=1, delay_cost=1)
	T5_510_mem1 += INPUT_mem_r
	S += T5_510_mem1<=T5_510

	T5_511 = S.Task('T5_511', length=1, delay_cost=1)
	T5_511 += alt(ADD)

	T5_511_mem0 = S.Task('T5_511_mem0', length=1, delay_cost=1)
	T5_511_mem0 += INPUT_mem_r
	S += T5_511_mem0<=T5_511

	T5_511_mem1 = S.Task('T5_511_mem1', length=1, delay_cost=1)
	T5_511_mem1 += INPUT_mem_r
	S += T5_511_mem1<=T5_511

	T5_600 = S.Task('T5_600', length=1, delay_cost=1)
	T5_600 += alt(ADD)

	T5_600_mem0 = S.Task('T5_600_mem0', length=1, delay_cost=1)
	T5_600_mem0 += INPUT_mem_r
	S += T5_600_mem0<=T5_600

	T5_600_mem1 = S.Task('T5_600_mem1', length=1, delay_cost=1)
	T5_600_mem1 += INPUT_mem_r
	S += T5_600_mem1<=T5_600

	T5_601 = S.Task('T5_601', length=1, delay_cost=1)
	T5_601 += alt(ADD)

	T5_601_mem0 = S.Task('T5_601_mem0', length=1, delay_cost=1)
	T5_601_mem0 += INPUT_mem_r
	S += T5_601_mem0<=T5_601

	T5_601_mem1 = S.Task('T5_601_mem1', length=1, delay_cost=1)
	T5_601_mem1 += INPUT_mem_r
	S += T5_601_mem1<=T5_601

	T5_610 = S.Task('T5_610', length=1, delay_cost=1)
	T5_610 += alt(ADD)

	T5_610_mem0 = S.Task('T5_610_mem0', length=1, delay_cost=1)
	T5_610_mem0 += INPUT_mem_r
	S += T5_610_mem0<=T5_610

	T5_610_mem1 = S.Task('T5_610_mem1', length=1, delay_cost=1)
	T5_610_mem1 += INPUT_mem_r
	S += T5_610_mem1<=T5_610

	T5_611 = S.Task('T5_611', length=1, delay_cost=1)
	T5_611 += alt(ADD)

	T5_611_mem0 = S.Task('T5_611_mem0', length=1, delay_cost=1)
	T5_611_mem0 += INPUT_mem_r
	S += T5_611_mem0<=T5_611

	T5_611_mem1 = S.Task('T5_611_mem1', length=1, delay_cost=1)
	T5_611_mem1 += INPUT_mem_r
	S += T5_611_mem1<=T5_611

	T6_100 = S.Task('T6_100', length=1, delay_cost=1)
	T6_100 += alt(ADD)

	T6_100_mem0 = S.Task('T6_100_mem0', length=1, delay_cost=1)
	T6_100_mem0 += INPUT_mem_r
	S += T6_100_mem0<=T6_100

	T6_100_mem1 = S.Task('T6_100_mem1', length=1, delay_cost=1)
	T6_100_mem1 += INPUT_mem_r
	S += T6_100_mem1<=T6_100

	T6_101 = S.Task('T6_101', length=1, delay_cost=1)
	T6_101 += alt(ADD)

	T6_101_mem0 = S.Task('T6_101_mem0', length=1, delay_cost=1)
	T6_101_mem0 += INPUT_mem_r
	S += T6_101_mem0<=T6_101

	T6_101_mem1 = S.Task('T6_101_mem1', length=1, delay_cost=1)
	T6_101_mem1 += INPUT_mem_r
	S += T6_101_mem1<=T6_101

	T6_110 = S.Task('T6_110', length=1, delay_cost=1)
	T6_110 += alt(ADD)

	T6_110_mem0 = S.Task('T6_110_mem0', length=1, delay_cost=1)
	T6_110_mem0 += INPUT_mem_r
	S += T6_110_mem0<=T6_110

	T6_110_mem1 = S.Task('T6_110_mem1', length=1, delay_cost=1)
	T6_110_mem1 += INPUT_mem_r
	S += T6_110_mem1<=T6_110

	T6_111 = S.Task('T6_111', length=1, delay_cost=1)
	T6_111 += alt(ADD)

	T6_111_mem0 = S.Task('T6_111_mem0', length=1, delay_cost=1)
	T6_111_mem0 += INPUT_mem_r
	S += T6_111_mem0<=T6_111

	T6_111_mem1 = S.Task('T6_111_mem1', length=1, delay_cost=1)
	T6_111_mem1 += INPUT_mem_r
	S += T6_111_mem1<=T6_111

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "m24_mul1_add4/m24_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_m24_mul1_add4_1(0, 0)