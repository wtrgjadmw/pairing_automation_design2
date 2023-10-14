from lib.operate_Fp import add, sub, mul, invFp
from lib.parameters import MontConv, bits_of, p, A


def ep_add(T, Q):
    xt = T[0]
    yt = T[1]
    xq = Q[0]
    yq = Q[1]
    dy = sub(yt, yq)
    dx = sub(xt, xq)
    dx_inv = invFp(dx)
    la = mul(dy, dx_inv)
    xtxq = add(xt, xq)
    la2 = mul(la, la)
    new_xt = sub(la2, xtxq)
    xtnewxt = sub(xt, new_xt)
    laxtnewxt = mul(la, xtnewxt)
    new_yt = sub(laxtnewxt, yt)
    return [new_xt, new_yt]


def ep_dbl(T):
    xt = T[0]
    yt = T[1]
    t0 = (3 * mul(xt, xt)) % p
    t1 = add(t0, A)
    t2 = (2 * yt) % p
    t2_inv = invFp(t2)
    la = mul(t1, t2_inv)
    t3 = (2 * xt) % p
    t4 = mul(la, la)
    new_xt = sub(t4, t3)
    xtnewxt = sub(xt, new_xt)
    laxtnewxt = mul(la, xtnewxt)
    new_yt = sub(laxtnewxt, yt)
    return [new_xt, new_yt]


def ep_mul(n, T_):
    res = T_
    for nb in bits_of(n)[1:]:
        res = ep_dbl(res)
        if nb == 1:
            res = ep_add(res, T_)
    return res
