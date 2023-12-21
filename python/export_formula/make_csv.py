from export_formula.fp12 import fp12_mul, fp12_conj, fp12_frob, fp12_sqr
from export_formula.ep2 import ep2_add, ep2_dbl, fp12_sparse_d6, fp12_sparse_m6, fp12_SQR012345
from export_formula.transform import remove_extra_formula

def printCsv(filename, formulaList):
    write_f = open(filename, 'w')
    formulaList = remove_extra_formula(formulaList)
    for formula in formulaList:
        write_f.write("{},{},{},{}\n".format(formula.ret, formula.opr1, formula.opr2, formula.type))


def fp12_makeCsv():
    printCsv(fp12_conj("a", "b", "c"))
    printCsv(fp12_frob("a", "b", "c"))
    printCsv(fp12_mul("a", "b", "c"))
    printCsv(fp12_sqr("a", "b", "c"))
    printCsv(ep2_dbl())
    printCsv(ep2_add())
    printCsv(fp12_SQR012345())
    printCsv(fp12_sparse_d6())
    printCsv(fp12_sparse_m6())
