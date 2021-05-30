from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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

# TODO: CAUSE VIEWS

# TODO: EFFECT VIEWS


