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
`define WORD_SIZE 'd509
`define CHAR 509'h155556ffff39ca9bfcedf2b4f9c0ecf6cb8ac8495d187e8c32ea0103e01090bb626e85bf7c18a0f0cfcb5c6071bad3d2ee63bd076e8d9300a13d118db8bfd2ab
`define CHAR_INV 509'h1922cc4dbc91ad02c33fdcaf9a10427a60052008bdf3ace572c3c0515ccafe787a9496ab23308026cef91820f4fbfcae1ec48e9039f5b1dd6efa1180a5fe67fd
`define INVERSION_INITIAL_VALUE 509'h13b0f3de7b04db52ce290bb80c4cfb1b6f5ef967006a906bab0e036e439d6a98b54c03153b92a7a5ae57cc39d92d991f7f74c77ac4802d9dfd9176d059a3f93c
`define CHAR_3X 511'h400004fffdad5fd3f6c9d81eed42c6e462a058dc17497ba498be030ba031b232274b913e7449e2d26f62152155307b78cb2b37164ba8b901e3b734a92a3f7801

// parameters for twisted curve (Ep4)
`define BT00 509'h0
`define BT01 509'h0
`define BT10 509'h10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
`define BT11 509'h55556ffff39ca9bfcedf2b4f9c0ecf6cb8ac8495d187e8c32ea0103e01090bb626e85bf7c18a0f0cfcb5c6071bad3d2ee63bd076e8d9300a13d118db8bfd2ab
// // constants independent from elliptic curve
`define ZERO 509'd0
`define ONE 509'haaaa90000c6356403120d4b063f1309347537b6a2e78173cd15fefc1fef6f449d917a4083e75f0f3034a39f8e452c2d119c42f891726cff5ec2ee7247402d55

// Frobenius pre-calculated coefficients
`define K0 509'hfd44521e0682228172563d40eab174f8d2bb9178e21743cf9d3eae85d02a127c3b41316dc78c6cf6f65ee74a4c552eec849030c6bcf45cfc1159357d16dbe21
`define K1 509'hfd44521e0682228172563d40eab174f8d2bb9178e21743cf9d3eae85d02a127c3b41316dc78c6cf6f65ee74a4c552eec849030c6bcf45cfc1159357d16dbe21
`define XI100 509'h0
`define XI101 509'h0
`define XI110 509'h10acb9b02a820d6f8473487884344299fac4854f41eba42d49a02a41865a20ac0558161843f3e7b2c3895626d14f1fcc5b25b301b86641b642b4d30546d3e6ac
`define XI111 509'h4a89d4fd4b7bd2c787aaa3c758caa5cd0c642fa1b2cda5ee949d6c259b6700f5d166fa73824b93e0c420639a06bb406933e0a05b627514a5e883e8871ebebff
`define XI200 509'hc9965f0f92ec9a599e0904ba8c472df4a7a51edba6a9457a7387897630c273905366199919aa3c0b87f411b0041260d1892cff90132d39df88a273e59e64d72
`define XI201 509'h8bbf10f060b00f6630d626950fc7a178110765ba2adea348bb1886c7d0469825d382425ea7dfd30174c1b457179adc5d5d0ed0e6d5abf62a8b2ea4f5ed98539
`define XI210 509'h0
`define XI211 509'h0
`define XI300 509'h0
`define XI301 509'h0
`define XI310 509'h0
`define XI311 509'hc30e442f472d6192f8274ce5601ea174fc5f28d807cfe2ae7621b75adb43d81e1edae78c1accb9aafbad04e97776cdf4551aa2b103c6a24cb9102d2e7dfa74c
`define XI400 509'h0
`define XI401 509'habca984925c7f7b73b1c55e0ec988a1dd9e261022d43e92108bf1f21d5f7981591c8837acf6bc589cf0a60f176fc41ff9cd6920e6d53d9ff74694515724a612
`define XI410 509'h0
`define XI411 509'h0
`define XI500 509'h0
`define XI501 509'h0
`define XI510 509'h3c23130f8d6a0c8deda88fbf16660ac85e0f93733c42b9b55c38f40fd63b67c2a5b5cf1a14e38f9753fe1b5b9935e4ba0010385041503b410c0f5d8d8bef142
`define XI511 509'h3c23130f8d6a0c8deda88fbf16660ac85e0f93733c42b9b55c38f40fd63b67c2a5b5cf1a14e38f9753fe1b5b9935e4ba0010385041503b410c0f5d8d8bef142
`define CMD_MEMDEPTH_ML 157
`define CMD_MEMSIZE_ML 8

`define CMD_MEMDEPTH_FE 524
`define CMD_MEMSIZE_FE 10

`define CMD_MEMSIZE 10
