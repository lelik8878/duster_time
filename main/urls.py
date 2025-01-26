
from django.urls import path
from .views import get_home_page, check_time, set_time


urlpatterns = [
    path('', get_home_page, name='home'),
    path('checktime/', check_time, name='check_time'),
    path('settime/', set_time, name='set_time'),
]