import re
from lib.util import formulaSet

def transform_valuename(transformList: dict, opr: str):
    if "ZERO" in opr:
        return "ZERO"
    for key in transformList.keys():
        if opr == key:
            # transform_used_list.append(key)
            return transformList[key]
    return opr

def remove_extra_formula(formulaList: list[formulaSet]):
    isToAdd = True
    transformList = {}
    negList = {}
    resultList = []
    for formula in formulaList:
        if "ZERO" in formula.opr1 and formula.type == "ADD":
            transformList[formula.ret] = transform_valuename(transformList, formula.opr2)
            continue
        if "ZERO" in formula.opr2 and formula.type == "ADD":
            transformList[formula.ret] = transform_valuename(transformList, formula.opr1)
            continue
        if "ZERO" in formula.opr2 and formula.type == "SUB":
            transformList[formula.ret] = transform_valuename(transformList, formula.opr1)
            continue
        resultList.append(formulaSet(
            opr1=transform_valuename(transformList, formula.opr1), 
            opr2=transform_valuename(transformList, formula.opr2),
            ret=formula.ret, type=formula.type
        ))
    return resultList