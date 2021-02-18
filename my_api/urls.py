from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse, JsonResponse

def welcome(request):
    return HttpResponse("Welcome!")

urlpatterns = [
    path('', welcome, name="welcome"),
    path('api/', include('my_api.polls.api.urls')),
    path('admin/', admin.site.urls),
]
