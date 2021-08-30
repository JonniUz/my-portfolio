from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-message/', views.receive_message, name='message'),
    path('send-message/thanks/', views.contact_thank, name='thanks'),
]
