from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from controls.forms import ControlForm
from controls.models import Control


class ControlListView(ListView):
    model = Control


class ControlDetailView(DetailView):
    model = Control


@method_decorator(staff_member_required, name='dispatch')
class CreateControlView(CreateView):
    model = Control
    success_url = reverse_lazy('controls:list')
    form_class = ControlForm


@method_decorator(staff_member_required, name='dispatch')
class UpdateControlView(UpdateView):
    model = Control
    template_name_suffix = "_update_form"
    form_class = ControlForm

    def get_success_url(self):
        return reverse_lazy('controls:control', args=[self.object.id])
