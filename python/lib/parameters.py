import sys, csv
import json

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

args = sys.argv
dict = read_json(args[1])

curve_group = dict["curve_group"]
A = 0
B = dict["b"]

u = dict["u"]
U = bits_list(u)
D_twist = dict["D_twist"]
r = dict["r"]
p = dict["p"]

p_len = p.bit_length()
L = 2 ** p_len
montgomery_inv = pow(L, -1, p)
inv_init_val = (2 ** (2 * p_len)) % p
p_inv = (-pow(p, -1, L))%L
p_mod8 = p % 8
if p & 1 == 0:
    Exception("characteristic number p is not prime")

one = MontConv(1)

# PはFpの楕円曲線(y^2 = x^3 + 1)上，QはFp4の楕円曲線(y^2 = x^3 - 1/v)上，TはQの射影座標変換
if curve_group == "bls12" or curve_group == "bn":
    A2 = [0, 0]
    B2 = [MontConv(x) for x in dict["btw"]]
    P = [[MontConv(x), 0] for x in dict["P"]] # 計算のためFp2の形式
    Q = [[MontConv(x) for x in xx] for xx in dict["Q"]]
    T = [Q[0], Q[1], [one, 0]]
elif curve_group == "bls24":
    A4 = [[0, 0], [0, 0]]
    btw = dict["btw"]
    B4 = [[MontConv(btw[0]), MontConv(btw[1])], [MontConv(btw[2]), MontConv(btw[3])]]
    P = [[[MontConv(x), 0], [0, 0]] for x in dict["P"]] # 計算のためFp4の形式
    Q = [[[MontConv(x[0]), MontConv(x[1])], [MontConv(x[2]), MontConv(x[3])]] for x in dict["Q"]]
    T = [Q[0], Q[1], [[one, 0], [0, 0]]]


if __name__ == "__main__":
    print(p_mod8)
    print(p_len)