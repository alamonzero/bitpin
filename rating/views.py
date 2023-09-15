from rest_framework.generics import CreateAPIView
from rest_framework.authentication import BasicAuthentication

from rating.serializers import CreateRatingSerializer


class CreateRatingView(CreateAPIView):

    authentication_classes = (BasicAuthentication, )
    serializer_class = CreateRatingSerializer
