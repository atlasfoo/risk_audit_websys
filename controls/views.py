from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from controls.forms import ControlForm
from controls.models import Control


class ControlListView(ListView):
    model = Control


class ControlDetailView(DetailView):
    model = Control


class CreateControlView(CreateView):
    model = Control
    success_url = reverse_lazy('controls:list')
    form_class = ControlForm


class UpdateControlView(UpdateView):
    model = Control
    template_name_suffix = "_update_form"
    form_class = ControlForm

    def get_success_url(self):
        return reverse_lazy('controls:control', args=[self.object.id])
