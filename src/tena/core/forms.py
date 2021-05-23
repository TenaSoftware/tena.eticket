from django import forms

class SearchRouteForm(forms.Form):
    START_STATION = (("A", "!@"),("B", "@#$"))
    DESTINATION = (("A", "!@"),("B", "@#$"))
    start_station = forms.ChoiceField(choices=START_STATION)
    destination = forms.ChoiceField(choices=DESTINATION)
    date = forms.DateField(widget=forms.SelectDateWidget())
