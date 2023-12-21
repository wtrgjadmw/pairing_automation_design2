from export_formula.fp import add, sub, neg, mul, guzai, inv, constMul
from lib.parameters import fp4_qnr
from export_formula.transform import remove_extra_formula

def fp2_add(opr1: str, opr2: str, ret: str):

    return add(opr1+'0', opr2+'0', ret+'0') + add(opr1+'1', opr2+'1', ret+'1')

def fp2_sub(opr1: str, opr2: str, ret: str):
    return sub(opr1+'0', opr2+'0', ret+'0') + sub(opr1+'1', opr2+'1', ret+'1')

def fp2_constMul(opr1: str, k: int, ret: str):
    return constMul(opr1+'0', k, ret+'0') + constMul(opr1+'1', k, ret+'1')

def fp2_constMulNotMont(opr1: str, opr2: int, ret: str):
    return mul(opr1+'0', opr2, ret+'0') + mul(opr1+'1', opr2, ret+'1')

def fp2_mul(opr1: str, opr2: str, ret: str):
    formulaList = []
    formulaList += mul(opr1+'0', opr2+'0', ret+"_t0")
    formulaList += mul(opr1+'1', opr2+'1', ret+"_t1")
    formulaList += add(opr1+'0', opr1+'1', ret+"_t2")
    formulaList += add(opr2+'0', opr2+'1', ret+"_t3")
    formulaList += mul(ret+"_t2", ret+"_t3", ret+"_t4")
    formulaList += guzai(ret+"_t1", ret+"_s0")
    formulaList += add(ret+"_t0", ret+"_s0", ret+"0")
    formulaList += add(ret+"_t0", ret+"_t1", ret+"_t5")
    formulaList += sub(ret+"_t4", ret+"_t5", ret+"1")
    return formulaList

def fp2_sqr(opr1: str, ret: str):
    formulaList = []
    formulaList += guzai(opr1+'1', ret+"_a1_")
    formulaList += add(opr1+'0', ret+"_a1_", ret+"_t0")
    formulaList += add(opr1+'0', opr1+'1', ret+"_t1")
    formulaList += mul(ret+"_t0", ret+"_t1", ret+"_t2")
    formulaList += mul(opr1+'0', opr1+'1', ret+"_t3")
    formulaList += guzai(ret+"_t3", ret+"_t4")
    formulaList += add(ret+"_t3", ret+"_t4", ret+"_t5")
    formulaList += sub(ret+"_t2", ret+"_t5", ret+"0")
    formulaList += add(ret+"_t3", ret+"_t3", ret+"1")
    return formulaList

def fp2_conj(opr1: str, ret: str):
    return add(opr1+'0', "ZERO", ret+'0') + neg(opr1+'1', ret+'1')

def fp2_inv(opr1: str, ret: str):
    formulaList = []
    formulaList += fp2_conj(opr1, ret+'_a_')
    formulaList += fp2_mul(opr1, ret+'_a_', ret+"_aa_")
    formulaList += inv(ret+"_aa_0", ret+"_s")
    formulaList += mul(ret+'_a_0', ret+'_s', ret+"0")
    formulaList += mul(ret+'_a_1', ret+'_s', ret+"1")
    return formulaList

def fp2_neg(opr1: str, ret: str):
    return neg(opr1+'0', ret+'0') + neg(opr1+'1', ret+'1')

# (ret: Fp2) = (opr1: Fp2) * fp4_qnr
def fp2_guzai(opr1: str, ret: str):  # Fp4 = Fp2[v]/(v^2 - fp4_qnr), fp4_qnr = x + yi
    formulaList = []
    formulaList += fp2_constMul(opr1, fp4_qnr[0], ret+"_x")
    formulaList += fp2_constMul(opr1, fp4_qnr[1], ret+"_y")
    formulaList += guzai(ret+"_y1", ret+"_y1_")
    formulaList += add(ret+"_x0", ret+"_y1_", ret+"0")
    formulaList += add(ret+"_x1", ret+"_y0", ret+"1")
    return formulaList

def fp2_exp(opr1: str, x: int, ret: str):
    twiceVal = opr1
    tmpVal = "ONE"
    formulaList = []
    i = 0
    while x > 0:
        nextTwiceVal = ret + "_twice{}".format(i)
        nextTmpVal = ret + str(i)
        if x & 1:
            formulaList += fp2_mul(twiceVal, tmpVal, nextTmpVal)
        x >>= 1
        i += 1
        formulaList += fp2_mul(twiceVal, twiceVal, nextTwiceVal)
    formulaList[-1].ret = ret
    return formulaList

if __name__ == "__main__":
    formulaList = fp2_mul("a", "b", "c")
    formulaList = remove_extra_formula(formulaList)
    for formula in formulaList:
        print("{},{},{},{}".format(formula.ret, formula.opr1, formula.opr2, formula.type))