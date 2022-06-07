from django.shortcuts import render

from .models import CertificateModel, WorkModel


def home(request):
    return render(request, 'mainpages/home.html')


def aboutus(request):
    return render(request, 'mainpages/aboutus.html')


def certificate(request):
    certificates = CertificateModel.objects.all()

    return render(request, 'mainpages/certificate.html',
                  {'certificates': certificates})


def contactus(request):
    return render(request, 'mainpages/contactus.html')


def foundernote(request):
    return render(request, 'mainpages/foundernote.html')


def work(request):
    works = WorkModel.objects.all()

    return render(request, 'mainpages/work.html', {'works': works})


def login(request):
    return render(request, 'mainpages/login.html')


def admin_panel(request):
    return render(request, 'mainpages/admin.html')
