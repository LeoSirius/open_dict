from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import redirect



def home_view(request):
    return TemplateResponse(request, 'home_page.html')


@login_required
def profile_view(request):
    return HttpResponse('my profile')


def login_view(request):
    if request.method == 'POST':
        print('request.POST = {}'.format(request.POST))
        # login_form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')


        user = authenticate(username=email, password=password)
        print('user = {}'.format(user))
        if not user:
            return HttpResponse('err not user')

        login(request, user)
        return redirect('/')

    else:
        # login_form = LoginForm()
        pass

    return TemplateResponse(request, 'login_page.html')

@login_required
def logout_view(request):
    logout(request)

    return redirect('/')
