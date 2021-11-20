from typing import Reversible
from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import View
from .models import VinderSession
from .models import Movie
from django.db.models import Q
from django.contrib import messages
import logging
import csv
import json
# Create your views here.


def first(request):
    return HttpResponse("Pierwszy response HTTP Zuzia")


class CustomView(View):
    def get(self, request):
        all_vinder_session = VinderSession.objects.all()
        sessions_data_list=[]
        for session in all_vinder_session:
            current_session = {
                "Initializing_user": session.init_user.username,
                "Other_user": session.other_user.username,
                "init_user_choice": session.choices1,
                "other_user_choice": session.choices2,

            }
            sessions_data_list.append(current_session)
        response_data = {"sessions": sessions_data_list}
        return JsonResponse(response_data)

class Filters(View):
    def get(self, request, **kwargs):
        print(kwargs)
        username = kwargs["username"]
        user_sessions = VinderSession.objects.filter(Q(init_user__username = username) | Q(other_user__username = username)) 
        sessions_data_list=[]
        for session in user_sessions:
            current_session = {
                "Initializing_user": session.init_user.username,
                "Other_user": session.other_user.username,
                "init_user_choice": session.choices1,
                "other_user_choice": session.choices2,

            }
            sessions_data_list.append(current_session)
        response_data = {"sessions": sessions_data_list}
        return JsonResponse(response_data)

class LoadMovies(View):
    def get(self, request):

        with open('imdb_top_1000.csv', encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
         
            for rows in csvReader:
                movie =  Movie()

                movie.poster = rows['Poster_Link']
                movie.title = rows['Series_Title']
                movie.release_year = rows['Released_Year']
                movie.duration = rows['Runtime']
                movie.genre = rows['Genre']
                movie.director = rows['Director']
                movie.description = rows['Overview']
                movie.IMDB_Rating =rows['IMDB_Rating']
                movie.cast = [rows['Star1'], rows['Star2'], rows['Star3'], rows['Star4']]
                

                movie.save()

        return HttpResponse("Movies database loaded successfully")


class AllMovies(View):
    def get(self, request):
         
                
        return render(request, "vinder_rest_api/movies.html", { "movies": Movie.objects.all})          
 
