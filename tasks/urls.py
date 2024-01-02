from django.urls import path
from tasks.views import test

app_name = "bids"

urlpatterns = [
    path('', test, name='test')
]