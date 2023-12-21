import csv
from lib.pairing import add_line_twist6, double_line_twist6, sparse_mult_m6_twist, sparse_mult_d6_twist, SQR012345
from lib.util import formulaSet
from lib.parameters import Fp, Fp2, Fp4, Fp12, Fp24, P, Q, T, b_t, D_twist, xi

def csv2Formula(path):
    f = open(path, "r")
    formulaList = []
    for line in csv.reader(f):
        formulaList.append(formulaSet(ret=line[0], opr1=line[1], opr2=line[2], type=line[3]))
    return formulaList

def test_formula(formulaList: list, k: int):
    valueList = {}

    # initialize
    valueList["ZERO"] = Fp.zero()
    valueList["ONE"] = Fp.one()
    valueList["xp"] = P[0]
    valueList["yp"] = P[1]
    if k == 2:
        a = Fp2.random_element()
        b = Fp2.random_element()
        for i in range(2):
            valueList['a{}'.format(i)] = a[i]
            valueList['b{}'.format(i)] = b[i]
    elif k == 4:
        a = Fp4.random_element()
        b = Fp4.random_element()
        for j in range(2):
            for i in range(2):
                valueList['a{}{}'.format(j, i)] = a[j][i]
                valueList['b{}{}'.format(j, i)] = b[j][i]
    elif k == 12:
        a = Fp12.random_element()
        b = Fp12.random_element()
        for m in range(3):
            for j in range(2):
                for i in range(2):
                    valueList['a{}{}{}'.format(m, j, i)] = a[m][j][i]
                    valueList['b{}{}{}'.format(m, j, i)] = b[m][j][i]
    elif k == 24:
        a = Fp24.random_element()
        b = Fp24.random_element()
        for n in range(2):
            for m in range(3):
                for j in range(2):
                    for i in range(2):
                        valueList['a{}{}{}{}'.format(n, m, j, i)] = a[n][m][j][i]
                        valueList['b{}{}{}{}'.format(n, m, j, i)] = b[n][m][j][i]
        # T_ = scalar_mul_twist6(Fp4, 2, T, P, b_t, xi, D_twist)
        # for j in range(2):
        #     for i in range(2):
        #         valueList['b_t{}{}'.format(j, i)] = b_t[j][i]
        #         valueList['xq{}{}'.format(j, i)] = Q[0][j][i]
        #         valueList['yq{}{}'.format(j, i)] = Q[1][j][i]
        #         valueList['xt{}{}'.format(j, i)] = T_[0][j][i]
        #         valueList['yt{}{}'.format(j, i)] = T_[1][j][i]
        #         valueList['zt{}{}'.format(j, i)] = T_[2][j][i]

    # calculate
    for formula in formulaList:
        if formula.type == "ADD":
            valueList[formula.ret] = Fp.add(valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "SUB":
            valueList[formula.ret] = Fp.sub(valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "MUL":
            valueList[formula.ret] = Fp.mul(valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "INV":
            valueList[formula.ret] = Fp.inv(valueList[formula.opr1])

    # check result
    if k == 2:
        c = Fp2.mul(a, b)
        for i in range(2):
            if valueList['c{}'.format(i)] != c[i]:
                print("Error: this formula has some error;")
                return            
    elif k == 4:
        for j in range(2):
            for i in range(2):
                if valueList['c{}{}'.format(j, i)] != c[j][i]:
                    print("Error: this formula has some error;")
                    return
    elif k == 12:
        c = Fp12.mul(a, b)
        for m in range(3):
            for j in range(2):
                for i in range(2):
                    if valueList['c{}{}{}'.format(m, j, i)] != c[m][j][i]:
                        print("Error: this formula has some error;")
                        return
    elif k == 24:
        c = SQR012345(Fp4, xi, [a[0][0], a[1][0], a[0][1], a[1][1], a[0][2], a[1][2]])
        # print(c)
        # for j in range(2):
        #     for i in range(2):
        #         if valueList['l01{}{}'.format(j, i)] != c[0][j][i]:
        #             print("Error: this formula has some error;")
        #             return
        #         if valueList['l10{}{}'.format(j, i)] != c[2][j][i]:
        #             print("Error: this formula has some error;")
        #             return
        #         if valueList['l00{}{}'.format(j, i)] != c[3][j][i]:
        #             print("Error: this formula has some error;")
        #             return
        for n in range(2):
            for m in range(3):
                for j in range(2):
                    for i in range(2):
                        # print(valueList['c{}{}{}{}'.format(n, m, j, i)])
                        if valueList['c{}{}{}{}'.format(n, m, j, i)] != c[n+m*2][j][i]:
                            print("Error: this formula has some error;")
                            return
    print("Success!")


if __name__ == "__main__":
    formulaList = csv2Formula(path="/home/mfukuda/pairing_automation_design/python/SQR012345.csv")
    test_formula(formulaList, 24)
