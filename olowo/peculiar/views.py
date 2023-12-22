from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import MyForm
from .models import Details
from django.forms import modelformset_factory


def pecu(request):
    template = loader.get_template('dami.html')
    name = {
        'student': 'Kambok', 'age': 35, 'school': 'kambok infotech'
     }
    stu = MyForm()
    return render(request, "dami.html", {'form': stu})
    return HttpResponse(template.render(name))


def pecupecu(request):

    stu = modelformset_factory(Details, fields=('__all__'))
    form = stu()
    return render(request, "pelu.html", {'former': form})
