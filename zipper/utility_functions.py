import hashlib

from zipper.constants import BASE62_DIGITS


def encode_to_base_62(url):
    """
    Converts url to a hashcode (base 62)
    """

    hash_string = inbuilt_encoder(url)
    base62_digits = []
    hash_code = int(hash_string, 16)  # url is converted to a numeric hashcode using built in hash function
    base = len(BASE62_DIGITS)

    # numeric hashcode create above is further converted to a base 62 numeric system
    while hash_code > 0:
        rem = hash_code % base
        base62_digits.append(BASE62_DIGITS[rem])
        hash_code = hash_code // base

    return "".join(base62_digits[::-1])


def inbuilt_encoder(url):
    """
    Inbuilt hashing function. However it returns a different hashcode for same url input.
    """
    h = hashlib.blake2b(digest_size=5)
    h.update(url.encode())
    return h.hexdigest()