from export_formula.fp import sub
from export_formula.fp2 import fp2_mul, fp2_sub, fp2_add, fp2_sqr, fp2_neg, fp2_constMul, fp2_guzai
from export_formula.transform import FormulaOrganizer


def ep2_dbl():
    formulaList = fp2_sqr("yt", "t0")
    formulaList += fp2_sqr("zt", "t1")
    formulaList += fp2_mul("b_t", "t1", "t2")
    formulaList += fp2_add("t2", "t2", "t3")
    formulaList += fp2_add("t3", "t2", "t4")
    formulaList += fp2_mul("xt", "yt", "t5")
    formulaList += fp2_add("t5", "t5", "t6")
    formulaList += fp2_sqr("xt", "t7")
    formulaList += fp2_add("t7", "t7", "t8")
    formulaList += fp2_add("t8", "t7", "t9")
    formulaList += fp2_mul("yt", "zt", "t10")
    formulaList += fp2_add("t10", "t10", "t11")
    formulaList += fp2_mul("t0", "t11", "t12")
    formulaList += fp2_add("t12", "t12", "t13")
    formulaList += fp2_add("t13", "t13", "new_zt")
    formulaList += fp2_sub("t0", "t4", "l01")
    formulaList += fp2_add("t4", "t4", "t14")
    formulaList += fp2_sub("l01", "t14", "t15")
    formulaList += fp2_mul("t15", "t6", "new_xt")
    formulaList += fp2_add("t0", "l01", "t16")
    formulaList += fp2_add("t14", "t4", "b3")
    formulaList += fp2_mul("b3", "t16", "t17")
    formulaList += fp2_sqr("t0", "t18")
    formulaList += fp2_add("t17", "t18", "new_yt")
    formulaList += fp2_constMul("t11", "yp", "l00")
    formulaList += fp2_constMul("t9", "xp", "l10")
    return formulaList


def ep2_add():
    formulaList = fp2_mul("yq", "zt", "t0")
    formulaList += fp2_sub("yt", "t0", "t1")
    formulaList += fp2_mul("xq", "zt", "t2")
    formulaList += fp2_sub("xt", "t2", "t3")
    formulaList += fp2_sqr("t1", "t4")
    formulaList += fp2_sqr("t3", "t5")
    formulaList += fp2_mul("t3", "t5", "t6")
    formulaList += fp2_mul("zt", "t4", "t7")
    formulaList += fp2_add("t6", "t7", "t8")
    formulaList += fp2_mul("xt", "t5", "t9")
    formulaList += fp2_add("t9", "t9", "t10")
    formulaList += fp2_sub("t8", "t10", "t11")
    formulaList += fp2_sub("t11", "t9", "t12")
    formulaList += fp2_mul("t3", "t11", "new_xt")
    formulaList += fp2_mul("t1", "t12", "t13")
    formulaList += fp2_mul("yt", "t6", "t14")
    formulaList += fp2_add("t13", "t14", "t15")
    formulaList += fp2_neg("t13", "new_yt")
    formulaList += fp2_mul("zt", "t6", "new_zt")
    formulaList += fp2_constMul("t3", "yp", "l00")
    formulaList += fp2_constMul("t1", "xp", "l10")
    formulaList += fp2_mul("yq", "t3", "t16")
    formulaList += fp2_mul("xq", "t1", "t17")
    formulaList += fp2_sub("t16", "t17", "l01")
    return formulaList


def fp12_SQR012345(opr1: str, ret: str):
    formulaList = fp2_sqr(opr1 + "00", "t0")
    formulaList += fp2_add(opr1 + "00", opr1 + "11", "t1")
    formulaList += fp2_sub("t1", opr1 + "20", "t2")
    formulaList += fp2_add("t1", opr1 + "20", "t8")
    formulaList += fp2_sqr("t8", "t9")
    formulaList += fp2_sqr("t2", "t10")
    formulaList += fp2_mul(opr1 + "11", opr1 + "20", "t3")
    formulaList += fp2_add("t3", "t3", "t11")
    formulaList += fp2_sqr(opr1 + "11", "t4")
    formulaList += fp2_mul(opr1 + "00", opr1 + "01", "t5")
    formulaList += fp2_mul(opr1 + "20", opr1 + "21", "t6")
    formulaList += fp2_mul(opr1 + "10", opr1 + "11", "t7")
    formulaList += fp2_guzai("t11", "t12")
    formulaList += fp2_add("t0", "t12", "t13")
    formulaList += sub("t130", "ONE", "t140")
    formulaList += sub("t131", "ZERO", "t141")
    formulaList += fp2_add("t13", "t14", ret + "00")
    formulaList += fp2_add("t5", "t5", "t29")
    formulaList += fp2_add("t29", "t5", "t30")
    formulaList += fp2_add("t30", opr1 + "01", "t31")
    formulaList += fp2_add("t31", "t31", ret + "01")
    formulaList += fp2_add("t0", "t4", "t15")
    formulaList += fp2_add("t15", "t15", "t16")
    formulaList += fp2_sub("t9", "t16", "t17")
    formulaList += fp2_add("t10", "t17", ret + "11")
    formulaList += fp2_guzai("t4", "t18")
    formulaList += fp2_sub("t18", "t11", "t19")
    formulaList += fp2_add("t19", "t19", "t20")
    formulaList += fp2_add("t20", "t9", "t21")
    formulaList += fp2_sub("t21", "t10", ret + "20")
    formulaList += fp2_add("t6", "t6", "t22")
    formulaList += fp2_add("t22", "t6", "t23")
    formulaList += fp2_guzai("t23", "t24")
    formulaList += fp2_add(opr1 + "10", "t24", "t25")
    formulaList += fp2_add("t25", "t25", ret + "10")
    formulaList += fp2_add("t7", "t7", "t26")
    formulaList += fp2_add("t26", "t7", "t27")
    formulaList += fp2_add("t27", opr1 + "21", "t28")
    formulaList += fp2_add("t28", "t28", ret + "21")
    return formulaList


def Fp2SparseMul(a0, a1, b0, b1, b2, ret):
    formulaList = fp2_mul(a0, b0, ret + "_t0")
    formulaList += fp2_mul(a1, b1, ret + "_t1")
    formulaList += fp2_mul(a1, b2, ret + "_t2")
    formulaList += fp2_guzai(ret + "_t2", ret + "_t10")
    formulaList += fp2_add(ret + "_t0", ret + "_t10", ret + "0")
    formulaList += fp2_add(a0, a1, ret + "_t4")
    formulaList += fp2_add(b0, b1, ret + "_t5")
    formulaList += fp2_mul(ret + "_t4", ret + "_t5", ret + "_t6")
    formulaList += fp2_add(ret + "_t0", ret + "_t1", ret + "_t7")
    formulaList += fp2_sub(ret + "_t6", ret + "_t7", ret + "1")
    formulaList += fp2_mul(a0, b2, ret + "_t8")
    formulaList += fp2_add(ret + "_t8", ret + "_t1", ret + "2")
    return formulaList


def fp12_sparse_m6(opr1: str, opr2: str, ret: str):  # opr1: line evaluation
    formulaList = fp2_mul(opr1 + "01", opr2 + "10", "t1")
    formulaList += fp2_mul(opr1 + "01", opr2 + "01", "t2")
    formulaList += fp2_mul(opr1 + "01", opr2 + "21", "t0")
    formulaList += fp2_guzai("t0", "t3")
    formulaList += Fp2SparseMul(opr1 + "00", opr1 + "20", opr2 + "00", opr2 + "20", opr2 + "11", "t4")
    formulaList += fp2_add(opr1 + "20", opr1 + "01", "t7")
    formulaList += fp2_add(opr2 + "00", opr2 + "10", "t8")
    formulaList += fp2_add(opr2 + "20", opr2 + "01", "t9")
    formulaList += fp2_add(opr2 + "11", opr2 + "21", "t10")
    formulaList += Fp2SparseMul(opr1 + "00", "t7", "t8", "t9", "t10", "t5")
    formulaList += fp2_add("t3", "t40", "t14")
    formulaList += fp2_add("t1", "t41", "t15")
    formulaList += fp2_add("t2", "t42", "t16")
    formulaList += fp2_sub("t50", "t14", ret + "10")
    formulaList += fp2_sub("t51", "t15", ret + "01")
    formulaList += fp2_sub("t52", "t16", ret + "21")
    formulaList += fp2_guzai("t2", "t17")
    formulaList += fp2_add("t17", "t40", ret + "00")
    formulaList += fp2_add("t3", "t41", ret + "20")
    formulaList += fp2_add("t1", "t42", ret + "11")
    return formulaList


def fp12_sparse_d6(opr1: str, opr2: str, ret: str):  # opr1: line evaluation
    formulaList = fp2_mul(opr1 + "00", opr2 + "00", "t0")
    formulaList += fp2_mul(opr1 + "00", opr2 + "20", "t1")
    formulaList += fp2_mul(opr1 + "00", opr2 + "11", "t2")
    formulaList += Fp2SparseMul(opr1 + "10", opr1 + "01", opr2 + "10", opr2 + "01", opr2 + "21", "t4")
    formulaList += fp2_add(opr1 + "00", opr1 + "10", "t7")
    formulaList += fp2_add(opr2 + "00", opr2 + "10", "t8")
    formulaList += fp2_add(opr2 + "20", opr2 + "01", "t9")
    formulaList += fp2_add(opr2 + "11", opr2 + "21", "t10")
    formulaList += Fp2SparseMul("t7", opr1 + "01", "t8", "t9", "t10", "t5")
    formulaList += fp2_add("t0", "t40", "t14")
    formulaList += fp2_add("t1", "t41", "t15")
    formulaList += fp2_add("t2", "t42", "t16")
    formulaList += fp2_sub("t50", "t14", ret + "10")
    formulaList += fp2_sub("t51", "t15", ret + "01")
    formulaList += fp2_sub("t52", "t16", ret + "21")
    formulaList += fp2_guzai("t42", "t17")
    formulaList += fp2_add("t0", "t17", ret + "00")
    formulaList += fp2_add("t1", "t40", ret + "20")
    formulaList += fp2_add("t2", "t41", ret + "11")
    return formulaList


if __name__ == "__main__":
    formulaList = fp12_SQR012345()
    organizer = FormulaOrganizer()
    formulaList = organizer.remove_extra_formula(formulaList)
    for formula in formulaList:
        print(
            "{},{},{},{}".format(
                formula.ret,
                formula.opr1,
                formula.opr2,
                formula.type))
