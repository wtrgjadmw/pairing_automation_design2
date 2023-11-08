from lib.util import bits_of
from export_formula.transform import *

fp2_qnr = -1

def add(opr1: str, opr2: str, ret: str):
    return [formulaSet(opr1=opr1, opr2=opr2, ret=ret, type="ADD")]


def sub(opr1: str, opr2: str, ret: str):
    return [formulaSet(opr1=opr1, opr2=opr2, ret=ret, type="SUB")]


def mul(opr1: str, opr2: str, ret: str):
    return [formulaSet(opr1=opr1, opr2=opr2, ret=ret, type="MUL")]


def inv(opr1: str, ret: str):
    return [formulaSet(opr1=opr1, opr2=opr1, ret=ret, type="INV")]


def neg(opr1: str, ret: str):
    return [formulaSet(opr1="ZERO", opr2=opr1, ret=ret, type="SUB")]


def constMul(opr1: str, k: int, ret: str):
    # print("-----constMul: {}={}*{}-------------------".format(ret, opr1, k))
    if k == 0:
        raise Exception("ERROR: *0の掛け算です".format(opr1))
    if k == 1:
        return [add(opr1=opr1, opr2="ZERO", ret=ret)]
    formulaList = []
    bits_k = bits_of(abs(k))
    twiceVal = opr1
    tmpVal = "ZERO"
    for i in range(0, len(bits_k) - 1):
        nextTwiceVal = ret + "_twice{}".format(i)
        nextTmpVal = ret + str(i)
        if bits_k[i]:
            formulaList += add(twiceVal, tmpVal, nextTmpVal)
        formulaList += add(twiceVal, twiceVal, nextTwiceVal)
        twiceVal = nextTwiceVal
        tmpVal = nextTmpVal
    if k > 0:
        formulaList += add(twiceVal, tmpVal, ret)
    else:
        negVal = ret + "_neg"
        formulaList += add(twiceVal, tmpVal, negVal)
        formulaList += neg(negVal, ret)
    return formulaList


def guzai(opr1: str, ret: str):
    return constMul(opr1, fp2_qnr, ret)


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
