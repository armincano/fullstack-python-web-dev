from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={'type': 'email'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            permission = Permission.objects.get(codename='can_see_catalog')
            user.user_permissions.add(permission)
        return user
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso.")
        return email