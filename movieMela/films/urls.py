from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/',views.FilmsViewSet.as_view() ),
    path('user/', views.UserProfileViewSet.as_view()),
    path('user/<int:pk>/', views.FilmsViewSetDetail.as_view())
]

