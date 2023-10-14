import random
from lib.parameters import *

"""
E/Fp: y^2 = x^3 + Ax + B
"""


def MontConvInv(a):
    c = (a * montgomery_inv) % p
    return c


def MontConv(a):
    t = (a * L) % p
    return t


def add(x, y):
    t0 = x + y
    t1 = x + y - p
    # NOTE: ハードウェアではMSBによって正負を判断する
    if t1 >= 0:
        out = t1
    else:
        out = t0
    return out


# 倍精度
def addDP(x, y):
    t0 = x + y
    t1 = x + y - (p << p_len)
    # NOTE: ハードウェアではMSBによって正負を判断する
    if t1 >= 0:
        out = t1
    else:
        out = t0
    return out


def sub(x, y):
    t0 = x - y
    t1 = x - y + p
    # NOTE: ハードウェアではMSBによって正負を判断する
    if t0 >= 0:
        out = t0
    else:
        out = t1
    return out


# 倍精度
def subDP(x, y):
    t0 = x - y
    t1 = x - y + (p << p_len)
    # NOTE: ハードウェアではMSBによって正負を判断する
    if t0 >= 0:
        out = t0
    else:
        out = t1
    return out


def constMul(x, k):
    bits_k = bits_of(k)
    r0 = x
    r1 = add(x, x)
    for i in range(1, len(bits_k)):
        if bits_k[i]:
            r0_tmp = add(r0, r1)
            r1_tmp = add(r1, r1)
        else:
            r0_tmp = add(r0, r0)
            r1_tmp = add(r0, r1)
        r0 = r0_tmp
        r1 = r1_tmp
    return r0


def constMulDP(x, k):
    bits_k = bits_of(k)
    r0 = x
    r1 = addDP(x, x)
    for i in range(1, len(bits_k)):
        if bits_k[i]:
            r0_tmp = addDP(r0, r1)
            r1_tmp = addDP(r1, r1)
        else:
            r0_tmp = addDP(r0, r0)
            r1_tmp = addDP(r0, r1)
        r0 = r0_tmp
        r1 = r1_tmp
    return r0


def mul(x, y):
    return (x * y % p) * montgomery_inv % p


def reduction(x):
    t = (x * p_inv) & (L - 1)  # t = (x * p_inv) mod L
    tp = t * p
    z = addDP(tp, x) >> p_len
    return z


def invFp(a):
    b = pow(a, p - 2, p)
    # montgomery変換の補正 1/(c*L) * L**2 = (1/c)*L
    b = (b * L % p) * L % p
    return b


def negFp(a):
    return p - a


def Div2(a, p_):
    if a % 2 == 0:
        return (a >> 1) % p_
    else:
        return ((a + p_) >> 1) % p_


def Div4(a, p_):
    if a % 4 == 0:
        return (a >> 2) % p_
    elif a % 4 == 2:
        return ((a + 2 * p_) >> 2) % p_
    elif (a + p_) % 4 == 2:
        return ((a + 3 * p_) >> 2) % p_
    else:
        return ((a + p_) >> 2) % p_


# this method is based on "Ultra High-Speed SM2 ASIC Implementation", 2014.
def invFp_forRTL(a, p_):
    v = p_
    p_len_ = len(str(bin(p_))) - 2
    u = a
    x1 = (2 ** (2 * p_len_)) % p_

    x2 = 0
    while v > 0:
        c = u % 4
        d = v % 4
        if c == 0:
            u = u >> 2
            x1 = Div4(x1, p_)
        elif d == 0:
            v = v >> 2
            x2 = Div4(x2, p_)
        elif c == d:
            if u > v:
                u = (u - v) >> 2
                x1 = Div4(x1 - x2, p_)
            else:
                v = (v - u) >> 2
                x2 = Div4(x2 - x1, p_)
        elif c == 2:
            if (u >> 1) > v:
                u = ((u >> 1) - v) >> 1
                x1 = (Div4(x1, p_) - Div2(x2, p_)) % p_
            else:
                v = (v - (u >> 1)) >> 1
                u = u >> 1
                x1 = Div2(x1, p_)
                x2 = Div2(x2 - x1, p_)
        elif d == 2:
            if u > (v >> 1):
                u = (u - (v >> 1)) >> 1
                v = v >> 1
                x2 = Div2(x2, p_)
                x1 = Div2(x1 - x2, p_)
            else:
                v = ((v >> 1) - u) >> 1
                x2 = (Div4(x2, p_) - Div2(x1, p_)) % p_
        else:
            if u > v:
                u = (u - v) >> 1
                x1 = Div2(x1 - x2, p_)
            else:
                v = (v - u) >> 1
                x2 = Div2(x2 - x1, p_)
    return x1


def expFp(a, x):
    r = a
    res = MontConv(1)
    while x > 0:
        if x & 1:
            res = mul(res, r)
        x >>= 1
        r = mul(r, r)
    return res


def expFp_(a, x):
    r = a
    res = 1
    while x > 0:
        if x & 1:
            res = (res * r) % p
        x >>= 1
        r = (r * r) % p
    return res


def is_qr(a):  # quadratic residue
    p_ = (p - 1) >> 1
    x = expFp(a, p_)
    return x == MontConv(1)


def get_qnr1():
    if p_mod8 == 3:
        return -1
    elif p_mod8 == 1 or p_mod8 == 5 or p_mod8 == 7:
        qnr1 = -2
        while is_qr(p + qnr1):
            qnr1 -= 1
        return qnr1
    else:
        raise Exception("error: p is not valid")


def srtFp(a):  # square root
    if not is_qr(a):
        # raise Exception("a is qnr1")
        return 0, False
    if p_mod8 == 3:
        p_ = (p + 1) >> 2
        c = expFp(a, p_)
        return c, True
    elif p_mod8 == 1 or p_mod8 == 5 or p_mod8 == 7:
        a = MontConvInv(a)
        z = random.randint(0, p - 1)
        while is_qr(z):
            z = random.randint(0, p - 1)
        q = p - 1
        s = 0
        while q % 2 == 0:
            q >>= 1
            s += 1
        m = s
        c = expFp_(z, q)
        t = expFp_(a, q)
        r = expFp_(a, (q + 1) >> 1)

        while t != 1:
            pow_t = (t * t) % p
            for j in range(1, m):
                if pow_t == 1:
                    m_update = j
                    break
                pow_t = (pow_t * pow_t) % p
            for i in range(m - m_update - 1):
                c = (c * c) % p
            b = c
            m = m_update
            c = (b * b) % p
            t = (t * c) % p
            r = (r * b) % p
        return MontConv(r), True


qnr1 = get_qnr1()

if __name__ == "__main__":
    qnr_ = get_qnr1()
    print(qnr_)
