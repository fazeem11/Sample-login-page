
from django.http import HttpResponse
from django.template import loader
def jijimiss(request):
    template =loader.get_template('myfile.html')
    return HttpResponse(template.render())