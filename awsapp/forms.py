from django import forms

from awsapp.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = '__all__'