*prerequisite*
python version >= 3.10

1. calculate necessary parameters for pairing (p, r, b, b_t, Tower Extension, twist type, P, Q) from the integer u
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

3. create python scripts for split scheduling


