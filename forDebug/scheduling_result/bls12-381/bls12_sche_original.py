from split_sche import make_split_scheduling, read_formula_csv
from io import TextIOWrapper
import sys, csv, time, re
import copy
import os 
import argparse
args = sys.argv

alpha2num = lambda c: ord(c) - ord('A')


def find_prev_formula(formulas, operand):
    for formula in formulas:
        if formula[0] == operand:
            return formula
    return None

def find_prev_resource(pre_sche_result, operand):
    for pre in pre_sche_result:
        if pre[0] == operand:
            resource = pre[1][:-1]
            resource_num = pre[1][-1]
            end_time = int(pre[3])
            return resource, resource_num, end_time
    return None, None, None

def make_mem_task_definition(f_write: TextIOWrapper, input_value, pre_sche_result, formulas, value, operands: list, MULnum: int, ADDnum: int):
    if operands[0] == operands[1]:
        operand_num = 1
    else:
        operand_num = 2
    for i in range(operand_num):
        operand = operands[i]
        mem_value_name = "{0}_mem{1}".format(value, i)
        # mem_table[mem_value_name] = operand
        if operand in input_value:
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            f_write.write("\t{0} += INPUT_mem_r\n".format(mem_value_name))
        else:
            formula = find_prev_formula(formulas, operand)
            pre_resource, pre_resource_num, pre_end_time = find_prev_resource(pre_sche_result, operand)
            if formula is None:
                raise Exception("can't find previous formula")
            opcode = formula[1]
            if opcode == "INV":
                f_write.write("\tS += {0}<{1}\n\n".format(operand, value))
                continue
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            if opcode == "MONTMUL":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(MUL_mem)\n".format(mem_value_name))
                    for j in range(MULnum):
                        f_write.write("\tS += ({0}*MUL[{3}])-1<{1}_mem{2}*MUL_mem[{3}]\n".format(operand, value, i, j))
                else:
                    f_write.write("\t{0} += MUL_mem[{1}]\n".format(mem_value_name, pre_resource_num))
                    f_write.write("\tS += {1}<{0}\n".format(mem_value_name, operand))
            elif opcode == "ADD" or opcode == "SUB":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(ADD_mem)\n".format(mem_value_name))
                    for j in range(ADDnum):
                        f_write.write("\tS += ({0}*ADD[{3}])-1<{1}_mem{2}*ADD_mem[{3}]\n".format(operand, value, i, j))
                else:
                    f_write.write("\t{0} += ADD_mem[{1}]\n".format(mem_value_name, pre_resource_num))
                    f_write.write("\tS += {1}<{0}\n".format(mem_value_name, operand))
        f_write.write("\tS += {1}<={0}\n\n".format(value, mem_value_name))

def find_mistake(split_ope, depth, pre_sche_result, output_value):
    mistakes = []
    for formula in split_ope[depth]:
        suffixes = ["", "_mem0", "_mem1", "_in", "_w"]
        cnt = 0
        exclude_results = []
        # prev_formula = find_prev_formula(formula, formu)
        if formula[2] == formula[3]: # "_mem1" is not exist
            cnt += 1
        # if formula[2] == "T4_13T3" or formula[3] == "T4_13T3":
        #     cnt += 1
        if formula[1] != "MONTMUL": # "_in" is not exist
            cnt += 1
        if formula[0] not in output_value: # "_w" is not exist
            cnt += 1

        for sol in pre_sche_result:
            for suffix in suffixes:
                if formula[0]+suffix == sol[0]:
                    cnt += 1
                    exclude_results.append(sol)
                    break

        if cnt != 5:
            for exclude_result in exclude_results:
                pre_sche_result.remove(exclude_result)
            mistakes.append(formula)
            print(formula, cnt)
    # print(mistakes)
        # split_ope[depth] = mistakes + split_ope[depth]
    return pre_sche_result, mistakes

def make_pyschedule(file_name, formulas, mem_table, split_ope, pre_sche_result, depth, filename_write, input_value, output_value, MULnum, ADDnum, input_num):
    scheduling_title = file_name + "_" + str(depth)

    f_write = open(filename_write, "w")
    f_write.write("from pyschedule import Scenario, solvers, plotters, alt\n\n")
    f_write.write("def solve_{0}(ConstStep, ExpStep):\n".format(scheduling_title))

    # mul_cycle = mul_num_list[depth]
    # add_cycle = (add_num_list[depth] // ADDnum)
    pre_cycle = 0
    if pre_sche_result != []:
        pre_cycle = int(pre_sche_result[-1][3])
    f_write.write("\thorizon = {0}\n".format(max(pre_cycle+90, input_num//2+50)))
    # f_write.write("\thorizon = {0}\n".format(max(mul_cycle+70, add_cycle+70, pre_cycle+90, input_num//2+50)))
        
    f_write.write("\tS=Scenario(\"" + scheduling_title + "\",horizon = horizon)\n")

    f_write.write("\n\t# resource\n")
    f_write.write("\tMUL = S.Resources('MUL', num={0}, size=7)\n".format(MULnum))
    f_write.write("\tMUL_in = S.Resources('MUL_in', num={0})\n".format(MULnum))
    f_write.write("\tINV = S.Resource('INV')\n")
    f_write.write("\tADD = S.Resources('ADD', num={0}, periods=range(1, horizon))\n".format(ADDnum))

    # 1write-2read RAM
    f_write.write("\tMUL_mem = S.Resources('MUL_mem', num={0}, size=2)\n".format(MULnum))
    f_write.write("\tADD_mem = S.Resources('ADD_mem', num={0}, size=2)\n".format(ADDnum))

    # 2write-2read RAM
    f_write.write("\tINPUT_mem_w = S.Resource('INPUT_mem_w', size=2)\n")
    f_write.write("\tINPUT_mem_r = S.Resource('INPUT_mem_r', size=2)\n")

    multi_resources = ["MUL", "MUL_in", "ADD", "MUL_mem", "ADD_mem"]
    single_resources = ["INV", "INPUT_mem_w", "INPUT_mem_r"]

    f_write.write("\n\t# result of previous scheduling\n")

    # pre_tasks = [[]] if depth == 0 else split_ope[depth-1]
    input_last_used_time = 0
    for pre in pre_sche_result:
        task = pre[0]
        # for pre_task in pre_tasks:
        #     if pre_task[0] == task:
        #         pre_tasks.remove(pre_task)
        start_time = int(pre[2])
        end_time = int(pre[3])
        length = end_time - start_time
        f_write.write("\t{0} = S.Task('{0}', length={1}, delay_cost=1)\n".format(task, length))
        f_write.write("\tS += {0} >= {1}\n".format(task, start_time))
        if pre[1] in single_resources:
            f_write.write("\t{0} += {1}\n\n".format(task, pre[1]))
        else:
            resource = pre[1][:-1]
            resource_num = pre[1][-1]
            f_write.write("\t{0} += {1}[{2}]\n\n".format(task, resource, resource_num))
        for i in range(2):
            mem_name = "{0}_mem{1}".format(task, i)
            if mem_name in mem_table.keys() and mem_table[mem_name] in input_value:
                input_last_used_time = max(input_last_used_time, start_time) 

    f_write.write("\n\t# new tasks\n")

    for line in split_ope[depth]:
        if line[1] == "MONTMUL":
            f_write.write("\t{0}_in = S.Task('{0}_in', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + "_in += alt(MUL_in)\n")
            f_write.write("\t{0} = S.Task('{0}', length=7, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(MUL)\n")
            f_write.write("\tS+={0}>={0}_in\n\n".format(line[0]))
        elif line[1] == "CONST":
            f_write.write("\t{0} = S.Task('{0}', length=ConstStep, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(CONST)\n\n")
        elif line[1] == "EXP":
            f_write.write("\t{0} = S.Task('{0}', length=ExpStep, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(EXP)\n\n")
        elif line[1] == "ADD" or line[1] == "SUB":
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(ADD)\n\n")
        elif line[1] == "INV":
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(INV)\n\n")
        else:
            raise Exception("ERROR: invalid operand: " + line[1])
        make_mem_task_definition(f_write, input_value, pre_sche_result, formulas, line[0], [line[2], line[3]], MULnum, ADDnum)
        if line[0] in output_value:
            f_write.write("\t{0}_w = S.Task('{0}_w', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t{0}_w += alt(INPUT_mem_w)\n".format(line[0]))
            if depth != 0:
                f_write.write("\tS += {0} < {1}_w\n".format(input_last_used_time, line[0]))
            f_write.write("\tS += {0}-1 <= {0}_w\n\n".format(line[0]))

    
    f_write.write("\tsolvers.mip.solve(S,msg=1,kind='CPLEX', time_limit=3600)\n\n")
    f_write.write("\tsolution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]\n")
    f_write.write("\tfor i in range(len(S.solution())):\n\t\tfor j in range(len(S.solution()[i])):\n\t\t\tsolution[i][j]=str(S.solution()[i][j])\n")
    f_write.write("\tprint(solution)\n\n")
    f_write.write("\tcycles = int(solution[-1][3])\n\n")

    # TODO: pic_file_nameの変更
    f_write.write("\tpic_file_name = \"" + file_name + "/" + scheduling_title + ".png\"\n")
    f_write.write("\tif(S.solution() != []):\n\t\tplotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)\n\n")
    f_write.write("\treturn solution\n\n")
    f_write.write("if __name__ == \"__main__\":\n")
    f_write.write("\tsolution = solve_"+scheduling_title+"(0, 0)")
    return

def write_result(file_name, input_value, output_value, solution, formulas, mem_table):
    f = open(file_name+".txt", "w")
    print("input = ", file=f, end="")
    print(input_value, file=f)
    print("output = ", file=f, end="")
    print(output_value, file=f)
    print("solution = ", file=f, end="")
    print(solution, file=f)
    print("formulas = ", file=f, end="")
    print(formulas, file=f)
    print("mem_table = ", file=f, end="")
    print(mem_table, file=f)
    f.close()

def file_replace(old_filename, new_filename, old_str, new_str):
    with open(old_filename, "r") as file:
        content = file.read()
    updated_content = content.replace(old_str, new_str)
    with open(new_filename, "w") as file:
        file.write(updated_content)


if __name__ == "__main__":

    start_time = time.perf_counter()
    psr  = argparse.ArgumentParser(
        prog='プログラムの名前',
        usage='プログラムの使い方',
        description='プログラムの説明'
    )
    psr.add_argument('-m', '--mul', default=1, help='乗算器の個数')
    psr.add_argument('-a', '--add', default=4, help='加減算器の個数')
    psr.add_argument('-n', '--name', required=True, help='スケジューリング対象の名前')
    args = psr.parse_args()

    mul_num = int(args.mul)
    add_num = int(args.add)
    algo_name = args.name

    func_name = "{2}_mul{0}_add{1}".format(mul_num, add_num, algo_name)
    formulas, mem_table, add_formula_num, mul_formula_num = read_formula_csv("/home/mfukuda/optimal-ate-pairing/scheduling/formulas/bls12/{0}.csv".format(algo_name))

    #exec(open("./" + "sche_test.py", 'r', encoding="utf-8").read())
    file_name = func_name

    # スケジューリングの解を保存するリスト
    solution = []
    # 分割したfomulas
    split_ope, input_value, output_value, input_num = make_split_scheduling(formulas)
    split_ope.append([])
    os.makedirs(file_name, exist_ok=True)

    for i in range(len(split_ope)) :
        print(i, len(split_ope[i]), split_ope[i])
    # print(len(split_ope))
    # print(mul_num_list)
    # print(add_num_list)
    print(input_value)
    print(output_value)

    pre_sche_result = solution

    for i in range(len(split_ope)):
        if len(split_ope[i]) == 0:
            continue
        write_file = "./{0}/{0}_{1}.py".format(file_name, i)
        make_pyschedule(file_name, formulas, mem_table, split_ope, pre_sche_result, i, write_file, input_value, output_value, mul_num, add_num, input_num)
        exec(open(write_file).read())
        if solution == []:
            raise Exception("no solution found in schedule_{0}".format(i))
        pre_sche_result, mistakes = find_mistake(split_ope, i, solution, output_value)
        if i != len(split_ope)-1:
            split_ope[i+1] = mistakes + split_ope[i+1]

    write_result(file_name, input_value, output_value, solution, formulas, mem_table)

    if algo_name == "padd":
        pminus_filename = "{2}_mul{0}_add{1}".format(mul_num, add_num, "pminus")
        file_replace(file_name+".txt", pminus_filename+".txt", "QY", "QY_")
    elif algo_name == "mul":
        conj_formulas, conj_mem_table, add_formula_num, mul_formula_num = read_formula_csv("/home/mfukuda/optimal-ate-pairing/scheduling/formulas/bls12/{0}.csv".format("mul_conj"))
        conj_filename = "{2}_mul{0}_add{1}".format(mul_num, add_num, "conj")
        write_result(conj_filename, input_value, output_value, solution, formulas, conj_mem_table)

    for filename in os.listdir("./"):
        if filename.endswith(".log") and "clone" in filename:
            file_path = os.path.join("./", filename)
            os.remove(file_path)

    end_time = time.perf_counter()
    print("time = ", end_time - start_time)
    # # os.remove("./Integer_Program-pulp.lp")
    # # os.remove("./Integer_Program-pulp.sol")
