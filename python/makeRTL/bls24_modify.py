import shutil
from io import TextIOWrapper

from lib.parameters import args, dict, u, U, p, r, L, p_len, p_mod8, p_inv, inv_init_val, one, P, Q, T, B4
from lib.operate_Fp import get_qnr1, add, negFp
from lib.operate_Fp4 import addFp4, expFp4, negFp4, k
from util import make_define_Fp4

def int2hexstr(x):
    return str(hex(x))[2:]

def write_parameter_vh(f_param):
    p_str = str(hex(p))[2:]
    p_len_str = str(p_len)
    p3 = p * 3

    with open("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/ram_addr.v", "r") as file:
        content = file.read()
    
    f = open(f_param, 'a')
    f.write(content)

    f.write("\n\n// constants --------------------------------------------------------\n")
    f.write("`define WORD_SIZE 'd" + p_len_str + "\n")
    f.write("`define CHAR " + p_len_str + "'h" + p_str + "\n")
    f.write("`define CHAR_INV " + p_len_str + "'h" + int2hexstr(p_inv)+"\n")
    f.write("`define INVERSION_INITIAL_VALUE " + p_len_str + "'h" + int2hexstr(inv_init_val)+"\n")
    f.write("`define CHAR_3X " + str(p3.bit_length()) + "'h" + int2hexstr(p3)+"\n\n")  #NOTE: Div4PathUnit-aug_p のbit幅要確認

    f.write("// parameters for twisted curve (Ep4)\n")
    f.write("`define B400 " + p_len_str + "'h" + int2hexstr(B4[0][0])+"\n")
    f.write("`define B401 " + p_len_str + "'h" + int2hexstr(B4[0][1])+"\n")
    f.write("`define B410 " + p_len_str + "'h" + int2hexstr(B4[1][0])+"\n")
    f.write("`define B411 " + p_len_str + "'h" + int2hexstr(B4[1][1])+"\n\n")

    # one = MontConv(1, L, p)
    v = [[0, 0], [one, 0]]
    xi = [
        [[one, 0], [0, 0]],
        expFp4(v, (p-1)//6),
        expFp4(v, 2*(p-1)//6),
        expFp4(v, 3*(p-1)//6),
        expFp4(v, 4*(p-1)//6),
        expFp4(v, 5*(p-1)//6)
    ]

    f.write("// // constants independent from elliptic curve\n")
    f.write("`define ZERO " + p_len_str + "'h0\n")
    f.write("`define ONE " + p_len_str + "'h"+int2hexstr(B4[0][0])+"\n")

    f.write("\n// Frobenius pre-calculated coefficients\n")
    f.write("`define K0 " + p_len_str + "'h"+int2hexstr(k[0])+"\n\n")
    f.write("`define K1 " + p_len_str + "'h"+int2hexstr(k[1])+"\n\n")

    f.write("`define XI100 " + p_len_str + "'h" + int2hexstr(xi[1][0][0])+"\n")
    f.write("`define XI101 " + p_len_str + "'h" + int2hexstr(xi[1][0][1])+"\n")
    f.write("`define XI110 " + p_len_str + "'h" + int2hexstr(xi[1][1][0])+"\n")
    f.write("`define XI111 " + p_len_str + "'h" + int2hexstr(xi[1][1][1])+"\n\n")

    f.write("`define XI200 " + p_len_str + "'h" + int2hexstr(xi[2][0][0])+"\n")
    f.write("`define XI201 " + p_len_str + "'h" + int2hexstr(xi[2][0][1])+"\n")
    f.write("`define XI210 " + p_len_str + "'h" + int2hexstr(xi[2][1][0])+"\n")
    f.write("`define XI211 " + p_len_str + "'h" + int2hexstr(xi[2][1][1])+"\n\n")

    f.write("`define XI300 " + p_len_str + "'h" + int2hexstr(xi[3][0][0])+"\n")
    f.write("`define XI301 " + p_len_str + "'h" + int2hexstr(xi[3][0][1])+"\n")
    f.write("`define XI310 " + p_len_str + "'h" + int2hexstr(xi[3][1][0])+"\n")
    f.write("`define XI311 " + p_len_str + "'h" + int2hexstr(xi[3][1][1])+"\n\n")

    f.write("`define XI400 " + p_len_str + "'h" + int2hexstr(xi[4][0][0])+"\n")
    f.write("`define XI401 " + p_len_str + "'h" + int2hexstr(xi[4][0][1])+"\n")
    f.write("`define XI410 " + p_len_str + "'h" + int2hexstr(xi[4][1][0])+"\n")
    f.write("`define XI411 " + p_len_str + "'h" + int2hexstr(xi[4][1][1])+"\n\n")

    f.write("`define XI500 " + p_len_str + "'h" + int2hexstr(xi[5][0][0])+"\n")
    f.write("`define XI501 " + p_len_str + "'h" + int2hexstr(xi[5][0][1])+"\n")
    f.write("`define XI510 " + p_len_str + "'h" + int2hexstr(xi[5][1][0])+"\n")
    f.write("`define XI511 " + p_len_str + "'h" + int2hexstr(xi[5][1][1])+"\n\n")
    f.close()

def write_input_vh(f_input):
    f = open(f_input, 'w')
    p_len_str = str(p_len)
    
    # a = random.randint(1, r-1)
    # print("a: " + str(a))
    # aP = ep_mul(a, [P[0][0][0], P[1][0][0]])
    # aP = [[[aP[0][0][0], 0], [0, 0]], [[aP[1][0][0], 0], [0, 0]]]
    aP = P
    f.write("`define PX " + p_len_str + "'h" + int2hexstr(aP[0][0][0])+"\n")
    f.write("`define PX_ " + p_len_str + "'h" + int2hexstr(negFp(aP[0][0][0]))+"\n")
    f.write("`define PX3 " + p_len_str + "'h" + int2hexstr(add(aP[0][0][0], add(aP[0][0][0], aP[0][0][0])))+"\n")
    f.write("`define PY " + p_len_str + "'h" + int2hexstr(aP[1][0][0])+"\n")
    f.write("`define PY_ " + p_len_str + "'h" + int2hexstr(negFp(aP[1][0][0]))+"\n")

    # b = random.randint(1, r-1)
    # print("b: " + str(b))
    # bT = ep4_mul(b, T)
    # bT = change_to_affine(bT)
    # bQ = bT[: 2]
    bQ = T[:2]
    bT = T
    make_define_Fp4(f, "QX", bQ[0])
    make_define_Fp4(f, "TX", bQ[0])
    make_define_Fp4(f, "QY", bQ[1])
    make_define_Fp4(f, "QY_", negFp4(bQ[1]))
    if u > 0:
        make_define_Fp4(f, "TY", bQ[1])
    else:
        make_define_Fp4(f, "TY", negFp4(bQ[1]))
    make_define_Fp4(f, "TZ", bT[2])
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
            commands_list.append(["MODE_PDBL", "`RAM_QX00", "`RAM_QX00", "`RAM_F"])
        else:
            commands_list.append(["MODE_PDBL", "`RAM_QX00", "`RAM_QX00", "`RAM_E"])
            commands_list.append(["MODE_SQUARE", "`RAM_F", "`RAM_F", "`RAM_F"])
            commands_list.append(["MODE_SPARSE_MUL", "`RAM_E", "`RAM_F", "`RAM_F"])
        if l == 1:
            commands_list.append(["MODE_PADD", "`RAM_QX00", "`RAM_QX00", "`RAM_E"])
            commands_list.append(["MODE_SPARSE_MUL", "`RAM_E", "`RAM_F", "`RAM_F"])
        if l == -1:
            commands_list.append(["MODE_PMINUS", "`RAM_QX00", "`RAM_QX00", "`RAM_E"])
            commands_list.append(["MODE_SPARSE_MUL", "`RAM_E", "`RAM_F", "`RAM_F"])
    print_commands_list(0, commands_list, f)
    f.close()
    return len(commands_list)

def expFp24_commands(cnt, opr, ret, f:TextIOWrapper):
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
    f.write("writeCommands(0, {`MODE_INV, `RAM_F, `RAM_F, `RAM_E});  // e = invFp24(f)\n")
    f.write("writeCommands(1, {`MODE_MUL_CONJ, `RAM_E, `RAM_F, `RAM_F}); // f = mulFp24_conj_forRTL(e, f)\n")
    f.write("writeCommands(2, {`MODE_FROB, `RAM_F, `RAM_F, `RAM_E}); // e = FrobFp24(FrobFp24(FrobFp24(FrobFp24(f))))\n")
    f.write("writeCommands(3, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});\n")
    f.write("writeCommands(4, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});\n")
    f.write("writeCommands(5, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});\n")
    f.write("writeCommands(6, {`MODE_MUL, `RAM_E, `RAM_F, `RAM_F}); // f = mulFp24(e, f)\n\n")

    f.write("// Hard Part -------------------------------------------------------\n")
    f.write("// a = expFp24(f)\n")
    cnt = expFp24_commands(7, "`RAM_F", "`RAM_A", f)
    f.write("// b = expFp24(a)\n")
    cnt = expFp24_commands(cnt, "`RAM_A", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_SQR012345, `RAM_A, `RAM_A, `RAM_A}}); // a = squareFp24(a)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL_CONJ, `RAM_B, `RAM_A, `RAM_A}}); // a = mulFp24_conj_forRTL(b, a)\n".format(cnt+1))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_A, `RAM_F, `RAM_A}}); // a = mulFp24(a, f)\n".format(cnt+2))
    f.write("// b = expFp24(a)\n")
    cnt = expFp24_commands(cnt+3, "`RAM_A", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_A, `RAM_C, `RAM_E}}); // e = FrobFp24(a)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}}); // e = mulFp24(e, b)\n".format(cnt+1))
    f.write("writeCommands({0}, {{`MODE_CONJ, `RAM_A, `RAM_A, `RAM_A}}); // a = conjFp24(a)\n".format(cnt+2))
    f.write("// b = expFp24(b)\n")
    cnt = expFp24_commands(cnt+3, "`RAM_B", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}}); // e = FrobFp24(e)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}}); // e = mulFp24(e, b)\n".format(cnt+1))
    f.write("// b = expFp24(b)\n")
    cnt = expFp24_commands(cnt+2, "`RAM_B", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}}); // e = FrobFp24(e)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}}); // e = mulFp24(e, b)\n".format(cnt+1))
    f.write("// b = expFp24(b)\n")
    cnt = expFp24_commands(cnt+2, "`RAM_B", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_B, `RAM_A, `RAM_B}}); // b = mulFp24(b, a)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}}); // e = FrobFp24(e)\n".format(cnt+1))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}}); // e = mulFp24(e, b)\n".format(cnt+2))
    f.write("// b = expFp24(b)\n")
    cnt = expFp24_commands(cnt+3, "`RAM_B", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}}); // e = FrobFp24(e)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}}); // e = mulFp24(e, b)\n".format(cnt+1))
    f.write("// b = expFp24(b)\n")
    cnt = expFp24_commands(cnt+2, "`RAM_B", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}}); // e = FrobFp24(e)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}}); // e = mulFp24(e, b)\n".format(cnt+1))
    f.write("// b = expFp24(b)\n")
    cnt = expFp24_commands(cnt+2, "`RAM_B", "`RAM_B", f)
    f.write("writeCommands({0}, {{`MODE_SQR012345, `RAM_F, `RAM_F, `RAM_A}}); // a = squareFp24(f)\n".format(cnt))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_A, `RAM_B, `RAM_A}}); // a = mulFp24(a, b)\n".format(cnt+1))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_A, `RAM_F, `RAM_A}}); // a = mulFp24(a, f)\n".format(cnt+2))
    f.write("writeCommands({0}, {{`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}}); // e = FrobFp24(e)\n".format(cnt+3))
    f.write("writeCommands({0}, {{`MODE_MUL, `RAM_E, `RAM_A, `RAM_E}}); // e = mulFp24(e, a)\n".format(cnt+4))
    return cnt+5


def testbench_copy(output_directory):
    shutil.copy("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/input_values.v", output_directory+"/testbench/include/")
    shutil.copy("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/SQR_test.v", output_directory+"/testbench/include/")
    shutil.copy("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/sim_new_arch.v", output_directory+"/testbench/")
    shutil.copy("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/simML.v", output_directory+"/testbench/")
    shutil.copy("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/simPairing.v", output_directory+"/testbench/")
    shutil.copy("/home/mfukuda/optimal-ate-pairing/template/lib/bls24/simRAM_wr.v", output_directory+"/testbench/")


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
    make_RTL(dict, args[2])