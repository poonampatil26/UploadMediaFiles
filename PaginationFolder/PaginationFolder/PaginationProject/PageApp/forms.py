from .models import Mobile
from django import forms

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'

        widgets = {
            'sim_type': forms.RadioSelect()
        }

        labels = {
            'mobile_name': 'Mobile',
            'brand': 'Brand',
            'ram': 'RAM',
            'price': 'Price',
            'internal_storage': 'Internal_Storage',
            'battery_capacity': 'Battery_Capacity',
            'sim_type': 'Sim_Type'
        }

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Mobile
#         fields = ('image',)