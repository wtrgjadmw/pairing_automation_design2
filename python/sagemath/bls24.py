from sage.all_cmdline import *  # import sage library

from sage.rings.integer_ring import ZZ  # 整数
from sage.rings.rational_field import QQ  # 有理数
from sage.misc.functional import cyclotomic_polynomial
from sage.rings.finite_rings.finite_field_constructor import FiniteField, GF
from sage.schemes.elliptic_curves.constructor import EllipticCurve
import json

from parameter import (
    find_curve_parameter_b,
    find_twist_curve_parameter_xi_ab,
)
from test_pairing import test_order, test_ate_pairing_bls24_aklgl

def get_parameters(u0):
    print("u0 = {:#x}".format(u0))
    # preparse("QQx.<x> = QQ[]")
    QQx = QQ["x"]
    (x,) = QQx._first_ngens(1)
    # the problem with BLS24 is the cost of the final exponentiation, and the size of G2.
    # BLS24 polynomials
    px = (x - 1) ** 2 * (x**8 - x**4 + 1) / 3 + x
    rx = x**8 - x**4 + 1
    tx = x + 1
    cx = (x - 1) ** 2 / 3
    yx = (x - 1) * (2 * x**4 - 1) / 3
    c2x = (x**32 - 8 * x**31 + 28 * x**30 - 56 * x**29 + 67 * x**28 - 32 * x**27 - 56 * x**26 + 160 * x**25 - 203 * x**24 + 132 * x**23 + 12 * x**22 - 132 * x**21 + 170 * x**20 - 124 * x**19 + 44 * x**18 - 4 * x**17 + 2 * x**16 + 20 * x**15 - 46 * x**14 + 20 * x**13 + 5 * x**12 + 24 * x**11 - 42 * x**10 + 48 * x**9 - 101 * x**8 + 100 * x**7 + 70 * x**6 - 128 * x**5 + 70 * x**4 - 56 * x**3 - 44 * x**2 + 40 * x + 100) / 81  # cofactor for G2
    D = 3  # discriminant (-D = -3)
    k = 24

    p = ZZ(px(u0))
    r = ZZ(rx(u0))
    c = ZZ(cx(u0))
    c2 = ZZ(c2x(u0))
    t = ZZ(tx(u0))
    y = ZZ(yx(u0))
    Fp = GF(p, proof=False)
    b, E = find_curve_parameter_b(Fp, r, c)

    print("u = {:#x}".format(u0))
    print("p = {:#x}, {} mod 4 # {} bits".format(p, p % 4, p.nbits()))
    print("r = {:#x} # {} bits".format(r, r.nbits()))
    print("c = {:#x} # {} bits".format(c, c.nbits()))
    print("y = {:#x}".format(y))
    print("t = {:#x}".format(t))
    print("BLS{}-{} E(Fp): y^2 = x^3 {:+d}".format(k, p.nbits(), b))

    # define Fp2
    Fpz = Fp["z"]
    (z,) = Fpz._first_ngens(1)
    if (p % 4) == 3:
        Fp2 = Fp.extension(z**2 + 1, names=("i",))
        (i,) = Fp2._first_ngens(1)
        a = -1
        print("Fp2 = Fp[x]/(x^2 + 1)")
    else:
        a = 2
        while not (z**2 - a).is_irreducible():
            a = a + 1
        print("Fp2 = Fp[x]/(x^2 - {})".format(a))
        Fp2 = Fp.extension(z**2 - a, names=("i",))
        (i,) = Fp2._first_ngens(1)

    # define Fp4
    Fp2w = Fp2["w"]
    (w,) = Fp2w._first_ngens(1)
    a2 = i
    while not (w**2 - a2).is_irreducible():
        a2 = a2 + 1
    print("Fp4 = Fp2[w]/(w^2 - ({}))".format(a2))
    # Fp22 = Fp2.extension(w**2 - a2, names=("j",))
    try:
        coeffs_a2 = a2.polynomial().list()
    except AttributeError as err:
        coeffs_a2 = a2.list()
    a20 = coeffs_a2[0]
    a21 = coeffs_a2[1]
    a20m = ZZ(a20)
    if abs(a20m - p) < abs(a20m):
        a20m = a20m - p
    a21m = ZZ(a21)
    if abs(a21m - p) < abs(a21m):
        a21m = a21m - p
    # w^2 = a21*i+a20 <=> w^2-a20 = a21*i <=> (w^2-a20)^2 = a21*a <=> w^4 -2*a20*w^2 + a20^2 - a21*a = 0
    Fp4 = Fp.extension(z**4 - 2 * a20 * z**2 + a20**2 - a21 * a, names=("v",))
    (ii,) = Fp4._first_ngens(1)
    print(
        "Fp4 = Fp[z]/(z^4{:+d}*z^2{:+d})".format(
            int(-2 * a20m), int(a20**2 - a21 * a)
        )
    )

    # Fq = Fp4
    Fp4s = Fp4["s"]
    (s,) = Fp4s._first_ngens(1)
    E2, xi, btw, D_twist = find_twist_curve_parameter_xi_ab(b, Fp4, r, d=6)
    
    # Fq = Fp4
    Fp4s = Fp4["s"]
    (s,) = Fp4s._first_ngens(1)
    E2, xi, btw, D_twist = find_twist_curve_parameter_xi_ab(b, Fp4, r, d=6)
    print("test E' (G2): ", end="")
    test_order(E2, r * c2)
    if D_twist:
        print(
            "BLS{}-{} E'(Fp4): y^2 = x^3 {:+d}/({}): D-twist".format(
                k, p.nbits(), b, xi
            )
        )
    else:
        print(
            "BLS{}-{} E'(Fp4): y^2 = x^3 {:+d}*({}): M-twist".format(
                k, p.nbits(), b, xi
            )
        )
    
    # (px, py, 1)
    P = c * E.random_element()
    while P == E(0) or r * P != E(0):
        P = c * E.random_element()
    # (qx3*v^3 + qx2*v^2 + qx1*v + qx0, qy3*v^3 + qy2*v^2 + qy1*v + qy0, 1)
    Q = c2 * E2.random_element()
    while Q == E2(0) or r * Q != E2(0):
        Q = c2 * E2.random_element()

    params = {
        "u": int(u0),
        "p": int(p), 
        "r": int(r), 
        "b": int(b), 
        "beta": int(a), # Fp2[i]/(i^2-beta)
        "beta2": [int(x) for x in a2.polynomial().list()], # Fp4[v]/(v^2-(beta21*i+beta20))
        "xi": [int(x) for x in xi.polynomial().list()], # Fp24[w]/(w^6-(xi1*v+xi0))
        "D_twist": D_twist
    }

    return params 

def test_curve(u0):
    print("u0 = {:#x}".format(u0))
    # preparse("QQx.<x> = QQ[]")
    QQx = QQ["x"]
    (x,) = QQx._first_ngens(1)
    # the problem with BLS24 is the cost of the final exponentiation, and the size of G2.
    # BLS24 polynomials
    px = (x - 1) ** 2 * (x**8 - x**4 + 1) / 3 + x
    rx = x**8 - x**4 + 1
    tx = x + 1
    cx = (x - 1) ** 2 / 3
    yx = (x - 1) * (2 * x**4 - 1) / 3
    c2x = (x**32 - 8 * x**31 + 28 * x**30 - 56 * x**29 + 67 * x**28 - 32 * x**27 - 56 * x**26 + 160 * x**25 - 203 * x**24 + 132 * x**23 + 12 * x**22 - 132 * x**21 + 170 * x**20 - 124 * x**19 + 44 * x**18 - 4 * x**17 + 2 * x**16 + 20 * x**15 - 46 * x**14 + 20 * x**13 + 5 * x**12 + 24 * x**11 - 42 * x**10 + 48 * x**9 - 101 * x**8 + 100 * x**7 + 70 * x**6 - 128 * x**5 + 70 * x**4 - 56 * x**3 - 44 * x**2 + 40 * x + 100) / 81  # cofactor for G2
    D = 3  # discriminant (-D = -3)
    k = 24

    p = ZZ(px(u0))
    r = ZZ(rx(u0))
    c = ZZ(cx(u0))
    c2 = ZZ(c2x(u0))
    t = ZZ(tx(u0))
    y = ZZ(yx(u0))
    Fp = GF(p, proof=False)
    b, E = find_curve_parameter_b(Fp, r, c)

    print("u = {:#x}".format(u0))
    print("p = {:#x}, {} mod 4 # {} bits".format(p, p % 4, p.nbits()))
    print("r = {:#x} # {} bits".format(r, r.nbits()))
    print("c = {:#x} # {} bits".format(c, c.nbits()))
    print("y = {:#x}".format(y))
    print("t = {:#x}".format(t))
    print("BLS{}-{} E(Fp): y^2 = x^3 {:+d}".format(k, p.nbits(), b))
    print("test E (G1): ", end="")
    test_order(E, r * c)

    # define Fp2
    Fpz = Fp["z"]
    (z,) = Fpz._first_ngens(1)
    if (p % 4) == 3:
        Fp2 = Fp.extension(z**2 + 1, names=("i",))
        (i,) = Fp2._first_ngens(1)
        a = -1
        print("Fp2 = Fp[x]/(x^2 + 1)")
    else:
        a = 2
        while not (z**2 - a).is_irreducible():
            a = a + 1
        print("Fp2 = Fp[x]/(x^2 - {})".format(a))
        Fp2 = Fp.extension(z**2 - a, names=("i",))
        (i,) = Fp2._first_ngens(1)

    # define Fp4
    Fp2w = Fp2["w"]
    (w,) = Fp2w._first_ngens(1)
    a2 = i
    while not (w**2 - a2).is_irreducible():
        a2 = a2 + 1
    print("Fp4 = Fp2[w]/(w^2 - ({}))".format(a2))
    # Fp22 = Fp2.extension(w**2 - a2, names=("j",))
    try:
        coeffs_a2 = a2.polynomial().list()
    except AttributeError as err:
        coeffs_a2 = a2.list()
    a20 = coeffs_a2[0]
    a21 = coeffs_a2[1]
    a20m = ZZ(a20)
    if abs(a20m - p) < abs(a20m):
        a20m = a20m - p
    a21m = ZZ(a21)
    if abs(a21m - p) < abs(a21m):
        a21m = a21m - p
    # w^2 = a21*i+a20 <=> w^2-a20 = a21*i <=> (w^2-a20)^2 = a21*a <=> w^4 -2*a20*w^2 + a20^2 - a21*a = 0
    Fp4 = Fp.extension(z**4 - 2 * a20 * z**2 + a20**2 - a21 * a, names=("v",))
    (ii,) = Fp4._first_ngens(1)
    print(
        "Fp4 = Fp[z]/(z^4{:+d}*z^2{:+d})".format(
            int(-2 * a20m), int(a20**2 - a21 * a)
        )
    )

    # Fq = Fp4
    Fp4s = Fp4["s"]
    (s,) = Fp4s._first_ngens(1)
    E2, xi, btw, D_twist = find_twist_curve_parameter_xi_ab(b, Fp4, r, d=6)
    print("test E' (G2): ", end="")
    test_order(E2, r * c2)
    if D_twist:
        print(
            "BLS{}-{} E'(Fp4): y^2 = x^3 {:+d}/({}): D-twist".format(
                k, p.nbits(), b, xi
            )
        )
    else:
        print(
            "BLS{}-{} E'(Fp4): y^2 = x^3 {:+d}*({}): M-twist".format(
                k, p.nbits(), b, xi
            )
        )

    Fq6 = Fp4.extension(s**6 - xi, names=("w",))
    (w,) = Fq6._first_ngens(1)
    try:
        coeffs_xi = xi.polynomial().list()
    except AttributeError as err:
        coeffs_xi = xi.list()
    i0 = ZZ(coeffs_xi[0])
    i1 = ZZ(coeffs_xi[1])
    if abs(i0 - p) < abs(i0):
        i0 = i0 - p
    if abs(i1 - p) < abs(i1):
        i1 = i1 - p

    # w^6 = ii+4 <=> w^6-4 = ii <=> (w^6-4)^4 - 2*(w^6-4)^2 + 2 = 0
    # w^6 = i1*ii + i0 <=> w^6-i0 = i1*ii => (w^6-i0)^2 = i1^2*(a21*i+a20)
    #                                         => ((w^6-i0)^2 - i1^2*a20)^2 = i1^4*a21^2 * a
    poly = ((z**6 - i0) ** 2 - a20 * i1**2) ** 2 - a * a21**2 * i1**4
    Fp24 = Fp.extension(poly, names=("S",))
    (S,) = Fp24._first_ngens(1)
    # E_Fp24 = EllipticCurve([Fp24(0), Fp24(b)])
    print("Fq6 = Fq[s]/(s^6{:+d}{:+d}*v): Fq = Fp4".format(int(-i0), int(-i1)))
    print("Fp24 = Fp[z]/({})".format(poly))

    def map_Fq6_Fp24(x, a=S):
        return sum(
            [
                xi.polynomial()((a**6 - i0) / i1) * a**e
                for e, xi in enumerate(x.list())
            ]
        )

    test_ate_pairing_bls24_aklgl(E, E2, r, c, c2, u0, Fq6, map_Fq6_Fp24, D_twist)

if __name__ == "__main__":
    args = sys.argv
    param_file = args[1]
    size = os.path.getsize(param_file)
    if size == 0:
        json_load = dict()
    else:
        with open(param_file, "r") as file:
            json_load = json.load(file)

    json_load["bls24"] = dict()
    # BLS24-315
    u0 = ZZ(-(2**32) + 2**30 + 2**21 + 2**20 + 1)
    json_load["bls24"]["P315"] = get_parameters(u0)
    # test_curve(u0)

    # BLS24-317
    u0 = ZZ(2**31 + 2**30 + 2**28 + 2**27 + 2**24 + 2**16 + 2**15)
    json_load["bls24"]["P317"] = get_parameters(u0)
    # test_curve(u0)

    # BLS24-318
    u0 = ZZ(-(2**32) + 2**28 + 2**12)
    json_load["bls24"]["P318"] = get_parameters(u0)
    # test_curve(u0)

    # BLS24-509
    u0 = ZZ(-(2**51) - 2**28 + 2**11 - 1)
    json_load["bls24"]["P509"] = get_parameters(u0)
    # test_curve(u0)
    
    with open(param_file, "w") as file:
        json.dump(json_load, file, indent=4)
