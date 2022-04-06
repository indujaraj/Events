from django import forms

from awsapp.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            "start_time": forms.TimeInput(attrs={'type': 'time'}),
            "end_time": forms.TimeInput(attrs={'type': 'time'}),
        }
