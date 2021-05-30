from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from risk.forms import RiskForm, CauseForm
from risk.models import Risk, Cause


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


# CAUSE VIEWS
class CauseListView(ListView):
    model = Cause


class CauseDetailView(DetailView):
    model = Cause


class CreateCauseView(CreateView):
    model = Cause
    success_url = reverse_lazy('risks:cause_list')
    form_class = CauseForm


class UpdateCauseView(UpdateView):
    model = Cause
    template_name_suffix = "_update_form"
    form_class = CauseForm

    def get_success_url(self):
        return reverse_lazy('risks:cause', args=[self.object.id])


# TODO: EFFECT VIEWS


