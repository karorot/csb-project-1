from django.urls import path

from . import views


urlpatterns = [
    path("", views.homePageView, name="home"),
    path("<int:user_id>/", views.diaryView, name="diary"),
    path("<int:user_id>/<int:entry_id>/", views.entryReadView, name="entry"),
    path("<int:user_id>/new/", views.entryCreateView, name="new")
]
