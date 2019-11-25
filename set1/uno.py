import codecs
from binascii import unhexlify
from base64 import b64encode


def hex_to_b64(h: str) -> str:
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()


# https://www.reddit.com/r/learnpython/comments/2vj4o5/cryptography_bytes_vs_encoded_strings/
def hb64(h: str) -> str:
    return b64encode(unhexlify(h))


if __name__ == "__main__":
    hex = (
        '49276d206b696c6c696e6720796f757220627261696e20'
        '6c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    )
    # print(hex_to_b64(hex))
    print(hb64(hex))
