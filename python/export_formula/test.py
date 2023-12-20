import csv
from lib.fpx import Fp_t, Fp2_t, Fp4_t, Fp12_t, Fp24_t
from lib.util import formulaSet

def csv2Formula(path):
    f = open(path, "r")
    formulaList = []
    for line in csv.reader(f):
        formulaList.append(formulaSet(ret=line[0], opr1=line[1], opr2=line[2], type=line[3]))
    return formulaList

def test_formula(formulaList: list, p: int, k: int):
    valueList = {}
    # initialize
    Fp = Fp_t(p=p)
    Fp2 = Fp2_t(Fp=Fp, qnr=-1)
    Fp4 = Fp4_t(Fp2=Fp2, qnr=[1, 1])
    Fp12 = Fp12_t(Fp4=Fp4, cnr=[[0, 0], [1, 0]])
    Fp24 = Fp24_t(Fp12=Fp12, qnr=[[[0, 0], [0, 0]], [[1, 0], [0, 0]]])
    valueList["ZERO"] = Fp.zero()
    valueList["ONE"] = Fp.one()
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

    # calculate
    for formula in formulaList:
        if formula.type == "ADD":
            valueList[formula.ret] = Fp.add(valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "SUB":
            valueList[formula.ret] = Fp.sub(valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "MUL":
            valueList[formula.ret] = Fp.mul(valueList[formula.opr1], valueList[formula.opr2])
        elif formula.type == "INV":
            valueList[formula.ret] = Fp.inv(valueList[formula.opr1], valueList[formula.opr2])

    # check result
    if k == 2:
        c = Fp2.mul(a, b)
        for i in range(2):
            if valueList['c{}'.format(i)] != c[i]:
                print("Error: this formula has some error;")
                return            
    elif k == 4:
        c = Fp4.mul(a, b)
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
        c = Fp24.mul(a, b)
        for n in range(2):
            for m in range(3):
                for j in range(2):
                    for i in range(2):
                        if valueList['c{}{}{}{}'.format(n, m, j, i)] != c[n][m][j][i]:
                            print("Error: this formula has some error;")
                            return
    print("Success!")


if __name__ == "__main__":
    formulaList = csv2Formula(path="/home/mfukuda/pairing_automation_design/python/M12.csv")
    # bls12-381
    u = -(2**63 + 2**62 + 2**60 + 2**57 + 2**48 + 2**16)
    # bls12
    r = u**4 - u**2 + 1
    p = (((u-1)**2) * r) // 3 + u
    test_formula(formulaList, p, 12)

    # formulaList = csv2Formula(path="/home/mfukuda/pairing_automation_design/python/M24.csv")
    # # bls24-317 
    # u = 2**31 + 2**30 + 2**28 + 2**27 + 2**24 + 2**16 + 2**15
    # # bls24
    # r = u**8 - u**4 + 1
    # n = (((u-1)**2) * r) // 3
    # p = n + u
    # test_formula(formulaList, p, 24)
