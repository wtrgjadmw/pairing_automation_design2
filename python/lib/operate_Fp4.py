from lib.operate_Fp2 import (
    mulFp2,
    reductionFp2,
    addFp2,
    expFp2,
    subFp2,
    mulFp2_unr,
    constMulFp2,
    guzaiFp2,
    addDPFp2,
    subDPFp2,
    squareFp2,
    conjFp2,
    negFp2,
    invFp2,
    v2,
)
from lib.operate_Fp import mul, add, sub, invFp
from lib.parameters import *
from util import *

"""
E/Fp^4: y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]

Fp4: [a0, a1] -> a0 + a1v (Fp2: a0 = [a00, a01] -> a00 + a01u)
"""


def get_k():
    k = expFp2(v2, (p - 1) // 2)
    return k


k = get_k()


def reductionFp4(x):
    c0 = reductionFp2(x[0])
    c1 = reductionFp2(x[1])
    return [c0, c1]


def addFp4(a, b):
    c0 = addFp2(a[0], b[0])
    c1 = addFp2(a[1], b[1])
    return [c0, c1]


def subFp4(a, b):
    c0 = subFp2(a[0], b[0])
    c1 = subFp2(a[1], b[1])
    return [c0, c1]


def mulFp4(a, b):
    t0 = mulFp2(a[0], b[0])
    t1 = mulFp2(a[1], b[1])
    t2 = addFp2(a[0], a[1])
    t3 = addFp2(b[0], b[1])
    t4 = mulFp2(t2, t3)
    s0 = guzaiFp2(t1)
    c0 = addFp2(t0, s0)
    t5 = addFp2(t0, t1)
    c1 = subFp2(t4, t5)
    return [c0, c1]


def mulFp4_unr(a, b):
    T0 = mulFp2_unr(a[0], b[0])
    T1 = mulFp2_unr(a[1], b[1])
    t0 = addFp2(a[0], a[1])
    t1 = addFp2(b[0], b[1])
    T2 = mulFp2_unr(t0, t1)
    T3 = guzaiFp2(T1)
    C0 = addDPFp2(T0, T3)
    T4 = addDPFp2(T0, T1)
    C1 = subDPFp2(T2, T4)
    return [C0, C1]


def mulFp4_lazyr(a, b):
    C = mulFp4_unr(a, b)
    return reductionFp4(C)


def squareFp4(a):
    t0 = addFp2(a[0], guzaiFp2(a[1]))
    t1 = addFp2(a[0], a[1])
    t2 = mulFp2(t0, t1)
    t3 = mulFp2(a[0], a[1])
    t4 = guzaiFp2(t3)
    t5 = addFp2(t3, t4)
    c0 = subFp2(t2, t5)
    c1 = addFp2(t3, t3)
    return [c0, c1]


def squareFp4_unr(a):
    t0 = guzaiFp2(a[1])
    t1 = addFp2(a[0], t0)
    t2 = addFp2(a[0], a[1])
    T0 = mulFp2_unr(t1, t2)
    T1 = mulFp2_unr(a[0], a[1])
    T2 = guzaiFp2(T1)
    T3 = addDPFp2(T1, T2)
    C0 = subDPFp2(T0, T3)
    C1 = addDPFp2(T1, T1)
    return [C0, C1]


def squareFp4_lazyr(a):
    B = squareFp4_unr(a)
    return reductionFp4(B)


def constMulFp4(a, k):
    return [constMulFp2(a[0], k), constMulFp2(a[1], k)]


def negFp4(a):
    return [negFp2(a[0]), negFp2(a[1])]


def conjFp4(a):
    return [a[0], negFp2(a[1])]


def guzaiFp4(a):  # v^2 = guzai = u
    return [guzaiFp2(a[1]), a[0]]


def invFp4(a):
    aa = squareFp2(a[0])
    bb = squareFp2(a[1])
    bbxi = guzaiFp2(bb)
    denom = subFp2(aa, bbxi)
    denom_inv = invFp2(denom)
    c0 = mulFp2(a[0], denom_inv)
    c1 = mulFp2(a[1], denom_inv)
    return [c0, negFp2(c1)]


def invFp4_forRTL(a):  # for BLS24-509
    # aa = squareFp2(a[0])
    t0 = sub(a[0][0], a[0][1])
    t1_a0 = add(a[0][0], a[0][1])
    c0 = mul(t0, t1_a0)
    t3 = mul(a[0][0], a[0][1])
    c1 = add(t3, t3)
    # bb = squareFp2(a[1])
    t0 = sub(a[1][0], a[1][1])
    t1_a1 = add(a[1][0], a[1][1])
    c2 = mul(t0, t1_a1)
    t3 = mul(a[1][0], a[1][1])
    c3 = add(t3, t3)
    # bbxi = guzaiFp2(bb)
    c4 = sub(c2, c3)
    c5 = add(c2, c3)
    # denom = subFp2(aa, bbxi)
    c0 = sub(c0, c4)
    c1 = sub(c1, c5)
    # denom_inv = invFp2(denom)
    cc0 = mul(c0, c0)
    cc1 = mul(c1, c1)
    cc = add(cc0, cc1)
    cc = invFp(cc)
    c0 = mul(c0, cc)
    c1 = mul(c1, cc)
    # c0 = mulFp2(a[0], denom_inv)
    t0 = mul(a[0][0], c0)
    t1 = mul(a[0][1], c1)
    t3 = sub(c0, c1)
    t4 = mul(t1_a0, t3)
    c2 = add(t0, t1)
    c3 = sub(t4, t0)
    c3 = add(c3, t1)
    # c1 = mulFp2(a[1], denom_inv)
    t0 = mul(a[1][0], c0)
    t1 = mul(a[1][1], c1)
    t4 = mul(t1_a1, t3)
    c4 = add(t0, t1)
    c4 = sub(0, c4)
    c5 = add(t4, t1)
    c5 = sub(t0, c5)
    return [[c2, c3], [c4, c5]]


def expFp4(f, u_):
    r = f
    for ub in bits_of(u_)[1:]:
        r = mulFp4(r, r)
        if ub == 1:
            r = mulFp4(r, f)
    # TODO: この場合分けの意味調べる
    if u_ < 0:
        r = conjFp4(r)
    return r


def FrobFp4(a):
    c0 = conjFp2(a[0])
    c1 = mulFp2(conjFp2(a[1]), k)
    return [c0, c1]


if __name__ == "__main__":
    printFp2(k)
