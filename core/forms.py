#log/forms.py
import csv
import logging

from core.models import Product, Manufacturer, Category
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from openboxes.middleware import get_current_user
from django.utils.crypto import get_random_string

log = logging.getLogger(__name__)

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


class UploadFileForm(forms.Form):
    myfile = forms.FileField()

    def save(self):
        #records = csv.reader(self.cleaned_data["myfile"])
        dataReader = csv.DictReader(self.cleaned_data["myfile"], delimiter=',', quotechar='"')
        for row in dataReader:
            log.info("row: %s ", row)
            user = get_current_user()
            log.info("user: %s ", user)

            # Find product by its SKU if it exists, otherwise create a new one
            try:
                product = Product.objects.get(code=row["Code"])
            except Product.DoesNotExist:
                product = Product()
            log.info ("product: %s", product)
            product.code = row["Code"]
            product.name = row["Name"]
            product.unit_of_measure = row["Unit of Measure"]
            product.description = row["Description"]
            product.created_by = user


            # Find category if it exists or create a new one
            try:
                product.category = Category.objects.get(name=row["Category"])
            except Category.DoesNotExist:
                category_code = get_random_string(length=10)
                product.category = Category.objects.create(code=category_code, name=row["Category"])

            # Find manufacturer if it exists or create a new one
            try:
                product.manufacturer = Manufacturer.objects.get(name=row["Manufacturer"])
            except Manufacturer.DoesNotExist:
                product.manufacturer = Manufacturer.objects.create(name=row["Manufacturer"])

            # Save product
            product.save()

