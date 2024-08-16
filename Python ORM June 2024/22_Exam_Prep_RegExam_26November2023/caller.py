import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, Avg
from main_app.models import Author, Article


# 4. Django Queries I

def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ''

    query = Q()
    query_by_name = Q(full_name__icontains=search_name)
    query_by_email = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = query_by_name & query_by_email
    else:
        query = query_by_email if search_name is None else query_by_name

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ''

    return '\n'.join([
        f'Author: {a.full_name}, email: {a.email}, status: {"Banned" if a.is_banned else "Not Banned"}'
        for a in authors
    ])


def get_top_publisher() -> str:
    top_publisher = (
        Author.objects
        .get_authors_by_article_count()
        .order_by('-articles_count', 'email')
        .first()
    )

    if not top_publisher or not top_publisher.articles_count:
        return ""

    return f"Top Author: {top_publisher.full_name} with {top_publisher.articles_count} published articles."


def get_top_reviewer() -> str:
    top_reviewer = (
        Author.objects
        .annotate(num_of_reviews=Count('reviews'))
        .order_by('-num_of_reviews', 'email')
        .first()
    )

    if not top_reviewer or not top_reviewer.num_of_reviews:
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.num_of_reviews} published reviews."


# 5. Django Queries II

def get_latest_article() -> str:
    latest_article = (
        Article.objects
        .prefetch_related('authors', 'reviews')
        .annotate(avg_rating=Avg('reviews__rating'), num_of_reviews=Count('reviews'))
        .order_by('-published_on')
        .first()
    )

    if not latest_article:
        return ""

    authors = ', '.join(author.full_name for author in latest_article.authors.all().order_by('full_name'))

    avg_rating = f"{latest_article.avg_rating:.2f}" if latest_article.avg_rating is not None else "0.00"

    return (
        f"The latest article is: {latest_article.title}. "
        f"Authors: {authors}. "
        f"Reviewed: {latest_article.num_of_reviews} times. "
        f"Average Rating: {avg_rating}."
    )


def get_top_rated_article() -> str:
    top_rated_article = (
        Article.objects
        .annotate(avg_rating=Avg('reviews__rating'), num_reviews=Count('reviews'))
        .filter(num_reviews__gt=0)
        .order_by('-avg_rating', 'title')
        .first()
    )

    if not top_rated_article:
        return ""

    return f"The top-rated article is: {top_rated_article.title}, " \
           f"with an average rating of {top_rated_article.avg_rating:.2f}, " \
           f"reviewed {top_rated_article.num_reviews} times."


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    try:
        author = Author.objects.get(email=email)
    except Author.DoesNotExist:
        return "No authors banned."

    num_reviews = author.reviews.count()
    author.reviews.all().delete()
    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."
