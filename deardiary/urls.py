from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("entry/<int:entry_id>/", views.read_entry, name="entry"),
    path("new/", views.create_entry, name="new"),
    path("add/", views.add_entry, name="add")
]
