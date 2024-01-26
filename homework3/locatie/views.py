import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from locatie.forms import LocationForm
from locatie.models import Location


# Create your views here.
class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'locatie/location_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(LocationView, self).get_context_data(*args, **kwargs)
        data['data_curenta'] = datetime.datetime.now()

        return data


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'locatie/location_form.html'

    def get_form_kwargs(self):
        data = super(CreateLocationView, self).get_form_kwargs()
        data.update({'pk': None})

        return data

    def get_success_url(self):
        return reverse('locatie:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'locatie/location_form.html'

    def get_form_kwargs(self):
        data = super(UpdateLocationView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})

        return data

    def get_success_url(self):
        return reverse('locatie:lista_locatii')


@login_required
def deactivate_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)

    return redirect('locatie:lista_locatii')


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)

    return redirect('locatie:lista_locatii')