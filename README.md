# pairing_automation_design

Under implementation...

This is an automatic design tool for optimized pairing hardware accelerator of ASIC. This can be used for multiple pairing-friendly curves, so it helps to compare the curves in terms of security level, latency, chip area and power.

# How to use

## Prerequisite
- python version >= 3.10
- [sagemath](https://doc.sagemath.org/html/en/index.html) version >= 10.4 
- scheduler: [CPLEX](https://www.ibm.com/jp-ja/products/ilog-cplex-optimization-studio)

## Steps
1. Calculate necessary parameters for pairing (p, r, b, BT, Tower Extension, twist type, P, Q) from the integer u

```bash
$ cd ./python/sagemath
$ path/to/sage-python bls12.py (or bls24.py) -u <unique_parameter> 
```

2. Create CSV file to list necessary Fp operations and its operand for scheduling

```bash
$ cd ../
$ python export_formula/make_csv.py -c <curve_group> -p <p[bit]> -f ../parameter/param.json
```

note: The test for the CSVs is following;

```bash
$ python export_formula/test.py -c <curve_group> -p <p[bit]> -f ../parameter/param.json
```

3. Create python scripts for split scheduling & repeat scheduling

```bash
$ python scheduling/all_schedule.py  -c <curve_group> -p <p[bit]> -m <number_of_multipliers: default=1> -a <number_of_adders: default=4>
```

The command generates text file like `padd_mul1_add4.txt` which contains the information about the algorithm's input, output, scheduling result, formulas, assignment of RAM addresses

4. Convert the scheduling result to RTL of sequencer & modify other parts as needed

```bash
$ python makeRTL/<curve_group>_modify.py -c <curve_group> -p <p[bit]>
$ python makeRTL/write_sequence.py -c <curve_group> -p <p[bit]>
```
