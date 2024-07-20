# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('view_obituaries/', views.view_obituaries, name='view_obituaries'),
    path('submit_obituary/', views.submit_obituary, name='submit_obituary'),
    path('obituaries/', views.view_obituaries, name='view_obituaries')
    # Other paths for your application
]
