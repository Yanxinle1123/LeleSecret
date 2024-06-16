import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 生成一个密钥
key = os.urandom(32)

# 创建一个加密对象
cipher = Cipher(algorithms.Blowfish(key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()

# 加密数据（注意：Blowfish需要8字节的倍数）
plaintext = b"Hello, world!123"
padder = padding.PKCS7(64).padder()
padded_data = padder.update(plaintext) + padder.finalize()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("密文:", ciphertext)

# 解密数据
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(64).unpadder()
decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

print("明文:", decrypted)
