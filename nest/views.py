from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    notices = Notices.objects.filter().order_by('-id')[:5]
    results = Result.objects.filter().order_by('-id')[:5]
    news_tickers = NewsTicker.objects.filter().order_by('id')

    context = {'notices':notices, 'results': results,'news_tickers': news_tickers }
    return render(request,'nest/home.html',context)

def notices(request):
    notices = Notices.objects.filter().order_by('-id')

    context = {'notices': notices}
    return render(request,'nest/notices.html',context)

def results(request):
    results = Result.objects.filter().order_by('-id')

    context = {'results': results}
    return render(request,'nest/results.html',context)

def routine(request):
    return render(request,'nest/routine.html')

def contact(request):
    return render(request,'nest/contact.html')

def admission(request):
    return render(request,'nest/admission.html')

def view_notice(request, pk):
    notice = Notices.objects.get(id=pk)

    return render(request, 'nest/view_notice.html', {'notice': notice})

def view_result(request, pk):
    result = Result.objects.get(id=pk)

    return render(request, 'nest/view_result.html', {'result': result})