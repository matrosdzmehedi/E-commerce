from django.urls import path
from .views import ProfileView,Profiledit


urlpatterns = [
    
    path('profile/',ProfileView.as_view(),name='profile' ),
    path('profile_edit/',Profiledit.as_view(),name='profile-edit' ),
    
]