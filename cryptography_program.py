import binascii
import tkinter as tk

import customtkinter as ctk
from LeleEasyTkinter.easy_auto_window import EasyAutoWindow
from LeleEasyTkinter.easy_button import EasyButton
from LeleEasyTkinter.easy_drop_list import EasyDropList
from LeleEasyTkinter.easy_fade_animation import fade_in, fade_out
from LeleEasyTkinter.easy_frame import EasyFrame
from LeleEasyTkinter.easy_label import EasyLabel
from LeleEasyTkinter.easy_multi_text import EasyMultiText
from LeleEasyTkinter.easy_warning_windows import EasyWarningWindows
from cryptography.exceptions import InvalidTag
from cryptography.fernet import InvalidToken

from AEAD.AEAD_method import AEADEncryptionMethod, AEADDecryptionMethod
from AES.AES_method import AESEncryptionMethod, AESDecryptionMethod
from Fernet.Fernet_method import FernetEncryptionMethod, FernetDecryptionMethod
from RSA.RSA_method import RSADecryptionMethod, RSAEncryptionMethod


def quit_window():
    global settings_window, settings_num, instructions_num

    if settings_num == 1:
        on_settings_window_close2()
    if instructions_num == 1:
        on_instructions_window_close()
    fade_out(window, ms=4)


def on_settings_window_close():
    global settings_window, settings_num

    save_settings()
    fade_out(settings_window, ms=4)
    settings_num -= 1


def on_settings_window_close2():
    global settings_window, settings_num

    result = EasyWarningWindows("是/否", "是否保存更改？").show_warning()
    if result:
        save_settings()
    fade_out(settings_window, ms=4)
    settings_num -= 1


def on_instructions_window_close():
    global instructions_window, instructions_num

    fade_out(instructions_window, ms=4)
    instructions_num -= 1


def replace(text_box, text):
    text_box.get_text().config(state="normal")
    text_box.get_text().delete("1.0", tk.END)
    text_box.get_text().insert(tk.END, text)
    text_box.get_text().config(state="disabled")


def get_data():
    decryption_text = decryption_text_need.get_content()
    key_and_algorithm = key_text_need.get_content()
    algorithm_choice = key_and_algorithm[0]
    key = key_and_algorithm[1:]
    return decryption_text, algorithm_choice, key


def AES_encryption():
    encrypt_obj = AESEncryptionMethod(encryption_text_need.get_content())
    cipher_text, key = encrypt_obj.encryption()
    key = f'2{key}'
    replace(key_text, key)
    replace(encryption_text_after, cipher_text)


def Fernet_encryption():
    CEM = FernetEncryptionMethod(encryption_text_need.get_content())
    key, cipher_text = CEM.encryption()
    key = f'3{key}'
    replace(key_text, key)
    replace(encryption_text_after, cipher_text)


def RSA_encryption():
    REM = RSAEncryptionMethod(encryption_text_need.get_content())
    cipher_text, key = REM.encryption()
    key = f'4{key}'
    replace(key_text, key)
    replace(encryption_text_after, cipher_text)


def AEAD_encryption():
    AEADEM = AEADEncryptionMethod(encryption_text_need.get_content())
    cipher_text, key = AEADEM.encryption()
    key = f'5{key}'
    replace(key_text, key)
    replace(encryption_text_after, cipher_text)


def auto_encryption():
    if len(encryption_text_need.get_content().encode('utf-8')) <= 50:
        RSA_encryption()
    else:
        AEAD_encryption()


def AES_decryption(decryption_text, key):
    try:
        decrypt_obj = AESDecryptionMethod(decryption_text, key)
        plain_text = decrypt_obj.decryption()
        replace(decryption_text_after, plain_text)
    except TypeError:
        EasyWarningWindows("警告", "错误\n\n无效的密钥, 请输入正确的Base64编码密钥").show_warning()
    except binascii.Error:
        EasyWarningWindows("警告", "错误\n\n密钥长度不正确, 请输入正确的Base64编码密钥").show_warning()
    except InvalidTag:
        EasyWarningWindows("警告", "错误\n\n解密失败, 密钥不正确").show_warning()
    except ValueError:
        EasyWarningWindows("警告", "错误\n\n解密失败, 密文长度不正确").show_warning()
    except Exception as e:
        EasyWarningWindows("警告", f"未知错误\n\n{str(e)}").show_warning()


def Fernet_decryption(decryption_text, key):
    try:
        CDM = FernetDecryptionMethod(decryption_text, key)
        plain_text = CDM.decryption()
        replace(decryption_text_after, plain_text)
    except ValueError:
        EasyWarningWindows("警告", "错误\n\n无效的密钥, 请输入32个URL安全的base64编码字节").show_warning()
    except InvalidToken:
        EasyWarningWindows("警告", "错误\n\n解密失败, 密钥或密文无效").show_warning()


def RSA_decryption(decryption_text, key):
    try:
        RDM = RSADecryptionMethod(decryption_text, key)
        plain_text = RDM.decryption()
        replace(decryption_text_after, plain_text)
    except UnicodeDecodeError:
        EasyWarningWindows("警告",
                           "错误\n\n解密后的数据无法使用UTF-8编码解码, 请检查输入的密钥是否正确").show_warning()
    except ValueError:
        EasyWarningWindows("警告", "错误\n\n输入的密钥或密文不正确").show_warning()
    except IndexError:
        EasyWarningWindows("警告", "错误\n\n解密失败, 密钥错误").show_warning()


def AEAD_decryption(decryption_text, key):
    try:
        AEADDM = AEADDecryptionMethod(decryption_text, key)
        plain_text = AEADDM.decryption()
        replace(decryption_text_after, plain_text)
    except ValueError:
        EasyWarningWindows("警告", "错误\n\n解密失败, 无效的密文或密钥").show_warning()
    except IndexError:
        EasyWarningWindows("警告", "错误\n\n解密失败, 密钥错误").show_warning()


def encryption():
    global algorithm_settings

    with open('settings/algorithm_settings.txt', 'r', encoding='utf-8') as file:
        algorithm_settings = file.read()
    if algorithm_settings == '自动':
        algorithm_settings = 1
    elif algorithm_settings == 'AES':
        algorithm_settings = 2
    elif algorithm_settings == 'Fernet':
        algorithm_settings = 3
    elif algorithm_settings == 'RSA':
        algorithm_settings = 4
    elif algorithm_settings == 'AEAD':
        algorithm_settings = 5
    if algorithm_settings == 1:
        auto_encryption()
    elif algorithm_settings == 2:
        AES_encryption()
    elif algorithm_settings == 3:
        Fernet_encryption()
    elif algorithm_settings == 4:
        RSA_encryption()
    elif algorithm_settings == 5:
        AEAD_encryption()


def decryption():
    decryption_text, algorithm_choice, key = get_data()

    if algorithm_choice == '2':
        AES_decryption(decryption_text, key)
    elif algorithm_choice == '3':
        Fernet_decryption(decryption_text, key)
    elif algorithm_choice == '4':
        RSA_decryption(decryption_text, key)
    elif algorithm_choice == '5':
        AEAD_decryption(decryption_text, key)


def save_settings():
    global algorithm

    with open('settings/algorithm_settings.txt', 'w', encoding='utf-8') as file:
        file.write(algorithm.get_combo_value())


def settings():
    global settings_window, settings_num, algorithm, algorithm_settings

    if settings_num != 1:
        settings_num += 1

        with open('settings/algorithm_settings.txt', 'r', encoding='utf-8') as file:
            algorithm_settings = file.read()
        if algorithm_settings == '自动':
            algorithm_settings = 1
        elif algorithm_settings == 'AES':
            algorithm_settings = 2
        elif algorithm_settings == 'Fernet':
            algorithm_settings = 3
        elif algorithm_settings == 'RSA':
            algorithm_settings = 4
        elif algorithm_settings == 'AEAD':
            algorithm_settings = 5

        settings_window = ctk.CTkToplevel()

        EasyAutoWindow(settings_window, window_title="settings", window_width_value=600, window_height_value=150,
                       adjust_x=False, adjust_y=False)

        f1 = EasyFrame(settings_window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()
        f2 = EasyFrame(settings_window, fill=tk.BOTH, side=tk.TOP, expand=tk.YES).get()

        EasyLabel(f1, text="加密解密的算法:", side=tk.LEFT)
        algorithm = EasyDropList(f1, options=['自动', 'AES', 'Fernet', 'RSA', 'AEAD'], default=algorithm_settings,
                                 side=tk.LEFT)

        EasyButton(f2, text="保存并退出设置", expand=tk.YES, height=2, cmd=on_settings_window_close, side=tk.LEFT)

        fade_in(settings_window, ms=4)
        settings_window.attributes('-topmost', 'true')
        settings_window.protocol("WM_DELETE_WINDOW", on_settings_window_close2)


def instructions():
    global instructions_num, instructions_window

    if instructions_num != 1:
        instructions_num += 1
        instructions_window = ctk.CTkToplevel()

        EasyAutoWindow(instructions_window, window_title="使用方法", window_width_value=600, window_height_value=400,
                       adjust_x=False, adjust_y=False)

        EasyLabel(instructions_window, text="hello", fill=tk.Y, expand=tk.YES)

        fade_in(instructions_window, ms=4)

        instructions_window.attributes('-topmost', 'true')
        instructions_window.protocol("WM_DELETE_WINDOW", on_instructions_window_close)


settings_window = None
algorithm = None
algorithm_settings = None
instructions_window = None
instructions_num = 0
settings_num = 0

window = ctk.CTk()
EasyAutoWindow(window, window_title="cryptography", minimum_value_x=640, minimum_value_y=870)

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

EasyButton(window, text="退出", fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, height=2, cmd=quit_window)

EasyButton(window, text="设置", fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, height=2, cmd=settings)

EasyButton(window, text="使用方法", fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, height=2, cmd=instructions)

fade_in(window, ms=4)
window.protocol("WM_DELETE_WINDOW", quit_window)
window.mainloop()
