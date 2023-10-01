DIRNAME=
P_BIT=

bls12:
	#!/bin/bash
	set -euxo pipefail
	# cd "$(dirname "$(DIRNAME)")"
	rm -rf ./example/BLS12-$(P_BIT)
	rsync -a ./RTL/ ./example/BLS12-$(P_BIT)/
	python3 ./python/bls12_modify.py ./parameter/bls12/P$(P_BIT)_param.json ./example/BLS12-$(P_BIT)
	python3 ./python/bls12_sequence_write.py ./example/BLS12-$(P_BIT)

bls24:
	#!/bin/bash
	set -euxo pipefail
	# cd "$(dirname "$(DIRNAME)")"
	rsync -a ./RTL/ ./example/BLS24-$(P_BIT)/
	python3 ./python/bls24_modify.py ./parameter/bls24/P$(P_BIT)_param.json ./example/BLS24-$(P_BIT)
	python3 ./python/bls24_sequence_write.py ./example/BLS24-$(P_BIT)