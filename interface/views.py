from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from zipper.constants import PROTOCOL_SECURE
from zipper.models import UrlMapper


def show_homepage(request):
    """
    Returns html of homepage
    """
    if request.method == "GET":
        return render(request, "homepage.html")


def resolve_and_redirect(request, hashed_url):
    """
    Passed in minified_url is looked up in db. If found, user is redirected to corresponding url.
    If not found, User is shown an error message
    """
    try:
        instance = get_object_or_404(UrlMapper, hashcode=hashed_url)
        instance.clicks = instance.clicks + 1
        instance.save()
    except Http404:
        return HttpResponse("<h2>Url does not exist</h2>")

    return HttpResponseRedirect("{}{}".format(PROTOCOL_SECURE, instance.url))  # prefixing https
