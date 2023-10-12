from django import forms
from .models import Ticket, Comment


class CreateTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'priority',
            'title',
            'description',
            'message',
            'image',
        )

