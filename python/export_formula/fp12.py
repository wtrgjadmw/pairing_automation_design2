from export_formula.fp2 import fp2_add, fp2_neg, fp2_conj, fp2_mul
from export_formula.fp4 import fp4_add, fp4_sub, fp4_neg, fp4_mul, fp4_guzai, fp4_inv, fp4_constMul, fp4_sqr
from export_formula.transform import remove_extra_formula

def fp12_add(opr1: str, opr2: str, ret: str):
    return fp4_add(opr1+'0', opr2+'0', ret+'0') + fp4_add(opr1+'1', opr2+'1', ret+'1') + fp4_add(opr1+'2', opr2+'2', ret+'2')

def fp12_sub(opr1: str, opr2: str, ret: str):
    return fp4_sub(opr1+'0', opr2+'0', ret+'0') + fp4_sub(opr1+'1', opr2+'1', ret+'1') + fp4_sub(opr1+'2', opr2+'2', ret+'2')

def fp12_constMul(opr1: str, k: int, ret: str):
    return fp4_constMul(opr1+'0', k, ret+'0') + fp4_constMul(opr1+'1', k, ret+'1') + fp4_constMul(opr1+'2', k, ret+'2')

def fp12_mul(opr1: str, opr2: str, ret: str):
    formulaList = fp4_mul(opr1+'0', opr2+'0', ret+"_t0")
    formulaList += fp4_mul(opr1+'1', opr2+'1', ret+"_t1")
    formulaList += fp4_mul(opr1+'2', opr2+'2', ret+"_t2")
    formulaList += fp4_add(opr1+'0', opr1+'1', ret+"_t30")
    formulaList += fp4_add(opr2+'0', opr2+'1', ret+"_t31")
    formulaList += fp4_mul(ret+"_t30", ret+"_t31", ret+"_t3")
    formulaList += fp4_add(opr1+'1', opr1+'2', ret+"_t40")
    formulaList += fp4_add(opr2+'1', opr2+'2', ret+"_t41")
    formulaList += fp4_mul(ret+"_t40", ret+"_t41", ret+"_t4")
    formulaList += fp4_add(opr1+'2', opr1+'0', ret+"_t50")
    formulaList += fp4_add(opr2+'2', opr2+'0', ret+"_t51")
    formulaList += fp4_mul(ret+"_t50", ret+"_t51", ret+"_t5")
    formulaList += fp4_add(ret+'_t0', ret+'_t1', ret+"_t60")
    formulaList += fp4_sub(ret+'_t3', ret+'_t60', ret+"_t6")
    formulaList += fp4_add(ret+'_t1', ret+'_t2', ret+"_t70")
    formulaList += fp4_sub(ret+'_t4', ret+'_t70', ret+"_t71")
    formulaList += fp4_guzai(ret+'_t71', ret+"_t7")
    formulaList += fp4_add(ret+'_t0', ret+'_t7', ret+"0")
    formulaList += fp4_add(ret+'_t2', ret+'_t0', ret+"_t80")
    formulaList += fp4_sub(ret+'_t5', ret+'_t80', ret+"_t8")
    formulaList += fp4_guzai(ret+'_t2', ret+"_t9")
    formulaList += fp4_add(ret+'_t6', ret+'_t9', ret+"1")
    formulaList += fp4_add(ret+'_t1', ret+'_t8', ret+"2")
    return formulaList

def fp12_sqr(opr1: str, ret: str):
    formulaList = fp4_sqr(opr1+'0', ret+"_t0")
    formulaList += fp4_sqr(opr1+'1', ret+"_t1")
    formulaList += fp4_sqr(opr1+'2', ret+"_t2")
    formulaList += fp4_add(opr1+'0', opr1+'1', ret+"_t30")
    formulaList += fp4_sqr(ret+"_t30", ret+"_t3")
    formulaList += fp4_add(opr1+'1', opr1+'2', ret+"_t40")
    formulaList += fp4_sqr(ret+"_t40", ret+"_t4")
    formulaList += fp4_add(opr1+'2', opr1+'0', ret+"_t40")
    formulaList += fp4_sqr(ret+"_t40", ret+"_t4")
    formulaList += fp4_add(ret+"_t0", ret+"_t1", ret+"_s00")
    formulaList += fp4_sub(ret+"_t3", ret+"_s00", ret+"_s0")
    formulaList += fp4_add(ret+"_t1", ret+"_t2", ret+"_s10")
    formulaList += fp4_sub(ret+"_t4", ret+"_s10", ret+"_s11")
    formulaList += fp4_add(ret+"_t2", ret+"_t0", ret+"_s20")
    formulaList += fp4_sub(ret+"_t5", ret+"_s20", ret+"_s2")
    formulaList += fp4_guzai(ret+"_s11", ret+"_s1")
    formulaList += fp4_guzai(ret+"_t2", ret+"_t6")
    formulaList += fp4_add(ret+"_t0", ret+"_s1", ret+"0")
    formulaList += fp4_add(ret+"_s0", ret+"_t6", ret+"1")
    formulaList += fp4_add(ret+"_t1", ret+"_s2", ret+"2")
    return formulaList

def fp12_conj(opr1: str, ret: str):
    formulaList = fp2_add(opr1+'00', "ZERO", ret+'00')
    formulaList += fp2_neg(opr1+'01', ret+'01')
    formulaList += fp2_neg(opr1+'10', ret+'10')
    formulaList += fp2_add(opr1+'11', "ZERO", ret+'11')
    formulaList += fp2_add(opr1+'20', "ZERO", ret+'20')
    formulaList += fp2_neg(opr1+'21', ret+'21')
    return formulaList

def fp12_inv(opr1: str, ret: str):
    formulaList = fp4_sqr(opr1+'0', ret+"_aa")
    formulaList += fp4_sqr(opr1+'1', ret+"_bb")
    formulaList += fp4_sqr(opr1+'2', ret+"_cc")
    formulaList += fp4_mul(opr1+'0', opr1+'1', ret+"_ab")
    formulaList += fp4_mul(opr1+'1', opr1+'2', ret+"_bc")
    formulaList += fp4_mul(opr1+'2', opr1+'0', ret+"_ac")
    formulaList += fp4_guzai(ret+"_bc", ret+"_bcxi")
    formulaList += fp4_sub(ret+'_aa', ret+'_bcxi', ret+"_pa")
    formulaList += fp4_guzai(ret+"_cc", ret+"_ccxi")
    formulaList += fp4_sub(ret+'_ccxi', ret+'_ab', ret+"_pb")
    formulaList += fp4_sub(ret+'_bb', ret+'_ac', ret+"_pc")
    formulaList += fp4_mul(ret+'_pb', opr1+'2', ret+"_pbc")
    formulaList += fp4_mul(ret+'_pc', opr1+'1', ret+"_pcb")
    formulaList += fp4_add(ret+'_pbc', ret+"_pcb", ret+"_pbccb")
    formulaList += fp4_guzai(ret+"_pbccb", ret+"_pxi")
    formulaList += fp4_mul(ret+'_pa', opr1+'0', ret+"_paa")
    formulaList += fp4_add(ret+'_pxi', ret+'_paa', ret+"_q")
    formulaList += fp4_inv(ret+'_q', ret+"_qinv")
    formulaList += fp4_mul(ret+'_pa', ret+"_qinv", ret+"0")
    formulaList += fp4_mul(ret+'_pb', ret+"_qinv", ret+"1")
    formulaList += fp4_mul(ret+'_pc', ret+"_qinv", ret+"2")
    return formulaList

def fp12_neg(opr1: str, ret: str):
    return fp4_neg(opr1+'0', ret+'0') + fp4_neg(opr1+'1', ret+'1') + fp4_neg(opr1+'2', ret+'2')

# (ret: Fp12) = (opr1: Fp12) * w
def fp12_guzai(opr1: str, ret: str):  # Fp24 = Fp12[z]/(z^3 - w)
    formulaList = fp4_guzai(opr1+"2", ret+"0")
    formulaList += fp4_add(opr1+"0", "ZERO", ret+"1")
    formulaList += fp4_add(opr1+"1", "ZERO", ret+"2")
    return formulaList

def fp12_exp(opr1: str, x: int, ret: str):
    twiceVal = opr1
    tmpVal = "ONE"
    formulaList = []
    i = 0
    while x > 0:
        nextTwiceVal = ret + "_twice{}".format(i)
        nextTmpVal = ret + str(i)
        if x & 1:
            formulaList += fp12_mul(twiceVal, tmpVal, nextTmpVal)
        x >>= 1
        i += 1
        formulaList += fp12_mul(twiceVal, twiceVal, nextTwiceVal)
    formulaList[-1].ret = ret
    return formulaList

def fp12_frob(opr1, ret):
    formulaList = fp2_conj(opr1+"10", ret+"_f10")
    formulaList += fp2_conj(opr1+"20", ret+"_f12")
    formulaList += fp2_conj(opr1+"01", ret+"_f01")
    formulaList += fp2_conj(opr1+"11", ret+"_f11")
    formulaList += fp2_conj(opr1+"21", ret+"_f21")
    formulaList += fp2_conj(opr1+"00", ret+"00")
    formulaList += fp2_mul(ret+"_f10", "XI1", ret+"10")
    formulaList += fp2_mul(ret+"_f20", "XI2", ret+"20")
    formulaList += fp2_mul(ret+"_f01", "XI3", ret+"01")
    formulaList += fp2_mul(ret+"_f11", "XI4", ret+"11")
    formulaList += fp2_mul(ret+"_f21", "XI5", ret+"21")
    return formulaList

if __name__ == "__main__":
    formulaList = fp12_mul("a", "b", "c")
    formulaList = remove_extra_formula(formulaList)
    for formula in formulaList:
        print("{},{},{},{}".format(formula.ret, formula.opr1, formula.opr2, formula.type))