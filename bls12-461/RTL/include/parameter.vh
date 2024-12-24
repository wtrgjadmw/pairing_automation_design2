// for wrapper -------------------------------------------------------------------------------------------------

// modes for the wrapper
`define I_INPUTMODE_SIZE    2
`define REF_RESULT                       2'd0
`define INPUT_COORD_CORE                 2'd1
`define EXEC_CORE                        2'd2
`define INPUT_CMD_CORE                   2'd3

// modes for the calculation core -------------------------------------------------------------------------------------------------
`define MODE_SIZE 'd4

// `define MODE_PDBL_FIRST 4'b0000
`define MODE_PDBL 4'b0001
`define MODE_PADD 4'b0010
`define MODE_PMINUS 4'b0011
`define MODE_SQUARE 4'b0100
`define MODE_SPARSE_MUL 4'b0101
`define MODE_CONJ 4'b0110
`define MODE_MUL 4'b0111
`define MODE_FROB 4'b1000
`define MODE_INV 4'b1001
`define MODE_MUL_CONJ 4'b1010
`define MODE_SQR012345 4'b1011

// for command buffer -----------------------------------------------------------------------------
// modes for the core 
`define CMD_SIZE   `MODE_SIZE + `RAM_ADDR_SIZE * 3

`define CMD_INSTTYPE 'd1
`define inst_ML 'b0
`define inst_FE 'b1
// for RAM -----------------------------------------------------------------------------

`define RAM_DEPTH 114
`define RAM_ADDR_SIZE 7


`define RAM_PX	    `RAM_ADDR_SIZE'd0
`define RAM_PY_	    `RAM_ADDR_SIZE'd1
`define RAM_BT0	    `RAM_ADDR_SIZE'd2
`define RAM_BT1	    `RAM_ADDR_SIZE'd3
`define RAM_PX_	    `RAM_ADDR_SIZE'd4
`define RAM_PY      `RAM_ADDR_SIZE'd5
`define RAM_QX0	    `RAM_ADDR_SIZE'd6
`define RAM_QX1	    `RAM_ADDR_SIZE'd7
`define RAM_QY0	    `RAM_ADDR_SIZE'd8
`define RAM_QY1	    `RAM_ADDR_SIZE'd9
`define RAM_QY_0	`RAM_ADDR_SIZE'd10
`define RAM_QY_1	`RAM_ADDR_SIZE'd11
`define RAM_TX0	    `RAM_ADDR_SIZE'd12
`define RAM_TX1	    `RAM_ADDR_SIZE'd13
`define RAM_TY0	    `RAM_ADDR_SIZE'd14
`define RAM_TY1	    `RAM_ADDR_SIZE'd15
`define RAM_TZ0	    `RAM_ADDR_SIZE'd16
`define RAM_TZ1	    `RAM_ADDR_SIZE'd17

`define RAM_XI10	`RAM_ADDR_SIZE'd18
`define RAM_XI11	`RAM_ADDR_SIZE'd19
`define RAM_XI20	`RAM_ADDR_SIZE'd20
`define RAM_XI21	`RAM_ADDR_SIZE'd21
`define RAM_XI30	`RAM_ADDR_SIZE'd22
`define RAM_XI31	`RAM_ADDR_SIZE'd23
`define RAM_XI40	`RAM_ADDR_SIZE'd24
`define RAM_XI41	`RAM_ADDR_SIZE'd25
`define RAM_XI50	`RAM_ADDR_SIZE'd26
`define RAM_XI51	`RAM_ADDR_SIZE'd27
`define RAM_ZERO	`RAM_ADDR_SIZE'd28
`define RAM_ONE	    `RAM_ADDR_SIZE'd29

`define RAM_A	`RAM_ADDR_SIZE'd30
`define RAM_B	`RAM_ADDR_SIZE'd42
`define RAM_C	`RAM_ADDR_SIZE'd54
`define RAM_D	`RAM_ADDR_SIZE'd66
`define RAM_E	`RAM_ADDR_SIZE'd78
`define RAM_F	`RAM_ADDR_SIZE'd90
`define RAM_G	`RAM_ADDR_SIZE'd102

// constants -------------------------------------------------------------------------------------------------
`define WORD_SIZE 'd461
`define CHAR 461'h15555545554d5a555a55d69414935fbd6f1e32d8bacca47b14848b42a8dffa5c1cc00f26aa91557f00400020000555554aaaaaac0000aaaaaaab
`define CHAR_INV 461'h90da93ec05ba426feac8a3e18f2aab3b447b94da8787b3a4bb9eb18bd2ab03be768ccc5eb29eeb2827301b18017ffcf9ff4000c0005fffffffd
`define INVERSION_INITIAL_VALUE 461'h36495ca7783ee736195beac4e818196020185607704329eeea5d102f2886ffc00a1c5c1fdb464df0825a7b7e10ef770a6a634a8e9143cafe28a
`define CHAR_3X 463'h3fffffcfffe80f000f0183bc3dba1f384d5a988a3065ed713d8da1c7fa9fef1456402d73ffb4007d00c00060000fffffe0000004000200000001

// parameters for twisted curve (Ep2)
`define BT0 461'h60002fe1ffe1fcf887848bc18f654aceeb9f34251d84e4bc700ac021d7537fa5180097ff05fe7fff3fffe000003ffffff7fffbfffffffe
`define BT1 461'h60002fe1ffe1fcf887848bc18f654aceeb9f34251d84e4bc700ac021d7537fa5180097ff05fe7fff3fffe000003ffffff7fffbfffffffe
// // constants independent from elliptic curve
`define ZERO 461'd0
`define ONE 461'haaaaabaaab2a5aaa5aa296beb6ca04290e1cd2745335b84eb7b74bd572005a3e33ff0d9556eaa80ffbfffdffffaaaaab5555553ffff55555555

// Frobenius pre-calculated coefficients
`define XI10 461'h3873eb41c37b45e263a0690045208962a82e724978e43ea294d5c16b3cb1319a5925a1af582c64ae6bc6f83d74137080d76b0b0259d458e06e1
`define XI11 461'h11ce16913915a5f7341bd00410415727449b4bb4233e6090eb372f2bf514e742772db50bb50e8f341983909c28c41e4d3d33f9fbda63651ca3ca
`define XI20 461'h0
`define XI21 461'h13807c4a44b6478908f968a7be3fe4d9ac327d062187e9365cdc0819a18830c076e1d39f76cbda2548a4ac3b1a282f1fa75b423d1a60d4c55ccf
`define XI30 461'h2f310c358b429633d9883e97779b173192f8550e6f4006f6730edae4697a176ebf2897c335fbd6b2cdd7787e14da8bbce12db93dfa5570caf3f
`define XI31 461'h2f310c358b429633d9883e97779b173192f8550e6f4006f6730edae4697a176ebf2897c335fbd6b2cdd7787e14da8bbce12db93dfa5570caf3f
`define XI40 461'h8d5d1bf9a1b92de544dbb7f9519255ecdf61754abeea04033d2f1944fc83c083d61b55221a92f274824abfb1a1d84751205ece51a5f7f700779
`define XI41 461'h0
`define XI50 461'h67a4f7774ebddc163d28a797bcbba0943b26c757e824459907e49c4fa62b4909184e39728e283b61399e70bb88edfc3db898c4405429c9ab620
`define XI51 461'hedb05cde0617c93f6834c1a98c7a5b42b6bc6633c4a60218406417dae7d45cb8b3b2b8f81aed1c8eca61914477675916f211e67fabe0e0ff48b
`define CMD_MEMDEPTH_ML 233
`define CMD_MEMSIZE_ML 8

`define CMD_MEMDEPTH_FE 418
`define CMD_MEMSIZE_FE 9

`define CMD_MEMSIZE 9
