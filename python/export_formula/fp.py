from lib.util import bits_of, FormulaSet
from lib.parameters import fp2_qnr
from export_formula.transform import *


def add(opr1: str, opr2: str, ret: str):
    return [FormulaSet(opr1=opr1, opr2=opr2, ret=ret, type="ADD")]


def sub(opr1: str, opr2: str, ret: str):
    return [FormulaSet(opr1=opr1, opr2=opr2, ret=ret, type="SUB")]


def mul(opr1: str, opr2: str, ret: str):
    return [FormulaSet(opr1=opr1, opr2=opr2, ret=ret, type="MUL")]


def inv(opr1: str, ret: str):
    return [FormulaSet(opr1=opr1, opr2=opr1, ret=ret, type="INV")]


def neg(opr1: str, ret: str):
    return [FormulaSet(opr1="ZERO", opr2=opr1, ret=ret, type="SUB")]


def constMulNotMont(opr1: str, k: int, ret: str):
    # print("-----constMul: {}={}*{}-------------------".format(ret, opr1, k))
    if k == 0:
        raise ValueError("*ZERO")
    formulaList = []
    bits_k = bits_of(abs(k))
    twiceVal = opr1
    tmpVal = "ZERO"
    for i in range(0, len(bits_k) - 1):
        nextTwiceVal = ret + "_twice{}".format(i)
        nextTmpVal = ret + str(i)
        if bits_k[i]:
            formulaList += add(twiceVal, tmpVal, nextTmpVal)
            tmpVal = nextTmpVal
        formulaList += add(twiceVal, twiceVal, nextTwiceVal)
        twiceVal = nextTwiceVal
    if k > 0:
        formulaList += add(twiceVal, tmpVal, ret)
    else:
        negVal = ret + "_neg"
        formulaList += add(twiceVal, tmpVal, negVal)
        formulaList += neg(negVal, ret)
    return formulaList

# (ret: Fp) = (opr1: Fp) * fp2_qnr


def guzai(opr1: str, ret: str):  # Fp2 = Fp[i]/(i^2 - fp2_qnr)
    return constMulNotMont(opr1, fp2_qnr, ret)


def exp(opr1: str, x: int, ret: str):
    twiceVal = opr1
    tmpVal = "ONE"
    formulaList = []
    i = 0
    while x > 0:
        nextTwiceVal = ret + "_twice{}".format(i)
        nextTmpVal = ret + str(i)
        if x & 1:
            formulaList += mul(twiceVal, tmpVal, nextTmpVal)
        x >>= 1
        i += 1
        formulaList += mul(twiceVal, twiceVal, nextTwiceVal)
    formulaList[-1].ret = ret
    return formulaList


if __name__ == "__main__":
    formulaList = constMulNotMont("x", 13, "y")
    for formula in formulaList:
        print("{},{},{},{}".format(formula.ret,
              formula.opr1, formula.opr2, formula.type))
