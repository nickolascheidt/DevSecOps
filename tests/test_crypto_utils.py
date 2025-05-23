from crypto_utils import encrypt_cbc, decrypt_cbc
from binascii import unhexlify
import os

def test_cbc_encryption_decryption():
    key = os.urandom(16)
    iv = os.urandom(16)
    text = "mensagem secreta"

    encrypted = encrypt_cbc(key, iv, text)
    decrypted = decrypt_cbc(key, iv, unhexlify(encrypted))
    assert decrypted == text