from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        """バリデーションを通った時"""
        form = UserCreationForm(self.request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(self.request, new_user)
        return HttpResponseRedirect('/')
