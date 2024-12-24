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
`define WORD_SIZE 'd446
`define CHAR 446'h3cdee0fb28c5e535200fc34965aad6400095a4b78a02fe320f75a64bbac71602824e6dc3e23acdee56ee4528c573b5cc311c0026aab0aaab
`define CHAR_INV 446'h1612282f09057505556f52f959aff0afa7bc1a092ce1c419622e58eee5c22e19c3e08a5394bf91b742c15d765a12fa2dcd63fd900035fffd
`define INVERSION_INITIAL_VALUE 446'h73066647c4ad7c845bc616c8f5bf138b9a6ec1577617504b0516e657ddb16f60965d5ceda582a8c4e9b5b7d0079085275c1b02048725d5f
`define CHAR_3X 448'hb69ca2f17a51af9f602f49dc310082c001c0ee269e08fa962e60f2e33055420786eb494ba6b069cb04cacf7a505b21649354007400120001

// parameters for twisted curve (Ep2)
`define BT0 446'h3211f04d73a1acadff03cb69a5529bfff6a5b4875fd01cdf08a59b44538e9fd7db1923c1dc53211a911bad73a8c4a33cee3ffd9554f5555
`define BT1 446'h3211f04d73a1acadff03cb69a5529bfff6a5b4875fd01cdf08a59b44538e9fd7db1923c1dc53211a911bad73a8c4a33cee3ffd9554f5555
// // constants independent from elliptic curve
`define ZERO 446'd0
`define ONE 446'h3211f04d73a1acadff03cb69a5529bfff6a5b4875fd01cdf08a59b44538e9fd7db1923c1dc53211a911bad73a8c4a33cee3ffd9554f5555

// Frobenius pre-calculated coefficients
`define XI10 446'h3797d8ec55bcb5413a5f637d674e6e0dc6ba6389ca0e274d2aa085dbade47523bffa0511e8f1d00b611eac97ffdb2d7c75f6f5795ed2ee73
`define XI11 446'h547080ed3092ff3e5b05fcbfe5c683239db412dbff4d6e4e4d520700ce2a0dec25468b1f948fde2f5cf9890c598884fbb250aad4bddbc38
`define XI20 446'h0
`define XI21 446'h17511cbbcb782e3578fe2f3ddf99ef888c36ce2a6e9ae23334f695dd3fc68d56e29a9e0c56b0dc6c81c3963db55b9acc2a61cf52562fcc5f
`define XI30 446'h1ab85024598ed168fde479aa427c5a3cd802cfcda90ef15be44ad0aa6b3423edd1afb087e8219a88777202c50b7aafd8719eea3130e75b1e
`define XI31 446'h1ab85024598ed168fde479aa427c5a3cd802cfcda90ef15be44ad0aa6b3423edd1afb087e8219a88777202c50b7aafd8719eea3130e75b1e
`define XI40 446'h1a723bc0a2b2490058ee6bf479ef19488ba12972e497e4012580ef9184ff7754604c304874760e7e2ad55114efe7e4fff945cf2bab7f21b4
`define XI41 446'h0
`define XI50 446'h157148158685a175183419de441ff20a9e278e9fe91a1a76ff75b03a5e51830f0f5b47d5eed89ca581a26a3445e22788b679df83e5099ee6
`define XI51 446'h276d98e5a24043c007dba96b218ae435626e1617a0e8e3bb0ffff6115c7592f372f325edf3623148d54bdaf47f918e437aa220a2c5a70bc5
`define CMD_MEMDEPTH_ML 235
`define CMD_MEMSIZE_ML 8

`define CMD_MEMDEPTH_FE 433
`define CMD_MEMSIZE_FE 9

`define CMD_MEMSIZE 9
