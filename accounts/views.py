from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('movie:movie_list')

    return render(request, 'registration/signup.html', context={'form':form})