from .models import Memo


def get_memos_separate_user(user, book) -> dict:
    memos = Memo.get_by_book(book)
    target_memo = None
    del_targets = []

    for i in range(len(memos)):
        if memos[i].user.pk is user.pk:
            target_memo = memos[i]
            del_targets.append(i)

    for del_target in del_targets:
        del memos[del_target]

    result = {
        'target_memo': target_memo,
        'memos': memos,
    }
    return result


def new_memo(user, book, memo_text: str) -> bool:
    memo = Memo()
    memo.user = user
    memo.book = book
    memo.text = memo_text
    memo.save()
    return True
