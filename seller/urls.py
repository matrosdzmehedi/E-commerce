from django.urls import path
from .views import ProfileView,Profiledit,Item,ItemDetailView,ItemUpdateView,ItemDeleteView


urlpatterns = [
    
    path('profile/',ProfileView.as_view(),name='profile' ),
    path('profile-edit/',Profiledit.as_view(),name='profile-edit' ),
    path('add-item/',Item.as_view(),name='add-item'),
    path('item-detail/<str:slug>/',ItemDetailView.as_view(), name='item-detail'),
    path('item-edit/<str:slug>/',ItemUpdateView.as_view(), name='item-edit'),
    path('item/<str:slug>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    
    
]