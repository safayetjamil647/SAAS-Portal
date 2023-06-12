from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def wordpress(request):
    return render(request, 'deployments/wordpress/index.html')
def saas(request):
    return render(request, 'deployments/saas/index.html')