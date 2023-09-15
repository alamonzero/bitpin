from django.db import models
from django.contrib.auth import get_user_model

from base.models import BaseModel, CustomBaseManager


class CustomArticleManager(CustomBaseManager):
    def get_queryset(self):
        return super(CustomArticleManager, self).get_queryset().prefetch_related("ratings")


class Article(BaseModel):
    slug = models.SlugField(null=False, blank=False, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=False, blank=False)
    auther = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return f"{self.title} By {self.auther}"

    class Meta:
        unique_together = ('title', 'auther')
