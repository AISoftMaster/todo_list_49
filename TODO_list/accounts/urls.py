from django.urls import path
from .views import login_view, logout_view, register_view, UserDetailView, UserListView,\
    UserChangePassword, UserUpdateView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', register_view, name='create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('users/list/', UserListView.as_view(), name='list'),
    path('user/change/<int:pk>/', UserChangePassword.as_view(), name='change_password'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]
