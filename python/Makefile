DIRNAME=.
CURVE=
P_BIT=

sage: sagemath/bls12.py
	cd ./sagemath
	sagepy bls12.py

csv: export_formula/make_csv.py
	cd ../
	python export_formula/make_csv.py -c $(CURVE) -p $(P_BIT) -f ../parameter/param.json

schedule: scheduling/all_schedule.py
	python scheduling/all_schedule.py  -c $(CURVE) -p $(P_BIT) 

rtl: makeRTL/bls12_modify.py makeRTL/bls12_sequence_write.py
	rsync -a ./RTL/ $(DIRNAME)/$(CURVE)-$(P_BIT)/
	python3 makeRTL/bls12_modify.py ./parameter/bls12/P$(P_BIT)_param.csv $(DIRNAME)/$(CURVE)-$(P_BIT)
	python3 makeRTL/bls12_sequence_write.py $(DIRNAME)/$(CURVE)-$(P_BIT)

all:
	sage
	csv
	schedule
	rtl