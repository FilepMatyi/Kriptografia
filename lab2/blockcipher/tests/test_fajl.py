from pathlib import Path

import pytest

from config import parse_config
from blockcipher import encrypt_bytes, decrypt_bytes

KEP = Path(__file__).parent / "test.jpg"

KULCSOK = {
    "AES-128": "MDEyMzQ1Njc4OWFiY2RlZg==",     # 16 bájt
    "VIGENERE-BIN": "a3VsY3M=",                # "kulcs"
}
IV = "AAECAwQFBgcICQoLDA0ODw=="                # 16 bájt


@pytest.mark.parametrize("cipher", ["AES-128", "VIGENERE-BIN"])
@pytest.mark.parametrize("mode", ["ECB", "CBC", "CFB", "OFB", "CTR"])
def test_fajl_oda_vissza(cipher, mode):
    adat = KEP.read_bytes()
    assert len(adat) >= 1024 * 1024            # legalább 1 MB

    json_config = {
        "blocksize": 16,
        "cipher": cipher,
        "key": KULCSOK[cipher],
        "mode": mode,
        "padding": "SF",
    }
    if mode != "ECB":
        json_config["iv"] = IV
    cfg = parse_config(json_config)

    titkos = encrypt_bytes(adat, cfg)
    assert titkos != adat                         # tényleg megváltozott
    assert decrypt_bytes(titkos, cfg) == adat     # bájtra visszajött