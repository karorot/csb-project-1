from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("entry/<int:entry_id>/", views.read_entry, name="entry"),
    path("entry/new/", views.create_entry, name="new")
]
