import jwt
import uuid
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from words_memo.utils import send_emails

def home_view(request):
    return TemplateResponse(request, 'home_page.html')

def register_view(request):
    print('settings.SECRET_KEY = {}'.format(settings.SECRET_KEY))
    if request.method == 'POST':
        # login_form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            return HttpResponse('用户名存在')

        vid = uuid.uuid4()
        payload = {
            'vid': vid.hex,
            'email': email,
            'elp': password,
        }
        token = jwt.encode(payload, key=settings.SECRET_KEY, algorithm='HS256')
        print('token = {}'.format(token))
        activate_url = 'http://39.106.229.224/accounts/register/' + token.decode('utf-8') + '/'
        print('activate_url = {}'.format(activate_url))
        # todo send http://hostname/accounts/register/token/ to email
        send_emails([email])

        # TODO tips check email

        return HttpResponse('验证链接已发送，请检查邮件')

    return TemplateResponse(request, 'register_page.html')

def register_confirm_view(request, token):
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithm='HS256')
    except jwt.PyJWTError:
        return HttpResponse('token invalid.')

    vid = payload.get('vid')
    email = payload.get('email')
    password = payload.get('elp')
    if (not vid) or (not email) or (not password):
        return HttpResponse('token invalid.')
    # create user but not activate
    user = User.objects.create(username=vid, email=email)
    user.set_password(password)
    user.save()
    try:
        login(request, user)
    except Exception as e:
        print('login error E = {}'.format(e))
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
