print("Starting")
import board
# import neopixel
# 
# pixels = neopixel.NeoPixel(board.D6, 1, brightness=0.3, auto_write=False)
# 
# pixels.fill((255,0,0))

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros, Delay, Tap, Press, Release
keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
macros = Macros()
media = MediaKeys()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(media)
# Matrix pins
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2
ROW1 = board.D7
ROW2 = board.D8
ROW3 = board.D10
# rotary encoder pins
ROTA = board.D3
ROTB = board.D9
PUSHBUTTON = None
# Matrix settings
keyboard.row_pins = (COL1, COL2, COL3)
keyboard.col_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL
# Encoder settingsadgbe7890987iadgbe7890987iiii7890987eeeeeeeeeee
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, True),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

# 

PAWD = KC.MACRO(
    "7",
    Delay(300),
    "-------" #censored
)

CTV = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Delay(100),
    Tap(KC.T),
    Delay(100),
    Tap(KC.V),
    Release(KC.LCTL),
)

WK = KC.MACRO(
    Tap(KC.LWIN),
    "WaniKani",
    Tap(KC.ENTER)
)

JLC = KC.MACRO(
    Tap(KC.LCTL(KC.T)),
    "https://jlcpcb.com/parts/all-electronic-components",
    Tap(KC.ENTER)
)

ENTER = KC.ENTER

keyboard.keymap = [
    [
        KC.LSHIFT(KC.B)		, KC.N1	, KC.LALT(KC.T)	, WK		, PAWD		,
        KC.LSHIFT(KC.M)		, KC.N2	, KC.LALT(KC.B)	, JLC		
    ]
]
if __name__ == "__main__":
    keyboard.go()


