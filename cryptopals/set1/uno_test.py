from .uno import hex_to_b64


def test_hex_to_b64():
    input = (
        "49276d206b696c6c696e6720796f757220627261696e20"
        "6c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    )
    output = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert hex_to_b64(input) == output
