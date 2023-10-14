from io import TextIOWrapper
from lib.parameters import *

def printFp(a):
    a_str = str(hex(a))
    a_for_veri = str(p_len) + "'h" + a_str[2:]
    print(a_for_veri)


def file_printFp(f: TextIOWrapper, a: int):
    a_str = str(hex(a))
    a_for_veri = str(p_len) + "'h" + a_str[2:] + "\n"
    f.write(a_for_veri)

def MontConvFp2(a):
    return [MontConv(a[0]), MontConv(a[1])]

def MontConvInvFp2(a):
    return [MontConvInv(a[0]), MontConvInv(a[1])]

def MontConvFp4(a):
    return [MontConvFp2(a[0]), MontConvFp2(a[1])]

def MontConvInvFp4(a):
    return [MontConvInvFp2(a[0]), MontConvInvFp2(a[1])]

def MontConvFp12(a):
    return [MontConvFp4(a[0]), MontConvFp4(a[1]), MontConvFp4(a[2])]

def MontConvInvFp12(a):
    return [MontConvInvFp4(a[0]), MontConvInvFp4(a[1]), MontConvInvFp4(a[2])]

def MontConvFp24(a):
    return [MontConvFp12(a[0]), MontConvFp12(a[1])]

def MontConvInvFp24(a):
    return [MontConvInvFp12(a[0]), MontConvInvFp12(a[1])]

def printFp2(a):
    printFp(a[0])
    printFp(a[1])


def printFp4(a):
    printFp2(a[0])
    printFp2(a[1])
    print()


def printFp12(a):
    printFp4(a[0])
    printFp4(a[1])
    printFp4(a[2])


def printFp24(a):
    printFp12(a[0])
    printFp12(a[1])


def make_define_Fp2(f: TextIOWrapper, name, a): # name: variable name , a: Fp4 variable
    f.write("`define " + name + "0 ")
    file_printFp(f, a[0])
    f.write("`define " + name + "1 ")
    file_printFp(f, a[1])
    f.write("\n")

def make_define_Fp4(f: TextIOWrapper, name, a): # name: variable name , a: Fp4 variable
    f.write("`define " + name + "00 ")
    file_printFp(f, a[0][0])
    f.write("`define " + name + "01 ")
    file_printFp(f, a[0][1])
    f.write("`define " + name + "10 ")
    file_printFp(f, a[1][0])
    f.write("`define " + name + "11 ")
    file_printFp(f, a[1][1])
    f.write("\n")
