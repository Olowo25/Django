from django.shortcuts import render
from django.template import loader
from .form import StudentForm
from django.http import HttpResponse
from .functions import handle_uploaded_file

def daddy(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['username'])
        return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
    return render(request,"daddy.html",{'form':student})

def practice(request):
    template = loader.get_template('template.html')
    context ={
        'fruits':['Apple','Banana','Cherry'],
        'greeting' : 1,
        'cars': [
            {'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',},

            {   'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',  },

            {   'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964', },

            {  'brand': 'Toyota',
               'model': '23456',
               'year': '1999', }
        ]
    }

    return HttpResponse(template.render(context, request))



