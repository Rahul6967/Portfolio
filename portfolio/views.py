from django.shortcuts import render

# Create your views here.
def home(request):
    error=""
    if request.method == "POST" :
        nm=request.POST['name']
        desig=request.POST['designation']
        sa=request.POST['name']
        pic=request.POST['name']
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def skills(request):
    return render(request,'skills.html')

def projects(request):
    return render(request,'projects.html')