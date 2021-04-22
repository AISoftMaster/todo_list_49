from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, UserChangePasswordForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.urls import reverse


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


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        projects = self.object.projects.order_by('-created')
        paginator = Paginator(projects, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['project'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UserListView(PermissionRequiredMixin, ListView):
    template_name = "users_list.html"
    model = get_user_model()
    context_object_name = "users"
    permission_required = "accounts.can_view_userlist"
    paginate_by = 10


class UserChangePassword(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    context_object_name = 'user_obj'
    template_name = 'user_change_password.html'
    form_class = UserChangePasswordForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super(UserChangePassword, self).form_valid(form)

        update_session_auth_hash(self.request, self.request.user)
        return response

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm

    profile_form_class = ProfileUpdateForm

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['profile_form'] = kwargs.get('profile_form')
        if context['profile_form'] is None:
            context['profile_form'] = self.get_profile_form()
        return context

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.get_form()
        profile_form = self.get_profile_form()

        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)
        return self.form_invalid(user_form, profile_form)

    def get_object(self, queryset=None):
        return self.request.user

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data(
            form=user_form,
            profile_form=profile_form
        )
        return self.render_to_response(context)

    def form_valid(self, user_form, profile_form):
        response = super(UserUpdateView, self).form_valid(user_form)
        profile_form.save()
        return response

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}

        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return self.profile_form_class(**form_kwargs)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})
