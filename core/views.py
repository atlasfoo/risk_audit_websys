import operator

from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from controls.models import Control
from incidences.models import Incidence
from risk.models import Risk


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        # Most frequent risk
        risks = Risk.objects.all()
        risk_probs = {}
        for risk in risks:
            risk_probs[risk.name] = (Incidence.objects.filter(
                risk_id=risk.id).count() / Incidence.objects.all().count()) * 100
        freq_risk = max(risk_probs.items(), key=operator.itemgetter(1))

        # Most effective control
        controls = Control.objects.all()
        control_probs = {}
        for control in controls:
            incidences = Incidence.objects.filter(risk_id=control.risk.id)
            control_probs[control.name] = (incidences.filter(
                controls__id=control.id).count() / incidences.count()) * 100
        effect_control = max(control_probs.items(), key=operator.itemgetter(1))

        # Risk presented (GRAPH)
        risks = list(Incidence.objects.all().values('risk__name').annotate(total=Count('risk_id')).order_by('total'))
        print(risks)

        # Total economic loss
        tot_loss=0
        incidences = Incidence.objects.all()
        for incidence in incidences:
            tot_loss += sum(el.economic_loss for el in incidence.effects.all())

        return render(request, self.template_name, {'freq_risk_name': freq_risk[0], 'freq_risk_prob': freq_risk[1],
                                                    'effect_control_name': effect_control[0],
                                                    'effect_control_eff': effect_control[1],
                                                    'risks': risks, 'tot_loss': tot_loss})
