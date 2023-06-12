from django.shortcuts import render

# Create your views here.
import calendar
from django.shortcuts import render
from django.utils import timezone

def onpremise(request):
    return render(request, 'clusteradmin/onpremise/index.html')
def aws(request):
    return render(request, 'clusteradmin/aws/index.html')