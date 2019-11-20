from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
from .forms import loginform
from .forms import regform

def home(request):
    return render(request,'home.html')
def reg(request):
    if request.method=='POST':
        form=regform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('registration successful')
    else:
        form=regform()
        return render(request,'reg.html',{'form':form})
def login(request):
    if request.method=='POST':
        myloginform=loginform(request.POST)
        if myloginform.is_valid():
            un=myloginform.cleaned_data['user']
            pw=myloginform.cleaned_data['pwd']
            dbuser=Reg.objects.filter(user=un,pwd=pw)
            if not dbuser:
                return HttpResponse('login Failed')
            else:
                return HttpResponse('login success')
    else:
        form=loginform()
        return render(request,'login.html',{'form':form})


