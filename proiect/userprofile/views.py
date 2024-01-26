import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from userprofile.forms import NewAccountForm

# Create your views here.
class CreateNewAccountView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/location_form.html'
    form_class = NewAccountForm

    def get_form_kwargs(self, **kwargs):
        data = super(CreateNewAccountView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('userprofile:listare_utilizatori')


class ListOfUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/registration_index.html'


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'aplicatie1/location_form.html'
    form_class = NewAccountForm

    def get_form_kwargs(self, **kwargs):
        data = super(UpdateUserView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('userprofile:listare_utilizatori')


def reinvite_user(request, pk):
    if request.user.id != pk:

        psw = ''.join(random.choice(string.ascii_uppercase +
                                    string.ascii_lowercase +
                                    string.digits + '!$%#@') for _ in range(8))

        if (user_instance := User.objects.filter(id=pk)) and user_instance.exists():
            user_object = user_instance.first()
            user_object.set_password(psw)
            user_object.save()

            content = f"Buna ziua, \n Datele de autentificare sunt: \n username: {user_object.username} \n" \
                      f"parola: {psw}"
            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='Date contact platforma',
                                           body=content,
                                           from_email='contact@platforma.ro',
                                           to=[user_object.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
    return redirect('userprofile:listare_utilizatori')