from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse


def main(request):
    return HttpResponse("<h1>Welcome to valhalla's API, please visit /api/</h1>")


urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
