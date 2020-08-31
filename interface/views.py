from django.shortcuts import render


def show_homepage(request):
    if request.method == "GET":
        return render(request, "index.html")
