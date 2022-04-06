from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from awsapp.forms import EventForm
from awsapp.models import Event


class CreateEvent(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'home.html'
    success_url = '/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.model.objects.all()
        return context


