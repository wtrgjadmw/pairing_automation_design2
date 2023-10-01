#!/bin/bash
set -euxo pipefail
# cd "$(dirname "$0")"
rsync -a ./RTL/ ../BLS24-$1/
python3 ./python/bls24_modify.py ./parameter/bls24/P$1_param.csv ../BLS24-$1
python3 ./python/bls24_sequence_write.py ../BLS24-$1