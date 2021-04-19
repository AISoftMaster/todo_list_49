from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile',
                                on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    git_profile = models.URLField(max_length=300, null=True, blank=True)
    curriculum = models.CharField(max_length=600, null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = [('can_view_userlist', 'может видеть список пользователей')]
