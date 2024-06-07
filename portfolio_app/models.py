
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class About(models.Model):
    bio = models.TextField()

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description_portfolio= models.TextField()
    url_portfolio=models.URLField(blank=True, null=True)
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)

class Experience(models.Model):
    title_experience= models.CharField(max_length=100)
    company_experience = models.CharField(max_length=100)

class Contact(models.Model):
    email_contact=models.EmailField()
    phone_contact = models.CharField(max_length=15)
    address_contact=models.TextField()
