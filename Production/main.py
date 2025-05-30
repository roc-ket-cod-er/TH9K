print("Starting")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros
keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
macros = Macros()
media = MediaKeys()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(media)
# Matrix pins
COL1 = board.A0
COL2 = board.A1
COL3 = board.A2
ROW1 = board.D1
ROW2 = board.D2
ROW3 = board.D3
# rotary encoder pins
ROTA = board.A3
ROTB = board.D4
PUSHBUTTON = board.D9
# Matrix settings
keyboard.col_pins = (COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
# Encoder settings
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D, KC.E
        KC.F, KC.G, KC.H, KC.I
    ]
]
if __name__ == "__main__":
    keyboard.go()
