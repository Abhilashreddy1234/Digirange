from django.shortcuts import render
from django.template import loader
def members(request):
    template=loader.get_template('caurosal_plugin.html')
    return HttpResponse(template.render())
