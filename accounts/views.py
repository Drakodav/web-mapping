from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext, gettext_lazy as _


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'title': _('Profile'), 'pretitle': _('Manage your profile')})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
