from django.urls import path

from .views import IndexTemplateView, AboutTemplateView, BlogCreateView, ContactCreateView, ServiceTemplateView, \
    PagesTemplateView, SingleTemplateView, SearchListView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('blog/', BlogCreateView.as_view(), name='blog'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('service/', ServiceTemplateView.as_view(), name='services'),
    path('elements/', PagesTemplateView.as_view(), name='elements'),
    path('single-blog/', SingleTemplateView.as_view(), name='single-blog'),
    path('search/', SearchListView.as_view(), name='search'),





]

