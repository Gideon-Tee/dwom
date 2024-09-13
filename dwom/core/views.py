from django.shortcuts import render, redirect
from item.models import Item, Category
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from core.forms import SignUpForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)

@login_required(login_url='login')
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    context = {'items': items}
    return render(request, 'core/dashboard.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    form = SignUpForm()
    if request.user.is_authenticated:
        return redirect('index')
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