from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

import bleach

from .models import Entry


def random_entries():
    '''Picks five random entries from the db that are marked public'''
    public_entries = Entry.objects.filter(public=True).order_by('?')[:5]
    return list(public_entries)


# fix for flaw 2: sanitizing user's input for simple html tags
# def sanitize_html(content):
#     '''Sanitizes HTML elements in the input'''
#     if not content:
#         return ""
#     sanitized = bleach.clean(content, tags=['b', 'i', 'br'], strip=True)
#     sanitized = sanitized.replace("\n", "<br />")
#     return sanitized


@login_required
def read_entry(request, entry_id):
    '''Fetches the requested entry and renders it'''

    # fix for flaw 4: handling errors when the entry to be retrieved doesn't exist
    # try:
    #     entry = Entry.objects.get(pk=entry_id)
    # except Entry.DoesNotExist:
    #     raise Http404()

    entry = Entry.objects.get(pk=entry_id)

    # fix for flaw 1: broken access control
    # if request.user != entry.writer:
        # return HttpResponseForbidden()

    return render(request, 'deardiary/entry.html', {'entry': entry})


@login_required
def create_entry(request):
    '''Renders the page for creating a new diary entry'''
    return render(request, 'deardiary/new.html')


@login_required
def add_entry(request):
    '''Adds a new entry object to the db based on form contents'''

    if request.method == 'POST':
        writer = User.objects.get(id=request.user.id)

        title = request.POST.get('title')
        if not title or len(title) > 100:
            messages.error(request, 'Title too long or missing')
            return redirect('new')

        #Fix for flaw 2 to be used instead of the line below: sanitize_html(request.POST.get('body'))
        body = request.POST.get('body') 
        if not body or len(body) > 10000:
            messages.error(request, 'Entry too long or missing')
            return redirect('new')

        visibility = request.POST.get('public')
        if not visibility:
            messages.error(request, 'Specify visibility for the entry')
            return redirect('new')

        public = False
        if visibility == 'public':
            public = True

        Entry.objects.create(writer=writer, title=title, body=body, public=public)
        messages.success(request, 'Entry saved!')

    return redirect('/')


def index(request):
    '''Renders the home/index page'''
    context = {}

    if request.user.is_authenticated:
        entries = Entry.objects.filter(writer=request.user)
        context['entries'] = entries
        context['random'] = random_entries()

    return render(request, 'deardiary/index.html', context)
