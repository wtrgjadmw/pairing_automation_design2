import sys
sys.path.append('./')
import os
import time
import argparse
import importlib
import shutil
from lib.util import read_json
from scheduling.schedule import read_formula_csv, make_pyschedule, find_mistake
from scheduling.split_sche import make_split_scheduling
sys.path.append("..")
from scheduling.debug import reproduce_memtable


def merge_dicts(table):
    new_table = {}
    for entry in table:
        new_table.update(entry)
    return new_table

def copy_and_replace_4padd(input_file, output_file):
    # ファイルをコピー
    shutil.copy2(input_file, output_file)

    # コピー先のファイルを読み取りモードで開く
    with open(output_file, 'r') as file:
        # ファイルの内容を取得
        content = file.read()

    new_content = content.replace("QY", "QY_")

    # コピー先のファイルを書き込みモードで開いて新しい内容を書き込む
    with open(output_file, 'w') as file:
        file.write(new_content)


def copy_and_replace_4mul(input_file, output_file, csv_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    if len(lines) == 5:
        with open(output_file, 'w') as file:
            for i in range(len(lines)):
                if i == 3:
                    print("formulas = ", file=file, end="")
                    print(read_formula_csv(csv_file), file=file)
                else:
                    file.write(lines[i])
    else:
        print("inputファイルが不適切です")


def repeat_schedule(target_dir: str, curve_group: str, curve_name: str, algo_name: str, mul_num: int, add_num: int):
    sys.stdout = open("{}/scheduling/{}.log".format(target_dir, algo_name), "w")
    start_time = time.perf_counter()

    formulas = read_formula_csv(
        "{}/csv/{}.csv".format(target_dir, algo_name)
    )

    # exec(open("./" + "sche_test.py", 'r', encoding="utf-8").read())
    dir_name = "{}/scheduling/{}_mul{}_add{}".format(target_dir, algo_name, mul_num, add_num)
    print(dir_name)

    # スケジューリングの解を保存するリスト
    solution = []
    # 分割したfomulas
    split_ope, input_value, output_value, input_num = make_split_scheduling(formulas)
    split_ope.append([])
    os.makedirs(dir_name, exist_ok=True)
    mem_table_list = []

    for i in range(len(split_ope)):
        print(i, len(split_ope[i]), split_ope[i])

    pre_sche_result = solution

    i = 0
    while i < len(split_ope):
        if len(split_ope[i]) == 0:
            break
        file_name = "{}_{}".format(algo_name, i)
        make_pyschedule(
            dir_name,
            file_name,
            formulas,
            mem_table_list,
            split_ope,
            pre_sche_result,
            i,
            input_value,
            output_value,
            mul_num,
            add_num,
            input_num)
        print(i)
        scheduling_i = importlib.import_module("{}-{}.scheduling.{}_mul{}_add{}.{}".format(curve_group, curve_name, algo_name, mul_num, add_num, file_name))
        solution = scheduling_i.solve()
        if solution == []:
            raise Exception("no solution found in schedule_{}".format(i))
        pre_sche_result = solution
        pre_sche_result, split_ope = find_mistake(formulas, mem_table_list, output_value, split_ope, i, solution)
        i += 1

    end_time = time.perf_counter()
    
    mem_table = merge_dicts(mem_table_list)

    f = open("{}/scheduling/result/{}.txt".format(target_dir, "SPARSE" if "SPARSE" in algo_name else algo_name), "w")
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

    try:
        for filename in os.listdir("./"):
            if filename.endswith(".log") and "clone" in filename:
                file_path = os.path.join("./", filename)
                os.remove(file_path)
        os.remove("./Integer_Program-pulp.lp")
        os.remove("./Integer_Program-pulp.sol")
    except Exception as e:
        print(e)


def all_schedule(curve_group: str, curve_name: str, mul_num: int, add_num: int):
    target_dir = "{}/{}-{}".format(os.path.dirname(os.getcwd()), curve_group, curve_name)
    # os.makedirs("{}/scheduling/result".format(target_dir), exist_ok=True)
    # repeat_schedule(target_dir, curve_group, curve_name, "CONJ", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "FROB", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "MUL", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "PADD", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "PDBL", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "SPARSE", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "SQR", mul_num, add_num)
    repeat_schedule(target_dir, curve_group, curve_name, "SQR012345", mul_num, add_num)
    # repeat_schedule(target_dir, curve_group, curve_name, "INV", mul_num, add_num)

    copy_and_replace_4padd("{}/scheduling/result/PADD.txt".format(target_dir), "{}/scheduling/result/PMINUS.txt".format(target_dir))
    copy_and_replace_4mul("{}/scheduling/result/MUL.txt".format(target_dir), "{}/scheduling/result/MUL_CONJ.txt".format(target_dir), "{}/csv/MUL_CONJ.csv".format(target_dir))


if __name__ == "__main__":
    psr = argparse.ArgumentParser(
        usage='all_schedule.py -c <curve_group> -p <p[bit]> [-h]',
        description='Execute scheduling for all subalgorithms (Point doubling/addition, Fq6 operation) with a 7-stage pipelined Fp montgomery multiplier, four Fp adders/subtractors, an Fp inversion operator.'
    )
    psr.add_argument("-c", "--curve", required=True, help="curve group")
    psr.add_argument("-p", "--characteristic", required=True, help="bit width of characteristic number p")
    psr.add_argument('-m', '--mul', required=False, default=1, help='number of Fp montgomery multipliers (default is 1)')
    psr.add_argument('-a', '--add', required=False, default=4, help='number of Fp adders/subtractors (default is 4)')
    args = psr.parse_args()

    mul_num = int(args.mul)
    add_num = int(args.add)
    curve_group = args.curve
    curve_name = args.characteristic

    param = read_json("{}/{}-{}/param.json".format(os.path.dirname(os.getcwd()), curve_group, curve_name))
    all_schedule(curve_group, curve_name, mul_num, add_num)
