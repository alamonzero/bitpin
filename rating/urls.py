from rest_framework.urls import path

from rating.views import CreateRatingView

urlpatterns = [
    path('', CreateRatingView.as_view(), name="rate_an_article"),
]
