# coding:utf-8
from django.shortcuts import render
from django.utils import timezone
from  django.http import request
from .models import Movie
# Create your views here.

def movie_list(request):
    movies = Movie.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request,
                  'base.html',
                  {
                      "movies" :movies
                  })