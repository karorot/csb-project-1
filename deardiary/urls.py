from django.urls import path

from . import views


urlpatterns = [
    path("", views.homePageView, name="home"),
    path("entry/<int:entry_id>/", views.entryReadView, name="entry"),
    path("entry/new/", views.entryCreateView, name="new")
]
