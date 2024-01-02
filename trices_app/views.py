from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'trices_app/base/home.html')

def about(request):
    return render(request,'trices_app/base/about.html')

def services(request):
    return render(request,'trices_app/base/services.html')

def ser_ind(request):
    return render(request,'trices_app/base/services_ind.html')

def contact(request):
    return render(request,'trices_app/base/contact.html')
    