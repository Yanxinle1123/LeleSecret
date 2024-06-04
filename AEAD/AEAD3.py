import os

from comm.common import green_input, orange_print, blue_print, yellow_print, red_print
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

backend = default_backend()


def encrypt(plaintext, key, nonce):
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return ciphertext


def decrypt(ciphertext, key, nonce):
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=backend)
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext)
    return decrypted_text


while True:
    try:
        key = os.urandom(32)
        nonce = os.urandom(16)
        plaintext = green_input("请输入需要加密的文字(输入q退出): ")
        if plaintext == 'q':
            orange_print("已退出")
            break
        ciphertext = encrypt(plaintext.encode('utf-8'), key, nonce)
        yellow_print(f"密文: {ciphertext.hex()}")
        blue_print(f"密钥: {key.hex()}")
        ciphertext_input = green_input("\n请输入需要解密的文字(输入q退出): ")
        if ciphertext_input == 'q':
            orange_print("已退出")
            break
        key_input = green_input("请输入密钥(输入q退出): ")
        if key_input == 'q':
            orange_print("已退出")
            break
        ciphertext_bytes = bytes.fromhex(ciphertext_input)
        key_bytes = bytes.fromhex(key_input)
        decrypted_text = decrypt(ciphertext_bytes, key_bytes, nonce)
        yellow_print(f"明文: {decrypted_text.decode('utf-8')}\n")
    except ValueError:
        red_print("解密失败, 无效的密文或密钥\n")
