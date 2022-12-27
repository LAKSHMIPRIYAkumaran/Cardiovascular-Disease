
from django.urls import path
from .views import Cardiovascular_finder

urlpatterns = [
    path('show_Health/', Cardiovascular_finder, name ='Health_show'),
    #path ('results-Cardiovascular/', reults, name='results_show'),
]