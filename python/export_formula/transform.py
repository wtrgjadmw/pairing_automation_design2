import re
from lib.util import formulaSet

def transform_valuename(transformList: dict, opr: str):
    if "ZERO" in opr:
        return "ZERO"
    while True:
        isChanged = False
        for key in transformList.keys():
            if opr == key:
                # transform_used_list.append(key)
                opr = transformList[key]
                isChanged = True
        if not isChanged:
            break
    return opr

def remove_extra_formula(formulaList: list[formulaSet]):
    isToAdd = True
    transformList = {}
    negList = {}
    resultList = []
    for formula in formulaList:
        opr1 = transform_valuename(transformList, formula.opr1)
        opr2 = transform_valuename(transformList, formula.opr2)
        if "ZERO" in opr1 and formula.type == "ADD":
            transformList[formula.ret] = transform_valuename(transformList, opr2)
            continue
        if "ZERO" in opr2 and formula.type == "ADD":
            transformList[formula.ret] = transform_valuename(transformList, opr1)
            continue
        if ("ZERO" in opr1 or "ZERO" in opr2) and formula.type == "MUL":
            transformList[formula.ret] = "ZERO"
            continue
        if "ZERO" in opr2 and formula.type == "SUB":
            transformList[formula.ret] = transform_valuename(transformList, opr1)
            continue
        resultList.append(formulaSet(
            opr1=opr1, 
            opr2=opr2,
            ret=formula.ret, type=formula.type
        ))
    return resultList