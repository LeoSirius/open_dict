from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse

def home_view(request):
    return HttpResponse('home view')

@login_required
def profile_view(request):
    return HttpResponse('my profile')