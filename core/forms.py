from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact

        fields=("__all__")
        widgets={
            "name": forms.TextInput(attrs={'placeholder':"first_name",'class': "form-control"})
        }

