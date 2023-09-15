from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from base.models import CustomBaseManager, BaseModel
from article.models import Article

User = get_user_model()


class CustomRatingManager(CustomBaseManager):
    def get_queryset(self) -> models.query.QuerySet:
        return super().get_queryset().select_related("user", "article")


class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="ratings")
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    custom_objects = CustomRatingManager()

    def __str__(self):
        return f"{self.user.username} gave score: {self.score} to article: {self.article.title} by {self.article.author}"

    class Meta:
        unique_together = ('user', 'article')
