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


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'message',
        )