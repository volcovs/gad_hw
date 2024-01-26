import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from companie.forms import CompanyForm
from companie.models import Companies


# Create your views here.
class CompanyView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'companie/companie_index.html'


    def get_context_data(self, *args, **kwargs):
        data = super(CompanyView, self).get_context_data(*args, **kwargs)
        data['data_curenta'] = datetime.datetime.now()

        return data


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    form_class = CompanyForm
    template_name = 'companie/companie_form.html'

    def get_form_kwargs(self):
        data = super(CreateCompanyView, self).get_form_kwargs()
        data.update({'pk': None})

        return data

    def get_success_url(self):
        return reverse('companie:lista_companii')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    # fields = ['name', 'type', 'location']
    form_class = CompanyForm
    template_name = 'companie/companie_form.html'

    def get_form_kwargs(self):
        data = super(UpdateCompanyView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})

        return data

    def get_success_url(self):
        return reverse('companie:lista_companii')


@login_required
def deactivate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)

    return redirect('companie:lista_companii')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)

    return redirect('companie:lista_companii')