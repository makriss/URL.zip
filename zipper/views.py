import re

from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

import zipper.utility_functions as uf
# Create your views here.
from zipper.constants import MINIFIED_URL_REGEX
from zipper.models import UrlMapper


@uf.input_validation
def minify_url(request, url):
    # url is first checked will in db. If present, retireve the existing hashcode.
    # If not, then generate a new hashcode
    try:
        # check if url exists in db
        mapper_instance = get_object_or_404(UrlMapper, url=url)
        # hashcode already exists in db, meaning url has been hashed earlier. In this case,
        # increment the url shortening count by one, and return the hashcode
        mapper_instance.increment_url_shorten_count()

    except Http404 as e:
        # url does not exist in db
        print("Hashcode exists for given url:", e)
        # Generating a hash code for the url
        hashed_url = uf.encode_to_base_62(url)
        # hashcode, along with original url, is saved to db
        mapper_instance = UrlMapper.save_hashcode(hashed_url, url)

    return JsonResponse(uf.parseUrl(mapper_instance))


@uf.input_validation
def get_shortening_count(request, url):
    match = re.search(MINIFIED_URL_REGEX, url)
    if match:
        return JsonResponse({"error": True, "value": 'invalid', "msg": "Please enter a valid url"})

    try:
        instance = UrlMapper.objects.get(url=url)
    except UrlMapper.DoesNotExist:
        return JsonResponse({"error": True, "value": 'invalid', "msg": "Url has not been minified yet"})

    return_object = uf.parseUrl(instance)
    return_object.update({'count': instance.url_shorten_count})
    return JsonResponse(return_object)


@uf.input_validation
def get_total_clicks(request, minified_url):
    match = re.search(MINIFIED_URL_REGEX, minified_url)
    if not match:
        return JsonResponse({"error": True, "value": 'invalid', "msg": "Please enter a valid minified url"})

    try:
        instance = UrlMapper.objects.get(hashcode=match.group(1))
    except UrlMapper.DoesNotExist:
        return JsonResponse({"error": True, "value": 'invalid', "msg": "Url does not exist"})

    return_object = uf.parseUrl(instance)
    return_object.update({'clicks': instance.clicks})
    return JsonResponse(return_object)
