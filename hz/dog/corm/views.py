from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Team

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
        context.update(self.context)
        return context

    def get_queryset(self):
        return [
            Team.objects.filter(is_published=True),
        ]


class AboutTemplateView(BaseMixin,TemplateView):
    template_name = 'main/about.html'




# class WorkScheduleListView(ListView):
#     template_name = 'main/store.html'
#     context_object_name = 'week'
#     model = WorkSchedule
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['weekday'] = datetime.today().isoweekday() + 6
#         return context