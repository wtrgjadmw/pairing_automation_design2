DIRNAME=.
P_BIT=

bls12_debug:
	#!/bin/bash
	set -euxo pipefail
	# cd "$(dirname "$(DIRNAME)")"
	rm -rf $(DIRNAME)/BLS12-$(P_BIT)
	rsync -a ./RTL/ $(DIRNAME)/BLS12-$(P_BIT)/
	python3 ./python/bls12_modify.py ./parameter/bls12/P$(P_BIT)_param.csv $(DIRNAME)/BLS12-$(P_BIT)
	python3 ./forDebug/bls12_sequence_write.py $(DIRNAME)/BLS12-$(P_BIT)

bls12:
	#!/bin/bash
	set -euxo pipefail
	# cd "$(dirname "$(DIRNAME)")"
	rm -rf $(DIRNAME)/BLS12-$(P_BIT)
	rsync -a ./RTL/ $(DIRNAME)/BLS12-$(P_BIT)/
	python3 ./python/bls12_modify.py ./parameter/bls12/P$(P_BIT)_param.csv $(DIRNAME)/BLS12-$(P_BIT)
	python3 ./python/bls12_sequence_write.py $(DIRNAME)/BLS12-$(P_BIT)

bls24:
	#!/bin/bash
	set -euxo pipefail
	# cd "$(dirname "$(DIRNAME)")"
	rsync -a ./RTL/ $(DIRNAME)/BLS24-$(P_BIT)/
	python3 ./python/bls24_modify.py ./parameter/bls24/P$(P_BIT)_param.csv $(DIRNAME)/BLS24-$(P_BIT)
	python3 ./python/bls24_sequence_write.py $(DIRNAME)/BLS24-$(P_BIT)

clear:
	rm -rf python/__pycache__