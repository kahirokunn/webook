from .models import Review


def get_reviews_separate_user(user, book) -> dict:
    reviews = Review.get_by_book(book)
    target_review = None

    for i in range(len(reviews)):
        if reviews[i].user.pk is user.pk:
            target_review = reviews[i]
            del reviews[i]
            break

    result = {'target_review': target_review,
              'reviews': reviews, }
    return result


def new_review(user, book, review_text: str, star: int) -> bool:
    review = Review()
    review.user = user
    review.book = book
    review.text = review_text
    review.star = star
    review.save()
    return True
