from django.urls import path
from . import views


urlpatterns = [
    path('', views.console, name='console'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('comment/<int:id>', views.add_comment, name='add_comment'),
]