from django.forms import ModelForm
from home.models import Lead

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'estate_name':('Which Land'),
            'number_of_plots': ('How Many Plots'),
            'home_address': ('Home Address'),
            'office_address': ('Office Address'),
            'email': ('Email'),
            'phone_number': ('Phone Number'),
            'date': ('Date'),
        }
