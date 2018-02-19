from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from submodules import logger
from constants import ROOT_NAME
from modules.profile.forms import NewUserForm, UpdateUserForm
from modules.profile import service as profile_sv
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from submodules.helper import simple_upload_file, \
    flatten_dict_only_one_element as flatten


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy(ROOT_NAME)
    template_name = 'registration/signup.html'
    success_messages = [
        'Welcome to Webook app! \
        It succeeded in user registration! \
        Let\'s immediately read the book together now!',
    ]

    # バリデーションを通った時に実行されるメソッド
    # Http Responseを必ず返さなければならない仕様
    def form_valid(self, form):
        """新規登録してホーム画面で歓迎する"""

        post_data = flatten(self.request.POST)
        # ユーザー生成する
        user_fields = ('username', 'password1',)
        profile_fields = ('join_at',)
        user_data = {}
        profile_data = {}

        for field in user_fields:
            user_data[field] = post_data[field]

        for field in profile_fields:
            profile_data[field] = post_data[field]

        user, created = User.objects.get_or_create(
            username=user_data['username'])
        if created:
            user.set_password(user_data['password1'])
            user.save()
            profile_sv.new_profile(user, profile_data['join_at'])

        for success_message in self.success_messages:
            messages.success(self.request, success_message)

        logger.info('success to signup.')

        # 自動ログインする
        user = authenticate(self.request,
                            username=post_data['username'],
                            password=post_data['password1'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            logger.warning('failed auto login in after registration.')
            return HttpResponseRedirect(reverse_lazy('accounts:login'))


@require_GET
def get(request):
    return render(request, app_name + '/update.html', {'form': UpdateUserForm})


@require_POST
def post(request):
    """プロフィールを更新する"""
    data = flatten(request.POST)

    if 'thumbnail_url' in request.FILES:
        data['thumbnail_url'] = simple_upload_file(
            request.FILES['thumbnail_url'])

    update_params = {}
    if 'thumbnail_url' in data:
        update_params['thumbnail_url'] = data['thumbnail_url']

    if 'join_at' in data:
        update_params['join_at'] = data['join_at']

    if len(update_params) > 0:
        profile_sv.update_profile(request.user, update_params)

    messages.success(request, 'プロフィールを更新しました')
    return redirect(app_name + ':update', pk=orderbook.book.pk)
