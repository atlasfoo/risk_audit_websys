from django.urls import path

from controls.views import *


controls_urls = ([
                 path('', ControlListView.as_view(), name='list'),
                 path('<int:pk>', ControlDetailView.as_view(), name='control'),
                 path('create/', CreateControlView.as_view(), name='create'),
                 path('update/<int:pk>', UpdateControlView.as_view(), name='update'),
             ], 'risks')