from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from autos.models import Make, Auto
from autos.forms import MakeForm
from django.urls import reverse_lazy
# Create your views here.


class MainView(LoginRequiredMixin, View):
    template_name = "autos/auto_list.html"

    def get(self, request):
        make_count = Make.objects.count()
        auto_list = Auto.objects.all()
        return render(request=request, template_name=self.template_name,
                      context={"auto_list": auto_list,
                               "make_count": make_count
                               }
                      )


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        m = Make.objects.all()
        ctx = {"make_list": m}
        return render(request=request, template_name="autos/make_list.html",
                      context=ctx)


class MakeCreate(LoginRequiredMixin, View):
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:auto_list")

    def get(self, request):
        form = MakeForm()
        return render(request=request, template_name=self.template, context={
            "form": form
        })

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request=request, template_name=self.template,
                          context={"form": form})
        _ = form.save()
        return redirect(to=self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:auto_list")

    def get(self, request, pk):
        m = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=m)
        return render(request=request, template_name=self.template,
                      context={"form": form})

    def post(self, request, pk):
        m = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=m)
        if not form.is_valid():
            return render(request=request, template_name=self.template,
                          context={"form": form})
        form.save()
        return redirect(to=self.success_url)


class MakeDelete(LoginRequiredMixin, View):
    model = Make
    template = "autos/make_confirm_delete.html"
    success_url = reverse_lazy("autos:auto_list")

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        return render(request=request, template_name=self.template,
                      context={"make": make})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(to=self.success_url)


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')
    template_name = "autos/auto_form.html"


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')
    template_name = "autos/auto_form.html"


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')
    template_name = "autos/make_confirm_delete.html"
