from django import forms

from world_of_speed_app.cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
        widgets = {
            'image_url': forms.TextInput(attrs={
                'placeholder': 'https://...',
            })
        }