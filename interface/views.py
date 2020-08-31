from django.shortcuts import render


def show_homepage(request):
    if request.method == "GET":
        return render(request, "homepage.html")
