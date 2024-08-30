from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def newpost(request):
    return render(request, 'newpost.html')

def create(request):
    para = request.POST.get('paragraph', '')  
    return render(request, 'home.html', {'para': para})

def dashboard(request):
 return render(request,'dashboard.html')

def posts(request):
    return render(request, 'myposts.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
 return render(request,'settings.html')

def notifications(request):
 return render(request,'notifications.html')