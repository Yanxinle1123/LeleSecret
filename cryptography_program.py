import tkinter as tk

from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_drop_list import EasyDropList
from LeleEasyTkinter.easy_fade_animation import fade_in, fade_out
from LeleEasyTkinter.easy_frame import EasyFrame
from LeleEasyTkinter.easy_label import EasyLabel
from LeleEasyTkinter.easy_multi_text import EasyMultiText
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows

from RSA.RSA_method import RSADecryptionMethod, RSAEncryptionMethod


def on_window_close():
    global settings_window, num

    if num == 1:
        fade_out(settings_window)
    fade_out(window)


def on_settings_window_close():
    global settings_window, num

    fade_out(settings_window)
    num -= 1


def quit_window():
    global settings_window, num

    if num == 1:
        fade_out(settings_window)
    fade_out(window)


def replace(text_box, text):
    text_box.get_text().config(state="normal")
    text_box.get_text().delete("1.0", tk.END)
    text_box.get_text().insert(tk.END, text)
    text_box.get_text().config(state="disabled")


def encryption():
    REM = RSAEncryptionMethod(encryption_text_need.get_content())
    cipher_text, key = REM.encryption()
    replace(key_text, key)
    replace(encryption_text_after, cipher_text)


def decryption():
    try:
        RDM = RSADecryptionMethod(decryption_text_need.get_content(), key_text_need.get_content())
        plain_text = RDM.decryption()
        replace(decryption_text_after, plain_text)
    except UnicodeDecodeError:
        EasyWarningWindows("警告", "错误\n\n解密后的数据无法使用UTF-8编码解码, 请检查输入的密钥是否正确").show_warning()
    except ValueError:
        EasyWarningWindows("警告", "错误\n\n输入的密钥或密文不正确").show_warning()


def settings():
    global settings_window, num

    if num != 1:
        num += 1
        settings_window = tk.Toplevel()

        EasyAutoWindow(settings_window, window_title="settings", window_width_value=600, window_height_value=150,
                       adjust_x=False, adjust_y=False)

        f1 = EasyFrame(settings_window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f2 = EasyFrame(settings_window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f3 = EasyFrame(settings_window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()

        EasyLabel(f1, text="加密解密的算法:", side=tk.LEFT)
        EasyDropList(f1, options=['AES', 'Fernet', 'RSA'], side=tk.LEFT)

        EasyLabel(f2, text="主题:", side=tk.LEFT)
        EasyDropList(f2, options=['跟随系统', '自动', '深色', '浅色'], side=tk.LEFT)

        EasyButton(f3, text="保存并退出设置", expand=tk.YES, height=2, cmd=on_settings_window_close)

        fade_in(settings_window)
        settings_window.attributes('-topmost', 'true')
        settings_window.protocol("WM_DELETE_WINDOW", on_settings_window_close)


settings_window = None
num = 0
window = tk.Tk()
EasyAutoWindow(window, window_title="cryptography", minimum_value_x=1312, minimum_value_y=876,
               window_width_value=1400, window_height_value=890)

f1 = EasyFrame(window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f11 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f12 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f13 = EasyFrame(f1, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f14 = EasyFrame(f1, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES).get()

f2 = EasyFrame(window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f21 = EasyFrame(f2, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f22 = EasyFrame(f2, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f23 = EasyFrame(f2, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
f24 = EasyFrame(f2, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES).get()

EasyLabel(f11, text="要加密的文本:", side=tk.LEFT)
encryption_text_need = EasyMultiText(f11, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

EasyLabel(f12, text="加密时的密钥:", side=tk.LEFT)
key_text = EasyMultiText(f12, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
key_text.get_text().config(state="disabled")

EasyLabel(f13, text="加密后的文本:", side=tk.LEFT)
encryption_text_after = EasyMultiText(f13, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
encryption_text_after.get_text().config(state="disabled")

EasyButton(f14, text="加密", fill=tk.BOTH, side=tk.TOP, expand=tk.YES, height=2, cmd=encryption)

EasyLabel(f21, text="要解密的文本:", side=tk.LEFT)
decryption_text_need = EasyMultiText(f21, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

EasyLabel(f22, text="解密时的密钥:", side=tk.LEFT)
key_text_need = EasyMultiText(f22, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

EasyLabel(f23, text="解密后的文本:", side=tk.LEFT)
decryption_text_after = EasyMultiText(f23, fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
decryption_text_after.get_text().config(state="disabled")

EasyButton(f24, text="解密", fill=tk.BOTH, side=tk.TOP, expand=tk.YES, height=2, cmd=decryption)

EasyButton(window, text="退出", fill=tk.BOTH, side=tk.TOP, expand=tk.NO, height=2, cmd=quit_window)

EasyButton(window, text="设置", side=tk.RIGHT, width=5, height=2, cmd=settings)

fade_in(window, ms=500)
window.protocol("WM_DELETE_WINDOW", on_window_close)
window.mainloop()