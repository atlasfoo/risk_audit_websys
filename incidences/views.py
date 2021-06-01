from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView

from incidences.forms import IncidenceForm
from incidences.models import Incidence


class IncidencesListView(ListView):
    model = Incidence


class IncidencesDetailView(DetailView):
    model = Incidence


@method_decorator(login_required, name='dispatch')
class CreateIncidenceView(CreateView):
    model = Incidence
    success_url = reverse_lazy('controls:list')
    form_class = IncidenceForm

    def get_initial(self):
        """Set the user as user in session"""
        return{
            'user': self.request.user.id
        }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
