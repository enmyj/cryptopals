from binascii import unhexlify
from base64 import b64encode


def hex_to_b64(h: str) -> bytes:
    return b64encode(bytes.fromhex(h))


# https://www.reddit.com/r/learnpython/comments/2vj4o5/cryptography_bytes_vs_encoded_strings/
def hb64(h: str) -> str:
    return b64encode(unhexlify(h))
