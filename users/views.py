from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import Register, UserInfoUpdate , ProfileUpdate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account Created for {username}') # f is actually format
            return redirect('login')
        # else:
        #     messages.warning(request , f'Please Read the rules and fill !')
        #     return redirect('register')
    else:
        form = Register()
    return render(request , 'users/register.html' , { 'form' : form})

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserInfoUpdate(request.POST , instance=request.user)
        p_form = ProfileUpdate(request.POST , request.FILES ,instance=request.user.profiel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request , f' Profile Updated for {username}') # f is actually format
            return redirect('profile')
    else:
        u_form = UserInfoUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profiel)
    context = {
        'u_form' : u_form , 
        'p_form' : p_form , 
    }
    return render(request , 'users/profile.html' , context=context)