from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from calc import views as calc_view
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns=[
path('', views.home, name='home'),
path('create/',views.create, name='create'),
path('newpost/', views.newpost, name='newpost'),
path('dashboard/',views.dashboard, name='dashboard'),
path('posts/', views.posts, name='posts'),
path('profile/',views.profile, name='profile'),
path('notifications/',views.notifications, name='notifications'),
path('login/',views.loginPage, name='login'),
path('logout/',views.logoutPage, name='logout'),
path('edit_profile/', views.edit_profile, name='edit_profile'),
path('settings/',views.settings, name='settings'),
path('register/', views.register, name='register'),
path('login/', auth_views.LoginView.as_view(), name='login'), 
path('change_password/', views.change_password, name = 'change_password'),
path('delete_post/<int:index>/', views.delete_post, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)