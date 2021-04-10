from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm


# Create your views here.


def login_view(request):
    context = {}
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(next)
            if not next:
                return redirect('project:listview')
            return redirect(next)
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('project:listview')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project:listview')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})
