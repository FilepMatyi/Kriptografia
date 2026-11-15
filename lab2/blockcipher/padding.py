def pad(data: bytes, block_size: int, scheme: str) -> bytes:

    missing = block_size - len(data) % block_size

    if scheme == "ZERO":
        if missing == block_size:
            return data
        return data + bytes(missing)

    if scheme == "DES":
        return data + b"\x80" + bytes (missing - 1)

    if scheme == "SF":
        return data + bytes([missing]) * missing

    raise ValueError(f"Hibas kitoltes")

def unpad(data : bytes, block_size : int, scheme : str) -> bytes:
    if scheme == "ZERO":
        return data.rstrip(b"\x00")

    if scheme == "DES":
        stripped = data.rstrip(b"\x00")
        if not stripped or stripped[-1] != 0x80:
            raise ValueError("Hibas Des")
        return stripped[:-1]

    if scheme == "SF":
        n = data[-1]
        if n < 1 or n > block_size or data [-n:] != bytes([n]) * n:
            raise ValueError("Hibas Sf kitoltes")
        return data[:-n]

    raise ValueError(f"ismeretlen kitoltes")