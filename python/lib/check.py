from lib.fpx import *
from lib.pairing import (
    double_line_twist6,
    add_line_twist6,
    sparse_mult_d6_twist,
    sparse_mult_m6_twist,
    pairing_bls12,
    pairing_bls24,
    scalar_mul_twist6,
    final_exp_bls24,
)
from lib.ep import scalar_mul
import argparse
from lib.util import read_json, bits_list, bits_of


def change_to_affine(Fq, T):
    # 射影座標(X,Y,Z)のZ座標を1に補正する　X,Y座標を取り出せばそのままアフィン座標
    # Montgomery 空間中
    zinv = Fq.inv(T[2])
    xaff = Fq.mul(T[0], zinv)
    yaff = Fq.mul(T[1], zinv)
    return [xaff, yaff, Fq.one()]


def check_rP_Fq(Fq, r, T, P, b_t, xi, D_twist):
    # 曲線上の点P，位数rがある時rP = O（無限遠点）となるはず
    inf = scalar_mul_twist6(Fq, r, T, P, b_t, xi, D_twist)
    if inf[0] == Fq.zero() and inf[2] == Fq.zero():
        print(
            "check_rP completed: the point on the curve and the field number is correct"
        )
    else:
        print("check_rP uncompleted")


def check_on_curve_Fq_projective(Fq, T, b_t):
    # 点T_がFp4曲線上にのっているか y^2 = x^3 + [[A0, A1], [A2, A3]]x + [[B0, B1], [B2, B3]]
    # モンゴメリ空間上の射影座標の点(X,Y,Z)を入力にとる
    # x = X/Z, y = Y/Z より (Y^2)Z = X^3 + AX(Z^2) + B(Z^3) が成立
    A4 = Fq.zero()
    ax = Fq.mul(A4, T[0])
    bz = Fq.mul(b_t, T[2])
    axbz = Fq.add(ax, bz)
    z2 = Fq.sqr(T[2])
    axz2bz3 = Fq.mul(axbz, z2)
    x2 = Fq.sqr(T[0])
    x3 = Fq.mul(x2, T[0])
    x3axz2bz3 = Fq.add(x3, axz2bz3)
    y2 = Fq.sqr(T[1])
    y2z = Fq.mul(y2, T[2])
    if y2z == x3axz2bz3:
        print("on the Fq curve: projective coordinates")
    else:
        print("Not on the Fq curve: projective coordinates")


def check_ml(Fq6, Fq, Fp, r, P, Q, b_t, xi, D_twist, miller_param_list):
    f = Fq6.one()
    negQ = [Q[0], Fq.neg(Q[1])]
    P_dbl = [Fp.neg(P[0]), P[1]]
    P_add = [P[0], Fp.neg(P[1])]

    if miller_param_list[0] < 0:
        T = [Q[0], Fq.neg(Q[1]), Fq.one()]
    else:
        T = [Q[0], Q[1], Fq.one()]

    check_rP_Fq(Fq, r, T, P, b_t, xi, D_twist)
    check_on_curve_Fq_projective(Fq, T, b_t)
    for l in miller_param_list[1:]:
        T, e = double_line_twist6(Fq, T, P_dbl, b_t, xi, D_twist)
        f = Fq6.sqr(f)
        f = Fq6.mapToFq6(f)
        if D_twist:
            f = sparse_mult_d6_twist(Fq, xi, e, f)
        else:
            f = sparse_mult_m6_twist(Fq, xi, e, f)
        if l == 1:
            T, e = add_line_twist6(Fq, T, P_add, Q, b_t, xi, D_twist)
            if D_twist:
                f = sparse_mult_d6_twist(Fq, xi, e, f)
            else:
                f = sparse_mult_m6_twist(Fq, xi, e, f)
        if l == -1:
            T, e = add_line_twist6(Fq, T, P_add, negQ, b_t, xi, D_twist)
            if D_twist:
                f = sparse_mult_d6_twist(Fq, xi, e, f)
            else:
                f = sparse_mult_m6_twist(Fq, xi, e, f)
        f = Fq6.mapFromFq6(f)
        check_rP_Fq(Fq, r, change_to_affine(Fq, T), P, b_t, xi, D_twist)
        check_on_curve_Fq_projective(Fq, T, b_t)
    return T, f


def check_mul(group):
    a = group.random_element()
    a_inv = group.inv(a)
    one = group.mul(a, a_inv)
    print(group.MontConvInv(one))
    # if group.MontConvInv() == 1:
    #     print("Fp12 ok")
    # else:
    #     print("Fp12 ng")


def check_bilinear(curve_group, Fq6, Fq, Fp, P, Q, b_t, xi, D_twist, U):
    if curve_group == "bls12":
        f = pairing_bls12(Fq6, Fq, Fp, P, Q, b_t, xi, D_twist, U)
    elif curve_group == "bls24":
        f = pairing_bls24(Fq6, Fq, Fp, P, Q, b_t, xi, D_twist, U)

    a = random.randint(1, p - 1)
    aP = scalar_mul(Fp, a, P)

    b = random.randint(1, p - 1)
    bQ = scalar_mul_twist6(Fq, b, T, P, b_t, xi, D_twist)
    bQ = change_to_affine(Fq, bQ)

    if curve_group == "bls12":
        abf = pairing_bls12(Fq6, Fq, Fp, aP, bQ, b_t, xi, D_twist, U)
    elif curve_group == "bls24":
        abf = pairing_bls24(Fq6, Fq, Fp, aP, bQ, b_t, xi, D_twist, U)

    if abf == Fq6.exp(f, a * b):
        print("e(aP, bQ) == e(P, Q)^ab")
    else:
        print("e(aP, bQ) != e(P, Q)^ab")


if __name__ == "__main__":
    psr = argparse.ArgumentParser(
        prog="プログラムの名前", usage="プログラムの使い方", description="プログラムの説明"
    )
    psr.add_argument("-c", "--curve", default=1, help="楕円曲線群")
    psr.add_argument("-p", "--characteristic", default=1, help="楕円曲線の標数のbit幅")
    psr.add_argument("-f", "--filename", default=1, help="読み込むJSONファイル")
    args = psr.parse_args()
    curve_group = args.curve
    curve_name = args.characteristic
    param = read_json(args.filename)[curve_group][curve_name]
    b = param["b"]
    u = param["u"]
    U = bits_list(u)
    D_twist = param["D_twist"]
    r = param["r"]
    p = param["p"]

    if curve_group == "bls12":
        # bls12-381
        Fp = Fp_t(p=p)
        Fp2 = Fp2_t(Fp=Fp, qnr=param["beta"])
        Fq = Fp2
        Fp4 = Fp4_t(Fp2=Fp2, qnr=param["xi"])
        Fp12 = Fp12_t(Fp4=Fp4, cnr=[[0, 0], [1, 0]])
        Fq6 = Fp12
        # b_t = Fq.MontConv([4, 4])
        # xi = [1, 1]
    elif curve_group == "bls24":
        Fp = Fp_t(p=p)
        Fp2 = Fp2_t(Fp=Fp, qnr=param["beta"])
        Fp4 = Fp4_t(Fp2=Fp2, qnr=param["beta2"])
        Fq = Fp4
        Fp12 = Fp12_t(Fp4=Fp4, cnr=[[param["xi"][0], 0], [param["xi"][1], 0]])
        Fp24 = Fp24_t(
            Fp12=Fp12, qnr=[[[0, 0], [0, 0]], [[1, 0], [0, 0]], [[0, 0], [0, 0]]]
        )
        Fq6 = Fp24

    xi_montconv = Fq.MontConv([[param["xi"][0], 0], [param["xi"][1], 0]])
    if D_twist:
        xi_inv = Fq.inv(xi_montconv)
        b_t = Fq.constMul(xi_inv, Fp.MontConv(b))
    else:
        b_t = Fq.constMul(xi_montconv, Fp.MontConv(b))

    P = [Fp.MontConv(param["P"][0]), Fp.MontConv(param["P"][1])]
    Q = [Fq.MontConv(param["Q"][0]), Fq.MontConv(param["Q"][1])]
    T = [Fq.MontConv(param["Q"][0]), Fq.MontConv(param["Q"][1]), Fq.one()]

    # check_ml(Fq6, Fq, Fp, r, P, Q, b_t, xi, D_twist, miller_param_list=U[::-1])

    check_bilinear(
        curve_group,
        Fq6,
        Fq,
        Fp,
        P,
        Q,
        b_t,
        [[param["xi"][0], 0], [param["xi"][1], 0]],
        D_twist,
        U,
    )
