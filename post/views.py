from django.shortcuts import render,redirect
# Create your views here.
from .models import Post

from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def addpost(request):
	if request.method=='POST':
		a=Post()
		a.doc=request.FILES['doc']
		
		a.caption=request.POST['cap']
		
		a.save()
		return redirect('alp')
	else:
		return render(request,"post/addpost.html")

def allpost(request):
	al=Post.objects.all()
	return render(request,"post/allpost.html",{'data1':al})	

def updatepost1(request,pk1):
	al=Post.objects.get(id=pk1)
	return render(request,"post/updatepost.html",{'data1':al})	

def updatepost2(request,pk1):
	if request.method=='POST':
		a=Post.objects.get(id=pk1)
		a.doc=request.FILES['doc']
		a.caption=request.POST['cap']
		a.save()
	return redirect('alp')

	
def delconf(request,pk1):
	al=Post.objects.get(id=pk1)
	return render(request,"post/delconf.html",{'data1':al})

def deletepost(request,pk1):
	al=Post.objects.get(id=pk1)
	al.delete()	
	return redirect('alp')


