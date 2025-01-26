from django import forms


class DusterTimeForm(forms.Form):
    duster_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'], label="Новый дастер")
