from django.urls import path

from risk.views import RiskListView, RiskDetailView, CreateRiskView, UpdateRiskView

risk_urls = ([
    path('', RiskListView.as_view(), name='list'),
    path('<int:pk>', RiskDetailView.as_view(), name='risk'),
    path('create/', CreateRiskView.as_view(), name='create'),
    path('update/<int:pk>', UpdateRiskView.as_view(), name='update'),
], 'risks')
