from django import forms
from .models import Leave
from .widgets import DatePickerInput

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['halaqa_name', 'halaqa_type', 'date_of_leave', 'date_of_return']
        widgets = {'date_of_leave' : DatePickerInput(), 'date_of_return' : DatePickerInput(),}

