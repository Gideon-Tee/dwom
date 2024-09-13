from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item, Category
from .forms import ItemCreationForm, EditItemForm
from django.db.models import Q
# Create your views here.


def detail(request, id):
    item = get_object_or_404(Item, id=id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=id)[0:3]
    context = {'item': item, 'related_items': related_items}
    return render(request, 'item/detail.html', context)


@login_required(login_url='login')
def create_item(request):
    form = ItemCreationForm()
    if request.method == 'POST':
        form = ItemCreationForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.image = form.cleaned_data['image']
            new_item.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'item/create-item.html', context)


def delete(request, id):
    item = get_object_or_404(Item, id=id)
    if item.created_by == request.user:
        item.delete()
    else:
        messages.info(request, 'You cannot delete this item')
        return redirect('detail', id)
    return redirect('dashboard')


def edit(request, id):
    item = get_object_or_404(Item, id=id)
    if item.created_by == request.user:
        form = EditItemForm(instance=item)
        if request.method == 'POST':
            form = EditItemForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('detail', id)
            
        context = {'form': form}

        return render(request, 'item/edit-item.html', context)
    
    else:
        messages.info(request, 'You cannot edit this item')
        return redirect('detail', id)
    
    
def browse_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.all()

    categories = Category.objects.all().order_by('name')
    
    if category_id:
        if category_id == 0:
            items = Item.objects.filter(is_sold=False)
        else:
            items = Item.objects.filter(is_sold=False, category__id=category_id)

    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'items': items,
        'query': query, 
        'categories': categories, 
        'category_id': int(category_id) 
        }
    return render(request, 'item/browse.html', context)