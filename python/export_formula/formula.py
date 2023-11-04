import argparse
from lib.fpx import *
from lib.util import read_json, bits_list, bits_of
from lib.pairing import double_line_twist6


def make_formula(Fq, T, P, b_t, xi, D_twist):
    double_line_twist6(Fq, T, P, b_t, xi, D_twist)


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
        Fp = Fp_t(p=p, formulaMode=True)
        Fp2 = Fp2_t(Fp=Fp, qnr=param["beta"])
        Fq = Fp2
        Fp4 = Fp4_t(Fp2=Fp2, qnr=param["xi"])
        Fp12 = Fp12_t(Fp4=Fp4, cnr=[[0, 0], [1, 0]])
        Fq6 = Fp12
        # b_t = Fq.MontConv([4, 4])
        # xi = [1, 1]
    elif curve_group == "bls24":
        Fp = Fp_t(p=p, formulaMode=True)
        Fp2 = Fp2_t(Fp=Fp, qnr=param["beta"])
        Fp4 = Fp4_t(Fp2=Fp2, qnr=param["beta2"])
        Fq = Fp4
        Fp12 = Fp12_t(Fp4=Fp4, cnr=[[param["xi"][0], 0], [param["xi"][1], 0]])
        Fp24 = Fp24_t(
            Fp12=Fp12, qnr=[[[0, 0], [0, 0]], [[1, 0], [0, 0]], [[0, 0], [0, 0]]]
        )
        Fq6 = Fp24

    xi = [[param["xi"][0], 0], [param["xi"][1], 0]]
    xi_montconv = Fq.MontConv([[param["xi"][0], 0], [param["xi"][1], 0]])
    if D_twist:
        xi_inv = Fq.inv(xi_montconv)
        b_t = Fq.constMul(xi_inv, Fp.MontConv(b))
    else:
        b_t = Fq.constMul(xi_montconv, Fp.MontConv(b))

    P = [Fp.MontConv(param["P"][0]), Fp.MontConv(param["P"][1])]
    Q = [Fq.MontConv(param["Q"][0]), Fq.MontConv(param["Q"][1])]
    T = [Fq.MontConv(param["Q"][0]), Fq.MontConv(param["Q"][1]), Fq.one()]
    print("ok")
    make_formula(Fq, T, P, b_t, xi, D_twist)
