from django import forms
from .models import Item


class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['created_by', 'created_at', 'is_sold']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-3 rounded-xl'
            }),
            'price': forms.NumberInput(attrs={'class': 'w-1/2 rounded-xl p-4'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'item brand, model, year, condition, faults, etc',
                'rows': 4,
                'class': 'w-full p-3 rounded-xl'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g: nasco fridge',
                'class': 'w-full p-3 rounded-xl'        
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-3 rounded-xl bg-white'        
            }),
        }



class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['created_by', 'created_at', 'category']
        widgets = {
            
            'price': forms.NumberInput(attrs={'class': 'w-1/2 rounded-xl p-4'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'item brand, model, year, condition, faults, etc',
                'rows': 4,
                'class': 'w-full p-3 rounded-xl'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g: nasco fridge',
                'class': 'w-full p-3 rounded-xl'        
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-3 rounded-xl bg-white'        
            }),
            'is_sold': forms.CheckboxInput(attrs={'class': 'p-3 rounded-xl'})
        }
