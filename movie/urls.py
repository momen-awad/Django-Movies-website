from django.urls import path
from .views import movie_list, movie_details, movie_create, movie_delete , movie_update

app_name = 'movie'

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('details/<int:id>', movie_details, name='movie_details'),
    path('create/', movie_create, name='movie_create'),
    path('delete/<int:pk>/', movie_delete, name='movie_delete'),
    path('update/<int:pk>/', movie_update, name='movie_update')

]