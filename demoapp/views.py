from django.shortcuts import render
# from django.http import HttpResponse
from .models import place, person


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1 = person.objects.all()
    return render(request, "index.html", {'result': obj})
    return render(request, "index.html", {'result1': obj1})
