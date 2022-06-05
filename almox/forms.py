from django import forms

from .models import Comp, Loc, Mod

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
class ModForm(forms.ModelForm):

    class Meta:
        model = Mod
        fields = (
            'mod_brand',
            'mod_model',
            'mod_description'
        )

class LocForm(forms.ModelForm):

    class Meta:
        model = Loc
        fields = (
            'loc_name',
            'loc_addrss'
        )
