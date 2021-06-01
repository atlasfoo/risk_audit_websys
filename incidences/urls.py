from django.urls import path

from incidences.views import *

incidences_urls = ([
                     path('', IncidencesListView.as_view(), name='list'),
                     path('<int:pk>', IncidencesDetailView.as_view(), name='incidence'),
                     path('create/', CreateIncidenceView.as_view(), name='create'),
                 ], 'incidences')