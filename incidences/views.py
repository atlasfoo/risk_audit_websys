from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView

from incidences.models import Incidence


class IncidencesListView(ListView):
    model = Incidence


class IncidencesDetailView(DetailView):
    model = Incidence


@method_decorator(login_required, name='dispatch')
class CreateControlView(CreateView):
    model = Incidence
    success_url = reverse_lazy('controls:list')

    def get_initial(self):
        """Set the user as user in session"""
        return{
            'user': self.request.user
        }
