from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('about',views.about,name='about'),
    path('courses',views.courses,name='courses'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout')
]