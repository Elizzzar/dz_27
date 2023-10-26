from django.shortcuts import render, redirect
from .forms import test_form
from .models import test_model
# Create your views here.

def process_form(request):
    if request.method == "POST":
        form = test_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            
            new_object = test_model(name=name, email=email)
            new_object.save()

            return redirect('success')
    else:
        form = test_form()

    return render(request, "test_template.html", {"form": form})

def success(request):
    return render(request, "success.html")