// Easy Part -------------------------------------------------------
writeCommands(0, {`MODE_INV, `RAM_F, `RAM_F, `RAM_E});  // e = invFp24(f)
writeCommands(1, {`MODE_MUL_CONJ, `RAM_E, `RAM_F, `RAM_F}); // f = mulFp24_conj_forRTL(e, f)
writeCommands(2, {`MODE_FROB, `RAM_F, `RAM_F, `RAM_E}); // e = FrobFp24(FrobFp24(FrobFp24(FrobFp24(f))))
writeCommands(3, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});
writeCommands(4, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});
writeCommands(5, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E});
writeCommands(6, {`MODE_MUL, `RAM_E, `RAM_F, `RAM_F}); // f = mulFp24(e, f)

// Hard Part -------------------------------------------------------
// a = expFp24(f)
writeCommands(7, {`MODE_SQR012345, `RAM_F, `RAM_C, `RAM_C});
writeCommands(8, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(9, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(10, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(11, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(12, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(13, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(14, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(15, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(16, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(17, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(18, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(19, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(20, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(21, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(22, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_A});
writeCommands(23, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(24, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(25, {`MODE_MUL, `RAM_A, `RAM_C, `RAM_A});
writeCommands(26, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(27, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(28, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(29, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(30, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(31, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(32, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(33, {`MODE_MUL, `RAM_A, `RAM_C, `RAM_A});
writeCommands(34, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(35, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(36, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(37, {`MODE_MUL_CONJ, `RAM_A, `RAM_C, `RAM_A});
writeCommands(38, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(39, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(40, {`MODE_MUL_CONJ, `RAM_A, `RAM_C, `RAM_A});
writeCommands(41, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(42, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(43, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(44, {`MODE_MUL, `RAM_A, `RAM_C, `RAM_A});
// b = expFp24(a)
writeCommands(45, {`MODE_SQR012345, `RAM_A, `RAM_C, `RAM_C});
writeCommands(46, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(47, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(48, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(49, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(50, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(51, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(52, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(53, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(54, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(55, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(56, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(57, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(58, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(59, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(60, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(61, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(62, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(63, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(64, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(65, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(66, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(67, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(68, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(69, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(70, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(71, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(72, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(73, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(74, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(75, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(76, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(77, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(78, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(79, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(80, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(81, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(82, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(83, {`MODE_SQR012345, `RAM_A, `RAM_A, `RAM_A}); // a = squareFp24(a)
writeCommands(84, {`MODE_MUL_CONJ, `RAM_B, `RAM_A, `RAM_A}); // a = mulFp24_conj_forRTL(b, a)
writeCommands(85, {`MODE_MUL, `RAM_A, `RAM_F, `RAM_A}); // a = mulFp24(a, f)
// b = expFp24(a)
writeCommands(86, {`MODE_SQR012345, `RAM_A, `RAM_C, `RAM_C});
writeCommands(87, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(88, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(89, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(90, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(91, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(92, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(93, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(94, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(95, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(96, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(97, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(98, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(99, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(100, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(101, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(102, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(103, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(104, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(105, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(106, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(107, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(108, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(109, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(110, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(111, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(112, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(113, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(114, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(115, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(116, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(117, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(118, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(119, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(120, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(121, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(122, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(123, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(124, {`MODE_FROB, `RAM_A, `RAM_C, `RAM_E}); // e = FrobFp24(a)
writeCommands(125, {`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}); // e = mulFp24(e, b)
writeCommands(126, {`MODE_CONJ, `RAM_A, `RAM_A, `RAM_A}); // a = conjFp24(a)
// b = expFp24(b)
writeCommands(127, {`MODE_SQR012345, `RAM_B, `RAM_C, `RAM_C});
writeCommands(128, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(129, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(130, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(131, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(132, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(133, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(134, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(135, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(136, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(137, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(138, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(139, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(140, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(141, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(142, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(143, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(144, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(145, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(146, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(147, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(148, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(149, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(150, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(151, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(152, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(153, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(154, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(155, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(156, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(157, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(158, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(159, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(160, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(161, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(162, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(163, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(164, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(165, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}); // e = FrobFp24(e)
writeCommands(166, {`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}); // e = mulFp24(e, b)
// b = expFp24(b)
writeCommands(167, {`MODE_SQR012345, `RAM_B, `RAM_C, `RAM_C});
writeCommands(168, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(169, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(170, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(171, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(172, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(173, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(174, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(175, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(176, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(177, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(178, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(179, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(180, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(181, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(182, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(183, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(184, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(185, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(186, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(187, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(188, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(189, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(190, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(191, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(192, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(193, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(194, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(195, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(196, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(197, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(198, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(199, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(200, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(201, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(202, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(203, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(204, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(205, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}); // e = FrobFp24(e)
writeCommands(206, {`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}); // e = mulFp24(e, b)
// b = expFp24(b)
writeCommands(207, {`MODE_SQR012345, `RAM_B, `RAM_C, `RAM_C});
writeCommands(208, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(209, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(210, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(211, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(212, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(213, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(214, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(215, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(216, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(217, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(218, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(219, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(220, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(221, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(222, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(223, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(224, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(225, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(226, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(227, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(228, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(229, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(230, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(231, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(232, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(233, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(234, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(235, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(236, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(237, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(238, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(239, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(240, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(241, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(242, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(243, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(244, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(245, {`MODE_MUL, `RAM_B, `RAM_A, `RAM_B}); // b = mulFp24(b, a)
writeCommands(246, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}); // e = FrobFp24(e)
writeCommands(247, {`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}); // e = mulFp24(e, b)
// b = expFp24(b)
writeCommands(248, {`MODE_SQR012345, `RAM_B, `RAM_C, `RAM_C});
writeCommands(249, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(250, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(251, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(252, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(253, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(254, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(255, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(256, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(257, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(258, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(259, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(260, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(261, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(262, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(263, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(264, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(265, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(266, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(267, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(268, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(269, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(270, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(271, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(272, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(273, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(274, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(275, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(276, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(277, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(278, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(279, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(280, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(281, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(282, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(283, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(284, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(285, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(286, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}); // e = FrobFp24(e)
writeCommands(287, {`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}); // e = mulFp24(e, b)
// b = expFp24(b)
writeCommands(288, {`MODE_SQR012345, `RAM_B, `RAM_C, `RAM_C});
writeCommands(289, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(290, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(291, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(292, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(293, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(294, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(295, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(296, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(297, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(298, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(299, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(300, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(301, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(302, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(303, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(304, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(305, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(306, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(307, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(308, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(309, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(310, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(311, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(312, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(313, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(314, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(315, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(316, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(317, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(318, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(319, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(320, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(321, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(322, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(323, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(324, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(325, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(326, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}); // e = FrobFp24(e)
writeCommands(327, {`MODE_MUL, `RAM_E, `RAM_B, `RAM_E}); // e = mulFp24(e, b)
// b = expFp24(b)
writeCommands(328, {`MODE_SQR012345, `RAM_B, `RAM_C, `RAM_C});
writeCommands(329, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(330, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(331, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(332, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(333, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(334, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(335, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(336, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(337, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(338, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(339, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(340, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(341, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(342, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(343, {`MODE_CONJ, `RAM_C, `RAM_C, `RAM_B});
writeCommands(344, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(345, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(346, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(347, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(348, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(349, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(350, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(351, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(352, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(353, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(354, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(355, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(356, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(357, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(358, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(359, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(360, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(361, {`MODE_MUL_CONJ, `RAM_B, `RAM_C, `RAM_B});
writeCommands(362, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(363, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(364, {`MODE_SQR012345, `RAM_C, `RAM_C, `RAM_C});
writeCommands(365, {`MODE_MUL, `RAM_B, `RAM_C, `RAM_B});
writeCommands(366, {`MODE_SQR012345, `RAM_F, `RAM_F, `RAM_A}); // a = squareFp24(f)
writeCommands(367, {`MODE_MUL, `RAM_A, `RAM_B, `RAM_A}); // a = mulFp24(a, b)
writeCommands(368, {`MODE_MUL, `RAM_A, `RAM_F, `RAM_A}); // a = mulFp24(a, f)
writeCommands(369, {`MODE_FROB, `RAM_E, `RAM_E, `RAM_E}); // e = FrobFp24(e)
writeCommands(370, {`MODE_MUL, `RAM_E, `RAM_A, `RAM_E}); // e = mulFp24(e, a)
