from operate_Fp2 import negFp2, addFp2, subFp2, mulFp2, squareFp2, guzaiFp2, expFp2, conjFp2, v2
from operate_Fp4 import addFp4, subFp4, mulFp4, guzaiFp4, invFp4, negFp4, constMulFp4, squareFp4, mulFp4
from util import printFp4
from parameters import MontConv, p, bits_list, bits_of
from constants import U, twist_type

# Fp12: [a0, a1, a2] -> a0 + a1w + a2w^2 (Fp4: a0 = [a00, a01] -> a00 + a01v)
# w^3 + v = 0, v^2 + u + 1 = 0, u^2 + 1 = 0

def addFp12(a, b):
    c0 = addFp4(a[0], b[0])
    c1 = addFp4(a[1], b[1])
    c2 = addFp4(a[2], b[2])
    return [c0, c1, c2]


def subFp12(a, b):
    c0 = subFp4(a[0], b[0])
    c1 = subFp4(a[1], b[1])
    c2 = subFp4(a[2], b[2])
    return [c0, c1, c2]


def mulFp12(a, b):
    t0 = mulFp4(a[0], b[0])
    t1 = mulFp4(a[1], b[1])
    t2 = mulFp4(a[2], b[2])
    t3 = mulFp4(addFp4(a[0], a[1]), addFp4(b[0], b[1]))
    t4 = mulFp4(addFp4(a[1], a[2]), addFp4(b[1], b[2]))
    t5 = mulFp4(addFp4(a[2], a[0]), addFp4(b[2], b[0]))
    t3 = subFp4(t3, addFp4(t0, t1))
    t4 = subFp4(t4, addFp4(t1, t2))
    t4 = guzaiFp4(t4)
    c0 = addFp4(t0, t4)
    t5 = subFp4(t5, addFp4(t2, t0))
    t2 = guzaiFp4(t2)
    c1 = addFp4(t3, t2)
    c2 = addFp4(t1, t5)
    return [c0, c1, c2]


def squareFp12(a):
    t0 = squareFp4(a[0])
    t1 = squareFp4(a[1])
    t2 = squareFp4(a[2])
    t3 = squareFp4(addFp4(a[0], a[1]))
    t4 = squareFp4(addFp4(a[1], a[2]))
    t5 = squareFp4(addFp4(a[2], a[0]))
    s0 = subFp4(t3, addFp4(t0, t1))
    s1 = subFp4(t4, addFp4(t1, t2))
    s2 = subFp4(t5, addFp4(t2, t0))
    s1 = guzaiFp4(s1)
    t2 = guzaiFp4(t2)
    c0 = addFp4(t0, s1)
    c1 = addFp4(s0, t2)
    c2 = addFp4(t1, s2)
    return [c0, c1, c2]


def constMulFp12(a, k):
    return [constMulFp4(a[0], k), constMulFp4(a[1], k), constMulFp4(a[2], k)]


def guzaiFp12(a): # w^3 = guzai = v
    return [guzaiFp4(a[2]), a[0], a[1]]


def invFp12(a):
    aa = squareFp4(a[0])
    bb = squareFp4(a[1])
    cc = squareFp4(a[2])
    ab = mulFp4(a[0], a[1])
    bc = mulFp4(a[1], a[2])
    ac = mulFp4(a[2], a[0])
    bcxi = guzaiFp4(bc)
    pa = subFp4(aa, bcxi)
    ccxi = guzaiFp4(cc)
    pb = subFp4(ccxi, ab)
    pc = subFp4(bb, ac)
    pbc = mulFp4(pb, a[2])
    pcb = mulFp4(pc, a[1])
    pbccb = addFp4(pbc, pcb)
    pxi = guzaiFp4(pbccb)
    paa = mulFp4(pa, a[0])
    q = addFp4(pxi, paa)
    q_inv = invFp4(q)
    ya = mulFp4(pa, q_inv)
    yb = mulFp4(pb, q_inv)
    yc = mulFp4(pc, q_inv)
    return [ya, yb, yc]


def negFp12(a):
    return [negFp4(a[0]), negFp4(a[1]), negFp4(a[2])]


def conjFp12(a):
    a10 = negFp2(a[1][0])
    a01 = negFp2(a[0][1])
    a21 = negFp2(a[2][1])
    return [[a[0][0], a01], [a10, a[1][1]], [a[2][0], a21]]

def SQR012345Fp12(a):
    T0 = squareFp2(a[0][0])
    T1 = addFp2(a[0][0], a[1][1])
    T2 = subFp2(T1, a[2][0])
    T1 = addFp2(T1, a[2][0])
    T1 = squareFp2(T1)
    T2 = squareFp2(T2)
    T3 = mulFp2(a[1][1], a[2][0])
    T3 = addFp2(T3, T3)
    T4 = squareFp2(a[1][1])
    T5 = mulFp2(a[0][0], a[0][1]) #B01
    T6 = mulFp2(a[2][0], a[2][1]) #B45
    T7 = mulFp2(a[1][0], a[1][1]) #B23
    c00 = guzaiFp2(T3)
    c00 = addFp2(T0, c00)
    c00 = addFp2(c00, c00)
    c00 = subFp2(c00, [MontConv(1), 0])
    c01 = addFp2(T5, T5)
    c01 = addFp2(c01, T5)
    c01 = addFp2(c01, a[0][1])
    c01 = addFp2(c01, c01)
    c10 = addFp2(T6, T6)
    c10 = addFp2(c10, T6)
    c10 = guzaiFp2(c10)
    c10 = addFp2(c10, a[1][0])
    c10 = addFp2(c10, c10)
    c11 = addFp2(T0, T4)
    c11 = addFp2(c11, c11)
    c11 = subFp2(T1, c11)
    c11 = addFp2(c11, T2)
    c20 = guzaiFp2(T4)
    c20 = subFp2(c20, T3)
    c20 = addFp2(c20, c20)
    c20 = addFp2(c20, T1)
    c20 = subFp2(c20, T2)
    c21 = addFp2(T7, T7)
    c21 = addFp2(c21, T7)
    c21 = addFp2(c21, a[2][1])
    c21 = addFp2(c21, c21)
    return [[c00, c01], [c10, c11], [c20, c21]]


def expFp12(a):
    r = a
    res = [[[MontConv(1), 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    for ui in U:
        if (ui == 1):
            res = mulFp12(res, r)
        if (ui == -1):
            # NOTE: hard partでは冪乗する数a(=conj(f)/f)がunitaryなのでinv(a)=conj(a)
            res = mulFp12(res, conjFp12(r))
        r = SQR012345Fp12(r)
    return res


def expFp12_for_test(a, k):
    r = a
    abs_k = abs(k)
    k_bit_list = bits_of(abs_k)
    for ui in k_bit_list[1:]:
        r = squareFp12(r)
        if (ui == 1):
            r = mulFp12(r, a)
    if k < 0:
        r = invFp12(r)
    return r



def FrobFp12(f):
    xi1 = [
        [MontConv(1), 0],
        expFp2(v2, (p-1)//6),
        expFp2(v2, 2*(p-1)//6),
        expFp2(v2, 3*(p-1)//6),
        expFp2(v2, 4*(p-1)//6),
        expFp2(v2, 5*(p-1)//6)
    ]
    f10_c = conjFp2(f[1][0])
    f20_c = conjFp2(f[2][0])
    f01_c = conjFp2(f[0][1])
    f11_c = conjFp2(f[1][1])
    f21_c = conjFp2(f[2][1])
    new_f00 = conjFp2(f[0][0])
    new_f10 = mulFp2(f10_c, xi1[1])
    new_f20 = mulFp2(f20_c, xi1[2])
    new_f01 = mulFp2(f01_c, xi1[3])
    new_f11 = mulFp2(f11_c, xi1[4])
    new_f21 = mulFp2(f21_c, xi1[5])
    return [[new_f00, new_f01], [new_f10, new_f11], [new_f20, new_f21]]


def sparseFp12(a, b):
    # a = Dtype: [[l00, l01], [l10, zero], [zero, zero]], Mtype:[[l01, l00], [zero, zero], [l10, zero]]
    if twist_type == "D":
        T0 = mulFp2(a[0][0], b[0][0])
        T1 = mulFp2(a[0][0], b[2][0])
        T2 = mulFp2(a[0][0], b[1][1])  # A = [T0, T1, T2]
        B = Fq6SparseMul(a[1][0], a[0][1], b[1][0], b[0][1], b[2][1])
        T3 = addFp2(a[0][0], a[1][0])
    else:
        T1 = mulFp2(a[0][1], b[1][0])
        T2 = mulFp2(a[0][1], b[0][1])
        T0 = mulFp2(a[0][1], b[2][1])
        T0 = guzaiFp2(T0)   # A = [T0, T1, T2]
        B = Fq6SparseMul(a[0][0], a[2][0], b[0][0], b[2][0], b[1][1])
        T3 = addFp2(a[2][0], a[0][1])
    T4 = addFp2(b[0][0], b[1][0])
    T5 = addFp2(b[2][0], b[0][1])
    T6 = addFp2(b[1][1], b[2][1])
    if twist_type == "D":
        E = Fq6SparseMul(T3, a[0][1], T4, T5, T6)
    else:
        E = Fq6SparseMul(a[0][0], T3, T4, T5, T6)
    T7 = addFp2(T0, B[0])
    T8 = addFp2(T1, B[1])
    T9 = addFp2(T2, B[2])
    T7 = subFp2(E[0], T7)
    T8 = subFp2(E[1], T8)
    T9 = subFp2(E[2], T9)
    if twist_type == "D":
        B[2] = guzaiFp2(B[2])
        T0 = addFp2(T0, B[2])
        T1 = addFp2(T1, B[0])
        T2 = addFp2(T2, B[1])
        return [[T0, T8], [T7, T2], [T1, T9]]
    else:
        T2 = guzaiFp2(T2)
        T2 = addFp2(T2, B[0])
        T0 = addFp2(T0, B[1])
        T1 = addFp2(T1, B[2])
        return [[T2, T8], [T7, T1], [T0, T9]]


def Fq6SparseMul(a0, a1, b0, b1, b2):
    t0 = mulFp2(a0, b0)
    t1 = mulFp2(a1, b1)
    t2 = mulFp2(a1, b2)
    t2 = guzaiFp2(t2)
    t3 = addFp2(t0, t2)
    t4 = addFp2(a0, a1)
    t5 = addFp2(b0, b1)
    t6 = mulFp2(t4, t5)
    t7 = addFp2(t0, t1)
    t7 = subFp2(t6, t7)
    t8 = mulFp2(a0, b2)
    t9 = addFp2(t8, t1)   
    return [t3, t7, t9]

def Fp12SparseMul(a, b): # P317で違う
    # a = [a0, a1, 0], b = [b0, b1, b2]

    # MEMO: RTLのメモリ割り当て: E = Fp12SparseMul([T3, a[1][1], 0], b[1])の計算内では T3->T3, T4->T4, T5->T8, T6->T9, T7->T10
    T3 = mulFp4(a[0], b[0])
    T4 = mulFp4(a[1], b[1])
    T5 = mulFp4(a[1], b[2])
    T5 = guzaiFp4(T5)
    T5 = addFp4(T3, T5)
    T6 = addFp4(a[0], a[1])
    T7 = addFp4(b[0], b[1])
    T6 = mulFp4(T6, T7)
    T7 = subFp4(T6, T3)
    T7 = subFp4(T7, T4)
    T6 = mulFp4(a[0], b[2])
    T6 = addFp4(T4, T6)
    return  [T5, T7, T6]


def Fp12SparseMul_forRTL(a, b):
    # a = [a0, 0, a2], b = [b0, b1, b2]

    # MEMO: RTLのメモリ割り当て: E = Fp12SparseMul([T3, a[1][1], 0], b[1])の計算内では T3->T3, T4->T8, T5->T5, T6->T9, T7->T10
    T3 = mulFp4(a[0], b[0])
    T4 = mulFp4(a[2], b[1])
    T4 = guzaiFp4(T4)
    T4 = addFp4(T3, T4)
    T5 = mulFp4(a[2], b[2])
    T6 = addFp4(a[0], a[2])
    T7 = addFp4(b[0], b[2])
    T6 = mulFp4(T6, T7)
    T7 = subFp4(T6, T5)
    T7 = subFp4(T7, T3)
    T6 = mulFp4(a[0], b[1])
    T5 = guzaiFp4(T5)
    T6 = addFp4(T5, T6)
    return  [T4, T6, T7]