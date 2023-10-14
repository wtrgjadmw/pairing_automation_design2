import random, time

from parameters import MontConv, MontConvInv, bits_list
from parameters import P, Q, T, A4, B4, A, B
from parameters import p, r, u, U

from operate_Fp import invFp_forRTL, srtFp, expFp, Div2, Div4, add, sub
from operate_Fp2 import mul, invFp, mulFp2, invFp2, squareFp2, srtFp2
from operate_Fp4 import mulFp4, invFp4, invFp4_forRTL, squareFp4, addFp4, negFp4, srtFp4
from operate_Fp12 import mulFp12, invFp12, Fp12SparseMul
from operate_Fp24 import conjFp24, mulFp24, mulFp24_conj_forRTL, invFp24, invFp24_forRTL, FrobFp24, sparseFp24, expFp24_for_test, squareFp24, SQR012345Fp24, expFp24

from ep4_operation import ep4_add, ep4_dbl, ep4_mul
from ep_operation import ep_mul
from optimal_ate_k24 import pp_fe_k24, pp_oatep_k24, pp_ml_k24

from util import *

def check_mongomery_inv():
    a = random.randint(0, p-1)
    am = MontConv(a)
    b = random.randint(0, p-1)
    bm = MontConv(b)
    c = (a * b) % p
    mont_ab = mul(am, bm)
    mont_c = MontConv(c)
    if (mont_ab == mont_c):
        print("mongomery_inv ok")


def check_inv_mul_Fp():
    a = random.randint(0, p-1)
    ainv = invFp(a)
    one = mul(a, ainv)
    if(MontConvInv(one) == 1):
        print("inv Fp correct")


def check_inv_forRTL():
    p_ = 7
    a = random.randint(1, p_-1)
    ainv = invFp_forRTL(a, p_)
    print(ainv)
    one = (a * ainv) % p_
    print(one)


def check_inv_mul_Fp_forRTL():
    a = random.randint(1, p-1)
    ainv = invFp_forRTL(a, p)
    ainv_ = invFp(a)
    one = (a * ainv) % p
    # one = mul(a, ainv)
    if(one == 1):
        print("inv Fp correct")
    else:
        print(one)
        print("inv Fp incorrect")
    # print("montgomery inversion: ", end="")
    # printFp(ainv_)
    # one = mul(a, ainv_)
    # if(MontConvInv(one) == 1):
    #     print("inv Fp correct")
    # else:
    #     print("inv Fp incorrect")


def check_inv_mul_Fp2():
    a = [random.randint(0, p-1), random.randint(0, p-1)]
    ainv = invFp2(a)
    one = mulFp2(a, ainv)
    if([MontConvInv(one[0]), MontConvInv(one[1])] == [1, 0]):
        print("inv Fp2 correct")


def check_square_Fp2():
    a = [random.randint(0, p-1), random.randint(0, p-1)]
    a1 = mulFp2(a, a)
    a2 = squareFp2(a)
    if(a1 == a2):
        print("square Fp2 correct")


def check_div():
    print(Div4(3, 5))


def check_srt_Fp():
    is_square = False
    while not is_square:
        x = random.randint(0, p-1)
        a = mul(x, mul(x, x))
        a = add(a, MontConv(5))
        c, is_square = srtFp(a)
        if is_square:
            cc = mul(c, c)
            if cc == a:
                printFp(MontConvInv(x))
                printFp(MontConvInv(c))
                print("srt Fp correct")
        else:
            print("this value is qnr1")


def check_srt_Fp2():
    is_square = False
    while not is_square:
        a = [random.randint(1, p-1), random.randint(1, p-1)]
        # a = [random.randint(0, p-1), 0]
        c, is_square = srtFp2(a)
        if is_square:  
            cc = squareFp2(c)
            if cc == a:
                print("srt Fp2 correct")
            else:
                print("srt Fp2 incorrect")
        else:
            print("this value is quadratic non-residue")

def check_srt_Fp4():
    is_square = False
    while not is_square:
        x = [[random.randint(1, p-1), random.randint(1, p-1)], [random.randint(1, p-1), random.randint(1, p-1)]]
        a = squareFp4(x)
        a = mulFp4(x, a)
        a = addFp4(a, B4)
        # a = [random.randint(0, p-1), 0]
        c, is_square = srtFp4(a)
        if is_square:  
            cc = squareFp4(c)
            if cc == a:
                printFp4([[MontConvInv(x[0][0]), MontConvInv(x[0][1])], [MontConvInv(x[1][0]), MontConvInv(x[1][1])]])
                printFp4([[MontConvInv(c[0][0]), MontConvInv(c[0][1])], [MontConvInv(c[1][0]), MontConvInv(c[1][1])]])
                print("srt Fp4 correct")
            else:
                print("srt Fp4 incorrect")
        else:
            print("this value is quadratic non-residue")


def check_inv_mul_Fp4():
    a = [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]
    a_inv = invFp4(a)
    one = mulFp4(a, a_inv)
    if([[MontConvInv(one[0][0]), MontConvInv(one[0][1])], [MontConvInv(one[1][0]), MontConvInv(one[1][1])]] == [[1, 0], [0, 0]]):
        print("inv Fp4 correct")

def check_inv_mul_Fp4_forRTL():
    a = [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]
    a_inv = invFp4_forRTL(a)
    one = mulFp4(a, a_inv)
    if([[MontConvInv(one[0][0]), MontConvInv(one[0][1])], [MontConvInv(one[1][0]), MontConvInv(one[1][1])]] == [[1, 0], [0, 0]]):
        print("inv Fp4 correct")


def check_inv_mul_Fp12():
    a = [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]
    ainv = invFp12(a)
    one = mulFp12(a, ainv)
    one[0][0][0] = MontConvInv(one[0][0][0])
    if(one == [[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]):
        print("inv Fp12 correct")


def check_inv_mul_Fp24():
    a = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    ainv = invFp24(a)
    one = mulFp24(a, ainv)
    one[0][0][0][0] = MontConvInv(one[0][0][0][0])
    if(one == [[[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]]):
        print("inv Fp24 correct")
        
def check_mul_conj_Fp24():
    a = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    b = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    ab_ = mulFp24(a, conjFp24(b))
    ab = mulFp24_conj_forRTL(a, b)
    if (ab == ab_) :
        print("ok")
    else:
        print("-----")
    

def check_inv_mul_Fp24_forRTL():
    a = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    ainv = invFp24_forRTL(a)
    if ainv == invFp24(a):
        print("invFp24_forRTL is correct")
    one = mulFp24(a, ainv)
    one[0][0][0][0] = MontConvInv(one[0][0][0][0])
    if(one == [[[[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]]):
        print("inv Fp24 for RTL correct")
    else:
        print("inv Fp24 for RTL incorrect")
        printFp24(one)


def expFp(a, u):
    r = a
    res = MontConv(1)
    for ui in bits_list(u):
        if (ui == 1):
            res = mul(res, r)
        if (ui == -1):
            res = mul(res, invFp(r))
        r = mul(r, r)
    # if (u < 0):
    #     res = conjFp24(r)
    return res

def check_fp12_sparse():
    a = [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]], [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]], [[0, 0], [0, 0]]]
    b = [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]
    mul_ab = mulFp12(a, b)
    sparse_ab = Fp12SparseMul(a, b)
    if (mul_ab == sparse_ab):
        print("sparse fp12 ok")
    else:
        print("sparse fp12 ng")

def check_sparse():
    # for i in range(10):
    a = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]], [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]], [[0, 0], [0, 0]]], 
        [[[0, 0], [0, 0]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[0, 0], [0, 0]]]]
    b = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], 
        [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]

    mul_ab = mulFp24(a, b)
    sparseforRTL_ab = sparseFp24(a, b)
    
    if (mul_ab == sparseforRTL_ab):
        print("sparse for 509 ok\n")
    else:
        print("sparse for 509 ng\n")
        print(mul_ab)
        print(sparseforRTL_ab)


def check_frob():
    f = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], 
        [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    f12 = FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(
        FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(f))))))))))))
    f24 = FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(
        FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(FrobFp24(f12))))))))))))
    frob_f = FrobFp24(f)
    f_exp = expFp24_for_test(f, p)
    if (f_exp == frob_f):
        print("exp == frob ok")
    if(f == f24):
        print("f == frob^24(f) ok")
    if(f12 == conjFp24(f)):
        print("conj(f) == frob^12(f) ok")


def check_compressed_squaring():
    f = pp_ml_k24(P, Q, T)
    # FE - easy part
    e = invFp24(f)
    f = mulFp24_conj_forRTL(e, f)
    e = FrobFp24(FrobFp24(FrobFp24(FrobFp24(f))))
    f = mulFp24(e, f)
    f2 = squareFp24(f)
    f2_ = SQR012345Fp24(f)
    if (f2 == f2_):
        print("SQR012345Fp24 is ok")
    else:
        printFp24(f2)
        print("----")
        printFp24(f2_)


def check_exp_hard_part():
    # hard partでinv(f) == conj(f)になるか確認
    f = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], 
        [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    f_ = conjFp24(f)
    f_inv = invFp24(f)
    t0 = mulFp24(f_, f_inv) # t0 = f^(p^12-1) = conj(f)/f
    f_exp = expFp24_for_test(t0, 2)
    f_exp_new = expFp24(t0, 2)
    if (f_exp == f_exp_new):
        print("expFp24 hard part ok")


def change_to_affine(T_):
    # 射影座標(X,Y,Z)のZ座標を1に補正する　X,Y座標を取り出せばそのままアフィン座標
    # Montgomery 空間中
    zinv = invFp4(T_[2])
    xaff = mulFp4(T_[0], zinv)
    yaff = mulFp4(T_[1], zinv)
    return [xaff, yaff, [[MontConv(1), 0], [0, 0]]]


def check_rP_Fp():
    # 曲線上の点P，位数rがある時rP = O（無限遠点）となるはず
    inf = ep_mul(r, [P[0][0][0], P[1][0][0]])
    printFp(P[0][0][0])
    printFp(P[1][0][0])
    printFp(inf[0])
    printFp(inf[1])


def check_rP_Fp4(r, T_):
    # 曲線上の点P，位数rがある時rP = O（無限遠点）となるはず
    inf = ep4_mul(r, T_)
    if(inf[0] == [[0, 0], [0, 0]] and inf[2] == [[0, 0], [0, 0]]):
        print("check_rP completed: the point on the curve and the field number is correct")
    else:
        print("check_rP uncompleted")


def check_on_curve_Fp(x, y):
    # 点Pが曲線上にのっているか y**2 = x**3 + Ax + B
    x2 = mul(x, x)
    x2a = (x2 + MontConv(A)) % p
    x3ax = mul(x2a, x)
    x3axb = (x3ax + MontConv(B)) % p
    y2 = mul(y, y)
    if(y2 == x3axb):
        print("on the BLS curve")
    else:
        print("Not on curve")

# ep4_on_curve
def check_on_curve_Fp4_affine(Q_):
    # 点Q_がFp4曲線上にのっているか y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]
    x2 = squareFp4(Q_[0])
    x2a = addFp4(x2, A4)
    x3ax = mulFp4(Q_[0], x2a)
    x3axb = addFp4(x3ax, B4)
    y2 = squareFp4(Q_[1])
    if(y2 == x3axb):
        print("on the Fp4 curve: affine coordinates")
    else:
        print("Not on the Fp4 curve: affine coordinates")


def check_on_curve_Fp4_projective(T_):
    # 点T_がFp4曲線上にのっているか y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]
    # モンゴメリ空間上の射影座標の点(X,Y,Z)を入力にとる
    # x = X/Z, y = Y/Z より (Y^2)Z = X^3 + AX(Z^2) + B(Z^3) が成立
    ax = mulFp4(A4, T_[0])
    bz = mulFp4(B4, T_[2])
    axbz = addFp4(ax, bz)
    z2 = squareFp4(T_[2])
    axz2bz3 = mulFp4(axbz, z2)
    x2 = squareFp4(T_[0])
    x3 = mulFp4(x2, T_[0])
    x3axz2bz3 = addFp4(x3, axz2bz3)
    y2 = squareFp4(T_[1])
    y2z = mulFp4(y2, T_[2])
    if (y2z == x3axz2bz3):
        print("on the Fp4 curve: projective coordinates")
    else:
        print("Not on the Fp4 curve: projective coordinates")


def check_miller_Loop(P_, Q_, T_, u):
    m = bits_list(u)
    f = [[[[MontConv(1), 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]]]
    negQ_ = [Q_[0], negFp4(Q_[1])]
    if u < 0:
        T_ = [Q_[0], negFp4(Q_[1]), [[MontConv(1), 0], [0, 0]]]
    check_rP_Fp4(r, T_)
    check_on_curve_Fp4_projective(T_)
    for l in m[1:]:
        print(l)
        T_ = ep4_dbl(T_)
        if l == 1:
            T_ = ep4_add(T_, Q_)
        if l == -1:
            T_ = ep4_add(T_, negQ_)
        # 無限遠点に飛ぶかの確認はaffine座標に直してから
        check_rP_Fp4(r, change_to_affine(T_))
        check_on_curve_Fp4_projective(T_)
    return T_, f


def check_final_exponentiation():
    f = [[[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]], 
        [[[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]],
        [[random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1)]]]]
    z1 = pp_fe_k24(f) # z1 = f**((p**24-1)//r)
    q = (p**12-1)*(p**4+1)*((p**8-p**4+1)//r)
    z2 = expFp24_for_test(f, q)
    z1r = expFp24_for_test(z1, r)
    if (MontConvInv(z1r[0][0][0][0]) == 1):
        print("pp_fe_k24 rth root is ok")
    # NOTE: 成り立たなかった
    if (z1 == z2):
        print("pp_fe_k24 equals f**((p**24-1)//r)")


def check_bit(u_):
    m = bits_list(u_)
    m_abs = bits_list(abs(u_))
    print(m)
    print(m_abs)
    U.reverse()
    print(U)

def bilinear_check(r_, P_, Q_, T_):
    check_on_curve_Fp(P_[0][0][0], P_[1][0][0])

    a = random.randint(1, r_-1)
    aP = ep_mul(a, [P_[0][0][0], P_[1][0][0]])
    check_on_curve_Fp(aP[0], aP[1])
    aP = [[[aP[0], 0], [0, 0]], [[aP[1], 0], [0, 0]]]
    
    check_on_curve_Fp4_affine(T_)
    b = random.randint(1, r_-1)
    bT = ep4_mul(b, T_)
    bT = change_to_affine(bT)
    check_on_curve_Fp4_affine(bT)

    bQ = bT[: 2]
    
    f = pp_oatep_k24(P_, Q_, T_)

    af = pp_oatep_k24(aP, Q_, T_)
    af_exp = expFp24_for_test(f, a)

    bf = pp_oatep_k24(P_, bQ, bT)
    bf_exp = expFp24_for_test(f, b)

    abf = pp_oatep_k24(aP, bQ, bT)
    abf_exp = expFp24_for_test(f, a*b)
    
    if (af == af_exp):
        print("e(aP, Q) == e(P, Q)^a")
    if (bf == bf_exp):
        print("e(P, bQ) == e(P, Q)^b")
    if (abf == abf_exp):
        print("e(aP, bQ) == e(P, Q)^ab")


def time_check():
    a = random.randint(1, r-1)
    aP = ep_mul(a, [P[0][0][0], P[1][0][0]])
    aP = [[[aP[0], 0], [0, 0]], [[aP[1], 0], [0, 0]]]
    
    b = random.randint(1, r-1)
    bT = ep4_mul(b, T)
    bT = change_to_affine(bT)

    bQ = bT[: 2]

    time_start = time.time()
    f = pp_oatep_k24(aP, bQ, bT)
    time_end = time.time()
    print(time_end - time_start)

if __name__ == "__main__":
    # bilinear_check(r, P, Q, T)
    check_frob()
    # check_final_exponentiation()
    # check_inv_mul_Fp_forRTL()
    # check_srt_Fp4()
    # check_on_curve_Fp4_affine(Q)
    # check_on_curve_Fp4_projective(T)