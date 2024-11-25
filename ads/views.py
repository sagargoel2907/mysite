from django.db.utils import IntegrityError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, reverse
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.models import Ad, Comment, Fav
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.forms import AdForm, CommentForm
from django.http import HttpResponse
# Create your views here.


class AdListView(View):
    model = Ad
    template_name = 'ads/ad_list.html'

    def get(self, request):
        ads = Ad.objects.all()
        rows = request.user.favorite_ads.values('id') if request.user.is_authenticated else []
        favorites = [row['id'] for row in rows]
        ctx = {'ads': ads, 'favorites': favorites}
        return render(request=request, template_name=self.template_name, context=ctx)


class AdDetailView(View):
    model = Ad
    template_name = 'ads/ad_detail.html'

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        comment_form = CommentForm()
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        ctx = {'ad': ad, 'commentForm': comment_form, 'comments': comments}
        return render(request=request, template_name=self.template_name, context=ctx)


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
    response['Content-Type'] = 'image/jpeg'
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        comment = Comment(
            text=request.POST['comment'], ad=ad, owner=request.user)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

    def get(self, request, pk):
        return redirect(f'{reverse("ads:ad_detail", args=[pk])}#comment_form')


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'ads/comment_confirm_delete.html'

    def get_success_url(self):
        ad = self.object.ad
        return reverse("ads:ad_detail", args=[ad.id])

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav(ad=ad, user=request.user)
            fav.save()
        except IntegrityError:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(ad=ad, user=request.user)
            fav.delete()
        except Fav.DoesNotExist:
            pass
        return HttpResponse()
