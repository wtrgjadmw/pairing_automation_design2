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
`define WORD_SIZE 'd638
`define CHAR 638'h3cb868653d300b3fe80015554dd25db0fc01dcde95d4000000631bbd421715013955555555529c005c75d6c2ab00000000000ac79600d2abaaaaaaaaaaaaaa93eaf3ff000aaaaaaaaaaaaaaabeab000b
`define CHAR_INV 638'h292b910681a83c72d3f874d144a6ee352038259855e4310b293364904bd2b2e08f04c64a6057a830a0f48534b5e8c379f5c9f83efc66a4d1145a03a20f9f98e6fe245a84be4d513dfad7ab621d14745d
`define INVERSION_INITIAL_VALUE 638'h1844da4d59d66ffd6cf0d3924ea81e49414c782feda6c346ce45c4ddd731e52a03bea6c4c5bc6dd111a992a803bb5b168df384b1a42f6859446958e4ac576e96b1738787077f9fa27f310236b1696f22
`define CHAR_3X 640'hb629392fb79021bfb8003fffe9771912f405969bc17c000001295337c6453f03abfffffffff7d401156184480100000000002056c2027802ffffffffffffffbbc0dbfd0020000000000000003c010021

// parameters for twisted curve (Ep2)
`define BT0 638'hd1e5e6b0b3fd3005fffaaaac8b6893c0ff88c85a8affffffe73910af7a3abfb1aaaaaaaaab58ffe8e28a4f553ffffffffffd4e1a7fcb55155555555555555b0543003ffd5555555555555550553ffd4
`define BT1 638'hd1e5e6b0b3fd3005fffaaaac8b6893c0ff88c85a8affffffe73910af7a3abfb1aaaaaaaaab58ffe8e28a4f553ffffffffffd4e1a7fcb55155555555555555b0543003ffd5555555555555550553ffd4
// // constants independent from elliptic curve
`define ZERO 638'd0
`define ONE 638'h347979ac2cff4c017ffeaaab22da24f03fe23216a2bffffff9ce442bde8eafec6aaaaaaaaad63ffa38a293d54fffffffffff53869ff2d54555555555555556c150c00fff5555555555555554154fff5

// Frobenius pre-calculated coefficients
`define XI10 638'h2c3cbb182b36e52819334bbc8f7b3215d1c929c8471a23deec0e455c5a6f0390e9039950a8ff261309a1e827f4a2e9c515ee00155d415b66652c04d87458db66440995dd8406d3c61d59a4bef71705b8
`define XI11 638'h107bad4d11f92617ceccc998be572b9b2a38b3164eb9dc211454d660e7a811705051bc04ac5375ed52d3ee9ab65d163aea120ab238bf7745457ea5d23651cf2da6ea692286a3d6e48d5105ebc793fa53
`define XI20 638'h0
`define XI21 638'h691e0ad9cd6638e184f0b41bb393066330fe0aec54cee4002a93c39c3d16ad846140f287fc89c623f2b646f87eca90f7b52840f21e7aebacc1b03dc2a572b69df98051330ce6905d34ed21f9343aa69
`define XI30 638'h2cdeb53e10b9459d9859aa6759d74a26b6b303dd36715b8465e5759c8f72f4f7467572cc0a672d9a05ebc500a5001fe5882bad4733e96f46e7737dc83be1ad6a610cf6ce1adf0a4183ac62b175ab3e03
`define XI31 638'h2cdeb53e10b9459d9859aa6759d74a26b6b303dd36715b8465e5759c8f72f4f7467572cc0a672d9a05ebc500a5001fe5882bad4733e96f46e7737dc83be1ad6a610cf6ce1adf0a4183ac62b175ab3e03
`define XI40 638'h9d978485fa6584e304ef5ec6d66d2b5370e03d02f78ee400246207c81ba55d70cbeb9d32a760061e2b58dacdceca90f7b5279478be6dc0f217059317fac80d5f4a406132623be5b28a42774d498aa5e
`define XI41 638'h0
`define XI50 638'h1c6307f0fec01f85c98ce0ce9b801e8b8c7a50c6e7b77f6351909f3ba7cae386f623b6c75e13b7acb317d665eea309aa9e19a294fb29f801a1f4d7f6058fde3cba228dab943b335cf65b5cc5ae1743b0
`define XI51 638'h205560743e6febba1e733486b2523f256f878c17ae1c809caed27c819a4c317a43319e8df73ee453a95e005cbc5cf65561e668329ad6daaa08b5d2b4a51acc5730d17154766f774db44f4de51093bc5b
`define CMD_MEMDEPTH_ML 325
`define CMD_MEMSIZE_ML 9

`define CMD_MEMDEPTH_FE 573
`define CMD_MEMSIZE_FE 10

`define CMD_MEMSIZE 10
