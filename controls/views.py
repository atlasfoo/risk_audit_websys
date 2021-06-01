from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from controls.forms import ControlForm
from controls.models import Control
from incidences.models import Incidence


class ControlListView(ListView):
    model = Control


class ControlDetailView(DetailView):
    model = Control

    def get_context_data(self, **kwargs):
        context = super(ControlDetailView, self).get_context_data(**kwargs)
        incidences = Incidence.objects.filter(risk_id=self.object.risk.id)
        prob = (incidences.filter(controls__id=self.object.id).count() / incidences.count()) * 100
        context['control_effect'] = prob
        return context


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
