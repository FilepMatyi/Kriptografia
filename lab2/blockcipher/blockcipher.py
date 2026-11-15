# blockcipher.py
import sys

import modes
from ciphers import create_cipher
from config import load_config
from padding import pad, unpad


def encrypt_bytes(data: bytes, cfg: dict) -> bytes:
    cipher = create_cipher(cfg["cipher"], cfg["key"], cfg["blocksize"])
    padded = pad(data, cfg["blocksize"], cfg["padding"])           # 1) kitöltés
    return modes.encrypt(cipher, padded, cfg["mode"], cfg["iv"])   # 2) kódolás


def decrypt_bytes(data: bytes, cfg: dict) -> bytes:
    cipher = create_cipher(cfg["cipher"], cfg["key"], cfg["blocksize"])
    padded = modes.decrypt(cipher, data, cfg["mode"], cfg["iv"])   # 1) dekódolás
    return unpad(padded, cfg["blocksize"], cfg["padding"])         # 2) kitöltés le


def encrypt_file(config_path, src, dst):
    cfg = load_config(config_path)
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(encrypt_bytes(data, cfg))


def decrypt_file(config_path, src, dst):
    cfg = load_config(config_path)
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(decrypt_bytes(data, cfg))


if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] not in ("encrypt", "decrypt"):
        print("Használat: python blockcipher.py encrypt|decrypt <config.json> <be> <ki>")
        sys.exit(1)
    action, config_path, src, dst = sys.argv[1:]
    if action == "encrypt":
        encrypt_file(config_path, src, dst)
    else:
        decrypt_file(config_path, src, dst)
    print("Kész.")