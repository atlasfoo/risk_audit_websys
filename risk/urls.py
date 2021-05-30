from django.urls import path

from risk.views import *

risk_urls = ([
    path('', RiskListView.as_view(), name='list'),
    path('<int:pk>', RiskDetailView.as_view(), name='risk'),
    path('create/', CreateRiskView.as_view(), name='create'),
    path('update/<int:pk>', UpdateRiskView.as_view(), name='update'),
    path('cause/', CauseListView.as_view(), name='cause_list'),
    path('cause/<int:pk>', CauseDetailView.as_view(), name='cause'),
    path('cause/create/', CreateCauseView.as_view(), name='create_cause'),
    path('cause/update/<int:pk>', UpdateCauseView.as_view(), name='update_cause'),
], 'risks')
