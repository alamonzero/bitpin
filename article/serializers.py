from rest_framework import serializers


class ArticleListSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    number_of_users = serializers.SerializerMethodField()
    average_score = serializers.SerializerMethodField()
    user_score = serializers.SerializerMethodField()

    def get_title(self, record):
        return record.title

    def get_number_of_users(self, record):
        return record.number_of_users

    def get_average_score(self, record):
        return record.average_score

    def get_user_score(self, record):
        return record.user_score
