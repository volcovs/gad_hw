from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
        }


        def __init__(self, pk, *args, **kwargs):
            super(NewAccountForm, self).__init__(*args, **kwargs)
            self.pk = pk

        def clean(self):
            field_data = self.cleaned_data
            email_value = field_data.get('email')
            username_value = field_data.get('username')

            if self.pk:
                # update user action
                if User.objects.filter(email=email_value).exclude(id=self.pk).exists():
                    self._errors['email'] = self.error_class(['Emailul deja exista!'])
                if User.objects.filter(username=username_value).exclude(id=self.pk).exists():
                    self._errors['username'] = self.error_class(['Username-ul deja exista!'])
            else:
                # create user action
                if User.objects.filter(email=email_value).exists():
                    self._errors['email'] = self.error_class(['Emailul deja exista!'])
                if User.objects.filter(username=username_value).exists():
                    self._errors['username'] = self.error_class(['Username-ul deja exista!'])
            return field_data