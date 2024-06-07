

from django import forms
from .models import Profile, About, Portfolio, Education, Experience, Contact


class DetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()



    title = forms.CharField(max_length=200)
    description_portfolio = forms.CharField(widget=forms.Textarea)
    url_portfolio = forms.URLField(required=False)

    degree = forms.CharField(max_length=100)
    institution = forms.CharField(max_length=100)






    title_experience = forms.CharField(max_length=100)
    company_experience = forms.CharField(max_length=100)



    email_contact = forms.EmailField()
    phone_contact = forms.CharField(max_length=15)
    address_contact = forms.CharField(widget=forms.Textarea)