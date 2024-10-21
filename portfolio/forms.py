from django import forms
from.models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Make sure this points to your correct model
        fields = ['name', 'email', 'phone', 'subject', 'message']  # Include 'message' here
