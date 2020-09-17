from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Information
from django.contrib.auth.decorators import login_required
from django.db import connection


def cremp(request):
	return render(request,'information/cremp.html')

def cremp2(request):
	if request.method=="POST":
		a=Information()
		a.Iname=request.POST['name']
		a.Imob=request.POST['mob']
		a.Imail=request.POST['email']
		a.Iadhar=request.POST['adhar']
		a.Isalary=request.POST['salary']
		a.save()
		return redirect('list')
	return render(request,"information/cremp.html")		

@login_required(login_url="/accounts/login/")
def listemp(request):
	pass
	# a=Information.objects.all()
 #    return render(request,"information/listemp.html",{'data':a})	
    
	

def confdel(request,pk):
	a=Information.objects.get(id=pk)
	return render(request,"information/confdel.html",{'data':a})

def delete(request,pk):
	a=Information.objects.get(id=pk)
	a.delete()	
	return redirect('list')

def update(request,pk):
	a=Information.objects.get(id=pk)
	return render(request,"information/updateemp.html",{'data':a})	

def update2(request,pk):
	if request.method=="POST":
		a=Information.objects.get(id=pk)
		a.Iname=request.POST['name']
		a.Imob=request.POST['mob']
		a.Imail=request.POST['email']
		a.Iadhar=request.POST['adhar']
		a.Isalary=request.POST['salary']
		a.save()
	return redirect('list')
		

