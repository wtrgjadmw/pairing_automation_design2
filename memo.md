_prerequisite_
python version >= 3.10

1. calculate necessary parameters for pairing (p, r, b, BT, Tower Extension, twist type, P, Q) from the integer u

```bash
$ cd ./python/sagemath
$ path/to/sage-python bls12.py (or bls24.py)
```

2. create CSV file to list necessary Fp operations and its operand for scheduling

```bash
$ cd ../
$ python export_formula/make_csv.py -c <curve_group> -p <p[bit]> -f ../parameter/param.json
```

note: The test for the CSVs is following;

```bash
$ python export_formula/test.py -c <curve_group> -p <p[bit]> -f ../parameter/param.json
```

3. create python scripts for split scheduling & repeat scheduling

```bash
$ python scheduling/all_schedule.py  -c <curve_group> -p <p[bit]> -m <number_of_multipliers: default=1> -a <number_of_adders: default=4>
```

The command generate text file like `padd_mul1_add4.txt` which contains the information about the algorithm's input, output, scheduling result, formulas, assignment of RAM addresses

4. convert the scheduling result to RTL of sequencer & modify other parts as needed

```bash
$ rsync -a ./RTL/ /BLS12-$(P_BIT)/RTL/
$ python makeRTL/bls12_modify.py python3 makeRTL/bls12_modify.py -c bls12 -p 381
$ python makeRTL/bls12_sequence_write.py $(DIRNAME)/BLS12-$(P_BIT)
```
