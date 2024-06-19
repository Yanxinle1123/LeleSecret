import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def camellia_encrypt(plaintext, key):
    cipher = Cipher(algorithms.Camellia(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return ciphertext


def camellia_decrypt(ciphertext, key):
    cipher = Cipher(algorithms.Camellia(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext)
    return plaintext


# 生成一个16字节的随机密钥
key = os.urandom(16)

# 输入需要加密的文本，确保其长度为16的倍数
plaintext = b"Hello, World!123"

# 使用Camellia加密
ciphertext = camellia_encrypt(plaintext, key)
print("密文:", ciphertext.hex())
print("密钥:", key.hex())

# 使用Camellia解密
decrypted_text = camellia_decrypt(ciphertext, key)
print("明文:", decrypted_text.decode('utf-8'))
