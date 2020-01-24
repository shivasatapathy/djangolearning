from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   return render(request,'index.html')
def add(request):
    n1=request.GET['num1']
    n2=request.GET['num2']
    sum=int(n1)+int(n2)
    return render(request,'result.html',{"result":sum})
