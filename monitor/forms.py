from django import forms
from .models import Criterion

class CriterionForm(forms.ModelForm):
    class Meta:
        model = Criterion
        fields = ['parameter', 'operator', 'threshold', 'frequency']
        widgets = {
            'threshold': forms.TextInput(attrs={'placeholder': 'number of decimals'}),
        }


