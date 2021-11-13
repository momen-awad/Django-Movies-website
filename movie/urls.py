from django.urls import path
from .views import movie_list, movie_details, movie_create, movie_delete , movie_update
from .api import movie_data, create_movie ,movie_detail, movie_deleted, movie_updated

app_name = 'movie'

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('details/<int:id>', movie_details, name='movie_details'),
    path('create/', movie_create, name='movie_create'),
    path('delete/<int:pk>/', movie_delete, name='movie_delete'),
    path('update/<int:pk>/', movie_update, name='movie_update'),
    path('api/list', movie_data, name="movie_data"),
    path('api/list/create', create_movie, name="movie_create"),
    path('api/list/<int:id>', movie_detail, name="movie_create"),
    path('api/list/delete/<int:id>', movie_deleted, name="movie_deleted"),
    path('api/list/update/<int:id>', movie_updated, name="movie_updated"),

    #class based views
    #path('api/v2/list',MovieList.as_view(),name="movie_list_api_v2"),
    #path('api/v2/list/<int:id>', MovieDetails.as_view(), name="movie_Details_api_v2")

]