import shutil
from io import TextIOWrapper

from parameters import args, u, U, p, p_len, p_inv, inv_init_val, one, P, Q, T, B2
from operate_Fp import get_qnr1, add, negFp
from operate_Fp2 import addFp2, expFp2, negFp2, v2
from util import make_define_Fp2

def int2hexstr(x):
    return str(hex(x))[2:]

def write_parameter_vh(f_param):
    p_str = str(hex(p))[2:]
    p_len_str = str(p_len)
    p3 = p * 3
    with open("./lib/bls12/ram_addr.v", "r") as file:
        content = file.read()
    
    f = open(f_param, 'a')
    f.write(content)

    f.write("\n\n// constants -------------------------------------------------------------------------------------------------\n")
    f.write("`define WORD_SIZE 'd" + p_len_str + "\n")
    f.write("`define CHAR " + p_len_str + "'h" + p_str + "\n")
    f.write("`define CHAR_INV " + p_len_str + "'h" + int2hexstr(p_inv)+"\n")
    f.write("`define INVERSION_INITIAL_VALUE " + p_len_str + "'h" + int2hexstr(inv_init_val)+"\n")
    f.write("`define CHAR_3X " + str(p3.bit_length()) + "'h" + int2hexstr(p3)+"\n\n")  #NOTE: Div4PathUnit-aug_p のbit幅要確認

    f.write("// parameters for twisted curve (Ep2)\n")
    f.write("`define B20 " + p_len_str + "'h" + int2hexstr(B2[0])+"\n")
    f.write("`define B21 " + p_len_str + "'h" + int2hexstr(B2[1])+"\n")

    # one = MontConv(1, L, p)
    xi = [
        [[one, 0], [0, 0]],
        expFp2(v2, (p-1)//6),
        expFp2(v2, 2*(p-1)//6),
        expFp2(v2, 3*(p-1)//6),
        expFp2(v2, 4*(p-1)//6),
        expFp2(v2, 5*(p-1)//6)
    ]

    f.write("// // constants independent from elliptic curve\n")
    f.write("`define ZERO " + p_len_str + "'h0\n")
    f.write("`define ONE " + p_len_str + "'h"+int2hexstr(one)+"\n")

    f.write("\n// Frobenius pre-calculated coefficients\n")

    f.write("`define XI10 " + p_len_str + "'h" + int2hexstr(xi[1][0])+"\n")
    f.write("`define XI11 " + p_len_str + "'h" + int2hexstr(xi[1][1])+"\n")

    f.write("`define XI20 " + p_len_str + "'h" + int2hexstr(xi[2][0])+"\n")
    f.write("`define XI21 " + p_len_str + "'h" + int2hexstr(xi[2][1])+"\n")

    f.write("`define XI30 " + p_len_str + "'h" + int2hexstr(xi[3][0])+"\n")
    f.write("`define XI31 " + p_len_str + "'h" + int2hexstr(xi[3][1])+"\n")

    f.write("`define XI40 " + p_len_str + "'h" + int2hexstr(xi[4][0])+"\n")
    f.write("`define XI41 " + p_len_str + "'h" + int2hexstr(xi[4][1])+"\n")

    f.write("`define XI50 " + p_len_str + "'h" + int2hexstr(xi[5][0])+"\n")
    f.write("`define XI51 " + p_len_str + "'h" + int2hexstr(xi[5][1])+"\n")
    f.close()

def write_input_vh(f_input):
    f = open(f_input, 'w')
    p_len_str = str(p_len)
    
    # a = random.randint(1, r-1)
    # print("a: " + str(a))
    # aP = ep_mul(a, [P[0][0][0], P[1][0][0]])
    # aP = [[[aP[0][0][0], 0], [0, 0]], [[aP[1][0][0], 0], [0, 0]]]
    aP = P
    f.write("`define PX " + p_len_str + "'h" + int2hexstr(aP[0][0])+"\n")
    f.write("`define PX_ " + p_len_str + "'h" + int2hexstr(negFp(aP[0][0]))+"\n")
    f.write("`define PX3 " + p_len_str + "'h" + int2hexstr(add(aP[0][0], add(aP[0][0], aP[0][0])))+"\n")
    f.write("`define PY " + p_len_str + "'h" + int2hexstr(aP[1][0])+"\n")
    f.write("`define PY_ " + p_len_str + "'h" + int2hexstr(negFp(aP[1][0]))+"\n")

    # b = random.randint(1, r-1)
    # print("b: " + str(b))
    # bT = ep4_mul(b, T)
    # bT = change_to_affine(bT)
    # bQ = bT[: 2]
    bQ = T[:2]
    bT = T
    make_define_Fp2(f, "QX", bQ[0])
    make_define_Fp2(f, "TX", bQ[0])
    make_define_Fp2(f, "QY", bQ[1])
    make_define_Fp2(f, "QY_", negFp2(bQ[1]))
    if u > 0:
        make_define_Fp2(f, "TY", bQ[1])
    else:
        make_define_Fp2(f, "TY", negFp2(bQ[1]))
    make_define_Fp2(f, "TZ", bT[2])
    f.close()


def print_commands_list(cnt, commands_list, f):
    for index, command in enumerate(commands_list):
        f.write("writeCommands({0}, {{`{1}, {2}, {3}, {4}}});\n".format(cnt+index, command[0], command[1], command[2], command[3]))

def make_ML_commands(f_ML_commands):
    f = open(f_ML_commands, 'w')
    m = U[::-1]
    cnt = 0
    commands_list = [] # [MODE, opr1, opr2, ret]
    for l in m[1:]:
        if cnt == 0:
            cnt = 1
            commands_list.append(["MODE_PDBL", "`RAM_QX0", "`RAM_QX0", "`RAM_F"])
        else:
            commands_list.append(["MODE_PDBL", "`RAM_QX0", "`RAM_QX0", "`RAM_E"])
            commands_list.append(["MODE_SQUARE", "`RAM_F", "`RAM_F", "`RAM_F"])
            commands_list.append(["MODE_SPARSE_MUL", "`RAM_E", "`RAM_F", "`RAM_F"])
        if l == 1:
            commands_list.append(["MODE_PADD", "`RAM_QX0", "`RAM_QX0", "`RAM_E"])
            commands_list.append(["MODE_SPARSE_MUL", "`RAM_E", "`RAM_F", "`RAM_F"])
        if l == -1:
            commands_list.append(["MODE_PMINUS", "`RAM_QX0", "`RAM_QX0", "`RAM_E"])
            commands_list.append(["MODE_SPARSE_MUL", "`RAM_E", "`RAM_F", "`RAM_F"])
    print_commands_list(0, commands_list, f)
    f.close()
    return len(commands_list)

def expFp12_commands(cnt, opr, ret, f:TextIOWrapper):
    delay_mul = False
    init_to_ret = False
    commands_list = [] # [MODE, opr1, opr2, ret]
    for index, l in enumerate(U):
        if l == 1:
            if index == 0:
                commands_list.append(["MODE_SQR012345", opr, "`RAM_C", "`RAM_C"])
                delay_mul = True
            else:
                if delay_mul:
                    commands_list.append(["MODE_MUL", opr, "`RAM_C", ret])
                    commands_list.append(["MODE_SQR012345", "`RAM_C", "`RAM_C", "`RAM_C"])
                    delay_mul = False
                elif init_to_ret:
                    commands_list[-1][3] = ret
                    commands_list.append(["MODE_SQR012345", ret, "`RAM_C", "`RAM_C"])
                    init_to_ret = False
                else:
                    commands_list.append(["MODE_MUL", ret, "`RAM_C", ret])
                    commands_list.append(["MODE_SQR012345", "`RAM_C", "`RAM_C", "`RAM_C"])
        elif l == -1:
            if index == 0:
                commands_list.append(["MODE_SQR012345", opr, "`RAM_C", "`RAM_C"])
                commands_list.append(["MODE_CONJ", opr, "`RAM_C", ret])
            else:
                if delay_mul:
                    commands_list.append(["MODE_MUL_CONJ", opr, "`RAM_C", ret])
                    delay_mul = False
                elif init_to_ret:
                    commands_list.append(["MODE_CONJ", "`RAM_C", "`RAM_C", ret])
                    init_to_ret = False
                else:
                    commands_list.append(["MODE_MUL_CONJ", ret, "`RAM_C", ret])
                commands_list.append(["MODE_SQR012345", "`RAM_C", "`RAM_C", "`RAM_C"])
        else:
            if index == 0:
                init_to_ret = True
                commands_list.append(["MODE_SQR012345", opr, "`RAM_C", "`RAM_C"])
            else:
                commands_list.append(["MODE_SQR012345", "`RAM_C", "`RAM_C", "`RAM_C"])
    print_commands_list(cnt, commands_list[:-1], f)
    return cnt + len(commands_list) - 1

def make_FE_commands(f_FE_commands):
    f = open(f_FE_commands, 'w')
    f.write("// Easy Part -------------------------------------------------------\n")
    f.write("writeCommands(0, {`MODE_FROB, `RAM_F, `RAM_F, `RAM_E});  // e = FrobFp12(FrobFp12(f))\n")
    f.write("writeCommands(1, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});\n")
    f.write("writeCommands(2, {`MODE_MUL, `RAM_F, `RAM_E, `RAM_E}); // e = mulFp12(e, f)\n")
    f.write("writeCommands(3, {`MODE_INV, `RAM_E, `RAM_E, `RAM_F}); // f = invFp12(e)\n")
    f.write("writeCommands(4, {`MODE_MUL_CONJ, `RAM_F, `RAM_E, `RAM_F}); // f = mulFp12_conj_forRTL(f, e)\n")

    f.write("// Hard Part -------------------------------------------------------\n")
    f.write("writeCommands(5, {`MODE_SQR012345, `RAM_F, `RAM_F, `RAM_G}); // t1 = SQR012345Fp12(f)\n")

    f.write("// t2 = expFp12(f)\n")
    cnt = expFp12_commands(6, "`RAM_F", "`RAM_E", f)

    f.write("writeCommands({0}, {{`MODE_MUL_CONJ, `RAM_E, `RAM_G, `RAM_G}}); // t1 = mulFp12_conj_forRTL(t2, t1)\n".format(cnt))

    f.write("// t4 = expFp12(t1)\n")
    cnt = expFp12_commands(cnt+1, "`RAM_G", "`RAM_B", f)

    f.write("writeCommands({0}, {{`MODE_MUL_CONJ, `RAM_F, `RAM_G, `RAM_G}}); // t1 = mulFp12_conj_forRTL(f, t1) \n".format(cnt))

    f.write("// t5 = expFp12(t4)\n")
    cnt = expFp12_commands(cnt+1, "`RAM_B", "`RAM_A", f)

    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_F, `RAM_B, `RAM_B}}); // t4 = mulFp12(f, t4)\n".format(cnt))

    f.write("// t3 = expFp12(t5)\n")
    cnt = expFp12_commands(cnt+1, "`RAM_A", "`RAM_D", f)

    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_A, `RAM_A}}); // t5 = mulFp12(t2, t5)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_SQR012345, `RAM_E, `RAM_E, `RAM_E}}); // t2 = SQR012345Fp12(t2)\n".format(cnt+1))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_B, `RAM_E, `RAM_B}}); // t4 = FrobFp12(FrobFp12(t4))\n".format(cnt+2))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_B, `RAM_B, `RAM_B}});\n".format(cnt+3))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_A, `RAM_A, `RAM_A}}); // t5 = FrobFp12(FrobFp12(t5))\n".format(cnt+4))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_A, `RAM_A, `RAM_A}});\n".format(cnt+5))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_D, `RAM_E}}); //t2 = mulFp12(t2, t3)\n".format(cnt+6))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_B, `RAM_B, `RAM_B}}); // t4 = FrobFp12(t4)\n".format(cnt+7))

    f.write("// t3 = expFp12(t2)\n")
    cnt = expFp12_commands(cnt+8, "`RAM_E", "`RAM_D", f)

    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_B, `RAM_A, `RAM_B}}); // t4 = mulFp12(t4, t5)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL_CONJ, `RAM_E, `RAM_F, `RAM_A}}); // t5 = mulFp12_conj_forRTL(t2, f)\n".format(cnt+1))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_G, `RAM_D, `RAM_G}}); // t1 = mulFp12(t1, t3)\n".format(cnt+2))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_A, `RAM_A, `RAM_A}}); // t5 = FrobFp12(t5)\n".format(cnt+3))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_G, `RAM_B, `RAM_G}}); // t1 = mulFp12(t1, t4)\n".format(cnt+4))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_G, `RAM_A, `RAM_G}}); // t1 = mulFp12(t1, t3)\n".format(cnt+5))

    return cnt+6

def testbench_copy(output_directory):
    shutil.copy("./lib/bls12/input_values.v", output_directory+"/testbench/include/")
    shutil.copy("./lib/bls12/SQR_test.v", output_directory+"/testbench/include/")
    shutil.copy("./lib/bls12/sim_new_arch.v", output_directory+"/testbench/")
    shutil.copy("./lib/bls12/simML.v", output_directory+"/testbench/")
    shutil.copy("./lib/bls12/simPairing.v", output_directory+"/testbench/")
    shutil.copy("./lib/bls12/simRAM_wr.v", output_directory+"/testbench/")


def make_RTL(output_directory):
    testbench_copy(output_directory)

    write_parameter_vh(f_param=output_directory+"/include/parameter.vh")
    write_input_vh(f_input=output_directory+"/include/parameter_input.vh")

    cmd_memdepth_ml = make_ML_commands(f_ML_commands=output_directory+"/testbench/include/ML_input_commands.v")
    cmd_memdepth_fe = make_FE_commands(f_FE_commands=output_directory+"/testbench/include/FE_input_commands.v")
    f = open(output_directory+"/include/parameter.vh", 'a')
    f.write("`define CMD_MEMDEPTH_ML {0}\n".format(cmd_memdepth_ml))
    f.write("`define CMD_MEMSIZE_ML {0}\n\n".format((cmd_memdepth_ml-1).bit_length()))
    f.write("`define CMD_MEMDEPTH_FE {0}\n".format(cmd_memdepth_fe))
    f.write("`define CMD_MEMSIZE_FE {0}\n\n".format((cmd_memdepth_fe-1).bit_length()))
    f.write("`define CMD_MEMSIZE {0}\n".format(max((cmd_memdepth_fe-1).bit_length(), (cmd_memdepth_ml-1).bit_length())))
    f.close()


if __name__ == '__main__':
    # args = sys.argv
    # dict = read_csv(args[2])
    make_RTL(args[2])