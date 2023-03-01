from django.urls import path

from .views import IndexTemplateView, AboutTemplateView, BlogTemplateView, ContactTemplateView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('blog/', BlogTemplateView.as_view(), name='blog'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),

]

