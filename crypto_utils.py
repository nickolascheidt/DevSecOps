from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
from binascii import hexlify

def encrypt_cbc(k, iv, text):
    cipher = AES.new(k, AES.MODE_CBC, iv)
    padded = pad(text.encode('utf-8'), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return hexlify(encrypted).decode('utf-8').upper()

def decrypt_cbc(k, iv, ciphertext):
    cipher = AES.new(k, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode('utf-8')

def encrypt_ctr(k, iv, text):
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher = AES.new(k, AES.MODE_CTR, counter=ctr)
    encrypted = cipher.encrypt(text.encode('utf-8'))
    return hexlify(encrypted).decode('utf-8').upper()

def decrypt_ctr(k, iv, ciphertext):
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher = AES.new(k, AES.MODE_CTR, counter=ctr)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode('utf-8')