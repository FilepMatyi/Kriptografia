from padding import pad, unpad

def test_peldak():
    assert pad(b"ABCDE", 8, "ZERO") == b"ABCDE\x00\x00\x00"
    assert pad(b"ABCDE", 8, "DES")  == b"ABCDE\x80\x00\x00"
    assert pad(b"ABCDE", 8, "SF")   == b"ABCDE\x03\x03\x03"

def test_teli_blokk():
    assert pad(b"ABCDEFGH", 8, "SF") == b"ABCDEFGH" + b"\x08" * 8

def test_oda_vissza():
    for scheme in ["ZERO", "DES", "SF"]:
        for hossz in range(0, 20):
            adat = b"X" * hossz
            assert unpad(pad(adat, 8, scheme), 8, scheme) == adat