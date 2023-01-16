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

# login_required() does the following: - If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Example: /accounts/login/?next=/polls/3/. If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.
@login_required
def profilepage(request):
    return render(request, 'riders/profile.html')