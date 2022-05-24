from django.urls import path
from . import views





urlpatterns = [
    
    path('bannerhome/',views.BannerHomeCreate.as_view()),
    path('bannerhome/<int:pk>/',views.BannerHomeUpdate.as_view())
]