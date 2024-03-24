from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import sklearn
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import numpy as np
import joblib
from . import forms

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False
import time
from  joblib import load


generation_model = joblib.load('G:/2023-2024/PROJECTS FOR 2023-2024/MACHINE LEARNING/ITPML01 - RENEWABLE/Deploy/project/app/Generation2.pkl')
speed_model = joblib.load('G:/2023-2024/PROJECTS FOR 2023-2024/MACHINE LEARNING/ITPML01 - RENEWABLE/Deploy/project/app/windspeed2.pkl')

generation = generation_model
speed = speed_model


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def landingpage(request):
    return render(request, 'landingpage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def herimorrhagic(request):
    return render(request, 'Hermorrhagic_stroke.html')

def ishemic_cancer(request):
    return render(request, 'ishemic_Cancer.html')

def tia(request):
    return render(request, 'TIA.html')


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register1.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'registration/login1.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')


# def generation_model(request):
#     if request.method == "POST":
#         int_features = [x for x in request.POST.values()]
#         int_features = int_features[1:]
#         print(int_features)
#         final_features = [np.array(int_features).astype(float)]
#         print(final_features)
#         prediction = generation_model.predict(final_features)
#         print(prediction)
#         output = prediction[0]
#         print(output)
#         return render(request, 'generation_model.html', {'prediction_text': f'{output}'})

  
def generation_model(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=float)]
        print(final_features)
        prediction = generation.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)

        return render(request, 'gen_output.html', {"prediction_text": output})
    else:
        return render(request, 'generation_model.html')
    
def speed_model(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=float)]
        print(final_features)
        prediction = speed.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)

        return render(request, 'speed_output.html', {"prediction_text":output})
    else:
        return render(request, 'speed_model.html')




