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

`define RAM_DEPTH 176
`define RAM_ADDR_SIZE 8


`define RAM_PX	    `RAM_ADDR_SIZE'd0
`define RAM_PY_	    `RAM_ADDR_SIZE'd1
`define RAM_BT00	`RAM_ADDR_SIZE'd2
`define RAM_BT01	`RAM_ADDR_SIZE'd3
`define RAM_BT10	`RAM_ADDR_SIZE'd4
`define RAM_BT11	`RAM_ADDR_SIZE'd5
`define RAM_PX_	    `RAM_ADDR_SIZE'd6
`define RAM_PY      `RAM_ADDR_SIZE'd7
`define RAM_QX00	`RAM_ADDR_SIZE'd8
`define RAM_QX01	`RAM_ADDR_SIZE'd9
`define RAM_QX10	`RAM_ADDR_SIZE'd10
`define RAM_QX11	`RAM_ADDR_SIZE'd11
`define RAM_QY00	`RAM_ADDR_SIZE'd12
`define RAM_QY01	`RAM_ADDR_SIZE'd13
`define RAM_QY10	`RAM_ADDR_SIZE'd14
`define RAM_QY11	`RAM_ADDR_SIZE'd15
`define RAM_QY_00	`RAM_ADDR_SIZE'd16
`define RAM_QY_01	`RAM_ADDR_SIZE'd17
`define RAM_QY_10	`RAM_ADDR_SIZE'd18
`define RAM_QY_11	`RAM_ADDR_SIZE'd19
`define RAM_TX00	`RAM_ADDR_SIZE'd20
`define RAM_TX01	`RAM_ADDR_SIZE'd21
`define RAM_TX10	`RAM_ADDR_SIZE'd22
`define RAM_TX11	`RAM_ADDR_SIZE'd23
`define RAM_TY00	`RAM_ADDR_SIZE'd24
`define RAM_TY01	`RAM_ADDR_SIZE'd25
`define RAM_TY10	`RAM_ADDR_SIZE'd26
`define RAM_TY11	`RAM_ADDR_SIZE'd27
`define RAM_TZ00	`RAM_ADDR_SIZE'd28
`define RAM_TZ01	`RAM_ADDR_SIZE'd29
`define RAM_TZ10	`RAM_ADDR_SIZE'd30
`define RAM_TZ11	`RAM_ADDR_SIZE'd31

`define RAM_XI100	`RAM_ADDR_SIZE'd32
`define RAM_XI101	`RAM_ADDR_SIZE'd33
`define RAM_XI110	`RAM_ADDR_SIZE'd34
`define RAM_XI111	`RAM_ADDR_SIZE'd35
`define RAM_XI200	`RAM_ADDR_SIZE'd36
`define RAM_XI201	`RAM_ADDR_SIZE'd37
`define RAM_XI210	`RAM_ADDR_SIZE'd38
`define RAM_XI211	`RAM_ADDR_SIZE'd39
`define RAM_XI300	`RAM_ADDR_SIZE'd40
`define RAM_XI301	`RAM_ADDR_SIZE'd41
`define RAM_XI310	`RAM_ADDR_SIZE'd42
`define RAM_XI311	`RAM_ADDR_SIZE'd43
`define RAM_XI400	`RAM_ADDR_SIZE'd44
`define RAM_XI401	`RAM_ADDR_SIZE'd45
`define RAM_XI410	`RAM_ADDR_SIZE'd46
`define RAM_XI411	`RAM_ADDR_SIZE'd47
`define RAM_XI500	`RAM_ADDR_SIZE'd48
`define RAM_XI501	`RAM_ADDR_SIZE'd49
`define RAM_XI510	`RAM_ADDR_SIZE'd50
`define RAM_XI511	`RAM_ADDR_SIZE'd51
`define RAM_K0	    `RAM_ADDR_SIZE'd52
`define RAM_K1	    `RAM_ADDR_SIZE'd53
`define RAM_ZERO	`RAM_ADDR_SIZE'd54
`define RAM_ONE	    `RAM_ADDR_SIZE'd55

`define RAM_A	`RAM_ADDR_SIZE'd56
`define RAM_B	`RAM_ADDR_SIZE'd80
`define RAM_C	`RAM_ADDR_SIZE'd104
`define RAM_E	`RAM_ADDR_SIZE'd128
`define RAM_F	`RAM_ADDR_SIZE'd152

// constants --------------------------------------------------------
`define WORD_SIZE 'd317
`define CHAR 317'h1058ca226f60892cf28fc5a0b7f9d039169a61e684c73446d6f339e43424bf7e8d512e565dab2aab
`define CHAR_INV 317'h1131c88bbcd979065521b593fa616990ec8486299a5c6ccfbb7f0805724f91b955b5e0028b047ffd
`define INVERSION_INITIAL_VALUE 317'h145322376c65b1e5819fffe5e303aafcecbf76aa26b22da4800d805f4b0af7cd69b6dafcd8b2eee
`define CHAR_3X 319'h310a5e674e219b86d7af50e227ed70ab43cf25b38e559cd484d9adac9c6e3e7ba7f38b0319018001

// parameters for twisted curve (Ep4)
`define BT00 317'h0
`define BT01 317'h0
`define BT10 317'hd92790ef45c3fc55e11989af82b4e7061c752b25e8d92101f596ac292fec38a22c7bba37051d553
`define BT11 317'h0
// // constants independent from elliptic curve
`define ZERO 317'd0
`define ONE 317'hfa735dd909f76d30d703a5f48062fc6e9659e197b38cbb9290cc61bcbdb408172aed1a9a254d555

// Frobenius pre-calculated coefficients
`define K0 317'h42502afc2c1abf6671c5f481eeb45925259fee732df7de38adfe0664383939f7320208da2caa872
`define K1 317'h42502afc2c1abf6671c5f481eeb45925259fee732df7de38adfe0664383939f7320208da2caa872
`define XI100 317'h0
`define XI101 317'h0
`define XI110 317'hc46cbf7dff6385de329140eb4ee7ad38d4fac30bf289db8e1d032faa0480b410721df168a9f6be8
`define XI111 317'h411fe2a8f6a50cf0f66b192030b5565894ab5b5c59e968df52306e993dcb43d862f4f3fd30bbec3
`define XI200 317'h91cc9beb340635fe76753eac7ea16650b9e6781d46df8700a5ea6bbfb0c79264afde3fbe4a21b46
`define XI201 317'h73c0063bc2025cd0b2871b5f00fb9d40afbfa64b0593bd6cc9493283918465842534a5a79090f65
`define XI210 317'h0
`define XI211 317'h0
`define XI300 317'h0
`define XI301 317'h0
`define XI310 317'h0
`define XI311 317'hd5d1dba35866e0629e85f0e24c935047f23e5f2f5b7fa1a7f7096a0336e418b12bf0748980c68c
`define XI400 317'h0
`define XI401 317'h60b795003eb8dd0e454bbe9ffbf369511c9949c41cb12509a713438f474d764f39cebe6a16c3038
`define XI410 317'h0
`define XI411 317'h0
`define XI500 317'h0
`define XI501 317'h0
`define XI510 317'hcb7337edf7b395b748cdad12d7e7710e14ec4514ed29307a59e97fe94abb16c4ddca232735c1884
`define XI511 317'hcb7337edf7b395b748cdad12d7e7710e14ec4514ed29307a59e97fe94abb16c4ddca232735c1884
`define CMD_MEMDEPTH_ML 104
`define CMD_MEMSIZE_ML 7

`define CMD_MEMDEPTH_FE 371
`define CMD_MEMSIZE_FE 9

`define CMD_MEMSIZE 9
