from lib.ep4_operation import ep4_add_relic, ep4_dbl_relic

from lib.parameters import MontConv
from lib.parameters import bits_list
from lib.parameters import p, r, u, U

from lib.operate_Fp4 import negFp4, constMulFp4
from lib.operate_Fp12 import conjFp12
from lib.operate_Fp24 import (
    mulFp24,
    conjFp24,
    FrobFp24,
    invFp24,
    expFp24,
    sparseFp24,
    squareFp24,
    sparseFp24,
    mulFp24_conj_forRTL,
    squareFp24_forRTL,
)

from util import *


def pp_dbl_first_k24(T, P):
    T, e = ep4_dbl_relic(T, P)
    return T, e


def pp_dbl_k24(T, f, P):
    T, e = ep4_dbl_relic(T, P)
    f = squareFp24_forRTL(f)
    f = sparseFp24(e, f)
    return T, f


def pp_add_k24(T, f, P, Q):
    T, e = ep4_add_relic(T, P, Q)
    f = sparseFp24(e, f)
    return T, f


def pp_ml_k24(P, Q, T):
    m = U[::-1]
    f = [
        [[[MontConv(1), 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    ]
    negQ = [Q[0], negFp4(Q[1])]
    PforDBL = [
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]]],
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    ]
    PforDBL[0] = constMulFp4(P[0], MontConv(3))
    PforDBL[1] = negFp4(P[1])

    if m[0] < 0:
        T = [Q[0], negFp4(Q[1]), [[MontConv(1), 0], [0, 0]]]

    for l in m[1:]:
        T, f = pp_dbl_k24(T, f, PforDBL)
        # printFp24(f)
        # print("-----")
        if l == 1:
            T, f = pp_add_k24(T, f, P, Q)
            # printFp24(f)
            # print("-----")
        if l == -1:
            T, f = pp_add_k24(T, f, P, negQ)
            # printFp24(f)
            # print("-----")
    return f


def pp_fe_k24(f):
    # f の (p**24-1)*3//r乗を求める

    # Easy Part
    f_ = conjFp24(f)
    f_inv = invFp24(f)
    t0 = mulFp24(f_, f_inv)
    t1 = FrobFp24(FrobFp24(FrobFp24(FrobFp24(t0))))
    fdash = mulFp24(t1, t0)

    # Hard Part
    t0 = expFp24(fdash)
    t1 = expFp24(t0)
    t2 = squareFp24(t0)
    t3 = conjFp24(t2)
    t4 = mulFp24(t1, t3)
    m7 = mulFp24(t4, fdash)
    m6 = expFp24(m7)
    m5 = expFp24(m6)
    m4 = expFp24(m5)
    t5 = expFp24(m4)
    t6 = conjFp24(m7)
    m3 = mulFp24(t5, t6)
    m2 = expFp24(m3)
    m1 = expFp24(m2)
    t7 = expFp24(m1)
    t8 = squareFp24(fdash)
    t9 = mulFp24(t7, t8)
    m0 = mulFp24(t9, fdash)
    res = FrobFp24(m7)
    res = mulFp24(res, m6)
    res = FrobFp24(res)
    res = mulFp24(res, m5)
    res = FrobFp24(res)
    res = mulFp24(res, m4)
    res = FrobFp24(res)
    res = mulFp24(res, m3)
    res = FrobFp24(res)
    res = mulFp24(res, m2)
    res = FrobFp24(res)
    res = mulFp24(res, m1)
    res = FrobFp24(res)
    res = mulFp24(res, m0)
    return res


def final_exponentiation_forRTL(f):
    # ans = pp_fe_k24(f)
    # f の (p**24-1)*3//r乗を求める

    # Easy Part
    e = invFp24(f)
    f = mulFp24_conj_forRTL(e, f)
    e = FrobFp24(FrobFp24(FrobFp24(FrobFp24(f))))
    f = mulFp24(e, f)

    # Hard Part
    a = expFp24(f)
    b = expFp24(a)
    a = squareFp24(a)
    a = mulFp24_conj_forRTL(b, a)
    a = mulFp24(a, f)
    b = expFp24(a)
    e = FrobFp24(a)
    e = mulFp24(e, b)
    a = conjFp24(a)
    b = expFp24(b)
    e = FrobFp24(e)
    e = mulFp24(e, b)
    b = expFp24(b)
    e = FrobFp24(e)
    e = mulFp24(e, b)
    b = expFp24(b)
    b = mulFp24(b, a)
    e = FrobFp24(e)
    e = mulFp24(e, b)
    b = expFp24(b)
    e = FrobFp24(e)
    e = mulFp24(e, b)
    b = expFp24(b)
    e = FrobFp24(e)
    e = mulFp24(e, b)
    b = expFp24(b)
    a = squareFp24(f)
    a = mulFp24(a, b)
    a = mulFp24(a, f)
    e = FrobFp24(e)
    e = mulFp24(e, a)

    return e


def pp_oatep_k24(P, Q, T):
    f = pp_ml_k24(P, Q, T)
    f = final_exponentiation_forRTL(f)
    return f
