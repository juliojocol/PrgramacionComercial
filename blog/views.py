from django.shortcuts import render, get_list_or_404
from django.utils import timezone
from django.utils.regex_helper import normalize

from.models import Publicacion

def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})

def publicacion_detalle(request, pk):
    publicacion = get_list_or_404(Publicacion, pk=pk)
    return render(request, 'blog/publicacion_detalle.html', {'publicacion':publicacion})
