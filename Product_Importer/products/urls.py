from django.urls import path
from .views import add_view, upload

urlpatterns = [
    path('add/', add_view),
    path('upload/', upload)
]