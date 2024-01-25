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
`define WORD_SIZE 'd318
`define CHAR 318'h2cc0e5b9310d9b6d1ac7e34522e5d188f0c6289ed6211ac41cbfb79cdc3adfbf0054f5ffb0555aab
`define CHAR_INV 318'h15c46d18e686c352cdc02c54cbd3ac2e0b5554f0d4811237d50090a65b272c70c86fffcd30002ffd
`define INVERSION_INITIAL_VALUE 318'h1fea8523d9913bac6db82405c2b4c3b6b404b432c8fb121593517dd350d94c89cd155e0e645c307
`define CHAR_3X 320'h8642b12b9328d2475057a9cf68b1749ad25279dc8263504c563f26d694b09f3d00fee1ff11001001

// parameters for twisted curve (Ep4)
`define BT00 318'hcfc691b3bc9924b94e072eb7468b9dc3ce75d84a77b94ef8d01218c8f148103feac28013eaa9554
`define BT01 318'h133f1a46cef26492e5381cbadd1a2e770f39d76129dee53be340486323c52040ffab0a004faaa555
`define BT10 318'h2642b12b9328d2475057a9cf68b1749ad25279dc8263504c563f26d694b09f3d00fee1ff11001001
`define BT11 318'hcc0e5b9310d9b6d1ac7e34522e5d188f0c6289ed6211ac41cbfb79cdc3adfbf0054f5ffb0555aab
// // constants independent from elliptic curve
`define ZERO 318'd0
`define ONE 318'h133f1a46cef26492e5381cbadd1a2e770f39d76129dee53be340486323c52040ffab0a004faaa555

// Frobenius pre-calculated coefficients
`define K0 318'hb66b631f200f6200cd45ef5cb8108e718a68d98295f2998e9ba556b4e1f3a941d8d9dd0d180d417
`define K1 318'hb66b631f200f6200cd45ef5cb8108e718a68d98295f2998e9ba556b4e1f3a941d8d9dd0d180d417
`define XI100 318'h7bb46c51db8c597731c2dbb0f1a8b9f3b13f690085eb0e63cdfec709eb533d0626b5eabf611c9c2
`define XI101 318'h17a3587b70bf6d0dbf45745f768f8112783faaf60be0918a885c18c0b824ba0ab949a52603be72c0
`define XI110 318'h2fa4de1d416530c2aa938984cce245464663b190b8ea9be525d528ab4721bf60ea2c02d489e4f25
`define XI111 318'h1d31275f851d5ae89fe7796f4a764d7fb956419aa08479ff781728b1f02332d5f6b6ec5d4dc4b265
`define XI200 318'h17858825e81c47bb8d41a07c4664f634c13801f236fc29d83fddd4de9d21efd0f535f2dd5af9bf1b
`define XI201 318'h133a61d90ba6dba0a76551ad7473778fca711b5d93c9c174a078029094bfe27f9e92024dbec62e88
`define XI210 318'h2b33fb76e02b4a4d4a2fd635b5af47016496da5f1d33fb5565b83b06688aefccacd3f073325bff78
`define XI211 318'h38c85de8a5a7e246e402de003bc2360d1590df225eee4e31ec6d599e57e73156fa736aa2f11b767
`define XI300 318'h29802f49ebc60f2e24f119bc3469f3a6ebc714bdf7b61beac0374bd37d54826fad13d91a564cd0e1
`define XI301 318'h1463a7076b7577c665843ec098a7e0b731156e0d4063388b9f1346a45753b460142fea3312e64c31
`define XI310 318'h16d410db815db772ff9d6c680c279a178957da08981b5b93e69be6a2fa19892cf60475ec808c92dd
`define XI311 318'h245f53a8321cb2e23f51f6bd83826d5c3605953aa64b66b0e9386e47948286117de815de60b08b27
`define XI400 318'h2302533f45a1dd159c701ee62eec3c6bea350a01452a733d3f6e7ece90c09ff764d0cd2b0d7c1b23
`define XI401 318'h28be3a9ea892355acdf01be17e84f3b67115c86bc5600851ff8d685c7ba2b9bbc72f77b404acd50b
`define XI410 318'h4be4d2c2bc96a992ec6a5027555549562f2457f12fca3929550d6bb927b3c7fdfd678a2e57f96a2
`define XI411 318'h236e10e53ecf43d707a91362e2a4c0fcb5a601bc7513239294ea8adea7a36a7c7fe30d0e94491c79
`define XI500 318'h3cf58cecdd5a8c9dedc9754a3bc6eabc5dcb8023568297bf03126377dade0287f718591695bd80a
`define XI501 318'h237808b8ba879c0d3ab4a0a9fdbbe1e20371a8422aad43dda04fc0ccbef5a9d3e6681c2ca7be7053
`define XI510 318'h113509f6684be47d2d50529c41e2c844b38ea34590c85682051fbd13e21def2b3b1cb34676b689f4
`define XI511 318'h48a312930037335ab978b17cf58fc72fb836101a9ea0ab8530774dc53fef8ef4f06a7d574380383
`define CMD_MEMDEPTH_ML 98
`define CMD_MEMSIZE_ML 7

`define CMD_MEMDEPTH_FE 335
`define CMD_MEMSIZE_FE 9

`define CMD_MEMSIZE 9
