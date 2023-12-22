from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Babes
from django.shortcuts import render, redirect
from .form import MyBabes
from .upload import upload


# Create your views here.
def babes(request):
    # if request.method == "POST":
    #     formBabes = MyBabes(request.POST, request.files)
    #     if formBabes.is_valid():
    #         upload(request.FILES['picture'])
    #     try:
    #         formBabes.save()
    #         return redirect('/show')
    #     except:
    #         pass
    #     else:
    template = loader.get_template('inde.html')
    return HttpResponse(template.render({}, request))
    # formBabes = MyBabes()
    # return render(request, 'inde.html', formBabes)


def addbabe(request):
    nam = request.POST['name']
    yea = request.POST['year']
    ratin = request.POST['rating']
    ag = request.POST['age']
    bab = Babes(name=nam, year=yea, rating=ratin, age=ag)
    bab.save()
    return HttpResponseRedirect(reverse('index'))

def show(request):
    mybabies = Babes.objects.all()
    return render(request, "show.html", {'mybabies': mybabies})


def edit(request, id):
    baby = Babes.objects.get(id=id)
    return render(request, 'edit.html', {'baby': baby})


def update(request, id):
    babie = Babes.objects.get(id=id)
    babe = MyBabes(request.POST, instance=babie)
    if babe.is_valid():
        babe.save()
        return redirect("/show")
    return render(request, 'edit.html', {'baby': babie})


def destroy(request, id):
    babe = Babes.objects.get(id=id)
    babe.delete()
    return redirect("/show")
