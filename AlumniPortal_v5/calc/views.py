import csv
import json
import os
from django.shortcuts import render, redirect

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


def newpost(request):
    return render(request, 'newpost.html')


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




def dashboard(request):
 return render(request,'dashboard.html')

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

def settings(request):
 return render(request,'settings.html')

def notifications(request):
 return render(request,'notifications.html')



