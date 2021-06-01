from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView

from incidences.forms import IncidenceForm, IncidenceControlForm
from incidences.models import Incidence


class IncidencesListView(ListView):
    model = Incidence


class IncidencesDetailView(DetailView):
    model = Incidence


@method_decorator(login_required, name='dispatch')
class CreateIncidenceView(CreateView):
    model = Incidence
    form_class = IncidenceForm

    def get_initial(self):
        """Set the user as user in session"""
        return{
            'user': self.request.user.id
        }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('controls:list') + f'?incidence_id{self.object.id}'
