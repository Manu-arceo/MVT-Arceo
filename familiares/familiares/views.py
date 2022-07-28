from django.http import HttpResponse
from django.template import Template, Context





def index(request):

    archivo = open(r"C:\Users\manu_\Documents\Python\MVT+ARCEO\familiares\familiares\templates\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)

    contexto = Context()

    documento_a_renderizar = plantilla.render(contexto)

    return HttpResponse(documento_a_renderizar)