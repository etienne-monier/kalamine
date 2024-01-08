import os
from textwrap import dedent

from kalamine import KeyboardLayout
from kalamine.template import osx_keymap, osx_actions, osx_terminators


def split(multiline_str):
    return dedent(multiline_str).lstrip().rstrip().splitlines()


EMPTY_KEYMAP = split('''
    <!-- Digits -->
    <key code="18"  output="&#x0010;" />
    <key code="19"  output="&#x0010;" />
    <key code="20"  output="&#x0010;" />
    <key code="21"  output="&#x0010;" />
    <key code="23"  output="&#x0010;" />
    <key code="22"  output="&#x0010;" />
    <key code="26"  output="&#x0010;" />
    <key code="28"  output="&#x0010;" />
    <key code="25"  output="&#x0010;" />
    <key code="29"  output="&#x0010;" />

    <!-- Letters, first row -->
    <key code="12"  output="&#x0010;" />
    <key code="13"  output="&#x0010;" />
    <key code="14"  output="&#x0010;" />
    <key code="15"  output="&#x0010;" />
    <key code="17"  output="&#x0010;" />
    <key code="16"  output="&#x0010;" />
    <key code="32"  output="&#x0010;" />
    <key code="34"  output="&#x0010;" />
    <key code="31"  output="&#x0010;" />
    <key code="35"  output="&#x0010;" />

    <!-- Letters, second row -->
    <key code="0"   output="&#x0010;" />
    <key code="1"   output="&#x0010;" />
    <key code="2"   output="&#x0010;" />
    <key code="3"   output="&#x0010;" />
    <key code="5"   output="&#x0010;" />
    <key code="4"   output="&#x0010;" />
    <key code="38"  output="&#x0010;" />
    <key code="40"  output="&#x0010;" />
    <key code="37"  output="&#x0010;" />
    <key code="41"  output="&#x0010;" />

    <!-- Letters, third row -->
    <key code="6"   output="&#x0010;" />
    <key code="7"   output="&#x0010;" />
    <key code="8"   output="&#x0010;" />
    <key code="9"   output="&#x0010;" />
    <key code="11"  output="&#x0010;" />
    <key code="45"  output="&#x0010;" />
    <key code="46"  output="&#x0010;" />
    <key code="43"  output="&#x0010;" />
    <key code="47"  output="&#x0010;" />
    <key code="44"  output="&#x0010;" />

    <!-- Pinky keys -->
    <key code="27"  output="&#x0010;" />
    <key code="24"  output="&#x0010;" />
    <key code="33"  output="&#x0010;" />
    <key code="30"  output="&#x0010;" />
    <key code="39"  output="&#x0010;" />
    <key code="50"  output="&#x0010;" />
    <key code="42"  output="&#x0010;" />
    <key code="10"  output="&#x0010;" />

    <!-- Space bar -->
    <key code="49"  output="&#x0010;" />
    ''')


def test_ansi():
    layout = KeyboardLayout(os.path.join('.', 'layouts', 'ansi.toml'))

    keymap = osx_keymap(layout)

    assert len(keymap[0]) == 60
    assert keymap[0] == split('''
        <!-- Digits -->
        <key code="18"  output="1" />
        <key code="19"  output="2" />
        <key code="20"  output="3" />
        <key code="21"  output="4" />
        <key code="23"  output="5" />
        <key code="22"  output="6" />
        <key code="26"  output="7" />
        <key code="28"  output="8" />
        <key code="25"  output="9" />
        <key code="29"  output="0" />

        <!-- Letters, first row -->
        <key code="12"  output="q" />
        <key code="13"  output="w" />
        <key code="14"  output="e" />
        <key code="15"  output="r" />
        <key code="17"  output="t" />
        <key code="16"  output="y" />
        <key code="32"  output="u" />
        <key code="34"  output="i" />
        <key code="31"  output="o" />
        <key code="35"  output="p" />

        <!-- Letters, second row -->
        <key code="0"   output="a" />
        <key code="1"   output="s" />
        <key code="2"   output="d" />
        <key code="3"   output="f" />
        <key code="5"   output="g" />
        <key code="4"   output="h" />
        <key code="38"  output="j" />
        <key code="40"  output="k" />
        <key code="37"  output="l" />
        <key code="41"  output=";" />

        <!-- Letters, third row -->
        <key code="6"   output="z" />
        <key code="7"   output="x" />
        <key code="8"   output="c" />
        <key code="9"   output="v" />
        <key code="11"  output="b" />
        <key code="45"  output="n" />
        <key code="46"  output="m" />
        <key code="43"  output="," />
        <key code="47"  output="." />
        <key code="44"  output="/" />

        <!-- Pinky keys -->
        <key code="27"  output="-" />
        <key code="24"  output="=" />
        <key code="33"  output="[" />
        <key code="30"  output="]" />
        <key code="39"  output="'" />
        <key code="50"  output="`" />
        <key code="42"  output="\\" />
        <key code="10"  output="&#x0010;" />

        <!-- Space bar -->
        <key code="49"  action="x0020" />
        ''')

    assert len(keymap[1]) == 60
    assert keymap[1] == split('''
        <!-- Digits -->
        <key code="18"  output="!" />
        <key code="19"  output="@" />
        <key code="20"  output="#" />
        <key code="21"  output="$" />
        <key code="23"  output="%" />
        <key code="22"  output="^" />
        <key code="26"  output="&#x0026;" />
        <key code="28"  output="*" />
        <key code="25"  output="(" />
        <key code="29"  output=")" />

        <!-- Letters, first row -->
        <key code="12"  output="Q" />
        <key code="13"  output="W" />
        <key code="14"  output="E" />
        <key code="15"  output="R" />
        <key code="17"  output="T" />
        <key code="16"  output="Y" />
        <key code="32"  output="U" />
        <key code="34"  output="I" />
        <key code="31"  output="O" />
        <key code="35"  output="P" />

        <!-- Letters, second row -->
        <key code="0"   output="A" />
        <key code="1"   output="S" />
        <key code="2"   output="D" />
        <key code="3"   output="F" />
        <key code="5"   output="G" />
        <key code="4"   output="H" />
        <key code="38"  output="J" />
        <key code="40"  output="K" />
        <key code="37"  output="L" />
        <key code="41"  output=":" />

        <!-- Letters, third row -->
        <key code="6"   output="Z" />
        <key code="7"   output="X" />
        <key code="8"   output="C" />
        <key code="9"   output="V" />
        <key code="11"  output="B" />
        <key code="45"  output="N" />
        <key code="46"  output="M" />
        <key code="43"  output="&#x003c;" />
        <key code="47"  output="&#x003e;" />
        <key code="44"  output="?" />

        <!-- Pinky keys -->
        <key code="27"  output="_" />
        <key code="24"  output="+" />
        <key code="33"  output="{" />
        <key code="30"  output="}" />
        <key code="39"  output="&#x0022;" />
        <key code="50"  output="~" />
        <key code="42"  output="|" />
        <key code="10"  output="&#x0010;" />

        <!-- Space bar -->
        <key code="49"  action="x0020" />
        ''')

    assert len(keymap[2]) == 60
    assert keymap[2] == split('''
        <!-- Digits -->
        <key code="18"  output="1" />
        <key code="19"  output="2" />
        <key code="20"  output="3" />
        <key code="21"  output="4" />
        <key code="23"  output="5" />
        <key code="22"  output="6" />
        <key code="26"  output="7" />
        <key code="28"  output="8" />
        <key code="25"  output="9" />
        <key code="29"  output="0" />

        <!-- Letters, first row -->
        <key code="12"  output="Q" />
        <key code="13"  output="W" />
        <key code="14"  output="E" />
        <key code="15"  output="R" />
        <key code="17"  output="T" />
        <key code="16"  output="Y" />
        <key code="32"  output="U" />
        <key code="34"  output="I" />
        <key code="31"  output="O" />
        <key code="35"  output="P" />

        <!-- Letters, second row -->
        <key code="0"   output="A" />
        <key code="1"   output="S" />
        <key code="2"   output="D" />
        <key code="3"   output="F" />
        <key code="5"   output="G" />
        <key code="4"   output="H" />
        <key code="38"  output="J" />
        <key code="40"  output="K" />
        <key code="37"  output="L" />
        <key code="41"  output=";" />

        <!-- Letters, third row -->
        <key code="6"   output="Z" />
        <key code="7"   output="X" />
        <key code="8"   output="C" />
        <key code="9"   output="V" />
        <key code="11"  output="B" />
        <key code="45"  output="N" />
        <key code="46"  output="M" />
        <key code="43"  output="," />
        <key code="47"  output="." />
        <key code="44"  output="/" />

        <!-- Pinky keys -->
        <key code="27"  output="-" />
        <key code="24"  output="=" />
        <key code="33"  output="[" />
        <key code="30"  output="]" />
        <key code="39"  output="'" />
        <key code="50"  output="`" />
        <key code="42"  output="\\" />
        <key code="10"  output="&#x0010;" />

        <!-- Space bar -->
        <key code="49"  action="x0020" />
        ''')

    assert len(keymap[3]) == 60
    assert keymap[3] == EMPTY_KEYMAP

    assert len(keymap[4]) == 60
    assert keymap[4] == EMPTY_KEYMAP

    actions = osx_actions(layout)
    assert actions[1:] == split('''
        <!-- Digits -->

        <!-- Letters, first row -->

        <!-- Letters, second row -->

        <!-- Letters, third row -->

        <!-- Pinky keys -->

        <!-- Space bar -->
        <action id="x0020">
          <when state="none"       output="&#x0020;" />
        </action>
        <action id="x00a0">
          <when state="none"       output="&#x00a0;" />
        </action>
        <action id="x202f">
          <when state="none"       output="&#x202f;" />
        </action>
        ''')

    terminators = osx_terminators(layout)
    assert len(terminators) == 0
