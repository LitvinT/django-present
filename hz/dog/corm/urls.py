from django.urls import path

from .views import IndexTemplateView, AboutTemplateView, BlogTemplateView, ContactCreateView, ServiceTemplateView, \
    PagesTemplateView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('blog/', BlogTemplateView.as_view(), name='blog'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('service/', ServiceTemplateView.as_view(), name='services'),
    path('elements/', PagesTemplateView.as_view(), name='elements')

]

