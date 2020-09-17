from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth import login,logout

# Create your views here.
def Sup(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form=UserCreationForm()
	return render(request,"accounts/signup.html",{'form':form})

def Lin(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect('home')
	else:
		form=AuthenticationForm()		
	return render(request,"accounts/login.html",{'form':form})

def Lout(request):
	logout(request)
	return redirect('home')