from pyschedule import Scenario, solvers, plotters, alt

def solve_inv_mul1_add4_0(ConstStep, ExpStep):
	horizon = 134
	S=Scenario("inv_mul1_add4_0",horizon = horizon)

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
	T0a10_new = S.Task('T0a10_new', length=1, delay_cost=1)
	T0a10_new += alt(ADD)

	T0a10_new_mem0 = S.Task('T0a10_new_mem0', length=1, delay_cost=1)
	T0a10_new_mem0 += INPUT_mem_r
	S += T0a10_new_mem0<=T0a10_new

	T0a10_new_mem1 = S.Task('T0a10_new_mem1', length=1, delay_cost=1)
	T0a10_new_mem1 += INPUT_mem_r
	S += T0a10_new_mem1<=T0a10_new

	T0a11_new = S.Task('T0a11_new', length=1, delay_cost=1)
	T0a11_new += alt(ADD)

	T0a11_new_mem0 = S.Task('T0a11_new_mem0', length=1, delay_cost=1)
	T0a11_new_mem0 += INPUT_mem_r
	S += T0a11_new_mem0<=T0a11_new

	T0a11_new_mem1 = S.Task('T0a11_new_mem1', length=1, delay_cost=1)
	T0a11_new_mem1 += INPUT_mem_r
	S += T0a11_new_mem1<=T0a11_new

	T0t10 = S.Task('T0t10', length=1, delay_cost=1)
	T0t10 += alt(ADD)

	T0t10_mem0 = S.Task('T0t10_mem0', length=1, delay_cost=1)
	T0t10_mem0 += INPUT_mem_r
	S += T0t10_mem0<=T0t10

	T0t10_mem1 = S.Task('T0t10_mem1', length=1, delay_cost=1)
	T0t10_mem1 += INPUT_mem_r
	S += T0t10_mem1<=T0t10

	T0t11 = S.Task('T0t11', length=1, delay_cost=1)
	T0t11 += alt(ADD)

	T0t11_mem0 = S.Task('T0t11_mem0', length=1, delay_cost=1)
	T0t11_mem0 += INPUT_mem_r
	S += T0t11_mem0<=T0t11

	T0t11_mem1 = S.Task('T0t11_mem1', length=1, delay_cost=1)
	T0t11_mem1 += INPUT_mem_r
	S += T0t11_mem1<=T0t11

	T0t0_a0a1_in = S.Task('T0t0_a0a1_in', length=1, delay_cost=1)
	T0t0_a0a1_in += alt(MUL_in)
	T0t0_a0a1 = S.Task('T0t0_a0a1', length=7, delay_cost=1)
	T0t0_a0a1 += alt(MUL)
	S+=T0t0_a0a1>=T0t0_a0a1_in

	T0t0_a0a1_mem0 = S.Task('T0t0_a0a1_mem0', length=1, delay_cost=1)
	T0t0_a0a1_mem0 += INPUT_mem_r
	S += T0t0_a0a1_mem0<=T0t0_a0a1

	T0t0_a0a1_mem1 = S.Task('T0t0_a0a1_mem1', length=1, delay_cost=1)
	T0t0_a0a1_mem1 += INPUT_mem_r
	S += T0t0_a0a1_mem1<=T0t0_a0a1

	T0t1_a0a1_in = S.Task('T0t1_a0a1_in', length=1, delay_cost=1)
	T0t1_a0a1_in += alt(MUL_in)
	T0t1_a0a1 = S.Task('T0t1_a0a1', length=7, delay_cost=1)
	T0t1_a0a1 += alt(MUL)
	S+=T0t1_a0a1>=T0t1_a0a1_in

	T0t1_a0a1_mem0 = S.Task('T0t1_a0a1_mem0', length=1, delay_cost=1)
	T0t1_a0a1_mem0 += INPUT_mem_r
	S += T0t1_a0a1_mem0<=T0t1_a0a1

	T0t1_a0a1_mem1 = S.Task('T0t1_a0a1_mem1', length=1, delay_cost=1)
	T0t1_a0a1_mem1 += INPUT_mem_r
	S += T0t1_a0a1_mem1<=T0t1_a0a1

	T0t2_a0a1 = S.Task('T0t2_a0a1', length=1, delay_cost=1)
	T0t2_a0a1 += alt(ADD)

	T0t2_a0a1_mem0 = S.Task('T0t2_a0a1_mem0', length=1, delay_cost=1)
	T0t2_a0a1_mem0 += INPUT_mem_r
	S += T0t2_a0a1_mem0<=T0t2_a0a1

	T0t2_a0a1_mem1 = S.Task('T0t2_a0a1_mem1', length=1, delay_cost=1)
	T0t2_a0a1_mem1 += INPUT_mem_r
	S += T0t2_a0a1_mem1<=T0t2_a0a1

	T1a10_new = S.Task('T1a10_new', length=1, delay_cost=1)
	T1a10_new += alt(ADD)

	T1a10_new_mem0 = S.Task('T1a10_new_mem0', length=1, delay_cost=1)
	T1a10_new_mem0 += INPUT_mem_r
	S += T1a10_new_mem0<=T1a10_new

	T1a10_new_mem1 = S.Task('T1a10_new_mem1', length=1, delay_cost=1)
	T1a10_new_mem1 += INPUT_mem_r
	S += T1a10_new_mem1<=T1a10_new

	T1a11_new = S.Task('T1a11_new', length=1, delay_cost=1)
	T1a11_new += alt(ADD)

	T1a11_new_mem0 = S.Task('T1a11_new_mem0', length=1, delay_cost=1)
	T1a11_new_mem0 += INPUT_mem_r
	S += T1a11_new_mem0<=T1a11_new

	T1a11_new_mem1 = S.Task('T1a11_new_mem1', length=1, delay_cost=1)
	T1a11_new_mem1 += INPUT_mem_r
	S += T1a11_new_mem1<=T1a11_new

	T1t10 = S.Task('T1t10', length=1, delay_cost=1)
	T1t10 += alt(ADD)

	T1t10_mem0 = S.Task('T1t10_mem0', length=1, delay_cost=1)
	T1t10_mem0 += INPUT_mem_r
	S += T1t10_mem0<=T1t10

	T1t10_mem1 = S.Task('T1t10_mem1', length=1, delay_cost=1)
	T1t10_mem1 += INPUT_mem_r
	S += T1t10_mem1<=T1t10

	T1t11 = S.Task('T1t11', length=1, delay_cost=1)
	T1t11 += alt(ADD)

	T1t11_mem0 = S.Task('T1t11_mem0', length=1, delay_cost=1)
	T1t11_mem0 += INPUT_mem_r
	S += T1t11_mem0<=T1t11

	T1t11_mem1 = S.Task('T1t11_mem1', length=1, delay_cost=1)
	T1t11_mem1 += INPUT_mem_r
	S += T1t11_mem1<=T1t11

	T1t0_a0a1_in = S.Task('T1t0_a0a1_in', length=1, delay_cost=1)
	T1t0_a0a1_in += alt(MUL_in)
	T1t0_a0a1 = S.Task('T1t0_a0a1', length=7, delay_cost=1)
	T1t0_a0a1 += alt(MUL)
	S+=T1t0_a0a1>=T1t0_a0a1_in

	T1t0_a0a1_mem0 = S.Task('T1t0_a0a1_mem0', length=1, delay_cost=1)
	T1t0_a0a1_mem0 += INPUT_mem_r
	S += T1t0_a0a1_mem0<=T1t0_a0a1

	T1t0_a0a1_mem1 = S.Task('T1t0_a0a1_mem1', length=1, delay_cost=1)
	T1t0_a0a1_mem1 += INPUT_mem_r
	S += T1t0_a0a1_mem1<=T1t0_a0a1

	T1t1_a0a1_in = S.Task('T1t1_a0a1_in', length=1, delay_cost=1)
	T1t1_a0a1_in += alt(MUL_in)
	T1t1_a0a1 = S.Task('T1t1_a0a1', length=7, delay_cost=1)
	T1t1_a0a1 += alt(MUL)
	S+=T1t1_a0a1>=T1t1_a0a1_in

	T1t1_a0a1_mem0 = S.Task('T1t1_a0a1_mem0', length=1, delay_cost=1)
	T1t1_a0a1_mem0 += INPUT_mem_r
	S += T1t1_a0a1_mem0<=T1t1_a0a1

	T1t1_a0a1_mem1 = S.Task('T1t1_a0a1_mem1', length=1, delay_cost=1)
	T1t1_a0a1_mem1 += INPUT_mem_r
	S += T1t1_a0a1_mem1<=T1t1_a0a1

	T1t2_a0a1 = S.Task('T1t2_a0a1', length=1, delay_cost=1)
	T1t2_a0a1 += alt(ADD)

	T1t2_a0a1_mem0 = S.Task('T1t2_a0a1_mem0', length=1, delay_cost=1)
	T1t2_a0a1_mem0 += INPUT_mem_r
	S += T1t2_a0a1_mem0<=T1t2_a0a1

	T1t2_a0a1_mem1 = S.Task('T1t2_a0a1_mem1', length=1, delay_cost=1)
	T1t2_a0a1_mem1 += INPUT_mem_r
	S += T1t2_a0a1_mem1<=T1t2_a0a1

	T2a10_new = S.Task('T2a10_new', length=1, delay_cost=1)
	T2a10_new += alt(ADD)

	T2a10_new_mem0 = S.Task('T2a10_new_mem0', length=1, delay_cost=1)
	T2a10_new_mem0 += INPUT_mem_r
	S += T2a10_new_mem0<=T2a10_new

	T2a10_new_mem1 = S.Task('T2a10_new_mem1', length=1, delay_cost=1)
	T2a10_new_mem1 += INPUT_mem_r
	S += T2a10_new_mem1<=T2a10_new

	T2a11_new = S.Task('T2a11_new', length=1, delay_cost=1)
	T2a11_new += alt(ADD)

	T2a11_new_mem0 = S.Task('T2a11_new_mem0', length=1, delay_cost=1)
	T2a11_new_mem0 += INPUT_mem_r
	S += T2a11_new_mem0<=T2a11_new

	T2a11_new_mem1 = S.Task('T2a11_new_mem1', length=1, delay_cost=1)
	T2a11_new_mem1 += INPUT_mem_r
	S += T2a11_new_mem1<=T2a11_new

	T2t10 = S.Task('T2t10', length=1, delay_cost=1)
	T2t10 += alt(ADD)

	T2t10_mem0 = S.Task('T2t10_mem0', length=1, delay_cost=1)
	T2t10_mem0 += INPUT_mem_r
	S += T2t10_mem0<=T2t10

	T2t10_mem1 = S.Task('T2t10_mem1', length=1, delay_cost=1)
	T2t10_mem1 += INPUT_mem_r
	S += T2t10_mem1<=T2t10

	T2t11 = S.Task('T2t11', length=1, delay_cost=1)
	T2t11 += alt(ADD)

	T2t11_mem0 = S.Task('T2t11_mem0', length=1, delay_cost=1)
	T2t11_mem0 += INPUT_mem_r
	S += T2t11_mem0<=T2t11

	T2t11_mem1 = S.Task('T2t11_mem1', length=1, delay_cost=1)
	T2t11_mem1 += INPUT_mem_r
	S += T2t11_mem1<=T2t11

	T2t0_a0a1_in = S.Task('T2t0_a0a1_in', length=1, delay_cost=1)
	T2t0_a0a1_in += alt(MUL_in)
	T2t0_a0a1 = S.Task('T2t0_a0a1', length=7, delay_cost=1)
	T2t0_a0a1 += alt(MUL)
	S+=T2t0_a0a1>=T2t0_a0a1_in

	T2t0_a0a1_mem0 = S.Task('T2t0_a0a1_mem0', length=1, delay_cost=1)
	T2t0_a0a1_mem0 += INPUT_mem_r
	S += T2t0_a0a1_mem0<=T2t0_a0a1

	T2t0_a0a1_mem1 = S.Task('T2t0_a0a1_mem1', length=1, delay_cost=1)
	T2t0_a0a1_mem1 += INPUT_mem_r
	S += T2t0_a0a1_mem1<=T2t0_a0a1

	T2t1_a0a1_in = S.Task('T2t1_a0a1_in', length=1, delay_cost=1)
	T2t1_a0a1_in += alt(MUL_in)
	T2t1_a0a1 = S.Task('T2t1_a0a1', length=7, delay_cost=1)
	T2t1_a0a1 += alt(MUL)
	S+=T2t1_a0a1>=T2t1_a0a1_in

	T2t1_a0a1_mem0 = S.Task('T2t1_a0a1_mem0', length=1, delay_cost=1)
	T2t1_a0a1_mem0 += INPUT_mem_r
	S += T2t1_a0a1_mem0<=T2t1_a0a1

	T2t1_a0a1_mem1 = S.Task('T2t1_a0a1_mem1', length=1, delay_cost=1)
	T2t1_a0a1_mem1 += INPUT_mem_r
	S += T2t1_a0a1_mem1<=T2t1_a0a1

	T2t2_a0a1 = S.Task('T2t2_a0a1', length=1, delay_cost=1)
	T2t2_a0a1 += alt(ADD)

	T2t2_a0a1_mem0 = S.Task('T2t2_a0a1_mem0', length=1, delay_cost=1)
	T2t2_a0a1_mem0 += INPUT_mem_r
	S += T2t2_a0a1_mem0<=T2t2_a0a1

	T2t2_a0a1_mem1 = S.Task('T2t2_a0a1_mem1', length=1, delay_cost=1)
	T2t2_a0a1_mem1 += INPUT_mem_r
	S += T2t2_a0a1_mem1<=T2t2_a0a1

	T1300 = S.Task('T1300', length=1, delay_cost=1)
	T1300 += alt(ADD)

	T1300_mem0 = S.Task('T1300_mem0', length=1, delay_cost=1)
	T1300_mem0 += INPUT_mem_r
	S += T1300_mem0<=T1300

	T1300_mem1 = S.Task('T1300_mem1', length=1, delay_cost=1)
	T1300_mem1 += INPUT_mem_r
	S += T1300_mem1<=T1300

	T1301 = S.Task('T1301', length=1, delay_cost=1)
	T1301 += alt(ADD)

	T1301_mem0 = S.Task('T1301_mem0', length=1, delay_cost=1)
	T1301_mem0 += INPUT_mem_r
	S += T1301_mem0<=T1301

	T1301_mem1 = S.Task('T1301_mem1', length=1, delay_cost=1)
	T1301_mem1 += INPUT_mem_r
	S += T1301_mem1<=T1301

	T1310 = S.Task('T1310', length=1, delay_cost=1)
	T1310 += alt(ADD)

	T1310_mem0 = S.Task('T1310_mem0', length=1, delay_cost=1)
	T1310_mem0 += INPUT_mem_r
	S += T1310_mem0<=T1310

	T1310_mem1 = S.Task('T1310_mem1', length=1, delay_cost=1)
	T1310_mem1 += INPUT_mem_r
	S += T1310_mem1<=T1310

	T1311 = S.Task('T1311', length=1, delay_cost=1)
	T1311 += alt(ADD)

	T1311_mem0 = S.Task('T1311_mem0', length=1, delay_cost=1)
	T1311_mem0 += INPUT_mem_r
	S += T1311_mem0<=T1311

	T1311_mem1 = S.Task('T1311_mem1', length=1, delay_cost=1)
	T1311_mem1 += INPUT_mem_r
	S += T1311_mem1<=T1311

	T1400 = S.Task('T1400', length=1, delay_cost=1)
	T1400 += alt(ADD)

	T1400_mem0 = S.Task('T1400_mem0', length=1, delay_cost=1)
	T1400_mem0 += INPUT_mem_r
	S += T1400_mem0<=T1400

	T1400_mem1 = S.Task('T1400_mem1', length=1, delay_cost=1)
	T1400_mem1 += INPUT_mem_r
	S += T1400_mem1<=T1400

	T1401 = S.Task('T1401', length=1, delay_cost=1)
	T1401 += alt(ADD)

	T1401_mem0 = S.Task('T1401_mem0', length=1, delay_cost=1)
	T1401_mem0 += INPUT_mem_r
	S += T1401_mem0<=T1401

	T1401_mem1 = S.Task('T1401_mem1', length=1, delay_cost=1)
	T1401_mem1 += INPUT_mem_r
	S += T1401_mem1<=T1401

	T1410 = S.Task('T1410', length=1, delay_cost=1)
	T1410 += alt(ADD)

	T1410_mem0 = S.Task('T1410_mem0', length=1, delay_cost=1)
	T1410_mem0 += INPUT_mem_r
	S += T1410_mem0<=T1410

	T1410_mem1 = S.Task('T1410_mem1', length=1, delay_cost=1)
	T1410_mem1 += INPUT_mem_r
	S += T1410_mem1<=T1410

	T1411 = S.Task('T1411', length=1, delay_cost=1)
	T1411 += alt(ADD)

	T1411_mem0 = S.Task('T1411_mem0', length=1, delay_cost=1)
	T1411_mem0 += INPUT_mem_r
	S += T1411_mem0<=T1411

	T1411_mem1 = S.Task('T1411_mem1', length=1, delay_cost=1)
	T1411_mem1 += INPUT_mem_r
	S += T1411_mem1<=T1411

	T1500 = S.Task('T1500', length=1, delay_cost=1)
	T1500 += alt(ADD)

	T1500_mem0 = S.Task('T1500_mem0', length=1, delay_cost=1)
	T1500_mem0 += INPUT_mem_r
	S += T1500_mem0<=T1500

	T1500_mem1 = S.Task('T1500_mem1', length=1, delay_cost=1)
	T1500_mem1 += INPUT_mem_r
	S += T1500_mem1<=T1500

	T1501 = S.Task('T1501', length=1, delay_cost=1)
	T1501 += alt(ADD)

	T1501_mem0 = S.Task('T1501_mem0', length=1, delay_cost=1)
	T1501_mem0 += INPUT_mem_r
	S += T1501_mem0<=T1501

	T1501_mem1 = S.Task('T1501_mem1', length=1, delay_cost=1)
	T1501_mem1 += INPUT_mem_r
	S += T1501_mem1<=T1501

	T1510 = S.Task('T1510', length=1, delay_cost=1)
	T1510 += alt(ADD)

	T1510_mem0 = S.Task('T1510_mem0', length=1, delay_cost=1)
	T1510_mem0 += INPUT_mem_r
	S += T1510_mem0<=T1510

	T1510_mem1 = S.Task('T1510_mem1', length=1, delay_cost=1)
	T1510_mem1 += INPUT_mem_r
	S += T1510_mem1<=T1510

	T1511 = S.Task('T1511', length=1, delay_cost=1)
	T1511 += alt(ADD)

	T1511_mem0 = S.Task('T1511_mem0', length=1, delay_cost=1)
	T1511_mem0 += INPUT_mem_r
	S += T1511_mem0<=T1511

	T1511_mem1 = S.Task('T1511_mem1', length=1, delay_cost=1)
	T1511_mem1 += INPUT_mem_r
	S += T1511_mem1<=T1511

	T0_1a10_new = S.Task('T0_1a10_new', length=1, delay_cost=1)
	T0_1a10_new += alt(ADD)

	T0_1a10_new_mem0 = S.Task('T0_1a10_new_mem0', length=1, delay_cost=1)
	T0_1a10_new_mem0 += INPUT_mem_r
	S += T0_1a10_new_mem0<=T0_1a10_new

	T0_1a10_new_mem1 = S.Task('T0_1a10_new_mem1', length=1, delay_cost=1)
	T0_1a10_new_mem1 += INPUT_mem_r
	S += T0_1a10_new_mem1<=T0_1a10_new

	T0_1a11_new = S.Task('T0_1a11_new', length=1, delay_cost=1)
	T0_1a11_new += alt(ADD)

	T0_1a11_new_mem0 = S.Task('T0_1a11_new_mem0', length=1, delay_cost=1)
	T0_1a11_new_mem0 += INPUT_mem_r
	S += T0_1a11_new_mem0<=T0_1a11_new

	T0_1a11_new_mem1 = S.Task('T0_1a11_new_mem1', length=1, delay_cost=1)
	T0_1a11_new_mem1 += INPUT_mem_r
	S += T0_1a11_new_mem1<=T0_1a11_new

	T0_1t10 = S.Task('T0_1t10', length=1, delay_cost=1)
	T0_1t10 += alt(ADD)

	T0_1t10_mem0 = S.Task('T0_1t10_mem0', length=1, delay_cost=1)
	T0_1t10_mem0 += INPUT_mem_r
	S += T0_1t10_mem0<=T0_1t10

	T0_1t10_mem1 = S.Task('T0_1t10_mem1', length=1, delay_cost=1)
	T0_1t10_mem1 += INPUT_mem_r
	S += T0_1t10_mem1<=T0_1t10

	T0_1t11 = S.Task('T0_1t11', length=1, delay_cost=1)
	T0_1t11 += alt(ADD)

	T0_1t11_mem0 = S.Task('T0_1t11_mem0', length=1, delay_cost=1)
	T0_1t11_mem0 += INPUT_mem_r
	S += T0_1t11_mem0<=T0_1t11

	T0_1t11_mem1 = S.Task('T0_1t11_mem1', length=1, delay_cost=1)
	T0_1t11_mem1 += INPUT_mem_r
	S += T0_1t11_mem1<=T0_1t11

	T0_1t0_a0a1_in = S.Task('T0_1t0_a0a1_in', length=1, delay_cost=1)
	T0_1t0_a0a1_in += alt(MUL_in)
	T0_1t0_a0a1 = S.Task('T0_1t0_a0a1', length=7, delay_cost=1)
	T0_1t0_a0a1 += alt(MUL)
	S+=T0_1t0_a0a1>=T0_1t0_a0a1_in

	T0_1t0_a0a1_mem0 = S.Task('T0_1t0_a0a1_mem0', length=1, delay_cost=1)
	T0_1t0_a0a1_mem0 += INPUT_mem_r
	S += T0_1t0_a0a1_mem0<=T0_1t0_a0a1

	T0_1t0_a0a1_mem1 = S.Task('T0_1t0_a0a1_mem1', length=1, delay_cost=1)
	T0_1t0_a0a1_mem1 += INPUT_mem_r
	S += T0_1t0_a0a1_mem1<=T0_1t0_a0a1

	T0_1t1_a0a1_in = S.Task('T0_1t1_a0a1_in', length=1, delay_cost=1)
	T0_1t1_a0a1_in += alt(MUL_in)
	T0_1t1_a0a1 = S.Task('T0_1t1_a0a1', length=7, delay_cost=1)
	T0_1t1_a0a1 += alt(MUL)
	S+=T0_1t1_a0a1>=T0_1t1_a0a1_in

	T0_1t1_a0a1_mem0 = S.Task('T0_1t1_a0a1_mem0', length=1, delay_cost=1)
	T0_1t1_a0a1_mem0 += INPUT_mem_r
	S += T0_1t1_a0a1_mem0<=T0_1t1_a0a1

	T0_1t1_a0a1_mem1 = S.Task('T0_1t1_a0a1_mem1', length=1, delay_cost=1)
	T0_1t1_a0a1_mem1 += INPUT_mem_r
	S += T0_1t1_a0a1_mem1<=T0_1t1_a0a1

	T0_1t2_a0a1 = S.Task('T0_1t2_a0a1', length=1, delay_cost=1)
	T0_1t2_a0a1 += alt(ADD)

	T0_1t2_a0a1_mem0 = S.Task('T0_1t2_a0a1_mem0', length=1, delay_cost=1)
	T0_1t2_a0a1_mem0 += INPUT_mem_r
	S += T0_1t2_a0a1_mem0<=T0_1t2_a0a1

	T0_1t2_a0a1_mem1 = S.Task('T0_1t2_a0a1_mem1', length=1, delay_cost=1)
	T0_1t2_a0a1_mem1 += INPUT_mem_r
	S += T0_1t2_a0a1_mem1<=T0_1t2_a0a1

	T1_1a10_new = S.Task('T1_1a10_new', length=1, delay_cost=1)
	T1_1a10_new += alt(ADD)

	T1_1a10_new_mem0 = S.Task('T1_1a10_new_mem0', length=1, delay_cost=1)
	T1_1a10_new_mem0 += INPUT_mem_r
	S += T1_1a10_new_mem0<=T1_1a10_new

	T1_1a10_new_mem1 = S.Task('T1_1a10_new_mem1', length=1, delay_cost=1)
	T1_1a10_new_mem1 += INPUT_mem_r
	S += T1_1a10_new_mem1<=T1_1a10_new

	T1_1a11_new = S.Task('T1_1a11_new', length=1, delay_cost=1)
	T1_1a11_new += alt(ADD)

	T1_1a11_new_mem0 = S.Task('T1_1a11_new_mem0', length=1, delay_cost=1)
	T1_1a11_new_mem0 += INPUT_mem_r
	S += T1_1a11_new_mem0<=T1_1a11_new

	T1_1a11_new_mem1 = S.Task('T1_1a11_new_mem1', length=1, delay_cost=1)
	T1_1a11_new_mem1 += INPUT_mem_r
	S += T1_1a11_new_mem1<=T1_1a11_new

	T1_1t10 = S.Task('T1_1t10', length=1, delay_cost=1)
	T1_1t10 += alt(ADD)

	T1_1t10_mem0 = S.Task('T1_1t10_mem0', length=1, delay_cost=1)
	T1_1t10_mem0 += INPUT_mem_r
	S += T1_1t10_mem0<=T1_1t10

	T1_1t10_mem1 = S.Task('T1_1t10_mem1', length=1, delay_cost=1)
	T1_1t10_mem1 += INPUT_mem_r
	S += T1_1t10_mem1<=T1_1t10

	T1_1t11 = S.Task('T1_1t11', length=1, delay_cost=1)
	T1_1t11 += alt(ADD)

	T1_1t11_mem0 = S.Task('T1_1t11_mem0', length=1, delay_cost=1)
	T1_1t11_mem0 += INPUT_mem_r
	S += T1_1t11_mem0<=T1_1t11

	T1_1t11_mem1 = S.Task('T1_1t11_mem1', length=1, delay_cost=1)
	T1_1t11_mem1 += INPUT_mem_r
	S += T1_1t11_mem1<=T1_1t11

	T1_1t0_a0a1_in = S.Task('T1_1t0_a0a1_in', length=1, delay_cost=1)
	T1_1t0_a0a1_in += alt(MUL_in)
	T1_1t0_a0a1 = S.Task('T1_1t0_a0a1', length=7, delay_cost=1)
	T1_1t0_a0a1 += alt(MUL)
	S+=T1_1t0_a0a1>=T1_1t0_a0a1_in

	T1_1t0_a0a1_mem0 = S.Task('T1_1t0_a0a1_mem0', length=1, delay_cost=1)
	T1_1t0_a0a1_mem0 += INPUT_mem_r
	S += T1_1t0_a0a1_mem0<=T1_1t0_a0a1

	T1_1t0_a0a1_mem1 = S.Task('T1_1t0_a0a1_mem1', length=1, delay_cost=1)
	T1_1t0_a0a1_mem1 += INPUT_mem_r
	S += T1_1t0_a0a1_mem1<=T1_1t0_a0a1

	T1_1t1_a0a1_in = S.Task('T1_1t1_a0a1_in', length=1, delay_cost=1)
	T1_1t1_a0a1_in += alt(MUL_in)
	T1_1t1_a0a1 = S.Task('T1_1t1_a0a1', length=7, delay_cost=1)
	T1_1t1_a0a1 += alt(MUL)
	S+=T1_1t1_a0a1>=T1_1t1_a0a1_in

	T1_1t1_a0a1_mem0 = S.Task('T1_1t1_a0a1_mem0', length=1, delay_cost=1)
	T1_1t1_a0a1_mem0 += INPUT_mem_r
	S += T1_1t1_a0a1_mem0<=T1_1t1_a0a1

	T1_1t1_a0a1_mem1 = S.Task('T1_1t1_a0a1_mem1', length=1, delay_cost=1)
	T1_1t1_a0a1_mem1 += INPUT_mem_r
	S += T1_1t1_a0a1_mem1<=T1_1t1_a0a1

	T1_1t2_a0a1 = S.Task('T1_1t2_a0a1', length=1, delay_cost=1)
	T1_1t2_a0a1 += alt(ADD)

	T1_1t2_a0a1_mem0 = S.Task('T1_1t2_a0a1_mem0', length=1, delay_cost=1)
	T1_1t2_a0a1_mem0 += INPUT_mem_r
	S += T1_1t2_a0a1_mem0<=T1_1t2_a0a1

	T1_1t2_a0a1_mem1 = S.Task('T1_1t2_a0a1_mem1', length=1, delay_cost=1)
	T1_1t2_a0a1_mem1 += INPUT_mem_r
	S += T1_1t2_a0a1_mem1<=T1_1t2_a0a1

	T2_2a10_new = S.Task('T2_2a10_new', length=1, delay_cost=1)
	T2_2a10_new += alt(ADD)

	T2_2a10_new_mem0 = S.Task('T2_2a10_new_mem0', length=1, delay_cost=1)
	T2_2a10_new_mem0 += INPUT_mem_r
	S += T2_2a10_new_mem0<=T2_2a10_new

	T2_2a10_new_mem1 = S.Task('T2_2a10_new_mem1', length=1, delay_cost=1)
	T2_2a10_new_mem1 += INPUT_mem_r
	S += T2_2a10_new_mem1<=T2_2a10_new

	T2_2a11_new = S.Task('T2_2a11_new', length=1, delay_cost=1)
	T2_2a11_new += alt(ADD)

	T2_2a11_new_mem0 = S.Task('T2_2a11_new_mem0', length=1, delay_cost=1)
	T2_2a11_new_mem0 += INPUT_mem_r
	S += T2_2a11_new_mem0<=T2_2a11_new

	T2_2a11_new_mem1 = S.Task('T2_2a11_new_mem1', length=1, delay_cost=1)
	T2_2a11_new_mem1 += INPUT_mem_r
	S += T2_2a11_new_mem1<=T2_2a11_new

	T2_2t10 = S.Task('T2_2t10', length=1, delay_cost=1)
	T2_2t10 += alt(ADD)

	T2_2t10_mem0 = S.Task('T2_2t10_mem0', length=1, delay_cost=1)
	T2_2t10_mem0 += INPUT_mem_r
	S += T2_2t10_mem0<=T2_2t10

	T2_2t10_mem1 = S.Task('T2_2t10_mem1', length=1, delay_cost=1)
	T2_2t10_mem1 += INPUT_mem_r
	S += T2_2t10_mem1<=T2_2t10

	T2_2t11 = S.Task('T2_2t11', length=1, delay_cost=1)
	T2_2t11 += alt(ADD)

	T2_2t11_mem0 = S.Task('T2_2t11_mem0', length=1, delay_cost=1)
	T2_2t11_mem0 += INPUT_mem_r
	S += T2_2t11_mem0<=T2_2t11

	T2_2t11_mem1 = S.Task('T2_2t11_mem1', length=1, delay_cost=1)
	T2_2t11_mem1 += INPUT_mem_r
	S += T2_2t11_mem1<=T2_2t11

	T2_2t0_a0a1_in = S.Task('T2_2t0_a0a1_in', length=1, delay_cost=1)
	T2_2t0_a0a1_in += alt(MUL_in)
	T2_2t0_a0a1 = S.Task('T2_2t0_a0a1', length=7, delay_cost=1)
	T2_2t0_a0a1 += alt(MUL)
	S+=T2_2t0_a0a1>=T2_2t0_a0a1_in

	T2_2t0_a0a1_mem0 = S.Task('T2_2t0_a0a1_mem0', length=1, delay_cost=1)
	T2_2t0_a0a1_mem0 += INPUT_mem_r
	S += T2_2t0_a0a1_mem0<=T2_2t0_a0a1

	T2_2t0_a0a1_mem1 = S.Task('T2_2t0_a0a1_mem1', length=1, delay_cost=1)
	T2_2t0_a0a1_mem1 += INPUT_mem_r
	S += T2_2t0_a0a1_mem1<=T2_2t0_a0a1

	T2_2t1_a0a1_in = S.Task('T2_2t1_a0a1_in', length=1, delay_cost=1)
	T2_2t1_a0a1_in += alt(MUL_in)
	T2_2t1_a0a1 = S.Task('T2_2t1_a0a1', length=7, delay_cost=1)
	T2_2t1_a0a1 += alt(MUL)
	S+=T2_2t1_a0a1>=T2_2t1_a0a1_in

	T2_2t1_a0a1_mem0 = S.Task('T2_2t1_a0a1_mem0', length=1, delay_cost=1)
	T2_2t1_a0a1_mem0 += INPUT_mem_r
	S += T2_2t1_a0a1_mem0<=T2_2t1_a0a1

	T2_2t1_a0a1_mem1 = S.Task('T2_2t1_a0a1_mem1', length=1, delay_cost=1)
	T2_2t1_a0a1_mem1 += INPUT_mem_r
	S += T2_2t1_a0a1_mem1<=T2_2t1_a0a1

	T2_2t2_a0a1 = S.Task('T2_2t2_a0a1', length=1, delay_cost=1)
	T2_2t2_a0a1 += alt(ADD)

	T2_2t2_a0a1_mem0 = S.Task('T2_2t2_a0a1_mem0', length=1, delay_cost=1)
	T2_2t2_a0a1_mem0 += INPUT_mem_r
	S += T2_2t2_a0a1_mem0<=T2_2t2_a0a1

	T2_2t2_a0a1_mem1 = S.Task('T2_2t2_a0a1_mem1', length=1, delay_cost=1)
	T2_2t2_a0a1_mem1 += INPUT_mem_r
	S += T2_2t2_a0a1_mem1<=T2_2t2_a0a1

	T1600 = S.Task('T1600', length=1, delay_cost=1)
	T1600 += alt(ADD)

	T1600_mem0 = S.Task('T1600_mem0', length=1, delay_cost=1)
	T1600_mem0 += INPUT_mem_r
	S += T1600_mem0<=T1600

	T1600_mem1 = S.Task('T1600_mem1', length=1, delay_cost=1)
	T1600_mem1 += INPUT_mem_r
	S += T1600_mem1<=T1600

	T1601 = S.Task('T1601', length=1, delay_cost=1)
	T1601 += alt(ADD)

	T1601_mem0 = S.Task('T1601_mem0', length=1, delay_cost=1)
	T1601_mem0 += INPUT_mem_r
	S += T1601_mem0<=T1601

	T1601_mem1 = S.Task('T1601_mem1', length=1, delay_cost=1)
	T1601_mem1 += INPUT_mem_r
	S += T1601_mem1<=T1601

	T1610 = S.Task('T1610', length=1, delay_cost=1)
	T1610 += alt(ADD)

	T1610_mem0 = S.Task('T1610_mem0', length=1, delay_cost=1)
	T1610_mem0 += INPUT_mem_r
	S += T1610_mem0<=T1610

	T1610_mem1 = S.Task('T1610_mem1', length=1, delay_cost=1)
	T1610_mem1 += INPUT_mem_r
	S += T1610_mem1<=T1610

	T1611 = S.Task('T1611', length=1, delay_cost=1)
	T1611 += alt(ADD)

	T1611_mem0 = S.Task('T1611_mem0', length=1, delay_cost=1)
	T1611_mem0 += INPUT_mem_r
	S += T1611_mem0<=T1611

	T1611_mem1 = S.Task('T1611_mem1', length=1, delay_cost=1)
	T1611_mem1 += INPUT_mem_r
	S += T1611_mem1<=T1611

	T1700 = S.Task('T1700', length=1, delay_cost=1)
	T1700 += alt(ADD)

	T1700_mem0 = S.Task('T1700_mem0', length=1, delay_cost=1)
	T1700_mem0 += INPUT_mem_r
	S += T1700_mem0<=T1700

	T1700_mem1 = S.Task('T1700_mem1', length=1, delay_cost=1)
	T1700_mem1 += INPUT_mem_r
	S += T1700_mem1<=T1700

	T1701 = S.Task('T1701', length=1, delay_cost=1)
	T1701 += alt(ADD)

	T1701_mem0 = S.Task('T1701_mem0', length=1, delay_cost=1)
	T1701_mem0 += INPUT_mem_r
	S += T1701_mem0<=T1701

	T1701_mem1 = S.Task('T1701_mem1', length=1, delay_cost=1)
	T1701_mem1 += INPUT_mem_r
	S += T1701_mem1<=T1701

	T1710 = S.Task('T1710', length=1, delay_cost=1)
	T1710 += alt(ADD)

	T1710_mem0 = S.Task('T1710_mem0', length=1, delay_cost=1)
	T1710_mem0 += INPUT_mem_r
	S += T1710_mem0<=T1710

	T1710_mem1 = S.Task('T1710_mem1', length=1, delay_cost=1)
	T1710_mem1 += INPUT_mem_r
	S += T1710_mem1<=T1710

	T1711 = S.Task('T1711', length=1, delay_cost=1)
	T1711 += alt(ADD)

	T1711_mem0 = S.Task('T1711_mem0', length=1, delay_cost=1)
	T1711_mem0 += INPUT_mem_r
	S += T1711_mem0<=T1711

	T1711_mem1 = S.Task('T1711_mem1', length=1, delay_cost=1)
	T1711_mem1 += INPUT_mem_r
	S += T1711_mem1<=T1711

	T1800 = S.Task('T1800', length=1, delay_cost=1)
	T1800 += alt(ADD)

	T1800_mem0 = S.Task('T1800_mem0', length=1, delay_cost=1)
	T1800_mem0 += INPUT_mem_r
	S += T1800_mem0<=T1800

	T1800_mem1 = S.Task('T1800_mem1', length=1, delay_cost=1)
	T1800_mem1 += INPUT_mem_r
	S += T1800_mem1<=T1800

	T1801 = S.Task('T1801', length=1, delay_cost=1)
	T1801 += alt(ADD)

	T1801_mem0 = S.Task('T1801_mem0', length=1, delay_cost=1)
	T1801_mem0 += INPUT_mem_r
	S += T1801_mem0<=T1801

	T1801_mem1 = S.Task('T1801_mem1', length=1, delay_cost=1)
	T1801_mem1 += INPUT_mem_r
	S += T1801_mem1<=T1801

	T1810 = S.Task('T1810', length=1, delay_cost=1)
	T1810 += alt(ADD)

	T1810_mem0 = S.Task('T1810_mem0', length=1, delay_cost=1)
	T1810_mem0 += INPUT_mem_r
	S += T1810_mem0<=T1810

	T1810_mem1 = S.Task('T1810_mem1', length=1, delay_cost=1)
	T1810_mem1 += INPUT_mem_r
	S += T1810_mem1<=T1810

	T1811 = S.Task('T1811', length=1, delay_cost=1)
	T1811 += alt(ADD)

	T1811_mem0 = S.Task('T1811_mem0', length=1, delay_cost=1)
	T1811_mem0 += INPUT_mem_r
	S += T1811_mem0<=T1811

	T1811_mem1 = S.Task('T1811_mem1', length=1, delay_cost=1)
	T1811_mem1 += INPUT_mem_r
	S += T1811_mem1<=T1811

	solvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "inv_mul1_add4/inv_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_inv_mul1_add4_0(0, 0)