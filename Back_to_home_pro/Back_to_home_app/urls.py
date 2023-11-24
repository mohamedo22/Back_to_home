from django.urls import path
from .views import *

urlpatterns = [
    path('',index , name='index'),
    path('add_data/', add_data , name='add_data'),
    path('invalid_id/', invalid_id , name='invalid_id'),
    path('add_successfuly/', add_succ , name='add_succ'),
    path('data/', data , name='data_page'),
    path('invalid_ids/', invalid_ids , name='invalid_ids'),
]
