from django.shortcuts import render
from .models import Employee
from rest_framework import viewsets,generics
from .serializers import emp_serializer
from django.shortcuts import render,render_to_response

# Create your views here.


def index(request):

    data = Employee.objects.all()

    #return render(data)
    return render(request,'index.html',{'data':data})

class emp_viewset(viewsets.ModelViewSet):
    serializer_class = emp_serializer
    queryset = Employee.objects.all()






