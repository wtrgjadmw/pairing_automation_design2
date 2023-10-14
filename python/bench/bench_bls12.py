import random

from lib.parameters import MontConv, MontConvInv, bits_of
from lib.parameters import P, Q, T, B2, D_twist, A, B, A2
from lib.parameters import p, r, u, U

from lib.operate_Fp2 import mul, add
from lib.operate_Fp2 import negFp2, mulFp2, squareFp2, addFp2, invFp2, expFp2, conjFp2
from lib.operate_Fp12 import (
    mulFp12,
    squareFp12,
    sparseFp12,
    SQR012345Fp12,
    FrobFp12,
    conjFp12,
    invFp12,
    expFp12,
    expFp12_for_test,
)

from lib.ep_operation import ep_mul
from lib.ep2_operation import ep2_add, ep2_dbl, ep2_mul

from lib.optimal_ate_k12 import pp_ml_k12, pp_fe_k12, pp_oatep_k12

from lib.util import printFp12, printFp2, printFp


def check_mongomery_inv():
    a = random.randint(0, p - 1)
    am = MontConv(a)
    b = random.randint(0, p - 1)
    bm = MontConv(b)
    c = (a * b) % p
    mont_ab = mul(am, bm)
    mont_c = MontConv(c)
    if mont_ab == mont_c:
        print("mongomery_inv ok")


def check_sparse_Fp12():
    if D_twist:
        a = [
            [
                [random.randint(0, p - 1), random.randint(0, p - 1)],
                [random.randint(0, p - 1), random.randint(0, p - 1)],
            ],
            [[random.randint(0, p - 1), random.randint(0, p - 1)], [0, 0]],
            [[0, 0], [0, 0]],
        ]
    else:
        a = [
            [
                [random.randint(0, p - 1), random.randint(0, p - 1)],
                [random.randint(0, p - 1), random.randint(0, p - 1)],
            ],
            [[0, 0], [0, 0]],
            [[random.randint(0, p - 1), random.randint(0, p - 1)], [0, 0]],
        ]
    b = [
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
    ]

    ab = mulFp12(a, b)
    ab_sparse = sparseFp12(a, b)

    if ab == ab_sparse:
        print("sparse Fp12 correct")
    else:
        printFp12(ab)
        printFp12(ab_sparse)


def check_inv_Fp12():
    a = [
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
    ]
    a_inv1 = invFp12(a)
    a_inv2 = invFp12_forRTL(a)
    if a_inv1 == a_inv2:
        print("inv Fp12 ok")
    else:
        printFp12(a_inv1)
        printFp12(a_inv2)


def change_to_affine(T_):
    # 射影座標(X,Y,Z)のZ座標を1に補正する　X,Y座標を取り出せばそのままアフィン座標
    # Montgomery 空間中
    zinv = invFp2(T_[2])
    xaff = mulFp2(T_[0], zinv)
    yaff = mulFp2(T_[1], zinv)
    return [xaff, yaff, [MontConv(1), 0]]


def check_rP_ep(P_):
    # 曲線上の点P，位数rがある時rP = O（無限遠点）となるはず
    inf = ep_mul(r, P_)
    printFp(P_[0])
    printFp(P_[1])
    printFp(inf[0])
    printFp(inf[1])


def check_rP_ep2(T_):
    # 曲線上の点P，位数rがある時rP = O（無限遠点）となるはず
    inf = ep2_mul(r, T_)
    if inf[0] == [0, 0] and inf[2] == [0, 0]:
        print(
            "check_rP completed: the point on the curve and the field number is correct"
        )
    else:
        print("check_rP uncompleted")


def check_on_curve_Fp(x, y):
    # 点Pが曲線上にのっているか y**2 = x**3 + Ax + B
    x2 = mul(x, x)
    x2a = add(x2, MontConv(A))
    x3ax = mul(x2a, x)
    x3axb = add(x3ax, MontConv(B))
    y2 = mul(y, y)
    if y2 == x3axb:
        print("on the BLS curve")
    else:
        print("Not on curve")


# ep4_on_curve
def check_on_curve_Fp2_affine(Q_):
    # 点Q_がFp2曲線上にのっているか y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]
    x2 = squareFp2(Q_[0])
    x2a = addFp2(x2, A2)
    x3ax = mulFp2(Q_[0], x2a)
    x3axb = addFp2(x3ax, B2)
    y2 = squareFp2(Q_[1])
    if y2 == x3axb:
        print("on the Fp2 curve: affine coordinates")
    else:
        print("Not on the Fp2 curve: affine coordinates")


def check_on_curve_Fp2_projective(T_):
    # 点T_がFp2曲線上にのっているか y^2 = x^3 + [A0, A1]x + [B0, B1]
    # モンゴメリ空間上の射影座標の点(X,Y,Z)を入力にとる
    # x = X/Z, y = Y/Z より (Y^2)Z = X^3 + AX(Z^2) + B(Z^3) が成立
    ax = mulFp2(A2, T_[0])
    bz = mulFp2(B2, T_[2])
    axbz = addFp2(ax, bz)
    z2 = squareFp2(T_[2])
    axz2bz3 = mulFp2(axbz, z2)
    x2 = squareFp2(T_[0])
    x3 = mulFp2(x2, T_[0])
    x3axz2bz3 = addFp2(x3, axz2bz3)
    y2 = squareFp2(T_[1])
    y2z = mulFp2(y2, T_[2])
    if y2z == x3axz2bz3:
        print("on the Fp2 curve: projective coordinates")
    else:
        print("Not on the Fp2 curve: projective coordinates")


def check_miller_Loop(P_, Q_, T_, U):
    m = U[::-1]
    # f = [[MontConv(1), 0], [0, 0], [0, 0]]
    negQ_ = [Q_[0], negFp2(Q_[1])]
    if m[0] < 0:
        T_ = [Q_[0], negFp2(Q_[1]), [MontConv(1), 0]]
    check_rP(r, T_)
    check_on_curve_Fp2_projective(T_)
    for l in m[1:]:
        print(l)
        T_, e = ep2_dbl(T_, P_)
        if l == 1:
            T_, e = ep2_add(T_, P_, Q_)
        if l == -1:
            T_, e = ep2_add(T_, P_, negQ_)
        # 無限遠点に飛ぶかの確認はaffine座標に直してから
        check_rP(r, change_to_affine(T_))
        check_on_curve_Fp2_projective(T_)


def check_expFp12():
    f = pp_ml_k12(P, Q, T)
    # FE - easy part
    k = FrobFp12(FrobFp12(f))
    k = mulFp12(k, f)
    l = conjFp12(k)
    k = invFp12(k)
    f = mulFp12(l, k)
    f_exp = expFp12_for_test(f, -u)
    f_exp = conjFp12(f_exp)
    f_exp_new = expFp12(f)
    if f_exp == f_exp_new:
        print("expFp12 in hard part ok")
    else:
        printFp12(f_exp)
        print("-----")
        printFp12(f_exp_new)


def check_expFp12_for_test():
    f = [
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
    ]
    f2 = expFp12_for_test(f, 2)
    f2_ = squareFp12(f)
    if f2 == f2_:
        print("expFp12_for_test is ok")
    else:
        printFp12(f2)
        print("-----")
        printFp12(f2_)


def check_frob():
    f = [
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
        [
            [random.randint(0, p - 1), random.randint(0, p - 1)],
            [random.randint(0, p - 1), random.randint(0, p - 1)],
        ],
    ]
    f12 = FrobFp12(
        FrobFp12(
            FrobFp12(
                FrobFp12(
                    FrobFp12(
                        FrobFp12(
                            FrobFp12(
                                FrobFp12(FrobFp12(FrobFp12(FrobFp12(FrobFp12(f)))))
                            )
                        )
                    )
                )
            )
        )
    )
    frob_f = FrobFp12(f)
    f_exp = expFp12_for_test(f, p)
    if f_exp == frob_f:
        print("exp == frob ok")
    else:
        printFp12(f_exp)
        print("----")
        printFp12(frob_f)
    if f == f12:
        print("f == frob^12(f) ok")


def check_fe_easy_part():
    f = pp_ml_k12(P, Q, T)
    q = (p**6 - 1) * (p**2 + 1)
    f_ = expFp12_for_test(f, q)
    # FE - easy part
    k = FrobFp12(FrobFp12(f))
    k = mulFp12(k, f)
    l = conjFp12(k)
    k = invFp12(k)
    f = mulFp12(l, k)

    if f_ == f:
        print("final exponentiation easy part is ok")
    # else:
    # printFp12(f_)
    # printFp12(f_conj)


def check_compressed_squaring():
    T_, f = pp_ml_k12(P, Q, T, U[::-1])
    # FE - easy part
    k = FrobFp12(FrobFp12(f))
    k = mulFp12(k, f)
    l = conjFp12(k)
    k = invFp12(k)
    f = mulFp12(l, k)
    f2 = squareFp12(f)
    f2_ = SQR012345Fp12(f)
    if f2 == f2_:
        print("SQR012345Fp12 is ok")
    else:
        printFp12(f2)
        print("----")
        printFp12(f2_)


def check_final_exponentiation():
    # if curve_group == "bls12":
    #     miller_param_list = U
    # else:
    #     miller_param_list = bits_of(abs(6*u+2))
    miller_param_list = U
    T_, f = pp_ml_k12(P, Q, T, miller_param_list)
    # if curve_group == "bn":
    #     f = pp_fa_k12(f, P, Q, T_)
    z1 = pp_fe_k12(f)
    z1r = expFp12_for_test(z1, r)
    if MontConvInv(z1r[0][0][0]) == 1:
        print("pp_fe_k12 rth root is ok")


def bilinear_check(r_, P_, Q_, T_):
    check_on_curve_Fp(P_[0][0], P_[1][0])

    a = random.randint(1, r_ - 1)
    aP = ep_mul(a, [P_[0][0], P_[1][0]])
    check_on_curve_Fp(aP[0], aP[1])
    aP = [[aP[0], 0], [aP[1], 0]]

    check_on_curve_Fp2_affine(T_)
    b = random.randint(1, r_ - 1)
    bT = ep2_mul(b, T_)
    bT = change_to_affine(bT)
    check_on_curve_Fp2_affine(bT)

    bQ = bT[:2]

    f = pp_oatep_k12(P_, Q_, T_)

    af = pp_oatep_k12(aP, Q_, T_)
    af_exp = expFp12_for_test(f, a)

    bf = pp_oatep_k12(P_, bQ, bT)
    bf_exp = expFp12_for_test(f, b)

    abf = pp_oatep_k12(aP, bQ, bT)
    abf_exp = expFp12_for_test(f, a * b)

    if af == af_exp:
        print("e(aP, Q) == e(P, Q)^a")
    if bf == bf_exp:
        print("e(P, bQ) == e(P, Q)^b")
    if abf == abf_exp:
        print("e(aP, bQ) == e(P, Q)^ab")


if __name__ == "__main__":
    # check_miller_Loop(P, Q, T, U)
    # check_final_exponentiation()
    bilinear_check(r, P, Q, T)
    # check_compressed_squaring()
    # h1P = ep_mul(h1, [P[0][0], P[1][0]])
    # check_rP_ep(h1P)
    # h2T = ep2_mul(h2, T)
    # check_rP_ep2(change_to_affine(h2T))
    # check_on_curve_Fp2_affine(h2T)
    # check_rP_ep2(h2T)
