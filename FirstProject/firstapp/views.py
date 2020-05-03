from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.	
def hai(request):
	return HttpResponse("Welcome to raja's")
def hello(request,name):
	return HttpResponse("<h1>Welcome to GKRaja's<br> maha<br>MAHA</h1>")
def raja(request,name):
	return HttpResponse("<h1>Welcome to "+name)
def rolnum(request,id):
	text = "welcome your id {}".format(id)
	return HttpResponse(text)
def msg(request):
	return render(request,'firstapp/msg.html',{})
def register(request):
	if request.method == "POST":
		name = request.POST['uname']
		mobileno = request.POST['mbno']
		email = request.POST['email']
		data = {'name':name,'phoneno':mobileno,'email':email}
		#return HttpResponse("Done")
		return render (request,'firstapp/details.html',{'udata':data})
	return render(request,'firstapp/register.html',{})
def details(request):
	
	data = {'name':"Raja",'rollno':527}
	return render(request,'firstapp/details.html',{'data':data})