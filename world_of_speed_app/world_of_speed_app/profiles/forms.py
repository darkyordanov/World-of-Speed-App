from django import forms

from world_of_speed_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        
        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }
        
class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = 'readonly'
        self.fields['email'].widget.attrs['readonly'] = 'readonly'
        self.fields['age'].widget.attrs['readonly'] = 'readonly'
        self.fields['password'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')

        
        