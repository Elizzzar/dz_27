from django.urls import path
from .views import process_form, success

urlpatterns = [
    path('', process_form, name='test_template'),
    path('success/', success, name='success')
]
