import sys, csv

# 曲線によってimport元を変更
def MontConvInv(a):
    c = (a*montgomery_inv) % p
    return c


def MontConv(a):
    t = (a * L) % p
    return t


def bits_of(k):
    return [int(c) for c in "{0:b}".format(k)]

# NOTE: 各bitを[-1, 0, 1]に分ける
# NOTE: 合ってない
def bits_list(a):
    l = len(str(bin(abs(a)))) - 2
    res = [0] * l
    cnt = 0
    abs_a = abs(a)
    i = 0
    while abs_a > 0:
        if abs_a & 1:
            cnt += 1
        else:
            if cnt == 1:
                res[i-1] = 1
            elif cnt > 1:
                res[i] = 1
                res[i-cnt] = -1
            cnt = 0
        i += 1
        abs_a >>= 1
    if cnt == 1:
        res[i-1] = 1
    elif cnt > 1:
        res[i] = 1
        res[i-cnt] = -1
    res.reverse()
    return res if a > 0 else [-n for n in res]

def bits_calc(U):
    res = 1
    u = 0
    for ui in U:
        u += res * ui
        res <<= 1
    return u

def read_csv_dict(filename):
    f_read = open(filename, "r")
    dict = {}
    for line in csv.reader(f_read):
        if len(line) > 0 and line[0][0] == '#':
            continue
        if len(line) == 2:
            if line[0] == "twist_type" or line[0] == "curve_group":
                dict[line[0]] = line[1]
            else:
                dict[line[0]] = int(line[1], 16)
        elif len(line) > 0 and line[0] == "U":
            dict[line[0]] = [int(c) for c in line[1:]]
    return dict

args = sys.argv
dict = read_csv_dict(args[1])

curve_group = dict["curve_group"]

u = bits_calc(dict["U"])
U = dict["U"]
twist_type = dict["twist_type"]

if curve_group == "bls12":
    r = u**4 - u**2 + 1
    p = (((u-1)**2) * r) // 3 + u
elif curve_group == "bls24":
    r = u**8 - u**4 + 1
    p = (((u-1)**2) * r) // 3 + u
else:
    r = 0
    p = 0
    raise Exception("the curve is not implemented yet")

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
PX = dict["PX"]
PY = dict["PY"]
if curve_group == "bls12" or curve_group == "bn":
    B0 = dict["B0"]
    B1 = dict["B1"]
    B2 = [MontConv(B0), MontConv(B1)]
    QX0 = dict["QX0"]
    QX1 = dict["QX1"]
    QY0 = dict["QY0"]
    QY1 = dict["QY1"]
    P = [[MontConv(PX), 0], [MontConv(PY), 0]] # 計算のためFp2の形式
    Q = [[MontConv(QX0), MontConv(QX1)], [MontConv(QY0), MontConv(QY1)]]
    T = [[MontConv(QX0), MontConv(QX1)], [MontConv(QY0), MontConv(QY1)], [one, 0]]
elif curve_group == "bls24":
    B00 = dict["B00"]
    B01 = dict["B01"]
    B10 = dict["B10"]
    B11 = dict["B11"]
    B4 = [[MontConv(B00), MontConv(B01)], [MontConv(B10), MontConv(B11)]]
    QX00 = dict["QX00"]
    QX01 = dict["QX01"]
    QX10 = dict["QX10"]
    QX11 = dict["QX11"]
    QY00 = dict["QY00"]
    QY01 = dict["QY01"]
    QY10 = dict["QY10"]
    QY11 = dict["QY11"]
    P = [[[MontConv(PX), 0], [0, 0]], [[MontConv(PY), 0], [0, 0]]] # 計算のためFp4の形式
    Q = [[[MontConv(QX00), MontConv(QX01)], [MontConv(QX10), MontConv(QX11)]], [[MontConv(QY00), MontConv(QY01)], [MontConv(QY10), MontConv(QY11)]]]
    T = [Q[0], Q[1], [[one, 0], [0, 0]]]


if __name__ == "__main__":
    print(p_mod8)
    print(p_len)