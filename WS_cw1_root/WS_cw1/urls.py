"""WS_cw1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ratings.views import register_user
from ratings.views import logging_in
from ratings.views import logging_out
from ratings.views import list_modules
from ratings.views import view_ratings
from ratings.views import average_ratings
from ratings.views import rate_professor
from ratings import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user),
    path('login/', logging_in),
    path('logout/', logging_out),
    path('list/', list_modules),
    path('view/', view_ratings),
    path('average/', average_ratings),
    path('rate/', rate_professor),
]
