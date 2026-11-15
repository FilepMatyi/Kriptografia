from Crypto.Cipher import AES


class VigenereBin:

    def __init__(self, key: bytes, block_size: int):
        if len(key) == 0:
            raise ValueError("A kulcs nem lehet üres")
        self.key = key
        self.block_size = block_size

    def encrypt_block(self, block: bytes) -> bytes:
        result = []
        for i in range(len(block)):
            k = self.key[i % len(self.key)]          
            result.append((block[i] + k) % 256)
        return bytes(result)

    def decrypt_block(self, block: bytes) -> bytes:
        result = []
        for i in range(len(block)):
            k = self.key[i % len(self.key)]
            result.append((block[i] - k) % 256)
        return bytes(result)


class AESCipher:

    def __init__(self, key: bytes, block_size: int):
        if block_size != 16:
            raise ValueError("AES-nél a blokkméret mindig 16 bájt")
        if len(key) not in (16, 24, 32):
            raise ValueError("AES kulcs: 16, 24 vagy 32 bájt")
        self.block_size = block_size
        self.aes = AES.new(key, AES.MODE_ECB)    

    def encrypt_block(self, block: bytes) -> bytes:
        return self.aes.encrypt(block)

    def decrypt_block(self, block: bytes) -> bytes:
        return self.aes.decrypt(block)


def create_cipher(name: str, key: bytes, block_size: int):
    if name == "VIGENERE-BIN":
        return VigenereBin(key, block_size)
    if name in ("AES-128", "AES-192", "AES-256"):
        expected = {"AES-128": 16, "AES-192": 24, "AES-256": 32}[name]
        if len(key) != expected:
            raise ValueError(f"{name}: a kulcs {expected} bájt kell legyen")
        return AESCipher(key, block_size)
    raise ValueError(f"Ismeretlen algoritmus: {name}")