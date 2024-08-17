from django.db import models
from django.db.models import QuerySet, Count


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self) -> QuerySet:
        return (
            self
            .annotate(articles_count=Count("article"))  # It should be `article_set` (when no relation_name set)
            .order_by("-articles_count", "email")       # but Django maps it to `article`

        )
