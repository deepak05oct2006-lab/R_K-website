from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email (optional)', 'class': 'form-control'}),
            'service': forms.TextInput(attrs={'placeholder': 'Service needed', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your project...', 'class': 'form-control', 'rows': 4}),
        }
