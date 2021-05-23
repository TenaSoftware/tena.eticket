from collections import defaultdict

from django import forms
from django.db.utils import ProgrammingError

from core.models import Route

class SearchRouteForm(forms.Form):
    qs = Route.objects.values_list('start_station','destination')
    STATIONS = defaultdict(lambda: False)
    try:
        for start, end in qs:
            print("\n\n\t\tHERE\n\n")
            if not STATIONS[start]:
                STATIONS[start] = start
            if not STATIONS[end]:
                STATIONS[end] = end
    except ProgrammingError:
        pass
    start_station = forms.ChoiceField(choices=STATIONS.items())
    destination = forms.ChoiceField(choices=STATIONS.items())
    date = forms.DateField(widget=forms.SelectDateWidget())
