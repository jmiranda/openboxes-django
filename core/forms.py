#log/forms.py
from core.models import Product
from django.contrib.auth.forms import AuthenticationForm
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'created_by']

    code = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    #code = forms.CharField()
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
