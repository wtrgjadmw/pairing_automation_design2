import csv
from lib.pairing import add_line_twist6, double_line_twist6, sparse_mult_m6_twist, sparse_mult_d6_twist, SQR012345
from lib.util import FormulaSet
from lib.parameters import Fp, Fq, Fq6, P, Q, T, b_t, D_twist, xi, curve_group, curve_name


def csv2Formula(path):
    f = open(path, "r")
    formulaList = []
    for line in csv.reader(f):
        formulaList.append(FormulaSet(
            ret=line[0], opr1=line[1], opr2=line[2], type=line[3]))
    return formulaList


def initialize_valueList(k: int, a, b):
    valueList = {}

    # initialize
    valueList["ZERO"] = Fp.zero()
    valueList["ONE"] = Fp.one()
    valueList["xp"] = P[0]
    valueList["yp"] = P[1]
    if k == 2:
        for i in range(2):
            valueList['a{}'.format(i)] = a[i]
            valueList['b{}'.format(i)] = b[i]
    elif k == 4:
        for j in range(2):
            for i in range(2):
                valueList['a{}'.format(i)] = a[j][i]
                valueList['b{}'.format(i)] = b[j][i]
    elif k == 12:
        for m in range(3):
            for j in range(2):
                for i in range(2):
                    valueList['a{}{}{}'.format(m, j, i)] = a[m][j][i]
                    valueList['b{}{}{}'.format(m, j, i)] = b[m][j][i]
    elif k == 24:
        for n in range(2):
            for m in range(3):
                for j in range(2):
                    for i in range(2):
                        valueList['a{}{}{}{}'.format(
                            n, m, j, i)] = a[n][m][j][i]
                        valueList['b{}{}{}{}'.format(
                            n, m, j, i)] = b[n][m][j][i]
    return valueList


def calculate_test(valueList: dict, formulaList: list):
    # calculate
    for formula in formulaList:
        if formula.type == "ADD":
            valueList[formula.ret] = Fp.add(
                valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "SUB":
            valueList[formula.ret] = Fp.sub(
                valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "MUL":
            valueList[formula.ret] = Fp.mul(
                valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "INV":
            valueList[formula.ret] = Fp.inv(valueList[formula.opr1])
    return valueList


def check_result(valueList: dict, k: int, c, isOnCurve=False):
    # check result
    if k == 2:
        for i in range(2):
            if valueList['c{}'.format(i)] != c[i]:
                print("Error: this formula has some error;")
                return
    elif k == 4:
        for j in range(2):
            for i in range(2):
                if valueList['c{}'.format(i)] != c[j][i]:
                    print("Error: this formula has some error;")
                    return
    elif k == 12:
        if isOnCurve:
            for i in range(2):
                if valueList['l00{}'.format(i)] != (c[0][0][i] if D_twist else c[0][1][i]):
                    print("Error: this formula has some error;")
                    return
                if valueList['l10{}'.format(i)] != (c[1][0][i] if D_twist else c[2][0][i]):
                    print("Error: this formula has some error;")
                    return
                if valueList['l01{}'.format(i)] != (c[0][1][i] if D_twist else c[0][0][i]):
                    print("Error: this formula has some error;")
                    return
        else:
            for m in range(3):
                for j in range(2):
                    for i in range(2):
                        if valueList['c{}{}{}'.format(m, j, i)] != c[m][j][i]:
                            print("Error: this formula has some error;")
                            return
    elif k == 24:
        # print(c)
        for n in range(2):
            for m in range(3):
                for j in range(2):
                    for i in range(2):
                        # print(valueList['c{}{}{}{}'.format(n, m, j, i)])
                        if valueList['c{}{}{}{}'.format(
                                n, m, j, i)] != c[n + m * 2][j][i]:
                            print("Error: this formula has some error;")
                            return
    print("Success!")


def test_formula(k, formulaName, a, b, c, isOnCurve=False):
    valueList = fp12_initialize_value(a, b)
    formulaList = csv2Formula(
        path="/home/mfukuda/pairing_automation_design/csv/{}/{}/{}.csv".format(curve_group, curve_name, formulaName))
    valueList = calculate_test(valueList, formulaList)
    print(formulaName, end=": ")
    check_result(valueList, k, c, isOnCurve)


def fp12_initialize_value(a, b):
    valueList = {}
    valueList["ZERO"] = Fp.zero()
    valueList["ONE"] = Fp.one()
    valueList["xp"] = P[0]
    valueList["yp"] = P[1]
    for i in range(2):
        valueList['xq{}'.format(i)] = Q[0][i]
        valueList['yq{}'.format(i)] = Q[1][i]
        valueList['xt{}'.format(i)] = T[0][i]
        valueList['yt{}'.format(i)] = T[1][i]
        valueList['zt{}'.format(i)] = T[2][i]
        valueList['b_t{}'.format(i)] = b_t[i]
    for j in range(1, 6):
        for i in range(2):
            valueList['XI{}{}'.format(j, i)] = Fq6.k[j][i]
    for m in range(3):
        for j in range(2):
            for i in range(2):
                valueList['a{}{}{}'.format(m, j, i)] = a[m][j][i]
                valueList['b{}{}{}'.format(m, j, i)] = b[m][j][i]
    return valueList


def fp12_test_formula():
    a = Fq6.random_element()
    b = Fq6.random_element()
    test_formula(12, "CONJ", a, b, Fq6.conj(a))
    test_formula(12, "FROB", a, b, Fq6.frob(a))
    test_formula(12, "MUL", a, b, Fq6.mul(a, b))
    test_formula(12, "SQR", a, b, Fq6.sqr(a))
    new_T, l = double_line_twist6(Fq, T, P, b_t, xi, D_twist)
    test_formula(12, "PDBL", a, b, [[l[0], l[3]], [l[1], l[4]], [l[2], l[5]]], True)
    new_T, l = add_line_twist6(Fq, T, P, Q, b_t, xi, D_twist)
    test_formula(12, "PADD", a, b, [[l[0], l[3]], [l[1], l[4]], [l[2], l[5]]], True)
    c_6 = SQR012345(Fq, xi, [a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1]])
    test_formula(12, "SQR012345", a, b, [[c_6[0], c_6[3]], [c_6[1], c_6[4]], [c_6[2], c_6[5]]])
    c_6 = sparse_mult_d6_twist(Fq, xi,
        [a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1]],
        [b[0][0], b[1][0], b[2][0], b[0][1], b[1][1], b[2][1]],
    )
    test_formula(12, "SPARSE_D", a, b, [[c_6[0], c_6[3]], [c_6[1], c_6[4]], [c_6[2], c_6[5]]])
    c_6 = sparse_mult_m6_twist(Fq, xi,
        [a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1]],
        [b[0][0], b[1][0], b[2][0], b[0][1], b[1][1], b[2][1]],
    )
    test_formula(12, "SPARSE_M", a, b, [[c_6[0], c_6[3]], [c_6[1], c_6[4]], [c_6[2], c_6[5]]])


if __name__ == "__main__":
    if curve_group == "bls12":
        fp12_test_formula()
