from django.shortcuts import render
from django.views.generic import ListView, DetailView

from risk.models import Risk

# RISK VIEWS


class RiskListView(ListView):
    model = Risk


class RiskDetailView(DetailView):
    model = Risk


# TODO: CAUSE VIEWS

# TODO: EFFECT VIEWS


