from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

# Create your views here.

def comment(request):

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for your TIME...      PAMOJA TUKOMESHE CORONA')
            return redirect('world')

        else:
            return redirect('comment')

    context = {'form':form}


    return render(request,'user/comment.html',context)

def world(request):
    return render(request,'continents/world.html')

def n_america(request):
    return render(request,'continents/n_america.html')

def s_america(request):
    return render(request,'continents/s_america.html')

def asia(request):
    return render(request,'continents/asia.html')

def europe(request):
    return render(request,'continents/europe.html')

def africa(request):
    return render(request,'continents/africa.html')

def oceania(request):
    return render(request,'continents/oceania.html')
