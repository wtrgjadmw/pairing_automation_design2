from lib.parameters import *
from lib.operate_Fp import (
    mul,
    add,
    sub,
    invFp,
    reduction,
    addDP,
    subDP,
    constMul,
    constMulDP,
    qnr1,
    srtFp,
    negFp,
)
from lib.util import printFp

# モンゴメリ変換されたデータを扱う
# Fp2: [a0, a1] -> a0 + a1u (u^2 = -1)


def reductionFp2(x):
    c0 = reduction(x[0])
    c1 = reduction(x[1])
    return [c0, c1]


def addFp2(a, b):
    new_r = add(a[0], b[0])
    new_i = add(a[1], b[1])
    return [new_r, new_i]


def addDPFp2(a, b):
    new_r = addDP(a[0], b[0])
    new_i = addDP(a[1], b[1])
    return [new_r, new_i]


def subFp2(a, b):
    new_r = sub(a[0], b[0])
    new_i = sub(a[1], b[1])
    return [new_r, new_i]


def subDPFp2(a, b):
    new_r = subDP(a[0], b[0])
    new_i = subDP(a[1], b[1])
    return [new_r, new_i]


def mulFp2(a, b):
    t0 = mul(a[0], b[0])
    t1 = mul(a[1], b[1])
    t2 = add(a[0], a[1])
    t3 = add(b[0], b[1])
    t4 = mul(t2, t3)
    t5 = constMul(t1, abs(qnr1))
    if qnr1 > 0:
        c0 = add(t0, t5)
    else:
        c0 = sub(t0, t5)
    t6 = add(t0, t1)
    c1 = sub(t4, t6)
    return [c0, c1]


# reduction 無し, 大文字は倍精度
def mulFp2_unr(a, b):
    T0 = a[0] * b[0]
    T1 = a[1] * b[1]
    T2 = addDP(T0, T1)
    t0 = add(a[0], a[1])
    t1 = add(b[0], b[1])
    T3 = t0 * t1
    T4 = constMulDP(T1, abs(qnr1))
    if qnr1 > 0:
        C0 = addDP(T0, T4)
    else:
        C0 = subDP(T0, T4)
    C1 = subDP(T3, T2)
    return [C0, C1]


def squareFp2(a):
    t0 = (a[0] + (qnr1 * a[1]) % p) % p
    t1 = add(a[0], a[1])
    t2 = mul(t0, t1)
    t3 = mul(a[0], a[1])
    t4 = (qnr1 * t3) % p
    t5 = add(t3, t4)
    c0 = sub(t2, t5)
    c1 = add(t3, t3)
    return [c0, c1]


# kはモンゴメリ変換されている
def constMulFp2(a, k):
    new_r = mul(a[0], k)
    new_i = mul(a[1], k)
    return [new_r, new_i]


# https://github.com/relic-toolkit/relic/blob/83de89f714202f9b227a2138e4fe784ee6e202f5/src/fpx/relic_fp2_mul.c
def guzaiFp2(a):  # u^2 = guzai
    if p_mod8 == 3:  # guzai = i+1
        new_r = sub(a[0], a[1])
        new_i = add(a[0], a[1])
    elif p_mod8 == 1 or p_mod8 == 5:  # guzai = i
        new_r = (qnr1 * a[1]) % p
        new_i = a[0]
    elif p_mod8 == 7:  # guzai = 2^k + i
        b = a
        b[0] = (qnr1 * a[1]) % p
        b[1] = a[0]
        qnr2_ = qnr2
        c = a
        while qnr2_ > 1:
            c = addFp2(c, c)
            qnr2_ >>= 1
        return addFp2(b, c)
    else:
        raise Exception("characteristic number p is not prime")

    return [new_r, new_i]


def conjFp2(a):
    new_r = a[0]
    new_i = p - a[1]
    return [new_r, new_i]


def expFp2(f, u):
    r = f
    for ub in bits_of(u)[1:]:
        r = mulFp2(r, r)
        if ub == 1:
            r = mulFp2(r, f)
    if u < 0:
        r = invFp2(r)
    return r


def invFp2(a):  # Itoh-Tsujii Inversion
    a_ = conjFp2(a)
    t = mulFp2(a, a_)
    s = invFp(t[0])
    ainv = constMulFp2(a_, s)
    return ainv


def negFp2(a):
    return [negFp(a[0]), negFp(a[1])]


def srtFp2(a):
    if a == [0, 0]:
        return [0, 0], True
    if a[1] == 0:
        c0, is_qr = srtFp(a[0])
        if is_qr:
            return [c0, 0], True
        qnr_inv = invFp(MontConv(-qnr1))
        a[0] = mul(a[0], qnr_inv)
        c1, is_qr = srtFp(a[0])
        if not is_qr:
            # raise Exception("a is qnr1")
            return [0, 0], False
        return [0, negFp(c1)], True
    t0 = mul(a[0], a[0])
    t1 = mul(a[1], a[1])
    for i in range(-1, qnr1, -1):
        t0 = add(t0, t1)
    t0 = add(t0, t1)
    t0_srt, is_qr = srtFp(t0)
    if is_qr:
        t0 = add(a[0], t0_srt)
        inv_2 = invFp(MontConv(2))
        t0 = mul(t0, inv_2)
        c0, is_qr = srtFp(t0)
        if not is_qr:
            # raise Exception("a is qnr1")
            return [0, 0], False
        c1 = add(c0, c0)
        c1 = invFp(c1)
        c1 = mul(a[1], c1)
        return [c0, c1], True
    return [0, 0], False


def get_qnr2():
    if p_mod8 == 1 or p_mod8 == 3 or p_mod8 == 5:
        return 0
    elif p_mod8 == 7:
        qnr2 = 0
        t0 = [0, MontConv(1)]
        t1, is_qr = srtFp2(t0)
        if is_qr:
            qnr2 = 2
            t0[0] = qnr2
            t1, is_qr = srtFp2(t0)
            while is_qr:
                qnr2 *= 2
                t0[0] = qnr2
                t1, is_qr = srtFp2(t0)
        return qnr2
    else:
        Exception("characteristic number p is not prime")


qnr2 = get_qnr2()


def get_v2():
    if p_mod8 == 3:  # guzai = i+1
        v2 = [MontConv(1), MontConv(1)]
    elif p_mod8 == 1 or p_mod8 == 5:  # guzai = i
        v2 = [0, MontConv(1)]
    elif p_mod8 == 7:
        v2 = [MontConv(qnr2), MontConv(1)]
    else:
        raise Exception("characteristic number p is not prime")
    return v2


v2 = get_v2()
