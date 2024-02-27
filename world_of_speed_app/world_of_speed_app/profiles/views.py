from django.urls import reverse_lazy
from django.views.generic import \
    DetailView, UpdateView, DeleteView
from django.db.models import Sum

from world_of_speed_app.profiles.models import Profile
from world_of_speed_app.common.helpers import get_profile
from world_of_speed_app.profiles.forms import EditProfileForm


class DetailProfileView(DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'
    
    def get_object(self, queryset=None):
        return get_profile()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        
        total_price = profile.car_set.aggregate(total_price=Sum('price'))['total_price']
        total_price = total_price if total_price is not None else 0
        formatted_total_price = "{:.3f}".format(total_price)
        
        context['total_price'] = formatted_total_price
        
        return context
    

class EditProfileView(UpdateView):
    template_name = 'profiles/profile-edit.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('profile_details')
    
    def get_object(self, queryset=None):
        return get_profile()
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
    
    
class DeleteProfileView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        return get_profile() 
    

