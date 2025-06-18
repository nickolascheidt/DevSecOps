from flask import Flask, render_template, request, jsonify
from crypto_utils import encrypt_cbc, decrypt_cbc, encrypt_ctr, decrypt_ctr
from binascii import unhexlify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    key_hex = data.get("key")
    iv_hex = data.get("iv")
    text = data["text"]
    mode = data["mode"]

    if key_hex:
        key = unhexlify(key_hex)
    else:
        key = os.urandom(16)

    if iv_hex:
        iv = unhexlify(iv_hex)
    else:
        iv = os.urandom(16)

    if mode == "cbc":
        result = encrypt_cbc(key, iv, text)
    elif mode == "ctr":
        result = encrypt_ctr(key, iv, text)
    else:
        return jsonify({"error": "Invalid mode"}), 400

    return jsonify({
        "ciphertext": result,
        "key": key.hex().upper(),
        "iv": iv.hex().upper()
    })

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    key = unhexlify(data["key"])
    iv = unhexlify(data["iv"])
    ciphertext = unhexlify(data["ciphertext"])
    mode = data["mode"]

    if mode == "cbc":
        result = decrypt_cbc(key, iv, ciphertext)
    elif mode == "ctr":
        result = decrypt_ctr(key, iv, ciphertext)
    else:
        return jsonify({"error": "Invalid mode"}), 400

    return jsonify({"plaintext": result})

if __name__ == "__main__":
    app.run(debug=True) #trigger for ci/cd 4