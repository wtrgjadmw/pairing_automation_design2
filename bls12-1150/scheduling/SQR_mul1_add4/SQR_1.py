from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 118
	S = Scenario("SQR_1", horizon=horizon)

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
	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 0
	c_t2_t3_t1_in += MUL_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 0
	c_t2_t3_t1_mem0 += INPUT_mem_r

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 0
	c_t2_t3_t1_mem1 += INPUT_mem_r

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 1
	c_t1_t3_t0_in += MUL_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 1
	c_t1_t3_t0_mem0 += INPUT_mem_r

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 1
	c_t1_t3_t0_mem1 += INPUT_mem_r

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=7, delay_cost=1)
	S += c_t2_t3_t1 >= 1
	c_t2_t3_t1 += MUL[0]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=7, delay_cost=1)
	S += c_t1_t3_t0 >= 2
	c_t1_t3_t0 += MUL[0]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 2
	c_t2_t3_t0_in += MUL_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 2
	c_t2_t3_t0_mem0 += INPUT_mem_r

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 2
	c_t2_t3_t0_mem1 += INPUT_mem_r

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 3
	c_t0_t3_t1_in += MUL_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 3
	c_t0_t3_t1_mem0 += INPUT_mem_r

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 3
	c_t0_t3_t1_mem1 += INPUT_mem_r

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=7, delay_cost=1)
	S += c_t2_t3_t0 >= 3
	c_t2_t3_t0 += MUL[0]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=7, delay_cost=1)
	S += c_t0_t3_t1 >= 4
	c_t0_t3_t1 += MUL[0]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 4
	c_t1_t3_t1_in += MUL_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 4
	c_t1_t3_t1_mem0 += INPUT_mem_r

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 4
	c_t1_t3_t1_mem1 += INPUT_mem_r

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 5
	c_t0_t3_t0_in += MUL_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 5
	c_t0_t3_t0_mem0 += INPUT_mem_r

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 5
	c_t0_t3_t0_mem1 += INPUT_mem_r

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=7, delay_cost=1)
	S += c_t1_t3_t1 >= 5
	c_t1_t3_t1 += MUL[0]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=7, delay_cost=1)
	S += c_t0_t3_t0 >= 6
	c_t0_t3_t0 += MUL[0]

	c_t1_a1__x10_mem0 = S.Task('c_t1_a1__x10_mem0', length=1, delay_cost=1)
	S += c_t1_a1__x10_mem0 >= 6
	c_t1_a1__x10_mem0 += INPUT_mem_r

	c_t2_a1__x00_mem0 = S.Task('c_t2_a1__x00_mem0', length=1, delay_cost=1)
	S += c_t2_a1__x00_mem0 >= 6
	c_t2_a1__x00_mem0 += INPUT_mem_r

	c_t0_a1__x00_mem0 = S.Task('c_t0_a1__x00_mem0', length=1, delay_cost=1)
	S += c_t0_a1__x00_mem0 >= 7
	c_t0_a1__x00_mem0 += INPUT_mem_r

	c_t1_a1__x00_mem0 = S.Task('c_t1_a1__x00_mem0', length=1, delay_cost=1)
	S += c_t1_a1__x00_mem0 >= 7
	c_t1_a1__x00_mem0 += INPUT_mem_r

	c_t1_a1__x10 = S.Task('c_t1_a1__x10', length=1, delay_cost=1)
	S += c_t1_a1__x10 >= 7
	c_t1_a1__x10 += ADD[2]

	c_t2_a1__x00 = S.Task('c_t2_a1__x00', length=1, delay_cost=1)
	S += c_t2_a1__x00 >= 7
	c_t2_a1__x00 += ADD[3]

	c_t0_a1__x00 = S.Task('c_t0_a1__x00', length=1, delay_cost=1)
	S += c_t0_a1__x00 >= 8
	c_t0_a1__x00 += ADD[0]

	c_t0_a1__x10_mem0 = S.Task('c_t0_a1__x10_mem0', length=1, delay_cost=1)
	S += c_t0_a1__x10_mem0 >= 8
	c_t0_a1__x10_mem0 += INPUT_mem_r

	c_t1_a1__x00 = S.Task('c_t1_a1__x00', length=1, delay_cost=1)
	S += c_t1_a1__x00 >= 8
	c_t1_a1__x00 += ADD[2]

	c_t2_a1__x10_mem0 = S.Task('c_t2_a1__x10_mem0', length=1, delay_cost=1)
	S += c_t2_a1__x10_mem0 >= 8
	c_t2_a1__x10_mem0 += INPUT_mem_r

	c_t0_a1__x10 = S.Task('c_t0_a1__x10', length=1, delay_cost=1)
	S += c_t0_a1__x10 >= 9
	c_t0_a1__x10 += ADD[1]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 9
	c_t1_t3_t3_mem0 += INPUT_mem_r

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 9
	c_t1_t3_t3_mem1 += INPUT_mem_r

	c_t2_a1__x10 = S.Task('c_t2_a1__x10', length=1, delay_cost=1)
	S += c_t2_a1__x10 >= 9
	c_t2_a1__x10 += ADD[3]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	S += c_t1_t3_t3 >= 10
	c_t1_t3_t3 += ADD[3]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 10
	c_t4001_mem0 += INPUT_mem_r

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 10
	c_t4001_mem1 += INPUT_mem_r

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 11
	c_t0_t3_t3_mem0 += INPUT_mem_r

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 11
	c_t0_t3_t3_mem1 += INPUT_mem_r

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 11
	c_t4001 += ADD[3]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 12
	c_t0_t3_t2_mem0 += INPUT_mem_r

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 12
	c_t0_t3_t2_mem1 += INPUT_mem_r

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	S += c_t0_t3_t3 >= 12
	c_t0_t3_t3 += ADD[2]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	S += c_t0_t3_t2 >= 13
	c_t0_t3_t2 += ADD[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 13
	c_t3010_mem0 += INPUT_mem_r

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 13
	c_t3010_mem1 += INPUT_mem_r

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 14
	c_t3001_mem0 += INPUT_mem_r

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 14
	c_t3001_mem1 += INPUT_mem_r

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 14
	c_t3010 += ADD[2]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 15
	c_t2_t11_mem0 += INPUT_mem_r

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 15
	c_t2_t11_mem1 += INPUT_mem_r

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 15
	c_t3001 += ADD[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 16
	c_t0_t10_mem0 += INPUT_mem_r

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 16
	c_t0_t10_mem1 += INPUT_mem_r

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 16
	c_t2_t11 += ADD[2]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 17
	c_t0_t10 += ADD[1]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 17
	c_t3000_mem0 += INPUT_mem_r

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 17
	c_t3000_mem1 += INPUT_mem_r

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 18
	c_t1_t3_t2_mem0 += INPUT_mem_r

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 18
	c_t1_t3_t2_mem1 += INPUT_mem_r

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 18
	c_t3000 += ADD[3]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	S += c_t1_t3_t2 >= 19
	c_t1_t3_t2 += ADD[2]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 19
	c_t2_t3_t2_mem0 += INPUT_mem_r

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 19
	c_t2_t3_t2_mem1 += INPUT_mem_r

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	S += c_t2_t3_t2 >= 20
	c_t2_t3_t2 += ADD[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 20
	c_t4000_mem0 += INPUT_mem_r

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 20
	c_t4000_mem1 += INPUT_mem_r

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 21
	c_t2_t10_mem0 += INPUT_mem_r

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 21
	c_t2_t10_mem1 += INPUT_mem_r

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 21
	c_t4000 += ADD[3]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 22
	c_t1_t11_mem0 += INPUT_mem_r

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 22
	c_t1_t11_mem1 += INPUT_mem_r

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 22
	c_t2_t10 += ADD[1]

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 23
	c_t1_t11 += ADD[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 23
	c_t3011_mem0 += INPUT_mem_r

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 23
	c_t3011_mem1 += INPUT_mem_r

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 24
	c_t0_t11_mem0 += INPUT_mem_r

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 24
	c_t0_t11_mem1 += INPUT_mem_r

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 24
	c_t3011 += ADD[2]

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 25
	c_t0_t11 += ADD[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 25
	c_t1_t10_mem0 += INPUT_mem_r

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 25
	c_t1_t10_mem1 += INPUT_mem_r

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 26
	c_t1_t10 += ADD[1]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 26
	c_t2_t3_t3_mem0 += INPUT_mem_r

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 26
	c_t2_t3_t3_mem1 += INPUT_mem_r

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	S += c_t2_t3_t3 >= 27
	c_t2_t3_t3 += ADD[3]


	# new tasks
	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	c_t4010 += alt(ADD)

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	c_t4010_mem0 += INPUT_mem_r
	S += c_t4010_mem0 <= c_t4010

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	c_t4010_mem1 += INPUT_mem_r
	S += c_t4010_mem1 <= c_t4010

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	c_t4011 += alt(ADD)

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	c_t4011_mem0 += INPUT_mem_r
	S += c_t4011_mem0 <= c_t4011

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	c_t4011_mem1 += INPUT_mem_r
	S += c_t4011_mem1 <= c_t4011

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	c_t5000 += alt(ADD)

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	c_t5000_mem0 += INPUT_mem_r
	S += c_t5000_mem0 <= c_t5000

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	c_t5000_mem1 += INPUT_mem_r
	S += c_t5000_mem1 <= c_t5000

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	c_t5001 += alt(ADD)

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	c_t5001_mem0 += INPUT_mem_r
	S += c_t5001_mem0 <= c_t5001

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	c_t5001_mem1 += INPUT_mem_r
	S += c_t5001_mem1 <= c_t5001

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	c_t5010 += alt(ADD)

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	c_t5010_mem0 += INPUT_mem_r
	S += c_t5010_mem0 <= c_t5010

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	c_t5010_mem1 += INPUT_mem_r
	S += c_t5010_mem1 <= c_t5010

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	c_t5011 += alt(ADD)

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	c_t5011_mem0 += INPUT_mem_r
	S += c_t5011_mem0 <= c_t5011

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	c_t5011_mem1 += INPUT_mem_r
	S += c_t5011_mem1 <= c_t5011

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/pairing_automation_design2/bls12-1150/scheduling/SQR_mul1_add4/SQR_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

