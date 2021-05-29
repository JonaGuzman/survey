from django import template
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('qr_survey/index.html')
    return HttpResponse(template.render({}, request))