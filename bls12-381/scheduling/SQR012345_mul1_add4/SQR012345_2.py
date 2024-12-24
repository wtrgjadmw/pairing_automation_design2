from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 130
	S = Scenario("SQR012345_2", horizon=horizon)

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
	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 0
	t7_t1_in += MUL_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 0
	t7_t1_mem0 += INPUT_mem_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 0
	t7_t1_mem1 += INPUT_mem_r

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 1
	t7_t0_in += MUL_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 1
	t7_t0_mem0 += INPUT_mem_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 1
	t7_t0_mem1 += INPUT_mem_r

	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	S += t7_t1 >= 1
	t7_t1 += MUL[0]

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 2
	t3_t1_in += MUL_in[0]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 2
	t3_t1_mem0 += INPUT_mem_r

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 2
	t3_t1_mem1 += INPUT_mem_r

	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	S += t7_t0 >= 2
	t7_t0 += MUL[0]

	t3_t1 = S.Task('t3_t1', length=7, delay_cost=1)
	S += t3_t1 >= 3
	t3_t1 += MUL[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 3
	t5_t1_in += MUL_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 3
	t5_t1_mem0 += INPUT_mem_r

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 3
	t5_t1_mem1 += INPUT_mem_r

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 4
	t0_t3_in += MUL_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += INPUT_mem_r

	t5_t1 = S.Task('t5_t1', length=7, delay_cost=1)
	S += t5_t1 >= 4
	t5_t1 += MUL[0]

	t0_t3 = S.Task('t0_t3', length=7, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MUL[0]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 5
	t6_t0_in += MUL_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 5
	t6_t0_mem0 += INPUT_mem_r

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 5
	t6_t0_mem1 += INPUT_mem_r

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 6
	t3_t0_in += MUL_in[0]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 6
	t3_t0_mem0 += INPUT_mem_r

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 6
	t3_t0_mem1 += INPUT_mem_r

	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	S += t6_t0 >= 6
	t6_t0 += MUL[0]

	t3_t0 = S.Task('t3_t0', length=7, delay_cost=1)
	S += t3_t0 >= 7
	t3_t0 += MUL[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 7
	t6_t1_in += MUL_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 7
	t6_t1_mem0 += INPUT_mem_r

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 7
	t6_t1_mem1 += INPUT_mem_r

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 8
	t5_t0_in += MUL_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 8
	t5_t0_mem0 += INPUT_mem_r

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 8
	t5_t0_mem1 += INPUT_mem_r

	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	S += t6_t1 >= 8
	t6_t1 += MUL[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 9
	t4_t3_in += MUL_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 9
	t4_t3_mem0 += INPUT_mem_r

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 9
	t4_t3_mem1 += INPUT_mem_r

	t5_t0 = S.Task('t5_t0', length=7, delay_cost=1)
	S += t5_t0 >= 9
	t5_t0 += MUL[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 9
	t70_mem0 += MUL_mem[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 9
	t70_mem1 += MUL_mem[0]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 10
	t4_t1_mem0 += INPUT_mem_r

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 10
	t4_t1_mem1 += INPUT_mem_r

	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	S += t4_t3 >= 10
	t4_t3 += MUL[0]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 10
	t70 += ADD[0]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 10
	t7_t5_mem0 += MUL_mem[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 10
	t7_t5_mem1 += MUL_mem[0]

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	S += t260_mem0 >= 11
	t260_mem0 += ADD_mem[0]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 11
	t4_t1 += ADD[0]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 11
	t6_t2_mem0 += INPUT_mem_r

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 11
	t6_t2_mem1 += INPUT_mem_r

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 11
	t7_t5 += ADD[1]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 12
	t01_mem0 += MUL_mem[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 12
	t0_t5_mem0 += MUL_mem[0]

	t260 = S.Task('t260', length=1, delay_cost=1)
	S += t260 >= 12
	t260 += ADD[1]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 12
	t3_t3_mem0 += INPUT_mem_r

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 12
	t3_t3_mem1 += INPUT_mem_r

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 12
	t6_t2 += ADD[0]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 13
	t01 += ADD[2]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 13
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 13
	t0_t0_mem1 += INPUT_mem_r

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 13
	t0_t5 += ADD[3]

	t270_mem0 = S.Task('t270_mem0', length=1, delay_cost=1)
	S += t270_mem0 >= 13
	t270_mem0 += ADD_mem[1]

	t270_mem1 = S.Task('t270_mem1', length=1, delay_cost=1)
	S += t270_mem1 >= 13
	t270_mem1 += ADD_mem[0]

	t3_t3 = S.Task('t3_t3', length=1, delay_cost=1)
	S += t3_t3 >= 13
	t3_t3 += ADD[1]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 14
	t0_t0 += ADD[1]

	t270 = S.Task('t270', length=1, delay_cost=1)
	S += t270 >= 14
	t270 += ADD[2]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 14
	t30_mem0 += MUL_mem[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 14
	t30_mem1 += MUL_mem[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 14
	t5_t2_mem0 += INPUT_mem_r

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 14
	t5_t2_mem1 += INPUT_mem_r

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 15
	t11_mem0 += INPUT_mem_r

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 15
	t11_mem1 += INPUT_mem_r

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 15
	t30 += ADD[1]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 15
	t5_t2 += ADD[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 15
	t60_mem0 += MUL_mem[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 15
	t60_mem1 += MUL_mem[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 16
	t10_mem0 += INPUT_mem_r

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 16
	t10_mem1 += INPUT_mem_r

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 16
	t11 += ADD[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 16
	t110_mem0 += ADD_mem[1]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 16
	t50_mem0 += MUL_mem[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 16
	t50_mem1 += MUL_mem[0]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 16
	t60 += ADD[3]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 17
	t10 += ADD[1]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 17
	t110 += ADD[0]

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	S += t220_mem0 >= 17
	t220_mem0 += ADD_mem[3]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 17
	t3_t2_mem0 += INPUT_mem_r

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 17
	t3_t2_mem1 += INPUT_mem_r

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 17
	t41_mem0 += MUL_mem[0]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 17
	t4_t5_mem0 += MUL_mem[0]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 17
	t50 += ADD[2]

	t220 = S.Task('t220', length=1, delay_cost=1)
	S += t220 >= 18
	t220 += ADD[0]

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	S += t290_mem0 >= 18
	t290_mem0 += ADD_mem[2]

	t3_t2 = S.Task('t3_t2', length=1, delay_cost=1)
	S += t3_t2 >= 18
	t3_t2 += ADD[1]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 18
	t41 += ADD[2]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 18
	t4_t0_mem0 += INPUT_mem_r

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 18
	t4_t0_mem1 += INPUT_mem_r

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	S += t4_t5 >= 18
	t4_t5 += ADD[3]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 18
	t6_t5_mem0 += MUL_mem[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 18
	t6_t5_mem1 += MUL_mem[0]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 19
	t151_mem0 += ADD_mem[2]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 19
	t151_mem1 += ADD_mem[2]

	t230_mem0 = S.Task('t230_mem0', length=1, delay_cost=1)
	S += t230_mem0 >= 19
	t230_mem0 += ADD_mem[0]

	t230_mem1 = S.Task('t230_mem1', length=1, delay_cost=1)
	S += t230_mem1 >= 19
	t230_mem1 += ADD_mem[3]

	t290 = S.Task('t290', length=1, delay_cost=1)
	S += t290 >= 19
	t290 += ADD[2]

	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	S += t3_t4_in >= 19
	t3_t4_in += MUL_in[0]

	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	S += t3_t4_mem0 >= 19
	t3_t4_mem0 += ADD_mem[1]

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	S += t3_t4_mem1 >= 19
	t3_t4_mem1 += ADD_mem[1]

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	S += t3_t5_mem0 >= 19
	t3_t5_mem0 += MUL_mem[0]

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	S += t3_t5_mem1 >= 19
	t3_t5_mem1 += MUL_mem[0]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 19
	t4_t0 += ADD[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 19
	t5_t3_mem0 += INPUT_mem_r

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 19
	t5_t3_mem1 += INPUT_mem_r

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	S += t6_t5 >= 19
	t6_t5 += ADD[0]

	t151 = S.Task('t151', length=1, delay_cost=1)
	S += t151 >= 20
	t151 += ADD[0]

	t230 = S.Task('t230', length=1, delay_cost=1)
	S += t230 >= 20
	t230 += ADD[3]

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	S += t300_mem0 >= 20
	t300_mem0 += ADD_mem[2]

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	S += t300_mem1 >= 20
	t300_mem1 += ADD_mem[2]

	t3_t4 = S.Task('t3_t4', length=7, delay_cost=1)
	S += t3_t4 >= 20
	t3_t4 += MUL[0]

	t3_t5 = S.Task('t3_t5', length=1, delay_cost=1)
	S += t3_t5 >= 20
	t3_t5 += ADD[1]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 20
	t4_t2_in += MUL_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 20
	t4_t2_mem0 += ADD_mem[1]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 20
	t4_t2_mem1 += ADD_mem[0]

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 20
	t5_t3 += ADD[2]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 20
	t5_t5_mem0 += MUL_mem[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 20
	t5_t5_mem1 += MUL_mem[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 20
	t7_t3_mem0 += INPUT_mem_r

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 20
	t7_t3_mem1 += INPUT_mem_r

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 21
	t161_mem0 += ADD_mem[0]

	t300 = S.Task('t300', length=1, delay_cost=1)
	S += t300 >= 21
	t300 += ADD[2]

	t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
	S += t4_t2 >= 21
	t4_t2 += MUL[0]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 21
	t5_t4_in += MUL_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 21
	t5_t4_mem0 += ADD_mem[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 21
	t5_t4_mem1 += ADD_mem[2]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 21
	t5_t5 += ADD[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 21
	t7_t2_mem0 += INPUT_mem_r

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 21
	t7_t2_mem1 += INPUT_mem_r

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 21
	t7_t3 += ADD[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 22
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 22
	t0_t1_mem1 += INPUT_mem_r

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 22
	t161 += ADD[1]

	t5_t4 = S.Task('t5_t4', length=7, delay_cost=1)
	S += t5_t4 >= 22
	t5_t4 += MUL[0]

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 22
	t7_t2 += ADD[2]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 23
	t0_t1 += ADD[3]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 23
	t6_t3_mem0 += INPUT_mem_r

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 23
	t6_t3_mem1 += INPUT_mem_r

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 23
	t7_t4_in += MUL_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 23
	t7_t4_mem0 += ADD_mem[2]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 23
	t7_t4_mem1 += ADD_mem[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 24
	t0_t2_in += MUL_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 24
	t0_t2_mem0 += ADD_mem[1]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 24
	t0_t2_mem1 += ADD_mem[3]

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 24
	t6_t3 += ADD[1]

	t7_t4 = S.Task('t7_t4', length=7, delay_cost=1)
	S += t7_t4 >= 24
	t7_t4 += MUL[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 24
	t80_mem0 += ADD_mem[1]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 24
	t80_mem1 += INPUT_mem_r

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 24
	t81_mem0 += ADD_mem[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 24
	t81_mem1 += INPUT_mem_r

	t0_t2 = S.Task('t0_t2', length=7, delay_cost=1)
	S += t0_t2 >= 25
	t0_t2 += MUL[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 25
	t20_mem0 += ADD_mem[1]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 25
	t20_mem1 += INPUT_mem_r

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 25
	t21_mem0 += ADD_mem[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 25
	t21_mem1 += INPUT_mem_r

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 25
	t6_t4_in += MUL_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 25
	t6_t4_mem0 += ADD_mem[0]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 25
	t6_t4_mem1 += ADD_mem[1]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 25
	t80 += ADD[3]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 25
	t81 += ADD[1]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 26
	t20 += ADD[0]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 26
	t21 += ADD[2]

	t280_mem0 = S.Task('t280_mem0', length=1, delay_cost=1)
	S += t280_mem0 >= 26
	t280_mem0 += ADD_mem[2]

	t280_mem1 = S.Task('t280_mem1', length=1, delay_cost=1)
	S += t280_mem1 >= 26
	t280_mem1 += INPUT_mem_r

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	S += t310_mem0 >= 26
	t310_mem0 += ADD_mem[2]

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	S += t310_mem1 >= 26
	t310_mem1 += INPUT_mem_r

	t6_t4 = S.Task('t6_t4', length=7, delay_cost=1)
	S += t6_t4 >= 26
	t6_t4 += MUL[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 26
	t9_t0_mem0 += ADD_mem[3]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 26
	t9_t0_mem1 += ADD_mem[1]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 26
	t9_t3_in += MUL_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 26
	t9_t3_mem0 += ADD_mem[3]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 26
	t9_t3_mem1 += ADD_mem[1]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 27
	t10_t0_mem0 += ADD_mem[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 27
	t10_t0_mem1 += ADD_mem[2]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 27
	t10_t3_in += MUL_in[0]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 27
	t10_t3_mem0 += ADD_mem[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 27
	t10_t3_mem1 += ADD_mem[2]

	t280 = S.Task('t280', length=1, delay_cost=1)
	S += t280 >= 27
	t280 += ADD[3]

	t310 = S.Task('t310', length=1, delay_cost=1)
	S += t310 >= 27
	t310 += ADD[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 27
	t31_mem0 += MUL_mem[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 27
	t31_mem1 += ADD_mem[1]

	t9_t0 = S.Task('t9_t0', length=1, delay_cost=1)
	S += t9_t0 >= 27
	t9_t0 += ADD[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 27
	t9_t1_mem0 += ADD_mem[3]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 27
	t9_t1_mem1 += ADD_mem[1]

	t9_t3 = S.Task('t9_t3', length=7, delay_cost=1)
	S += t9_t3 >= 27
	t9_t3 += MUL[0]

	t10_t0 = S.Task('t10_t0', length=1, delay_cost=1)
	S += t10_t0 >= 28
	t10_t0 += ADD[3]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 28
	t10_t1_mem0 += ADD_mem[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 28
	t10_t1_mem1 += ADD_mem[2]

	t10_t3 = S.Task('t10_t3', length=7, delay_cost=1)
	S += t10_t3 >= 28
	t10_t3 += MUL[0]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 28
	t31 += ADD[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 28
	t40_mem0 += MUL_mem[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 28
	t40_mem1 += ADD_mem[3]

	t9_t1 = S.Task('t9_t1', length=1, delay_cost=1)
	S += t9_t1 >= 28
	t9_t1 += ADD[2]

	t10_t1 = S.Task('t10_t1', length=1, delay_cost=1)
	S += t10_t1 >= 29
	t10_t1 += ADD[0]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 29
	t111_mem0 += ADD_mem[1]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 29
	t40 += ADD[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 29
	t51_mem0 += MUL_mem[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 29
	t51_mem1 += ADD_mem[0]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 29
	t9_t2_in += MUL_in[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 29
	t9_t2_mem0 += ADD_mem[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 29
	t9_t2_mem1 += ADD_mem[2]

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 30
	t10_t2_in += MUL_in[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 30
	t10_t2_mem0 += ADD_mem[3]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 30
	t10_t2_mem1 += ADD_mem[0]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 30
	t111 += ADD[3]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 30
	t180_mem0 += ADD_mem[1]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 30
	t180_mem1 += ADD_mem[2]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 30
	t181_mem0 += ADD_mem[2]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 30
	t181_mem1 += ADD_mem[1]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 30
	t51 += ADD[1]

	t9_t2 = S.Task('t9_t2', length=7, delay_cost=1)
	S += t9_t2 >= 30
	t9_t2 += MUL[0]

	t10_t2 = S.Task('t10_t2', length=7, delay_cost=1)
	S += t10_t2 >= 31
	t10_t2 += MUL[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 31
	t120_mem0 += ADD_mem[0]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 31
	t120_mem1 += ADD_mem[3]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 31
	t121_mem0 += ADD_mem[3]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 31
	t121_mem1 += ADD_mem[0]

	t180 = S.Task('t180', length=1, delay_cost=1)
	S += t180 >= 31
	t180 += ADD[1]

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 31
	t181 += ADD[0]

	t291_mem0 = S.Task('t291_mem0', length=1, delay_cost=1)
	S += t291_mem0 >= 31
	t291_mem0 += ADD_mem[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 31
	t71_mem0 += MUL_mem[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 31
	t71_mem1 += ADD_mem[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 32
	t00_mem0 += MUL_mem[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 32
	t00_mem1 += ADD_mem[3]

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 32
	t120 += ADD[3]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 32
	t121 += ADD[2]

	t190_mem0 = S.Task('t190_mem0', length=1, delay_cost=1)
	S += t190_mem0 >= 32
	t190_mem0 += ADD_mem[1]

	t190_mem1 = S.Task('t190_mem1', length=1, delay_cost=1)
	S += t190_mem1 >= 32
	t190_mem1 += ADD_mem[0]

	t191_mem0 = S.Task('t191_mem0', length=1, delay_cost=1)
	S += t191_mem0 >= 32
	t191_mem0 += ADD_mem[0]

	t191_mem1 = S.Task('t191_mem1', length=1, delay_cost=1)
	S += t191_mem1 >= 32
	t191_mem1 += ADD_mem[3]

	t291 = S.Task('t291', length=1, delay_cost=1)
	S += t291 >= 32
	t291 += ADD[1]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 32
	t71 += ADD[0]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 33
	t00 += ADD[0]

	t190 = S.Task('t190', length=1, delay_cost=1)
	S += t190 >= 33
	t190 += ADD[2]

	t191 = S.Task('t191', length=1, delay_cost=1)
	S += t191 >= 33
	t191 += ADD[3]

	t261_mem0 = S.Task('t261_mem0', length=1, delay_cost=1)
	S += t261_mem0 >= 33
	t261_mem0 += ADD_mem[0]

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	S += t301_mem0 >= 33
	t301_mem0 += ADD_mem[1]

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	S += t301_mem1 >= 33
	t301_mem1 += ADD_mem[1]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 33
	t61_mem0 += MUL_mem[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 33
	t61_mem1 += ADD_mem[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 34
	t150_mem0 += ADD_mem[0]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 34
	t150_mem1 += ADD_mem[1]

	t261 = S.Task('t261', length=1, delay_cost=1)
	S += t261 >= 34
	t261 += ADD[0]

	t301 = S.Task('t301', length=1, delay_cost=1)
	S += t301 >= 34
	t301 += ADD[2]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 34
	t61 += ADD[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 34
	t91_mem0 += MUL_mem[0]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 34
	t9_t5_mem0 += MUL_mem[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 35
	t101_mem0 += MUL_mem[0]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 35
	t10_t5_mem0 += MUL_mem[0]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 35
	t150 += ADD[2]

	t221_mem0 = S.Task('t221_mem0', length=1, delay_cost=1)
	S += t221_mem0 >= 35
	t221_mem0 += ADD_mem[3]

	t271_mem0 = S.Task('t271_mem0', length=1, delay_cost=1)
	S += t271_mem0 >= 35
	t271_mem0 += ADD_mem[0]

	t271_mem1 = S.Task('t271_mem1', length=1, delay_cost=1)
	S += t271_mem1 >= 35
	t271_mem1 += ADD_mem[0]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 35
	t91 += ADD[1]

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	S += t9_t5 >= 35
	t9_t5 += ADD[3]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 36
	t101 += ADD[3]

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 36
	t10_t5 += ADD[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 36
	t160_mem0 += ADD_mem[2]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 36
	t171_mem0 += ADD_mem[1]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 36
	t171_mem1 += ADD_mem[1]

	t221 = S.Task('t221', length=1, delay_cost=1)
	S += t221 >= 36
	t221 += ADD[1]

	t271 = S.Task('t271', length=1, delay_cost=1)
	S += t271 >= 36
	t271 += ADD[2]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 37
	t160 += ADD[0]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 37
	t171 += ADD[3]

	t231_mem0 = S.Task('t231_mem0', length=1, delay_cost=1)
	S += t231_mem0 >= 37
	t231_mem0 += ADD_mem[1]

	t231_mem1 = S.Task('t231_mem1', length=1, delay_cost=1)
	S += t231_mem1 >= 37
	t231_mem1 += ADD_mem[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 37
	t90_mem0 += MUL_mem[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 37
	t90_mem1 += ADD_mem[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 38
	t100_mem0 += MUL_mem[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 38
	t100_mem1 += ADD_mem[0]

	t231 = S.Task('t231', length=1, delay_cost=1)
	S += t231 >= 38
	t231 += ADD[0]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 38
	t90 += ADD[3]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 39
	t100 += ADD[3]


	# new tasks
	t130 = S.Task('t130', length=1, delay_cost=1)
	t130 += alt(ADD)

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += ADD_mem[0]
	S += 34 < t130_mem0
	S += t130_mem0 <= t130

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	t130_mem1 += ADD_mem[3]
	S += 33 < t130_mem1
	S += t130_mem1 <= t130

	t131 = S.Task('t131', length=1, delay_cost=1)
	t131 += alt(ADD)

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += ADD_mem[2]
	S += 14 < t131_mem0
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += ADD_mem[2]
	S += 33 < t131_mem1
	S += t131_mem1 <= t131

	t311 = S.Task('t311', length=1, delay_cost=1)
	t311 += alt(ADD)

	t311_mem0 = S.Task('t311_mem0', length=1, delay_cost=1)
	t311_mem0 += ADD_mem[2]
	S += 35 < t311_mem0
	S += t311_mem0 <= t311

	t311_mem1 = S.Task('t311_mem1', length=1, delay_cost=1)
	t311_mem1 += INPUT_mem_r
	S += t311_mem1 <= t311

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(ADD)

	S += 27<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += ADD_mem[2]
	S += 28 < c010_mem0
	S += c010_mem0 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010 <= c010_w

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(ADD)

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += ADD_mem[3]
	S += 39 < t170_mem0
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += ADD_mem[0]
	S += 38 < t170_mem1
	S += t170_mem1 <= t170

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(ADD)

	S += 21<c111

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += ADD_mem[3]
	S += 37 < c111_mem0
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += ADD_mem[3]
	S += 38 < c111_mem1
	S += c111_mem1 <= c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(INPUT_mem_w)
	S += c111 <= c111_w

	t200 = S.Task('t200', length=1, delay_cost=1)
	t200 += alt(ADD)

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	t200_mem0 += ADD_mem[2]
	S += 34 < t200_mem0
	S += t200_mem0 <= t200

	t201 = S.Task('t201', length=1, delay_cost=1)
	t201 += alt(ADD)

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	t201_mem0 += ADD_mem[3]
	S += 34 < t201_mem0
	S += t201_mem0 <= t201

	t240 = S.Task('t240', length=1, delay_cost=1)
	t240 += alt(ADD)

	t240_mem0 = S.Task('t240_mem0', length=1, delay_cost=1)
	t240_mem0 += ADD_mem[3]
	S += 21 < t240_mem0
	S += t240_mem0 <= t240

	t240_mem1 = S.Task('t240_mem1', length=1, delay_cost=1)
	t240_mem1 += ADD_mem[0]
	S += 39 < t240_mem1
	S += t240_mem1 <= t240

	t241 = S.Task('t241', length=1, delay_cost=1)
	t241 += alt(ADD)

	t241_mem0 = S.Task('t241_mem0', length=1, delay_cost=1)
	t241_mem0 += ADD_mem[0]
	S += 39 < t241_mem0
	S += t241_mem0 <= t241

	t241_mem1 = S.Task('t241_mem1', length=1, delay_cost=1)
	t241_mem1 += ADD_mem[3]
	S += 21 < t241_mem1
	S += t241_mem1 <= t241

	t281 = S.Task('t281', length=1, delay_cost=1)
	t281 += alt(ADD)

	t281_mem0 = S.Task('t281_mem0', length=1, delay_cost=1)
	t281_mem0 += ADD_mem[2]
	S += 37 < t281_mem0
	S += t281_mem0 <= t281

	t281_mem1 = S.Task('t281_mem1', length=1, delay_cost=1)
	t281_mem1 += INPUT_mem_r
	S += t281_mem1 <= t281

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(ADD)

	S += 27<c210

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += ADD_mem[3]
	S += 28 < c210_mem0
	S += c210_mem0 <= c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(INPUT_mem_w)
	S += c210 <= c210_w

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(ADD)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(ADD_mem)
	S += (t130*ADD[0]) < t140_mem0*ADD_mem[0]
	S += (t130*ADD[1]) < t140_mem0*ADD_mem[1]
	S += (t130*ADD[2]) < t140_mem0*ADD_mem[2]
	S += (t130*ADD[3]) < t140_mem0*ADD_mem[3]
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += INPUT_mem_r
	S += t140_mem1 <= t140

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(ADD)

	S += 23<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(ADD_mem)
	S += (t131*ADD[0]) < c001_mem0*ADD_mem[0]
	S += (t131*ADD[1]) < c001_mem0*ADD_mem[1]
	S += (t131*ADD[2]) < c001_mem0*ADD_mem[2]
	S += (t131*ADD[3]) < c001_mem0*ADD_mem[3]
	S += c001_mem0 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(INPUT_mem_w)
	S += c001 <= c001_w

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(ADD)

	S += 20<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(ADD_mem)
	S += (t311*ADD[0]) < c011_mem0*ADD_mem[0]
	S += (t311*ADD[1]) < c011_mem0*ADD_mem[1]
	S += (t311*ADD[2]) < c011_mem0*ADD_mem[2]
	S += (t311*ADD[3]) < c011_mem0*ADD_mem[3]
	S += c011_mem0 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(INPUT_mem_w)
	S += c011 <= c011_w

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(ADD)

	S += 21<c110

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += ADD_mem[3]
	S += 40 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += alt(ADD_mem)
	S += (t170*ADD[0]) < c110_mem1*ADD_mem[0]
	S += (t170*ADD[1]) < c110_mem1*ADD_mem[1]
	S += (t170*ADD[2]) < c110_mem1*ADD_mem[2]
	S += (t170*ADD[3]) < c110_mem1*ADD_mem[3]
	S += c110_mem1 <= c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(INPUT_mem_w)
	S += c110 <= c110_w

	t210 = S.Task('t210', length=1, delay_cost=1)
	t210 += alt(ADD)

	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	t210_mem0 += alt(ADD_mem)
	S += (t200*ADD[0]) < t210_mem0*ADD_mem[0]
	S += (t200*ADD[1]) < t210_mem0*ADD_mem[1]
	S += (t200*ADD[2]) < t210_mem0*ADD_mem[2]
	S += (t200*ADD[3]) < t210_mem0*ADD_mem[3]
	S += t210_mem0 <= t210

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	t210_mem1 += ADD_mem[3]
	S += 39 < t210_mem1
	S += t210_mem1 <= t210

	t211 = S.Task('t211', length=1, delay_cost=1)
	t211 += alt(ADD)

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	t211_mem0 += alt(ADD_mem)
	S += (t201*ADD[0]) < t211_mem0*ADD_mem[0]
	S += (t201*ADD[1]) < t211_mem0*ADD_mem[1]
	S += (t201*ADD[2]) < t211_mem0*ADD_mem[2]
	S += (t201*ADD[3]) < t211_mem0*ADD_mem[3]
	S += t211_mem0 <= t211

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	t211_mem1 += ADD_mem[1]
	S += 36 < t211_mem1
	S += t211_mem1 <= t211

	t250 = S.Task('t250', length=1, delay_cost=1)
	t250 += alt(ADD)

	t250_mem0 = S.Task('t250_mem0', length=1, delay_cost=1)
	t250_mem0 += INPUT_mem_r
	S += t250_mem0 <= t250

	t250_mem1 = S.Task('t250_mem1', length=1, delay_cost=1)
	t250_mem1 += alt(ADD_mem)
	S += (t240*ADD[0]) < t250_mem1*ADD_mem[0]
	S += (t240*ADD[1]) < t250_mem1*ADD_mem[1]
	S += (t240*ADD[2]) < t250_mem1*ADD_mem[2]
	S += (t240*ADD[3]) < t250_mem1*ADD_mem[3]
	S += t250_mem1 <= t250

	t251 = S.Task('t251', length=1, delay_cost=1)
	t251 += alt(ADD)

	t251_mem0 = S.Task('t251_mem0', length=1, delay_cost=1)
	t251_mem0 += INPUT_mem_r
	S += t251_mem0 <= t251

	t251_mem1 = S.Task('t251_mem1', length=1, delay_cost=1)
	t251_mem1 += alt(ADD_mem)
	S += (t241*ADD[0]) < t251_mem1*ADD_mem[0]
	S += (t241*ADD[1]) < t251_mem1*ADD_mem[1]
	S += (t241*ADD[2]) < t251_mem1*ADD_mem[2]
	S += (t241*ADD[3]) < t251_mem1*ADD_mem[3]
	S += t251_mem1 <= t251

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(ADD)

	S += 24<c211

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(ADD_mem)
	S += (t281*ADD[0]) < c211_mem0*ADD_mem[0]
	S += (t281*ADD[1]) < c211_mem0*ADD_mem[1]
	S += (t281*ADD[2]) < c211_mem0*ADD_mem[2]
	S += (t281*ADD[3]) < c211_mem0*ADD_mem[3]
	S += c211_mem0 <= c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(INPUT_mem_w)
	S += c211 <= c211_w

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(ADD)

	S += 23<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(ADD_mem)
	S += (t130*ADD[0]) < c000_mem0*ADD_mem[0]
	S += (t130*ADD[1]) < c000_mem0*ADD_mem[1]
	S += (t130*ADD[2]) < c000_mem0*ADD_mem[2]
	S += (t130*ADD[3]) < c000_mem0*ADD_mem[3]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(ADD_mem)
	S += (t140*ADD[0]) < c000_mem1*ADD_mem[0]
	S += (t140*ADD[1]) < c000_mem1*ADD_mem[1]
	S += (t140*ADD[2]) < c000_mem1*ADD_mem[2]
	S += (t140*ADD[3]) < c000_mem1*ADD_mem[3]
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(INPUT_mem_w)
	S += c000 <= c000_w

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(ADD)

	S += 26<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(ADD_mem)
	S += (t210*ADD[0]) < c200_mem0*ADD_mem[0]
	S += (t210*ADD[1]) < c200_mem0*ADD_mem[1]
	S += (t210*ADD[2]) < c200_mem0*ADD_mem[2]
	S += (t210*ADD[3]) < c200_mem0*ADD_mem[3]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += ADD_mem[3]
	S += 40 < c200_mem1
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200 <= c200_w

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(ADD)

	S += 26<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(ADD_mem)
	S += (t211*ADD[0]) < c201_mem0*ADD_mem[0]
	S += (t211*ADD[1]) < c201_mem0*ADD_mem[1]
	S += (t211*ADD[2]) < c201_mem0*ADD_mem[2]
	S += (t211*ADD[3]) < c201_mem0*ADD_mem[3]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += ADD_mem[3]
	S += 37 < c201_mem1
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201 <= c201_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(ADD)

	S += 22<c100

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(ADD_mem)
	S += (t250*ADD[0]) < c100_mem0*ADD_mem[0]
	S += (t250*ADD[1]) < c100_mem0*ADD_mem[1]
	S += (t250*ADD[2]) < c100_mem0*ADD_mem[2]
	S += (t250*ADD[3]) < c100_mem0*ADD_mem[3]
	S += c100_mem0 <= c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(INPUT_mem_w)
	S += c100 <= c100_w

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(ADD)

	S += 22<c101

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(ADD_mem)
	S += (t251*ADD[0]) < c101_mem0*ADD_mem[0]
	S += (t251*ADD[1]) < c101_mem0*ADD_mem[1]
	S += (t251*ADD[2]) < c101_mem0*ADD_mem[2]
	S += (t251*ADD[3]) < c101_mem0*ADD_mem[3]
	S += c101_mem0 <= c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(INPUT_mem_w)
	S += c101 <= c101_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-381/scheduling/SQR012345_mul1_add4/SQR012345_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

