from operate_Fp import mul
from operate_Fp4 import mulFp4, subFp4, addFp4, constMulFp4, squareFp4, guzaiFp4
from parameters import MontConv, B4, p, bits_of, twist_type
from util import printFp4, printFp

# The Realm of the Pairing p15 参照
# T, Q: 射影座標変換済み
def ep4_add(T, Q):
    xt = T[0]
    yt = T[1]
    zt = T[2]
    xq = Q[0]
    yq = Q[1]
    A = mulFp4(yq, zt)
    B = mulFp4(xq, zt)
    si = subFp4(yt, A)
    la = subFp4(xt, B)
    C = squareFp4(si)
    D = squareFp4(la)
    E = mulFp4(D, la)
    F = mulFp4(zt, C)
    G = mulFp4(xt, D)
    t0 = addFp4(E, F)
    t1 = constMulFp4(G, MontConv(2))
    H = subFp4(t0, t1)
    new_xt = mulFp4(la, H)
    I = mulFp4(yt, E)
    t2 = subFp4(G, H)
    t3 = mulFp4(si, t2)
    new_yt = subFp4(t3, I)
    new_zt = mulFp4(zt, E)
    return [new_xt, new_yt, new_zt]


# NOTE: 点の公式は4倍
def ep4_dbl(T):
    xt = T[0]
    yt = T[1]
    zt = T[2]
    A = squareFp4(yt)
    t0 = squareFp4(zt)
    t1 = constMulFp4(t0, MontConv(3))
    B = mulFp4(t1, B4)
    t2 = mulFp4(xt, yt)
    C = constMulFp4(t2, MontConv(2))
    t4 = constMulFp4(B, MontConv(3))
    t5 = subFp4(A, t4)
    new_xt = mulFp4(t5, C)
    t6 = squareFp4(A)
    t7 = mulFp4(A, B)
    t8 = constMulFp4(t7, MontConv(6))
    t9 = squareFp4(B)
    t10 = constMulFp4(t9, MontConv(3))
    t11 = addFp4(t6, t8)
    new_yt = subFp4(t11, t10)
    t12 = mulFp4(yt, zt)
    E = constMulFp4(t12, MontConv(2))
    t13 = mulFp4(A, E)
    new_zt = constMulFp4(t13, MontConv(4))
    return [new_xt, new_yt, new_zt]


def ep4_mul(n, T_):
    res = T_
    for nb in bits_of(n)[1:]:
        res = ep4_dbl(res)
        if(nb == 1):
            res = ep4_add(res, T_)
    return res

# TODO: アルゴリズム確認
def ep4_add_relic(T, P, Q):
    xt = T[0]
    yt = T[1]
    zt = T[2]
    xp = P[0]
    yp = P[1]
    xq = Q[0]
    yq = Q[1]
    t0 = mulFp4(zt, xq)
    t0 = subFp4(xt, t0)
    t1 = mulFp4(zt, yq)
    t1 = subFp4(yt, t1)
    xp00_ = (-xp[0][0])%p
    
    l10 = [[mul(t1[0][0], xp00_), mul(t1[0][1], xp00_)], [mul(t1[1][0], xp00_), mul(t1[1][1], xp00_)]]
    t2 = squareFp4(t0)
    new_xt = mulFp4(xt, t2)
    t2 = mulFp4(t2, t0)
    t3 = squareFp4(t1)
    t3 = mulFp4(t3, zt)
    t3 = addFp4(t2, t3)
    t3 = subFp4(t3, new_xt)
    t3 = subFp4(t3, new_xt)
    new_xt = subFp4(new_xt, t3)
    t4 = mulFp4(xq, t1)
    t1 = mulFp4(t1, new_xt)
    new_yt = mulFp4(t2, yt)
    new_yt = subFp4(t1, new_yt)
    new_xt = mulFp4(t0, t3)
    new_zt = mulFp4(zt, t2)
    t2 = mulFp4(yq, t0)
    l11 = subFp4(t4, t2)
    
    l00 = [[mul(t0[0][0], yp[0][0]), mul(t0[0][1], yp[0][0])], [mul(t0[1][0], yp[0][0]), mul(t0[1][1], yp[0][0])]]
    zero = [[0, 0], [0, 0]]
    if twist_type == "D":
        l11 = guzaiFp4(l11)
        e = [[l11, zero, l10], [zero, l00, zero]]
    else:
        e = [[l11, l10, zero], [zero, l00, zero]]
    return [new_xt, new_yt, new_zt], e


def ep4_dbl_relic(T, P):
    xt = T[0]
    yt = T[1]
    zt = T[2]
    xp = P[0]
    yp = P[1]
    t0 = squareFp4(xt)
    t1 = squareFp4(yt)
    t2 = squareFp4(zt)
    t3 = addFp4(t2, t2)
    t3 = addFp4(t3, t2)
    t3 = mulFp4(t3, B4)
    t4 = addFp4(xt, yt)
    t4 = squareFp4(t4)
    t4 = subFp4(t4, t0)
    t4 = subFp4(t4, t1)
    t5 = addFp4(yt, zt)
    t5 = squareFp4(t5)
    t5 = subFp4(t5, t1)
    t5 = subFp4(t5, t2)
    t6 = addFp4(t3, t3)
    t6 = addFp4(t6, t3)
    new_xt = subFp4(t1, t6)
    new_xt = mulFp4(new_xt, t4)
    t6 = addFp4(t6, t1)
    t6 = squareFp4(t6)
    t2 = squareFp4(t3)
    new_yt = addFp4(t2, t2)
    t2 = addFp4(new_yt, new_yt)
    new_yt = addFp4(t2, t2)
    new_yt = addFp4(new_yt, t2)
    new_yt = subFp4(t6, new_yt)
    new_zt = addFp4(t1, t1)
    new_zt = addFp4(new_zt, new_zt)
    new_zt = mulFp4(new_zt, t5)
    l11 = subFp4(t3, t1)
    l10 = [[mul(t0[0][0], xp[0][0]), mul(t0[0][1], xp[0][0])], [mul(t0[1][0], xp[0][0]), mul(t0[1][1], xp[0][0])]]
    l00 = [[mul(t5[0][0], yp[0][0]), mul(t5[0][1], yp[0][0])], [mul(t5[1][0], yp[0][0]), mul(t5[1][1], yp[0][0])]]
    zero = [[0, 0], [0, 0]]
    if twist_type == "D":
        l11 = guzaiFp4(l11)
        e = [[l11, zero, l10], [zero, l00, zero]]
    else:
        e = [[l11, l10, zero], [zero, l00, zero]]
    return [new_xt, new_yt, new_zt], e
