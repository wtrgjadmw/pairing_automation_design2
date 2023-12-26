import sys
import os
import time
import argparse
import importlib
from scheduling.schedule import read_formula_csv, make_pyschedule, find_mistake
from scheduling.split_sche import make_split_scheduling


def repeat_schedule(curve_group: str, curve_name: str, algo_name: str, mul_num: int, add_num: int):
    sys.stdout = open("./{}.log".format(algo_name), "w")
    start_time = time.perf_counter()

    func_name = "{2}_mul{0}_add{1}".format(mul_num, add_num, algo_name)
    formulas = read_formula_csv(
        "/home/mfukuda/pairing_automation_design/csv/{}/{}/{}.csv".format(curve_group, curve_name, algo_name)
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

    i = 0
    while i < len(split_ope):
        if len(split_ope[i]) == 0:
            break
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
        scheduling_i = importlib.import_module("{0}.{0}_{1}".format(file_name, i))
        # print(split_ope[i])
        # make_pyschedule(file_name, formulas, mem_table, split_ope, pre_sche_result, i, write_file, input_value, mul_num, add_num, mul_num_list, add_num_list, input_num)
        # exec(open(write_file).read())
        solution = scheduling_i.solve()
        if solution == []:
            raise Exception("no solution found in schedule_{0}".format(i))
        pre_sche_result = solution
        i += 1
        pre_sche_result, split_ope = find_mistake(split_ope, i, pre_sche_result)

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


def all_schedule(curve_group: str, curve_name: str, mul_num: int, add_num: int):
    # repeat_schedule(curve_group, curve_name, "CONJ", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "FROB", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "MUL", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "PADD", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "PDBL", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "SPARSE_D", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "SPARSE_M", mul_num, add_num)
    # repeat_schedule(curve_group, curve_name, "SQR", mul_num, add_num)
    repeat_schedule(curve_group, curve_name, "SQR012345", mul_num, add_num)


if __name__ == "__main__":
    psr = argparse.ArgumentParser(
        prog='プログラムの名前',
        usage='プログラムの使い方',
        description='プログラムの説明'
    )
    psr.add_argument('-m', '--mul', default=1, help='乗算器の個数')
    psr.add_argument('-a', '--add', default=4, help='加減算器の個数')
    psr.add_argument("-c", "--curve", required=True, help="楕円曲線群")
    psr.add_argument("-p", "--characteristic", required=True, help="楕円曲線の標数のbit幅")
    args = psr.parse_args()

    mul_num = int(args.mul)
    add_num = int(args.add)
    curve_group = args.curve
    curve_name = args.characteristic
    all_schedule(curve_group, curve_name, mul_num, add_num)
