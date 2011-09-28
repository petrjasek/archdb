from models import *
from django.shortcuts import *

def index(request):
    projects = Project.objects.all().order_by('-id')
    return render_to_response('index.html', {
        'projects': projects,
        }, RequestContext(request))
