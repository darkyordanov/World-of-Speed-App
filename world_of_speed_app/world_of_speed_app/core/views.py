from django.shortcuts import redirect, render

from world_of_speed_app.profiles.forms import CreateProfileForm
from world_of_speed_app.common.helpers import get_profile


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
        return redirect('catalogue')
    
    context = {
            'form': form,
            'no_profile_nav': True,
    }
    
    return render(request, 'profiles/profile-create.html', context)
        


def index(request):
    no_profile_nav = False
    profile = get_profile()
    
    if profile is None:
        no_profile_nav = True
    
    context = {
        'no_profile_nav': no_profile_nav,
    }
    
    return render(request, 'core/index.html', context)
