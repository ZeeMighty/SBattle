from django.http import HttpResponse
from django.template import loader
from HiPage.models import event, heroe
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'HiPage/homepage.html'
    context_object_name = 'events_title'

    def get_queryset(self):
        return event.objects.order_by('id')[:20]

def hero(request, heroe_id):
    heroes = get_object_or_404(heroe, pk=heroe_id)
    context = {'heroes': heroes}
    return render(request, 'HiPage/heroesPage.html', context)
