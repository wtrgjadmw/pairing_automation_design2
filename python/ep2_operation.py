from operate_Fp import mul, negFp
from operate_Fp2 import mulFp2, subFp2, addFp2, constMulFp2, squareFp2, guzaiFp2, negFp2
from parameters import *
from util import printFp2, printFp


# TODO: アルゴリズム確認
def ep2_add(T, P, Q):
    xt = T[0]
    yt = T[1]
    zt = T[2]
    xp = P[0]
    yp = P[1]
    xq = Q[0]
    yq = Q[1]
    a = mulFp2(yq, zt)
    a = subFp2(yt, a)
    b = mulFp2(xq, zt)
    b = subFp2(xt, b)
    c = squareFp2(a)
    d = squareFp2(b)
    e = mulFp2(b, d)
    f = mulFp2(zt, c)
    f = addFp2(e, f)
    d = mulFp2(xt, d)
    d_ = addFp2(d, d)
    f = subFp2(f, d_)
    g = subFp2(f, d)
    new_xt = mulFp2(b, f)
    g = mulFp2(a, g)
    h = mulFp2(yt, e)
    new_yt = addFp2(g, h)
    new_yt = negFp2(new_yt)
    new_zt = mulFp2(zt, e)
    l00 = [mul(b[0], negFp(yp[0])), mul(b[1], negFp(yp[0]))]
    l10 = [mul(a[0], xp[0]), mul(a[1], xp[0])]
    l01 = mulFp2(yq, b)
    a = mulFp2(xq, a)
    l01 = subFp2(l01, a)
    zero = [0, 0]
    if twist_type == "D":
        l = [[l00, l01], [l10, zero], [zero, zero]] 
    else:
        l = [[l01, l00], [zero, zero], [l10, zero]]
    return [new_xt, new_yt, new_zt], l


def ep2_dbl(T, P):
    xt = T[0]
    yt = T[1]
    zt = T[2]
    xp = P[0]
    yp = P[1]
    a = squareFp2(yt)
    b = squareFp2(zt)
    b = mulFp2(B2, b)
    b_ = addFp2(b, b)
    b = addFp2(b_, b)
    c = mulFp2(xt, yt)
    c = addFp2(c, c)
    d = squareFp2(xt)
    d_ = addFp2(d, d)
    d = addFp2(d_, d)
    e = mulFp2(yt, zt)
    e = addFp2(e, e)
    new_zt = mulFp2(a, e)
    new_zt = addFp2(new_zt, new_zt)
    new_zt = addFp2(new_zt, new_zt)
    l01 = subFp2(a, b)
    b2 = addFp2(b, b)
    new_xt = subFp2(l01, b2)
    new_xt = mulFp2(new_xt, c)
    new_yt = addFp2(a, l01)
    b3 = addFp2(b2, b)
    new_yt = mulFp2(b3, new_yt)
    a = squareFp2(a)
    new_yt = addFp2(new_yt, a)
    l00 = [mul(e[0], yp[0]), mul(e[1], yp[0])]
    l10 = [mul(d[0], negFp(xp[0])), mul(d[1], negFp(xp[0]))]
    zero = [0, 0]
    if twist_type == "D":
        l = [[l00, l01], [l10, zero], [zero, zero]] 
    else:
        l = [[l01, l00], [zero, zero], [l10, zero]]
    return [new_xt, new_yt, new_zt], l

def ep2_mul(n, T_):
    res = T_
    for nb in bits_of(n)[1:]:
        res, e = ep2_dbl(res, P)
        if(nb == 1):
            res, e = ep2_add(res, P, T_)
    return res