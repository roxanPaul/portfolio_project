from django.urls import path
from . import views
urlpatterns=[

    path('home/',views.index,name='home'),
    path('add/',views.add_details,name='add'),
    path('resume/',views.resume,name='resume'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('update_portfolio/',views.update_portfolio,name='update_portfolio'),
    path('experience/',views.work_experience,name='experience'),
    path('contact/',views.contacts,name='contact'),
    path('',views.base,name='base')
]