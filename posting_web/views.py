from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Product, Rating, Comment
from django.shortcuts import render
from .models import Item


def home(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('posting:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['title', 'description']


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('posting:product_list')


class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    template_name = 'rating_form.html'
    fields = ['rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posting:product_detail', args=[self.kwargs['pk']])


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_form.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posting:product_detail', args=[self.kwargs['pk']])
