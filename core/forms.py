from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    '''
    Form per aggiunta cibo
    '''
    class Meta:
        model = Food
        fields = ['name', 'quantity', 'calories', 'totalfat', 'saturatedfat', 'carbs', 'cholestorol'
                  'sodium', 'fiber', 'sugars', 'protein']

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'