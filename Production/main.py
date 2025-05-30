import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.A0, board.A1, board.A2)
keyboard.row_pins = (board.GPIO1, board.GPIO2, board.GPIO3)

keyboard.diode_orientation = DiodeOrientation.COL2ROW



# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

keyboard.keymap = [
    #[KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
    [KC.N1, KC.N2, KC.N3], [KC.N4, KC.N5,
                            
    KC.N6], [KC.N7, KC.N8, KC.N9],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
