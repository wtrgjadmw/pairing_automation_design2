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
`define WORD_SIZE 'd1032
`define CHAR 1032'hc6aea1548ea68254b113065eb2656023afccd8f309a295ba5006f6b31b61f9766c7450b5d7fd5cb049660227f3a38468f34fb7f1b1a0dcc5a115cad45213ea637a852deb6071f5d69063147ecab77c77356059551e53caff878005656100025fffe2aa8aaaa555765555554eaaa9000055557fffd0000000055556aaaaaaaaaaab
`define CHAR_INV 1032'h52dff5ad12dcbc3ab9f26da4c94c9b6af2d4a439df3c2612d684262679ebd9ebe6388150c6ce351b9c596161a8c186df0b71421427ef3f37fed126d1d947b35074dccad940941a15d00e8fe693ae05dad46c4ae0e53174fe78810cb01dffcb7ff22005a002d00029ffdbfff6ffff3ffffffffffe2000000030000bfffffffffffd
`define INVERSION_INITIAL_VALUE 1032'h675d8e9d0680ce83dad20c86412029fe2986483ade67e7e524f5caf45da58f0bb7374f3c8b1ca93d680c912a8af94583b35fef731a562c31dfe2c5aceb768d20bfc02b31d069c43a659808855c4c00e4665cbbdee9736fe9fc45a4ee4895af0d2f217bcf884b0508bddead0d070c276579e90f6d315282e36e3d0732cb84804cb3
`define CHAR_3X 1034'h2540be3fdabf386fe1339131c1730206b0f668ad91ce7c12ef014e4195225ec63455cf22187f81610dc320677daea8d3ad9ef27d514e29650e341607cf63bbf2a6f8f89c22155e183b1293d7c60267565a0210bff5afb60fe968010302300071fffa7ff9ffff00062ffffffebfffb000100007fff70000000100004000000000001

// parameters for twisted curve (Ep4)
`define BT00 1032'h0
`define BT01 1032'h0
`define BT10 1032'h8d5d42a91d4d04a962260cbd64cac0475f99b1e613452b74a00ded6636c3f2ecd8e8a16baffab96092cc044fe74708d1e69f6fe36341b98b422b95a8a427d4c6f50a5bd6c0e3ebad20c628fd956ef8ee6ac0b2aa3ca795ff0f000acac20004bfffc55515554aaaecaaaaaa9d55520000aaaaffffa00000000aaaad555555555556
`define BT11 1032'h39515eab71597dab4eecf9a14d9a9fdc5033270cf65d6a45aff9094ce49e0689938baf4a2802a34fb699fdd80c5c7b970cb0480e4e5f233a5eea352badec159c857ad2149f8e0a296f9ceb8135488388ca9fa6aae1ac3500787ffa9a9efffda0001d5575555aaa89aaaaaab15556ffffaaaa80002ffffffffaaaa9555555555555
// // constants independent from elliptic curve
`define ZERO 1032'd0
`define ONE 1032'h39515eab71597dab4eecf9a14d9a9fdc5033270cf65d6a45aff9094ce49e0689938baf4a2802a34fb699fdd80c5c7b970cb0480e4e5f233a5eea352badec159c857ad2149f8e0a296f9ceb8135488388ca9fa6aae1ac3500787ffa9a9efffda0001d5575555aaa89aaaaaab15556ffffaaaa80002ffffffffaaaa9555555555555

// Frobenius pre-calculated coefficients
`define K0 1032'h4aa1a098b4533f7eefa513897c8b151075773d4f03208800570ec166e5d4d6289495c2d5a1b23085c13d90380733a2a7bebe2990ed0829acf27d89888b49d82dac00f4b0869e95cc77af4b9aea9977fd6b18c9cf2d62303ea83b1c0b9c5752b5fe15ecbe25a88019565b3b26d05a0f46f03ab80256f42b487df44c628e1c12a777
`define K1 1032'h4aa1a098b4533f7eefa513897c8b151075773d4f03208800570ec166e5d4d6289495c2d5a1b23085c13d90380733a2a7bebe2990ed0829acf27d89888b49d82dac00f4b0869e95cc77af4b9aea9977fd6b18c9cf2d62303ea83b1c0b9c5752b5fe15ecbe25a88019565b3b26d05a0f46f03ab80256f42b487df44c628e1c12a777
`define XI100 1032'h0
`define XI101 1032'h0
`define XI110 1032'h15d8023603879b54f9669b39f78855a4ffb47ef74b5f567a1ac2ef7b5604712e6820057374e36abcdade8fd19eb37a670b24bd86292008d361547c21be8b2b8e65b5f5434f5ca6d28fcc108bf88b16c48c873704792eb13579062c29be8792caefd1f90d2d8375e2a749e4ae9e15ca55a19c28c5eee143084e8ca66e1c415b1f9f
`define XI111 1032'hb0d69f1e8b1ee6ffb7ac6b24badd0a7eb01859fbbe433f4035440737c55d884804544b426319f1f36e87725654f00a01e82afa6b8880d3f23fc14eb29388bed514cf38a811154f04009703f2d22c65b2a8d92250a52519ca0e79d93ba2786f951010b17d7d21df93ae0b70a00c9335aab3b95739e11ebcf7b6c8b03c8e694f8b0c
`define XI200 1032'h2e9b9c03081f6044d3c0d28dc14bc75ac39534c5842f2a69252e05dd564b53197be603da42249939ba6179b477cab99c988cff4fee9ace61e294bde758acb430bb214a66c6daff9c25870565a55c1e10e1fa23579dcdd3310e5ab3e2ff9b9ecf075fc45250e3dd03314db5fd0526c35b5dda2ebb1934a75fead81556552c02a73d
`define XI201 1032'h981305518687220fdd5233d0f11998c8ec37a42d85736b512ad8f0d5c516a65cf08e4cdb95d8c3768f0488737bd8cacc5ac2b8a1c3060e63be810cecf9673632bf63e3849996f63a6adc0f19255b5e66536635fd8085f7ce7925518261646390f882e63859c1787324079f51a5823ca4f77b5144b6cb58a01a7d4154557ea8036e
`define XI210 1032'h0
`define XI211 1032'h0
`define XI300 1032'h0
`define XI301 1032'h0
`define XI310 1032'h0
`define XI311 1032'h5a30229e848a61a3c378d005d744cccbb89071c647d2c31d207564cb66676b32519c1b3b4f9b0b3ff0f94a938f68b5ea8c671854d4cb8921d4cd51825237232b19bd225fff64f25b3a20edb77adfae4e1ac74d96bfba7c91bd9d371b3fedda69e9f0d6ac3e0e593b944678697afbef4ef45046203e5aeebbd8b9d09487e503d94a
`define XI400 1032'h0
`define XI401 1032'ha2ded927efbd612fc173eb5dc75f9af6baff529b17dbc4e268dea7818325815f00dad7d4c6519ef3e17bd6d0e05458a043845daf92c16e2b925e7052ed7882dde0849fda52ae344f8c185f8881d02a21cbd2b29cd4b14ad9ecb4dc28068477785f15441466990cfa4b967f4c7ae6f372e532694cd38ebf7cf65b871256189c7048
`define XI410 1032'h0
`define XI411 1032'h0
`define XI500 1032'h0
`define XI501 1032'h0
`define XI510 1032'h2beb8d93b8ab24099e26a841e9d6a479158f1d75a8984dba9294605afe4e214da986297ee97e54efcf827432f47fb323d65e6f16bd5735062dc8de17683cd80021e899087d9601f4b150b36d064fc9739f131ea25ecd8d2595f4a300e005f74fab20eaf1068dbff97a8fe9b5bd2edad44ab3b766726261ba757bbed52783529c88
`define XI511 1032'h2beb8d93b8ab24099e26a841e9d6a479158f1d75a8984dba9294605afe4e214da986297ee97e54efcf827432f47fb323d65e6f16bd5735062dc8de17683cd80021e899087d9601f4b150b36d064fc9739f131ea25ecd8d2595f4a300e005f74fab20eaf1068dbff97a8fe9b5bd2edad44ab3b766726261ba757bbed52783529c88
`define CMD_MEMDEPTH_ML 313
`define CMD_MEMSIZE_ML 9

`define CMD_MEMDEPTH_FE 983
`define CMD_MEMSIZE_FE 10

`define CMD_MEMSIZE 10
