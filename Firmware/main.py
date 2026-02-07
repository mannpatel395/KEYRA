from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import Oled, OledDisplayMode
from kmk.extensions.media_keys import MediaKeys

# -------------------------
# Keyboard setup
# -------------------------
keyboard = KMKKeyboard()

keyboard.col_pins = (28, 29)   # COL0, COL1
keyboard.row_pins = (26, 27)   # ROW0, ROW1

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# -------------------------
# Keymap (2x2)
# Layout:
# [ K1  K2 ]
# [ K3  K4 ]
# -------------------------
keyboard.keymap = [
    [
        'A', 'B',
        'C', 'D',
    ]
]

# -------------------------
# Encoder
# -------------------------
encoder = EncoderHandler()
encoder.pins = ((2, 4),)  # (A, B)
encoder.map = [
    (( 'VOLD', 'VOLU' ),)  # rotate left / right
]
keyboard.modules.append(encoder)

# -------------------------
# Encoder Button
# -------------------------
keyboard.coord_mapping.append((1, 0))  # maps encoder button
keyboard.keymap[0].append('MUTE')

# -------------------------
# OLED
# -------------------------
oled = Oled(
    sda=6,
    scl=7,
    to_display=OledDisplayMode.TEXT,
    flip=False,
)
keyboard.modules.append(oled)

# -------------------------
# Media keys
# -------------------------
keyboard.extensions.append(MediaKeys())

# -------------------------
# Start KMK
# -------------------------
if __name__ == '__main__':
    keyboard.go()
