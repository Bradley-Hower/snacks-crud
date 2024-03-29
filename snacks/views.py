from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  
class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack
  
class SnackCreateView(CreateView):
  template_name = 'snack_create.html'
  model = Snack
  fields = 'name', 'purchaser', 'rating' #'__all__'
  
  
class SnackUpdateView(UpdateView):
  template_name = 'snack_update.html'
  model = Snack
  fields = '__all__'
  
class SnackDeleteView(DeleteView):
  template_name = 'snack_delete.html'
  model = Snack
  success_url = reverse_lazy('snack_list')