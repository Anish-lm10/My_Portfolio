import os
from django.http import FileResponse
from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from .models import *

# Create your views here.
date=datetime.now().year
def home(request):
    data=Education.objects.all()
    data1=Works.objects.all()
    return render(request,'myhtml/home.html',{'date':date ,'data':data,'data1':data1})

def about(request):
    data=Education.objects.all()
    return render(request,'myhtml/about.html',{'date':date ,'data':data})

def services(request):
    return render(request,'myhtml/services.html',{'date':date})

def works(request):
    data=Works.objects.all()
    return render(request,'myhtml/works.html',{'date':date, 'data':data})

def contact(request):
    return render(request,'myhtml/contact.html',{'date':date})

def download_cv(request):
    cv_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')  # Ensure your CV is located here
    return FileResponse(open(cv_path, 'rb'), as_attachment=True, filename='cv.pdf')

