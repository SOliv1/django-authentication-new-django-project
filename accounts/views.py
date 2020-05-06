from django.shortcuts import render

""" return the .html file """


def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')
