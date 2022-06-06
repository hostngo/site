from django.shortcuts import render


def home(request):
    return render(request, 'mainpages/home.html')


def aboutus(request):
    return render(request, 'mainpages/aboutus.html')


def certificate(request):
    return render(request, 'mainpages/certificate.html')


def contactus(request):
    return render(request, 'mainpages/contactus.html')


def foundernote(request):
    return render(request, 'mainpages/foundernote.html')


def work(request):
    return render(request, 'mainpages/work.html')
