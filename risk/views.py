from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from incidences.models import Incidence
from risk.forms import RiskForm, CauseForm, EffectForm
from risk.models import Risk, Cause, Effect


# RISK VIEWS
class RiskListView(ListView):
    model = Risk


class RiskDetailView(DetailView):
    model = Risk

    def get_context_data(self, **kwargs):
        context = super(RiskDetailView, self).get_context_data(**kwargs)
        prob = (Incidence.objects.filter(risk_id=self.object.id).count() / Incidence.objects.all().count()) * 100
        context['risk_prob'] = prob
        return context


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

    def get_context_data(self, **kwargs):
        context = super(CauseDetailView, self).get_context_data(**kwargs)
        tot = 0
        for inc in Incidence.objects.all():
            tot += inc.causes.all().count()
        prob = (Incidence.objects.filter(causes__id=self.object.id).count() / tot) * 100
        context['cause_prob'] = prob
        return context


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

    def get_context_data(self, **kwargs):
        context = super(EffectDetailView, self).get_context_data(**kwargs)
        tot = 0
        for inc in Incidence.objects.all():
            tot += inc.effects.all().count()
        prob = (Incidence.objects.filter(effects__id=self.object.id).count() / tot) * 100
        context['effect_prob'] = prob
        return context


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
