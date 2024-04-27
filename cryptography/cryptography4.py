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
EasyAutoWindow(window, window_title="CryptographyMethod", minimum_value_x=800, minimum_value_y=500,
               maximum_value_x=1640, maximum_value_y=980, window_height_value=720, window_width_value=1150)

f1 = EasyFrame(window, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f11 = EasyFrame(f1, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f111 = EasyFrame(f11, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f112 = EasyFrame(f11, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f113 = EasyFrame(f11, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()

f12 = EasyFrame(f1, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f121 = EasyFrame(f12, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f122 = EasyFrame(f12, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()
f123 = EasyFrame(f12, fill=tk.BOTH, is_debug=True, side=tk.TOP, expand=tk.YES).get()

f2 = EasyFrame(window, fill=tk.BOTH, is_debug=True, side=tk.TOP).get()

EasyLabel(f111, text="加密:", side=tk.LEFT)
EasyButton(f113, text="加密", side=tk.TOP, fill=tk.BOTH)
EasyMultiText(f111, fill=tk.BOTH, side=tk.TOP, expand=tk.YES)

EasyLabel(f121, text="密钥:", side=tk.LEFT)
EasyMultiText(f121, fill=tk.BOTH, side=tk.TOP, expand=tk.YES)

EasyLabel(f112, text="密钥:", side=tk.LEFT)
EasyMultiText(f112, fill=tk.BOTH, side=tk.TOP, expand=tk.YES)

EasyLabel(f122, text="解密:", side=tk.LEFT)
EasyButton(f122, text="解密", side=tk.RIGHT, fill=tk.BOTH)
EasyMultiText(f122, fill=tk.BOTH, side=tk.TOP, expand=tk.YES)

EasyButton(f2, text="退出", expand=tk.YES, fill=tk.BOTH, height=2, cmd=quit_window)

window.mainloop()
