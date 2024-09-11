from django.urls import path
from . import views
from item import views as item_views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('items/<int:id>', item_views.detail, name='detail'),
    path('signup', views.signup, name='signup'),
]