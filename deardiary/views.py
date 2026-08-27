from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from random import sample

from .models import Entry

def random_entries():
    public_entries = Entry.objects.filter(public=True).order_by('?')[:5]
    return list(public_entries)


@login_required
def read_entry(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404()

    # fix for flaw 1: broken access control
    # if request.user != entry.writer:
        # return HttpResponseForbidden()

    return render(request, 'deardiary/entry.html', {'entry': entry})


@login_required
def create_entry(request):
    return render(request, 'deardiary/new.html')


@login_required
def add_entry(request):
    writer = User.objects.get(id=request.user.id)
    title = request.POST.get('title')
    body = request.POST.get('body')
    public = False

    if request.POST.get('public') == 'public':
        public = True

    Entry.objects.create(writer=writer, title=title, body=body, public=public)

    messages.success(request, 'Entry saved!')

    return redirect('/')


def index(request):
    context = {}

    if request.user.is_authenticated:
        entries = Entry.objects.filter(writer=request.user)
        context['entries'] = entries
        context['random'] = random_entries()

    return render(request, 'deardiary/index.html', context)
