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
`define WORD_SIZE 'd440
`define CHAR 440'hf3000003cbf869ec5488b672e553d97f3ed0d45e8bb15310e1a7ed5d90f4f19deb13ab4dc9a805ccbe6e62b2cb7ae007ff54aaabffaaab
`define CHAR_INV 440'h10b40d0971c468f1226527e93088c140c1a75e2df476e17e80b6315dfed9d3ce7bb2e467edb11286c0f6103df7ef715fc711fd0bfcfffd
`define INVERSION_INITIAL_VALUE 440'h911872ef72b687de3409a1190c170f7805defb528f21277960ac67118d52605b4542c894b5fc724765c47da05d112d77a94312638521
`define CHAR_3X 442'h2d900000b63e93dc4fd9a2358affb8c7dbc727d1ba313f932a4f7c818b2ded4d9c13b01e95cf811663b4b28186270a017fdfe0003ff0001

// parameters for twisted curve (Ep2)
`define BT0 440'hcc00000f2fe1a7b15222d9cb954f65fcfb43517a2ec54c43869fb57643d3c677ac4ead3726a01732f9b98acb2deb801ffd52aaaffeaaac
`define BT1 440'hcc00000f2fe1a7b15222d9cb954f65fcfb43517a2ec54c43869fb57643d3c677ac4ead3726a01732f9b98acb2deb801ffd52aaaffeaaac
// // constants independent from elliptic curve
`define ZERO 440'd0
`define ONE 440'hcfffffc34079613ab77498d1aac2680c12f2ba1744eacef1e5812a26f0b0e6214ec54b23657fa3341919d4d34851ff800ab5554005555

// Frobenius pre-calculated coefficients
`define XI10 440'hada3d1fa67c99ae4d025df022f1ef8830c0a7f56053e4fa8c8772ab1eeddc78e2d636d573821228bedf1d184d8cc444aa6c0e32306b597
`define XI11 440'h455c2e09642ecf078462d770b634e0fc32c65508867303681930c2aba2172a0fbdb03df69186e340d07c912df2ae9bbd5893c788f8f514
`define XI20 440'h0
`define XI21 440'hef534155c2a2cc56442f841fccf941392728e7ff0e96a89cd0eda3441562efade335ef9a4a5d3a4b42cb9cc72abdf3fc4bac04efe689c2
`define XI30 440'h8cb93322281af74c1ee3e00eb3c984a793b48863a015aec83ecada20c51c84ff1f40dcfa00af6235b72804ef27a9f3639eeec81098c357
`define XI31 440'h8cb93322281af74c1ee3e00eb3c984a793b48863a015aec83ecada20c51c84ff1f40dcfa00af6235b72804ef27a9f3639eeec81098c357
`define XI40 440'h953414e2ab1f87d9b1e173a02518e3aa9873f41f734027b0d9dc888f3790c720d0e98feb70d2eb1c5eed76193c833ec4d02af97e7346c
`define XI41 440'h0
`define XI50 440'h475d0518c3ec28449a81089dfd94a3ab60ee335b19a2ab60259a177523055aef61909f036f287ef4e6ab73c134fb57a6465b00879fce43
`define XI51 440'haba2faeb080c41a7ba07add4e7bf35d3dde2a103720ea7b0bc0dd5e86def96ae89830c4a5a7f86d7d7c2eef1967f8861b8f9aa245fdc68
`define CMD_MEMDEPTH_ML 228
`define CMD_MEMSIZE_ML 8

`define CMD_MEMDEPTH_FE 418
`define CMD_MEMSIZE_FE 9

`define CMD_MEMSIZE 9
