from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/',views.FilmsViewSet.as_view() ),
]

