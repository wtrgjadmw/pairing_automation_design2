import re

class formulaSet:
    def __init__(self, opr1: str, opr2: str, ret: str, type) -> None:
        self.opr1 = opr1
        self.opr2 = opr2
        self.ret = ret
        self.type = type

def transform_valuename(transformList: dict, opr: str):
    for key in transformList.keys():
        if opr == key:
            # transform_used_list.append(key)
            return transformList[key]
    return opr

def remove_extra_formula(formulaList: list[formulaSet]):
    isToAdd = True
    transformList = {}
    resultList = []
    for formula in formulaList:
        if formula.opr1 == "ZERO" and formula.type == "ADD":
            transformList[formula.ret] = formula.opr2
            continue
        if formula.opr2 == "ZERO" and formula.type == "ADD":
            transformList[formula.ret] = formula.opr1
            continue
        if formula.opr2 == "ZERO" and formula.type == "SUB":
            transformList[formula.ret] = formula.opr1
            continue
        resultList.append(formulaSet(
            opr1=transform_valuename(transformList, formula.opr1), 
            opr2=transform_valuename(transformList, formula.opr2),
            ret=formula.ret, type=formula.type
        ))
    return resultList