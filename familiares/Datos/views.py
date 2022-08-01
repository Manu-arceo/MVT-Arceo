from django.shortcuts import render
from django.http import HttpResponse
from Datos.models import padres

def padres(request):

    Padres = padres.objects.all()

    return render(request, "Datos/padres.html", {"padres": padres} )
