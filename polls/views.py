from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> hallo </h1>")


def meme(request):
    return HttpResponse('<img src="https://n1s1.hsmedia.ru/c8/9f/cb/c89fcb31dd077084bc8bbc2284586b7f/1000x600_0xac120003_16946826431608901545.jpg">')