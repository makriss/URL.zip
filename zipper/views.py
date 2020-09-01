import re

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from zipper.constants import URL_SYNTAX_REGEX
from zipper.models import UrlMapper
import zipper.utility_functions as uf


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

    return uf.parseUrl(mapper_instance)


@uf.input_validation
def get_shortening_count(request, url):
    instance = UrlMapper.objects.get(url=url)
    return JsonResponse({'url': url, 'count': instance.url_shorten_count, 'minified_url': instance.hashcode})