from django.urls import path
from . import views
from item import views as item_views
from django.contrib.auth.views import LoginView
from .forms import LoginForm



urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('items/<int:id>', item_views.detail, name='detail'),
    path('items/browse', item_views.browse_items, name='browse'),
    path('items/create', item_views.create_item, name='create_item'),
    path('items/delete/<int:id>', item_views.delete, name='delete_item'),
    path('items/edit/<int:id>', item_views.edit, name='edit_item'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm,), name='login'),
]