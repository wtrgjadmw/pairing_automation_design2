from lib.operate_Fp12 import (
    Fp12SparseMul_forRTL,
    addFp12,
    subFp12,
    mulFp12,
    guzaiFp12,
    negFp12,
    invFp12,
    constMulFp12,
    squareFp12,
    Fp12SparseMul,
)
from lib.operate_Fp4 import (
    addFp4,
    invFp4_forRTL,
    mulFp4,
    subFp4,
    expFp4,
    conjFp4,
    guzaiFp4,
    squareFp4,
    negFp4,
    FrobFp4,
    mulFp4,
    invFp4,
)
from lib.parameters import p, MontConv, bits_of, U
from lib.util import *

# Fp24: [a0, a1] -> a0 + a1z (Fp12: a0 = [a00, a01, a02] -> a00 + a01w + a02w^2)


def mulFp24(a, b):
    t0 = mulFp12(a[0], b[0])
    t1 = mulFp12(a[1], b[1])
    t2 = mulFp12(addFp12(a[0], a[1]), addFp12(b[0], b[1]))
    c1 = subFp12(t2, addFp12(t0, t1))
    t1 = guzaiFp12(t1)
    c0 = addFp12(t0, t1)
    return [c0, c1]


def mulFp24_forRTL(a, b):
    # t0 = mulFp12(a[0], b[0])
    T0 = mulFp4(a[0][0], b[0][0])
    T1 = mulFp4(a[0][1], b[0][1])
    T2 = mulFp4(a[0][2], b[0][2])
    T3 = addFp4(a[0][0], a[0][1])
    T4 = addFp4(b[0][0], b[0][1])
    T3 = mulFp4(T3, T4)
    T4 = addFp4(a[0][1], a[0][2])
    T5 = addFp4(b[0][1], b[0][2])
    T4 = mulFp4(T4, T5)
    T5 = addFp4(a[0][0], a[0][2])
    T6 = addFp4(b[0][0], b[0][2])
    T5 = mulFp4(T5, T6)
    T3 = subFp4(T3, T0)
    T3 = subFp4(T3, T1)
    T4 = subFp4(T4, T1)
    T4 = subFp4(T4, T2)
    T4 = guzaiFp4(T4)
    T7 = addFp4(T0, T4)  # c0
    T5 = subFp4(T5, T2)
    T5 = subFp4(T5, T0)
    T2 = guzaiFp4(T2)
    T8 = addFp4(T3, T2)  # c1
    T9 = addFp4(T1, T5)  # c2
    # t1 = mulFp12(a[1], b[1])
    T0 = mulFp4(a[1][0], b[1][0])
    T1 = mulFp4(a[1][1], b[1][1])
    T2 = mulFp4(a[1][2], b[1][2])
    T3 = addFp4(a[1][0], a[1][1])
    T4 = addFp4(b[1][0], b[1][1])
    T3 = mulFp4(T3, T4)
    T4 = addFp4(a[1][1], a[1][2])
    T5 = addFp4(b[1][1], b[1][2])
    T4 = mulFp4(T4, T5)
    T5 = addFp4(a[1][0], a[1][2])
    T6 = addFp4(b[1][0], b[1][2])
    T5 = mulFp4(T5, T6)
    T3 = subFp4(T3, T0)
    T3 = subFp4(T3, T1)
    T4 = subFp4(T4, T1)
    T4 = subFp4(T4, T2)
    T4 = guzaiFp4(T4)
    T10 = addFp4(T0, T4)  # c0
    T5 = subFp4(T5, T2)
    T5 = subFp4(T5, T0)
    T2 = guzaiFp4(T2)
    T11 = addFp4(T3, T2)  # c1
    T12 = addFp4(T1, T5)  # c2
    # t2 = mulFp12(addFp12(a[0], a[1]), addFp12(b[0], b[1]))
    T13 = addFp4(a[0][0], a[1][0])
    T14 = addFp4(a[0][1], a[1][1])
    T15 = addFp4(a[0][2], a[1][2])
    T16 = addFp4(b[0][0], b[1][0])
    T17 = addFp4(b[0][1], b[1][1])
    T18 = addFp4(b[0][2], b[1][2])
    T0 = mulFp4(T13, T16)
    T1 = mulFp4(T14, T17)
    T2 = mulFp4(T15, T18)
    T3 = addFp4(T13, T14)
    T4 = addFp4(T16, T17)
    T3 = mulFp4(T3, T4)
    T4 = addFp4(T14, T15)
    T5 = addFp4(T17, T18)
    T4 = mulFp4(T4, T5)
    T5 = addFp4(T13, T15)
    T6 = addFp4(T16, T18)
    T5 = mulFp4(T5, T6)
    T3 = subFp4(T3, T0)
    T3 = subFp4(T3, T1)
    T4 = subFp4(T4, T1)
    T4 = subFp4(T4, T2)
    T4 = guzaiFp4(T4)
    T4 = addFp4(T0, T4)  # c0
    T5 = subFp4(T5, T2)
    T5 = subFp4(T5, T0)
    T2 = guzaiFp4(T2)
    T3 = addFp4(T3, T2)  # c1
    T5 = addFp4(T1, T5)  # c2
    # c1 = subFp12(t2, addFp12(t0, t1))
    C10 = subFp4(T4, T7)
    C10 = subFp4(C10, T10)
    C11 = subFp4(T3, T8)
    C11 = subFp4(C11, T11)
    C12 = subFp4(T5, T9)
    C12 = subFp4(C12, T12)
    # t1 = guzaiFp12(t1)
    T12 = guzaiFp4(T12)
    # c0 = addFp12(t0, t1)
    C00 = addFp4(T7, T12)
    C01 = addFp4(T8, T10)
    C02 = addFp4(T9, T11)
    return [[C00, C01, C02], [C10, C11, C12]]


def mulFp24_conj_forRTL(a, b):
    # t0 = mulFp12(a[0], b[0])
    T0 = mulFp4(a[0][0], b[0][0])
    T1 = mulFp4(a[0][1], b[0][1])
    T2 = mulFp4(a[0][2], b[0][2])
    T3 = addFp4(a[0][0], a[0][1])
    T4 = addFp4(b[0][0], b[0][1])
    T3 = mulFp4(T3, T4)
    T4 = addFp4(a[0][1], a[0][2])
    T5 = addFp4(b[0][1], b[0][2])
    T4 = mulFp4(T4, T5)
    T5 = addFp4(a[0][0], a[0][2])
    T6 = addFp4(b[0][0], b[0][2])
    T5 = mulFp4(T5, T6)
    T3 = subFp4(T3, T0)
    T3 = subFp4(T3, T1)
    T4 = subFp4(T4, T1)
    T4 = subFp4(T4, T2)
    T4 = guzaiFp4(T4)
    T7 = addFp4(T0, T4)  # c0
    T5 = subFp4(T5, T2)
    T5 = subFp4(T5, T0)
    T2 = guzaiFp4(T2)
    T8 = addFp4(T3, T2)  # c1
    T9 = addFp4(T1, T5)  # c2
    # t1 = mulFp12(a[1], negFp12(b[1]))
    T0 = mulFp4(a[1][0], b[1][0])
    T1 = mulFp4(a[1][1], b[1][1])
    T2 = mulFp4(a[1][2], b[1][2])
    T3 = addFp4(a[1][0], a[1][1])
    T4 = addFp4(b[1][0], b[1][1])
    T3 = mulFp4(T3, T4)
    T4 = addFp4(a[1][1], a[1][2])
    T5 = addFp4(b[1][1], b[1][2])
    T4 = mulFp4(T4, T5)
    T5 = addFp4(a[1][0], a[1][2])
    T6 = addFp4(b[1][0], b[1][2])
    T5 = mulFp4(T5, T6)
    T3 = subFp4(T0, T3)
    T3 = addFp4(T3, T1)
    T4 = subFp4(T1, T4)
    T4 = addFp4(T4, T2)
    T4 = guzaiFp4(T4)
    T10 = subFp4(T4, T0)  # c0
    T5 = subFp4(T2, T5)
    T5 = addFp4(T5, T0)
    T2 = guzaiFp4(T2)
    T11 = subFp4(T3, T2)  # c1
    T12 = subFp4(T5, T1)  # c2
    # t2 = mulFp12(addFp12(a[0], a[1]), subFp12(b[0], b[1]))
    a[0][0] = addFp4(a[0][0], a[1][0])
    a[0][1] = addFp4(a[0][1], a[1][1])
    a[0][2] = addFp4(a[0][2], a[1][2])
    b[0][0] = subFp4(b[0][0], b[1][0])
    b[0][1] = subFp4(b[0][1], b[1][1])
    b[0][2] = subFp4(b[0][2], b[1][2])
    T0 = mulFp4(a[0][0], b[0][0])
    T1 = mulFp4(a[0][1], b[0][1])
    T2 = mulFp4(a[0][2], b[0][2])
    T3 = addFp4(a[0][0], a[0][1])
    T4 = addFp4(b[0][0], b[0][1])
    T3 = mulFp4(T3, T4)
    T4 = addFp4(a[0][1], a[0][2])
    T5 = addFp4(b[0][1], b[0][2])
    T4 = mulFp4(T4, T5)
    T5 = addFp4(a[0][0], a[0][2])
    T6 = addFp4(b[0][0], b[0][2])
    T5 = mulFp4(T5, T6)
    T3 = subFp4(T3, T0)
    T3 = subFp4(T3, T1)
    T4 = subFp4(T4, T1)
    T4 = subFp4(T4, T2)
    T4 = guzaiFp4(T4)
    T4 = addFp4(T0, T4)  # c0
    T5 = subFp4(T5, T2)
    T5 = subFp4(T5, T0)
    T2 = guzaiFp4(T2)
    T3 = addFp4(T3, T2)  # c1
    T5 = addFp4(T1, T5)  # c2
    # c1 = subFp12(t2, addFp12(t0, t1))
    C10 = subFp4(T4, T7)
    C10 = subFp4(C10, T10)
    C11 = subFp4(T3, T8)
    C11 = subFp4(C11, T11)
    C12 = subFp4(T5, T9)
    C12 = subFp4(C12, T12)
    # t1 = guzaiFp12(t1)
    T12 = guzaiFp4(T12)
    # c0 = addFp12(t0, t1)
    C00 = addFp4(T7, T12)
    C01 = addFp4(T8, T10)
    C02 = addFp4(T9, T11)
    return [[C00, C01, C02], [C10, C11, C12]]


def squareFp24(a):
    t0 = addFp12(a[0], guzaiFp12(a[1]))
    t1 = addFp12(a[0], a[1])
    t2 = mulFp12(t0, t1)
    t3 = mulFp12(a[0], a[1])
    t4 = guzaiFp12(t3)
    t5 = addFp12(t3, t4)
    c0 = subFp12(t2, t5)
    c1 = addFp12(t3, t3)
    return [c0, c1]


def squareFp24_forRTL(a):
    # t0 = addFp12(a[0], guzaiFp12(a[1]))
    T0 = guzaiFp4(a[1][2])
    T0 = addFp4(a[0][0], T0)
    T1 = addFp4(a[0][1], a[1][0])
    T2 = addFp4(a[0][2], a[1][1])
    # t1 = addFp12(a[0], a[1])
    T3 = addFp4(a[0][0], a[1][0])
    T4 = addFp4(a[0][1], a[1][1])
    T5 = addFp4(a[0][2], a[1][2])
    # t2 = mulFp12(t0, t1)
    T6 = mulFp4(T0, T3)
    T7 = mulFp4(T1, T4)
    T8 = mulFp4(T2, T5)
    T9 = addFp4(T0, T1)
    T10 = addFp4(T3, T4)
    T9 = mulFp4(T9, T10)
    T1 = addFp4(T1, T2)
    T4 = addFp4(T4, T5)
    T1 = mulFp4(T1, T4)
    T2 = addFp4(T0, T2)
    T5 = addFp4(T3, T5)
    T2 = mulFp4(T2, T5)
    T9 = subFp4(T9, T6)
    T9 = subFp4(T9, T7)
    T1 = subFp4(T1, T7)
    T1 = subFp4(T1, T8)
    T1 = guzaiFp4(T1)
    T0 = addFp4(T6, T1)  # c0
    T2 = subFp4(T2, T8)
    T2 = subFp4(T2, T6)
    T8 = guzaiFp4(T8)
    T1 = addFp4(T9, T8)  # c1
    T2 = addFp4(T7, T2)  # c2
    # t3 = mulFp12(a[0], a[1])
    T6 = mulFp4(a[0][0], a[1][0])
    T7 = mulFp4(a[0][1], a[1][1])
    T8 = mulFp4(a[0][2], a[1][2])
    T9 = addFp4(a[0][0], a[0][1])
    T10 = addFp4(a[1][0], a[1][1])
    T9 = mulFp4(T9, T10)
    T3 = addFp4(a[0][1], a[0][2])
    T4 = addFp4(a[1][1], a[1][2])
    T3 = mulFp4(T3, T4)
    T4 = addFp4(a[0][0], a[0][2])
    T5 = addFp4(a[1][0], a[1][2])
    T4 = mulFp4(T4, T5)
    T9 = subFp4(T9, T6)
    T9 = subFp4(T9, T7)
    T3 = subFp4(T3, T7)
    T3 = subFp4(T3, T8)
    T3 = guzaiFp4(T3)
    T3 = addFp4(T6, T3)  # c0
    T4 = subFp4(T4, T8)
    T4 = subFp4(T4, T6)
    T8 = guzaiFp4(T8)
    T5 = addFp4(T7, T4)  # c2
    T4 = addFp4(T9, T8)  # c1
    # t4 = guzaiFp12(t3)
    # t5 = addFp12(t3, t4)
    T6 = guzaiFp4(T5)
    T6 = addFp4(T3, T6)
    T7 = addFp4(T4, T3)
    T8 = addFp4(T5, T4)
    # c0 = subFp12(t2, t5)
    C00 = subFp4(T0, T6)
    C01 = subFp4(T1, T7)
    C02 = subFp4(T2, T8)
    # c1 = addFp12(t3, t3)
    C10 = addFp4(T3, T3)
    C11 = addFp4(T4, T4)
    C12 = addFp4(T5, T5)
    return [[C00, C01, C02], [C10, C11, C12]]


def SQR012345Fp24(a):
    T0 = squareFp4(a[0][0])
    T1 = addFp4(a[0][0], a[0][2])
    T2 = subFp4(T1, a[0][1])
    T1 = addFp4(T1, a[0][1])
    T1 = squareFp4(T1)
    T2 = squareFp4(T2)
    T3 = mulFp4(a[0][2], a[0][1])
    T3 = addFp4(T3, T3)
    T4 = squareFp4(a[0][2])
    T5 = mulFp4(a[0][0], a[1][1])
    T6 = mulFp4(a[0][1], a[1][2])
    T7 = mulFp4(a[1][0], a[0][2])
    c00 = guzaiFp4(T3)
    c00 = addFp4(T0, c00)
    c00 = addFp4(c00, c00)
    c00 = subFp4(c00, [[MontConv(1), 0], [0, 0]])
    c02 = addFp4(T0, T4)
    c02 = addFp4(c02, c02)
    c02 = subFp4(T1, c02)
    c02 = addFp4(T2, c02)
    T4 = guzaiFp4(T4)
    c01 = subFp4(T4, T3)
    c01 = addFp4(c01, c01)
    c01 = addFp4(c01, T1)
    c01 = subFp4(c01, T2)
    T1 = addFp4(T6, T6)
    T1 = addFp4(T1, T6)
    T1 = guzaiFp4(T1)
    c10 = addFp4(a[1][0], T1)
    c10 = addFp4(c10, c10)
    T2 = addFp4(T7, T7)
    T2 = addFp4(T2, T7)
    c12 = addFp4(T2, a[1][2])
    c12 = addFp4(c12, c12)
    T3 = addFp4(T5, T5)
    T3 = addFp4(T3, T5)
    c11 = addFp4(T3, a[1][1])
    c11 = addFp4(c11, c11)
    return [[c00, c01, c02], [c10, c11, c12]]


def invFp24(a):
    aa = squareFp12(a[0])
    bb = squareFp12(a[1])
    bbxi = guzaiFp12(bb)
    denom = subFp12(aa, bbxi)
    denom_inv = invFp12(denom)
    c0 = mulFp12(a[0], denom_inv)
    c1 = mulFp12(a[1], denom_inv)
    return [c0, negFp12(c1)]


def invFp24_forRTL(a):
    # aa = squareFp12(a[0])
    t0 = squareFp4(a[0][0])
    t1 = squareFp4(a[0][1])
    t2 = squareFp4(a[0][2])
    A00 = addFp4(a[0][0], a[0][1])
    t3 = squareFp4(A00)
    t4 = addFp4(t0, t1)
    t3 = subFp4(t3, t4)
    A01 = addFp4(a[0][1], a[0][2])
    t4 = squareFp4(A01)
    t5 = addFp4(t1, t2)
    t4 = subFp4(t4, t5)
    t4 = guzaiFp4(t4)
    A02 = addFp4(a[0][2], a[0][0])
    t5 = squareFp4(A02)
    t6 = addFp4(t2, t0)
    t5 = subFp4(t5, t6)
    t2 = guzaiFp4(t2)
    c0 = addFp4(t0, t4)
    c1 = addFp4(t3, t2)
    c2 = addFp4(t1, t5)
    # bb = squareFp12(a[1])
    t0 = squareFp4(a[1][0])
    t1 = squareFp4(a[1][1])
    t2 = squareFp4(a[1][2])
    A10 = addFp4(a[1][0], a[1][1])
    t3 = squareFp4(A10)
    t4 = addFp4(t0, t1)
    t3 = subFp4(t3, t4)
    A11 = addFp4(a[1][1], a[1][2])
    t4 = squareFp4(A11)
    t5 = addFp4(t1, t2)
    t4 = subFp4(t4, t5)
    t4 = guzaiFp4(t4)
    A12 = addFp4(a[1][2], a[1][0])
    t5 = squareFp4(A12)
    t6 = addFp4(t2, t0)
    t5 = subFp4(t5, t6)
    t2 = guzaiFp4(t2)
    c3 = addFp4(t0, t4)
    c4 = addFp4(t3, t2)
    c5 = addFp4(t1, t5)
    # bbxi = guzaiFp12(bb)
    c5 = guzaiFp4(c5)
    # denom = subFp12(aa, bbxi)
    c0 = subFp4(c0, c5)
    c1 = subFp4(c1, c3)
    c2 = subFp4(c2, c4)
    # denom_inv = invFp12(denom)
    t0 = squareFp4(c0)
    t1 = squareFp4(c1)
    t2 = squareFp4(c2)
    t3 = mulFp4(c0, c1)
    t4 = mulFp4(c1, c2)
    t5 = mulFp4(c2, c0)
    t4 = guzaiFp4(t4)
    t0 = subFp4(t0, t4)
    t2 = guzaiFp4(t2)
    t2 = subFp4(t2, t3)
    t1 = subFp4(t1, t5)
    t3 = mulFp4(t2, c2)
    t4 = mulFp4(t1, c1)
    t4 = addFp4(t3, t4)
    t4 = guzaiFp4(t4)
    t5 = mulFp4(t0, c0)
    t4 = addFp4(t4, t5)
    t4 = invFp4(t4)
    t7 = mulFp4(t0, t4)
    t8 = mulFp4(t2, t4)
    t9 = mulFp4(t1, t4)
    # C0 = mulFp12(a[0], denom_inv)
    t0 = mulFp4(a[0][0], t7)
    t1 = mulFp4(a[0][1], t8)
    t2 = mulFp4(a[0][2], t9)
    t10 = addFp4(t7, t8)
    t3 = mulFp4(A00, t10)
    t4 = addFp4(t0, t1)
    t3 = subFp4(t3, t4)
    t11 = addFp4(t8, t9)
    t4 = mulFp4(A01, t11)
    t5 = addFp4(t1, t2)
    t4 = subFp4(t4, t5)
    t4 = guzaiFp4(t4)
    t12 = addFp4(t9, t7)
    t5 = mulFp4(A02, t12)
    t6 = addFp4(t2, t0)
    t5 = subFp4(t5, t6)
    c0 = addFp4(t0, t4)
    t2 = guzaiFp4(t2)
    c1 = addFp4(t3, t2)
    c2 = addFp4(t1, t5)
    # C1 = mulFp12(a[1], denom_inv)
    t0 = mulFp4(a[1][0], t7)
    t1 = mulFp4(a[1][1], t8)
    t2 = mulFp4(a[1][2], t9)
    t3 = mulFp4(A10, t10)
    t4 = addFp4(t0, t1)
    t3 = subFp4(t4, t3)
    t4 = mulFp4(A11, t11)
    t5 = addFp4(t1, t2)
    t4 = subFp4(t5, t4)
    t4 = guzaiFp4(t4)
    t5 = mulFp4(A12, t12)
    t6 = addFp4(t2, t0)
    t5 = subFp4(t6, t5)
    c3 = subFp4(t4, t0)
    t2 = guzaiFp4(t2)
    c4 = subFp4(t3, t2)
    c5 = subFp4(t5, t1)
    return [[c0, c1, c2], [c3, c4, c5]]


def conjFp24(a):
    return [a[0], negFp12(a[1])]


# referring to https://link.springer.com/chapter/10.1007/978-3-642-35999-6_11
def sparseFp24(a, b):
    # a = Dtype: [[a00, 0, a02], [0, a11, 0]], Mtype:[[a00, a01, 0], [0, a11, 0]]
    # b = [b0, b1] (= [[b00, T5, b02], [b10, b11, b12]])
    if D_twist:
        T0 = mulFp4(a[1][1], b[0][2])
        T0 = guzaiFp4(T0)
        T1 = mulFp4(a[1][1], b[0][0])
        T2 = mulFp4(a[1][1], b[0][1])
    else:
        T0 = mulFp4(a[1][1], b[1][2])
        T0 = guzaiFp4(T0)
        T1 = mulFp4(a[1][1], b[1][0])
        T2 = mulFp4(a[1][1], b[1][1])
    A = [T0, T1, T2]
    if D_twist:
        B = Fp12SparseMul_forRTL(a[0], b[1])  # [T4, T6, T7]
    else:
        B = Fp12SparseMul(a[0], b[0])  # [T5, T7, T6]
    if D_twist:
        a[0][2] = addFp4(a[0][2], a[1][1])  # E02
    else:
        a[0][1] = addFp4(a[0][1], a[1][1])  # E01
    b[0] = addFp12(b[0], b[1])  # [F00, F01, F02]
    if D_twist:
        H = addFp12(A, B)  # [F10, F11, F12]
        E = Fp12SparseMul_forRTL(a[0], b[0])  # [T8, T9, T10]
        T2 = guzaiFp4(T2)
        A = [T2, T0, T1]
        F = subFp12(E, A)  # [F00, F01, F02]
    else:
        E = Fp12SparseMul(a[0], b[0])  # [T8, T10, T9]
        F = subFp12(E, A)  # [F00, F01, F02]
        T2 = guzaiFp4(T2)
        A = [T2, T0, T1]
        H = addFp12(A, B)  # [F10, F11, F12]
    F = subFp12(F, B)  # [F00, F01, F02]
    return [F, H] if D_twist else [H, F]


def expFp24_for_test(a, u):
    u_abs = abs(u)
    r = a
    for ub in bits_of(u_abs)[1:]:
        r = squareFp24(r)
        if ub == 1:
            r = mulFp24(r, a)
    if u < 0:
        r = invFp24(r)
    return r


# NOTE: Final Exponentiation Hard Partではこっちを使う
def expFp24(a):
    r = a
    res = [
        [[[MontConv(1), 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]],
    ]
    for ui in U:
        if ui == 1:
            res = mulFp24(res, r)
        if ui == -1:
            # NOTE: hard partでは冪乗する数a(=conj(f)/f)がunitaryなのでinv(a)=conj(a)
            res = mulFp24(res, conjFp24(r))
        r = SQR012345Fp24(r)
    return res


def FrobFp24(f):
    v = [[0, 0], [MontConv(1), 0]]
    xi1 = [
        [[MontConv(1), 0], [0, 0]],
        expFp4(v, (p - 1) // 6),
        expFp4(v, 2 * (p - 1) // 6),
        expFp4(v, 3 * (p - 1) // 6),
        expFp4(v, 4 * (p - 1) // 6),
        expFp4(v, 5 * (p - 1) // 6),
    ]
    f10_c = FrobFp4(f[1][0])
    f01_c = FrobFp4(f[0][1])
    f11_c = FrobFp4(f[1][1])
    f02_c = FrobFp4(f[0][2])
    f12_c = FrobFp4(f[1][2])
    new_f00 = FrobFp4(f[0][0])
    new_f10 = mulFp4(f10_c, xi1[1])
    new_f01 = mulFp4(f01_c, xi1[2])
    new_f11 = mulFp4(f11_c, xi1[3])
    new_f02 = mulFp4(f02_c, xi1[4])
    new_f12 = mulFp4(f12_c, xi1[5])
    return [[new_f00, new_f01, new_f02], [new_f10, new_f11, new_f12]]
