#!/bin/bash
set -euxo pipefail
# python3 bls12_sche_original.py -n sparse > sparse.log
# python3 bls12_sche_original.py -n SQR012345 > SQR012345.log
# python3 bls12_sche_original.py -n pdbl > pdbl.log
# python3 bls12_sche_original.py -n padd > padd.log
python3 bls12_sche_original.py -n frob > frob.log
# python3 bls12_sche_original.py -n square > square.log
# python3 bls12_sche_original.py -n mul > mul.log
python3 bls12_sche_original.py -n inv > inv.log