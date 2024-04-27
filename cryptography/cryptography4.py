import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_frame import EasyFrame
from LeleEasyTkinter.easy_label import EasyLabel
from LeleEasyTkinter.easy_multi_text import EasyMultiText


def quit_window():
    window.destroy()


def encryption():
    return


def decryption():
    return


window = tk.Tk()
EasyAutoWindow(window, window_title="CryptographyMethod", minimum_value_x=1312, minimum_value_y=876,
               maximum_value_x=1640, maximum_value_y=980, window_width_value=1400, window_height_value=890)

f1 = EasyFrame(window, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f11 = EasyFrame(f1, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f12 = EasyFrame(f1, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f13 = EasyFrame(f1, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f14 = EasyFrame(f1, fill=tk.BOTH, is_debug=True, side=tk.RIGHT, expand=tk.YES).get()

f2 = EasyFrame(window, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f21 = EasyFrame(f2, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f22 = EasyFrame(f2, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f23 = EasyFrame(f2, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f24 = EasyFrame(f2, fill=tk.BOTH, is_debug=True, side=tk.RIGHT, expand=tk.YES).get()

EasyLabel(f11, text="要加密的文本:", side=tk.LEFT)
EasyMultiText(f11, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
EasyLabel(f12, text="加密时的密钥:", side=tk.LEFT)
EasyMultiText(f12, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
EasyLabel(f13, text="加密后的文本:", side=tk.LEFT)
EasyMultiText(f13, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
EasyButton(f14, text="加密", fill=tk.BOTH, side=tk.TOP, expand=tk.YES, height=2)

EasyLabel(f21, text="要解密的文本:", side=tk.LEFT)
EasyMultiText(f21, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
EasyLabel(f22, text="解密时的密钥:", side=tk.LEFT)
EasyMultiText(f22, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
EasyLabel(f23, text="解密后的文本:", side=tk.LEFT)
EasyMultiText(f23, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
EasyButton(f24, text="解密", fill=tk.BOTH, side=tk.TOP, expand=tk.YES, height=2)

EasyButton(window, text="退出", fill=tk.BOTH, side=tk.TOP, expand=tk.NO, height=2)

window.mainloop()
