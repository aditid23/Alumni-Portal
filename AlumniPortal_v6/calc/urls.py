from django.urls import path
from . import views
urlpatterns=[
path('', views.home, name='home'),
path('create/',views.create, name='create'),
path('newpost/', views.newpost, name='newpost'),
path('dashboard/',views.dashboard, name='dashboard'),
path('posts/', views.posts, name='posts'),
path('profile/',views.profile, name='profile'),
path('settings/',views.settings, name='settings'),
path('notifications/',views.notifications, name='notifications'),
path('register/',views.registerPage, name='register'),
path('login/',views.loginPage, name='login'),
path('logout/',views.logoutPage, name='logout'),
path('profile/edit/', views.edit_profile, name='edit_profile'),
]