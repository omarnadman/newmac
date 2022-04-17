from cgitb import html
from email import message
from wsgiref.util import request_uri
from django.shortcuts import render, redirect ,HttpResponseRedirect
from .models import UserPage, Link
from .forms import register, createList
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required


from django.contrib import messages

@login_required(login_url='login')
def home(request,):
    user = UserPage.objects.all()
    link = Link.objects.all()
    m = 0

    form = createList(request.POST)
    if request.method == 'POST':
        print(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            
            t = user.create(name=n)
            
        request.user.newlist.add(t)

    return render(request,'home.html',{'link':link,'form':form ,'m':m})


@login_required(login_url='login')
def create(request,pk):
    user = UserPage.objects.get(id=pk)
    link = Link.objects.all()
    
    l = request.POST.get('link')
    n = request.POST.get('name')
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get ('submit'):
            m1 = (l[0:7])
            hh = ['https:/', 'http://']
            if len(n) > 3:
                if m1 in hh :
                    user.link_set.create(links=l ,linkname=n)
                else:
                    messages.error(request, " your link must start with https:// ")
                

    return render(request, 'creat.html',{'link':link ,'user':user})


def registration(request):
    form = register()
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usern = authenticate(request,username=username,password=password)
        if usern is not None:
            login(request,usern)
            
            return HttpResponseRedirect('home')
        

    return render(request,'login.html',{})

def logoutPage(request):

    logout(request)
    
    return render(request,'login.html')


@login_required(login_url='login')
def deletelink(request,pk):
    list = UserPage.objects.get(id=pk)

    if request.method == 'POST':
        list.delete()
        return redirect('home')

    return render(request,'delete.html',{'list':list})


@login_required(login_url='login')
def deleteli(request,pk):
    link = Link.objects.get(id=pk)
    
    list = UserPage.objects.all()

    if request.method == 'POST':
        link.delete()
        return redirect('home')
    
    return render(request,'deleteli.html',{'link':link,'list':list})

def share(request, id):
    user1 = UserPage.objects.get(id=id)
    link = Link.objects.all()
    return render(request, 'share.html' , {'user':user1, 'link':link} )


def wel(request):
    return render(request, 'wel.html')