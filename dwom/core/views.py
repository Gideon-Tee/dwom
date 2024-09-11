from django.shortcuts import render, redirect
from item.models import Item, Category
from django.contrib.auth.models import User, auth
from core.forms import SignUpForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
            
            auth.login(request, user)
            return redirect('index')
    return render(request, 'core/signup.html', {'form': form})