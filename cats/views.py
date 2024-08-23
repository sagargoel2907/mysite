from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views import View
from django.urls import reverse_lazy
from cats.models import Breed, Cat
# Create your views here.


class BreedView(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html'


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    template_name = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'


class CatView(LoginRequiredMixin, View):
    template_name = 'cats/cat_list.html'

    def get(self, request):
        breed_count = Breed.objects.count()
        cat_list = Cat.objects.all()
        return render(request=request,
                      template_name=self.template_name, context={
                          "breed_count": breed_count,
                          "cat_list": cat_list,
                      })


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    template_name = 'cats/cat_confirm_delete.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'
