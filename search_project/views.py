from django.shortcuts import render
from search_project.models import Employee


def showresult(request):
    display = Employee.objects.all()
    return render(request, 'index.html',{ "data":display})