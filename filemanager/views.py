from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import FileForm

# Create your views here.
from .models import Files


def welcome(request):
    if request.method == 'POST':
        return redirect('upload')
    files = Files.objects.all()
    return render(request, 'welcome.html', {
        'files': files
    })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('welcome')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form': form
    })


def delete(request, pk):
    if request.method == 'POST':
        file = Files.objects.get(pk=pk)
        file.delete()
    return redirect('welcome')


def signup(response):
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/welcome")
    else:
        form = UserCreationForm()

    return render(response, "signup.html", {"form": form})
