import string

BASE62_CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62_CHARS[0]
    
    result = []
    while num > 0:
        remainder = num % 62
        result.append(BASE62_CHARS[remainder])
        num //= 62
    return "".join(reversed(result))