from pyschedule import Scenario, solvers, plotters, alt

def solve_s24_mul1_add4_1(ConstStep, ExpStep):
	horizon = 174
	S=Scenario("s24_mul1_add4_1",horizon = horizon)

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
	T82t0_a1b1_in = S.Task('T82t0_a1b1_in', length=1, delay_cost=1)
	S += T82t0_a1b1_in >= 0
	T82t0_a1b1_in += MUL_in[0]

	T82t0_a1b1_mem0 = S.Task('T82t0_a1b1_mem0', length=1, delay_cost=1)
	S += T82t0_a1b1_mem0 >= 0
	T82t0_a1b1_mem0 += INPUT_mem_r

	T82t0_a1b1_mem1 = S.Task('T82t0_a1b1_mem1', length=1, delay_cost=1)
	S += T82t0_a1b1_mem1 >= 0
	T82t0_a1b1_mem1 += INPUT_mem_r

	T82t0_a0b0_in = S.Task('T82t0_a0b0_in', length=1, delay_cost=1)
	S += T82t0_a0b0_in >= 1
	T82t0_a0b0_in += MUL_in[0]

	T82t0_a0b0_mem0 = S.Task('T82t0_a0b0_mem0', length=1, delay_cost=1)
	S += T82t0_a0b0_mem0 >= 1
	T82t0_a0b0_mem0 += INPUT_mem_r

	T82t0_a0b0_mem1 = S.Task('T82t0_a0b0_mem1', length=1, delay_cost=1)
	S += T82t0_a0b0_mem1 >= 1
	T82t0_a0b0_mem1 += INPUT_mem_r

	T82t0_a1b1 = S.Task('T82t0_a1b1', length=7, delay_cost=1)
	S += T82t0_a1b1 >= 1
	T82t0_a1b1 += MUL[0]

	T71t1_a0b0_in = S.Task('T71t1_a0b0_in', length=1, delay_cost=1)
	S += T71t1_a0b0_in >= 2
	T71t1_a0b0_in += MUL_in[0]

	T71t1_a0b0_mem0 = S.Task('T71t1_a0b0_mem0', length=1, delay_cost=1)
	S += T71t1_a0b0_mem0 >= 2
	T71t1_a0b0_mem0 += INPUT_mem_r

	T71t1_a0b0_mem1 = S.Task('T71t1_a0b0_mem1', length=1, delay_cost=1)
	S += T71t1_a0b0_mem1 >= 2
	T71t1_a0b0_mem1 += INPUT_mem_r

	T82t0_a0b0 = S.Task('T82t0_a0b0', length=7, delay_cost=1)
	S += T82t0_a0b0 >= 2
	T82t0_a0b0 += MUL[0]

	T71t1_a0b0 = S.Task('T71t1_a0b0', length=7, delay_cost=1)
	S += T71t1_a0b0 >= 3
	T71t1_a0b0 += MUL[0]

	T71t1_a1b1_in = S.Task('T71t1_a1b1_in', length=1, delay_cost=1)
	S += T71t1_a1b1_in >= 3
	T71t1_a1b1_in += MUL_in[0]

	T71t1_a1b1_mem0 = S.Task('T71t1_a1b1_mem0', length=1, delay_cost=1)
	S += T71t1_a1b1_mem0 >= 3
	T71t1_a1b1_mem0 += INPUT_mem_r

	T71t1_a1b1_mem1 = S.Task('T71t1_a1b1_mem1', length=1, delay_cost=1)
	S += T71t1_a1b1_mem1 >= 3
	T71t1_a1b1_mem1 += INPUT_mem_r

	T71t1_a1b1 = S.Task('T71t1_a1b1', length=7, delay_cost=1)
	S += T71t1_a1b1 >= 4
	T71t1_a1b1 += MUL[0]

	T82t1_a0b0_in = S.Task('T82t1_a0b0_in', length=1, delay_cost=1)
	S += T82t1_a0b0_in >= 4
	T82t1_a0b0_in += MUL_in[0]

	T82t1_a0b0_mem0 = S.Task('T82t1_a0b0_mem0', length=1, delay_cost=1)
	S += T82t1_a0b0_mem0 >= 4
	T82t1_a0b0_mem0 += INPUT_mem_r

	T82t1_a0b0_mem1 = S.Task('T82t1_a0b0_mem1', length=1, delay_cost=1)
	S += T82t1_a0b0_mem1 >= 4
	T82t1_a0b0_mem1 += INPUT_mem_r

	T71t0_a0b0_in = S.Task('T71t0_a0b0_in', length=1, delay_cost=1)
	S += T71t0_a0b0_in >= 5
	T71t0_a0b0_in += MUL_in[0]

	T71t0_a0b0_mem0 = S.Task('T71t0_a0b0_mem0', length=1, delay_cost=1)
	S += T71t0_a0b0_mem0 >= 5
	T71t0_a0b0_mem0 += INPUT_mem_r

	T71t0_a0b0_mem1 = S.Task('T71t0_a0b0_mem1', length=1, delay_cost=1)
	S += T71t0_a0b0_mem1 >= 5
	T71t0_a0b0_mem1 += INPUT_mem_r

	T82t1_a0b0 = S.Task('T82t1_a0b0', length=7, delay_cost=1)
	S += T82t1_a0b0 >= 5
	T82t1_a0b0 += MUL[0]

	T61t1_a1b1_in = S.Task('T61t1_a1b1_in', length=1, delay_cost=1)
	S += T61t1_a1b1_in >= 6
	T61t1_a1b1_in += MUL_in[0]

	T61t1_a1b1_mem0 = S.Task('T61t1_a1b1_mem0', length=1, delay_cost=1)
	S += T61t1_a1b1_mem0 >= 6
	T61t1_a1b1_mem0 += INPUT_mem_r

	T61t1_a1b1_mem1 = S.Task('T61t1_a1b1_mem1', length=1, delay_cost=1)
	S += T61t1_a1b1_mem1 >= 6
	T61t1_a1b1_mem1 += INPUT_mem_r

	T71t0_a0b0 = S.Task('T71t0_a0b0', length=7, delay_cost=1)
	S += T71t0_a0b0 >= 6
	T71t0_a0b0 += MUL[0]

	T61t1_a0b0_in = S.Task('T61t1_a0b0_in', length=1, delay_cost=1)
	S += T61t1_a0b0_in >= 7
	T61t1_a0b0_in += MUL_in[0]

	T61t1_a0b0_mem0 = S.Task('T61t1_a0b0_mem0', length=1, delay_cost=1)
	S += T61t1_a0b0_mem0 >= 7
	T61t1_a0b0_mem0 += INPUT_mem_r

	T61t1_a0b0_mem1 = S.Task('T61t1_a0b0_mem1', length=1, delay_cost=1)
	S += T61t1_a0b0_mem1 >= 7
	T61t1_a0b0_mem1 += INPUT_mem_r

	T61t1_a1b1 = S.Task('T61t1_a1b1', length=7, delay_cost=1)
	S += T61t1_a1b1 >= 7
	T61t1_a1b1 += MUL[0]

	T61t0_a1b1_in = S.Task('T61t0_a1b1_in', length=1, delay_cost=1)
	S += T61t0_a1b1_in >= 8
	T61t0_a1b1_in += MUL_in[0]

	T61t0_a1b1_mem0 = S.Task('T61t0_a1b1_mem0', length=1, delay_cost=1)
	S += T61t0_a1b1_mem0 >= 8
	T61t0_a1b1_mem0 += INPUT_mem_r

	T61t0_a1b1_mem1 = S.Task('T61t0_a1b1_mem1', length=1, delay_cost=1)
	S += T61t0_a1b1_mem1 >= 8
	T61t0_a1b1_mem1 += INPUT_mem_r

	T61t1_a0b0 = S.Task('T61t1_a0b0', length=7, delay_cost=1)
	S += T61t1_a0b0 >= 8
	T61t1_a0b0 += MUL[0]

	T61t0_a1b1 = S.Task('T61t0_a1b1', length=7, delay_cost=1)
	S += T61t0_a1b1 >= 9
	T61t0_a1b1 += MUL[0]

	T82t1_a1b1_in = S.Task('T82t1_a1b1_in', length=1, delay_cost=1)
	S += T82t1_a1b1_in >= 9
	T82t1_a1b1_in += MUL_in[0]

	T82t1_a1b1_mem0 = S.Task('T82t1_a1b1_mem0', length=1, delay_cost=1)
	S += T82t1_a1b1_mem0 >= 9
	T82t1_a1b1_mem0 += INPUT_mem_r

	T82t1_a1b1_mem1 = S.Task('T82t1_a1b1_mem1', length=1, delay_cost=1)
	S += T82t1_a1b1_mem1 >= 9
	T82t1_a1b1_mem1 += INPUT_mem_r

	T71t0_a1b1_in = S.Task('T71t0_a1b1_in', length=1, delay_cost=1)
	S += T71t0_a1b1_in >= 10
	T71t0_a1b1_in += MUL_in[0]

	T71t0_a1b1_mem0 = S.Task('T71t0_a1b1_mem0', length=1, delay_cost=1)
	S += T71t0_a1b1_mem0 >= 10
	T71t0_a1b1_mem0 += INPUT_mem_r

	T71t0_a1b1_mem1 = S.Task('T71t0_a1b1_mem1', length=1, delay_cost=1)
	S += T71t0_a1b1_mem1 >= 10
	T71t0_a1b1_mem1 += INPUT_mem_r

	T82t1_a1b1 = S.Task('T82t1_a1b1', length=7, delay_cost=1)
	S += T82t1_a1b1 >= 10
	T82t1_a1b1 += MUL[0]

	T61t0_a0b0_in = S.Task('T61t0_a0b0_in', length=1, delay_cost=1)
	S += T61t0_a0b0_in >= 11
	T61t0_a0b0_in += MUL_in[0]

	T61t0_a0b0_mem0 = S.Task('T61t0_a0b0_mem0', length=1, delay_cost=1)
	S += T61t0_a0b0_mem0 >= 11
	T61t0_a0b0_mem0 += INPUT_mem_r

	T61t0_a0b0_mem1 = S.Task('T61t0_a0b0_mem1', length=1, delay_cost=1)
	S += T61t0_a0b0_mem1 >= 11
	T61t0_a0b0_mem1 += INPUT_mem_r

	T71t0_a1b1 = S.Task('T71t0_a1b1', length=7, delay_cost=1)
	S += T71t0_a1b1 >= 11
	T71t0_a1b1 += MUL[0]

	T61t0_a0b0 = S.Task('T61t0_a0b0', length=7, delay_cost=1)
	S += T61t0_a0b0 >= 12
	T61t0_a0b0 += MUL[0]

	T82t2_1_mem0 = S.Task('T82t2_1_mem0', length=1, delay_cost=1)
	S += T82t2_1_mem0 >= 12
	T82t2_1_mem0 += INPUT_mem_r

	T82t2_1_mem1 = S.Task('T82t2_1_mem1', length=1, delay_cost=1)
	S += T82t2_1_mem1 >= 12
	T82t2_1_mem1 += INPUT_mem_r

	T71t3_a0b0_mem0 = S.Task('T71t3_a0b0_mem0', length=1, delay_cost=1)
	S += T71t3_a0b0_mem0 >= 13
	T71t3_a0b0_mem0 += INPUT_mem_r

	T71t3_a0b0_mem1 = S.Task('T71t3_a0b0_mem1', length=1, delay_cost=1)
	S += T71t3_a0b0_mem1 >= 13
	T71t3_a0b0_mem1 += INPUT_mem_r

	T82t2_1 = S.Task('T82t2_1', length=1, delay_cost=1)
	S += T82t2_1 >= 13
	T82t2_1 += ADD[0]

	T4210_mem0 = S.Task('T4210_mem0', length=1, delay_cost=1)
	S += T4210_mem0 >= 14
	T4210_mem0 += INPUT_mem_r

	T4210_mem1 = S.Task('T4210_mem1', length=1, delay_cost=1)
	S += T4210_mem1 >= 14
	T4210_mem1 += INPUT_mem_r

	T71t3_a0b0 = S.Task('T71t3_a0b0', length=1, delay_cost=1)
	S += T71t3_a0b0 >= 14
	T71t3_a0b0 += ADD[2]

	T4210 = S.Task('T4210', length=1, delay_cost=1)
	S += T4210 >= 15
	T4210 += ADD[2]

	T61t3_a1b1_mem0 = S.Task('T61t3_a1b1_mem0', length=1, delay_cost=1)
	S += T61t3_a1b1_mem0 >= 15
	T61t3_a1b1_mem0 += INPUT_mem_r

	T61t3_a1b1_mem1 = S.Task('T61t3_a1b1_mem1', length=1, delay_cost=1)
	S += T61t3_a1b1_mem1 >= 15
	T61t3_a1b1_mem1 += INPUT_mem_r

	T61t3_a1b1 = S.Task('T61t3_a1b1', length=1, delay_cost=1)
	S += T61t3_a1b1 >= 16
	T61t3_a1b1 += ADD[1]

	T71t2_1_mem0 = S.Task('T71t2_1_mem0', length=1, delay_cost=1)
	S += T71t2_1_mem0 >= 16
	T71t2_1_mem0 += INPUT_mem_r

	T71t2_1_mem1 = S.Task('T71t2_1_mem1', length=1, delay_cost=1)
	S += T71t2_1_mem1 >= 16
	T71t2_1_mem1 += INPUT_mem_r

	T61t2_a0b0_mem0 = S.Task('T61t2_a0b0_mem0', length=1, delay_cost=1)
	S += T61t2_a0b0_mem0 >= 17
	T61t2_a0b0_mem0 += INPUT_mem_r

	T61t2_a0b0_mem1 = S.Task('T61t2_a0b0_mem1', length=1, delay_cost=1)
	S += T61t2_a0b0_mem1 >= 17
	T61t2_a0b0_mem1 += INPUT_mem_r

	T71t2_1 = S.Task('T71t2_1', length=1, delay_cost=1)
	S += T71t2_1 >= 17
	T71t2_1 += ADD[0]

	T61t2_a0b0 = S.Task('T61t2_a0b0', length=1, delay_cost=1)
	S += T61t2_a0b0 >= 18
	T61t2_a0b0 += ADD[2]

	T71t2_a0b0_mem0 = S.Task('T71t2_a0b0_mem0', length=1, delay_cost=1)
	S += T71t2_a0b0_mem0 >= 18
	T71t2_a0b0_mem0 += INPUT_mem_r

	T71t2_a0b0_mem1 = S.Task('T71t2_a0b0_mem1', length=1, delay_cost=1)
	S += T71t2_a0b0_mem1 >= 18
	T71t2_a0b0_mem1 += INPUT_mem_r

	T10111_mem0 = S.Task('T10111_mem0', length=1, delay_cost=1)
	S += T10111_mem0 >= 19
	T10111_mem0 += INPUT_mem_r

	T10111_mem1 = S.Task('T10111_mem1', length=1, delay_cost=1)
	S += T10111_mem1 >= 19
	T10111_mem1 += INPUT_mem_r

	T71t2_a0b0 = S.Task('T71t2_a0b0', length=1, delay_cost=1)
	S += T71t2_a0b0 >= 19
	T71t2_a0b0 += ADD[0]

	T10111 = S.Task('T10111', length=1, delay_cost=1)
	S += T10111 >= 20
	T10111 += ADD[2]

	T5200_mem0 = S.Task('T5200_mem0', length=1, delay_cost=1)
	S += T5200_mem0 >= 20
	T5200_mem0 += INPUT_mem_r

	T5200_mem1 = S.Task('T5200_mem1', length=1, delay_cost=1)
	S += T5200_mem1 >= 20
	T5200_mem1 += INPUT_mem_r

	T5200 = S.Task('T5200', length=1, delay_cost=1)
	S += T5200 >= 21
	T5200 += ADD[1]

	T61t2_1_mem0 = S.Task('T61t2_1_mem0', length=1, delay_cost=1)
	S += T61t2_1_mem0 >= 21
	T61t2_1_mem0 += INPUT_mem_r

	T61t2_1_mem1 = S.Task('T61t2_1_mem1', length=1, delay_cost=1)
	S += T61t2_1_mem1 >= 21
	T61t2_1_mem1 += INPUT_mem_r

	T61t2_1 = S.Task('T61t2_1', length=1, delay_cost=1)
	S += T61t2_1 >= 22
	T61t2_1 += ADD[1]

	T71t3_1_mem0 = S.Task('T71t3_1_mem0', length=1, delay_cost=1)
	S += T71t3_1_mem0 >= 22
	T71t3_1_mem0 += INPUT_mem_r

	T71t3_1_mem1 = S.Task('T71t3_1_mem1', length=1, delay_cost=1)
	S += T71t3_1_mem1 >= 22
	T71t3_1_mem1 += INPUT_mem_r

	T411_mem0 = S.Task('T411_mem0', length=1, delay_cost=1)
	S += T411_mem0 >= 23
	T411_mem0 += INPUT_mem_r

	T411_mem1 = S.Task('T411_mem1', length=1, delay_cost=1)
	S += T411_mem1 >= 23
	T411_mem1 += INPUT_mem_r

	T71t3_1 = S.Task('T71t3_1', length=1, delay_cost=1)
	S += T71t3_1 >= 23
	T71t3_1 += ADD[0]

	T411 = S.Task('T411', length=1, delay_cost=1)
	S += T411 >= 24
	T411 += ADD[0]

	T511_mem0 = S.Task('T511_mem0', length=1, delay_cost=1)
	S += T511_mem0 >= 24
	T511_mem0 += INPUT_mem_r

	T511_mem1 = S.Task('T511_mem1', length=1, delay_cost=1)
	S += T511_mem1 >= 24
	T511_mem1 += INPUT_mem_r

	T510_mem0 = S.Task('T510_mem0', length=1, delay_cost=1)
	S += T510_mem0 >= 25
	T510_mem0 += INPUT_mem_r

	T510_mem1 = S.Task('T510_mem1', length=1, delay_cost=1)
	S += T510_mem1 >= 25
	T510_mem1 += INPUT_mem_r

	T511 = S.Task('T511', length=1, delay_cost=1)
	S += T511 >= 25
	T511 += ADD[0]

	T510 = S.Task('T510', length=1, delay_cost=1)
	S += T510 >= 26
	T510 += ADD[1]

	T61t2_0_mem0 = S.Task('T61t2_0_mem0', length=1, delay_cost=1)
	S += T61t2_0_mem0 >= 26
	T61t2_0_mem0 += INPUT_mem_r

	T61t2_0_mem1 = S.Task('T61t2_0_mem1', length=1, delay_cost=1)
	S += T61t2_0_mem1 >= 26
	T61t2_0_mem1 += INPUT_mem_r

	T300_mem0 = S.Task('T300_mem0', length=1, delay_cost=1)
	S += T300_mem0 >= 27
	T300_mem0 += INPUT_mem_r

	T300_mem1 = S.Task('T300_mem1', length=1, delay_cost=1)
	S += T300_mem1 >= 27
	T300_mem1 += INPUT_mem_r

	T61t2_0 = S.Task('T61t2_0', length=1, delay_cost=1)
	S += T61t2_0 >= 27
	T61t2_0 += ADD[0]

	T300 = S.Task('T300', length=1, delay_cost=1)
	S += T300 >= 28
	T300 += ADD[1]

	T82t2_a0b0_mem0 = S.Task('T82t2_a0b0_mem0', length=1, delay_cost=1)
	S += T82t2_a0b0_mem0 >= 28
	T82t2_a0b0_mem0 += INPUT_mem_r

	T82t2_a0b0_mem1 = S.Task('T82t2_a0b0_mem1', length=1, delay_cost=1)
	S += T82t2_a0b0_mem1 >= 28
	T82t2_a0b0_mem1 += INPUT_mem_r

	T0110_mem0 = S.Task('T0110_mem0', length=1, delay_cost=1)
	S += T0110_mem0 >= 29
	T0110_mem0 += INPUT_mem_r

	T0110_mem1 = S.Task('T0110_mem1', length=1, delay_cost=1)
	S += T0110_mem1 >= 29
	T0110_mem1 += INPUT_mem_r

	T82t2_a0b0 = S.Task('T82t2_a0b0', length=1, delay_cost=1)
	S += T82t2_a0b0 >= 29
	T82t2_a0b0 += ADD[0]

	T0110 = S.Task('T0110', length=1, delay_cost=1)
	S += T0110 >= 30
	T0110 += ADD[3]

	T9410_mem0 = S.Task('T9410_mem0', length=1, delay_cost=1)
	S += T9410_mem0 >= 30
	T9410_mem0 += INPUT_mem_r

	T9410_mem1 = S.Task('T9410_mem1', length=1, delay_cost=1)
	S += T9410_mem1 >= 30
	T9410_mem1 += INPUT_mem_r

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 31
	T211_mem0 += INPUT_mem_r

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 31
	T211_mem1 += INPUT_mem_r

	T9410 = S.Task('T9410', length=1, delay_cost=1)
	S += T9410 >= 31
	T9410 += ADD[0]

	T211 = S.Task('T211', length=1, delay_cost=1)
	S += T211 >= 32
	T211 += ADD[0]

	T9400_mem0 = S.Task('T9400_mem0', length=1, delay_cost=1)
	S += T9400_mem0 >= 32
	T9400_mem0 += INPUT_mem_r

	T9400_mem1 = S.Task('T9400_mem1', length=1, delay_cost=1)
	S += T9400_mem1 >= 32
	T9400_mem1 += INPUT_mem_r

	T9400 = S.Task('T9400', length=1, delay_cost=1)
	S += T9400 >= 33
	T9400 += ADD[0]

	T9401_mem0 = S.Task('T9401_mem0', length=1, delay_cost=1)
	S += T9401_mem0 >= 33
	T9401_mem0 += INPUT_mem_r

	T9401_mem1 = S.Task('T9401_mem1', length=1, delay_cost=1)
	S += T9401_mem1 >= 33
	T9401_mem1 += INPUT_mem_r

	T61t3_1_mem0 = S.Task('T61t3_1_mem0', length=1, delay_cost=1)
	S += T61t3_1_mem0 >= 34
	T61t3_1_mem0 += INPUT_mem_r

	T61t3_1_mem1 = S.Task('T61t3_1_mem1', length=1, delay_cost=1)
	S += T61t3_1_mem1 >= 34
	T61t3_1_mem1 += INPUT_mem_r

	T9401 = S.Task('T9401', length=1, delay_cost=1)
	S += T9401 >= 34
	T9401 += ADD[0]

	T61t2_a1b1_mem0 = S.Task('T61t2_a1b1_mem0', length=1, delay_cost=1)
	S += T61t2_a1b1_mem0 >= 35
	T61t2_a1b1_mem0 += INPUT_mem_r

	T61t2_a1b1_mem1 = S.Task('T61t2_a1b1_mem1', length=1, delay_cost=1)
	S += T61t2_a1b1_mem1 >= 35
	T61t2_a1b1_mem1 += INPUT_mem_r

	T61t3_1 = S.Task('T61t3_1', length=1, delay_cost=1)
	S += T61t3_1 >= 35
	T61t3_1 += ADD[2]

	T5211_mem0 = S.Task('T5211_mem0', length=1, delay_cost=1)
	S += T5211_mem0 >= 36
	T5211_mem0 += INPUT_mem_r

	T5211_mem1 = S.Task('T5211_mem1', length=1, delay_cost=1)
	S += T5211_mem1 >= 36
	T5211_mem1 += INPUT_mem_r

	T61t2_a1b1 = S.Task('T61t2_a1b1', length=1, delay_cost=1)
	S += T61t2_a1b1 >= 36
	T61t2_a1b1 += ADD[0]

	T500_mem0 = S.Task('T500_mem0', length=1, delay_cost=1)
	S += T500_mem0 >= 37
	T500_mem0 += INPUT_mem_r

	T500_mem1 = S.Task('T500_mem1', length=1, delay_cost=1)
	S += T500_mem1 >= 37
	T500_mem1 += INPUT_mem_r

	T5211 = S.Task('T5211', length=1, delay_cost=1)
	S += T5211 >= 37
	T5211 += ADD[0]

	T500 = S.Task('T500', length=1, delay_cost=1)
	S += T500 >= 38
	T500 += ADD[0]

	T71t3_0_mem0 = S.Task('T71t3_0_mem0', length=1, delay_cost=1)
	S += T71t3_0_mem0 >= 38
	T71t3_0_mem0 += INPUT_mem_r

	T71t3_0_mem1 = S.Task('T71t3_0_mem1', length=1, delay_cost=1)
	S += T71t3_0_mem1 >= 38
	T71t3_0_mem1 += INPUT_mem_r

	T71t3_0 = S.Task('T71t3_0', length=1, delay_cost=1)
	S += T71t3_0 >= 39
	T71t3_0 += ADD[0]

	T71t3_a1b1_mem0 = S.Task('T71t3_a1b1_mem0', length=1, delay_cost=1)
	S += T71t3_a1b1_mem0 >= 39
	T71t3_a1b1_mem0 += INPUT_mem_r

	T71t3_a1b1_mem1 = S.Task('T71t3_a1b1_mem1', length=1, delay_cost=1)
	S += T71t3_a1b1_mem1 >= 39
	T71t3_a1b1_mem1 += INPUT_mem_r

	T71t2_a1b1_mem0 = S.Task('T71t2_a1b1_mem0', length=1, delay_cost=1)
	S += T71t2_a1b1_mem0 >= 40
	T71t2_a1b1_mem0 += INPUT_mem_r

	T71t2_a1b1_mem1 = S.Task('T71t2_a1b1_mem1', length=1, delay_cost=1)
	S += T71t2_a1b1_mem1 >= 40
	T71t2_a1b1_mem1 += INPUT_mem_r

	T71t3_a1b1 = S.Task('T71t3_a1b1', length=1, delay_cost=1)
	S += T71t3_a1b1 >= 40
	T71t3_a1b1 += ADD[0]

	T4300_mem0 = S.Task('T4300_mem0', length=1, delay_cost=1)
	S += T4300_mem0 >= 41
	T4300_mem0 += INPUT_mem_r

	T4300_mem1 = S.Task('T4300_mem1', length=1, delay_cost=1)
	S += T4300_mem1 >= 41
	T4300_mem1 += INPUT_mem_r

	T71t2_a1b1 = S.Task('T71t2_a1b1', length=1, delay_cost=1)
	S += T71t2_a1b1 >= 41
	T71t2_a1b1 += ADD[0]

	T3110_mem0 = S.Task('T3110_mem0', length=1, delay_cost=1)
	S += T3110_mem0 >= 42
	T3110_mem0 += INPUT_mem_r

	T3110_mem1 = S.Task('T3110_mem1', length=1, delay_cost=1)
	S += T3110_mem1 >= 42
	T3110_mem1 += INPUT_mem_r

	T4300 = S.Task('T4300', length=1, delay_cost=1)
	S += T4300 >= 42
	T4300 += ADD[0]

	T3110 = S.Task('T3110', length=1, delay_cost=1)
	S += T3110 >= 43
	T3110 += ADD[0]

	T501_mem0 = S.Task('T501_mem0', length=1, delay_cost=1)
	S += T501_mem0 >= 43
	T501_mem0 += INPUT_mem_r

	T501_mem1 = S.Task('T501_mem1', length=1, delay_cost=1)
	S += T501_mem1 >= 43
	T501_mem1 += INPUT_mem_r

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	S += T201_mem0 >= 44
	T201_mem0 += INPUT_mem_r

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	S += T201_mem1 >= 44
	T201_mem1 += INPUT_mem_r

	T501 = S.Task('T501', length=1, delay_cost=1)
	S += T501 >= 44
	T501 += ADD[0]

	T201 = S.Task('T201', length=1, delay_cost=1)
	S += T201 >= 45
	T201 += ADD[1]

	T9411_mem0 = S.Task('T9411_mem0', length=1, delay_cost=1)
	S += T9411_mem0 >= 45
	T9411_mem0 += INPUT_mem_r

	T9411_mem1 = S.Task('T9411_mem1', length=1, delay_cost=1)
	S += T9411_mem1 >= 45
	T9411_mem1 += INPUT_mem_r

	T71t2_0_mem0 = S.Task('T71t2_0_mem0', length=1, delay_cost=1)
	S += T71t2_0_mem0 >= 46
	T71t2_0_mem0 += INPUT_mem_r

	T71t2_0_mem1 = S.Task('T71t2_0_mem1', length=1, delay_cost=1)
	S += T71t2_0_mem1 >= 46
	T71t2_0_mem1 += INPUT_mem_r

	T9411 = S.Task('T9411', length=1, delay_cost=1)
	S += T9411 >= 46
	T9411 += ADD[0]

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	S += T410_mem0 >= 47
	T410_mem0 += INPUT_mem_r

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	S += T410_mem1 >= 47
	T410_mem1 += INPUT_mem_r

	T71t2_0 = S.Task('T71t2_0', length=1, delay_cost=1)
	S += T71t2_0 >= 47
	T71t2_0 += ADD[1]

	T410 = S.Task('T410', length=1, delay_cost=1)
	S += T410 >= 48
	T410 += ADD[1]

	T4310_mem0 = S.Task('T4310_mem0', length=1, delay_cost=1)
	S += T4310_mem0 >= 48
	T4310_mem0 += INPUT_mem_r

	T4310_mem1 = S.Task('T4310_mem1', length=1, delay_cost=1)
	S += T4310_mem1 >= 48
	T4310_mem1 += INPUT_mem_r

	T3101_mem0 = S.Task('T3101_mem0', length=1, delay_cost=1)
	S += T3101_mem0 >= 49
	T3101_mem0 += INPUT_mem_r

	T3101_mem1 = S.Task('T3101_mem1', length=1, delay_cost=1)
	S += T3101_mem1 >= 49
	T3101_mem1 += INPUT_mem_r

	T4310 = S.Task('T4310', length=1, delay_cost=1)
	S += T4310 >= 49
	T4310 += ADD[1]

	T3101 = S.Task('T3101', length=1, delay_cost=1)
	S += T3101 >= 50
	T3101 += ADD[0]

	T4211_mem0 = S.Task('T4211_mem0', length=1, delay_cost=1)
	S += T4211_mem0 >= 50
	T4211_mem0 += INPUT_mem_r

	T4211_mem1 = S.Task('T4211_mem1', length=1, delay_cost=1)
	S += T4211_mem1 >= 50
	T4211_mem1 += INPUT_mem_r

	T4211 = S.Task('T4211', length=1, delay_cost=1)
	S += T4211 >= 51
	T4211 += ADD[0]

	T82t3_0_mem0 = S.Task('T82t3_0_mem0', length=1, delay_cost=1)
	S += T82t3_0_mem0 >= 51
	T82t3_0_mem0 += INPUT_mem_r

	T82t3_0_mem1 = S.Task('T82t3_0_mem1', length=1, delay_cost=1)
	S += T82t3_0_mem1 >= 51
	T82t3_0_mem1 += INPUT_mem_r

	T4311_mem0 = S.Task('T4311_mem0', length=1, delay_cost=1)
	S += T4311_mem0 >= 52
	T4311_mem0 += INPUT_mem_r

	T4311_mem1 = S.Task('T4311_mem1', length=1, delay_cost=1)
	S += T4311_mem1 >= 52
	T4311_mem1 += INPUT_mem_r

	T82t3_0 = S.Task('T82t3_0', length=1, delay_cost=1)
	S += T82t3_0 >= 52
	T82t3_0 += ADD[1]

	T4200_mem0 = S.Task('T4200_mem0', length=1, delay_cost=1)
	S += T4200_mem0 >= 53
	T4200_mem0 += INPUT_mem_r

	T4200_mem1 = S.Task('T4200_mem1', length=1, delay_cost=1)
	S += T4200_mem1 >= 53
	T4200_mem1 += INPUT_mem_r

	T4311 = S.Task('T4311', length=1, delay_cost=1)
	S += T4311 >= 53
	T4311 += ADD[3]

	T4200 = S.Task('T4200', length=1, delay_cost=1)
	S += T4200 >= 54
	T4200 += ADD[0]

	T5201_mem0 = S.Task('T5201_mem0', length=1, delay_cost=1)
	S += T5201_mem0 >= 54
	T5201_mem0 += INPUT_mem_r

	T5201_mem1 = S.Task('T5201_mem1', length=1, delay_cost=1)
	S += T5201_mem1 >= 54
	T5201_mem1 += INPUT_mem_r

	T5201 = S.Task('T5201', length=1, delay_cost=1)
	S += T5201 >= 55
	T5201 += ADD[1]

	T82t3_a0b0_mem0 = S.Task('T82t3_a0b0_mem0', length=1, delay_cost=1)
	S += T82t3_a0b0_mem0 >= 55
	T82t3_a0b0_mem0 += INPUT_mem_r

	T82t3_a0b0_mem1 = S.Task('T82t3_a0b0_mem1', length=1, delay_cost=1)
	S += T82t3_a0b0_mem1 >= 55
	T82t3_a0b0_mem1 += INPUT_mem_r

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	S += T401_mem0 >= 56
	T401_mem0 += INPUT_mem_r

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	S += T401_mem1 >= 56
	T401_mem1 += INPUT_mem_r

	T82t3_a0b0 = S.Task('T82t3_a0b0', length=1, delay_cost=1)
	S += T82t3_a0b0 >= 56
	T82t3_a0b0 += ADD[0]

	T401 = S.Task('T401', length=1, delay_cost=1)
	S += T401 >= 57
	T401 += ADD[1]

	T5210_mem0 = S.Task('T5210_mem0', length=1, delay_cost=1)
	S += T5210_mem0 >= 57
	T5210_mem0 += INPUT_mem_r

	T5210_mem1 = S.Task('T5210_mem1', length=1, delay_cost=1)
	S += T5210_mem1 >= 57
	T5210_mem1 += INPUT_mem_r

	T4301_mem0 = S.Task('T4301_mem0', length=1, delay_cost=1)
	S += T4301_mem0 >= 58
	T4301_mem0 += INPUT_mem_r

	T4301_mem1 = S.Task('T4301_mem1', length=1, delay_cost=1)
	S += T4301_mem1 >= 58
	T4301_mem1 += INPUT_mem_r

	T5210 = S.Task('T5210', length=1, delay_cost=1)
	S += T5210 >= 58
	T5210 += ADD[1]

	T4201_mem0 = S.Task('T4201_mem0', length=1, delay_cost=1)
	S += T4201_mem0 >= 59
	T4201_mem0 += INPUT_mem_r

	T4201_mem1 = S.Task('T4201_mem1', length=1, delay_cost=1)
	S += T4201_mem1 >= 59
	T4201_mem1 += INPUT_mem_r

	T4301 = S.Task('T4301', length=1, delay_cost=1)
	S += T4301 >= 59
	T4301 += ADD[2]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 60
	T210_mem0 += INPUT_mem_r

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 60
	T210_mem1 += INPUT_mem_r

	T4201 = S.Task('T4201', length=1, delay_cost=1)
	S += T4201 >= 60
	T4201 += ADD[1]

	T210 = S.Task('T210', length=1, delay_cost=1)
	S += T210 >= 61
	T210 += ADD[2]

	T82t2_0_mem0 = S.Task('T82t2_0_mem0', length=1, delay_cost=1)
	S += T82t2_0_mem0 >= 61
	T82t2_0_mem0 += INPUT_mem_r

	T82t2_0_mem1 = S.Task('T82t2_0_mem1', length=1, delay_cost=1)
	S += T82t2_0_mem1 >= 61
	T82t2_0_mem1 += INPUT_mem_r

	T311_mem0 = S.Task('T311_mem0', length=1, delay_cost=1)
	S += T311_mem0 >= 62
	T311_mem0 += INPUT_mem_r

	T311_mem1 = S.Task('T311_mem1', length=1, delay_cost=1)
	S += T311_mem1 >= 62
	T311_mem1 += INPUT_mem_r

	T82t2_0 = S.Task('T82t2_0', length=1, delay_cost=1)
	S += T82t2_0 >= 62
	T82t2_0 += ADD[0]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 63
	T110_mem0 += INPUT_mem_r

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 63
	T110_mem1 += INPUT_mem_r

	T311 = S.Task('T311', length=1, delay_cost=1)
	S += T311 >= 63
	T311 += ADD[2]

	T110 = S.Task('T110', length=1, delay_cost=1)
	S += T110 >= 64
	T110 += ADD[0]

	T61t3_0_mem0 = S.Task('T61t3_0_mem0', length=1, delay_cost=1)
	S += T61t3_0_mem0 >= 64
	T61t3_0_mem0 += INPUT_mem_r

	T61t3_0_mem1 = S.Task('T61t3_0_mem1', length=1, delay_cost=1)
	S += T61t3_0_mem1 >= 64
	T61t3_0_mem1 += INPUT_mem_r

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 65
	T101_mem0 += INPUT_mem_r

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 65
	T101_mem1 += INPUT_mem_r

	T61t3_0 = S.Task('T61t3_0', length=1, delay_cost=1)
	S += T61t3_0 >= 65
	T61t3_0 += ADD[0]

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 66
	T101 += ADD[1]

	T400_mem0 = S.Task('T400_mem0', length=1, delay_cost=1)
	S += T400_mem0 >= 66
	T400_mem0 += INPUT_mem_r

	T400_mem1 = S.Task('T400_mem1', length=1, delay_cost=1)
	S += T400_mem1 >= 66
	T400_mem1 += INPUT_mem_r

	T310_mem0 = S.Task('T310_mem0', length=1, delay_cost=1)
	S += T310_mem0 >= 67
	T310_mem0 += INPUT_mem_r

	T310_mem1 = S.Task('T310_mem1', length=1, delay_cost=1)
	S += T310_mem1 >= 67
	T310_mem1 += INPUT_mem_r

	T400 = S.Task('T400', length=1, delay_cost=1)
	S += T400 >= 67
	T400 += ADD[0]

	T310 = S.Task('T310', length=1, delay_cost=1)
	S += T310 >= 68
	T310 += ADD[0]

	T82t2_a1b1_mem0 = S.Task('T82t2_a1b1_mem0', length=1, delay_cost=1)
	S += T82t2_a1b1_mem0 >= 68
	T82t2_a1b1_mem0 += INPUT_mem_r

	T82t2_a1b1_mem1 = S.Task('T82t2_a1b1_mem1', length=1, delay_cost=1)
	S += T82t2_a1b1_mem1 >= 68
	T82t2_a1b1_mem1 += INPUT_mem_r

	T82t2_a1b1 = S.Task('T82t2_a1b1', length=1, delay_cost=1)
	S += T82t2_a1b1 >= 69
	T82t2_a1b1 += ADD[2]

	T82t3_1_mem0 = S.Task('T82t3_1_mem0', length=1, delay_cost=1)
	S += T82t3_1_mem0 >= 69
	T82t3_1_mem0 += INPUT_mem_r

	T82t3_1_mem1 = S.Task('T82t3_1_mem1', length=1, delay_cost=1)
	S += T82t3_1_mem1 >= 69
	T82t3_1_mem1 += INPUT_mem_r

	T61t3_a0b0_mem0 = S.Task('T61t3_a0b0_mem0', length=1, delay_cost=1)
	S += T61t3_a0b0_mem0 >= 70
	T61t3_a0b0_mem0 += INPUT_mem_r

	T61t3_a0b0_mem1 = S.Task('T61t3_a0b0_mem1', length=1, delay_cost=1)
	S += T61t3_a0b0_mem1 >= 70
	T61t3_a0b0_mem1 += INPUT_mem_r

	T82t3_1 = S.Task('T82t3_1', length=1, delay_cost=1)
	S += T82t3_1 >= 70
	T82t3_1 += ADD[3]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 71
	T100_mem0 += INPUT_mem_r

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 71
	T100_mem1 += INPUT_mem_r

	T61t3_a0b0 = S.Task('T61t3_a0b0', length=1, delay_cost=1)
	S += T61t3_a0b0 >= 71
	T61t3_a0b0 += ADD[0]

	T100 = S.Task('T100', length=1, delay_cost=1)
	S += T100 >= 72
	T100 += ADD[0]

	T10110_mem0 = S.Task('T10110_mem0', length=1, delay_cost=1)
	S += T10110_mem0 >= 72
	T10110_mem0 += INPUT_mem_r

	T10110_mem1 = S.Task('T10110_mem1', length=1, delay_cost=1)
	S += T10110_mem1 >= 72
	T10110_mem1 += INPUT_mem_r

	T10110 = S.Task('T10110', length=1, delay_cost=1)
	S += T10110 >= 73
	T10110 += ADD[0]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 73
	T111_mem0 += INPUT_mem_r

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 73
	T111_mem1 += INPUT_mem_r

	T111 = S.Task('T111', length=1, delay_cost=1)
	S += T111 >= 74
	T111 += ADD[1]

	T3100_mem0 = S.Task('T3100_mem0', length=1, delay_cost=1)
	S += T3100_mem0 >= 74
	T3100_mem0 += INPUT_mem_r

	T3100_mem1 = S.Task('T3100_mem1', length=1, delay_cost=1)
	S += T3100_mem1 >= 74
	T3100_mem1 += INPUT_mem_r

	T3100 = S.Task('T3100', length=1, delay_cost=1)
	S += T3100 >= 75
	T3100 += ADD[0]

	T3111_mem0 = S.Task('T3111_mem0', length=1, delay_cost=1)
	S += T3111_mem0 >= 75
	T3111_mem0 += INPUT_mem_r

	T3111_mem1 = S.Task('T3111_mem1', length=1, delay_cost=1)
	S += T3111_mem1 >= 75
	T3111_mem1 += INPUT_mem_r

	T001_mem0 = S.Task('T001_mem0', length=1, delay_cost=1)
	S += T001_mem0 >= 76
	T001_mem0 += INPUT_mem_r

	T001_mem1 = S.Task('T001_mem1', length=1, delay_cost=1)
	S += T001_mem1 >= 76
	T001_mem1 += INPUT_mem_r

	T3111 = S.Task('T3111', length=1, delay_cost=1)
	S += T3111 >= 76
	T3111 += ADD[0]

	T001 = S.Task('T001', length=1, delay_cost=1)
	S += T001 >= 77
	T001 += ADD[0]

	T10101_mem0 = S.Task('T10101_mem0', length=1, delay_cost=1)
	S += T10101_mem0 >= 77
	T10101_mem0 += INPUT_mem_r

	T10101_mem1 = S.Task('T10101_mem1', length=1, delay_cost=1)
	S += T10101_mem1 >= 77
	T10101_mem1 += INPUT_mem_r

	T10100_mem0 = S.Task('T10100_mem0', length=1, delay_cost=1)
	S += T10100_mem0 >= 78
	T10100_mem0 += INPUT_mem_r

	T10100_mem1 = S.Task('T10100_mem1', length=1, delay_cost=1)
	S += T10100_mem1 >= 78
	T10100_mem1 += INPUT_mem_r

	T10101 = S.Task('T10101', length=1, delay_cost=1)
	S += T10101 >= 78
	T10101 += ADD[0]

	T10100 = S.Task('T10100', length=1, delay_cost=1)
	S += T10100 >= 79
	T10100 += ADD[0]

	T301_mem0 = S.Task('T301_mem0', length=1, delay_cost=1)
	S += T301_mem0 >= 79
	T301_mem0 += INPUT_mem_r

	T301_mem1 = S.Task('T301_mem1', length=1, delay_cost=1)
	S += T301_mem1 >= 79
	T301_mem1 += INPUT_mem_r

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	S += T200_mem0 >= 80
	T200_mem0 += INPUT_mem_r

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	S += T200_mem1 >= 80
	T200_mem1 += INPUT_mem_r

	T301 = S.Task('T301', length=1, delay_cost=1)
	S += T301 >= 80
	T301 += ADD[0]

	T0111_mem0 = S.Task('T0111_mem0', length=1, delay_cost=1)
	S += T0111_mem0 >= 81
	T0111_mem0 += INPUT_mem_r

	T0111_mem1 = S.Task('T0111_mem1', length=1, delay_cost=1)
	S += T0111_mem1 >= 81
	T0111_mem1 += INPUT_mem_r

	T200 = S.Task('T200', length=1, delay_cost=1)
	S += T200 >= 81
	T200 += ADD[0]

	T000_mem0 = S.Task('T000_mem0', length=1, delay_cost=1)
	S += T000_mem0 >= 82
	T000_mem0 += INPUT_mem_r

	T000_mem1 = S.Task('T000_mem1', length=1, delay_cost=1)
	S += T000_mem1 >= 82
	T000_mem1 += INPUT_mem_r

	T0111 = S.Task('T0111', length=1, delay_cost=1)
	S += T0111 >= 82
	T0111 += ADD[0]

	T000 = S.Task('T000', length=1, delay_cost=1)
	S += T000 >= 83
	T000 += ADD[0]



	# new tasks
	T0100 = S.Task('T0100', length=1, delay_cost=1)
	T0100 += alt(ADD)

	T0101 = S.Task('T0101', length=1, delay_cost=1)
	T0101 += alt(ADD)

	T6t3_0 = S.Task('T6t3_0', length=1, delay_cost=1)
	T6t3_0 += alt(ADD)

	T6t3_1 = S.Task('T6t3_1', length=1, delay_cost=1)
	T6t3_1 += alt(ADD)

	T6t3_a0b0 = S.Task('T6t3_a0b0', length=1, delay_cost=1)
	T6t3_a0b0 += alt(ADD)

	T6t0_a1b1_in = S.Task('T6t0_a1b1_in', length=1, delay_cost=1)
	T6t0_a1b1_in += alt(MUL_in)
	T6t0_a1b1 = S.Task('T6t0_a1b1', length=7, delay_cost=1)
	T6t0_a1b1 += alt(MUL)
	S+=T6t0_a1b1>=T6t0_a1b1_in

	T6t1_a1b1_in = S.Task('T6t1_a1b1_in', length=1, delay_cost=1)
	T6t1_a1b1_in += alt(MUL_in)
	T6t1_a1b1 = S.Task('T6t1_a1b1', length=7, delay_cost=1)
	T6t1_a1b1 += alt(MUL)
	S+=T6t1_a1b1>=T6t1_a1b1_in

	T6t2_a1b1 = S.Task('T6t2_a1b1', length=1, delay_cost=1)
	T6t2_a1b1 += alt(ADD)

	T6t3_a1b1 = S.Task('T6t3_a1b1', length=1, delay_cost=1)
	T6t3_a1b1 += alt(ADD)

	T7t2_0 = S.Task('T7t2_0', length=1, delay_cost=1)
	T7t2_0 += alt(ADD)

	T7t2_1 = S.Task('T7t2_1', length=1, delay_cost=1)
	T7t2_1 += alt(ADD)

	T7t3_0 = S.Task('T7t3_0', length=1, delay_cost=1)
	T7t3_0 += alt(ADD)

	T7t3_1 = S.Task('T7t3_1', length=1, delay_cost=1)
	T7t3_1 += alt(ADD)

	T7t0_a0b0_in = S.Task('T7t0_a0b0_in', length=1, delay_cost=1)
	T7t0_a0b0_in += alt(MUL_in)
	T7t0_a0b0 = S.Task('T7t0_a0b0', length=7, delay_cost=1)
	T7t0_a0b0 += alt(MUL)
	S+=T7t0_a0b0>=T7t0_a0b0_in

	T7t1_a0b0_in = S.Task('T7t1_a0b0_in', length=1, delay_cost=1)
	T7t1_a0b0_in += alt(MUL_in)
	T7t1_a0b0 = S.Task('T7t1_a0b0', length=7, delay_cost=1)
	T7t1_a0b0 += alt(MUL)
	S+=T7t1_a0b0>=T7t1_a0b0_in

	T7t2_a0b0 = S.Task('T7t2_a0b0', length=1, delay_cost=1)
	T7t2_a0b0 += alt(ADD)

	T7t3_a0b0 = S.Task('T7t3_a0b0', length=1, delay_cost=1)
	T7t3_a0b0 += alt(ADD)

	T7t0_a1b1_in = S.Task('T7t0_a1b1_in', length=1, delay_cost=1)
	T7t0_a1b1_in += alt(MUL_in)
	T7t0_a1b1 = S.Task('T7t0_a1b1', length=7, delay_cost=1)
	T7t0_a1b1 += alt(MUL)
	S+=T7t0_a1b1>=T7t0_a1b1_in

	T7t1_a1b1_in = S.Task('T7t1_a1b1_in', length=1, delay_cost=1)
	T7t1_a1b1_in += alt(MUL_in)
	T7t1_a1b1 = S.Task('T7t1_a1b1', length=7, delay_cost=1)
	T7t1_a1b1 += alt(MUL)
	S+=T7t1_a1b1>=T7t1_a1b1_in

	T7t2_a1b1 = S.Task('T7t2_a1b1', length=1, delay_cost=1)
	T7t2_a1b1 += alt(ADD)

	T7t3_a1b1 = S.Task('T7t3_a1b1', length=1, delay_cost=1)
	T7t3_a1b1 += alt(ADD)

	T8t2_0 = S.Task('T8t2_0', length=1, delay_cost=1)
	T8t2_0 += alt(ADD)

	T8t2_1 = S.Task('T8t2_1', length=1, delay_cost=1)
	T8t2_1 += alt(ADD)

	T8t3_0 = S.Task('T8t3_0', length=1, delay_cost=1)
	T8t3_0 += alt(ADD)

	T8t3_1 = S.Task('T8t3_1', length=1, delay_cost=1)
	T8t3_1 += alt(ADD)

	T8t0_a0b0_in = S.Task('T8t0_a0b0_in', length=1, delay_cost=1)
	T8t0_a0b0_in += alt(MUL_in)
	T8t0_a0b0 = S.Task('T8t0_a0b0', length=7, delay_cost=1)
	T8t0_a0b0 += alt(MUL)
	S+=T8t0_a0b0>=T8t0_a0b0_in

	T8t1_a0b0_in = S.Task('T8t1_a0b0_in', length=1, delay_cost=1)
	T8t1_a0b0_in += alt(MUL_in)
	T8t1_a0b0 = S.Task('T8t1_a0b0', length=7, delay_cost=1)
	T8t1_a0b0 += alt(MUL)
	S+=T8t1_a0b0>=T8t1_a0b0_in

	T8t2_a0b0 = S.Task('T8t2_a0b0', length=1, delay_cost=1)
	T8t2_a0b0 += alt(ADD)

	T8t3_a0b0 = S.Task('T8t3_a0b0', length=1, delay_cost=1)
	T8t3_a0b0 += alt(ADD)

	T8t0_a1b1_in = S.Task('T8t0_a1b1_in', length=1, delay_cost=1)
	T8t0_a1b1_in += alt(MUL_in)
	T8t0_a1b1 = S.Task('T8t0_a1b1', length=7, delay_cost=1)
	T8t0_a1b1 += alt(MUL)
	S+=T8t0_a1b1>=T8t0_a1b1_in

	T8t1_a1b1_in = S.Task('T8t1_a1b1_in', length=1, delay_cost=1)
	T8t1_a1b1_in += alt(MUL_in)
	T8t1_a1b1 = S.Task('T8t1_a1b1', length=7, delay_cost=1)
	T8t1_a1b1 += alt(MUL)
	S+=T8t1_a1b1>=T8t1_a1b1_in

	T8t2_a1b1 = S.Task('T8t2_a1b1', length=1, delay_cost=1)
	T8t2_a1b1 += alt(ADD)

	T8t3_a1b1 = S.Task('T8t3_a1b1', length=1, delay_cost=1)
	T8t3_a1b1 += alt(ADD)

	T910 = S.Task('T910', length=1, delay_cost=1)
	T910 += alt(ADD)

	T911 = S.Task('T911', length=1, delay_cost=1)
	T911 += alt(ADD)

	T1000 = S.Task('T1000', length=1, delay_cost=1)
	T1000 += alt(ADD)

	T1001 = S.Task('T1001', length=1, delay_cost=1)
	T1001 += alt(ADD)

	T1010 = S.Task('T1010', length=1, delay_cost=1)
	T1010 += alt(ADD)

	T1011 = S.Task('T1011', length=1, delay_cost=1)
	T1011 += alt(ADD)

	T1100 = S.Task('T1100', length=1, delay_cost=1)
	T1100 += alt(ADD)

	T1101 = S.Task('T1101', length=1, delay_cost=1)
	T1101 += alt(ADD)

	T1110 = S.Task('T1110', length=1, delay_cost=1)
	T1110 += alt(ADD)

	T1111 = S.Task('T1111', length=1, delay_cost=1)
	T1111 += alt(ADD)

	T4100 = S.Task('T4100', length=1, delay_cost=1)
	T4100 += alt(ADD)

	T4101 = S.Task('T4101', length=1, delay_cost=1)
	T4101 += alt(ADD)

	T4110 = S.Task('T4110', length=1, delay_cost=1)
	T4110 += alt(ADD)

	T4111 = S.Task('T4111', length=1, delay_cost=1)
	T4111 += alt(ADD)

	T2110 = S.Task('T2110', length=1, delay_cost=1)
	T2110 += alt(ADD)

	T2111 = S.Task('T2111', length=1, delay_cost=1)
	T2111 += alt(ADD)

	T5100 = S.Task('T5100', length=1, delay_cost=1)
	T5100 += alt(ADD)

	T5101 = S.Task('T5101', length=1, delay_cost=1)
	T5101 += alt(ADD)

	T5110 = S.Task('T5110', length=1, delay_cost=1)
	T5110 += alt(ADD)

	T5111 = S.Task('T5111', length=1, delay_cost=1)
	T5111 += alt(ADD)

	T61t4_a0b0_in = S.Task('T61t4_a0b0_in', length=1, delay_cost=1)
	T61t4_a0b0_in += alt(MUL_in)
	T61t4_a0b0 = S.Task('T61t4_a0b0', length=7, delay_cost=1)
	T61t4_a0b0 += alt(MUL)
	S+=T61t4_a0b0>=T61t4_a0b0_in

	T61c0_a0b0 = S.Task('T61c0_a0b0', length=1, delay_cost=1)
	T61c0_a0b0 += alt(ADD)

	T61t6_a0b0 = S.Task('T61t6_a0b0', length=1, delay_cost=1)
	T61t6_a0b0 += alt(ADD)

	T61t4_a1b1_in = S.Task('T61t4_a1b1_in', length=1, delay_cost=1)
	T61t4_a1b1_in += alt(MUL_in)
	T61t4_a1b1 = S.Task('T61t4_a1b1', length=7, delay_cost=1)
	T61t4_a1b1 += alt(MUL)
	S+=T61t4_a1b1>=T61t4_a1b1_in

	T61c0_a1b1 = S.Task('T61c0_a1b1', length=1, delay_cost=1)
	T61c0_a1b1 += alt(ADD)

	T61t6_a1b1 = S.Task('T61t6_a1b1', length=1, delay_cost=1)
	T61t6_a1b1 += alt(ADD)

	T61t0_t2t3_in = S.Task('T61t0_t2t3_in', length=1, delay_cost=1)
	T61t0_t2t3_in += alt(MUL_in)
	T61t0_t2t3 = S.Task('T61t0_t2t3', length=7, delay_cost=1)
	T61t0_t2t3 += alt(MUL)
	S+=T61t0_t2t3>=T61t0_t2t3_in

	T61t1_t2t3_in = S.Task('T61t1_t2t3_in', length=1, delay_cost=1)
	T61t1_t2t3_in += alt(MUL_in)
	T61t1_t2t3 = S.Task('T61t1_t2t3', length=7, delay_cost=1)
	T61t1_t2t3 += alt(MUL)
	S+=T61t1_t2t3>=T61t1_t2t3_in

	T61t2_t2t3 = S.Task('T61t2_t2t3', length=1, delay_cost=1)
	T61t2_t2t3 += alt(ADD)

	T61t3_t2t3 = S.Task('T61t3_t2t3', length=1, delay_cost=1)
	T61t3_t2t3 += alt(ADD)

	T71t4_a0b0_in = S.Task('T71t4_a0b0_in', length=1, delay_cost=1)
	T71t4_a0b0_in += alt(MUL_in)
	T71t4_a0b0 = S.Task('T71t4_a0b0', length=7, delay_cost=1)
	T71t4_a0b0 += alt(MUL)
	S+=T71t4_a0b0>=T71t4_a0b0_in

	T71c0_a0b0 = S.Task('T71c0_a0b0', length=1, delay_cost=1)
	T71c0_a0b0 += alt(ADD)

	T71t6_a0b0 = S.Task('T71t6_a0b0', length=1, delay_cost=1)
	T71t6_a0b0 += alt(ADD)

	T71t4_a1b1_in = S.Task('T71t4_a1b1_in', length=1, delay_cost=1)
	T71t4_a1b1_in += alt(MUL_in)
	T71t4_a1b1 = S.Task('T71t4_a1b1', length=7, delay_cost=1)
	T71t4_a1b1 += alt(MUL)
	S+=T71t4_a1b1>=T71t4_a1b1_in

	T71c0_a1b1 = S.Task('T71c0_a1b1', length=1, delay_cost=1)
	T71c0_a1b1 += alt(ADD)

	T71t6_a1b1 = S.Task('T71t6_a1b1', length=1, delay_cost=1)
	T71t6_a1b1 += alt(ADD)

	T71t0_t2t3_in = S.Task('T71t0_t2t3_in', length=1, delay_cost=1)
	T71t0_t2t3_in += alt(MUL_in)
	T71t0_t2t3 = S.Task('T71t0_t2t3', length=7, delay_cost=1)
	T71t0_t2t3 += alt(MUL)
	S+=T71t0_t2t3>=T71t0_t2t3_in

	T71t1_t2t3_in = S.Task('T71t1_t2t3_in', length=1, delay_cost=1)
	T71t1_t2t3_in += alt(MUL_in)
	T71t1_t2t3 = S.Task('T71t1_t2t3', length=7, delay_cost=1)
	T71t1_t2t3 += alt(MUL)
	S+=T71t1_t2t3>=T71t1_t2t3_in

	T71t2_t2t3 = S.Task('T71t2_t2t3', length=1, delay_cost=1)
	T71t2_t2t3 += alt(ADD)

	T71t3_t2t3 = S.Task('T71t3_t2t3', length=1, delay_cost=1)
	T71t3_t2t3 += alt(ADD)

	T82t4_a0b0_in = S.Task('T82t4_a0b0_in', length=1, delay_cost=1)
	T82t4_a0b0_in += alt(MUL_in)
	T82t4_a0b0 = S.Task('T82t4_a0b0', length=7, delay_cost=1)
	T82t4_a0b0 += alt(MUL)
	S+=T82t4_a0b0>=T82t4_a0b0_in

	T82c0_a0b0 = S.Task('T82c0_a0b0', length=1, delay_cost=1)
	T82c0_a0b0 += alt(ADD)

	T82t6_a0b0 = S.Task('T82t6_a0b0', length=1, delay_cost=1)
	T82t6_a0b0 += alt(ADD)

	T82t4_a1b1_in = S.Task('T82t4_a1b1_in', length=1, delay_cost=1)
	T82t4_a1b1_in += alt(MUL_in)
	T82t4_a1b1 = S.Task('T82t4_a1b1', length=7, delay_cost=1)
	T82t4_a1b1 += alt(MUL)
	S+=T82t4_a1b1>=T82t4_a1b1_in

	T82c0_a1b1 = S.Task('T82c0_a1b1', length=1, delay_cost=1)
	T82c0_a1b1 += alt(ADD)

	T82t6_a1b1 = S.Task('T82t6_a1b1', length=1, delay_cost=1)
	T82t6_a1b1 += alt(ADD)

	T82t0_t2t3_in = S.Task('T82t0_t2t3_in', length=1, delay_cost=1)
	T82t0_t2t3_in += alt(MUL_in)
	T82t0_t2t3 = S.Task('T82t0_t2t3', length=7, delay_cost=1)
	T82t0_t2t3 += alt(MUL)
	S+=T82t0_t2t3>=T82t0_t2t3_in

	T82t1_t2t3_in = S.Task('T82t1_t2t3_in', length=1, delay_cost=1)
	T82t1_t2t3_in += alt(MUL_in)
	T82t1_t2t3 = S.Task('T82t1_t2t3', length=7, delay_cost=1)
	T82t1_t2t3 += alt(MUL)
	S+=T82t1_t2t3>=T82t1_t2t3_in

	T82t2_t2t3 = S.Task('T82t2_t2t3', length=1, delay_cost=1)
	T82t2_t2t3 += alt(ADD)

	T82t3_t2t3 = S.Task('T82t3_t2t3', length=1, delay_cost=1)
	T82t3_t2t3 += alt(ADD)

	T95t2_0 = S.Task('T95t2_0', length=1, delay_cost=1)
	T95t2_0 += alt(ADD)

	T95t2_1 = S.Task('T95t2_1', length=1, delay_cost=1)
	T95t2_1 += alt(ADD)

	T95t3_0 = S.Task('T95t3_0', length=1, delay_cost=1)
	T95t3_0 += alt(ADD)

	T95t3_1 = S.Task('T95t3_1', length=1, delay_cost=1)
	T95t3_1 += alt(ADD)

	T95t0_a0b0_in = S.Task('T95t0_a0b0_in', length=1, delay_cost=1)
	T95t0_a0b0_in += alt(MUL_in)
	T95t0_a0b0 = S.Task('T95t0_a0b0', length=7, delay_cost=1)
	T95t0_a0b0 += alt(MUL)
	S+=T95t0_a0b0>=T95t0_a0b0_in

	T95t1_a0b0_in = S.Task('T95t1_a0b0_in', length=1, delay_cost=1)
	T95t1_a0b0_in += alt(MUL_in)
	T95t1_a0b0 = S.Task('T95t1_a0b0', length=7, delay_cost=1)
	T95t1_a0b0 += alt(MUL)
	S+=T95t1_a0b0>=T95t1_a0b0_in

	T95t2_a0b0 = S.Task('T95t2_a0b0', length=1, delay_cost=1)
	T95t2_a0b0 += alt(ADD)

	T95t3_a0b0 = S.Task('T95t3_a0b0', length=1, delay_cost=1)
	T95t3_a0b0 += alt(ADD)

	T95t0_a1b1_in = S.Task('T95t0_a1b1_in', length=1, delay_cost=1)
	T95t0_a1b1_in += alt(MUL_in)
	T95t0_a1b1 = S.Task('T95t0_a1b1', length=7, delay_cost=1)
	T95t0_a1b1 += alt(MUL)
	S+=T95t0_a1b1>=T95t0_a1b1_in

	T95t1_a1b1_in = S.Task('T95t1_a1b1_in', length=1, delay_cost=1)
	T95t1_a1b1_in += alt(MUL_in)
	T95t1_a1b1 = S.Task('T95t1_a1b1', length=7, delay_cost=1)
	T95t1_a1b1 += alt(MUL)
	S+=T95t1_a1b1>=T95t1_a1b1_in

	T95t2_a1b1 = S.Task('T95t2_a1b1', length=1, delay_cost=1)
	T95t2_a1b1 += alt(ADD)

	T95t3_a1b1 = S.Task('T95t3_a1b1', length=1, delay_cost=1)
	T95t3_a1b1 += alt(ADD)

	T32t2_0 = S.Task('T32t2_0', length=1, delay_cost=1)
	T32t2_0 += alt(ADD)

	T32t2_1 = S.Task('T32t2_1', length=1, delay_cost=1)
	T32t2_1 += alt(ADD)

	T32t3_0 = S.Task('T32t3_0', length=1, delay_cost=1)
	T32t3_0 += alt(ADD)

	T32t3_1 = S.Task('T32t3_1', length=1, delay_cost=1)
	T32t3_1 += alt(ADD)

	T32t0_a0b0_in = S.Task('T32t0_a0b0_in', length=1, delay_cost=1)
	T32t0_a0b0_in += alt(MUL_in)
	T32t0_a0b0 = S.Task('T32t0_a0b0', length=7, delay_cost=1)
	T32t0_a0b0 += alt(MUL)
	S+=T32t0_a0b0>=T32t0_a0b0_in

	T32t1_a0b0_in = S.Task('T32t1_a0b0_in', length=1, delay_cost=1)
	T32t1_a0b0_in += alt(MUL_in)
	T32t1_a0b0 = S.Task('T32t1_a0b0', length=7, delay_cost=1)
	T32t1_a0b0 += alt(MUL)
	S+=T32t1_a0b0>=T32t1_a0b0_in

	T32t2_a0b0 = S.Task('T32t2_a0b0', length=1, delay_cost=1)
	T32t2_a0b0 += alt(ADD)

	T32t3_a0b0 = S.Task('T32t3_a0b0', length=1, delay_cost=1)
	T32t3_a0b0 += alt(ADD)

	T32t0_a1b1_in = S.Task('T32t0_a1b1_in', length=1, delay_cost=1)
	T32t0_a1b1_in += alt(MUL_in)
	T32t0_a1b1 = S.Task('T32t0_a1b1', length=7, delay_cost=1)
	T32t0_a1b1 += alt(MUL)
	S+=T32t0_a1b1>=T32t0_a1b1_in

	T32t1_a1b1_in = S.Task('T32t1_a1b1_in', length=1, delay_cost=1)
	T32t1_a1b1_in += alt(MUL_in)
	T32t1_a1b1 = S.Task('T32t1_a1b1', length=7, delay_cost=1)
	T32t1_a1b1 += alt(MUL)
	S+=T32t1_a1b1>=T32t1_a1b1_in

	T32t2_a1b1 = S.Task('T32t2_a1b1', length=1, delay_cost=1)
	T32t2_a1b1 += alt(ADD)

	T32t3_a1b1 = S.Task('T32t3_a1b1', length=1, delay_cost=1)
	T32t3_a1b1 += alt(ADD)

	T44t2_0 = S.Task('T44t2_0', length=1, delay_cost=1)
	T44t2_0 += alt(ADD)

	T44t2_1 = S.Task('T44t2_1', length=1, delay_cost=1)
	T44t2_1 += alt(ADD)

	T44t3_0 = S.Task('T44t3_0', length=1, delay_cost=1)
	T44t3_0 += alt(ADD)

	T44t3_1 = S.Task('T44t3_1', length=1, delay_cost=1)
	T44t3_1 += alt(ADD)

	T44t0_a0b0_in = S.Task('T44t0_a0b0_in', length=1, delay_cost=1)
	T44t0_a0b0_in += alt(MUL_in)
	T44t0_a0b0 = S.Task('T44t0_a0b0', length=7, delay_cost=1)
	T44t0_a0b0 += alt(MUL)
	S+=T44t0_a0b0>=T44t0_a0b0_in

	T44t1_a0b0_in = S.Task('T44t1_a0b0_in', length=1, delay_cost=1)
	T44t1_a0b0_in += alt(MUL_in)
	T44t1_a0b0 = S.Task('T44t1_a0b0', length=7, delay_cost=1)
	T44t1_a0b0 += alt(MUL)
	S+=T44t1_a0b0>=T44t1_a0b0_in

	T44t2_a0b0 = S.Task('T44t2_a0b0', length=1, delay_cost=1)
	T44t2_a0b0 += alt(ADD)

	T44t3_a0b0 = S.Task('T44t3_a0b0', length=1, delay_cost=1)
	T44t3_a0b0 += alt(ADD)

	T44t0_a1b1_in = S.Task('T44t0_a1b1_in', length=1, delay_cost=1)
	T44t0_a1b1_in += alt(MUL_in)
	T44t0_a1b1 = S.Task('T44t0_a1b1', length=7, delay_cost=1)
	T44t0_a1b1 += alt(MUL)
	S+=T44t0_a1b1>=T44t0_a1b1_in

	T44t1_a1b1_in = S.Task('T44t1_a1b1_in', length=1, delay_cost=1)
	T44t1_a1b1_in += alt(MUL_in)
	T44t1_a1b1 = S.Task('T44t1_a1b1', length=7, delay_cost=1)
	T44t1_a1b1 += alt(MUL)
	S+=T44t1_a1b1>=T44t1_a1b1_in

	T44t2_a1b1 = S.Task('T44t2_a1b1', length=1, delay_cost=1)
	T44t2_a1b1 += alt(ADD)

	T44t3_a1b1 = S.Task('T44t3_a1b1', length=1, delay_cost=1)
	T44t3_a1b1 += alt(ADD)

	T0100_mem0 = S.Task('T0100_mem0', length=1, delay_cost=1)
	T0100_mem0 += INPUT_mem_r
	S += T0100_mem0<=T0100

	T0100_mem1 = S.Task('T0100_mem1', length=1, delay_cost=1)
	T0100_mem1 += ADD_mem[0]
	S += 83<T0100_mem1
	S += T0100_mem1<=T0100

	T0101_mem0 = S.Task('T0101_mem0', length=1, delay_cost=1)
	T0101_mem0 += INPUT_mem_r
	S += T0101_mem0<=T0101

	T0101_mem1 = S.Task('T0101_mem1', length=1, delay_cost=1)
	T0101_mem1 += ADD_mem[0]
	S += 77<T0101_mem1
	S += T0101_mem1<=T0101

	T6t3_0_mem0 = S.Task('T6t3_0_mem0', length=1, delay_cost=1)
	T6t3_0_mem0 += ADD_mem[1]
	S += 28<T6t3_0_mem0
	S += T6t3_0_mem0<=T6t3_0

	T6t3_0_mem1 = S.Task('T6t3_0_mem1', length=1, delay_cost=1)
	T6t3_0_mem1 += ADD_mem[0]
	S += 68<T6t3_0_mem1
	S += T6t3_0_mem1<=T6t3_0

	T6t3_1_mem0 = S.Task('T6t3_1_mem0', length=1, delay_cost=1)
	T6t3_1_mem0 += ADD_mem[0]
	S += 80<T6t3_1_mem0
	S += T6t3_1_mem0<=T6t3_1

	T6t3_1_mem1 = S.Task('T6t3_1_mem1', length=1, delay_cost=1)
	T6t3_1_mem1 += ADD_mem[2]
	S += 63<T6t3_1_mem1
	S += T6t3_1_mem1<=T6t3_1

	T6t3_a0b0_mem0 = S.Task('T6t3_a0b0_mem0', length=1, delay_cost=1)
	T6t3_a0b0_mem0 += ADD_mem[1]
	S += 28<T6t3_a0b0_mem0
	S += T6t3_a0b0_mem0<=T6t3_a0b0

	T6t3_a0b0_mem1 = S.Task('T6t3_a0b0_mem1', length=1, delay_cost=1)
	T6t3_a0b0_mem1 += ADD_mem[0]
	S += 80<T6t3_a0b0_mem1
	S += T6t3_a0b0_mem1<=T6t3_a0b0

	T6t0_a1b1_mem0 = S.Task('T6t0_a1b1_mem0', length=1, delay_cost=1)
	T6t0_a1b1_mem0 += ADD_mem[3]
	S += 30<T6t0_a1b1_mem0
	S += T6t0_a1b1_mem0<=T6t0_a1b1

	T6t0_a1b1_mem1 = S.Task('T6t0_a1b1_mem1', length=1, delay_cost=1)
	T6t0_a1b1_mem1 += ADD_mem[0]
	S += 68<T6t0_a1b1_mem1
	S += T6t0_a1b1_mem1<=T6t0_a1b1

	T6t1_a1b1_mem0 = S.Task('T6t1_a1b1_mem0', length=1, delay_cost=1)
	T6t1_a1b1_mem0 += ADD_mem[0]
	S += 82<T6t1_a1b1_mem0
	S += T6t1_a1b1_mem0<=T6t1_a1b1

	T6t1_a1b1_mem1 = S.Task('T6t1_a1b1_mem1', length=1, delay_cost=1)
	T6t1_a1b1_mem1 += ADD_mem[2]
	S += 63<T6t1_a1b1_mem1
	S += T6t1_a1b1_mem1<=T6t1_a1b1

	T6t2_a1b1_mem0 = S.Task('T6t2_a1b1_mem0', length=1, delay_cost=1)
	T6t2_a1b1_mem0 += ADD_mem[3]
	S += 30<T6t2_a1b1_mem0
	S += T6t2_a1b1_mem0<=T6t2_a1b1

	T6t2_a1b1_mem1 = S.Task('T6t2_a1b1_mem1', length=1, delay_cost=1)
	T6t2_a1b1_mem1 += ADD_mem[0]
	S += 82<T6t2_a1b1_mem1
	S += T6t2_a1b1_mem1<=T6t2_a1b1

	T6t3_a1b1_mem0 = S.Task('T6t3_a1b1_mem0', length=1, delay_cost=1)
	T6t3_a1b1_mem0 += ADD_mem[0]
	S += 68<T6t3_a1b1_mem0
	S += T6t3_a1b1_mem0<=T6t3_a1b1

	T6t3_a1b1_mem1 = S.Task('T6t3_a1b1_mem1', length=1, delay_cost=1)
	T6t3_a1b1_mem1 += ADD_mem[2]
	S += 63<T6t3_a1b1_mem1
	S += T6t3_a1b1_mem1<=T6t3_a1b1

	T7t2_0_mem0 = S.Task('T7t2_0_mem0', length=1, delay_cost=1)
	T7t2_0_mem0 += ADD_mem[0]
	S += 72<T7t2_0_mem0
	S += T7t2_0_mem0<=T7t2_0

	T7t2_0_mem1 = S.Task('T7t2_0_mem1', length=1, delay_cost=1)
	T7t2_0_mem1 += ADD_mem[0]
	S += 64<T7t2_0_mem1
	S += T7t2_0_mem1<=T7t2_0

	T7t2_1_mem0 = S.Task('T7t2_1_mem0', length=1, delay_cost=1)
	T7t2_1_mem0 += ADD_mem[1]
	S += 66<T7t2_1_mem0
	S += T7t2_1_mem0<=T7t2_1

	T7t2_1_mem1 = S.Task('T7t2_1_mem1', length=1, delay_cost=1)
	T7t2_1_mem1 += ADD_mem[1]
	S += 74<T7t2_1_mem1
	S += T7t2_1_mem1<=T7t2_1

	T7t3_0_mem0 = S.Task('T7t3_0_mem0', length=1, delay_cost=1)
	T7t3_0_mem0 += ADD_mem[0]
	S += 67<T7t3_0_mem0
	S += T7t3_0_mem0<=T7t3_0

	T7t3_0_mem1 = S.Task('T7t3_0_mem1', length=1, delay_cost=1)
	T7t3_0_mem1 += ADD_mem[1]
	S += 48<T7t3_0_mem1
	S += T7t3_0_mem1<=T7t3_0

	T7t3_1_mem0 = S.Task('T7t3_1_mem0', length=1, delay_cost=1)
	T7t3_1_mem0 += ADD_mem[1]
	S += 57<T7t3_1_mem0
	S += T7t3_1_mem0<=T7t3_1

	T7t3_1_mem1 = S.Task('T7t3_1_mem1', length=1, delay_cost=1)
	T7t3_1_mem1 += ADD_mem[0]
	S += 24<T7t3_1_mem1
	S += T7t3_1_mem1<=T7t3_1

	T7t0_a0b0_mem0 = S.Task('T7t0_a0b0_mem0', length=1, delay_cost=1)
	T7t0_a0b0_mem0 += ADD_mem[0]
	S += 72<T7t0_a0b0_mem0
	S += T7t0_a0b0_mem0<=T7t0_a0b0

	T7t0_a0b0_mem1 = S.Task('T7t0_a0b0_mem1', length=1, delay_cost=1)
	T7t0_a0b0_mem1 += ADD_mem[0]
	S += 67<T7t0_a0b0_mem1
	S += T7t0_a0b0_mem1<=T7t0_a0b0

	T7t1_a0b0_mem0 = S.Task('T7t1_a0b0_mem0', length=1, delay_cost=1)
	T7t1_a0b0_mem0 += ADD_mem[1]
	S += 66<T7t1_a0b0_mem0
	S += T7t1_a0b0_mem0<=T7t1_a0b0

	T7t1_a0b0_mem1 = S.Task('T7t1_a0b0_mem1', length=1, delay_cost=1)
	T7t1_a0b0_mem1 += ADD_mem[1]
	S += 57<T7t1_a0b0_mem1
	S += T7t1_a0b0_mem1<=T7t1_a0b0

	T7t2_a0b0_mem0 = S.Task('T7t2_a0b0_mem0', length=1, delay_cost=1)
	T7t2_a0b0_mem0 += ADD_mem[0]
	S += 72<T7t2_a0b0_mem0
	S += T7t2_a0b0_mem0<=T7t2_a0b0

	T7t2_a0b0_mem1 = S.Task('T7t2_a0b0_mem1', length=1, delay_cost=1)
	T7t2_a0b0_mem1 += ADD_mem[1]
	S += 66<T7t2_a0b0_mem1
	S += T7t2_a0b0_mem1<=T7t2_a0b0

	T7t3_a0b0_mem0 = S.Task('T7t3_a0b0_mem0', length=1, delay_cost=1)
	T7t3_a0b0_mem0 += ADD_mem[0]
	S += 67<T7t3_a0b0_mem0
	S += T7t3_a0b0_mem0<=T7t3_a0b0

	T7t3_a0b0_mem1 = S.Task('T7t3_a0b0_mem1', length=1, delay_cost=1)
	T7t3_a0b0_mem1 += ADD_mem[1]
	S += 57<T7t3_a0b0_mem1
	S += T7t3_a0b0_mem1<=T7t3_a0b0

	T7t0_a1b1_mem0 = S.Task('T7t0_a1b1_mem0', length=1, delay_cost=1)
	T7t0_a1b1_mem0 += ADD_mem[0]
	S += 64<T7t0_a1b1_mem0
	S += T7t0_a1b1_mem0<=T7t0_a1b1

	T7t0_a1b1_mem1 = S.Task('T7t0_a1b1_mem1', length=1, delay_cost=1)
	T7t0_a1b1_mem1 += ADD_mem[1]
	S += 48<T7t0_a1b1_mem1
	S += T7t0_a1b1_mem1<=T7t0_a1b1

	T7t1_a1b1_mem0 = S.Task('T7t1_a1b1_mem0', length=1, delay_cost=1)
	T7t1_a1b1_mem0 += ADD_mem[1]
	S += 74<T7t1_a1b1_mem0
	S += T7t1_a1b1_mem0<=T7t1_a1b1

	T7t1_a1b1_mem1 = S.Task('T7t1_a1b1_mem1', length=1, delay_cost=1)
	T7t1_a1b1_mem1 += ADD_mem[0]
	S += 24<T7t1_a1b1_mem1
	S += T7t1_a1b1_mem1<=T7t1_a1b1

	T7t2_a1b1_mem0 = S.Task('T7t2_a1b1_mem0', length=1, delay_cost=1)
	T7t2_a1b1_mem0 += ADD_mem[0]
	S += 64<T7t2_a1b1_mem0
	S += T7t2_a1b1_mem0<=T7t2_a1b1

	T7t2_a1b1_mem1 = S.Task('T7t2_a1b1_mem1', length=1, delay_cost=1)
	T7t2_a1b1_mem1 += ADD_mem[1]
	S += 74<T7t2_a1b1_mem1
	S += T7t2_a1b1_mem1<=T7t2_a1b1

	T7t3_a1b1_mem0 = S.Task('T7t3_a1b1_mem0', length=1, delay_cost=1)
	T7t3_a1b1_mem0 += ADD_mem[1]
	S += 48<T7t3_a1b1_mem0
	S += T7t3_a1b1_mem0<=T7t3_a1b1

	T7t3_a1b1_mem1 = S.Task('T7t3_a1b1_mem1', length=1, delay_cost=1)
	T7t3_a1b1_mem1 += ADD_mem[0]
	S += 24<T7t3_a1b1_mem1
	S += T7t3_a1b1_mem1<=T7t3_a1b1

	T8t2_0_mem0 = S.Task('T8t2_0_mem0', length=1, delay_cost=1)
	T8t2_0_mem0 += ADD_mem[0]
	S += 81<T8t2_0_mem0
	S += T8t2_0_mem0<=T8t2_0

	T8t2_0_mem1 = S.Task('T8t2_0_mem1', length=1, delay_cost=1)
	T8t2_0_mem1 += ADD_mem[2]
	S += 61<T8t2_0_mem1
	S += T8t2_0_mem1<=T8t2_0

	T8t2_1_mem0 = S.Task('T8t2_1_mem0', length=1, delay_cost=1)
	T8t2_1_mem0 += ADD_mem[1]
	S += 45<T8t2_1_mem0
	S += T8t2_1_mem0<=T8t2_1

	T8t2_1_mem1 = S.Task('T8t2_1_mem1', length=1, delay_cost=1)
	T8t2_1_mem1 += ADD_mem[0]
	S += 32<T8t2_1_mem1
	S += T8t2_1_mem1<=T8t2_1

	T8t3_0_mem0 = S.Task('T8t3_0_mem0', length=1, delay_cost=1)
	T8t3_0_mem0 += ADD_mem[0]
	S += 38<T8t3_0_mem0
	S += T8t3_0_mem0<=T8t3_0

	T8t3_0_mem1 = S.Task('T8t3_0_mem1', length=1, delay_cost=1)
	T8t3_0_mem1 += ADD_mem[1]
	S += 26<T8t3_0_mem1
	S += T8t3_0_mem1<=T8t3_0

	T8t3_1_mem0 = S.Task('T8t3_1_mem0', length=1, delay_cost=1)
	T8t3_1_mem0 += ADD_mem[0]
	S += 44<T8t3_1_mem0
	S += T8t3_1_mem0<=T8t3_1

	T8t3_1_mem1 = S.Task('T8t3_1_mem1', length=1, delay_cost=1)
	T8t3_1_mem1 += ADD_mem[0]
	S += 25<T8t3_1_mem1
	S += T8t3_1_mem1<=T8t3_1

	T8t0_a0b0_mem0 = S.Task('T8t0_a0b0_mem0', length=1, delay_cost=1)
	T8t0_a0b0_mem0 += ADD_mem[0]
	S += 81<T8t0_a0b0_mem0
	S += T8t0_a0b0_mem0<=T8t0_a0b0

	T8t0_a0b0_mem1 = S.Task('T8t0_a0b0_mem1', length=1, delay_cost=1)
	T8t0_a0b0_mem1 += ADD_mem[0]
	S += 38<T8t0_a0b0_mem1
	S += T8t0_a0b0_mem1<=T8t0_a0b0

	T8t1_a0b0_mem0 = S.Task('T8t1_a0b0_mem0', length=1, delay_cost=1)
	T8t1_a0b0_mem0 += ADD_mem[1]
	S += 45<T8t1_a0b0_mem0
	S += T8t1_a0b0_mem0<=T8t1_a0b0

	T8t1_a0b0_mem1 = S.Task('T8t1_a0b0_mem1', length=1, delay_cost=1)
	T8t1_a0b0_mem1 += ADD_mem[0]
	S += 44<T8t1_a0b0_mem1
	S += T8t1_a0b0_mem1<=T8t1_a0b0

	T8t2_a0b0_mem0 = S.Task('T8t2_a0b0_mem0', length=1, delay_cost=1)
	T8t2_a0b0_mem0 += ADD_mem[0]
	S += 81<T8t2_a0b0_mem0
	S += T8t2_a0b0_mem0<=T8t2_a0b0

	T8t2_a0b0_mem1 = S.Task('T8t2_a0b0_mem1', length=1, delay_cost=1)
	T8t2_a0b0_mem1 += ADD_mem[1]
	S += 45<T8t2_a0b0_mem1
	S += T8t2_a0b0_mem1<=T8t2_a0b0

	T8t3_a0b0_mem0 = S.Task('T8t3_a0b0_mem0', length=1, delay_cost=1)
	T8t3_a0b0_mem0 += ADD_mem[0]
	S += 38<T8t3_a0b0_mem0
	S += T8t3_a0b0_mem0<=T8t3_a0b0

	T8t3_a0b0_mem1 = S.Task('T8t3_a0b0_mem1', length=1, delay_cost=1)
	T8t3_a0b0_mem1 += ADD_mem[0]
	S += 44<T8t3_a0b0_mem1
	S += T8t3_a0b0_mem1<=T8t3_a0b0

	T8t0_a1b1_mem0 = S.Task('T8t0_a1b1_mem0', length=1, delay_cost=1)
	T8t0_a1b1_mem0 += ADD_mem[2]
	S += 61<T8t0_a1b1_mem0
	S += T8t0_a1b1_mem0<=T8t0_a1b1

	T8t0_a1b1_mem1 = S.Task('T8t0_a1b1_mem1', length=1, delay_cost=1)
	T8t0_a1b1_mem1 += ADD_mem[1]
	S += 26<T8t0_a1b1_mem1
	S += T8t0_a1b1_mem1<=T8t0_a1b1

	T8t1_a1b1_mem0 = S.Task('T8t1_a1b1_mem0', length=1, delay_cost=1)
	T8t1_a1b1_mem0 += ADD_mem[0]
	S += 32<T8t1_a1b1_mem0
	S += T8t1_a1b1_mem0<=T8t1_a1b1

	T8t1_a1b1_mem1 = S.Task('T8t1_a1b1_mem1', length=1, delay_cost=1)
	T8t1_a1b1_mem1 += ADD_mem[0]
	S += 25<T8t1_a1b1_mem1
	S += T8t1_a1b1_mem1<=T8t1_a1b1

	T8t2_a1b1_mem0 = S.Task('T8t2_a1b1_mem0', length=1, delay_cost=1)
	T8t2_a1b1_mem0 += ADD_mem[2]
	S += 61<T8t2_a1b1_mem0
	S += T8t2_a1b1_mem0<=T8t2_a1b1

	T8t2_a1b1_mem1 = S.Task('T8t2_a1b1_mem1', length=1, delay_cost=1)
	T8t2_a1b1_mem1 += ADD_mem[0]
	S += 32<T8t2_a1b1_mem1
	S += T8t2_a1b1_mem1<=T8t2_a1b1

	T8t3_a1b1_mem0 = S.Task('T8t3_a1b1_mem0', length=1, delay_cost=1)
	T8t3_a1b1_mem0 += ADD_mem[1]
	S += 26<T8t3_a1b1_mem0
	S += T8t3_a1b1_mem0<=T8t3_a1b1

	T8t3_a1b1_mem1 = S.Task('T8t3_a1b1_mem1', length=1, delay_cost=1)
	T8t3_a1b1_mem1 += ADD_mem[0]
	S += 25<T8t3_a1b1_mem1
	S += T8t3_a1b1_mem1<=T8t3_a1b1

	T910_mem0 = S.Task('T910_mem0', length=1, delay_cost=1)
	T910_mem0 += ADD_mem[3]
	S += 30<T910_mem0
	S += T910_mem0<=T910

	T910_mem1 = S.Task('T910_mem1', length=1, delay_cost=1)
	T910_mem1 += ADD_mem[0]
	S += 64<T910_mem1
	S += T910_mem1<=T910

	T911_mem0 = S.Task('T911_mem0', length=1, delay_cost=1)
	T911_mem0 += ADD_mem[0]
	S += 82<T911_mem0
	S += T911_mem0<=T911

	T911_mem1 = S.Task('T911_mem1', length=1, delay_cost=1)
	T911_mem1 += ADD_mem[1]
	S += 74<T911_mem1
	S += T911_mem1<=T911

	T1000_mem0 = S.Task('T1000_mem0', length=1, delay_cost=1)
	T1000_mem0 += ADD_mem[1]
	S += 28<T1000_mem0
	S += T1000_mem0<=T1000

	T1000_mem1 = S.Task('T1000_mem1', length=1, delay_cost=1)
	T1000_mem1 += ADD_mem[0]
	S += 67<T1000_mem1
	S += T1000_mem1<=T1000

	T1001_mem0 = S.Task('T1001_mem0', length=1, delay_cost=1)
	T1001_mem0 += ADD_mem[0]
	S += 80<T1001_mem0
	S += T1001_mem0<=T1001

	T1001_mem1 = S.Task('T1001_mem1', length=1, delay_cost=1)
	T1001_mem1 += ADD_mem[1]
	S += 57<T1001_mem1
	S += T1001_mem1<=T1001

	T1010_mem0 = S.Task('T1010_mem0', length=1, delay_cost=1)
	T1010_mem0 += ADD_mem[0]
	S += 68<T1010_mem0
	S += T1010_mem0<=T1010

	T1010_mem1 = S.Task('T1010_mem1', length=1, delay_cost=1)
	T1010_mem1 += ADD_mem[1]
	S += 48<T1010_mem1
	S += T1010_mem1<=T1010

	T1011_mem0 = S.Task('T1011_mem0', length=1, delay_cost=1)
	T1011_mem0 += ADD_mem[2]
	S += 63<T1011_mem0
	S += T1011_mem0<=T1011

	T1011_mem1 = S.Task('T1011_mem1', length=1, delay_cost=1)
	T1011_mem1 += ADD_mem[0]
	S += 24<T1011_mem1
	S += T1011_mem1<=T1011

	T1100_mem0 = S.Task('T1100_mem0', length=1, delay_cost=1)
	T1100_mem0 += ADD_mem[0]
	S += 72<T1100_mem0
	S += T1100_mem0<=T1100

	T1100_mem1 = S.Task('T1100_mem1', length=1, delay_cost=1)
	T1100_mem1 += ADD_mem[0]
	S += 81<T1100_mem1
	S += T1100_mem1<=T1100

	T1101_mem0 = S.Task('T1101_mem0', length=1, delay_cost=1)
	T1101_mem0 += ADD_mem[1]
	S += 66<T1101_mem0
	S += T1101_mem0<=T1101

	T1101_mem1 = S.Task('T1101_mem1', length=1, delay_cost=1)
	T1101_mem1 += ADD_mem[1]
	S += 45<T1101_mem1
	S += T1101_mem1<=T1101

	T1110_mem0 = S.Task('T1110_mem0', length=1, delay_cost=1)
	T1110_mem0 += ADD_mem[0]
	S += 64<T1110_mem0
	S += T1110_mem0<=T1110

	T1110_mem1 = S.Task('T1110_mem1', length=1, delay_cost=1)
	T1110_mem1 += ADD_mem[2]
	S += 61<T1110_mem1
	S += T1110_mem1<=T1110

	T1111_mem0 = S.Task('T1111_mem0', length=1, delay_cost=1)
	T1111_mem0 += ADD_mem[1]
	S += 74<T1111_mem0
	S += T1111_mem0<=T1111

	T1111_mem1 = S.Task('T1111_mem1', length=1, delay_cost=1)
	T1111_mem1 += ADD_mem[0]
	S += 32<T1111_mem1
	S += T1111_mem1<=T1111

	T4100_mem0 = S.Task('T4100_mem0', length=1, delay_cost=1)
	T4100_mem0 += ADD_mem[0]
	S += 67<T4100_mem0
	S += T4100_mem0<=T4100

	T4100_mem1 = S.Task('T4100_mem1', length=1, delay_cost=1)
	T4100_mem1 += ADD_mem[0]
	S += 38<T4100_mem1
	S += T4100_mem1<=T4100

	T4101_mem0 = S.Task('T4101_mem0', length=1, delay_cost=1)
	T4101_mem0 += ADD_mem[1]
	S += 57<T4101_mem0
	S += T4101_mem0<=T4101

	T4101_mem1 = S.Task('T4101_mem1', length=1, delay_cost=1)
	T4101_mem1 += ADD_mem[0]
	S += 44<T4101_mem1
	S += T4101_mem1<=T4101

	T4110_mem0 = S.Task('T4110_mem0', length=1, delay_cost=1)
	T4110_mem0 += ADD_mem[1]
	S += 48<T4110_mem0
	S += T4110_mem0<=T4110

	T4110_mem1 = S.Task('T4110_mem1', length=1, delay_cost=1)
	T4110_mem1 += ADD_mem[1]
	S += 26<T4110_mem1
	S += T4110_mem1<=T4110

	T4111_mem0 = S.Task('T4111_mem0', length=1, delay_cost=1)
	T4111_mem0 += ADD_mem[0]
	S += 24<T4111_mem0
	S += T4111_mem0<=T4111

	T4111_mem1 = S.Task('T4111_mem1', length=1, delay_cost=1)
	T4111_mem1 += ADD_mem[0]
	S += 25<T4111_mem1
	S += T4111_mem1<=T4111

	T2110_mem0 = S.Task('T2110_mem0', length=1, delay_cost=1)
	T2110_mem0 += ADD_mem[3]
	S += 30<T2110_mem0
	S += T2110_mem0<=T2110

	T2110_mem1 = S.Task('T2110_mem1', length=1, delay_cost=1)
	T2110_mem1 += ADD_mem[2]
	S += 61<T2110_mem1
	S += T2110_mem1<=T2110

	T2111_mem0 = S.Task('T2111_mem0', length=1, delay_cost=1)
	T2111_mem0 += ADD_mem[0]
	S += 82<T2111_mem0
	S += T2111_mem0<=T2111

	T2111_mem1 = S.Task('T2111_mem1', length=1, delay_cost=1)
	T2111_mem1 += ADD_mem[0]
	S += 32<T2111_mem1
	S += T2111_mem1<=T2111

	T5100_mem0 = S.Task('T5100_mem0', length=1, delay_cost=1)
	T5100_mem0 += ADD_mem[1]
	S += 28<T5100_mem0
	S += T5100_mem0<=T5100

	T5100_mem1 = S.Task('T5100_mem1', length=1, delay_cost=1)
	T5100_mem1 += ADD_mem[0]
	S += 38<T5100_mem1
	S += T5100_mem1<=T5100

	T5101_mem0 = S.Task('T5101_mem0', length=1, delay_cost=1)
	T5101_mem0 += ADD_mem[0]
	S += 80<T5101_mem0
	S += T5101_mem0<=T5101

	T5101_mem1 = S.Task('T5101_mem1', length=1, delay_cost=1)
	T5101_mem1 += ADD_mem[0]
	S += 44<T5101_mem1
	S += T5101_mem1<=T5101

	T5110_mem0 = S.Task('T5110_mem0', length=1, delay_cost=1)
	T5110_mem0 += ADD_mem[0]
	S += 68<T5110_mem0
	S += T5110_mem0<=T5110

	T5110_mem1 = S.Task('T5110_mem1', length=1, delay_cost=1)
	T5110_mem1 += ADD_mem[1]
	S += 26<T5110_mem1
	S += T5110_mem1<=T5110

	T5111_mem0 = S.Task('T5111_mem0', length=1, delay_cost=1)
	T5111_mem0 += ADD_mem[2]
	S += 63<T5111_mem0
	S += T5111_mem0<=T5111

	T5111_mem1 = S.Task('T5111_mem1', length=1, delay_cost=1)
	T5111_mem1 += ADD_mem[0]
	S += 25<T5111_mem1
	S += T5111_mem1<=T5111

	T61t4_a0b0_mem0 = S.Task('T61t4_a0b0_mem0', length=1, delay_cost=1)
	T61t4_a0b0_mem0 += ADD_mem[2]
	S += 18<T61t4_a0b0_mem0
	S += T61t4_a0b0_mem0<=T61t4_a0b0

	T61t4_a0b0_mem1 = S.Task('T61t4_a0b0_mem1', length=1, delay_cost=1)
	T61t4_a0b0_mem1 += ADD_mem[0]
	S += 71<T61t4_a0b0_mem1
	S += T61t4_a0b0_mem1<=T61t4_a0b0

	T61c0_a0b0_mem0 = S.Task('T61c0_a0b0_mem0', length=1, delay_cost=1)
	T61c0_a0b0_mem0 += MUL_mem[0]
	S += 18<T61c0_a0b0_mem0
	S += T61c0_a0b0_mem0<=T61c0_a0b0

	T61c0_a0b0_mem1 = S.Task('T61c0_a0b0_mem1', length=1, delay_cost=1)
	T61c0_a0b0_mem1 += MUL_mem[0]
	S += 14<T61c0_a0b0_mem1
	S += T61c0_a0b0_mem1<=T61c0_a0b0

	T61t6_a0b0_mem0 = S.Task('T61t6_a0b0_mem0', length=1, delay_cost=1)
	T61t6_a0b0_mem0 += MUL_mem[0]
	S += 18<T61t6_a0b0_mem0
	S += T61t6_a0b0_mem0<=T61t6_a0b0

	T61t6_a0b0_mem1 = S.Task('T61t6_a0b0_mem1', length=1, delay_cost=1)
	T61t6_a0b0_mem1 += MUL_mem[0]
	S += 14<T61t6_a0b0_mem1
	S += T61t6_a0b0_mem1<=T61t6_a0b0

	T61t4_a1b1_mem0 = S.Task('T61t4_a1b1_mem0', length=1, delay_cost=1)
	T61t4_a1b1_mem0 += ADD_mem[0]
	S += 36<T61t4_a1b1_mem0
	S += T61t4_a1b1_mem0<=T61t4_a1b1

	T61t4_a1b1_mem1 = S.Task('T61t4_a1b1_mem1', length=1, delay_cost=1)
	T61t4_a1b1_mem1 += ADD_mem[1]
	S += 16<T61t4_a1b1_mem1
	S += T61t4_a1b1_mem1<=T61t4_a1b1

	T61c0_a1b1_mem0 = S.Task('T61c0_a1b1_mem0', length=1, delay_cost=1)
	T61c0_a1b1_mem0 += MUL_mem[0]
	S += 15<T61c0_a1b1_mem0
	S += T61c0_a1b1_mem0<=T61c0_a1b1

	T61c0_a1b1_mem1 = S.Task('T61c0_a1b1_mem1', length=1, delay_cost=1)
	T61c0_a1b1_mem1 += MUL_mem[0]
	S += 13<T61c0_a1b1_mem1
	S += T61c0_a1b1_mem1<=T61c0_a1b1

	T61t6_a1b1_mem0 = S.Task('T61t6_a1b1_mem0', length=1, delay_cost=1)
	T61t6_a1b1_mem0 += MUL_mem[0]
	S += 15<T61t6_a1b1_mem0
	S += T61t6_a1b1_mem0<=T61t6_a1b1

	T61t6_a1b1_mem1 = S.Task('T61t6_a1b1_mem1', length=1, delay_cost=1)
	T61t6_a1b1_mem1 += MUL_mem[0]
	S += 13<T61t6_a1b1_mem1
	S += T61t6_a1b1_mem1<=T61t6_a1b1

	T61t0_t2t3_mem0 = S.Task('T61t0_t2t3_mem0', length=1, delay_cost=1)
	T61t0_t2t3_mem0 += ADD_mem[0]
	S += 27<T61t0_t2t3_mem0
	S += T61t0_t2t3_mem0<=T61t0_t2t3

	T61t0_t2t3_mem1 = S.Task('T61t0_t2t3_mem1', length=1, delay_cost=1)
	T61t0_t2t3_mem1 += ADD_mem[0]
	S += 65<T61t0_t2t3_mem1
	S += T61t0_t2t3_mem1<=T61t0_t2t3

	T61t1_t2t3_mem0 = S.Task('T61t1_t2t3_mem0', length=1, delay_cost=1)
	T61t1_t2t3_mem0 += ADD_mem[1]
	S += 22<T61t1_t2t3_mem0
	S += T61t1_t2t3_mem0<=T61t1_t2t3

	T61t1_t2t3_mem1 = S.Task('T61t1_t2t3_mem1', length=1, delay_cost=1)
	T61t1_t2t3_mem1 += ADD_mem[2]
	S += 35<T61t1_t2t3_mem1
	S += T61t1_t2t3_mem1<=T61t1_t2t3

	T61t2_t2t3_mem0 = S.Task('T61t2_t2t3_mem0', length=1, delay_cost=1)
	T61t2_t2t3_mem0 += ADD_mem[0]
	S += 27<T61t2_t2t3_mem0
	S += T61t2_t2t3_mem0<=T61t2_t2t3

	T61t2_t2t3_mem1 = S.Task('T61t2_t2t3_mem1', length=1, delay_cost=1)
	T61t2_t2t3_mem1 += ADD_mem[1]
	S += 22<T61t2_t2t3_mem1
	S += T61t2_t2t3_mem1<=T61t2_t2t3

	T61t3_t2t3_mem0 = S.Task('T61t3_t2t3_mem0', length=1, delay_cost=1)
	T61t3_t2t3_mem0 += ADD_mem[0]
	S += 65<T61t3_t2t3_mem0
	S += T61t3_t2t3_mem0<=T61t3_t2t3

	T61t3_t2t3_mem1 = S.Task('T61t3_t2t3_mem1', length=1, delay_cost=1)
	T61t3_t2t3_mem1 += ADD_mem[2]
	S += 35<T61t3_t2t3_mem1
	S += T61t3_t2t3_mem1<=T61t3_t2t3

	T71t4_a0b0_mem0 = S.Task('T71t4_a0b0_mem0', length=1, delay_cost=1)
	T71t4_a0b0_mem0 += ADD_mem[0]
	S += 19<T71t4_a0b0_mem0
	S += T71t4_a0b0_mem0<=T71t4_a0b0

	T71t4_a0b0_mem1 = S.Task('T71t4_a0b0_mem1', length=1, delay_cost=1)
	T71t4_a0b0_mem1 += ADD_mem[2]
	S += 14<T71t4_a0b0_mem1
	S += T71t4_a0b0_mem1<=T71t4_a0b0

	T71c0_a0b0_mem0 = S.Task('T71c0_a0b0_mem0', length=1, delay_cost=1)
	T71c0_a0b0_mem0 += MUL_mem[0]
	S += 12<T71c0_a0b0_mem0
	S += T71c0_a0b0_mem0<=T71c0_a0b0

	T71c0_a0b0_mem1 = S.Task('T71c0_a0b0_mem1', length=1, delay_cost=1)
	T71c0_a0b0_mem1 += MUL_mem[0]
	S += 9<T71c0_a0b0_mem1
	S += T71c0_a0b0_mem1<=T71c0_a0b0

	T71t6_a0b0_mem0 = S.Task('T71t6_a0b0_mem0', length=1, delay_cost=1)
	T71t6_a0b0_mem0 += MUL_mem[0]
	S += 12<T71t6_a0b0_mem0
	S += T71t6_a0b0_mem0<=T71t6_a0b0

	T71t6_a0b0_mem1 = S.Task('T71t6_a0b0_mem1', length=1, delay_cost=1)
	T71t6_a0b0_mem1 += MUL_mem[0]
	S += 9<T71t6_a0b0_mem1
	S += T71t6_a0b0_mem1<=T71t6_a0b0

	T71t4_a1b1_mem0 = S.Task('T71t4_a1b1_mem0', length=1, delay_cost=1)
	T71t4_a1b1_mem0 += ADD_mem[0]
	S += 41<T71t4_a1b1_mem0
	S += T71t4_a1b1_mem0<=T71t4_a1b1

	T71t4_a1b1_mem1 = S.Task('T71t4_a1b1_mem1', length=1, delay_cost=1)
	T71t4_a1b1_mem1 += ADD_mem[0]
	S += 40<T71t4_a1b1_mem1
	S += T71t4_a1b1_mem1<=T71t4_a1b1

	T71c0_a1b1_mem0 = S.Task('T71c0_a1b1_mem0', length=1, delay_cost=1)
	T71c0_a1b1_mem0 += MUL_mem[0]
	S += 17<T71c0_a1b1_mem0
	S += T71c0_a1b1_mem0<=T71c0_a1b1

	T71c0_a1b1_mem1 = S.Task('T71c0_a1b1_mem1', length=1, delay_cost=1)
	T71c0_a1b1_mem1 += MUL_mem[0]
	S += 10<T71c0_a1b1_mem1
	S += T71c0_a1b1_mem1<=T71c0_a1b1

	T71t6_a1b1_mem0 = S.Task('T71t6_a1b1_mem0', length=1, delay_cost=1)
	T71t6_a1b1_mem0 += MUL_mem[0]
	S += 17<T71t6_a1b1_mem0
	S += T71t6_a1b1_mem0<=T71t6_a1b1

	T71t6_a1b1_mem1 = S.Task('T71t6_a1b1_mem1', length=1, delay_cost=1)
	T71t6_a1b1_mem1 += MUL_mem[0]
	S += 10<T71t6_a1b1_mem1
	S += T71t6_a1b1_mem1<=T71t6_a1b1

	T71t0_t2t3_mem0 = S.Task('T71t0_t2t3_mem0', length=1, delay_cost=1)
	T71t0_t2t3_mem0 += ADD_mem[1]
	S += 47<T71t0_t2t3_mem0
	S += T71t0_t2t3_mem0<=T71t0_t2t3

	T71t0_t2t3_mem1 = S.Task('T71t0_t2t3_mem1', length=1, delay_cost=1)
	T71t0_t2t3_mem1 += ADD_mem[0]
	S += 39<T71t0_t2t3_mem1
	S += T71t0_t2t3_mem1<=T71t0_t2t3

	T71t1_t2t3_mem0 = S.Task('T71t1_t2t3_mem0', length=1, delay_cost=1)
	T71t1_t2t3_mem0 += ADD_mem[0]
	S += 17<T71t1_t2t3_mem0
	S += T71t1_t2t3_mem0<=T71t1_t2t3

	T71t1_t2t3_mem1 = S.Task('T71t1_t2t3_mem1', length=1, delay_cost=1)
	T71t1_t2t3_mem1 += ADD_mem[0]
	S += 23<T71t1_t2t3_mem1
	S += T71t1_t2t3_mem1<=T71t1_t2t3

	T71t2_t2t3_mem0 = S.Task('T71t2_t2t3_mem0', length=1, delay_cost=1)
	T71t2_t2t3_mem0 += ADD_mem[1]
	S += 47<T71t2_t2t3_mem0
	S += T71t2_t2t3_mem0<=T71t2_t2t3

	T71t2_t2t3_mem1 = S.Task('T71t2_t2t3_mem1', length=1, delay_cost=1)
	T71t2_t2t3_mem1 += ADD_mem[0]
	S += 17<T71t2_t2t3_mem1
	S += T71t2_t2t3_mem1<=T71t2_t2t3

	T71t3_t2t3_mem0 = S.Task('T71t3_t2t3_mem0', length=1, delay_cost=1)
	T71t3_t2t3_mem0 += ADD_mem[0]
	S += 39<T71t3_t2t3_mem0
	S += T71t3_t2t3_mem0<=T71t3_t2t3

	T71t3_t2t3_mem1 = S.Task('T71t3_t2t3_mem1', length=1, delay_cost=1)
	T71t3_t2t3_mem1 += ADD_mem[0]
	S += 23<T71t3_t2t3_mem1
	S += T71t3_t2t3_mem1<=T71t3_t2t3

	T82t4_a0b0_mem0 = S.Task('T82t4_a0b0_mem0', length=1, delay_cost=1)
	T82t4_a0b0_mem0 += ADD_mem[0]
	S += 29<T82t4_a0b0_mem0
	S += T82t4_a0b0_mem0<=T82t4_a0b0

	T82t4_a0b0_mem1 = S.Task('T82t4_a0b0_mem1', length=1, delay_cost=1)
	T82t4_a0b0_mem1 += ADD_mem[0]
	S += 56<T82t4_a0b0_mem1
	S += T82t4_a0b0_mem1<=T82t4_a0b0

	T82c0_a0b0_mem0 = S.Task('T82c0_a0b0_mem0', length=1, delay_cost=1)
	T82c0_a0b0_mem0 += MUL_mem[0]
	S += 8<T82c0_a0b0_mem0
	S += T82c0_a0b0_mem0<=T82c0_a0b0

	T82c0_a0b0_mem1 = S.Task('T82c0_a0b0_mem1', length=1, delay_cost=1)
	T82c0_a0b0_mem1 += MUL_mem[0]
	S += 11<T82c0_a0b0_mem1
	S += T82c0_a0b0_mem1<=T82c0_a0b0

	T82t6_a0b0_mem0 = S.Task('T82t6_a0b0_mem0', length=1, delay_cost=1)
	T82t6_a0b0_mem0 += MUL_mem[0]
	S += 8<T82t6_a0b0_mem0
	S += T82t6_a0b0_mem0<=T82t6_a0b0

	T82t6_a0b0_mem1 = S.Task('T82t6_a0b0_mem1', length=1, delay_cost=1)
	T82t6_a0b0_mem1 += MUL_mem[0]
	S += 11<T82t6_a0b0_mem1
	S += T82t6_a0b0_mem1<=T82t6_a0b0

	T82t4_a1b1_mem0 = S.Task('T82t4_a1b1_mem0', length=1, delay_cost=1)
	T82t4_a1b1_mem0 += ADD_mem[2]
	S += 69<T82t4_a1b1_mem0
	S += T82t4_a1b1_mem0<=T82t4_a1b1

	T82t4_a1b1_mem1 = S.Task('T82t4_a1b1_mem1', length=1, delay_cost=1)
	T82t4_a1b1_mem1 += ADD_mem[0]
	S += 77<T82t4_a1b1_mem1
	S += T82t4_a1b1_mem1<=T82t4_a1b1

	T82c0_a1b1_mem0 = S.Task('T82c0_a1b1_mem0', length=1, delay_cost=1)
	T82c0_a1b1_mem0 += MUL_mem[0]
	S += 7<T82c0_a1b1_mem0
	S += T82c0_a1b1_mem0<=T82c0_a1b1

	T82c0_a1b1_mem1 = S.Task('T82c0_a1b1_mem1', length=1, delay_cost=1)
	T82c0_a1b1_mem1 += MUL_mem[0]
	S += 16<T82c0_a1b1_mem1
	S += T82c0_a1b1_mem1<=T82c0_a1b1

	T82t6_a1b1_mem0 = S.Task('T82t6_a1b1_mem0', length=1, delay_cost=1)
	T82t6_a1b1_mem0 += MUL_mem[0]
	S += 7<T82t6_a1b1_mem0
	S += T82t6_a1b1_mem0<=T82t6_a1b1

	T82t6_a1b1_mem1 = S.Task('T82t6_a1b1_mem1', length=1, delay_cost=1)
	T82t6_a1b1_mem1 += MUL_mem[0]
	S += 16<T82t6_a1b1_mem1
	S += T82t6_a1b1_mem1<=T82t6_a1b1

	T82t0_t2t3_mem0 = S.Task('T82t0_t2t3_mem0', length=1, delay_cost=1)
	T82t0_t2t3_mem0 += ADD_mem[0]
	S += 62<T82t0_t2t3_mem0
	S += T82t0_t2t3_mem0<=T82t0_t2t3

	T82t0_t2t3_mem1 = S.Task('T82t0_t2t3_mem1', length=1, delay_cost=1)
	T82t0_t2t3_mem1 += ADD_mem[1]
	S += 52<T82t0_t2t3_mem1
	S += T82t0_t2t3_mem1<=T82t0_t2t3

	T82t1_t2t3_mem0 = S.Task('T82t1_t2t3_mem0', length=1, delay_cost=1)
	T82t1_t2t3_mem0 += ADD_mem[0]
	S += 13<T82t1_t2t3_mem0
	S += T82t1_t2t3_mem0<=T82t1_t2t3

	T82t1_t2t3_mem1 = S.Task('T82t1_t2t3_mem1', length=1, delay_cost=1)
	T82t1_t2t3_mem1 += ADD_mem[3]
	S += 70<T82t1_t2t3_mem1
	S += T82t1_t2t3_mem1<=T82t1_t2t3

	T82t2_t2t3_mem0 = S.Task('T82t2_t2t3_mem0', length=1, delay_cost=1)
	T82t2_t2t3_mem0 += ADD_mem[0]
	S += 62<T82t2_t2t3_mem0
	S += T82t2_t2t3_mem0<=T82t2_t2t3

	T82t2_t2t3_mem1 = S.Task('T82t2_t2t3_mem1', length=1, delay_cost=1)
	T82t2_t2t3_mem1 += ADD_mem[0]
	S += 13<T82t2_t2t3_mem1
	S += T82t2_t2t3_mem1<=T82t2_t2t3

	T82t3_t2t3_mem0 = S.Task('T82t3_t2t3_mem0', length=1, delay_cost=1)
	T82t3_t2t3_mem0 += ADD_mem[1]
	S += 52<T82t3_t2t3_mem0
	S += T82t3_t2t3_mem0<=T82t3_t2t3

	T82t3_t2t3_mem1 = S.Task('T82t3_t2t3_mem1', length=1, delay_cost=1)
	T82t3_t2t3_mem1 += ADD_mem[3]
	S += 70<T82t3_t2t3_mem1
	S += T82t3_t2t3_mem1<=T82t3_t2t3

	T95t2_0_mem0 = S.Task('T95t2_0_mem0', length=1, delay_cost=1)
	T95t2_0_mem0 += ADD_mem[0]
	S += 33<T95t2_0_mem0
	S += T95t2_0_mem0<=T95t2_0

	T95t2_0_mem1 = S.Task('T95t2_0_mem1', length=1, delay_cost=1)
	T95t2_0_mem1 += ADD_mem[0]
	S += 31<T95t2_0_mem1
	S += T95t2_0_mem1<=T95t2_0

	T95t2_1_mem0 = S.Task('T95t2_1_mem0', length=1, delay_cost=1)
	T95t2_1_mem0 += ADD_mem[0]
	S += 34<T95t2_1_mem0
	S += T95t2_1_mem0<=T95t2_1

	T95t2_1_mem1 = S.Task('T95t2_1_mem1', length=1, delay_cost=1)
	T95t2_1_mem1 += ADD_mem[0]
	S += 46<T95t2_1_mem1
	S += T95t2_1_mem1<=T95t2_1

	T95t3_0_mem0 = S.Task('T95t3_0_mem0', length=1, delay_cost=1)
	T95t3_0_mem0 += ADD_mem[0]
	S += 79<T95t3_0_mem0
	S += T95t3_0_mem0<=T95t3_0

	T95t3_0_mem1 = S.Task('T95t3_0_mem1', length=1, delay_cost=1)
	T95t3_0_mem1 += ADD_mem[0]
	S += 73<T95t3_0_mem1
	S += T95t3_0_mem1<=T95t3_0

	T95t3_1_mem0 = S.Task('T95t3_1_mem0', length=1, delay_cost=1)
	T95t3_1_mem0 += ADD_mem[0]
	S += 78<T95t3_1_mem0
	S += T95t3_1_mem0<=T95t3_1

	T95t3_1_mem1 = S.Task('T95t3_1_mem1', length=1, delay_cost=1)
	T95t3_1_mem1 += ADD_mem[2]
	S += 20<T95t3_1_mem1
	S += T95t3_1_mem1<=T95t3_1

	T95t0_a0b0_mem0 = S.Task('T95t0_a0b0_mem0', length=1, delay_cost=1)
	T95t0_a0b0_mem0 += ADD_mem[0]
	S += 33<T95t0_a0b0_mem0
	S += T95t0_a0b0_mem0<=T95t0_a0b0

	T95t0_a0b0_mem1 = S.Task('T95t0_a0b0_mem1', length=1, delay_cost=1)
	T95t0_a0b0_mem1 += ADD_mem[0]
	S += 79<T95t0_a0b0_mem1
	S += T95t0_a0b0_mem1<=T95t0_a0b0

	T95t1_a0b0_mem0 = S.Task('T95t1_a0b0_mem0', length=1, delay_cost=1)
	T95t1_a0b0_mem0 += ADD_mem[0]
	S += 34<T95t1_a0b0_mem0
	S += T95t1_a0b0_mem0<=T95t1_a0b0

	T95t1_a0b0_mem1 = S.Task('T95t1_a0b0_mem1', length=1, delay_cost=1)
	T95t1_a0b0_mem1 += ADD_mem[0]
	S += 78<T95t1_a0b0_mem1
	S += T95t1_a0b0_mem1<=T95t1_a0b0

	T95t2_a0b0_mem0 = S.Task('T95t2_a0b0_mem0', length=1, delay_cost=1)
	T95t2_a0b0_mem0 += ADD_mem[0]
	S += 33<T95t2_a0b0_mem0
	S += T95t2_a0b0_mem0<=T95t2_a0b0

	T95t2_a0b0_mem1 = S.Task('T95t2_a0b0_mem1', length=1, delay_cost=1)
	T95t2_a0b0_mem1 += ADD_mem[0]
	S += 34<T95t2_a0b0_mem1
	S += T95t2_a0b0_mem1<=T95t2_a0b0

	T95t3_a0b0_mem0 = S.Task('T95t3_a0b0_mem0', length=1, delay_cost=1)
	T95t3_a0b0_mem0 += ADD_mem[0]
	S += 79<T95t3_a0b0_mem0
	S += T95t3_a0b0_mem0<=T95t3_a0b0

	T95t3_a0b0_mem1 = S.Task('T95t3_a0b0_mem1', length=1, delay_cost=1)
	T95t3_a0b0_mem1 += ADD_mem[0]
	S += 78<T95t3_a0b0_mem1
	S += T95t3_a0b0_mem1<=T95t3_a0b0

	T95t0_a1b1_mem0 = S.Task('T95t0_a1b1_mem0', length=1, delay_cost=1)
	T95t0_a1b1_mem0 += ADD_mem[0]
	S += 31<T95t0_a1b1_mem0
	S += T95t0_a1b1_mem0<=T95t0_a1b1

	T95t0_a1b1_mem1 = S.Task('T95t0_a1b1_mem1', length=1, delay_cost=1)
	T95t0_a1b1_mem1 += ADD_mem[0]
	S += 73<T95t0_a1b1_mem1
	S += T95t0_a1b1_mem1<=T95t0_a1b1

	T95t1_a1b1_mem0 = S.Task('T95t1_a1b1_mem0', length=1, delay_cost=1)
	T95t1_a1b1_mem0 += ADD_mem[0]
	S += 46<T95t1_a1b1_mem0
	S += T95t1_a1b1_mem0<=T95t1_a1b1

	T95t1_a1b1_mem1 = S.Task('T95t1_a1b1_mem1', length=1, delay_cost=1)
	T95t1_a1b1_mem1 += ADD_mem[2]
	S += 20<T95t1_a1b1_mem1
	S += T95t1_a1b1_mem1<=T95t1_a1b1

	T95t2_a1b1_mem0 = S.Task('T95t2_a1b1_mem0', length=1, delay_cost=1)
	T95t2_a1b1_mem0 += ADD_mem[0]
	S += 31<T95t2_a1b1_mem0
	S += T95t2_a1b1_mem0<=T95t2_a1b1

	T95t2_a1b1_mem1 = S.Task('T95t2_a1b1_mem1', length=1, delay_cost=1)
	T95t2_a1b1_mem1 += ADD_mem[0]
	S += 46<T95t2_a1b1_mem1
	S += T95t2_a1b1_mem1<=T95t2_a1b1

	T95t3_a1b1_mem0 = S.Task('T95t3_a1b1_mem0', length=1, delay_cost=1)
	T95t3_a1b1_mem0 += ADD_mem[0]
	S += 73<T95t3_a1b1_mem0
	S += T95t3_a1b1_mem0<=T95t3_a1b1

	T95t3_a1b1_mem1 = S.Task('T95t3_a1b1_mem1', length=1, delay_cost=1)
	T95t3_a1b1_mem1 += ADD_mem[2]
	S += 20<T95t3_a1b1_mem1
	S += T95t3_a1b1_mem1<=T95t3_a1b1

	T32t2_0_mem0 = S.Task('T32t2_0_mem0', length=1, delay_cost=1)
	T32t2_0_mem0 += ADD_mem[0]
	S += 75<T32t2_0_mem0
	S += T32t2_0_mem0<=T32t2_0

	T32t2_0_mem1 = S.Task('T32t2_0_mem1', length=1, delay_cost=1)
	T32t2_0_mem1 += ADD_mem[0]
	S += 43<T32t2_0_mem1
	S += T32t2_0_mem1<=T32t2_0

	T32t2_1_mem0 = S.Task('T32t2_1_mem0', length=1, delay_cost=1)
	T32t2_1_mem0 += ADD_mem[0]
	S += 50<T32t2_1_mem0
	S += T32t2_1_mem0<=T32t2_1

	T32t2_1_mem1 = S.Task('T32t2_1_mem1', length=1, delay_cost=1)
	T32t2_1_mem1 += ADD_mem[0]
	S += 76<T32t2_1_mem1
	S += T32t2_1_mem1<=T32t2_1

	T32t3_0_mem0 = S.Task('T32t3_0_mem0', length=1, delay_cost=1)
	T32t3_0_mem0 += ADD_mem[0]
	S += 54<T32t3_0_mem0
	S += T32t3_0_mem0<=T32t3_0

	T32t3_0_mem1 = S.Task('T32t3_0_mem1', length=1, delay_cost=1)
	T32t3_0_mem1 += ADD_mem[2]
	S += 15<T32t3_0_mem1
	S += T32t3_0_mem1<=T32t3_0

	T32t3_1_mem0 = S.Task('T32t3_1_mem0', length=1, delay_cost=1)
	T32t3_1_mem0 += ADD_mem[1]
	S += 60<T32t3_1_mem0
	S += T32t3_1_mem0<=T32t3_1

	T32t3_1_mem1 = S.Task('T32t3_1_mem1', length=1, delay_cost=1)
	T32t3_1_mem1 += ADD_mem[0]
	S += 51<T32t3_1_mem1
	S += T32t3_1_mem1<=T32t3_1

	T32t0_a0b0_mem0 = S.Task('T32t0_a0b0_mem0', length=1, delay_cost=1)
	T32t0_a0b0_mem0 += ADD_mem[0]
	S += 75<T32t0_a0b0_mem0
	S += T32t0_a0b0_mem0<=T32t0_a0b0

	T32t0_a0b0_mem1 = S.Task('T32t0_a0b0_mem1', length=1, delay_cost=1)
	T32t0_a0b0_mem1 += ADD_mem[0]
	S += 54<T32t0_a0b0_mem1
	S += T32t0_a0b0_mem1<=T32t0_a0b0

	T32t1_a0b0_mem0 = S.Task('T32t1_a0b0_mem0', length=1, delay_cost=1)
	T32t1_a0b0_mem0 += ADD_mem[0]
	S += 50<T32t1_a0b0_mem0
	S += T32t1_a0b0_mem0<=T32t1_a0b0

	T32t1_a0b0_mem1 = S.Task('T32t1_a0b0_mem1', length=1, delay_cost=1)
	T32t1_a0b0_mem1 += ADD_mem[1]
	S += 60<T32t1_a0b0_mem1
	S += T32t1_a0b0_mem1<=T32t1_a0b0

	T32t2_a0b0_mem0 = S.Task('T32t2_a0b0_mem0', length=1, delay_cost=1)
	T32t2_a0b0_mem0 += ADD_mem[0]
	S += 75<T32t2_a0b0_mem0
	S += T32t2_a0b0_mem0<=T32t2_a0b0

	T32t2_a0b0_mem1 = S.Task('T32t2_a0b0_mem1', length=1, delay_cost=1)
	T32t2_a0b0_mem1 += ADD_mem[0]
	S += 50<T32t2_a0b0_mem1
	S += T32t2_a0b0_mem1<=T32t2_a0b0

	T32t3_a0b0_mem0 = S.Task('T32t3_a0b0_mem0', length=1, delay_cost=1)
	T32t3_a0b0_mem0 += ADD_mem[0]
	S += 54<T32t3_a0b0_mem0
	S += T32t3_a0b0_mem0<=T32t3_a0b0

	T32t3_a0b0_mem1 = S.Task('T32t3_a0b0_mem1', length=1, delay_cost=1)
	T32t3_a0b0_mem1 += ADD_mem[1]
	S += 60<T32t3_a0b0_mem1
	S += T32t3_a0b0_mem1<=T32t3_a0b0

	T32t0_a1b1_mem0 = S.Task('T32t0_a1b1_mem0', length=1, delay_cost=1)
	T32t0_a1b1_mem0 += ADD_mem[0]
	S += 43<T32t0_a1b1_mem0
	S += T32t0_a1b1_mem0<=T32t0_a1b1

	T32t0_a1b1_mem1 = S.Task('T32t0_a1b1_mem1', length=1, delay_cost=1)
	T32t0_a1b1_mem1 += ADD_mem[2]
	S += 15<T32t0_a1b1_mem1
	S += T32t0_a1b1_mem1<=T32t0_a1b1

	T32t1_a1b1_mem0 = S.Task('T32t1_a1b1_mem0', length=1, delay_cost=1)
	T32t1_a1b1_mem0 += ADD_mem[0]
	S += 76<T32t1_a1b1_mem0
	S += T32t1_a1b1_mem0<=T32t1_a1b1

	T32t1_a1b1_mem1 = S.Task('T32t1_a1b1_mem1', length=1, delay_cost=1)
	T32t1_a1b1_mem1 += ADD_mem[0]
	S += 51<T32t1_a1b1_mem1
	S += T32t1_a1b1_mem1<=T32t1_a1b1

	T32t2_a1b1_mem0 = S.Task('T32t2_a1b1_mem0', length=1, delay_cost=1)
	T32t2_a1b1_mem0 += ADD_mem[0]
	S += 43<T32t2_a1b1_mem0
	S += T32t2_a1b1_mem0<=T32t2_a1b1

	T32t2_a1b1_mem1 = S.Task('T32t2_a1b1_mem1', length=1, delay_cost=1)
	T32t2_a1b1_mem1 += ADD_mem[0]
	S += 76<T32t2_a1b1_mem1
	S += T32t2_a1b1_mem1<=T32t2_a1b1

	T32t3_a1b1_mem0 = S.Task('T32t3_a1b1_mem0', length=1, delay_cost=1)
	T32t3_a1b1_mem0 += ADD_mem[2]
	S += 15<T32t3_a1b1_mem0
	S += T32t3_a1b1_mem0<=T32t3_a1b1

	T32t3_a1b1_mem1 = S.Task('T32t3_a1b1_mem1', length=1, delay_cost=1)
	T32t3_a1b1_mem1 += ADD_mem[0]
	S += 51<T32t3_a1b1_mem1
	S += T32t3_a1b1_mem1<=T32t3_a1b1

	T44t2_0_mem0 = S.Task('T44t2_0_mem0', length=1, delay_cost=1)
	T44t2_0_mem0 += ADD_mem[0]
	S += 42<T44t2_0_mem0
	S += T44t2_0_mem0<=T44t2_0

	T44t2_0_mem1 = S.Task('T44t2_0_mem1', length=1, delay_cost=1)
	T44t2_0_mem1 += ADD_mem[1]
	S += 49<T44t2_0_mem1
	S += T44t2_0_mem1<=T44t2_0

	T44t2_1_mem0 = S.Task('T44t2_1_mem0', length=1, delay_cost=1)
	T44t2_1_mem0 += ADD_mem[2]
	S += 59<T44t2_1_mem0
	S += T44t2_1_mem0<=T44t2_1

	T44t2_1_mem1 = S.Task('T44t2_1_mem1', length=1, delay_cost=1)
	T44t2_1_mem1 += ADD_mem[3]
	S += 53<T44t2_1_mem1
	S += T44t2_1_mem1<=T44t2_1

	T44t3_0_mem0 = S.Task('T44t3_0_mem0', length=1, delay_cost=1)
	T44t3_0_mem0 += ADD_mem[1]
	S += 21<T44t3_0_mem0
	S += T44t3_0_mem0<=T44t3_0

	T44t3_0_mem1 = S.Task('T44t3_0_mem1', length=1, delay_cost=1)
	T44t3_0_mem1 += ADD_mem[1]
	S += 58<T44t3_0_mem1
	S += T44t3_0_mem1<=T44t3_0

	T44t3_1_mem0 = S.Task('T44t3_1_mem0', length=1, delay_cost=1)
	T44t3_1_mem0 += ADD_mem[1]
	S += 55<T44t3_1_mem0
	S += T44t3_1_mem0<=T44t3_1

	T44t3_1_mem1 = S.Task('T44t3_1_mem1', length=1, delay_cost=1)
	T44t3_1_mem1 += ADD_mem[0]
	S += 37<T44t3_1_mem1
	S += T44t3_1_mem1<=T44t3_1

	T44t0_a0b0_mem0 = S.Task('T44t0_a0b0_mem0', length=1, delay_cost=1)
	T44t0_a0b0_mem0 += ADD_mem[0]
	S += 42<T44t0_a0b0_mem0
	S += T44t0_a0b0_mem0<=T44t0_a0b0

	T44t0_a0b0_mem1 = S.Task('T44t0_a0b0_mem1', length=1, delay_cost=1)
	T44t0_a0b0_mem1 += ADD_mem[1]
	S += 21<T44t0_a0b0_mem1
	S += T44t0_a0b0_mem1<=T44t0_a0b0

	T44t1_a0b0_mem0 = S.Task('T44t1_a0b0_mem0', length=1, delay_cost=1)
	T44t1_a0b0_mem0 += ADD_mem[2]
	S += 59<T44t1_a0b0_mem0
	S += T44t1_a0b0_mem0<=T44t1_a0b0

	T44t1_a0b0_mem1 = S.Task('T44t1_a0b0_mem1', length=1, delay_cost=1)
	T44t1_a0b0_mem1 += ADD_mem[1]
	S += 55<T44t1_a0b0_mem1
	S += T44t1_a0b0_mem1<=T44t1_a0b0

	T44t2_a0b0_mem0 = S.Task('T44t2_a0b0_mem0', length=1, delay_cost=1)
	T44t2_a0b0_mem0 += ADD_mem[0]
	S += 42<T44t2_a0b0_mem0
	S += T44t2_a0b0_mem0<=T44t2_a0b0

	T44t2_a0b0_mem1 = S.Task('T44t2_a0b0_mem1', length=1, delay_cost=1)
	T44t2_a0b0_mem1 += ADD_mem[2]
	S += 59<T44t2_a0b0_mem1
	S += T44t2_a0b0_mem1<=T44t2_a0b0

	T44t3_a0b0_mem0 = S.Task('T44t3_a0b0_mem0', length=1, delay_cost=1)
	T44t3_a0b0_mem0 += ADD_mem[1]
	S += 21<T44t3_a0b0_mem0
	S += T44t3_a0b0_mem0<=T44t3_a0b0

	T44t3_a0b0_mem1 = S.Task('T44t3_a0b0_mem1', length=1, delay_cost=1)
	T44t3_a0b0_mem1 += ADD_mem[1]
	S += 55<T44t3_a0b0_mem1
	S += T44t3_a0b0_mem1<=T44t3_a0b0

	T44t0_a1b1_mem0 = S.Task('T44t0_a1b1_mem0', length=1, delay_cost=1)
	T44t0_a1b1_mem0 += ADD_mem[1]
	S += 49<T44t0_a1b1_mem0
	S += T44t0_a1b1_mem0<=T44t0_a1b1

	T44t0_a1b1_mem1 = S.Task('T44t0_a1b1_mem1', length=1, delay_cost=1)
	T44t0_a1b1_mem1 += ADD_mem[1]
	S += 58<T44t0_a1b1_mem1
	S += T44t0_a1b1_mem1<=T44t0_a1b1

	T44t1_a1b1_mem0 = S.Task('T44t1_a1b1_mem0', length=1, delay_cost=1)
	T44t1_a1b1_mem0 += ADD_mem[3]
	S += 53<T44t1_a1b1_mem0
	S += T44t1_a1b1_mem0<=T44t1_a1b1

	T44t1_a1b1_mem1 = S.Task('T44t1_a1b1_mem1', length=1, delay_cost=1)
	T44t1_a1b1_mem1 += ADD_mem[0]
	S += 37<T44t1_a1b1_mem1
	S += T44t1_a1b1_mem1<=T44t1_a1b1

	T44t2_a1b1_mem0 = S.Task('T44t2_a1b1_mem0', length=1, delay_cost=1)
	T44t2_a1b1_mem0 += ADD_mem[1]
	S += 49<T44t2_a1b1_mem0
	S += T44t2_a1b1_mem0<=T44t2_a1b1

	T44t2_a1b1_mem1 = S.Task('T44t2_a1b1_mem1', length=1, delay_cost=1)
	T44t2_a1b1_mem1 += ADD_mem[3]
	S += 53<T44t2_a1b1_mem1
	S += T44t2_a1b1_mem1<=T44t2_a1b1

	T44t3_a1b1_mem0 = S.Task('T44t3_a1b1_mem0', length=1, delay_cost=1)
	T44t3_a1b1_mem0 += ADD_mem[1]
	S += 58<T44t3_a1b1_mem0
	S += T44t3_a1b1_mem0<=T44t3_a1b1

	T44t3_a1b1_mem1 = S.Task('T44t3_a1b1_mem1', length=1, delay_cost=1)
	T44t3_a1b1_mem1 += ADD_mem[0]
	S += 37<T44t3_a1b1_mem1
	S += T44t3_a1b1_mem1<=T44t3_a1b1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "s24_mul1_add4/s24_mul1_add4_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_s24_mul1_add4_1(0, 0)