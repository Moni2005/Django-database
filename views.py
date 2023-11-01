# from django.http import HttpResponse
from django.shortcuts import render
from .forms import LandingPageEntryModelForm
from .models import LandingPageEntry

def home_page(request, *args, **kwargs):
    title = "Welcome home"
    # print(request.method== "POST")
    form = LandingPageEntryModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        obj = LandingPageEntry()
        obj.name = name
        obj.email = email 
        obj.save()
        form = LandingPageEntryModelForm()
    # print(request.POST.get('email'))
    
    
    context = {
        'title' : title,
        'form'  : form,
    }
    return render(request, "landing_pages/home.html", context)
