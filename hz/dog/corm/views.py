from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ContactForm
from .models import Team, Comment, Contact, Product


class BaseMixin:
    context = {
        'facebook': 'https://facebook.com',
        'fontawesome': 'https://fontawesome.com',
        'google': 'https://google.com',
        'linkedin': 'https://www.linkedin.com',
    }


class IndexTemplateView(BaseMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data()
        context['team'] = Team.objects.all()
        context['com'] = Comment.objects.all()
        context['product'] = Product.objects.all()
        context.update(self.context)
        return context

    def get_queryset(self):
        return [
            Team.objects.filter(is_published=True),
            Comment.objects.filter(is_published=True),
            Product.objects.filter(is_published=True)
        ]


class AboutTemplateView(BaseMixin, ListView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context['teams'] = Team.objects.all()
        context['com'] = Comment.objects.all()
        context.update(self.context)
        return context

    def get_queryset(self):
        return [
            Team.objects.filter(is_published=True),
            Comment.objects.filter(is_published=True),
        ]


class BlogTemplateView(BaseMixin, TemplateView):
    template_name = 'main/blog.html'


class ContactCreateView(BaseMixin, CreateView):
    template_name = 'main/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class ServiceTemplateView(BaseMixin, TemplateView):
    template_name = 'main/service.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceTemplateView, self).get_context_data()
        context['teams'] = Team.objects.all()
        context['com'] = Comment.objects.all()
        context['product'] = Product.objects.all()
        context.update(self.context)
        return context

    def get_queryset(self):
        return [
            Team.objects.filter(is_published=True),
            Comment.objects.filter(is_published=True),
            Product.objects.filter(is_published=True)
        ]


class PagesTemplateView(BaseMixin, TemplateView):
    template_name = 'main/elements.html'
