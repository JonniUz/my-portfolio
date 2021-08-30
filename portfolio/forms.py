from django import forms
from django.forms import TextInput, Textarea

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            "full_name": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name",
                    "type": "text",
                    "placeholder": "Enter your name...",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "type": "email",
                    "placeholder": "name@example.com",
                }
            ),
            "phone_num": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "phone",
                    "type": "tel",
                    "placeholder": "(123) 456-7890",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "form-control",
                    "id": "message",
                    "type": "text",
                    "placeholder": "Enter your message here...",
                    "style": "height: 10rem"
                }
            )
        }
