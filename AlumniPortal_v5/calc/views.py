import csv
import json
import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    data = []
    file_path = os.path.join('calc', 'data', 'output.csv')  

    print(f"Trying to open: {file_path}")  

    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                cleaned_row = [item.replace(',', '') for item in row]  
                data.append(' '.join(cleaned_row))

    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}") 

    data.reverse()
    return render(request, 'home.html', {'para': json.dumps(data)})

@login_required(login_url='login')
def newpost(request):
    return render(request, 'newpost.html')

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        para = request.POST.get('paragraph', '')
        if para:
            file_path = os.path.join('calc', 'data', 'output.csv') 
            try:
                with open(file_path, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([para])  

            except Exception as e:
                print(f"An error occurred while writing to CSV: {e}")  

    return redirect('home')  



@login_required(login_url='login')
def dashboard(request):
 return render(request,'dashboard.html')

@login_required(login_url='login')
def posts(request):
    data = []
    file_path = os.path.join('calc', 'data', 'output.csv')  

    print(f"Trying to open: {file_path}")  

    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                cleaned_row = [item.replace(',', '') for item in row]  
                data.append(' '.join(cleaned_row))

    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")  
    data.reverse()
    return render(request, 'myposts.html', {'para': json.dumps(data)})


@login_required(login_url='login')
def profile(request):
    data = []
    file_path = os.path.join('calc', 'data', 'output.csv')  

    print(f"Trying to open: {file_path}")  

    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                cleaned_row = [item.replace(',', '') for item in row]  
                data.append(' '.join(cleaned_row))

    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")  
    data.reverse()
    return render(request, 'profile.html', {'para': json.dumps(data)})


@login_required(login_url='login')
def settings(request):
 return render(request,'settings.html')


@login_required(login_url='login')
def notifications(request):
 return render(request,'notifications.html')


def registerPage(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.success(request,"Password does not follow the rules")
    context={'form':form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request,"Username or Password is incorrect")
    context={}
    return render(request,'login.html',context)

@login_required(login_url='login')
def logoutPage(request):
 logout(request)
 return redirect('login')