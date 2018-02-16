from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from modules.profile.forms import UpdateUserForm
from modules.profile import service as profile_sv
from django.views.decorators.http import require_GET, require_POST
from submodules.helper import simple_upload_file, \
    flatten_dict_only_one_element as flatten

app_name = 'accounts'


@require_GET
def get(request):
    return render(request, app_name + '/update.html', {'form': UpdateUserForm})


@require_POST
def post(request):
    """プロフィールを更新する"""
    data = flatten(request.POST)
    user = User.objects.get(pk=request.user.pk)

    if 'thumbnail_url' in request.FILES:
        data['thumbnail_url'] = simple_upload_file(
            request.FILES['thumbnail_url'])

    if 'thumbnail_url' in data:
        user.profile.thumbnail_url = data['thumbnail_url']

    if 'join_at' in data:
        user.profile.join_at = data['join_at']
    user.profile.save()

    messages.success(request, 'プロフィールを更新しました')
    return redirect(app_name + ':update', pk=orderbook.book.pk)
