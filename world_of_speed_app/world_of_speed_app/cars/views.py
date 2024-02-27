from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import \
    CreateView, ListView, DetailView, UpdateView, DeleteView

from world_of_speed_app.cars.models import Car
from world_of_speed_app.common.helpers import get_profile
from world_of_speed_app.cars.forms import CarForm
from world_of_speed_app.common.readonly_mixin import ReadonlyMixin
    

class CatalogCarsView(ListView):
    queryset = Car.objects.all()
    template_name = 'cars/catalogue.html'
    

class CreateCarView(CreateView):
    queryset = Car.objects.all()
    form_class = CarForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')
    
    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)
    

class DetailCarView(DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'


class EditCarView(UpdateView):
    queryset = Car.objects.all()
    form_class = CarForm
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue')
    
    
class DeleteCarView(ReadonlyMixin, DeleteView):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')
    
    form_class = modelform_factory(
        Car,
        fields=(
            'type', 'model', 'year', 'image_url', 'price',
        )
    )
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs