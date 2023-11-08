from export_formula.fp2 import fp2_add, fp2_sub, fp2_neg, fp2_mul, fp2_guzai, fp2_inv, fp2_constMul, fp2_conj
from export_formula.transform import *

fp4_qnr = [1, 1]

def fp4_add(opr1: str, opr2: str, ret: str):
    return fp2_add(opr1+'0', opr2+'0', ret+'0') + fp2_add(opr1+'1', opr2+'1', ret+'1')


def fp4_sub(opr1: str, opr2: str, ret: str):
    return fp2_sub(opr1+'0', opr2+'0', ret+'0') + fp2_sub(opr1+'1', opr2+'1', ret+'1')


def fp4_constMul(opr1: str, k: int, ret: str):
    return fp2_constMul(opr1+'0', k, ret+'0') + fp2_constMul(opr1+'1', k, ret+'1')


def fp4_mul(opr1: str, opr2: str, ret: str):
    formulaList = []
    formulaList += fp2_mul(opr1+'0', opr2+'0', ret+"_t0")
    formulaList += fp2_mul(opr1+'1', opr2+'1', ret+"_t1")
    formulaList += fp2_add(opr1+'0', opr1+'1', ret+"_t2")
    formulaList += fp2_add(opr2+'0', opr2+'1', ret+"_t3")
    formulaList += fp2_mul(ret+"_t2", ret+"_t3", ret+"_t4")
    formulaList += fp2_guzai(ret+"_t1", ret+"_s0")
    formulaList += fp2_add(ret+"_t0", ret+"_s0", ret+"0")
    formulaList += fp2_add(ret+"_t0", ret+"_t1", ret+"_t5")
    formulaList += fp2_sub(ret+"_t4", ret+"_t5", ret+"1")
    return formulaList

def fp4_sqr(opr1: str, ret: str):
    formulaList = []
    formulaList += fp2_guzai(opr1+'1', ret+"_a1_")
    formulaList += fp2_add(opr1+'0', ret+"_a1_", ret+"_t0")
    formulaList += fp2_add(opr1+'0', opr1+'1', ret+"_t1")
    formulaList += fp2_mul(ret+"_t0", ret+"_t1", ret+"_t2")
    formulaList += fp2_mul(opr1+'0', opr1+'1', ret+"_t3")
    formulaList += fp2_guzai(ret+"_t3", ret+"_t4")
    formulaList += fp2_add(ret+"_t3", ret+"_t4", ret+"_t5")
    formulaList += fp2_sub(ret+"_t2", ret+"_t5", ret+"0")
    formulaList += fp2_add(ret+"_t3", ret+"_t3", ret+"1")
    return formulaList

def fp4_conj(opr1: str, ret: str):
    return fp2_add(opr1+'0', "ZERO", ret+'0') + fp2_neg(opr1+'1', ret+'1')


def fp4_inv(opr1: str, ret: str):
    formulaList = []
    formulaList += fp4_conj(opr1, ret+'_a_')
    formulaList += fp4_mul(opr1, ret+'_a_', ret+"_aa_")
    formulaList += fp2_inv(ret+"_aa_0", ret+"_s")
    formulaList += fp2_mul(ret+'_a_0', ret+'_s', ret+"0")
    formulaList += fp2_mul(ret+'_a_1', ret+'_s', ret+"1")
    return formulaList

def fp4_neg(opr1: str, ret: str):
    return fp2_neg(opr1+'0', ret+'0') + fp2_neg(opr1+'1', ret+'1')

def fp4_guzai(opr1: str, ret: str):  # qnr = x + yi
    x0Val, x1Val, y0Val, y1Val = "ZERO", "ZERO", "ZERO", "ZERO"
    formulaList = []
    for i in range(fp4_qnr[0]):
        nextX0Val = ret+"_x0{}".format(i)
        nextX1Val = ret+"_x1{}".format(i)
        formulaList += fp2_add(x0Val, opr1+'0', nextX0Val)
        formulaList += fp2_add(x1Val, opr1+'0', nextX1Val)
        x0Val = nextX0Val
        x1Val = nextX1Val
    for i in range(fp4_qnr[1]):
        nextY0Val = ret+"_y0{}".format(i)
        nextY1Val = ret+"_y1{}".format(i)
        formulaList += fp2_add(y0Val, opr1+'0', nextY0Val)
        formulaList += fp2_add(y1Val, opr1+'0', nextY1Val)
        y0Val = nextY0Val
        y1Val = nextY1Val
    formulaList += fp2_guzai(y1Val, ret+"_y1_")
    formulaList += fp2_add(x0Val, ret+"_y1_", ret+"0")
    formulaList += fp2_add(x1Val, y0Val, ret+"1")
    return formulaList

def fp4_exp(opr1: str, x: int, ret: str):
    twiceVal = opr1
    tmpVal = "ONE"
    formulaList = []
    i = 0
    while x > 0:
        nextTwiceVal = ret + "_twice{}".format(i)
        nextTmpVal = ret + str(i)
        if x & 1:
            formulaList += fp4_mul(twiceVal, tmpVal, nextTmpVal)
        x >>= 1
        i += 1
        formulaList += fp4_mul(twiceVal, twiceVal, nextTwiceVal)
    formulaList[-1].ret = ret
    return formulaList

def fp4_frob(opr1: str, ret: str):
    formulaList = fp2_conj(opr1+"0", ret+"0")
    formulaList += fp2_conj(opr1+"1", ret+"1_")
    formulaList += fp2_conj(ret+"1_", ret+"1")
    return formulaList

if __name__ == "__main__":
    formulaList = fp4_mul("a", "b", "c")
    formulaList = remove_extra_formula(formulaList)
    for formula in formulaList:
        print("{},{},{},{}".format(formula.ret, formula.opr1, formula.opr2, formula.type))
        # print(formula)