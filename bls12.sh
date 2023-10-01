#!/bin/bash
set -euxo pipefail
# cd "$(dirname "$0")"
rm -rf ../BLS12-$1
rsync -a ./RTL/ ../BLS12-$1/
python3 ./python/bls12_modify.py ./parameter/bls12/P$1_param.csv ../BLS12-$1
python3 ./python/bls12_sequence_write.py ../BLS12-$1