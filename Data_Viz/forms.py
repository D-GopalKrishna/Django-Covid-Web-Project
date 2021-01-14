from django import forms
from .models import SendMsg

class ContactForm(forms.ModelForm):
    class Meta:
        model = SendMsg
        fields = '__all__'            # Can also put ['name', 'email', 'message', 'time']
        widgets = {
            'message': forms.Textarea()
        }
