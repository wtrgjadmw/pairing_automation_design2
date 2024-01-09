# NOTE: formulaを普通の配列ではなく双方向リストにしようとしている

from scheduling.split_sche import make_split_scheduling
from io import TextIOWrapper
import sys
import csv
import time
import re
import os
import argparse
args = sys.argv


def alpha2num(c): return ord(c) - ord('A')


class Formula:
    def __init__(self, val, operator, opr1, opr2):
        self.val = val
        self.operator = operator
        self.opr1 = opr1
        self.opr2 = opr2
        self.prev = None


def read_formula_csv(filename):
    f_read = open(filename, "r")
    formulas = []
    for line in csv.reader(f_read):
        if len(line) > 0 and line[0][0] == '#':
            continue
        if len(line) == 4:
            formulas.append([line[0], line[3], line[1], line[2]])
    f_read.close()
    return formulas


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


def make_mem_task_definition(
        f_write: TextIOWrapper,
        input_value,
        pre_sche_result,
        formulas,
        mem_table,
        value,
        operands: list,
        MULnum: int,
        ADDnum: int):
    for i in range(len(operands)):
        operand = operands[i]
        mem_value_name = "{0}_mem{1}".format(value, i)
        mem_table[mem_value_name] = operand
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
                f_write.write("\tS += {0}<{1}\n".format(operand, value))
                continue
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(mem_value_name))
            if opcode == "MUL":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(MUL_mem)\n".format(mem_value_name))
                    for j in range(MULnum):
                        f_write.write("\tS += ({0}*MUL[{3}])-1<{1}_mem{2}*MUL_mem[{3}]\n".format(operand, value, i, j))
                else:
                    f_write.write("\t{0} += MUL_mem[{1}]\n".format(mem_value_name, pre_resource_num))
                    f_write.write("\tS += {1}<{0}\n".format(mem_value_name, pre_end_time - 1))
            elif opcode == "ADD" or opcode == "SUB":
                if pre_resource is None:
                    f_write.write("\t{0} += alt(ADD_mem)\n".format(mem_value_name))
                    for j in range(ADDnum):
                        f_write.write("\tS += ({0}*ADD[{3}])-1<{1}_mem{2}*ADD_mem[{3}]\n".format(operand, value, i, j))
                else:
                    f_write.write("\t{0} += ADD_mem[{1}]\n".format(mem_value_name, pre_resource_num))
                    f_write.write("\tS += {1}<{0}\n".format(mem_value_name, pre_end_time - 1))
        f_write.write("\tS += {1}<={0}\n\n".format(value, mem_value_name))


def find_mistake(split_ope, depth, pre_sche_result):
    mistaken_formulas = []
    for i in range(0, depth):
        for formula in split_ope[i]:
            is_exist = False
            mem_is_exist = False
            mem_results = []
            min_finish_time = 1000
            for sol in pre_sche_result:
                if formula[0] == sol[0]:
                    is_exist = True
                elif formula[0] in sol[0]:
                    mem_is_exist = True
                    mem_results.append(sol)
            if not is_exist:
                if mem_is_exist:
                    for mem_result in mem_results:
                        pre_sche_result.remove(mem_result)
                for next_formula in split_ope[i+1]:
                    if (next_formula[2] == formula[0]) or (next_formula[3] == formula[0]):
                        for sol in pre_sche_result:
                            if formula[0] == sol[0]:
                                min_finish_time = min(min_finish_time, int(sol[2]))
                mistaken_formulas.append(formula + [min_finish_time])
    split_ope[depth] = mistaken_formulas + split_ope[depth]
    return pre_sche_result, split_ope


def make_pyschedule(
        dir_name,
        file_name,
        formulas,
        mem_table,
        split_ope,
        pre_sche_result,
        depth,
        input_value,
        output_value,
        MULnum,
        ADDnum,
        input_num):
    # def make_pyschedule(file_name, formulas, mem_table, split_ope,
    # pre_sche_result, depth, filename_write, input_value, MULnum, ADDnum,
    # mul_num_list, add_num_list, input_num):

    f_write = open("{}/{}.py".format(dir_name, file_name), "w")
    f_write.write("from pyschedule import Scenario, solvers, plotters, alt\n\n\n")
    f_write.write("def solve():\n")

    # mul_cycle = mul_num_list[depth]
    # add_cycle = (add_num_list[depth] // ADDnum)
    pre_cycle = 0
    if pre_sche_result != []:
        pre_cycle = int(pre_sche_result[-1][3])
    f_write.write("\thorizon = {0}\n".format(max(pre_cycle + 90, input_num // 2 + 50)))
    # f_write.write("\thorizon = {0}\n".format(max(mul_cycle+70, add_cycle+70, pre_cycle+90, input_num//2+50)))

    f_write.write("\tS = Scenario(\"" + file_name + "\", horizon=horizon)\n")

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
    output_limit = {}
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
            if mem_name in mem_table.keys() and re.match(r"[A-B][0-2]+", mem_table[mem_name]):
                if mem_table[mem_name][1:] in output_limit.keys():
                    output_limit[mem_table[mem_name][1:]] = max(output_limit[mem_table[mem_name][1:]], end_time)
                else:
                    output_limit[mem_table[mem_name][1:]] = end_time

    f_write.write("\n\t# new tasks\n")

    for line in split_ope[depth]:
        if line[1] == "MUL":
            f_write.write("\t{0}_in = S.Task('{0}_in', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + "_in += alt(MUL_in)\n")
            f_write.write("\t{0} = S.Task('{0}', length=7, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(MUL)\n")
            f_write.write("\tS += {0}>={0}_in\n\n".format(line[0]))
        elif line[1] == "ADD" or line[1] == "SUB":
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(ADD)\n\n")
        elif line[1] == "INV":
            f_write.write("\t{0} = S.Task('{0}', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t" + line[0] + " += alt(INV)\n\n")
        else:
            raise Exception("ERROR: invalid operand: " + line[1])
        if len(line) == 5:
            f_write.write("\tS += {}<{}\n\n".format(line[0], line[4]))
        make_mem_task_definition(f_write, input_value, pre_sche_result, formulas, mem_table, line[0], [line[2], line[3]], MULnum, ADDnum)
        if line[0] in output_value:
            f_write.write("\t{0}_w = S.Task('{0}_w', length=1, delay_cost=1)\n".format(line[0]))
            f_write.write("\t{0}_w += alt(INPUT_mem_w)\n".format(line[0]))
            if re.match(r"C[0-2]+", line[0]) and line[0][1:] in output_limit.keys():
                f_write.write("\tS += {0} < {1}_w\n".format(output_limit[line[0][1:]], line[0]))
            f_write.write("\tS += {0}-1 <= {0}_w\n\n".format(line[0]))

    f_write.write("\tsolvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)\n\n")
    f_write.write("\tsolution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]\n")
    f_write.write("\tfor i in range(len(S.solution())):\n\t\tfor j in range(len(S.solution()[i])):\n\t\t\tsolution[i][j]=str(S.solution()[i][j])\n")
    f_write.write("\tprint(solution)\n\n")
    f_write.write("\tcycles = int(solution[-1][3])\n\n")

    # TODO: pic_file_nameの変更
    f_write.write("\tpic_file_name = \"{}/{}.png\"\n".format(dir_name, file_name))
    f_write.write("\tif(S.solution() != []):\n\t\tplotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)\n\n")
    f_write.write("\treturn solution\n\n")
    return


if __name__ == "__main__":
    start_time = time.perf_counter()
    psr = argparse.ArgumentParser(
        prog='プログラムの名前',
        usage='プログラムの使い方',
        description='プログラムの説明'
    )
    psr.add_argument('-m', '--mul', default=1, help='乗算器の個数')
    psr.add_argument('-a', '--add', default=4, help='加減算器の個数')
    psr.add_argument("-c", "--curve", required=True, help="楕円曲線群")
    psr.add_argument("-p", "--characteristic", required=True, help="楕円曲線の標数のbit幅")
    psr.add_argument('-n', '--name', required=True, help='スケジューリング対象の名前')
    args = psr.parse_args()

    mul_num = int(args.mul)
    add_num = int(args.add)
    curve_group = args.curve
    curve_name = args.characteristic
    algo_name = args.name

    func_name = "{2}_mul{0}_add{1}".format(mul_num, add_num, algo_name)
    formulas, add_formula_num, mul_formula_num = read_formula_csv(
        "/home/mfukuda/pairing_automation_design/{}-{}/csv/{}.csv".format(curve_group, curve_name, algo_name)
    )

    # exec(open("./" + "sche_test.py", 'r', encoding="utf-8").read())
    file_name = func_name

    # スケジューリングの解を保存するリスト
    solution = []
    # 分割したfomulas
    split_ope, input_value, output_value, input_num = make_split_scheduling(formulas)
    split_ope.append([])
    os.makedirs(file_name, exist_ok=True)
    mem_table = {}

    for i in range(len(split_ope)):
        print(i, len(split_ope[i]), split_ope[i])

    pre_sche_result = solution

    for i in range(len(split_ope)):
        # pre_sche_result, split_ope = find_mistake(split_ope, i, pre_sche_result)
        if len(split_ope[i]) == 0:
            continue
        write_file = "{0}/{0}_{1}.py".format(file_name, i)
        make_pyschedule(
            file_name,
            formulas,
            mem_table,
            split_ope,
            pre_sche_result,
            i,
            write_file,
            input_value,
            output_value,
            mul_num,
            add_num,
            input_num)
        print(i)
        # print(split_ope[i])
        # make_pyschedule(file_name, formulas, mem_table, split_ope, pre_sche_result, i, write_file, input_value, mul_num, add_num, mul_num_list, add_num_list, input_num)
        exec(open(write_file).read())
        if solution == []:
            raise Exception("no solution found in schedule_{0}".format(i))
        pre_sche_result = solution

    end_time = time.perf_counter()

    f = open(file_name + ".txt", "w")
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
    print("time = ", end_time - start_time)

    for filename in os.listdir("./"):
        if filename.endswith(".log") and "clone" in filename:
            file_path = os.path.join("./", filename)
            os.remove(file_path)
    os.remove("./Integer_Program-pulp.lp")
    os.remove("./Integer_Program-pulp.sol")
