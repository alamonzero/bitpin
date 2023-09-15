from django.db.models import Count, Avg, Case, When, IntegerField
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed

from article.models import Article
from article.serializers import ArticleListSerializer


class ArticleListView(ListAPIView):
    authentication_classes = (BasicAuthentication,)
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Article.custom_objects.all().annotate(
                number_of_users=Count("ratings__user"),
                average_score=Avg("ratings__score"),
                user_score=Case(
                    When(ratings__user=user, then='ratings__score'),
                    default=None,
                    output_field=IntegerField()
                ),
            )
        raise AuthenticationFailed()
