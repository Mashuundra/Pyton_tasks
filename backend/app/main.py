def s(a: int, b: int):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError
