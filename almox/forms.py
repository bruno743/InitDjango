from django import forms

from .models import Comp

class CompForm(forms.ModelForm):

    class Meta:
        model = Comp
        fields = (
            'comp_name',
            'comp_mod',
            'comp_loc', 
            'comp_ean',
            'comp_nserial',
            'comp_status',
            'comp_estado',
            'comp_addobs'
            )