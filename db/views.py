from models import *
from django.shortcuts import *
from hashlib import md5

def index(request):
    m = md5()
    m.update('833177ac233dd470b0afd363c14d1f4d')
    m.update('db.flexibilni-architektura.cz')
    projects = Project.objects.all().order_by('year')
    return render_to_response('index.html', {
        'projects': projects,
        'key': 'b3984903484cf92da111a0012011a05d',
        'sig': m.hexdigest()
        }, RequestContext(request))
