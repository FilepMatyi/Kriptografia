# config.py
import base64
import binascii
import json
from pathlib import Path

import jsonschema

SCHEMA_PATH = Path(__file__).parent / "cipher-config.schema.json"
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def decode_b64(value: str, field: str) -> bytes:
    try:
        return base64.b64decode(value, validate=True)
    except binascii.Error:
        raise ValueError(f"A(z) '{field}' mező nem érvényes base64")


def parse_config(cfg: dict) -> dict:
    jsonschema.validate(instance=cfg, schema=SCHEMA)

    key = decode_b64(cfg["key"], "key")
    if len(key) == 0:
        raise ValueError("A kulcs nem lehet üres")

    iv = None
    if cfg["mode"] != "ECB":
        if "iv" not in cfg:
            raise ValueError(f"A(z) {cfg['mode']} mód IV-t igényel")
        iv = decode_b64(cfg["iv"], "iv")
        if len(iv) != cfg["blocksize"]:
            raise ValueError("Az IV hossza meg kell egyezzen a blokkmérettel")

    return {
        "blocksize": cfg["blocksize"],
        "cipher": cfg["cipher"],
        "key": key,          
        "mode": cfg["mode"],
        "iv": iv,            
        "padding": cfg["padding"],
    }


def load_config(path) -> dict:
    """JSON fájl beolvasása és ellenőrzése."""
    with open(path, encoding="utf-8") as f:
        return parse_config(json.load(f))