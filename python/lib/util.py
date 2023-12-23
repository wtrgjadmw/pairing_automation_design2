import json


def read_json(filename):
    with open(filename, "r") as f:
        dict = json.load(f)
    return dict


def bits_of(k):  # 0, 1
    return [int(c) for c in "{0:b}".format(k)]


def bits_list(a):  # -1, 0, 1
    a_abs = abs(a)
    mask = 0b11
    res = []
    while (a_abs != 0):
        if (a_abs & 1):
            ui = 2 - (a_abs & mask)
            if (ui > 0):
                a_abs -= 1
            else:
                a_abs += 1
            res.append(ui)
        else:
            res.append(0)
        a_abs >>= 1
    if (a < 0):
        res = [-ui for ui in res]
    return res


class FormulaSet:
    def __init__(self, opr1: str, opr2: str, ret: str, type) -> None:
        self.opr1 = opr1
        self.opr2 = opr2
        self.ret = ret
        self.type = type


if __name__ == "__main__":
    print(bits_of(8))
