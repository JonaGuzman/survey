from django.shortcuts import render

def index(request):
    return render(request, 'qr_survey/index.html')
