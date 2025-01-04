from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from . forms import SignUpForm, AddCustomerForm
from . models import Customer


def home(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in Successfully!!! ')
            return redirect('home')
        else:
            messages.success(request, 'There was a error logging in, Please try again...')
            return redirect('home')
    return render(request, 'home.html', {'customers':customers})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!!..')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully Registered! Welcome!!!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def single_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        return render(request, 'single_customer.html', {'customer':customer})
    else:
        messages.success(request, 'You must be logged in to view the customer details!!')
        return redirect('home')
    

def delete_customer(request,pk):
     if request.user.is_authenticated:
         customer = Customer.objects.get(id=pk)
         customer.delete()
         messages.success(request, 'Customer Record deleted successfully!!')
         return redirect('home')
     else:
         messages.success(request, 'You must be logged in to delete the customer record...')
         return redirect('home')
     

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, 'New Customer Added Successfully.')
                return redirect('home')
        else:
            return render(request, 'add_customer.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in to Add new Customers !!!')
        return redirect('home')
    

def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Record Changed Successfully..')
            return redirect('home')
        else:
            return render(request, 'update_customer.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in, to update the customer records!!!')
        return redirect('home')
    
    