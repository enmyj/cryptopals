
def sxor(foo: str, bar: str) -> str:
    xor = int(foo, base=16) ^ int(bar, base=16)
    return f'{xor:x}'
