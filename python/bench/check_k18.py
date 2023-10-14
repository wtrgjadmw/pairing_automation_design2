import random, time

from parameters import MontConv, MontConvInv, bits_list
from parameters import P, Q, T, A3, B3, A, B
from parameters import p, r, u, U

from operate_Fp import mul, invFp, invFp_forRTL, srtFp, expFp
from operate_Fp3 import mulFp3, invFp3, squareFp3, expFp3, FrobFp3, negFp3, addFp3
from operate_Fp9 import invFp9, mulFp9
from operate_Fp18 import invFp18, mulFp18, expFp18, FrobFp18, expFp18_for_test

from ep3_operation import ep3_add, ep3_dbl, ep3_mul
# from ep_operation import ep_mul
# from optimal_ate_k24 import pp_fe_k24, pp_oatep_k24, pp_ml_k24

from util import *

def check_inv_mul_Fp_forRTL():
    a = 0x1b12db9b710e91f86a7b232824e6f1524e1cec35013fb143012a0a4acad83fca1fe4093fb2b7f6f10b0764ad8b88cb5e7e5e56704d8088d9f8b464710cebebb4
    ainv = invFp_forRTL(a, p)
    printFp(ainv)
    ainv_ = invFp(a)
    one = mul(a, ainv)
    if(MontConvInv(one) == 1):
        print("inv Fp correct")
    else:
        printFp(one)
        print("inv Fp incorrect")
    printFp(ainv_)
    one = mul(a, ainv_)
    if(MontConvInv(one) == 1):
        print("inv Fp correct")
    else:
        print("inv Fp incorrect")


def check_inv_mul_Fp3():
    a = [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)]
    ainv = invFp3(a)
    one = mulFp3(a, ainv)
    if([MontConvInv(one[0]), MontConvInv(one[1]), MontConvInv(one[2])] == [1, 0, 0]):
        print("inv Fp3 correct")

def check_sqr_Fp3():
    a = [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)]
    a_mul = mulFp3(a, a)
    a_sqr = squareFp3(a)
    if a_mul == a_sqr:
        print("sqr Fp3 ok")

def check_inv_mul_Fp9():
    a = [[random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)]]
    ainv = invFp9(a)
    one = mulFp9(a, ainv)
    if([[MontConvInv(one[0][0]), MontConvInv(one[0][1]), MontConvInv(one[0][2])], [MontConvInv(one[1][0]), MontConvInv(one[1][1]), MontConvInv(one[1][2])], [MontConvInv(one[2][0]), MontConvInv(one[2][1]), MontConvInv(one[2][2])]] == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]):
        print("inv Fp9 correct")


def check_srt_Fp():
    a = random.randint(0, p-1)
    c, is_qr = srtFp(a)
    if is_qr:
        cc = mul(c, c)
        if cc == a:
            print("srt Fp correct")
    else:
        print("this value is qnr1")


def check_srt_Fp2():
    a = [random.randint(0, p-1), random.randint(0, p-1)]
    c, is_qr = srtFp2(a)
    if is_qr:  
        cc = mulFp2(c, c)
        if cc == a:
            print("srt Fp2 correct")
        else:
            print("srt Fp2 incorrect")
    else:
        print("this value is qnr1")


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

def check_frob_fp3():
    a = [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)]
    exp_a = expFp3(a, p)
    frob_a = FrobFp3(a)
    if exp_a == frob_a:
        print("frob fp3 ok")


def check_frob_fp18():
    a = [[[random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)]], [[random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)], [random.randint(0, p-1), random.randint(0, p-1), random.randint(0, p-1)]]]
    exp_a = expFp18_for_test(a, p)
    frob_a = FrobFp18(a)
    if exp_a == frob_a:
        print("frob fp18 ok")


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
    zinv = invFp3(T_[2])
    xaff = mulFp3(T_[0], zinv)
    yaff = mulFp3(T_[1], zinv)
    return [xaff, yaff, [MontConv(1), 0, 0]]


def check_rP(r, T_):
    # 曲線上の点P，位数rがある時rP = O（無限遠点）となるはず
    inf = ep3_mul(r, T_)
    if(inf[0] == [0, 0, 0] and inf[2] == [0, 0, 0]):
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
        print("on curve")
    else:
        print("Not on curve")

# ep3_on_curve
def check_on_curve_Fp3_affine(Q_):
    # 点Q_がFp3曲線上にのっているか y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]
    x2 = squareFp3(Q_[0])
    x2a = addFp3(x2, A3)
    x3ax = mulFp3(Q_[0], x2a)
    x3axb = addFp3(x3ax, B3)
    y2 = squareFp3(Q_[1])
    if(y2 == x3axb):
        print("on the Fp3 curve: affine coordinates")
    else:
        printFp3(y2)
        printFp3(x3axb)
        print("Not on the Fp3 curve: affine coordinates")


def check_on_curve_Fp3_projective(T_):
    # 点T_がFp3曲線上にのっているか y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]
    # モンゴメリ空間上の射影座標の点(X,Y,Z)を入力にとる
    # x = X/Z, y = Y/Z より (Y^2)Z = X^3 + AX(Z^2) + B(Z^3) が成立
    ax = mulFp3(A3, T_[0])
    bz = mulFp3(B3, T_[2])
    axbz = addFp3(ax, bz)
    z2 = squareFp3(T_[2])
    axz2bz3 = mulFp3(axbz, z2)
    x2 = squareFp3(T_[0])
    x3 = mulFp3(x2, T_[0])
    x3axz2bz3 = addFp3(x3, axz2bz3)
    y2 = squareFp3(T_[1])
    y2z = mulFp3(y2, T_[2])
    if (y2z == x3axz2bz3):
        print("on the Fp3 curve: projective coordinates")
    else:
        printFp3(y2z)
        printFp3(x3axz2bz3)
        print("Not on the Fp3 curve: projective coordinates")


def check_miller_Loop(P_, Q_, T_, u):
    m = U[::-1]
    negQ_ = [Q_[0], negFp3(Q_[1])]
    # if u < 0:
    #     T_ = [Q_[0], negFp3(Q_[1]), [MontConv(1), 0, 0]]
    check_rP(r, T_)
    check_on_curve_Fp3_projective(T_)
    # for l in m[1:]:
    #     print(l)
    #     T_, e = ep3_dbl(T_, P_)
    #     if l == 1:
    #         T_, e = ep3_add(T_, P_, Q_)
    #     if l == -1:
    #         T_, e = ep3_add(T_, P_, negQ_)
    #     # 無限遠点に飛ぶかの確認はaffine座標に直してから
    #     check_rP(r, change_to_affine(T_))
    #     check_on_curve_Fp3_projective(T_)
    # return T_


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
    check_on_curve_Fp3_affine(Q)
    # check_miller_Loop(P, Q, T, u)
    # bilinear_check(r, P, Q, T)
    # check_final_exponentiation()