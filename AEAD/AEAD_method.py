import os

from comm.common import green_input, orange_print, blue_print, yellow_print, red_print
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


class AEADEncryptionMethod:
    def __init__(self, text):
        self._text = text.encode('utf-8')

    def encryption(self):
        backend = default_backend()
        key = os.urandom(32)
        nonce = os.urandom(16)
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(self._text)
        key = f"{key.hex()}+{nonce.hex()}+{str(backend)}"
        return ciphertext.hex(), key


class AEADDecryptionMethod:
    def __init__(self, text, key):
        self._text = bytes.fromhex(text)  # Convert ciphertext_input to bytes
        self._key = key

    def decryption(self):
        decompose_text = self._key.split('+')
        key = decompose_text[0]
        nonce = decompose_text[1]
        backend = decompose_text[2]
        key_bytes = bytes.fromhex(key)
        nonce_bytes = bytes.fromhex(nonce)
        cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None, backend=backend)
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(self._text)
        return decrypted_text.decode('utf-8')


if __name__ == '__main__':
    while True:
        try:
            plaintext = green_input("请输入需要加密的文字(输入q退出): ")
            if plaintext == 'q':
                orange_print("已退出")
                break
            ciphertext, key = AEADEncryptionMethod(plaintext).encryption()
            blue_print(f"密文: {ciphertext}")
            yellow_print(f"密钥: {key}")
            ciphertext_input = green_input("\n请输入需要解密的文字(输入q退出): ")
            if ciphertext_input == 'q':
                orange_print("已退出")
                break
            key_input = green_input("请输入密钥(输入q退出): ")
            if key_input == 'q':
                orange_print("已退出")
                break
            decrypted_text = AEADDecryptionMethod(ciphertext_input, key_input).decryption()
            blue_print(f"明文: {decrypted_text}\n")
        except ValueError:
            red_print("解密失败, 无效的密文或密钥\n")
