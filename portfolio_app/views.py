from django.shortcuts import render,redirect
from .models import Profile, About, Portfolio, Education, Experience, Contact
from . forms import DetailsForm


def index(request):
    # Fetching data from various models
    profiles = Profile.objects.all()
    abouts = About.objects.all()
    portfolios = Portfolio.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    contacts = Contact.objects.first()  # Assuming there's only one contact

    # Passing data to the template
    return render(request, "home.html", {
        'result': profiles,
        'result2': abouts,
        'result3': portfolios,
        'result4': educations,
        'result5': experiences,
        'result6': contacts
    })

def add_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            # Save form data to respective models
            profile = Profile.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],

            )
            portfolio = Portfolio.objects.create(
                title=form.cleaned_data['title'],
                description_portfolio=form.cleaned_data['description_portfolio'],

                url_portfolio=form.cleaned_data['url_portfolio']
            )
            education = Education.objects.create(
                degree=form.cleaned_data['degree'],
                institution=form.cleaned_data['institution']
            )
            experience = Experience.objects.create(
                title_experience=form.cleaned_data['title_experience'],
                company_experience=form.cleaned_data['company_experience']
            )
            contact = Contact.objects.create(
                email_contact=form.cleaned_data['email_contact'],
                phone_contact=form.cleaned_data['phone_contact'],
                address_contact=form.cleaned_data['address_contact']
            )

            # Redirect to index page after successful submission
            return redirect('home')
    else:
        form = DetailsForm()
    return render(request, 'add.html', {'form': form})

def base(request):
    return render(request,'base.html')

def resume(request):
    return render(request,'resume.html')

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request,'portfolio.html',{'portfolios':portfolios})

def update_portfolio(request):
    user_profile = Portfolio.objects.get(user=request.user)
    if request.method == 'POST':
        profile_form = DetailsForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('portfolio')
    else:
        profile_form = DetailsForm(instance=user_profile)
    return render(request, 'update_profile.html', {'profile_form': profile_form})


def work_experience(request):
    experiences = Experience.objects.all()
    return render(request,'experience.html',{'experiences':experiences})


def contacts(request):
    contact_s = Contact.objects.first()
    return render(request,'contacts.html',{'contact_s':contact_s})