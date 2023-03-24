from django.contrib.auth.views import LoginView, TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm
from ..corm.models import Blog


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/index.html'
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'registration/index.html'


def posts_list(request):
    search_query = request.Get.get('search', '')

    if search_query:
        posts = Blog.objects.filter(title_icontains=search_query)
    else:
        posts = Blog.objects.all()
