import os
from textwrap import dedent

from kalamine import KeyboardLayout
from kalamine.template import klc_keymap, klc_deadkeys, klc_dk_index


def load_layout(filename):
    return KeyboardLayout(os.path.join('.', 'layouts', filename + '.toml'))


def split(multiline_str):
    return dedent(multiline_str).lstrip().rstrip().splitlines()


def test_ansi():
    layout = load_layout('ansi')

    keymap = klc_keymap(layout)
    assert len(keymap) == 49
    assert keymap == split('''
        02	1	0	1	0021	-1	// 1 !
        03	2	0	2	0040	-1	// 2 @
        04	3	0	3	0023	-1	// 3 #
        05	4	0	4	0024	-1	// 4 $
        06	5	0	5	0025	-1	// 5 %
        07	6	0	6	005e	-1	// 6 ^
        08	7	0	7	0026	-1	// 7 &
        09	8	0	8	002a	-1	// 8 *
        0a	9	0	9	0028	-1	// 9 (
        0b	0	0	0	0029	-1	// 0 )
        10	Q	1	q	Q	-1	// q Q
        11	W	1	w	W	-1	// w W
        12	E	1	e	E	-1	// e E
        13	R	1	r	R	-1	// r R
        14	T	1	t	T	-1	// t T
        15	Y	1	y	Y	-1	// y Y
        16	U	1	u	U	-1	// u U
        17	I	1	i	I	-1	// i I
        18	O	1	o	O	-1	// o O
        19	P	1	p	P	-1	// p P
        1e	A	1	a	A	-1	// a A
        1f	S	1	s	S	-1	// s S
        20	D	1	d	D	-1	// d D
        21	F	1	f	F	-1	// f F
        22	G	1	g	G	-1	// g G
        23	H	1	h	H	-1	// h H
        24	J	1	j	J	-1	// j J
        25	K	1	k	K	-1	// k K
        26	L	1	l	L	-1	// l L
        27	OEM_1	0	003b	003a	-1	// ; :
        2c	Z	1	z	Z	-1	// z Z
        2d	X	1	x	X	-1	// x X
        2e	C	1	c	C	-1	// c C
        2f	V	1	v	V	-1	// v V
        30	B	1	b	B	-1	// b B
        31	N	1	n	N	-1	// n N
        32	M	1	m	M	-1	// m M
        33	OEM_COMMA	0	002c	003c	-1	// , <
        34	OEM_PERIOD	0	002e	003e	-1	// . >
        35	OEM_2	0	002f	003f	-1	// / ?
        0c	OEM_MINUS	0	002d	005f	-1	// - _
        0d	OEM_PLUS	0	003d	002b	-1	// = +
        1a	OEM_4	0	005b	007b	-1	// [ {
        1b	OEM_6	0	005d	007d	-1	// ] }
        28	OEM_7	0	0027	0022	-1	// ' "
        29	OEM_3	0	0060	007e	-1	// ` ~
        2b	OEM_5	0	005c	007c	-1	// \\ |
        56	OEM_102	0	-1	-1	-1	//
        39	SPACE	0	0020	0020	-1	//
        ''')

    assert len(klc_dk_index(layout)) == 0
    assert len(klc_deadkeys(layout)) == 0


def test_intl():
    layout = load_layout('intl')

    keymap = klc_keymap(layout)
    assert len(keymap) == 49
    assert keymap == split('''
        02	1	0	1	0021	-1	// 1 !
        03	2	0	2	0040	-1	// 2 @
        04	3	0	3	0023	-1	// 3 #
        05	4	0	4	0024	-1	// 4 $
        06	5	0	5	0025	-1	// 5 %
        07	6	0	6	005e@	-1	// 6 ^
        08	7	0	7	0026	-1	// 7 &
        09	8	0	8	002a	-1	// 8 *
        0a	9	0	9	0028	-1	// 9 (
        0b	0	0	0	0029	-1	// 0 )
        10	Q	1	q	Q	-1	// q Q
        11	W	1	w	W	-1	// w W
        12	E	1	e	E	-1	// e E
        13	R	1	r	R	-1	// r R
        14	T	1	t	T	-1	// t T
        15	Y	1	y	Y	-1	// y Y
        16	U	1	u	U	-1	// u U
        17	I	1	i	I	-1	// i I
        18	O	1	o	O	-1	// o O
        19	P	1	p	P	-1	// p P
        1e	A	1	a	A	-1	// a A
        1f	S	1	s	S	-1	// s S
        20	D	1	d	D	-1	// d D
        21	F	1	f	F	-1	// f F
        22	G	1	g	G	-1	// g G
        23	H	1	h	H	-1	// h H
        24	J	1	j	J	-1	// j J
        25	K	1	k	K	-1	// k K
        26	L	1	l	L	-1	// l L
        27	OEM_1	0	003b	003a	-1	// ; :
        2c	Z	1	z	Z	-1	// z Z
        2d	X	1	x	X	-1	// x X
        2e	C	1	c	C	-1	// c C
        2f	V	1	v	V	-1	// v V
        30	B	1	b	B	-1	// b B
        31	N	1	n	N	-1	// n N
        32	M	1	m	M	-1	// m M
        33	OEM_COMMA	0	002c	003c	-1	// , <
        34	OEM_PERIOD	0	002e	003e	-1	// . >
        35	OEM_2	0	002f	003f	-1	// / ?
        0c	OEM_MINUS	0	002d	005f	-1	// - _
        0d	OEM_PLUS	0	003d	002b	-1	// = +
        1a	OEM_4	0	005b	007b	-1	// [ {
        1b	OEM_6	0	005d	007d	-1	// ] }
        28	OEM_7	0	0027@	0022@	-1	// ' "
        29	OEM_3	0	0060@	007e@	-1	// ` ~
        2b	OEM_5	0	005c	007c	-1	// \\ |
        56	OEM_102	0	005c	007c	-1	// \\ |
        39	SPACE	0	0020	0020	-1	//
        ''')

    assert len(klc_dk_index(layout)) == 5
    assert len(klc_deadkeys(layout)) == 138


def test_prog():
    layout = load_layout('prog')

    keymap = klc_keymap(layout)
    assert len(keymap) == 49
    assert keymap == split('''
        02	1	0	1	0021	-1	0021	-1	// 1 ! !
        03	2	0	2	0040	-1	0028	-1	// 2 @ (
        04	3	0	3	0023	-1	0029	-1	// 3 # )
        05	4	0	4	0024	-1	0027	-1	// 4 $ '
        06	5	0	5	0025	-1	0022	-1	// 5 % "
        07	6	0	6	005e	-1	005e@	-1	// 6 ^ ^
        08	7	0	7	0026	-1	7	-1	// 7 & 7
        09	8	0	8	002a	-1	8	-1	// 8 * 8
        0a	9	0	9	0028	-1	9	-1	// 9 ( 9
        0b	0	0	0	0029	-1	002f	-1	// 0 ) /
        10	Q	1	q	Q	-1	003d	-1	// q Q =
        11	W	1	w	W	-1	003c	2264	// w W < ≤
        12	E	1	e	E	-1	003e	2265	// e E > ≥
        13	R	1	r	R	-1	002d	-1	// r R -
        14	T	1	t	T	-1	002b	-1	// t T +
        15	Y	1	y	Y	-1	-1	-1	// y Y
        16	U	1	u	U	-1	4	-1	// u U 4
        17	I	1	i	I	-1	5	-1	// i I 5
        18	O	1	o	O	-1	6	-1	// o O 6
        19	P	1	p	P	-1	002a	-1	// p P *
        1e	A	1	a	A	-1	007b	-1	// a A {
        1f	S	1	s	S	-1	005b	-1	// s S [
        20	D	1	d	D	-1	005d	-1	// d D ]
        21	F	1	f	F	-1	007d	-1	// f F }
        22	G	1	g	G	-1	002f	-1	// g G /
        23	H	1	h	H	-1	-1	-1	// h H
        24	J	1	j	J	-1	1	-1	// j J 1
        25	K	1	k	K	-1	2	-1	// k K 2
        26	L	1	l	L	-1	3	-1	// l L 3
        27	OEM_1	0	003b	003a	-1	002d	-1	// ; : -
        2c	Z	1	z	Z	-1	007e	-1	// z Z ~
        2d	X	1	x	X	-1	0060	-1	// x X `
        2e	C	1	c	C	-1	007c	00a6	// c C | ¦
        2f	V	1	v	V	-1	005f	-1	// v V _
        30	B	1	b	B	-1	005c	-1	// b B \\
        31	N	1	n	N	-1	-1	-1	// n N
        32	M	1	m	M	-1	0	-1	// m M 0
        33	OEM_COMMA	0	002c	003c	-1	002c	-1	// , < ,
        34	OEM_PERIOD	0	002e	003e	-1	002e	-1	// . > .
        35	OEM_2	0	002f	003f	-1	002b	-1	// / ? +
        0c	OEM_MINUS	0	002d	005f	-1	-1	-1	// - _
        0d	OEM_PLUS	0	003d	002b	-1	-1	-1	// = +
        1a	OEM_4	0	005b	007b	-1	-1	-1	// [ {
        1b	OEM_6	0	005d	007d	-1	-1	-1	// ] }
        28	OEM_7	0	0027	0022	-1	0027@	0022@	// ' " ' "
        29	OEM_3	0	0060	007e	-1	0060@	007e@	// ` ~ ` ~
        2b	OEM_5	0	005c	007c	-1	-1	-1	// \\ |
        56	OEM_102	0	-1	-1	-1	-1	-1	//
        39	SPACE	0	0020	0020	-1	0020	0020	//
        ''')

    assert len(klc_dk_index(layout)) == 5
    assert len(klc_deadkeys(layout)) == 158
