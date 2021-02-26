from django.contrib.auth.models import User
from django import forms
from django.views.generic import TemplateView, FormView
from django.contrib.auth import password_validation


class RegisterForm(forms.Form):
    # This is a very basic example of a registration form,
    # and misses important checks like whether a username is unique.
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords are not equal')
        password_validation.validate_password(self.cleaned_data.get('password'), None)
        return self.cleaned_data

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register/register.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
