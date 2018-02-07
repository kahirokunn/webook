from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from application.helper import Log


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        """バリデーションを通った時"""
        # ユーザー登録をする
        form = UserCreationForm(self.request.POST)

        # get_success_urlでself.objectにformが入っている前提でコードが書かれている
        self.object = form.save()
        messages.success(self.request, "Welcome to Webook app!")
        messages.success(self.request, "It succeeded in user registration!")
        messages.success(self.request, "Let's immediately read the book together now!")
        Log.info('success to signup.')

        # 自動ログインする
        user = authenticate(self.request,
                            username=self.request.POST['username'],
                            password=self.request.POST['password1'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            Log.info('i don\'t no why, failed login.')
            return HttpResponseRedirect(reverse_lazy('login'))
