from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import Entry


def entryReadView(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404("No such entry in the diary")
    return render(request, 'deardiary/entry.html', {'entry': entry})

def entryCreateView(request):
    response = "Write a new diary entry"
    return HttpResponse(response)

def homePageView(request):
    #entries = Entry.objects.filter(writer=request.user)

    entries = ["moi"]
    context = {'entries' : entries}
    return render(request, 'deardiary/index.html', context)
