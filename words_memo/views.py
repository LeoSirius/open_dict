import jwt
import uuid
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect

def home_view(request):
    return TemplateResponse(request, 'home_page.html')

def register_view(request):
    print('settings.SECRET_KEY = {}'.format(settings.SECRET_KEY))
    if request.method == 'POST':
        # login_form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('password before = {}'.format(password))
        # password = make_password(password)
        print('password = {}'.format(password))
        vid = uuid.uuid4()

        payload = {
            'vid': vid.hex,
        }
        token = jwt.encode(payload, key=settings.SECRET_KEY)
        print('token = {}'.format(token))
        activate_url = 'http://39.106.229.224/accounts/register/' + token.decode('utf-8') + '/'
        print('activate_url = {}'.format(activate_url))
        # todo send http://hostname/accounts/register/token/ to email

        # create user but not activate
        if User.objects.filter(email=email).exists():
            return HttpResponse('用户名存在')

        user = User.objects.create(username=vid, email=email)
        user.set_password(password)
        user.save()
        try:
            login(request, user)
        except Exception as e:
            print('login error E = {}'.format(e))
        return redirect('/')

    return TemplateResponse(request, 'register_page.html')

def register_confirm_view(request, token):
    try:
        # TODO: secrete key check
        payload = jwt.decode(token, key=settings.SECRET_KEY)
    except Exception as e:
        pass
    vid = payload.get('vid')

    # activate


    return redirect('/')



@login_required
def profile_view(request):
    return HttpResponse('my profile')

def login_view(request):
    if request.method == 'POST':
        print('request.POST = {}'.format(request.POST))
        # login_form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('用户名错误')


        if not user.check_password(password):
            return HttpResponse('密码错误')

        # if not check_password(password, user.get_password())


        login(request, user)
        return redirect('/')

    else:
        pass

    return TemplateResponse(request, 'login_page.html')


@login_required
def logout_view(request):
    logout(request)

    return redirect('/')
