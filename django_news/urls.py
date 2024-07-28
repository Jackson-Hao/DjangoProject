"""
URL configuration for django_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import hmos.views

urlpatterns = [
    path('login_verify/',hmos.views.login_verify),
    # path('animals/', get_animals),
    path('regster/', hmos.views.regster),
    # path('led_status/', hmos.views.led_status),
    path('book_verify/', hmos.views.book_verify),
    # path('book_borrow/', hmos.views.book_borrow),
    # path('book_return/', hmos.views.book_return),
    # path('book_check/', hmos.views.book_check),
    path('book_creat/', hmos.views.book_creat),
    path('user_search/', hmos.views.user_search),
    path('led_control/',hmos.views.led_control),
    path('checkNetwork/',hmos.views.checkNetwork),
    path("alarm/",hmos.views.alarm),
]
