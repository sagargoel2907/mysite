from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class MyView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request=request, template_name='solo/form.html')

    def post(self, request):
        field1 = request.POST['field1']
        field2 = request.POST['field2']
        return render(request=request, template_name='solo/form.html', context={'result': f"{field1} {field2}".casefold()})
