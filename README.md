# pairing_automation_design

Under implementation...

This is an automatic design tool for optimized pairing hardware accelerator of ASIC. This can be used for multiple pairing-friendly curves, so it helps to compare the curves in terms of security level, latency, chip area and power.

# How to use
example: for BLS12-381,
```bash
$ make bls12 P_BIT=381
```
If you want other curves than BLS12-381, 446, BLS24-315, 317, 509, you have to add a parameter file to `./parameter` directory.

# Note
Supported curve groups: BLS12, BLS24
