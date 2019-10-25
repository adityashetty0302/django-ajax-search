from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse


def home(request):
    return render(request, 'app/home.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            unhashed_pass = user.password
            user.set_password(user.password)
            user.save()
            user_authenticated = authenticate(username=user.username,
                                              password=unhashed_pass)
            login(request, user_authenticated)
            return HttpResponseRedirect(reverse('app:home'))
        else:
            print(user_form.errors)
            user_form = UserForm()
            return render(request, 'app/registration.html',
                          {'user_form': user_form})
    else:
        user_form = UserForm()
        return render(request, 'app/registration.html',
                      {'user_form': user_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:home'))


def user_login(request):
    login_error = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('app:home'))
        else:
            login_error = True
            return render(request, 'app/login.html',
                          {"login_error": login_error})
    else:
        return render(request, 'app/login.html', {"login_error": login_error})


def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'

    return JsonResponse(data)
