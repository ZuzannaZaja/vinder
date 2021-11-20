from django.urls import path
from . import views

urlpatterns = [
    path("test",views.first,name= "First_strona_glowna"),
    path("get_all_sessions",views.CustomView.as_view()),
    path("user_sessions/<str:username>",views.Filters.as_view()),
    path("load_movies",views.LoadMovies.as_view()),
    path("show_movies",views.AllMovies.as_view()),
]