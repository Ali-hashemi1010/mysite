from .views import *
from django.urls import path


urlpatterns = [
    path('home/' , index_view),
    path('contact/' , contact_view),
    path('about/' , about_view),
    
]