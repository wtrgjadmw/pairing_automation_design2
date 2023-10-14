from lib.ep2_operation import ep2_add, ep2_dbl

from lib.parameters import MontConv
from lib.parameters import bits_list
from lib.parameters import p, r, u, U

from lib.operate_Fp2 import negFp2, constMulFp2
from lib.operate_Fp12 import (
    mulFp12,
    conjFp12,
    FrobFp12,
    invFp12,
    expFp12,
    squareFp12,
    sparseFp12,
    SQR012345Fp12,
    expFp12_for_test,
)

from util import *


def pp_dbl_first_k12(T, P):
    T, e = ep2_dbl(T, P)
    return T, e


def pp_dbl_k12(T, f, P):
    T, e = ep2_dbl(T, P)
    f = squareFp12(f)
    f = sparseFp12(e, f)
    return T, f


def pp_add_k12(T, f, P, Q):
    T, e = ep2_add(T, P, Q)
    f = sparseFp12(e, f)
    return T, f


def pp_ml_k12(P, Q, T):
    m = U[::-1]
    f = [[[MontConv(1), 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    negQ = [Q[0], negFp2(Q[1])]

    if m[0] < 0:
        T = [Q[0], negFp2(Q[1]), [MontConv(1), 0]]

    for l in m[1:]:
        T, f = pp_dbl_k12(T, f, P)
        # printFp12(f)
        # print("-----")
        if l == 1:
            T, f = pp_add_k12(T, f, P, Q)
            # printFp12(f)
            # print("-----")
        if l == -1:
            T, f = pp_add_k12(T, f, P, negQ)
            # printFp12(f)
            # print("-----")
    return f


def pp_fe_k12(f):
    # f の (p**12-1)**3//r乗を求める
    # Easy Part
    k = FrobFp12(FrobFp12(f))
    k = mulFp12(k, f)
    l = conjFp12(k)
    k = invFp12(k)
    f = mulFp12(l, k)
    # Hard Part
    t1 = SQR012345Fp12(f)  # f^2
    t2 = expFp12(f)  # f^u
    t1 = conjFp12(t1)
    t1 = mulFp12(t1, t2)  # f^(u-2)
    t4 = expFp12(t1)  # f^(u^2-2u)
    t1 = conjFp12(t1)  # f^(-u+2)
    t1 = mulFp12(t1, f)  # f^(-u+3)
    t5 = expFp12(t4)  # f^(u^3-2u^2)
    t4 = mulFp12(f, t4)  # f^(u^2-2u+1)
    t3 = expFp12(t5)  # f^(u^4-2u^3)
    t5 = mulFp12(t2, t5)  # f^(u^3-2u^2+u)
    t2 = SQR012345Fp12(t2)  # f^2u
    t4 = FrobFp12(FrobFp12(t4))
    t5 = FrobFp12(FrobFp12(t5))
    t2 = mulFp12(t2, t3)  # f^(u^4-2u^3+2u)
    t4 = FrobFp12(t4)
    t3 = expFp12(t2)  # f^(u^5-2u^4+2u^2)
    t4 = mulFp12(t4, t5)
    g = conjFp12(f)  # f^(-1)
    t5 = mulFp12(g, t2)  # f^(u^4-2u^3+2u-1)
    t1 = mulFp12(t1, t3)  # f^(u^5-2u^4+2u^2-u+3)
    t5 = FrobFp12(t5)
    t1 = mulFp12(t1, t4)
    t1 = mulFp12(t1, t5)
    return t1


# def final_exponentiation_forRTL(f):
#     # ans = pp_fe_k12(f)
#     # f の (p**24-1)*3//r乗を求める

#     # Easy Part
#     e = invFp12(f)
#     f = mulFp12_conj_forRTL(e, f)
#     e = FrobFp24(FrobFp24(FrobFp24(FrobFp24(f))))
#     f = mulFp12(e, f)

#     # Hard Part
#     a = expFp12(f)
#     b = expFp12(a)
#     a = squareFp12(a)
#     a = mulFp12_conj_forRTL(b, a)
#     a = mulFp12(a, f)
#     b = expFp12(a)
#     e = FrobFp24(a)
#     e = mulFp12(e, b)
#     a = conjFp12(a)
#     b = expFp12(b)
#     e = FrobFp24(e)
#     e = mulFp12(e, b)
#     b = expFp12(b)
#     e = FrobFp24(e)
#     e = mulFp12(e, b)
#     b = expFp12(b)
#     b = mulFp12(b, a)
#     e = FrobFp24(e)
#     e = mulFp12(e, b)
#     b = expFp12(b)
#     e = FrobFp24(e)
#     e = mulFp12(e, b)
#     b = expFp12(b)
#     e = FrobFp24(e)
#     e = mulFp12(e, b)
#     b = expFp12(b)
#     a = squareFp12(f)
#     a = mulFp12(a, b)
#     a = mulFp12(a, f)
#     e = FrobFp24(e)
#     e = mulFp12(e, a)

#     return e


def pp_oatep_k12(P, Q, T):
    f = pp_ml_k12(P, Q, T)
    f = pp_fe_k12(f)
    return f
