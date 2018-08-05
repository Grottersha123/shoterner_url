from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import AnimeUrl


# Create your views here.


def anime_redirect_view(request, shortcode=None, *args, **kwargs):
    print(shortcode)
    obj = get_object_or_404(AnimeUrl, short_code=shortcode)
    return HttpResponse("this is {}".format(obj.url))


def AnimeCBViews(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(AnimeUrl, short_code=shortcode)
        return HttpResponse("this is {}".format(obj.url))
    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()