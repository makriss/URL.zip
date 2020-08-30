from django.shortcuts import render

# Create your views here.
from zipper.constants import BASE62_DIGITS


def minify_url(request, url):

    #validate url syntax




    pass


def encode_to_base_62(url):
    base62_digits = []
    hash_code = abs(hash(url))
    base = len(BASE62_DIGITS)
    while hash_code > 0:
        rem = hash_code % base
        base62_digits.append(BASE62_DIGITS[rem])
        hash_code = hash_code // base

    return "".join(base62_digits[::-1])
