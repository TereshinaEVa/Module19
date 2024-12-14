from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *
from django.http import HttpResponse


def platform_menu(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform.html', context)


def games_menu(request):
    title = 'Магазин'
    games_ = Game.objects.all()
    context = {
        'title': title,
        'games_': games_,
        #'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'fourth_task/games.html', context)

def cart_str(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/cart.html', context)



users = ['Eva', 'Nik']


def sing_up_by_django(request):
    info = {}
    bayers = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if login in str(bayers):
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=login, balance=0, age=age)
                info['message'] = f'Приветствуем, {login}!'
    else:
        form = UserRegister()
        info['message'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sing_up_by_html(request):
    bayers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if login in str(bayers):
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=login, balance=0, age=age)
            info['message'] = f'Приветствуем, {login}!'
            return HttpResponse(f'Приветствуем, {login}!')
    return render(request, 'fifth_task/registration_page.html', info)
