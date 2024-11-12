import os
import re
from django.http import FileResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *

# Create your views here.
date = datetime.now().year


def home(request):
    data = Education.objects.all()
    data1 = Works.objects.all()
    return render(
        request, "myhtml/home.html", {"date": date, "data": data, "data1": data1}
    )


def about(request):
    data = Education.objects.all()
    return render(request, "myhtml/about.html", {"date": date, "data": data})


def services(request):
    return render(request, "myhtml/services.html", {"date": date})


def works(request):
    data = Works.objects.all()
    return render(request, "myhtml/works.html", {"date": date, "data": data})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        emails = request.POST.get("email")
        subject = request.POST.get("subject")
        textareas = request.POST.get("textareas")

        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", emails):
            messages.error(request, "Invalid email")
            return redirect("contact")
        else:
            try:
                email_message = EmailMessage(
                subject=subject,
                body=textareas,
                from_email="anishnepal000@gmail.com",  # Your verified email address
                to=["anishnepal000@gmail.com"],  # Recipient's email address
                headers={"Reply-To": emails}  # User's email in Reply-To header
            )
                email_message.send(fail_silently=False)
                messages.success(request, "Email has been sent!!")
                return redirect("home")
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
                return redirect("contact")

    return render(request, "myhtml/contact.html", {"date": date})


def download_cv(request):
    cv_path = os.path.join(
        settings.MEDIA_ROOT, "cv.pdf"
    )  # Ensure your CV is located here
    return FileResponse(open(cv_path, "rb"), as_attachment=True, filename="cv.pdf")
