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
`define WORD_SIZE 'd559
`define CHAR 559'h557003c04ffe89db51ef86c56921091e1c72d1e92397d41e37c255cd44eff051c38fa813a695c5d574923beee353ada1100a0b5fb2111a277d389362d77fcb581fe8b50105eb
`define CHAR_INV 559'h5b68300c8bc0d7d5769e26921dda8922d964b6a8fe9a8b68923ba8c906b1dd8b5221194a0df651412c379634483996a655b147487dce9e8808c84693297894dd3aa4efec053d
`define INVERSION_INITIAL_VALUE 559'h4137a920582628eff4bb2a256b6f51ea54ffa509e1179733b55d2da171c515f506e40505715f7b3b365a14fe94faaf23c2bfaccb7a769e5509b329f61be1e0afa67703a4959e
`define CHAR_3X 561'h100500b40effb9d91f5ce94503b631b5a555875bb6ac77c5aa7470167cecfd0f54aaef83af3c151805db6b3cca9fb08e3301e221f16334e7677a9ba28867f62085fba1f0311c1

// parameters for twisted curve (Ep4)
`define BT00 559'h0
`define BT01 559'h0
`define BT10 559'h2ae007809ffd13b6a3df0d8ad242123c38e5a3d2472fa83c6f84ab9a89dfe0a3871f50274d2b8baae92477ddc6a75b42201416bf6422344efa7126c5aeff96b03fd16a020bd6
`define BT11 559'h2a8ffc3fb0017624ae10793a96def6e1e38d2e16dc682be1c83daa32bb100fae3c7057ec596a3a2a8b6dc4111cac525eeff5f4a04deee5d882c76c9d288034a7e0174afefa15
// // constants independent from elliptic curve
`define ZERO 559'd0
`define ONE 559'h2a8ffc3fb0017624ae10793a96def6e1e38d2e16dc682be1c83daa32bb100fae3c7057ec596a3a2a8b6dc4111cac525eeff5f4a04deee5d882c76c9d288034a7e0174afefa15

// Frobenius pre-calculated coefficients
`define K0 559'h452bda30ad1a24a31f0498068dc0fed17af12797fcc70dd4f9ff3b44ccadb6498bfb4e57c7336488a2f516f4479e5ecce74b649935ac0cd2ebc29835bf44faee588a647edfff
`define K1 559'h452bda30ad1a24a31f0498068dc0fed17af12797fcc70dd4f9ff3b44ccadb6498bfb4e57c7336488a2f516f4479e5ecce74b649935ac0cd2ebc29835bf44faee588a647edfff
`define XI100 559'h0
`define XI101 559'h0
`define XI110 559'h4a4fe1d5c0609d1731ce07351b34d9ebbe25a1b4e4e4ff2553204648d49d20c3ec71764b60fa0e28cc51a3f79702f9466b036f8389584d6ecf369ee21a03a26e2254d86c5cb
`define XI111 559'h50cb05a2f3f88009ded2a652176dbb7f609077cdd549842be2905168b7a61e4584c890aef08624f2e7cd21af69e37e0ca959d467797b955090452974b5df91313dc3677a4020
`define XI200 559'h8094855a251d1217faa96af76fa09d3be408d9cd14035025d79835b9e21c30c576612e03fbdf6e19b1ca8ed61556ec02f9a790692c1a6922c46a0de46fa9904664d0312294a
`define XI201 559'h4d66bb6aadacb8b9d244f015f226ff4a5e32444c52579f1bda48d271a6ce2d456c29953366d7cef3d975930181fe3ee0e06f92591f4f739550f1f28490853253b99bb1eedca1
`define XI210 559'h0
`define XI211 559'h0
`define XI300 559'h0
`define XI301 559'h0
`define XI310 559'h0
`define XI311 559'h398d5a84e51eaf16051882644df31b6c077b541b88a6a50c6adab3f9da68c27808b99511722bd9f711e29806d73357cf356af09bc15061297513b2ae50374fee6ae8ade8133c
`define XI400 559'h0
`define XI401 559'h5567c3cbd2d549647096e82047b173fc94c20266d2bdacffa39b9f7d128cf1d0efd3ee34ca9f4cbea3e11542275dc039a3e25749b71fd97d8bb2cb8bc311eba875fbcb015bae
`define XI410 559'h0
`define XI411 559'h0
`define XI500 559'h0
`define XI501 559'h0
`define XI510 559'h28f04693b1e1bb3260e4afc795bf4e97d0d318fb6ec63d99ff2fd3b441bbcd8b8e6398b4bf6508e94a5079f3a7b362c0e62ce377e12745967153180024a24e764ba744bc9967
`define XI511 559'h28f04693b1e1bb3260e4afc795bf4e97d0d318fb6ec63d99ff2fd3b441bbcd8b8e6398b4bf6508e94a5079f3a7b362c0e62ce377e12745967153180024a24e764ba744bc9967
`define CMD_MEMDEPTH_ML 172
`define CMD_MEMSIZE_ML 8

`define CMD_MEMDEPTH_FE 569
`define CMD_MEMSIZE_FE 10

`define CMD_MEMSIZE 10
