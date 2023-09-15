from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from rating.models import Rating


class CreateRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ("article", "score")

    def get_user(self):
        request = self.context.get("request")
        if request:
            return request.user
        return None

    def validate(self, data):
        user = self.get_user()
        if not user or not user.is_authenticated:
            raise ValidationError("In order to set rating, you must login first")
        return super(CreateRatingSerializer, self).validate(data)

    def create(self, validated_data):
        user = self.get_user()
        try:
            record = Rating.custom_objects.get(user=user)
            record.score = validated_data["score"]
            record.save()
        except ObjectDoesNotExist:
            record = Rating.objects.create(user=user, **validated_data)
        return record


