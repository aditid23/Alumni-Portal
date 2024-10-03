import csv
import json
import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import CreateUserForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import Profile


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



@login_required
def profile(request):
    return render(request, 'users/profile.html')



@login_required(login_url='login')
def notifications(request):
 return render(request,'notifications.html')



def register(request):
    # If the user is already authenticated, redirect them to login or another page
    if request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if already authenticated
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User created successfully!')
            return redirect('login')  # Redirect to the login page or any other page
        else:
            messages.error(request, 'Error creating user. Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'your_template_name.html', {'form': form})   


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


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profiles/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # Redirect to the profile page after update
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/edit_profile.html', context)


@login_required
def settings(request):
    if request.method == 'POST':
        # Check if it's the password change request
        if 'change_password' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important to keep the user logged in
                messages.success(request, 'Your password has been updated!')
                return JsonResponse({'success': True, 'message': 'Your password has been updated!'})
            else:
                return JsonResponse({'success': False, 'errors': password_form.errors})

        # Handle profile update
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('settings')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'password_form': password_form,
    }
    return render(request, 'users/settings.html', context)

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors}, status=400)


from django.http import JsonResponse
import csv
import os

def delete_post(request, index):
    if request.method == 'DELETE':
        file_path = 'path/to/your/output.csv'  # Update this path accordingly
        if not os.path.exists(file_path):
            return JsonResponse({'error': 'File not found'}, status=404)

        # Read all lines from the CSV
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            lines = list(reader)

        # Ensure the index is within the range
        if index < 0 or index >= len(lines):
            return JsonResponse({'error': 'Index out of range'}, status=400)

        # Remove the specified line
        del lines[index]

        # Write back the updated lines to the CSV
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)

        return JsonResponse({'success': 'Post deleted successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

