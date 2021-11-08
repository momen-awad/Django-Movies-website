from django.shortcuts import render , redirect
from .models import Movie
from .forms import MovieForm
from django.core.mail import send_mail

# Create your views here.

def movie_list(request):
    movie_list = Movie.objects.all()
    return render(request, 'movie/movie_index.html', context={'movies': movie_list})


def movie_details(request, id):
    movie_details = Movie.objects.get(id=id)
    return render(request, 'movie/movie_details.html', context={'details': movie_details})


def movie_create(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            send_mail(subject='New movie created',
                      message= 'dear user a new movie {} is created '.format(request.POST.get('name')),
                      from_email='awadmomen@gmail.com',
                      recipient_list=['awadmomen@gmail.com'],
                      fail_silently=False
                      )
            form.save()
            return redirect('movie:movie_list')

    return render(request, 'movie/movie_create.html', context={'form': form})


def movie_update(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:movie_details', id=movie.id)

    return render(request, 'movie/movie_update.html', context={'form': form, 'movie': movie})



def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:movie_list')

def movie_edit(request,pk):
    return redirect('movie:movie_details', id=pk)


