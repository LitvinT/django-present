from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ContactForm
from .models import Team, Comment, Contact


class BaseMixin:
    context = {
        'facebook': 'https://facebook.com',
        'fontawesome': 'https://fontawesome.com',
        'google': 'https://google.com',
        'linkedin': 'https://www.linkedin.com',
    }


class IndexTemplateView(BaseMixin,TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data()
        context['team'] = Team.objects.all()
        context['com'] = Comment.objects.all()
        context.update(self.context)
        return context

    def get_queryset(self):
        return [
            Team.objects.filter(is_published=True),
            Comment.objects.filter(is_published=True),
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


class ContactTemplateView(BaseMixin, TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contact_form'] = ContactForm()
        return context

    def post(self, request: HttpRequest):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request)

