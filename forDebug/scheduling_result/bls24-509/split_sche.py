import copy, csv

def read_formula_csv(filename):
    f_read = open(filename, "r")
    formulas = []
    add_num = 0
    mul_num = 0
    mem_table = {}
    for line in csv.reader(f_read):
        if len(line) > 0 and line[0][0] == '#':
            continue
        if len(line) == 4:
            formulas.append([line[0], line[3], line[1], line[2]])
            if line[3] == "ADD" or line[3] == "SUB":
                add_num += 1
            elif line[3] == "MONTMUL":
                mul_num += 1
            mem_value_name0 = "{0}_mem{1}".format(line[0], 0)
            mem_value_name1 = "{0}_mem{1}".format(line[0], 1)
            mem_table[mem_value_name0] = line[1]
            if line[1] != line[2]:
                mem_table[mem_value_name1] = line[2]
    f_read.close()
    return formulas, mem_table, add_num, mul_num

def split_list(lst, division_num):
    return [lst[i:i + division_num] for i in range(0, len(lst), division_num)]

# 大規模スケジューリングの分割
def make_split_scheduling(formulas):

    inputs = []
    outputs = []
    input_num = 0
    d = []
    for s in formulas:
        d.append(s[0])
        outputs.append(s[0])
        if s[2] in inputs:
            input_num += 1
        elif s[2] not in d:
            inputs.append(s[2])
            input_num += 1
        if s[3] in inputs:
            input_num += 1
        elif s[3] not in d:
            inputs.append(s[3])
            input_num += 1
        if s[2] in outputs:
            outputs.remove(s[2])
        if s[3] in outputs:
            outputs.remove(s[3])
    # このinputsのlabel情報をmake_veriに回す？
    #print("\n\n\ninput\n", inputs, "\n\n\n")
    input_first = copy.deepcopy(inputs)
    knows = inputs
    alls = []
    alls += inputs
    for s in formulas:
        alls.append(s[0])
    cnt = 0
    split_ope = [[] for i in range(0, 100)]
    split_index = 0
    division_num = 70
    add_num = 0
    mul_num = 0
    add_num_list = []
    mul_num_list = []
    output_formulas = []
    while(set(knows) != set(alls)):
        knows_tmp = []
        split_tmp = []

        for s in formulas:
            # "square", "mulFp2"などは一般性欠く
            if(s[2] in knows) and (s[3] in knows):
                if(s[0] not in knows):
                    knows_tmp.append(s[0])
                    if s[0] in outputs:
                        output_formulas.append(s)
                    else:
                        split_tmp.append(s)
                        if s[1] == "MONTMUL":
                            mul_num += 1
                        elif s[1] == "ADD" or s[1] == "SUB":
                            add_num += 1                

        # print(mul_num_list)
        # print(add_num_list)
        print(cnt, split_index, len(knows_tmp), knows_tmp)
        if len(split_ope[split_index]) + len(split_tmp) > division_num:
            divided_split_tmp = split_list(split_tmp, division_num)
            for i in range(len(divided_split_tmp)):
                if len(split_ope[split_index]) != 0:
                    split_index += 1
                    cnt = 0
                split_ope[split_index] += divided_split_tmp[i]
            # mul_num_list.append(mul_num)
            # add_num_list.append(add_num)
        else:
            split_ope[split_index] += split_tmp
            # if len(mul_num_list) == 0:
            #     mul_num_list.append(mul_num)
            #     add_num_list.append(add_num)
            # else:
            #     mul_num_list[split_index] = mul_num
            #     add_num_list[split_index] = add_num

        knows += knows_tmp
        cnt += 1
        if cnt > 1:
            split_index += 1
            cnt = 0
    if(set(knows) != set(alls)):
        print("ng:split scheduling")
        exit()
    # split_ope内の[]を取り除く、冗長?
    split_ope_c = []
    for s in split_ope:
        if s != []:
            split_ope_c.append(s)
    if len(split_ope_c) == 0:
        return [output_formulas], input_first, outputs, input_num
    split_ope_c[-1] += output_formulas
    return split_ope_c, input_first, outputs, input_num 
    # return split_ope_c, input_first, outputs, mul_num_list, add_num_list, input_num 


if __name__ == "__main__":
    formulas, mem_table, add_formula_num, mul_formula_num = read_formula_csv("/home/mfukuda/optimal-ate-pairing/scheduling/formulas/bls24/m24_conj.csv")
    split_ope, input_value, output_value, input_num = make_split_scheduling(formulas)
    print(input_value)
    print(output_value)
    # for i in range(len(split_ope)):
    #     print(i, len(split_ope[i]), split_ope[i])
    print("formulas=", formulas)
    print("mem_table=", mem_table)