from django.contrib.auth.models import User
from django import forms


class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
                                       strip=False)
    email = forms.CharField(max_length=30, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        if not self.cleaned_data.get('first_name') and not self.cleaned_data.get('last_name'):
            raise forms.ValidationError('First name or last name should be registered.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password', 'password_confirm'}
