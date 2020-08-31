import hashlib
import re

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.forms import URLField
from django.http import JsonResponse

from zipper.constants import BASE62_DIGITS, URL_SYNTAX_REGEX, URL_PATH_REGEX

# Creating custom error codes to determine type of error in front end
# 11 -  Url input missing
# 12 - Url Syntax error
def input_validation(func):
    def inner(request):
        url = request.GET.get('url') or request.POST.get('url')
        if not url:
            return JsonResponse({"error": True, "value": 11, "msg": "No url sent"})

        # verifying syntax of url
        try:
            url_field = URLField()
            url = url_field.clean(url)
            url = re.match(URL_PATH_REGEX, url).group(2)  # extracting the domain and directory name
        except ValidationError as e:
            print(e)
            return JsonResponse({"error": True, "value": 12, "msg": "Invalid syntax"})

        return func(request, url)

    return inner


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
