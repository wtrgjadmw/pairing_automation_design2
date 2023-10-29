from io import TextIOWrapper

def make_define_Fp2(f: TextIOWrapper, name, a): # name: variable name , a: Fp4 variable
    f.write("`define {}0 {:#d}'h{:#x}".format(name, p_len, a[0]))
    f.write("`define {}1 {:#d}'h{:#x}".format(name, p_len, a[1]))
    f.write("\n")

def make_define_Fp4(f: TextIOWrapper, name, a): # name: variable name , a: Fp4 variable
    f.write("`define {}00 {:#d}'h{:#x}".format(name, p_len, a[0][0]))
    f.write("`define {}01 {:#d}'h{:#x}".format(name, p_len, a[1][1]))
    f.write("`define {}10 {:#d}'h{:#x}".format(name, p_len, a[1][0]))
    f.write("`define {}11 {:#d}'h{:#x}".format(name, p_len, a[1][1]))
    f.write("\n")

def write_parameter_vh(f_param):
    p_str = str(hex(p))[2:]
    p_len_str = str(p_len)
    p3 = p * 3

    f = open(f_param, 'a')

    f.write("\n\n// constants -------------------------------------------------------------------------------------------------\n")
    f.write("`define WORD_SIZE 'd" + p_len_str + "\n")
    f.write("`define CHAR " + p_len_str + "'h" + p_str + "\n")
    f.write("`define CHAR_INV " + p_len_str + "'h" + int2hexstr(p_inv)+"\n")
    f.write("`define INVERSION_INITIAL_VALUE " + p_len_str + "'h" + int2hexstr(inv_init_val)+"\n")
    f.write("`define CHAR_3X " + str(p3.bit_length()) + "'h" + int2hexstr(p3)+"\n\n")  #NOTE: Div4PathUnit-aug_p のbit幅要確認

    f.write("// // constants independent from elliptic curve\n")
    f.write("`define ZERO " + p_len_str + "'h0\n")
    f.write("`define ONE " + p_len_str + "'h"+int2hexstr(one)+"\n")

def print_commands_list(cnt, commands_list, f):
    for index, command in enumerate(commands_list):
        f.write("writeCommands({0}, {{`{1}, {2}, {3}, {4}}});\n".format(cnt+index, command[0], command[1], command[2], command[3]))