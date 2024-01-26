from django import forms
from django.forms import TextInput

from companie.models import Companies
from locatie.models import Location


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ['name', 'company_type', 'website', 'location']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Company name', 'class': 'form-control'}),
            'company_type': TextInput(attrs={'placeholder': 'Company type', 'class': 'form-control'}),
            'website': TextInput(attrs={'placeholder': 'Company website', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        company_choices = (('SRL', 'S.R.L.'),
                           ('SA', 'S.A.'))

        name_value = self.cleaned_data.get('name')
        type_value = self.cleaned_data.get('company_type')
        website = self.cleaned_data.get('website')

        if not type_value:
            self._errors['company_type'] = self.error_class(['Tip invalid de companie'])
        else:
            # daca pk != None => update
            if self.pk:
                if Companies.objects.filter(name__icontains=name_value, company_type__icontains=type_value, website__icontains=website).exclude(id=self.pk).exists():
                    self._errors['name'] = self.error_class(['Compania deja exista'])
            else:
                if Companies.objects.filter(name__icontains=name_value, company_type__icontains=type_value, website__icontains=website).exists():
                    self._errors['name'] = self.error_class(['Compania deja exista'])
                return self.cleaned_data
