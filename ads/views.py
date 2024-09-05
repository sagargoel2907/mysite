from django.shortcuts import render
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.models import Ad

# Create your views here.


class AdListView(OwnerListView):
    model = Ad
    # template_name = 'ads/ad_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad
    # template_name = 'ads/ad_detail.html'


class AdCreateView(OwnerCreateView):
    model = Ad
    # template_name = 'ads/ad_create.html'
    fields = ['title', 'price', 'text']


class AdUpdateView(OwnerCreateView):
    model = Ad
    # template_name = 'ads/ad_update.html'
    fields = ['title', 'price', 'text']
    fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad
