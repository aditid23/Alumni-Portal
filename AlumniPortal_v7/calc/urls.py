from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from calc import views as calc_view

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

path('edit_profile/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)