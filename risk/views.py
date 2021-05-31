from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from risk.forms import RiskForm, CauseForm, EffectForm
from risk.models import Risk, Cause, Effect


# RISK VIEWS
class RiskListView(ListView):
    model = Risk


class RiskDetailView(DetailView):
    model = Risk


@method_decorator(staff_member_required, name='dispatch')
class CreateRiskView(CreateView):
    model = Risk
    success_url = reverse_lazy('risks:list')
    form_class = RiskForm


@method_decorator(staff_member_required, name='dispatch')
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


@method_decorator(staff_member_required, name='dispatch')
class CreateCauseView(CreateView):
    model = Cause
    success_url = reverse_lazy('risks:cause_list')
    form_class = CauseForm


@method_decorator(staff_member_required, name='dispatch')
class UpdateCauseView(UpdateView):
    model = Cause
    template_name_suffix = "_update_form"
    form_class = CauseForm

    def get_success_url(self):
        return reverse_lazy('risks:cause', args=[self.object.id])


# EFFECT VIEWS
class EffectListView(ListView):
    model = Effect


class EffectDetailView(DetailView):
    model = Effect


@method_decorator(staff_member_required, name='dispatch')
class CreateEffectView(CreateView):
    model = Effect
    success_url = reverse_lazy('risks:effect_list')
    form_class = EffectForm


@method_decorator(staff_member_required, name='dispatch')
class UpdateEffectView(UpdateView):
    model = Effect
    template_name_suffix = "_update_form"
    form_class = EffectForm

    def get_success_url(self):
        return reverse_lazy('risks:effect', args=[self.object.id])
