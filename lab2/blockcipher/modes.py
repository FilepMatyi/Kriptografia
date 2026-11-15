# modes.py

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def split_blocks(data: bytes, bs: int) -> list[bytes]:
    if len(data) % bs != 0:
        raise ValueError("Az adat hossza nem többszöröse a blokkméretnek")
    return [data[i:i + bs] for i in range(0, len(data), bs)]


def ecb_encrypt(cipher, data, iv=None):
    return b"".join(cipher.encrypt_block(p) for p in split_blocks(data, cipher.block_size))

def ecb_decrypt(cipher, data, iv=None):
    return b"".join(cipher.decrypt_block(c) for c in split_blocks(data, cipher.block_size))


def cbc_encrypt(cipher, data, iv):
    result, prev = [], iv
    for p in split_blocks(data, cipher.block_size):
        c = cipher.encrypt_block(xor(p, prev)) 
        result.append(c)
        prev = c
    return b"".join(result)

def cbc_decrypt(cipher, data, iv):
    result, prev = [], iv
    for c in split_blocks(data, cipher.block_size):
        result.append(xor(cipher.decrypt_block(c), prev)) 
        prev = c
    return b"".join(result)


def cfb_encrypt(cipher, data, iv):
    result, prev = [], iv
    for p in split_blocks(data, cipher.block_size):
        c = xor(p, cipher.encrypt_block(prev))
        result.append(c)
        prev = c
    return b"".join(result)

def cfb_decrypt(cipher, data, iv):
    result, prev = [], iv
    for c in split_blocks(data, cipher.block_size):
        result.append(xor(c, cipher.encrypt_block(prev))) 
        prev = c
    return b"".join(result)


def ofb(cipher, data, iv):
    result, o = [], iv
    for block in split_blocks(data, cipher.block_size):
        o = cipher.encrypt_block(o)              
        result.append(xor(block, o))
    return b"".join(result)


def ctr(cipher, data, iv):
    bs = cipher.block_size
    counter = int.from_bytes(iv, "big")         
    result = []
    for block in split_blocks(data, bs):
        keystream = cipher.encrypt_block(counter.to_bytes(bs, "big"))
        result.append(xor(block, keystream))
        counter = (counter + 1) % (2 ** (8 * bs))   
    return b"".join(result)


MODES = {
    "ECB": (ecb_encrypt, ecb_decrypt),
    "CBC": (cbc_encrypt, cbc_decrypt),
    "CFB": (cfb_encrypt, cfb_decrypt),
    "OFB": (ofb, ofb),
    "CTR": (ctr, ctr),
}


def encrypt(cipher, data: bytes, mode: str, iv: bytes = None) -> bytes:
    _check(cipher, mode, iv)
    return MODES[mode][0](cipher, data, iv)


def decrypt(cipher, data: bytes, mode: str, iv: bytes = None) -> bytes:
    _check(cipher, mode, iv)
    return MODES[mode][1](cipher, data, iv)


def _check(cipher, mode, iv):
    if mode not in MODES:
        raise ValueError(f"Ismeretlen mód: {mode}")
    if mode != "ECB":
        if iv is None:
            raise ValueError(f"A(z) {mode} mód IV-t igényel")
        if len(iv) != cipher.block_size:
            raise ValueError("Az IV hossza meg kell egyezzen a blokkmérettel")