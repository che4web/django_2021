from django import forms
from sudentapp.models import Dish

class DishSearchForm(forms.Form):
    name = forms.CharField(max_length=255,)

class DishForm(forms.Form):
    name = forms.CharField(max_length=255,)
    slug = forms.CharField(max_length=255)
    recipe = forms.CharField()
    cooking_time = forms.IntegerField()

class BootstrapModel(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        '''
         добавим все inputan class form-control
         '''
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class DishFormModel(BootstrapModel):
    class Meta:
        model=Dish
        fields ="__all__"

