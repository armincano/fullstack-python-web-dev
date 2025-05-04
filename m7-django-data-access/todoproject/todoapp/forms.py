from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        label = {
        "title" : "Title",
        "description" : "Description",
        }

        widgets ={
        "title" : forms.TextInput(attrs={"placeholder":"Buy Groceries"}),
        "description" : forms.TextInput(attrs={"placeholder":"Visit super market and buy some groceries"}), 
        }