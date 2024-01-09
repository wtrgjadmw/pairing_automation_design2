from pyschedule import Scenario, solvers, plotters, alt


def solve():
    horizon = 136
    S = Scenario("PADD_mul1_add4_2", horizon=horizon)

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
    t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
    S += t0_t1_in >= 0
    t0_t1_in += MUL_in[0]

    t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
    S += t0_t1_mem0 >= 0
    t0_t1_mem0 += INPUT_mem_r

    t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
    S += t0_t1_mem1 >= 0
    t0_t1_mem1 += INPUT_mem_r

    t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
    S += t0_t1 >= 1
    t0_t1 += MUL[0]

    t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
    S += t2_t0_in >= 1
    t2_t0_in += MUL_in[0]

    t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
    S += t2_t0_mem0 >= 1
    t2_t0_mem0 += INPUT_mem_r

    t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
    S += t2_t0_mem1 >= 1
    t2_t0_mem1 += INPUT_mem_r

    t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
    S += t0_t0_in >= 2
    t0_t0_in += MUL_in[0]

    t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
    S += t0_t0_mem0 >= 2
    t0_t0_mem0 += INPUT_mem_r

    t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
    S += t0_t0_mem1 >= 2
    t0_t0_mem1 += INPUT_mem_r

    t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
    S += t2_t0 >= 2
    t2_t0 += MUL[0]

    t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
    S += t0_t0 >= 3
    t0_t0 += MUL[0]

    t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
    S += t2_t1_in >= 3
    t2_t1_in += MUL_in[0]

    t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
    S += t2_t1_mem0 >= 3
    t2_t1_mem0 += INPUT_mem_r

    t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
    S += t2_t1_mem1 >= 3
    t2_t1_mem1 += INPUT_mem_r

    t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
    S += t2_t1 >= 4
    t2_t1 += MUL[0]

    t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
    S += t9_t2_mem0 >= 4
    t9_t2_mem0 += INPUT_mem_r

    t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
    S += t9_t2_mem1 >= 4
    t9_t2_mem1 += INPUT_mem_r

    t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
    S += t7_t2_mem0 >= 5
    t7_t2_mem0 += INPUT_mem_r

    t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
    S += t7_t2_mem1 >= 5
    t7_t2_mem1 += INPUT_mem_r

    t9_t2 = S.Task('t9_t2', length=1, delay_cost=1)
    S += t9_t2 >= 5
    t9_t2 += ADD[0]

    t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
    S += t0_t3_mem0 >= 6
    t0_t3_mem0 += INPUT_mem_r

    t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
    S += t0_t3_mem1 >= 6
    t0_t3_mem1 += INPUT_mem_r

    t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
    S += t7_t2 >= 6
    t7_t2 += ADD[0]

    new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
    S += new_TZ_t2_mem0 >= 7
    new_TZ_t2_mem0 += INPUT_mem_r

    new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
    S += new_TZ_t2_mem1 >= 7
    new_TZ_t2_mem1 += INPUT_mem_r

    t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
    S += t0_t3 >= 7
    t0_t3 += ADD[3]

    new_TZ_t2 = S.Task('new_TZ_t2', length=1, delay_cost=1)
    S += new_TZ_t2 >= 8
    new_TZ_t2 += ADD[1]

    t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
    S += t2_t3_mem0 >= 8
    t2_t3_mem0 += INPUT_mem_r

    t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
    S += t2_t3_mem1 >= 8
    t2_t3_mem1 += INPUT_mem_r

    t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
    S += t0_t2_mem0 >= 9
    t0_t2_mem0 += INPUT_mem_r

    t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
    S += t0_t2_mem1 >= 9
    t0_t2_mem1 += INPUT_mem_r

    t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
    S += t0_t5_mem0 >= 9
    t0_t5_mem0 += MUL_mem[0]

    t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
    S += t0_t5_mem1 >= 9
    t0_t5_mem1 += MUL_mem[0]

    t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
    S += t2_t3 >= 9
    t2_t3 += ADD[3]

    t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
    S += t0_t2 >= 10
    t0_t2 += ADD[2]

    t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
    S += t0_t4_in >= 10
    t0_t4_in += MUL_in[0]

    t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
    S += t0_t4_mem0 >= 10
    t0_t4_mem0 += ADD_mem[2]

    t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
    S += t0_t4_mem1 >= 10
    t0_t4_mem1 += ADD_mem[3]

    t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
    S += t0_t5 >= 10
    t0_t5 += ADD[1]

    t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
    S += t14_t2_mem0 >= 10
    t14_t2_mem0 += INPUT_mem_r

    t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
    S += t14_t2_mem1 >= 10
    t14_t2_mem1 += INPUT_mem_r

    t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
    S += t2_t5_mem0 >= 10
    t2_t5_mem0 += MUL_mem[0]

    t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
    S += t2_t5_mem1 >= 10
    t2_t5_mem1 += MUL_mem[0]

    t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
    S += t0_t4 >= 11
    t0_t4 += MUL[0]

    t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
    S += t14_t2 >= 11
    t14_t2 += ADD[0]

    t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
    S += t20_mem0 >= 11
    t20_mem0 += MUL_mem[0]

    t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
    S += t20_mem1 >= 11
    t20_mem1 += MUL_mem[0]

    t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
    S += t2_t2_mem0 >= 11
    t2_t2_mem0 += INPUT_mem_r

    t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
    S += t2_t2_mem1 >= 11
    t2_t2_mem1 += INPUT_mem_r

    t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
    S += t2_t5 >= 11
    t2_t5 += ADD[2]

    t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
    S += t00_mem0 >= 12
    t00_mem0 += MUL_mem[0]

    t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
    S += t00_mem1 >= 12
    t00_mem1 += MUL_mem[0]

    t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
    S += t16_t2_mem0 >= 12
    t16_t2_mem0 += INPUT_mem_r

    t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
    S += t16_t2_mem1 >= 12
    t16_t2_mem1 += INPUT_mem_r

    t20 = S.Task('t20', length=1, delay_cost=1)
    S += t20 >= 12
    t20 += ADD[1]

    t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
    S += t2_t2 >= 12
    t2_t2 += ADD[2]

    t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
    S += t2_t4_in >= 12
    t2_t4_in += MUL_in[0]

    t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
    S += t2_t4_mem0 >= 12
    t2_t4_mem0 += ADD_mem[2]

    t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
    S += t2_t4_mem1 >= 12
    t2_t4_mem1 += ADD_mem[3]

    t00 = S.Task('t00', length=1, delay_cost=1)
    S += t00 >= 13
    t00 += ADD[3]

    t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
    S += t16_t2 >= 13
    t16_t2 += ADD[0]

    t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
    S += t17_t2_mem0 >= 13
    t17_t2_mem0 += INPUT_mem_r

    t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
    S += t17_t2_mem1 >= 13
    t17_t2_mem1 += INPUT_mem_r

    t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
    S += t2_t4 >= 13
    t2_t4 += MUL[0]

    t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
    S += t10_mem0 >= 14
    t10_mem0 += INPUT_mem_r

    t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
    S += t10_mem1 >= 14
    t10_mem1 += ADD_mem[3]

    t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
    S += t17_t2 >= 14
    t17_t2 += ADD[2]

    t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
    S += t30_mem0 >= 14
    t30_mem0 += INPUT_mem_r

    t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
    S += t30_mem1 >= 14
    t30_mem1 += ADD_mem[1]

    t10 = S.Task('t10', length=1, delay_cost=1)
    S += t10 >= 15
    t10 += ADD[3]

    t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
    S += t17_t0_in >= 15
    t17_t0_in += MUL_in[0]

    t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
    S += t17_t0_mem0 >= 15
    t17_t0_mem0 += INPUT_mem_r

    t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
    S += t17_t0_mem1 >= 15
    t17_t0_mem1 += ADD_mem[3]

    t30 = S.Task('t30', length=1, delay_cost=1)
    S += t30 >= 15
    t30 += ADD[2]

    t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
    S += t16_t0_in >= 16
    t16_t0_in += MUL_in[0]

    t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
    S += t16_t0_mem0 >= 16
    t16_t0_mem0 += INPUT_mem_r

    t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
    S += t16_t0_mem1 >= 16
    t16_t0_mem1 += ADD_mem[2]

    t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
    S += t17_t0 >= 16
    t17_t0 += MUL[0]

    t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
    S += t01_mem0 >= 17
    t01_mem0 += MUL_mem[0]

    t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
    S += t01_mem1 >= 17
    t01_mem1 += ADD_mem[1]

    t16_t0 = S.Task('t16_t0', length=7, delay_cost=1)
    S += t16_t0 >= 17
    t16_t0 += MUL[0]

    t01 = S.Task('t01', length=1, delay_cost=1)
    S += t01 >= 18
    t01 += ADD[2]

    t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
    S += t11_mem0 >= 18
    t11_mem0 += INPUT_mem_r

    t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
    S += t11_mem1 >= 18
    t11_mem1 += ADD_mem[2]

    t11 = S.Task('t11', length=1, delay_cost=1)
    S += t11 >= 19
    t11 += ADD[1]

    t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
    S += t17_t3_mem0 >= 19
    t17_t3_mem0 += ADD_mem[3]

    t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
    S += t17_t3_mem1 >= 19
    t17_t3_mem1 += ADD_mem[1]

    t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
    S += t21_mem0 >= 19
    t21_mem0 += MUL_mem[0]

    t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
    S += t21_mem1 >= 19
    t21_mem1 += ADD_mem[2]

    t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
    S += t4_t3_in >= 19
    t4_t3_in += MUL_in[0]

    t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
    S += t4_t3_mem0 >= 19
    t4_t3_mem0 += ADD_mem[3]

    t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
    S += t4_t3_mem1 >= 19
    t4_t3_mem1 += ADD_mem[1]

    t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
    S += t17_t3 >= 20
    t17_t3 += ADD[0]

    t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
    S += t17_t4_in >= 20
    t17_t4_in += MUL_in[0]

    t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
    S += t17_t4_mem0 >= 20
    t17_t4_mem0 += ADD_mem[2]

    t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
    S += t17_t4_mem1 >= 20
    t17_t4_mem1 += ADD_mem[0]

    t21 = S.Task('t21', length=1, delay_cost=1)
    S += t21 >= 20
    t21 += ADD[2]

    t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
    S += t31_mem0 >= 20
    t31_mem0 += INPUT_mem_r

    t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
    S += t31_mem1 >= 20
    t31_mem1 += ADD_mem[2]

    t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
    S += t4_t0_mem0 >= 20
    t4_t0_mem0 += ADD_mem[3]

    t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
    S += t4_t0_mem1 >= 20
    t4_t0_mem1 += ADD_mem[1]

    t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
    S += t4_t1_mem0 >= 20
    t4_t1_mem0 += ADD_mem[3]

    t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
    S += t4_t1_mem1 >= 20
    t4_t1_mem1 += ADD_mem[1]

    t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
    S += t4_t3 >= 20
    t4_t3 += MUL[0]

    t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
    S += t13_t2_mem0 >= 21
    t13_t2_mem0 += ADD_mem[3]

    t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
    S += t13_t2_mem1 >= 21
    t13_t2_mem1 += ADD_mem[1]

    t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
    S += t17_t4 >= 21
    t17_t4 += MUL[0]

    t31 = S.Task('t31', length=1, delay_cost=1)
    S += t31 >= 21
    t31 += ADD[0]

    t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
    S += t4_t0 >= 21
    t4_t0 += ADD[1]

    t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
    S += t4_t1 >= 21
    t4_t1 += ADD[3]

    t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
    S += t4_t2_in >= 21
    t4_t2_in += MUL_in[0]

    t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
    S += t4_t2_mem0 >= 21
    t4_t2_mem0 += ADD_mem[1]

    t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
    S += t4_t2_mem1 >= 21
    t4_t2_mem1 += ADD_mem[3]

    t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
    S += t5_t1_mem0 >= 21
    t5_t1_mem0 += ADD_mem[2]

    t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
    S += t5_t1_mem1 >= 21
    t5_t1_mem1 += ADD_mem[0]

    t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
    S += t13_t2 >= 22
    t13_t2 += ADD[0]

    t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
    S += t4_t2 >= 22
    t4_t2 += MUL[0]

    t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
    S += t5_t0_mem0 >= 22
    t5_t0_mem0 += ADD_mem[2]

    t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
    S += t5_t0_mem1 >= 22
    t5_t0_mem1 += ADD_mem[0]

    t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
    S += t5_t1 >= 22
    t5_t1 += ADD[1]

    t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
    S += t5_t3_in >= 22
    t5_t3_in += MUL_in[0]

    t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
    S += t5_t3_mem0 >= 22
    t5_t3_mem0 += ADD_mem[2]

    t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
    S += t5_t3_mem1 >= 22
    t5_t3_mem1 += ADD_mem[0]

    t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
    S += t16_t3_mem0 >= 23
    t16_t3_mem0 += ADD_mem[2]

    t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
    S += t16_t3_mem1 >= 23
    t16_t3_mem1 += ADD_mem[0]

    t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
    S += t5_t0 >= 23
    t5_t0 += ADD[3]

    t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
    S += t5_t2_in >= 23
    t5_t2_in += MUL_in[0]

    t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
    S += t5_t2_mem0 >= 23
    t5_t2_mem0 += ADD_mem[3]

    t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
    S += t5_t2_mem1 >= 23
    t5_t2_mem1 += ADD_mem[1]

    t5_t3 = S.Task('t5_t3', length=7, delay_cost=1)
    S += t5_t3 >= 23
    t5_t3 += MUL[0]

    t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
    S += t6_t2_mem0 >= 23
    t6_t2_mem0 += ADD_mem[2]

    t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
    S += t6_t2_mem1 >= 23
    t6_t2_mem1 += ADD_mem[0]

    t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
    S += t16_t3 >= 24
    t16_t3 += ADD[1]

    t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
    S += t16_t4_in >= 24
    t16_t4_in += MUL_in[0]

    t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
    S += t16_t4_mem0 >= 24
    t16_t4_mem0 += ADD_mem[0]

    t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
    S += t16_t4_mem1 >= 24
    t16_t4_mem1 += ADD_mem[1]

    t5_t2 = S.Task('t5_t2', length=7, delay_cost=1)
    S += t5_t2 >= 24
    t5_t2 += MUL[0]

    t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
    S += t6_t2 >= 24
    t6_t2 += ADD[0]

    t16_t4 = S.Task('t16_t4', length=7, delay_cost=1)
    S += t16_t4 >= 25
    t16_t4 += MUL[0]

    t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
    S += t17_t1_in >= 25
    t17_t1_in += MUL_in[0]

    t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
    S += t17_t1_mem0 >= 25
    t17_t1_mem0 += INPUT_mem_r

    t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
    S += t17_t1_mem1 >= 25
    t17_t1_mem1 += ADD_mem[1]

    t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
    S += t16_t1_in >= 26
    t16_t1_in += MUL_in[0]

    t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
    S += t16_t1_mem0 >= 26
    t16_t1_mem0 += INPUT_mem_r

    t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
    S += t16_t1_mem1 >= 26
    t16_t1_mem1 += ADD_mem[0]

    t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
    S += t17_t1 >= 26
    t17_t1 += MUL[0]

    t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
    S += t41_mem0 >= 26
    t41_mem0 += MUL_mem[0]

    t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
    S += t41_mem1 >= 26
    t41_mem1 += MUL_mem[0]

    t16_t1 = S.Task('t16_t1', length=7, delay_cost=1)
    S += t16_t1 >= 27
    t16_t1 += MUL[0]

    t41 = S.Task('t41', length=1, delay_cost=1)
    S += t41 >= 27
    t41 += ADD[3]

    t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
    S += t4_t5_mem0 >= 27
    t4_t5_mem0 += MUL_mem[0]

    t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
    S += t4_t5_mem1 >= 27
    t4_t5_mem1 += MUL_mem[0]

    t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
    S += t7_t1_in >= 27
    t7_t1_in += MUL_in[0]

    t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
    S += t7_t1_mem0 >= 27
    t7_t1_mem0 += INPUT_mem_r

    t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
    S += t7_t1_mem1 >= 27
    t7_t1_mem1 += ADD_mem[3]

    t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
    S += t40_mem0 >= 28
    t40_mem0 += MUL_mem[0]

    t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
    S += t40_mem1 >= 28
    t40_mem1 += ADD_mem[2]

    t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
    S += t4_t5 >= 28
    t4_t5 += ADD[2]

    t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
    S += t7_t1 >= 28
    t7_t1 += MUL[0]

    t40 = S.Task('t40', length=1, delay_cost=1)
    S += t40 >= 29
    t40 += ADD[0]

    t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
    S += t51_mem0 >= 29
    t51_mem0 += MUL_mem[0]

    t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
    S += t51_mem1 >= 29
    t51_mem1 += MUL_mem[0]

    t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
    S += t7_t0_in >= 29
    t7_t0_in += MUL_in[0]

    t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
    S += t7_t0_mem0 >= 29
    t7_t0_mem0 += INPUT_mem_r

    t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
    S += t7_t0_mem1 >= 29
    t7_t0_mem1 += ADD_mem[0]

    t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
    S += t7_t3_mem0 >= 29
    t7_t3_mem0 += ADD_mem[0]

    t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
    S += t7_t3_mem1 >= 29
    t7_t3_mem1 += ADD_mem[3]

    t51 = S.Task('t51', length=1, delay_cost=1)
    S += t51 >= 30
    t51 += ADD[3]

    t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
    S += t5_t5_mem0 >= 30
    t5_t5_mem0 += MUL_mem[0]

    t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
    S += t5_t5_mem1 >= 30
    t5_t5_mem1 += MUL_mem[0]

    t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
    S += t6_t1_in >= 30
    t6_t1_in += MUL_in[0]

    t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
    S += t6_t1_mem0 >= 30
    t6_t1_mem0 += ADD_mem[0]

    t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
    S += t6_t1_mem1 >= 30
    t6_t1_mem1 += ADD_mem[3]

    t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
    S += t7_t0 >= 30
    t7_t0 += MUL[0]

    t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
    S += t7_t3 >= 30
    t7_t3 += ADD[0]

    t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
    S += t50_mem0 >= 31
    t50_mem0 += MUL_mem[0]

    t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
    S += t50_mem1 >= 31
    t50_mem1 += ADD_mem[2]

    t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
    S += t5_t5 >= 31
    t5_t5 += ADD[2]

    t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
    S += t6_t1 >= 31
    t6_t1 += MUL[0]

    t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
    S += t9_t1_in >= 31
    t9_t1_in += MUL_in[0]

    t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
    S += t9_t1_mem0 >= 31
    t9_t1_mem0 += INPUT_mem_r

    t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
    S += t9_t1_mem1 >= 31
    t9_t1_mem1 += ADD_mem[3]

    t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
    S += t17_t5_mem0 >= 32
    t17_t5_mem0 += MUL_mem[0]

    t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
    S += t17_t5_mem1 >= 32
    t17_t5_mem1 += MUL_mem[0]

    t50 = S.Task('t50', length=1, delay_cost=1)
    S += t50 >= 32
    t50 += ADD[1]

    t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
    S += t6_t0_in >= 32
    t6_t0_in += MUL_in[0]

    t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
    S += t6_t0_mem0 >= 32
    t6_t0_mem0 += ADD_mem[2]

    t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
    S += t6_t0_mem1 >= 32
    t6_t0_mem1 += ADD_mem[1]

    t9_t1 = S.Task('t9_t1', length=7, delay_cost=1)
    S += t9_t1 >= 32
    t9_t1 += MUL[0]

    t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
    S += t9_t3_mem0 >= 32
    t9_t3_mem0 += ADD_mem[1]

    t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
    S += t9_t3_mem1 >= 32
    t9_t3_mem1 += ADD_mem[3]

    t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
    S += t16_t5_mem0 >= 33
    t16_t5_mem0 += MUL_mem[0]

    t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
    S += t16_t5_mem1 >= 33
    t16_t5_mem1 += MUL_mem[0]

    t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
    S += t17_t5 >= 33
    t17_t5 += ADD[1]

    t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
    S += t6_t0 >= 33
    t6_t0 += MUL[0]

    t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
    S += t6_t3_mem0 >= 33
    t6_t3_mem0 += ADD_mem[1]

    t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
    S += t6_t3_mem1 >= 33
    t6_t3_mem1 += ADD_mem[3]

    t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
    S += t9_t0_in >= 33
    t9_t0_in += MUL_in[0]

    t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
    S += t9_t0_mem0 >= 33
    t9_t0_mem0 += INPUT_mem_r

    t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
    S += t9_t0_mem1 >= 33
    t9_t0_mem1 += ADD_mem[1]

    t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
    S += t9_t3 >= 33
    t9_t3 += ADD[0]

    t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
    S += t161_mem0 >= 34
    t161_mem0 += MUL_mem[0]

    t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
    S += t161_mem1 >= 34
    t161_mem1 += ADD_mem[0]

    t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
    S += t16_t5 >= 34
    t16_t5 += ADD[0]

    t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
    S += t171_mem0 >= 34
    t171_mem0 += MUL_mem[0]

    t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
    S += t171_mem1 >= 34
    t171_mem1 += ADD_mem[1]

    t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
    S += t6_t3 >= 34
    t6_t3 += ADD[2]

    t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
    S += t6_t4_in >= 34
    t6_t4_in += MUL_in[0]

    t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
    S += t6_t4_mem0 >= 34
    t6_t4_mem0 += ADD_mem[0]

    t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
    S += t6_t4_mem1 >= 34
    t6_t4_mem1 += ADD_mem[2]

    t9_t0 = S.Task('t9_t0', length=7, delay_cost=1)
    S += t9_t0 >= 34
    t9_t0 += MUL[0]

    t161 = S.Task('t161', length=1, delay_cost=1)
    S += t161 >= 35
    t161 += ADD[0]

    t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
    S += t170_mem0 >= 35
    t170_mem0 += MUL_mem[0]

    t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
    S += t170_mem1 >= 35
    t170_mem1 += MUL_mem[0]

    t171 = S.Task('t171', length=1, delay_cost=1)
    S += t171 >= 35
    t171 += ADD[1]

    t6_t4 = S.Task('t6_t4', length=7, delay_cost=1)
    S += t6_t4 >= 35
    t6_t4 += MUL[0]

    t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
    S += t7_t4_in >= 35
    t7_t4_in += MUL_in[0]

    t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
    S += t7_t4_mem0 >= 35
    t7_t4_mem0 += ADD_mem[0]

    t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
    S += t7_t4_mem1 >= 35
    t7_t4_mem1 += ADD_mem[0]

    t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
    S += t160_mem0 >= 36
    t160_mem0 += MUL_mem[0]

    t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
    S += t160_mem1 >= 36
    t160_mem1 += MUL_mem[0]

    t170 = S.Task('t170', length=1, delay_cost=1)
    S += t170 >= 36
    t170 += ADD[1]

    t7_t4 = S.Task('t7_t4', length=7, delay_cost=1)
    S += t7_t4 >= 36
    t7_t4 += MUL[0]

    t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
    S += t9_t4_in >= 36
    t9_t4_in += MUL_in[0]

    t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
    S += t9_t4_mem0 >= 36
    t9_t4_mem0 += ADD_mem[0]

    t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
    S += t9_t4_mem1 >= 36
    t9_t4_mem1 += ADD_mem[0]

    t160 = S.Task('t160', length=1, delay_cost=1)
    S += t160 >= 37
    t160 += ADD[3]

    t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
    S += t70_mem0 >= 37
    t70_mem0 += MUL_mem[0]

    t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
    S += t70_mem1 >= 37
    t70_mem1 += MUL_mem[0]

    t9_t4 = S.Task('t9_t4', length=7, delay_cost=1)
    S += t9_t4 >= 37
    t9_t4 += MUL[0]

    t70 = S.Task('t70', length=1, delay_cost=1)
    S += t70 >= 38
    t70 += ADD[1]

    t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
    S += t7_t5_mem0 >= 38
    t7_t5_mem0 += MUL_mem[0]

    t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
    S += t7_t5_mem1 >= 38
    t7_t5_mem1 += MUL_mem[0]

    t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
    S += t60_mem0 >= 39
    t60_mem0 += MUL_mem[0]

    t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
    S += t60_mem1 >= 39
    t60_mem1 += MUL_mem[0]

    t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
    S += t7_t5 >= 39
    t7_t5 += ADD[0]

    new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
    S += new_TZ_t0_in >= 40
    new_TZ_t0_in += MUL_in[0]

    new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
    S += new_TZ_t0_mem0 >= 40
    new_TZ_t0_mem0 += INPUT_mem_r

    new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
    S += new_TZ_t0_mem1 >= 40
    new_TZ_t0_mem1 += ADD_mem[0]

    t60 = S.Task('t60', length=1, delay_cost=1)
    S += t60 >= 40
    t60 += ADD[0]

    t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
    S += t80_mem0 >= 40
    t80_mem0 += ADD_mem[0]

    t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
    S += t80_mem1 >= 40
    t80_mem1 += ADD_mem[1]

    t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
    S += t90_mem0 >= 40
    t90_mem0 += MUL_mem[0]

    t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
    S += t90_mem1 >= 40
    t90_mem1 += MUL_mem[0]

    new_TZ_t0 = S.Task('new_TZ_t0', length=7, delay_cost=1)
    S += new_TZ_t0 >= 41
    new_TZ_t0 += MUL[0]

    t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
    S += t100_mem0 >= 41
    t100_mem0 += ADD_mem[2]

    t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
    S += t100_mem1 >= 41
    t100_mem1 += ADD_mem[2]

    t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
    S += t14_t0_in >= 41
    t14_t0_in += MUL_in[0]

    t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
    S += t14_t0_mem0 >= 41
    t14_t0_mem0 += INPUT_mem_r

    t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
    S += t14_t0_mem1 >= 41
    t14_t0_mem1 += ADD_mem[0]

    t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
    S += t6_t5_mem0 >= 41
    t6_t5_mem0 += MUL_mem[0]

    t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
    S += t6_t5_mem1 >= 41
    t6_t5_mem1 += MUL_mem[0]

    t80 = S.Task('t80', length=1, delay_cost=1)
    S += t80 >= 41
    t80 += ADD[1]

    t90 = S.Task('t90', length=1, delay_cost=1)
    S += t90 >= 41
    t90 += ADD[2]

    t100 = S.Task('t100', length=1, delay_cost=1)
    S += t100 >= 42
    t100 += ADD[1]

    t14_t0 = S.Task('t14_t0', length=7, delay_cost=1)
    S += t14_t0 >= 42
    t14_t0 += MUL[0]

    t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
    S += t61_mem0 >= 42
    t61_mem0 += MUL_mem[0]

    t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
    S += t61_mem1 >= 42
    t61_mem1 += ADD_mem[0]

    t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
    S += t6_t5 >= 42
    t6_t5 += ADD[0]

    t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
    S += t71_mem0 >= 42
    t71_mem0 += MUL_mem[0]

    t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
    S += t71_mem1 >= 42
    t71_mem1 += ADD_mem[0]

    t61 = S.Task('t61', length=1, delay_cost=1)
    S += t61 >= 43
    t61 += ADD[0]

    t71 = S.Task('t71', length=1, delay_cost=1)
    S += t71 >= 43
    t71 += ADD[3]

    t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
    S += t9_t5_mem0 >= 43
    t9_t5_mem0 += MUL_mem[0]

    t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
    S += t9_t5_mem1 >= 43
    t9_t5_mem1 += MUL_mem[0]

    t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
    S += t91_mem0 >= 44
    t91_mem0 += MUL_mem[0]

    t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
    S += t91_mem1 >= 44
    t91_mem1 += ADD_mem[3]

    t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
    S += t9_t5 >= 44
    t9_t5 += ADD[3]

    t91 = S.Task('t91', length=1, delay_cost=1)
    S += t91 >= 45
    t91 += ADD[0]

    # new tasks
    new_xt_t2 = S.Task('new_xt_t2', length=1, delay_cost=1)
    new_xt_t2 += alt(ADD)

    new_xt_t2_mem0 = S.Task('new_xt_t2_mem0', length=1, delay_cost=1)
    new_xt_t2_mem0 += ADD_mem[2]
    S += 15 < new_xt_t2_mem0
    S += new_xt_t2_mem0 <= new_xt_t2

    new_xt_t2_mem1 = S.Task('new_xt_t2_mem1', length=1, delay_cost=1)
    new_xt_t2_mem1 += ADD_mem[0]
    S += 21 < new_xt_t2_mem1
    S += new_xt_t2_mem1 <= new_xt_t2

    t81 = S.Task('t81', length=1, delay_cost=1)
    t81 += alt(ADD)

    t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
    t81_mem0 += ADD_mem[0]
    S += 43 < t81_mem0
    S += t81_mem0 <= t81

    t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
    t81_mem1 += ADD_mem[3]
    S += 43 < t81_mem1
    S += t81_mem1 <= t81

    t101 = S.Task('t101', length=1, delay_cost=1)
    t101 += alt(ADD)

    t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
    t101_mem0 += ADD_mem[0]
    S += 45 < t101_mem0
    S += t101_mem0 <= t101

    t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
    t101_mem1 += ADD_mem[0]
    S += 45 < t101_mem1
    S += t101_mem1 <= t101

    t110 = S.Task('t110', length=1, delay_cost=1)
    t110 += alt(ADD)

    t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
    t110_mem0 += ADD_mem[1]
    S += 41 < t110_mem0
    S += t110_mem0 <= t110

    t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
    t110_mem1 += ADD_mem[1]
    S += 42 < t110_mem1
    S += t110_mem1 <= t110

    t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
    t14_t1_in += alt(MUL_in)
    t14_t1 = S.Task('t14_t1', length=7, delay_cost=1)
    t14_t1 += alt(MUL)
    S += t14_t1 >= t14_t1_in

    t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
    t14_t1_mem0 += INPUT_mem_r
    S += t14_t1_mem0 <= t14_t1

    t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
    t14_t1_mem1 += ADD_mem[0]
    S += 43 < t14_t1_mem1
    S += t14_t1_mem1 <= t14_t1

    t14_t3 = S.Task('t14_t3', length=1, delay_cost=1)
    t14_t3 += alt(ADD)

    t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
    t14_t3_mem0 += ADD_mem[0]
    S += 40 < t14_t3_mem0
    S += t14_t3_mem0 <= t14_t3

    t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
    t14_t3_mem1 += ADD_mem[0]
    S += 43 < t14_t3_mem1
    S += t14_t3_mem1 <= t14_t3

    new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
    new_TZ_t1_in += alt(MUL_in)
    new_TZ_t1 = S.Task('new_TZ_t1', length=7, delay_cost=1)
    new_TZ_t1 += alt(MUL)
    S += new_TZ_t1 >= new_TZ_t1_in

    new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
    new_TZ_t1_mem0 += INPUT_mem_r
    S += new_TZ_t1_mem0 <= new_TZ_t1

    new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
    new_TZ_t1_mem1 += ADD_mem[0]
    S += 43 < new_TZ_t1_mem1
    S += new_TZ_t1_mem1 <= new_TZ_t1

    new_TZ_t3 = S.Task('new_TZ_t3', length=1, delay_cost=1)
    new_TZ_t3 += alt(ADD)

    new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
    new_TZ_t3_mem0 += ADD_mem[0]
    S += 40 < new_TZ_t3_mem0
    S += new_TZ_t3_mem0 <= new_TZ_t3

    new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
    new_TZ_t3_mem1 += ADD_mem[0]
    S += 43 < new_TZ_t3_mem1
    S += new_TZ_t3_mem1 <= new_TZ_t3

    t111 = S.Task('t111', length=1, delay_cost=1)
    t111 += alt(ADD)

    t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
    t111_mem0 += alt(ADD_mem)
    S += (t81 * ADD[0]) - 1 < t111_mem0 * ADD_mem[0]
    S += (t81 * ADD[1]) - 1 < t111_mem0 * ADD_mem[1]
    S += (t81 * ADD[2]) - 1 < t111_mem0 * ADD_mem[2]
    S += (t81 * ADD[3]) - 1 < t111_mem0 * ADD_mem[3]
    S += t111_mem0 <= t111

    t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
    t111_mem1 += alt(ADD_mem)
    S += (t101 * ADD[0]) - 1 < t111_mem1 * ADD_mem[0]
    S += (t101 * ADD[1]) - 1 < t111_mem1 * ADD_mem[1]
    S += (t101 * ADD[2]) - 1 < t111_mem1 * ADD_mem[2]
    S += (t101 * ADD[3]) - 1 < t111_mem1 * ADD_mem[3]
    S += t111_mem1 <= t111

    t120 = S.Task('t120', length=1, delay_cost=1)
    t120 += alt(ADD)

    t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
    t120_mem0 += alt(ADD_mem)
    S += (t110 * ADD[0]) - 1 < t120_mem0 * ADD_mem[0]
    S += (t110 * ADD[1]) - 1 < t120_mem0 * ADD_mem[1]
    S += (t110 * ADD[2]) - 1 < t120_mem0 * ADD_mem[2]
    S += (t110 * ADD[3]) - 1 < t120_mem0 * ADD_mem[3]
    S += t120_mem0 <= t120

    t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
    t120_mem1 += ADD_mem[2]
    S += 41 < t120_mem1
    S += t120_mem1 <= t120

    new_xt_t0_in = S.Task('new_xt_t0_in', length=1, delay_cost=1)
    new_xt_t0_in += alt(MUL_in)
    new_xt_t0 = S.Task('new_xt_t0', length=7, delay_cost=1)
    new_xt_t0 += alt(MUL)
    S += new_xt_t0 >= new_xt_t0_in

    new_xt_t0_mem0 = S.Task('new_xt_t0_mem0', length=1, delay_cost=1)
    new_xt_t0_mem0 += ADD_mem[2]
    S += 15 < new_xt_t0_mem0
    S += new_xt_t0_mem0 <= new_xt_t0

    new_xt_t0_mem1 = S.Task('new_xt_t0_mem1', length=1, delay_cost=1)
    new_xt_t0_mem1 += alt(ADD_mem)
    S += (t110 * ADD[0]) - 1 < new_xt_t0_mem1 * ADD_mem[0]
    S += (t110 * ADD[1]) - 1 < new_xt_t0_mem1 * ADD_mem[1]
    S += (t110 * ADD[2]) - 1 < new_xt_t0_mem1 * ADD_mem[2]
    S += (t110 * ADD[3]) - 1 < new_xt_t0_mem1 * ADD_mem[3]
    S += new_xt_t0_mem1 <= new_xt_t0

    t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
    t14_t4_in += alt(MUL_in)
    t14_t4 = S.Task('t14_t4', length=7, delay_cost=1)
    t14_t4 += alt(MUL)
    S += t14_t4 >= t14_t4_in

    t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
    t14_t4_mem0 += ADD_mem[0]
    S += 11 < t14_t4_mem0
    S += t14_t4_mem0 <= t14_t4

    t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
    t14_t4_mem1 += alt(ADD_mem)
    S += (t14_t3 * ADD[0]) - 1 < t14_t4_mem1 * ADD_mem[0]
    S += (t14_t3 * ADD[1]) - 1 < t14_t4_mem1 * ADD_mem[1]
    S += (t14_t3 * ADD[2]) - 1 < t14_t4_mem1 * ADD_mem[2]
    S += (t14_t3 * ADD[3]) - 1 < t14_t4_mem1 * ADD_mem[3]
    S += t14_t4_mem1 <= t14_t4

    t140 = S.Task('t140', length=1, delay_cost=1)
    t140 += alt(ADD)

    t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
    t140_mem0 += MUL_mem[0]
    S += 48 < t140_mem0
    S += t140_mem0 <= t140

    t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
    t140_mem1 += alt(MUL_mem)
    S += (t14_t1 * MUL[0]) - 1 < t140_mem1 * MUL_mem[0]
    S += t140_mem1 <= t140

    t14_t5 = S.Task('t14_t5', length=1, delay_cost=1)
    t14_t5 += alt(ADD)

    t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
    t14_t5_mem0 += MUL_mem[0]
    S += 48 < t14_t5_mem0
    S += t14_t5_mem0 <= t14_t5

    t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
    t14_t5_mem1 += alt(MUL_mem)
    S += (t14_t1 * MUL[0]) - 1 < t14_t5_mem1 * MUL_mem[0]
    S += t14_t5_mem1 <= t14_t5

    new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
    new_TZ_t4_in += alt(MUL_in)
    new_TZ_t4 = S.Task('new_TZ_t4', length=7, delay_cost=1)
    new_TZ_t4 += alt(MUL)
    S += new_TZ_t4 >= new_TZ_t4_in

    new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
    new_TZ_t4_mem0 += ADD_mem[1]
    S += 8 < new_TZ_t4_mem0
    S += new_TZ_t4_mem0 <= new_TZ_t4

    new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
    new_TZ_t4_mem1 += alt(ADD_mem)
    S += (new_TZ_t3 * ADD[0]) - 1 < new_TZ_t4_mem1 * ADD_mem[0]
    S += (new_TZ_t3 * ADD[1]) - 1 < new_TZ_t4_mem1 * ADD_mem[1]
    S += (new_TZ_t3 * ADD[2]) - 1 < new_TZ_t4_mem1 * ADD_mem[2]
    S += (new_TZ_t3 * ADD[3]) - 1 < new_TZ_t4_mem1 * ADD_mem[3]
    S += new_TZ_t4_mem1 <= new_TZ_t4

    new_TZ_t5 = S.Task('new_TZ_t5', length=1, delay_cost=1)
    new_TZ_t5 += alt(ADD)

    new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
    new_TZ_t5_mem0 += MUL_mem[0]
    S += 47 < new_TZ_t5_mem0
    S += new_TZ_t5_mem0 <= new_TZ_t5

    new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
    new_TZ_t5_mem1 += alt(MUL_mem)
    S += (new_TZ_t1 * MUL[0]) - 1 < new_TZ_t5_mem1 * MUL_mem[0]
    S += new_TZ_t5_mem1 <= new_TZ_t5

    t121 = S.Task('t121', length=1, delay_cost=1)
    t121 += alt(ADD)

    t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
    t121_mem0 += alt(ADD_mem)
    S += (t111 * ADD[0]) - 1 < t121_mem0 * ADD_mem[0]
    S += (t111 * ADD[1]) - 1 < t121_mem0 * ADD_mem[1]
    S += (t111 * ADD[2]) - 1 < t121_mem0 * ADD_mem[2]
    S += (t111 * ADD[3]) - 1 < t121_mem0 * ADD_mem[3]
    S += t121_mem0 <= t121

    t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
    t121_mem1 += ADD_mem[0]
    S += 45 < t121_mem1
    S += t121_mem1 <= t121

    new_xt_t1_in = S.Task('new_xt_t1_in', length=1, delay_cost=1)
    new_xt_t1_in += alt(MUL_in)
    new_xt_t1 = S.Task('new_xt_t1', length=7, delay_cost=1)
    new_xt_t1 += alt(MUL)
    S += new_xt_t1 >= new_xt_t1_in

    new_xt_t1_mem0 = S.Task('new_xt_t1_mem0', length=1, delay_cost=1)
    new_xt_t1_mem0 += ADD_mem[0]
    S += 21 < new_xt_t1_mem0
    S += new_xt_t1_mem0 <= new_xt_t1

    new_xt_t1_mem1 = S.Task('new_xt_t1_mem1', length=1, delay_cost=1)
    new_xt_t1_mem1 += alt(ADD_mem)
    S += (t111 * ADD[0]) - 1 < new_xt_t1_mem1 * ADD_mem[0]
    S += (t111 * ADD[1]) - 1 < new_xt_t1_mem1 * ADD_mem[1]
    S += (t111 * ADD[2]) - 1 < new_xt_t1_mem1 * ADD_mem[2]
    S += (t111 * ADD[3]) - 1 < new_xt_t1_mem1 * ADD_mem[3]
    S += new_xt_t1_mem1 <= new_xt_t1

    new_xt_t3 = S.Task('new_xt_t3', length=1, delay_cost=1)
    new_xt_t3 += alt(ADD)

    new_xt_t3_mem0 = S.Task('new_xt_t3_mem0', length=1, delay_cost=1)
    new_xt_t3_mem0 += alt(ADD_mem)
    S += (t110 * ADD[0]) - 1 < new_xt_t3_mem0 * ADD_mem[0]
    S += (t110 * ADD[1]) - 1 < new_xt_t3_mem0 * ADD_mem[1]
    S += (t110 * ADD[2]) - 1 < new_xt_t3_mem0 * ADD_mem[2]
    S += (t110 * ADD[3]) - 1 < new_xt_t3_mem0 * ADD_mem[3]
    S += new_xt_t3_mem0 <= new_xt_t3

    new_xt_t3_mem1 = S.Task('new_xt_t3_mem1', length=1, delay_cost=1)
    new_xt_t3_mem1 += alt(ADD_mem)
    S += (t111 * ADD[0]) - 1 < new_xt_t3_mem1 * ADD_mem[0]
    S += (t111 * ADD[1]) - 1 < new_xt_t3_mem1 * ADD_mem[1]
    S += (t111 * ADD[2]) - 1 < new_xt_t3_mem1 * ADD_mem[2]
    S += (t111 * ADD[3]) - 1 < new_xt_t3_mem1 * ADD_mem[3]
    S += new_xt_t3_mem1 <= new_xt_t3

    t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
    t13_t0_in += alt(MUL_in)
    t13_t0 = S.Task('t13_t0', length=7, delay_cost=1)
    t13_t0 += alt(MUL)
    S += t13_t0 >= t13_t0_in

    t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
    t13_t0_mem0 += ADD_mem[3]
    S += 15 < t13_t0_mem0
    S += t13_t0_mem0 <= t13_t0

    t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
    t13_t0_mem1 += alt(ADD_mem)
    S += (t120 * ADD[0]) - 1 < t13_t0_mem1 * ADD_mem[0]
    S += (t120 * ADD[1]) - 1 < t13_t0_mem1 * ADD_mem[1]
    S += (t120 * ADD[2]) - 1 < t13_t0_mem1 * ADD_mem[2]
    S += (t120 * ADD[3]) - 1 < t13_t0_mem1 * ADD_mem[3]
    S += t13_t0_mem1 <= t13_t0

    t141 = S.Task('t141', length=1, delay_cost=1)
    t141 += alt(ADD)

    t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
    t141_mem0 += alt(MUL_mem)
    S += (t14_t4 * MUL[0]) - 1 < t141_mem0 * MUL_mem[0]
    S += t141_mem0 <= t141

    t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
    t141_mem1 += alt(ADD_mem)
    S += (t14_t5 * ADD[0]) - 1 < t141_mem1 * ADD_mem[0]
    S += (t14_t5 * ADD[1]) - 1 < t141_mem1 * ADD_mem[1]
    S += (t14_t5 * ADD[2]) - 1 < t141_mem1 * ADD_mem[2]
    S += (t14_t5 * ADD[3]) - 1 < t141_mem1 * ADD_mem[3]
    S += t141_mem1 <= t141

    new_xt_t4_in = S.Task('new_xt_t4_in', length=1, delay_cost=1)
    new_xt_t4_in += alt(MUL_in)
    new_xt_t4 = S.Task('new_xt_t4', length=7, delay_cost=1)
    new_xt_t4 += alt(MUL)
    S += new_xt_t4 >= new_xt_t4_in

    new_xt_t4_mem0 = S.Task('new_xt_t4_mem0', length=1, delay_cost=1)
    new_xt_t4_mem0 += alt(ADD_mem)
    S += (new_xt_t2 * ADD[0]) - 1 < new_xt_t4_mem0 * ADD_mem[0]
    S += (new_xt_t2 * ADD[1]) - 1 < new_xt_t4_mem0 * ADD_mem[1]
    S += (new_xt_t2 * ADD[2]) - 1 < new_xt_t4_mem0 * ADD_mem[2]
    S += (new_xt_t2 * ADD[3]) - 1 < new_xt_t4_mem0 * ADD_mem[3]
    S += new_xt_t4_mem0 <= new_xt_t4

    new_xt_t4_mem1 = S.Task('new_xt_t4_mem1', length=1, delay_cost=1)
    new_xt_t4_mem1 += alt(ADD_mem)
    S += (new_xt_t3 * ADD[0]) - 1 < new_xt_t4_mem1 * ADD_mem[0]
    S += (new_xt_t3 * ADD[1]) - 1 < new_xt_t4_mem1 * ADD_mem[1]
    S += (new_xt_t3 * ADD[2]) - 1 < new_xt_t4_mem1 * ADD_mem[2]
    S += (new_xt_t3 * ADD[3]) - 1 < new_xt_t4_mem1 * ADD_mem[3]
    S += new_xt_t4_mem1 <= new_xt_t4

    new_xt_t5 = S.Task('new_xt_t5', length=1, delay_cost=1)
    new_xt_t5 += alt(ADD)

    new_xt_t5_mem0 = S.Task('new_xt_t5_mem0', length=1, delay_cost=1)
    new_xt_t5_mem0 += alt(MUL_mem)
    S += (new_xt_t0 * MUL[0]) - 1 < new_xt_t5_mem0 * MUL_mem[0]
    S += new_xt_t5_mem0 <= new_xt_t5

    new_xt_t5_mem1 = S.Task('new_xt_t5_mem1', length=1, delay_cost=1)
    new_xt_t5_mem1 += alt(MUL_mem)
    S += (new_xt_t1 * MUL[0]) - 1 < new_xt_t5_mem1 * MUL_mem[0]
    S += new_xt_t5_mem1 <= new_xt_t5

    t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
    t13_t1_in += alt(MUL_in)
    t13_t1 = S.Task('t13_t1', length=7, delay_cost=1)
    t13_t1 += alt(MUL)
    S += t13_t1 >= t13_t1_in

    t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
    t13_t1_mem0 += ADD_mem[1]
    S += 19 < t13_t1_mem0
    S += t13_t1_mem0 <= t13_t1

    t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
    t13_t1_mem1 += alt(ADD_mem)
    S += (t121 * ADD[0]) - 1 < t13_t1_mem1 * ADD_mem[0]
    S += (t121 * ADD[1]) - 1 < t13_t1_mem1 * ADD_mem[1]
    S += (t121 * ADD[2]) - 1 < t13_t1_mem1 * ADD_mem[2]
    S += (t121 * ADD[3]) - 1 < t13_t1_mem1 * ADD_mem[3]
    S += t13_t1_mem1 <= t13_t1

    t13_t3 = S.Task('t13_t3', length=1, delay_cost=1)
    t13_t3 += alt(ADD)

    t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
    t13_t3_mem0 += alt(ADD_mem)
    S += (t120 * ADD[0]) - 1 < t13_t3_mem0 * ADD_mem[0]
    S += (t120 * ADD[1]) - 1 < t13_t3_mem0 * ADD_mem[1]
    S += (t120 * ADD[2]) - 1 < t13_t3_mem0 * ADD_mem[2]
    S += (t120 * ADD[3]) - 1 < t13_t3_mem0 * ADD_mem[3]
    S += t13_t3_mem0 <= t13_t3

    t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
    t13_t3_mem1 += alt(ADD_mem)
    S += (t121 * ADD[0]) - 1 < t13_t3_mem1 * ADD_mem[0]
    S += (t121 * ADD[1]) - 1 < t13_t3_mem1 * ADD_mem[1]
    S += (t121 * ADD[2]) - 1 < t13_t3_mem1 * ADD_mem[2]
    S += (t121 * ADD[3]) - 1 < t13_t3_mem1 * ADD_mem[3]
    S += t13_t3_mem1 <= t13_t3

    t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
    t13_t4_in += alt(MUL_in)
    t13_t4 = S.Task('t13_t4', length=7, delay_cost=1)
    t13_t4 += alt(MUL)
    S += t13_t4 >= t13_t4_in

    t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
    t13_t4_mem0 += ADD_mem[0]
    S += 22 < t13_t4_mem0
    S += t13_t4_mem0 <= t13_t4

    t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
    t13_t4_mem1 += alt(ADD_mem)
    S += (t13_t3 * ADD[0]) - 1 < t13_t4_mem1 * ADD_mem[0]
    S += (t13_t3 * ADD[1]) - 1 < t13_t4_mem1 * ADD_mem[1]
    S += (t13_t3 * ADD[2]) - 1 < t13_t4_mem1 * ADD_mem[2]
    S += (t13_t3 * ADD[3]) - 1 < t13_t4_mem1 * ADD_mem[3]
    S += t13_t4_mem1 <= t13_t4

    t130 = S.Task('t130', length=1, delay_cost=1)
    t130 += alt(ADD)

    t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
    t130_mem0 += alt(MUL_mem)
    S += (t13_t0 * MUL[0]) - 1 < t130_mem0 * MUL_mem[0]
    S += t130_mem0 <= t130

    t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
    t130_mem1 += alt(MUL_mem)
    S += (t13_t1 * MUL[0]) - 1 < t130_mem1 * MUL_mem[0]
    S += t130_mem1 <= t130

    t13_t5 = S.Task('t13_t5', length=1, delay_cost=1)
    t13_t5 += alt(ADD)

    t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
    t13_t5_mem0 += alt(MUL_mem)
    S += (t13_t0 * MUL[0]) - 1 < t13_t5_mem0 * MUL_mem[0]
    S += t13_t5_mem0 <= t13_t5

    t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
    t13_t5_mem1 += alt(MUL_mem)
    S += (t13_t1 * MUL[0]) - 1 < t13_t5_mem1 * MUL_mem[0]
    S += t13_t5_mem1 <= t13_t5

    t131 = S.Task('t131', length=1, delay_cost=1)
    t131 += alt(ADD)

    t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
    t131_mem0 += alt(MUL_mem)
    S += (t13_t4 * MUL[0]) - 1 < t131_mem0 * MUL_mem[0]
    S += t131_mem0 <= t131

    t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
    t131_mem1 += alt(ADD_mem)
    S += (t13_t5 * ADD[0]) - 1 < t131_mem1 * ADD_mem[0]
    S += (t13_t5 * ADD[1]) - 1 < t131_mem1 * ADD_mem[1]
    S += (t13_t5 * ADD[2]) - 1 < t131_mem1 * ADD_mem[2]
    S += (t13_t5 * ADD[3]) - 1 < t131_mem1 * ADD_mem[3]
    S += t131_mem1 <= t131

    l000_in = S.Task('l000_in', length=1, delay_cost=1)
    l000_in += alt(MUL_in)
    l000 = S.Task('l000', length=7, delay_cost=1)
    l000 += alt(MUL)
    S += l000 >= l000_in

    l000_mem0 = S.Task('l000_mem0', length=1, delay_cost=1)
    l000_mem0 += ADD_mem[2]
    S += 15 < l000_mem0
    S += l000_mem0 <= l000

    l000_mem1 = S.Task('l000_mem1', length=1, delay_cost=1)
    l000_mem1 += INPUT_mem_r
    S += l000_mem1 <= l000

    l000_w = S.Task('l000_w', length=1, delay_cost=1)
    l000_w += alt(INPUT_mem_w)
    S += l000 - 1 <= l000_w

    l100_in = S.Task('l100_in', length=1, delay_cost=1)
    l100_in += alt(MUL_in)
    l100 = S.Task('l100', length=7, delay_cost=1)
    l100 += alt(MUL)
    S += l100 >= l100_in

    l100_mem0 = S.Task('l100_mem0', length=1, delay_cost=1)
    l100_mem0 += ADD_mem[3]
    S += 15 < l100_mem0
    S += l100_mem0 <= l100

    l100_mem1 = S.Task('l100_mem1', length=1, delay_cost=1)
    l100_mem1 += INPUT_mem_r
    S += l100_mem1 <= l100

    l100_w = S.Task('l100_w', length=1, delay_cost=1)
    l100_w += alt(INPUT_mem_w)
    S += l100 - 1 <= l100_w

    l001_in = S.Task('l001_in', length=1, delay_cost=1)
    l001_in += alt(MUL_in)
    l001 = S.Task('l001', length=7, delay_cost=1)
    l001 += alt(MUL)
    S += l001 >= l001_in

    l001_mem0 = S.Task('l001_mem0', length=1, delay_cost=1)
    l001_mem0 += ADD_mem[0]
    S += 21 < l001_mem0
    S += l001_mem0 <= l001

    l001_mem1 = S.Task('l001_mem1', length=1, delay_cost=1)
    l001_mem1 += INPUT_mem_r
    S += l001_mem1 <= l001

    l001_w = S.Task('l001_w', length=1, delay_cost=1)
    l001_w += alt(INPUT_mem_w)
    S += l001 - 1 <= l001_w

    l101_in = S.Task('l101_in', length=1, delay_cost=1)
    l101_in += alt(MUL_in)
    l101 = S.Task('l101', length=7, delay_cost=1)
    l101 += alt(MUL)
    S += l101 >= l101_in

    l101_mem0 = S.Task('l101_mem0', length=1, delay_cost=1)
    l101_mem0 += ADD_mem[1]
    S += 19 < l101_mem0
    S += l101_mem0 <= l101

    l101_mem1 = S.Task('l101_mem1', length=1, delay_cost=1)
    l101_mem1 += INPUT_mem_r
    S += l101_mem1 <= l101

    l101_w = S.Task('l101_w', length=1, delay_cost=1)
    l101_w += alt(INPUT_mem_w)
    S += l101 - 1 <= l101_w

    l010 = S.Task('l010', length=1, delay_cost=1)
    l010 += alt(ADD)

    l010_mem0 = S.Task('l010_mem0', length=1, delay_cost=1)
    l010_mem0 += ADD_mem[3]
    S += 37 < l010_mem0
    S += l010_mem0 <= l010

    l010_mem1 = S.Task('l010_mem1', length=1, delay_cost=1)
    l010_mem1 += ADD_mem[1]
    S += 36 < l010_mem1
    S += l010_mem1 <= l010

    l010_w = S.Task('l010_w', length=1, delay_cost=1)
    l010_w += alt(INPUT_mem_w)
    S += l010 - 1 <= l010_w

    l011 = S.Task('l011', length=1, delay_cost=1)
    l011 += alt(ADD)

    l011_mem0 = S.Task('l011_mem0', length=1, delay_cost=1)
    l011_mem0 += ADD_mem[0]
    S += 35 < l011_mem0
    S += l011_mem0 <= l011

    l011_mem1 = S.Task('l011_mem1', length=1, delay_cost=1)
    l011_mem1 += ADD_mem[1]
    S += 35 < l011_mem1
    S += l011_mem1 <= l011

    l011_w = S.Task('l011_w', length=1, delay_cost=1)
    l011_w += alt(INPUT_mem_w)
    S += l011 - 1 <= l011_w

    new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
    new_TZ0 += alt(ADD)

    new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
    new_TZ0_mem0 += MUL_mem[0]
    S += 47 < new_TZ0_mem0
    S += new_TZ0_mem0 <= new_TZ0

    new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
    new_TZ0_mem1 += alt(MUL_mem)
    S += (new_TZ_t1 * MUL[0]) - 1 < new_TZ0_mem1 * MUL_mem[0]
    S += new_TZ0_mem1 <= new_TZ0

    new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
    new_TZ0_w += alt(INPUT_mem_w)
    S += new_TZ0 - 1 <= new_TZ0_w

    new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
    new_TZ1 += alt(ADD)

    new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
    new_TZ1_mem0 += alt(MUL_mem)
    S += (new_TZ_t4 * MUL[0]) - 1 < new_TZ1_mem0 * MUL_mem[0]
    S += new_TZ1_mem0 <= new_TZ1

    new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
    new_TZ1_mem1 += alt(ADD_mem)
    S += (new_TZ_t5 * ADD[0]) - 1 < new_TZ1_mem1 * ADD_mem[0]
    S += (new_TZ_t5 * ADD[1]) - 1 < new_TZ1_mem1 * ADD_mem[1]
    S += (new_TZ_t5 * ADD[2]) - 1 < new_TZ1_mem1 * ADD_mem[2]
    S += (new_TZ_t5 * ADD[3]) - 1 < new_TZ1_mem1 * ADD_mem[3]
    S += new_TZ1_mem1 <= new_TZ1

    new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
    new_TZ1_w += alt(INPUT_mem_w)
    S += new_TZ1 - 1 <= new_TZ1_w

    new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
    new_TX0 += alt(ADD)

    new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
    new_TX0_mem0 += alt(MUL_mem)
    S += (new_xt_t0 * MUL[0]) - 1 < new_TX0_mem0 * MUL_mem[0]
    S += new_TX0_mem0 <= new_TX0

    new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
    new_TX0_mem1 += alt(MUL_mem)
    S += (new_xt_t1 * MUL[0]) - 1 < new_TX0_mem1 * MUL_mem[0]
    S += new_TX0_mem1 <= new_TX0

    new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
    new_TX0_w += alt(INPUT_mem_w)
    S += new_TX0 - 1 <= new_TX0_w

    new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
    new_TX1 += alt(ADD)

    new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
    new_TX1_mem0 += alt(MUL_mem)
    S += (new_xt_t4 * MUL[0]) - 1 < new_TX1_mem0 * MUL_mem[0]
    S += new_TX1_mem0 <= new_TX1

    new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
    new_TX1_mem1 += alt(ADD_mem)
    S += (new_xt_t5 * ADD[0]) - 1 < new_TX1_mem1 * ADD_mem[0]
    S += (new_xt_t5 * ADD[1]) - 1 < new_TX1_mem1 * ADD_mem[1]
    S += (new_xt_t5 * ADD[2]) - 1 < new_TX1_mem1 * ADD_mem[2]
    S += (new_xt_t5 * ADD[3]) - 1 < new_TX1_mem1 * ADD_mem[3]
    S += new_TX1_mem1 <= new_TX1

    new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
    new_TX1_w += alt(INPUT_mem_w)
    S += new_TX1 - 1 <= new_TX1_w

    t150 = S.Task('t150', length=1, delay_cost=1)
    t150 += alt(ADD)

    t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
    t150_mem0 += alt(ADD_mem)
    S += (t130 * ADD[0]) - 1 < t150_mem0 * ADD_mem[0]
    S += (t130 * ADD[1]) - 1 < t150_mem0 * ADD_mem[1]
    S += (t130 * ADD[2]) - 1 < t150_mem0 * ADD_mem[2]
    S += (t130 * ADD[3]) - 1 < t150_mem0 * ADD_mem[3]
    S += t150_mem0 <= t150

    t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
    t150_mem1 += alt(ADD_mem)
    S += (t140 * ADD[0]) - 1 < t150_mem1 * ADD_mem[0]
    S += (t140 * ADD[1]) - 1 < t150_mem1 * ADD_mem[1]
    S += (t140 * ADD[2]) - 1 < t150_mem1 * ADD_mem[2]
    S += (t140 * ADD[3]) - 1 < t150_mem1 * ADD_mem[3]
    S += t150_mem1 <= t150

    t150_w = S.Task('t150_w', length=1, delay_cost=1)
    t150_w += alt(INPUT_mem_w)
    S += t150 - 1 <= t150_w

    new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
    new_TY0 += alt(ADD)

    new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
    new_TY0_mem0 += INPUT_mem_r
    S += new_TY0_mem0 <= new_TY0

    new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
    new_TY0_mem1 += alt(ADD_mem)
    S += (t130 * ADD[0]) - 1 < new_TY0_mem1 * ADD_mem[0]
    S += (t130 * ADD[1]) - 1 < new_TY0_mem1 * ADD_mem[1]
    S += (t130 * ADD[2]) - 1 < new_TY0_mem1 * ADD_mem[2]
    S += (t130 * ADD[3]) - 1 < new_TY0_mem1 * ADD_mem[3]
    S += new_TY0_mem1 <= new_TY0

    new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
    new_TY0_w += alt(INPUT_mem_w)
    S += new_TY0 - 1 <= new_TY0_w

    t151 = S.Task('t151', length=1, delay_cost=1)
    t151 += alt(ADD)

    t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
    t151_mem0 += alt(ADD_mem)
    S += (t131 * ADD[0]) - 1 < t151_mem0 * ADD_mem[0]
    S += (t131 * ADD[1]) - 1 < t151_mem0 * ADD_mem[1]
    S += (t131 * ADD[2]) - 1 < t151_mem0 * ADD_mem[2]
    S += (t131 * ADD[3]) - 1 < t151_mem0 * ADD_mem[3]
    S += t151_mem0 <= t151

    t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
    t151_mem1 += alt(ADD_mem)
    S += (t141 * ADD[0]) - 1 < t151_mem1 * ADD_mem[0]
    S += (t141 * ADD[1]) - 1 < t151_mem1 * ADD_mem[1]
    S += (t141 * ADD[2]) - 1 < t151_mem1 * ADD_mem[2]
    S += (t141 * ADD[3]) - 1 < t151_mem1 * ADD_mem[3]
    S += t151_mem1 <= t151

    t151_w = S.Task('t151_w', length=1, delay_cost=1)
    t151_w += alt(INPUT_mem_w)
    S += t151 - 1 <= t151_w

    new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
    new_TY1 += alt(ADD)

    new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
    new_TY1_mem0 += INPUT_mem_r
    S += new_TY1_mem0 <= new_TY1

    new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
    new_TY1_mem1 += alt(ADD_mem)
    S += (t131 * ADD[0]) - 1 < new_TY1_mem1 * ADD_mem[0]
    S += (t131 * ADD[1]) - 1 < new_TY1_mem1 * ADD_mem[1]
    S += (t131 * ADD[2]) - 1 < new_TY1_mem1 * ADD_mem[2]
    S += (t131 * ADD[3]) - 1 < new_TY1_mem1 * ADD_mem[3]
    S += new_TY1_mem1 <= new_TY1

    new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
    new_TY1_w += alt(INPUT_mem_w)
    S += new_TY1 - 1 <= new_TY1_w

    solvers.mip.solve(S, msg=1, kind='CPLEX', ratio_gap=1.01)

    solution = [['hoge'] * len(S.solution()[1]) for i in range(len(S.solution()))]
    for i in range(len(S.solution())):
        for j in range(len(S.solution()[i])):
            solution[i][j] = str(S.solution()[i][j])
    print(solution)

    cycles = int(solution[-1][3])

    pic_file_name = "PADD_mul1_add4/PADD_mul1_add4_2.png"
    if (S.solution() != []):
        plotters.matplotlib.plot(S, img_filename=pic_file_name, vertical_text=True, fig_size=(cycles * 0.25 + 3, 5), show_task_labels=False)

    return solution
