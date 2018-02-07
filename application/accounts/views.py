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
    success_messages = [
        'Welcome to Webook app!',
        'It succeeded in user registration!',
        'Let\'s immediately read the book together now!',
    ]

    # バリデーションを通った時に実行されるメソッド
    # Http Responseを必ず返さなければならない仕様
    def form_valid(self, form):
        """
        新規登録してホーム画面で歓迎する

        [issue]
        以下の登録・自動ログインなどを切り離したいどれも
        requestを利用するライブラリを多様している弊害で
        requestがserviceやcomponentにまで侵食してしまう課題がある
        **もし良いやり方があったら、提案してほしい**
        """

        # ユーザー生成する
        form = UserCreationForm(self.request.POST)

        # get_success_urlでself.objectにformが入っている前提でコードが書かれている
        self.object = form.save()

        for success_message in self.success_messages:
            messages.success(self.request, success_message)

        Log.info('success to signup.')

        # 自動ログインする
        user = authenticate(self.request,
                            username=self.request.POST['username'],
                            password=self.request.POST['password1'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            Log.info('failed auto login in after registration.')
            return HttpResponseRedirect(reverse_lazy('login'))
