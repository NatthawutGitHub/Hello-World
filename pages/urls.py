from django.urls import path  #
from .views import homePageView  # referring to view.py, .views are telling django look within the current directory.

urlpatterns = [
    path('', homePageView, name='home')
]
