from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteCreateList.as_view(), name="note-list"),
    path("notes/delete/<int:pk>", views.NoteDelete.as_view(), name="note-delete"),
]