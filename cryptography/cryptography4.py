import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow

window = tk.Tk()
EasyAutoWindow(window, window_title="CryptographyMethod", minimum_value_x=800, minimum_value_y=500,
               maximum_value_x=1640, maximum_value_y=980)
window.mainloop()
