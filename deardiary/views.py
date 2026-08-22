from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Entry


@login_required
def read_entry(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404("No such entry")
    return render(request, 'deardiary/entry.html', {'entry': entry})


@login_required
def create_entry(request):
    response = "Write a new diary entry"
    return HttpResponse(response)


def index(request):
    context = {}

    if request.user.is_authenticated:
        entries = Entry.objects.filter(writer=request.user)
        context['entries'] = entries

    return render(request, 'deardiary/index.html', context)
