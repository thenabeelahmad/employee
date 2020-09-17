from django.http import HttpResponse
from django.shortcuts import render

def home(requests):
	return render(requests,"home.html")

def about(requests):
	return render(requests,"about.html")	

def service(requests):
	return render(requests,"service.html")	

def contact(requests):
	return render(requests,"contact.html")	 

