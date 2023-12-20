import sys, csv
import json
import argparse
from lib.fpx import *

# 曲線によってimport元を変更
def MontConvInv(a):
    c = (a*montgomery_inv) % p
    return c


def MontConv(a):
    t = (a * L) % p
    return t


def bits_of(k):
    return [int(c) for c in "{0:b}".format(k)]


def bits_list(a):
    a_abs = abs(a)
    mask = 0b11
    res = []
    while (a_abs != 0):
        if (a_abs & 1):
            ui = 2 - (a_abs & mask)
            if (ui > 0):
                a_abs -= 1
            else:
                a_abs += 1
            res.append(ui)
        else:
            res.append(0)
        a_abs >>= 1
    if (a < 0):
        res = [-ui for ui in res]
    return res


def bits_calc(U):
    res = 1
    u = 0
    for ui in U:
        u += res * ui
        res <<= 1
    return u

def read_json(filename):
    with open(filename, "r") as f:
        dict = json.load(f)
    return dict


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
    fp2_qnr = param["beta"]
    fp4_qnr = param["xi"]
    Fp = Fp_t(p=p)
    Fp2 = Fp2_t(Fp=Fp, qnr=param["beta"])
    Fp4 = Fp4_t(Fp2=Fp2, qnr=param["xi"])
    Fp12 = Fp12_t(Fp4=Fp4, cnr=[[0, 0], [1, 0]])

if curve_group == "bls24":
    fp2_qnr = param["beta"]
    fp4_qnr = param["beta2"]
    fp12_cnr = param["xi"]
    Fp = Fp_t(p=p)
    Fp2 = Fp2_t(Fp=Fp, qnr=param["beta"])
    Fp4 = Fp4_t(Fp2=Fp2, qnr=param["beta2"])
    Fp12 = Fp12_t(Fp4=Fp4, cnr=[[param["xi"][0], 0], [param["xi"][1], 0]])
    Fp24 = Fp24_t(
        Fp12=Fp12, qnr=[[[0, 0], [0, 0]], [[1, 0], [0, 0]], [[0, 0], [0, 0]]]
    )