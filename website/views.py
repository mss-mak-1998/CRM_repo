from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationModelForm, RecordModelForm
from .models import Record
from django.contrib.auth.decorators import login_required


#AUTHENTICATION SECTION

def register_user(request):
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('website:login')
    else:
        form =  RegistrationModelForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'website/register.html', context)

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Verify credentials
            if user is not None:  # If authentication succeeds
                login(request, user)  # Log in the user
                return redirect('website:home')  # Redirect to the desired page
            else:
                form.add_error(None, 'Invalid username or password')  # Show error for invalid login
    
    context = {'form': form}
    return render(request, 'website/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('website:login')


# APP BACKENDS

@login_required
def home(request):
    records = Record.objects.all()
    
    context = {
        'records': records
    }
    
    return render(request, 'website/home.html', context)

@login_required
def create_record(request):
    if request.method == 'POST':
        form = RecordModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:home')
    
    else:
        form = RecordModelForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'website/create_record.html', context)

#LEAD DETAILS/RECORD
@login_required
def lead_record(request, pk):
    
    lead_record = Record.objects.get(id=pk)
    
    context ={
        'lead_record': lead_record
    }
    
    return render(request, 'website/lead_record.html', context)
    