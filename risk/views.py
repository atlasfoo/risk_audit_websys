from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from risk.forms import RiskForm
from risk.models import Risk


# RISK VIEWS
class RiskListView(ListView):
    model = Risk


class RiskDetailView(DetailView):
    model = Risk


class CreateRiskView(CreateView):
    model = Risk
    success_url = reverse_lazy('risks:list')
    form_class = RiskForm


class UpdateRiskView(UpdateView):
    model = Risk
    template_name_suffix = "_update_form"
    form_class = RiskForm

    def get_success_url(self):
        return reverse_lazy('risks:risk', args=[self.object.id])

# TODO: CAUSE VIEWS

# TODO: EFFECT VIEWS


