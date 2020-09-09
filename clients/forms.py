from django import forms
from .models import Vehicle

class DateInput(forms.DateInput):
    input_type = 'date'

class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'vinnumber', 'dateofpurchase', 'dateoflastservice','color','capacity','description')
        widgets = {
        'dateofpurchase': DateInput(),
        'dateoflastservice': DateInput()
        }


class VehicleEditForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('client','make', 'model', 'vinnumber', 'dateofpurchase', 'dateoflastservice','color','capacity','description')
        widgets = {
            'dateofpurchase': DateInput(),
            'dateoflastservice': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(VehicleEditForm, self).__init__(*args, **kwargs)
        self.fields['client'].disabled = True

