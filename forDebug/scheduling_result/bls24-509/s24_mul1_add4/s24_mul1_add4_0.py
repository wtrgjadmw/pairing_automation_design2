from pyschedule import Scenario, solvers, plotters, alt

def solve_s24_mul1_add4_0(ConstStep, ExpStep):
	horizon = 134
	S=Scenario("s24_mul1_add4_0",horizon = horizon)

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
	T000 = S.Task('T000', length=1, delay_cost=1)
	T000 += alt(ADD)

	T001 = S.Task('T001', length=1, delay_cost=1)
	T001 += alt(ADD)

	T0110 = S.Task('T0110', length=1, delay_cost=1)
	T0110 += alt(ADD)

	T0111 = S.Task('T0111', length=1, delay_cost=1)
	T0111 += alt(ADD)

	T100 = S.Task('T100', length=1, delay_cost=1)
	T100 += alt(ADD)

	T101 = S.Task('T101', length=1, delay_cost=1)
	T101 += alt(ADD)

	T110 = S.Task('T110', length=1, delay_cost=1)
	T110 += alt(ADD)

	T111 = S.Task('T111', length=1, delay_cost=1)
	T111 += alt(ADD)

	T200 = S.Task('T200', length=1, delay_cost=1)
	T200 += alt(ADD)

	T201 = S.Task('T201', length=1, delay_cost=1)
	T201 += alt(ADD)

	T210 = S.Task('T210', length=1, delay_cost=1)
	T210 += alt(ADD)

	T211 = S.Task('T211', length=1, delay_cost=1)
	T211 += alt(ADD)

	T300 = S.Task('T300', length=1, delay_cost=1)
	T300 += alt(ADD)

	T301 = S.Task('T301', length=1, delay_cost=1)
	T301 += alt(ADD)

	T310 = S.Task('T310', length=1, delay_cost=1)
	T310 += alt(ADD)

	T311 = S.Task('T311', length=1, delay_cost=1)
	T311 += alt(ADD)

	T400 = S.Task('T400', length=1, delay_cost=1)
	T400 += alt(ADD)

	T401 = S.Task('T401', length=1, delay_cost=1)
	T401 += alt(ADD)

	T410 = S.Task('T410', length=1, delay_cost=1)
	T410 += alt(ADD)

	T411 = S.Task('T411', length=1, delay_cost=1)
	T411 += alt(ADD)

	T500 = S.Task('T500', length=1, delay_cost=1)
	T500 += alt(ADD)

	T501 = S.Task('T501', length=1, delay_cost=1)
	T501 += alt(ADD)

	T510 = S.Task('T510', length=1, delay_cost=1)
	T510 += alt(ADD)

	T511 = S.Task('T511', length=1, delay_cost=1)
	T511 += alt(ADD)

	T61t2_0 = S.Task('T61t2_0', length=1, delay_cost=1)
	T61t2_0 += alt(ADD)

	T61t2_1 = S.Task('T61t2_1', length=1, delay_cost=1)
	T61t2_1 += alt(ADD)

	T61t3_0 = S.Task('T61t3_0', length=1, delay_cost=1)
	T61t3_0 += alt(ADD)

	T61t3_1 = S.Task('T61t3_1', length=1, delay_cost=1)
	T61t3_1 += alt(ADD)

	T61t0_a0b0_in = S.Task('T61t0_a0b0_in', length=1, delay_cost=1)
	T61t0_a0b0_in += alt(MUL_in)
	T61t0_a0b0 = S.Task('T61t0_a0b0', length=7, delay_cost=1)
	T61t0_a0b0 += alt(MUL)
	S+=T61t0_a0b0>=T61t0_a0b0_in

	T61t1_a0b0_in = S.Task('T61t1_a0b0_in', length=1, delay_cost=1)
	T61t1_a0b0_in += alt(MUL_in)
	T61t1_a0b0 = S.Task('T61t1_a0b0', length=7, delay_cost=1)
	T61t1_a0b0 += alt(MUL)
	S+=T61t1_a0b0>=T61t1_a0b0_in

	T61t2_a0b0 = S.Task('T61t2_a0b0', length=1, delay_cost=1)
	T61t2_a0b0 += alt(ADD)

	T61t3_a0b0 = S.Task('T61t3_a0b0', length=1, delay_cost=1)
	T61t3_a0b0 += alt(ADD)

	T61t0_a1b1_in = S.Task('T61t0_a1b1_in', length=1, delay_cost=1)
	T61t0_a1b1_in += alt(MUL_in)
	T61t0_a1b1 = S.Task('T61t0_a1b1', length=7, delay_cost=1)
	T61t0_a1b1 += alt(MUL)
	S+=T61t0_a1b1>=T61t0_a1b1_in

	T61t1_a1b1_in = S.Task('T61t1_a1b1_in', length=1, delay_cost=1)
	T61t1_a1b1_in += alt(MUL_in)
	T61t1_a1b1 = S.Task('T61t1_a1b1', length=7, delay_cost=1)
	T61t1_a1b1 += alt(MUL)
	S+=T61t1_a1b1>=T61t1_a1b1_in

	T61t2_a1b1 = S.Task('T61t2_a1b1', length=1, delay_cost=1)
	T61t2_a1b1 += alt(ADD)

	T61t3_a1b1 = S.Task('T61t3_a1b1', length=1, delay_cost=1)
	T61t3_a1b1 += alt(ADD)

	T71t2_0 = S.Task('T71t2_0', length=1, delay_cost=1)
	T71t2_0 += alt(ADD)

	T71t2_1 = S.Task('T71t2_1', length=1, delay_cost=1)
	T71t2_1 += alt(ADD)

	T71t3_0 = S.Task('T71t3_0', length=1, delay_cost=1)
	T71t3_0 += alt(ADD)

	T71t3_1 = S.Task('T71t3_1', length=1, delay_cost=1)
	T71t3_1 += alt(ADD)

	T71t0_a0b0_in = S.Task('T71t0_a0b0_in', length=1, delay_cost=1)
	T71t0_a0b0_in += alt(MUL_in)
	T71t0_a0b0 = S.Task('T71t0_a0b0', length=7, delay_cost=1)
	T71t0_a0b0 += alt(MUL)
	S+=T71t0_a0b0>=T71t0_a0b0_in

	T71t1_a0b0_in = S.Task('T71t1_a0b0_in', length=1, delay_cost=1)
	T71t1_a0b0_in += alt(MUL_in)
	T71t1_a0b0 = S.Task('T71t1_a0b0', length=7, delay_cost=1)
	T71t1_a0b0 += alt(MUL)
	S+=T71t1_a0b0>=T71t1_a0b0_in

	T71t2_a0b0 = S.Task('T71t2_a0b0', length=1, delay_cost=1)
	T71t2_a0b0 += alt(ADD)

	T71t3_a0b0 = S.Task('T71t3_a0b0', length=1, delay_cost=1)
	T71t3_a0b0 += alt(ADD)

	T71t0_a1b1_in = S.Task('T71t0_a1b1_in', length=1, delay_cost=1)
	T71t0_a1b1_in += alt(MUL_in)
	T71t0_a1b1 = S.Task('T71t0_a1b1', length=7, delay_cost=1)
	T71t0_a1b1 += alt(MUL)
	S+=T71t0_a1b1>=T71t0_a1b1_in

	T71t1_a1b1_in = S.Task('T71t1_a1b1_in', length=1, delay_cost=1)
	T71t1_a1b1_in += alt(MUL_in)
	T71t1_a1b1 = S.Task('T71t1_a1b1', length=7, delay_cost=1)
	T71t1_a1b1 += alt(MUL)
	S+=T71t1_a1b1>=T71t1_a1b1_in

	T71t2_a1b1 = S.Task('T71t2_a1b1', length=1, delay_cost=1)
	T71t2_a1b1 += alt(ADD)

	T71t3_a1b1 = S.Task('T71t3_a1b1', length=1, delay_cost=1)
	T71t3_a1b1 += alt(ADD)

	T82t2_0 = S.Task('T82t2_0', length=1, delay_cost=1)
	T82t2_0 += alt(ADD)

	T82t2_1 = S.Task('T82t2_1', length=1, delay_cost=1)
	T82t2_1 += alt(ADD)

	T82t3_0 = S.Task('T82t3_0', length=1, delay_cost=1)
	T82t3_0 += alt(ADD)

	T82t3_1 = S.Task('T82t3_1', length=1, delay_cost=1)
	T82t3_1 += alt(ADD)

	T82t0_a0b0_in = S.Task('T82t0_a0b0_in', length=1, delay_cost=1)
	T82t0_a0b0_in += alt(MUL_in)
	T82t0_a0b0 = S.Task('T82t0_a0b0', length=7, delay_cost=1)
	T82t0_a0b0 += alt(MUL)
	S+=T82t0_a0b0>=T82t0_a0b0_in

	T82t1_a0b0_in = S.Task('T82t1_a0b0_in', length=1, delay_cost=1)
	T82t1_a0b0_in += alt(MUL_in)
	T82t1_a0b0 = S.Task('T82t1_a0b0', length=7, delay_cost=1)
	T82t1_a0b0 += alt(MUL)
	S+=T82t1_a0b0>=T82t1_a0b0_in

	T82t2_a0b0 = S.Task('T82t2_a0b0', length=1, delay_cost=1)
	T82t2_a0b0 += alt(ADD)

	T82t3_a0b0 = S.Task('T82t3_a0b0', length=1, delay_cost=1)
	T82t3_a0b0 += alt(ADD)

	T82t0_a1b1_in = S.Task('T82t0_a1b1_in', length=1, delay_cost=1)
	T82t0_a1b1_in += alt(MUL_in)
	T82t0_a1b1 = S.Task('T82t0_a1b1', length=7, delay_cost=1)
	T82t0_a1b1 += alt(MUL)
	S+=T82t0_a1b1>=T82t0_a1b1_in

	T82t1_a1b1_in = S.Task('T82t1_a1b1_in', length=1, delay_cost=1)
	T82t1_a1b1_in += alt(MUL_in)
	T82t1_a1b1 = S.Task('T82t1_a1b1', length=7, delay_cost=1)
	T82t1_a1b1 += alt(MUL)
	S+=T82t1_a1b1>=T82t1_a1b1_in

	T82t2_a1b1 = S.Task('T82t2_a1b1', length=1, delay_cost=1)
	T82t2_a1b1 += alt(ADD)

	T9400 = S.Task('T9400', length=1, delay_cost=1)
	T9400 += alt(ADD)

	T9401 = S.Task('T9401', length=1, delay_cost=1)
	T9401 += alt(ADD)

	T9410 = S.Task('T9410', length=1, delay_cost=1)
	T9410 += alt(ADD)

	T9411 = S.Task('T9411', length=1, delay_cost=1)
	T9411 += alt(ADD)

	T10100 = S.Task('T10100', length=1, delay_cost=1)
	T10100 += alt(ADD)

	T10101 = S.Task('T10101', length=1, delay_cost=1)
	T10101 += alt(ADD)

	T10110 = S.Task('T10110', length=1, delay_cost=1)
	T10110 += alt(ADD)

	T10111 = S.Task('T10111', length=1, delay_cost=1)
	T10111 += alt(ADD)

	T3100 = S.Task('T3100', length=1, delay_cost=1)
	T3100 += alt(ADD)

	T3101 = S.Task('T3101', length=1, delay_cost=1)
	T3101 += alt(ADD)

	T3110 = S.Task('T3110', length=1, delay_cost=1)
	T3110 += alt(ADD)

	T3111 = S.Task('T3111', length=1, delay_cost=1)
	T3111 += alt(ADD)

	T4200 = S.Task('T4200', length=1, delay_cost=1)
	T4200 += alt(ADD)

	T4201 = S.Task('T4201', length=1, delay_cost=1)
	T4201 += alt(ADD)

	T4210 = S.Task('T4210', length=1, delay_cost=1)
	T4210 += alt(ADD)

	T4211 = S.Task('T4211', length=1, delay_cost=1)
	T4211 += alt(ADD)

	T4300 = S.Task('T4300', length=1, delay_cost=1)
	T4300 += alt(ADD)

	T4301 = S.Task('T4301', length=1, delay_cost=1)
	T4301 += alt(ADD)

	T4310 = S.Task('T4310', length=1, delay_cost=1)
	T4310 += alt(ADD)

	T4311 = S.Task('T4311', length=1, delay_cost=1)
	T4311 += alt(ADD)

	T5200 = S.Task('T5200', length=1, delay_cost=1)
	T5200 += alt(ADD)

	T5201 = S.Task('T5201', length=1, delay_cost=1)
	T5201 += alt(ADD)

	T5210 = S.Task('T5210', length=1, delay_cost=1)
	T5210 += alt(ADD)

	T5211 = S.Task('T5211', length=1, delay_cost=1)
	T5211 += alt(ADD)

	T000_mem0 = S.Task('T000_mem0', length=1, delay_cost=1)
	T000_mem0 += INPUT_mem_r
	S += T000_mem0<=T000

	T000_mem1 = S.Task('T000_mem1', length=1, delay_cost=1)
	T000_mem1 += INPUT_mem_r
	S += T000_mem1<=T000

	T001_mem0 = S.Task('T001_mem0', length=1, delay_cost=1)
	T001_mem0 += INPUT_mem_r
	S += T001_mem0<=T001

	T001_mem1 = S.Task('T001_mem1', length=1, delay_cost=1)
	T001_mem1 += INPUT_mem_r
	S += T001_mem1<=T001

	T0110_mem0 = S.Task('T0110_mem0', length=1, delay_cost=1)
	T0110_mem0 += INPUT_mem_r
	S += T0110_mem0<=T0110

	T0110_mem1 = S.Task('T0110_mem1', length=1, delay_cost=1)
	T0110_mem1 += INPUT_mem_r
	S += T0110_mem1<=T0110

	T0111_mem0 = S.Task('T0111_mem0', length=1, delay_cost=1)
	T0111_mem0 += INPUT_mem_r
	S += T0111_mem0<=T0111

	T0111_mem1 = S.Task('T0111_mem1', length=1, delay_cost=1)
	T0111_mem1 += INPUT_mem_r
	S += T0111_mem1<=T0111

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	T100_mem0 += INPUT_mem_r
	S += T100_mem0<=T100

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	T100_mem1 += INPUT_mem_r
	S += T100_mem1<=T100

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	T101_mem0 += INPUT_mem_r
	S += T101_mem0<=T101

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	T101_mem1 += INPUT_mem_r
	S += T101_mem1<=T101

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	T110_mem0 += INPUT_mem_r
	S += T110_mem0<=T110

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	T110_mem1 += INPUT_mem_r
	S += T110_mem1<=T110

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	T111_mem0 += INPUT_mem_r
	S += T111_mem0<=T111

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	T111_mem1 += INPUT_mem_r
	S += T111_mem1<=T111

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	T200_mem0 += INPUT_mem_r
	S += T200_mem0<=T200

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	T200_mem1 += INPUT_mem_r
	S += T200_mem1<=T200

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	T201_mem0 += INPUT_mem_r
	S += T201_mem0<=T201

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	T201_mem1 += INPUT_mem_r
	S += T201_mem1<=T201

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	T210_mem0 += INPUT_mem_r
	S += T210_mem0<=T210

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	T210_mem1 += INPUT_mem_r
	S += T210_mem1<=T210

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	T211_mem0 += INPUT_mem_r
	S += T211_mem0<=T211

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	T211_mem1 += INPUT_mem_r
	S += T211_mem1<=T211

	T300_mem0 = S.Task('T300_mem0', length=1, delay_cost=1)
	T300_mem0 += INPUT_mem_r
	S += T300_mem0<=T300

	T300_mem1 = S.Task('T300_mem1', length=1, delay_cost=1)
	T300_mem1 += INPUT_mem_r
	S += T300_mem1<=T300

	T301_mem0 = S.Task('T301_mem0', length=1, delay_cost=1)
	T301_mem0 += INPUT_mem_r
	S += T301_mem0<=T301

	T301_mem1 = S.Task('T301_mem1', length=1, delay_cost=1)
	T301_mem1 += INPUT_mem_r
	S += T301_mem1<=T301

	T310_mem0 = S.Task('T310_mem0', length=1, delay_cost=1)
	T310_mem0 += INPUT_mem_r
	S += T310_mem0<=T310

	T310_mem1 = S.Task('T310_mem1', length=1, delay_cost=1)
	T310_mem1 += INPUT_mem_r
	S += T310_mem1<=T310

	T311_mem0 = S.Task('T311_mem0', length=1, delay_cost=1)
	T311_mem0 += INPUT_mem_r
	S += T311_mem0<=T311

	T311_mem1 = S.Task('T311_mem1', length=1, delay_cost=1)
	T311_mem1 += INPUT_mem_r
	S += T311_mem1<=T311

	T400_mem0 = S.Task('T400_mem0', length=1, delay_cost=1)
	T400_mem0 += INPUT_mem_r
	S += T400_mem0<=T400

	T400_mem1 = S.Task('T400_mem1', length=1, delay_cost=1)
	T400_mem1 += INPUT_mem_r
	S += T400_mem1<=T400

	T401_mem0 = S.Task('T401_mem0', length=1, delay_cost=1)
	T401_mem0 += INPUT_mem_r
	S += T401_mem0<=T401

	T401_mem1 = S.Task('T401_mem1', length=1, delay_cost=1)
	T401_mem1 += INPUT_mem_r
	S += T401_mem1<=T401

	T410_mem0 = S.Task('T410_mem0', length=1, delay_cost=1)
	T410_mem0 += INPUT_mem_r
	S += T410_mem0<=T410

	T410_mem1 = S.Task('T410_mem1', length=1, delay_cost=1)
	T410_mem1 += INPUT_mem_r
	S += T410_mem1<=T410

	T411_mem0 = S.Task('T411_mem0', length=1, delay_cost=1)
	T411_mem0 += INPUT_mem_r
	S += T411_mem0<=T411

	T411_mem1 = S.Task('T411_mem1', length=1, delay_cost=1)
	T411_mem1 += INPUT_mem_r
	S += T411_mem1<=T411

	T500_mem0 = S.Task('T500_mem0', length=1, delay_cost=1)
	T500_mem0 += INPUT_mem_r
	S += T500_mem0<=T500

	T500_mem1 = S.Task('T500_mem1', length=1, delay_cost=1)
	T500_mem1 += INPUT_mem_r
	S += T500_mem1<=T500

	T501_mem0 = S.Task('T501_mem0', length=1, delay_cost=1)
	T501_mem0 += INPUT_mem_r
	S += T501_mem0<=T501

	T501_mem1 = S.Task('T501_mem1', length=1, delay_cost=1)
	T501_mem1 += INPUT_mem_r
	S += T501_mem1<=T501

	T510_mem0 = S.Task('T510_mem0', length=1, delay_cost=1)
	T510_mem0 += INPUT_mem_r
	S += T510_mem0<=T510

	T510_mem1 = S.Task('T510_mem1', length=1, delay_cost=1)
	T510_mem1 += INPUT_mem_r
	S += T510_mem1<=T510

	T511_mem0 = S.Task('T511_mem0', length=1, delay_cost=1)
	T511_mem0 += INPUT_mem_r
	S += T511_mem0<=T511

	T511_mem1 = S.Task('T511_mem1', length=1, delay_cost=1)
	T511_mem1 += INPUT_mem_r
	S += T511_mem1<=T511

	T61t2_0_mem0 = S.Task('T61t2_0_mem0', length=1, delay_cost=1)
	T61t2_0_mem0 += INPUT_mem_r
	S += T61t2_0_mem0<=T61t2_0

	T61t2_0_mem1 = S.Task('T61t2_0_mem1', length=1, delay_cost=1)
	T61t2_0_mem1 += INPUT_mem_r
	S += T61t2_0_mem1<=T61t2_0

	T61t2_1_mem0 = S.Task('T61t2_1_mem0', length=1, delay_cost=1)
	T61t2_1_mem0 += INPUT_mem_r
	S += T61t2_1_mem0<=T61t2_1

	T61t2_1_mem1 = S.Task('T61t2_1_mem1', length=1, delay_cost=1)
	T61t2_1_mem1 += INPUT_mem_r
	S += T61t2_1_mem1<=T61t2_1

	T61t3_0_mem0 = S.Task('T61t3_0_mem0', length=1, delay_cost=1)
	T61t3_0_mem0 += INPUT_mem_r
	S += T61t3_0_mem0<=T61t3_0

	T61t3_0_mem1 = S.Task('T61t3_0_mem1', length=1, delay_cost=1)
	T61t3_0_mem1 += INPUT_mem_r
	S += T61t3_0_mem1<=T61t3_0

	T61t3_1_mem0 = S.Task('T61t3_1_mem0', length=1, delay_cost=1)
	T61t3_1_mem0 += INPUT_mem_r
	S += T61t3_1_mem0<=T61t3_1

	T61t3_1_mem1 = S.Task('T61t3_1_mem1', length=1, delay_cost=1)
	T61t3_1_mem1 += INPUT_mem_r
	S += T61t3_1_mem1<=T61t3_1

	T61t0_a0b0_mem0 = S.Task('T61t0_a0b0_mem0', length=1, delay_cost=1)
	T61t0_a0b0_mem0 += INPUT_mem_r
	S += T61t0_a0b0_mem0<=T61t0_a0b0

	T61t0_a0b0_mem1 = S.Task('T61t0_a0b0_mem1', length=1, delay_cost=1)
	T61t0_a0b0_mem1 += INPUT_mem_r
	S += T61t0_a0b0_mem1<=T61t0_a0b0

	T61t1_a0b0_mem0 = S.Task('T61t1_a0b0_mem0', length=1, delay_cost=1)
	T61t1_a0b0_mem0 += INPUT_mem_r
	S += T61t1_a0b0_mem0<=T61t1_a0b0

	T61t1_a0b0_mem1 = S.Task('T61t1_a0b0_mem1', length=1, delay_cost=1)
	T61t1_a0b0_mem1 += INPUT_mem_r
	S += T61t1_a0b0_mem1<=T61t1_a0b0

	T61t2_a0b0_mem0 = S.Task('T61t2_a0b0_mem0', length=1, delay_cost=1)
	T61t2_a0b0_mem0 += INPUT_mem_r
	S += T61t2_a0b0_mem0<=T61t2_a0b0

	T61t2_a0b0_mem1 = S.Task('T61t2_a0b0_mem1', length=1, delay_cost=1)
	T61t2_a0b0_mem1 += INPUT_mem_r
	S += T61t2_a0b0_mem1<=T61t2_a0b0

	T61t3_a0b0_mem0 = S.Task('T61t3_a0b0_mem0', length=1, delay_cost=1)
	T61t3_a0b0_mem0 += INPUT_mem_r
	S += T61t3_a0b0_mem0<=T61t3_a0b0

	T61t3_a0b0_mem1 = S.Task('T61t3_a0b0_mem1', length=1, delay_cost=1)
	T61t3_a0b0_mem1 += INPUT_mem_r
	S += T61t3_a0b0_mem1<=T61t3_a0b0

	T61t0_a1b1_mem0 = S.Task('T61t0_a1b1_mem0', length=1, delay_cost=1)
	T61t0_a1b1_mem0 += INPUT_mem_r
	S += T61t0_a1b1_mem0<=T61t0_a1b1

	T61t0_a1b1_mem1 = S.Task('T61t0_a1b1_mem1', length=1, delay_cost=1)
	T61t0_a1b1_mem1 += INPUT_mem_r
	S += T61t0_a1b1_mem1<=T61t0_a1b1

	T61t1_a1b1_mem0 = S.Task('T61t1_a1b1_mem0', length=1, delay_cost=1)
	T61t1_a1b1_mem0 += INPUT_mem_r
	S += T61t1_a1b1_mem0<=T61t1_a1b1

	T61t1_a1b1_mem1 = S.Task('T61t1_a1b1_mem1', length=1, delay_cost=1)
	T61t1_a1b1_mem1 += INPUT_mem_r
	S += T61t1_a1b1_mem1<=T61t1_a1b1

	T61t2_a1b1_mem0 = S.Task('T61t2_a1b1_mem0', length=1, delay_cost=1)
	T61t2_a1b1_mem0 += INPUT_mem_r
	S += T61t2_a1b1_mem0<=T61t2_a1b1

	T61t2_a1b1_mem1 = S.Task('T61t2_a1b1_mem1', length=1, delay_cost=1)
	T61t2_a1b1_mem1 += INPUT_mem_r
	S += T61t2_a1b1_mem1<=T61t2_a1b1

	T61t3_a1b1_mem0 = S.Task('T61t3_a1b1_mem0', length=1, delay_cost=1)
	T61t3_a1b1_mem0 += INPUT_mem_r
	S += T61t3_a1b1_mem0<=T61t3_a1b1

	T61t3_a1b1_mem1 = S.Task('T61t3_a1b1_mem1', length=1, delay_cost=1)
	T61t3_a1b1_mem1 += INPUT_mem_r
	S += T61t3_a1b1_mem1<=T61t3_a1b1

	T71t2_0_mem0 = S.Task('T71t2_0_mem0', length=1, delay_cost=1)
	T71t2_0_mem0 += INPUT_mem_r
	S += T71t2_0_mem0<=T71t2_0

	T71t2_0_mem1 = S.Task('T71t2_0_mem1', length=1, delay_cost=1)
	T71t2_0_mem1 += INPUT_mem_r
	S += T71t2_0_mem1<=T71t2_0

	T71t2_1_mem0 = S.Task('T71t2_1_mem0', length=1, delay_cost=1)
	T71t2_1_mem0 += INPUT_mem_r
	S += T71t2_1_mem0<=T71t2_1

	T71t2_1_mem1 = S.Task('T71t2_1_mem1', length=1, delay_cost=1)
	T71t2_1_mem1 += INPUT_mem_r
	S += T71t2_1_mem1<=T71t2_1

	T71t3_0_mem0 = S.Task('T71t3_0_mem0', length=1, delay_cost=1)
	T71t3_0_mem0 += INPUT_mem_r
	S += T71t3_0_mem0<=T71t3_0

	T71t3_0_mem1 = S.Task('T71t3_0_mem1', length=1, delay_cost=1)
	T71t3_0_mem1 += INPUT_mem_r
	S += T71t3_0_mem1<=T71t3_0

	T71t3_1_mem0 = S.Task('T71t3_1_mem0', length=1, delay_cost=1)
	T71t3_1_mem0 += INPUT_mem_r
	S += T71t3_1_mem0<=T71t3_1

	T71t3_1_mem1 = S.Task('T71t3_1_mem1', length=1, delay_cost=1)
	T71t3_1_mem1 += INPUT_mem_r
	S += T71t3_1_mem1<=T71t3_1

	T71t0_a0b0_mem0 = S.Task('T71t0_a0b0_mem0', length=1, delay_cost=1)
	T71t0_a0b0_mem0 += INPUT_mem_r
	S += T71t0_a0b0_mem0<=T71t0_a0b0

	T71t0_a0b0_mem1 = S.Task('T71t0_a0b0_mem1', length=1, delay_cost=1)
	T71t0_a0b0_mem1 += INPUT_mem_r
	S += T71t0_a0b0_mem1<=T71t0_a0b0

	T71t1_a0b0_mem0 = S.Task('T71t1_a0b0_mem0', length=1, delay_cost=1)
	T71t1_a0b0_mem0 += INPUT_mem_r
	S += T71t1_a0b0_mem0<=T71t1_a0b0

	T71t1_a0b0_mem1 = S.Task('T71t1_a0b0_mem1', length=1, delay_cost=1)
	T71t1_a0b0_mem1 += INPUT_mem_r
	S += T71t1_a0b0_mem1<=T71t1_a0b0

	T71t2_a0b0_mem0 = S.Task('T71t2_a0b0_mem0', length=1, delay_cost=1)
	T71t2_a0b0_mem0 += INPUT_mem_r
	S += T71t2_a0b0_mem0<=T71t2_a0b0

	T71t2_a0b0_mem1 = S.Task('T71t2_a0b0_mem1', length=1, delay_cost=1)
	T71t2_a0b0_mem1 += INPUT_mem_r
	S += T71t2_a0b0_mem1<=T71t2_a0b0

	T71t3_a0b0_mem0 = S.Task('T71t3_a0b0_mem0', length=1, delay_cost=1)
	T71t3_a0b0_mem0 += INPUT_mem_r
	S += T71t3_a0b0_mem0<=T71t3_a0b0

	T71t3_a0b0_mem1 = S.Task('T71t3_a0b0_mem1', length=1, delay_cost=1)
	T71t3_a0b0_mem1 += INPUT_mem_r
	S += T71t3_a0b0_mem1<=T71t3_a0b0

	T71t0_a1b1_mem0 = S.Task('T71t0_a1b1_mem0', length=1, delay_cost=1)
	T71t0_a1b1_mem0 += INPUT_mem_r
	S += T71t0_a1b1_mem0<=T71t0_a1b1

	T71t0_a1b1_mem1 = S.Task('T71t0_a1b1_mem1', length=1, delay_cost=1)
	T71t0_a1b1_mem1 += INPUT_mem_r
	S += T71t0_a1b1_mem1<=T71t0_a1b1

	T71t1_a1b1_mem0 = S.Task('T71t1_a1b1_mem0', length=1, delay_cost=1)
	T71t1_a1b1_mem0 += INPUT_mem_r
	S += T71t1_a1b1_mem0<=T71t1_a1b1

	T71t1_a1b1_mem1 = S.Task('T71t1_a1b1_mem1', length=1, delay_cost=1)
	T71t1_a1b1_mem1 += INPUT_mem_r
	S += T71t1_a1b1_mem1<=T71t1_a1b1

	T71t2_a1b1_mem0 = S.Task('T71t2_a1b1_mem0', length=1, delay_cost=1)
	T71t2_a1b1_mem0 += INPUT_mem_r
	S += T71t2_a1b1_mem0<=T71t2_a1b1

	T71t2_a1b1_mem1 = S.Task('T71t2_a1b1_mem1', length=1, delay_cost=1)
	T71t2_a1b1_mem1 += INPUT_mem_r
	S += T71t2_a1b1_mem1<=T71t2_a1b1

	T71t3_a1b1_mem0 = S.Task('T71t3_a1b1_mem0', length=1, delay_cost=1)
	T71t3_a1b1_mem0 += INPUT_mem_r
	S += T71t3_a1b1_mem0<=T71t3_a1b1

	T71t3_a1b1_mem1 = S.Task('T71t3_a1b1_mem1', length=1, delay_cost=1)
	T71t3_a1b1_mem1 += INPUT_mem_r
	S += T71t3_a1b1_mem1<=T71t3_a1b1

	T82t2_0_mem0 = S.Task('T82t2_0_mem0', length=1, delay_cost=1)
	T82t2_0_mem0 += INPUT_mem_r
	S += T82t2_0_mem0<=T82t2_0

	T82t2_0_mem1 = S.Task('T82t2_0_mem1', length=1, delay_cost=1)
	T82t2_0_mem1 += INPUT_mem_r
	S += T82t2_0_mem1<=T82t2_0

	T82t2_1_mem0 = S.Task('T82t2_1_mem0', length=1, delay_cost=1)
	T82t2_1_mem0 += INPUT_mem_r
	S += T82t2_1_mem0<=T82t2_1

	T82t2_1_mem1 = S.Task('T82t2_1_mem1', length=1, delay_cost=1)
	T82t2_1_mem1 += INPUT_mem_r
	S += T82t2_1_mem1<=T82t2_1

	T82t3_0_mem0 = S.Task('T82t3_0_mem0', length=1, delay_cost=1)
	T82t3_0_mem0 += INPUT_mem_r
	S += T82t3_0_mem0<=T82t3_0

	T82t3_0_mem1 = S.Task('T82t3_0_mem1', length=1, delay_cost=1)
	T82t3_0_mem1 += INPUT_mem_r
	S += T82t3_0_mem1<=T82t3_0

	T82t3_1_mem0 = S.Task('T82t3_1_mem0', length=1, delay_cost=1)
	T82t3_1_mem0 += INPUT_mem_r
	S += T82t3_1_mem0<=T82t3_1

	T82t3_1_mem1 = S.Task('T82t3_1_mem1', length=1, delay_cost=1)
	T82t3_1_mem1 += INPUT_mem_r
	S += T82t3_1_mem1<=T82t3_1

	T82t0_a0b0_mem0 = S.Task('T82t0_a0b0_mem0', length=1, delay_cost=1)
	T82t0_a0b0_mem0 += INPUT_mem_r
	S += T82t0_a0b0_mem0<=T82t0_a0b0

	T82t0_a0b0_mem1 = S.Task('T82t0_a0b0_mem1', length=1, delay_cost=1)
	T82t0_a0b0_mem1 += INPUT_mem_r
	S += T82t0_a0b0_mem1<=T82t0_a0b0

	T82t1_a0b0_mem0 = S.Task('T82t1_a0b0_mem0', length=1, delay_cost=1)
	T82t1_a0b0_mem0 += INPUT_mem_r
	S += T82t1_a0b0_mem0<=T82t1_a0b0

	T82t1_a0b0_mem1 = S.Task('T82t1_a0b0_mem1', length=1, delay_cost=1)
	T82t1_a0b0_mem1 += INPUT_mem_r
	S += T82t1_a0b0_mem1<=T82t1_a0b0

	T82t2_a0b0_mem0 = S.Task('T82t2_a0b0_mem0', length=1, delay_cost=1)
	T82t2_a0b0_mem0 += INPUT_mem_r
	S += T82t2_a0b0_mem0<=T82t2_a0b0

	T82t2_a0b0_mem1 = S.Task('T82t2_a0b0_mem1', length=1, delay_cost=1)
	T82t2_a0b0_mem1 += INPUT_mem_r
	S += T82t2_a0b0_mem1<=T82t2_a0b0

	T82t3_a0b0_mem0 = S.Task('T82t3_a0b0_mem0', length=1, delay_cost=1)
	T82t3_a0b0_mem0 += INPUT_mem_r
	S += T82t3_a0b0_mem0<=T82t3_a0b0

	T82t3_a0b0_mem1 = S.Task('T82t3_a0b0_mem1', length=1, delay_cost=1)
	T82t3_a0b0_mem1 += INPUT_mem_r
	S += T82t3_a0b0_mem1<=T82t3_a0b0

	T82t0_a1b1_mem0 = S.Task('T82t0_a1b1_mem0', length=1, delay_cost=1)
	T82t0_a1b1_mem0 += INPUT_mem_r
	S += T82t0_a1b1_mem0<=T82t0_a1b1

	T82t0_a1b1_mem1 = S.Task('T82t0_a1b1_mem1', length=1, delay_cost=1)
	T82t0_a1b1_mem1 += INPUT_mem_r
	S += T82t0_a1b1_mem1<=T82t0_a1b1

	T82t1_a1b1_mem0 = S.Task('T82t1_a1b1_mem0', length=1, delay_cost=1)
	T82t1_a1b1_mem0 += INPUT_mem_r
	S += T82t1_a1b1_mem0<=T82t1_a1b1

	T82t1_a1b1_mem1 = S.Task('T82t1_a1b1_mem1', length=1, delay_cost=1)
	T82t1_a1b1_mem1 += INPUT_mem_r
	S += T82t1_a1b1_mem1<=T82t1_a1b1

	T82t2_a1b1_mem0 = S.Task('T82t2_a1b1_mem0', length=1, delay_cost=1)
	T82t2_a1b1_mem0 += INPUT_mem_r
	S += T82t2_a1b1_mem0<=T82t2_a1b1

	T82t2_a1b1_mem1 = S.Task('T82t2_a1b1_mem1', length=1, delay_cost=1)
	T82t2_a1b1_mem1 += INPUT_mem_r
	S += T82t2_a1b1_mem1<=T82t2_a1b1

	T9400_mem0 = S.Task('T9400_mem0', length=1, delay_cost=1)
	T9400_mem0 += INPUT_mem_r
	S += T9400_mem0<=T9400

	T9400_mem1 = S.Task('T9400_mem1', length=1, delay_cost=1)
	T9400_mem1 += INPUT_mem_r
	S += T9400_mem1<=T9400

	T9401_mem0 = S.Task('T9401_mem0', length=1, delay_cost=1)
	T9401_mem0 += INPUT_mem_r
	S += T9401_mem0<=T9401

	T9401_mem1 = S.Task('T9401_mem1', length=1, delay_cost=1)
	T9401_mem1 += INPUT_mem_r
	S += T9401_mem1<=T9401

	T9410_mem0 = S.Task('T9410_mem0', length=1, delay_cost=1)
	T9410_mem0 += INPUT_mem_r
	S += T9410_mem0<=T9410

	T9410_mem1 = S.Task('T9410_mem1', length=1, delay_cost=1)
	T9410_mem1 += INPUT_mem_r
	S += T9410_mem1<=T9410

	T9411_mem0 = S.Task('T9411_mem0', length=1, delay_cost=1)
	T9411_mem0 += INPUT_mem_r
	S += T9411_mem0<=T9411

	T9411_mem1 = S.Task('T9411_mem1', length=1, delay_cost=1)
	T9411_mem1 += INPUT_mem_r
	S += T9411_mem1<=T9411

	T10100_mem0 = S.Task('T10100_mem0', length=1, delay_cost=1)
	T10100_mem0 += INPUT_mem_r
	S += T10100_mem0<=T10100

	T10100_mem1 = S.Task('T10100_mem1', length=1, delay_cost=1)
	T10100_mem1 += INPUT_mem_r
	S += T10100_mem1<=T10100

	T10101_mem0 = S.Task('T10101_mem0', length=1, delay_cost=1)
	T10101_mem0 += INPUT_mem_r
	S += T10101_mem0<=T10101

	T10101_mem1 = S.Task('T10101_mem1', length=1, delay_cost=1)
	T10101_mem1 += INPUT_mem_r
	S += T10101_mem1<=T10101

	T10110_mem0 = S.Task('T10110_mem0', length=1, delay_cost=1)
	T10110_mem0 += INPUT_mem_r
	S += T10110_mem0<=T10110

	T10110_mem1 = S.Task('T10110_mem1', length=1, delay_cost=1)
	T10110_mem1 += INPUT_mem_r
	S += T10110_mem1<=T10110

	T10111_mem0 = S.Task('T10111_mem0', length=1, delay_cost=1)
	T10111_mem0 += INPUT_mem_r
	S += T10111_mem0<=T10111

	T10111_mem1 = S.Task('T10111_mem1', length=1, delay_cost=1)
	T10111_mem1 += INPUT_mem_r
	S += T10111_mem1<=T10111

	T3100_mem0 = S.Task('T3100_mem0', length=1, delay_cost=1)
	T3100_mem0 += INPUT_mem_r
	S += T3100_mem0<=T3100

	T3100_mem1 = S.Task('T3100_mem1', length=1, delay_cost=1)
	T3100_mem1 += INPUT_mem_r
	S += T3100_mem1<=T3100

	T3101_mem0 = S.Task('T3101_mem0', length=1, delay_cost=1)
	T3101_mem0 += INPUT_mem_r
	S += T3101_mem0<=T3101

	T3101_mem1 = S.Task('T3101_mem1', length=1, delay_cost=1)
	T3101_mem1 += INPUT_mem_r
	S += T3101_mem1<=T3101

	T3110_mem0 = S.Task('T3110_mem0', length=1, delay_cost=1)
	T3110_mem0 += INPUT_mem_r
	S += T3110_mem0<=T3110

	T3110_mem1 = S.Task('T3110_mem1', length=1, delay_cost=1)
	T3110_mem1 += INPUT_mem_r
	S += T3110_mem1<=T3110

	T3111_mem0 = S.Task('T3111_mem0', length=1, delay_cost=1)
	T3111_mem0 += INPUT_mem_r
	S += T3111_mem0<=T3111

	T3111_mem1 = S.Task('T3111_mem1', length=1, delay_cost=1)
	T3111_mem1 += INPUT_mem_r
	S += T3111_mem1<=T3111

	T4200_mem0 = S.Task('T4200_mem0', length=1, delay_cost=1)
	T4200_mem0 += INPUT_mem_r
	S += T4200_mem0<=T4200

	T4200_mem1 = S.Task('T4200_mem1', length=1, delay_cost=1)
	T4200_mem1 += INPUT_mem_r
	S += T4200_mem1<=T4200

	T4201_mem0 = S.Task('T4201_mem0', length=1, delay_cost=1)
	T4201_mem0 += INPUT_mem_r
	S += T4201_mem0<=T4201

	T4201_mem1 = S.Task('T4201_mem1', length=1, delay_cost=1)
	T4201_mem1 += INPUT_mem_r
	S += T4201_mem1<=T4201

	T4210_mem0 = S.Task('T4210_mem0', length=1, delay_cost=1)
	T4210_mem0 += INPUT_mem_r
	S += T4210_mem0<=T4210

	T4210_mem1 = S.Task('T4210_mem1', length=1, delay_cost=1)
	T4210_mem1 += INPUT_mem_r
	S += T4210_mem1<=T4210

	T4211_mem0 = S.Task('T4211_mem0', length=1, delay_cost=1)
	T4211_mem0 += INPUT_mem_r
	S += T4211_mem0<=T4211

	T4211_mem1 = S.Task('T4211_mem1', length=1, delay_cost=1)
	T4211_mem1 += INPUT_mem_r
	S += T4211_mem1<=T4211

	T4300_mem0 = S.Task('T4300_mem0', length=1, delay_cost=1)
	T4300_mem0 += INPUT_mem_r
	S += T4300_mem0<=T4300

	T4300_mem1 = S.Task('T4300_mem1', length=1, delay_cost=1)
	T4300_mem1 += INPUT_mem_r
	S += T4300_mem1<=T4300

	T4301_mem0 = S.Task('T4301_mem0', length=1, delay_cost=1)
	T4301_mem0 += INPUT_mem_r
	S += T4301_mem0<=T4301

	T4301_mem1 = S.Task('T4301_mem1', length=1, delay_cost=1)
	T4301_mem1 += INPUT_mem_r
	S += T4301_mem1<=T4301

	T4310_mem0 = S.Task('T4310_mem0', length=1, delay_cost=1)
	T4310_mem0 += INPUT_mem_r
	S += T4310_mem0<=T4310

	T4310_mem1 = S.Task('T4310_mem1', length=1, delay_cost=1)
	T4310_mem1 += INPUT_mem_r
	S += T4310_mem1<=T4310

	T4311_mem0 = S.Task('T4311_mem0', length=1, delay_cost=1)
	T4311_mem0 += INPUT_mem_r
	S += T4311_mem0<=T4311

	T4311_mem1 = S.Task('T4311_mem1', length=1, delay_cost=1)
	T4311_mem1 += INPUT_mem_r
	S += T4311_mem1<=T4311

	T5200_mem0 = S.Task('T5200_mem0', length=1, delay_cost=1)
	T5200_mem0 += INPUT_mem_r
	S += T5200_mem0<=T5200

	T5200_mem1 = S.Task('T5200_mem1', length=1, delay_cost=1)
	T5200_mem1 += INPUT_mem_r
	S += T5200_mem1<=T5200

	T5201_mem0 = S.Task('T5201_mem0', length=1, delay_cost=1)
	T5201_mem0 += INPUT_mem_r
	S += T5201_mem0<=T5201

	T5201_mem1 = S.Task('T5201_mem1', length=1, delay_cost=1)
	T5201_mem1 += INPUT_mem_r
	S += T5201_mem1<=T5201

	T5210_mem0 = S.Task('T5210_mem0', length=1, delay_cost=1)
	T5210_mem0 += INPUT_mem_r
	S += T5210_mem0<=T5210

	T5210_mem1 = S.Task('T5210_mem1', length=1, delay_cost=1)
	T5210_mem1 += INPUT_mem_r
	S += T5210_mem1<=T5210

	T5211_mem0 = S.Task('T5211_mem0', length=1, delay_cost=1)
	T5211_mem0 += INPUT_mem_r
	S += T5211_mem0<=T5211

	T5211_mem1 = S.Task('T5211_mem1', length=1, delay_cost=1)
	T5211_mem1 += INPUT_mem_r
	S += T5211_mem1<=T5211

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "s24_mul1_add4/s24_mul1_add4_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

if __name__ == "__main__":
	solution = solve_s24_mul1_add4_0(0, 0)