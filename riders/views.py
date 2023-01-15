from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def riders(request):
    return HttpResponse("This is riders")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you are now logged in.')
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render (request, 'riders/register.html', {'form':form})


@login_required
def profilepage(request):
    return render(request, 'riders/profile.html')