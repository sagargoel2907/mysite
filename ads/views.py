from django.shortcuts import render
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.models import Ad
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.forms import AdForm
from django.http import HttpResponse
# Create your views here.


class AdListView(OwnerListView):
    model = Ad
    # template_name = 'ads/ad_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad
    # template_name = 'ads/ad_detail.html'


# class AdCreateView(OwnerCreateView):
#     model = Ad
#     # template_name = 'ads/ad_create.html'
#     fields = ['title', 'price', 'text']


class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request):
        form = AdForm()
        ctx = {'form': form}
        return render(request=request, template_name=self.template_name, context=ctx)

    def post(self, request):
        form = AdForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request=request, template_name=self.template_name, context=ctx)

        ad = form.save(commit=False)
        ad.owner = request.user
        ad.save()
        return redirect(self.success_url)


# class AdUpdateView(OwnerUpdateView):
#     model = Ad
#     # template_name = 'ads/ad_update.html'
#     fields = ['title', 'price', 'text']
#     # exclude = ['owner', 'created_at', 'updated_at']


class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = AdForm(instance=ad)
        ctx = {'form': form}
        return render(request=request, template_name=self.template_name, context=ctx)

    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=request.user)
        form = AdForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request=request, template_name=self.template_name, context=ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.picture.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response
