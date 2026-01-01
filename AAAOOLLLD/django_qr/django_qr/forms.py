from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50,
        label='Restaurant Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter restaurant name'
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='Menu Url',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL if the of the online menu'
        })
        )