from rest_framework import serializers
from .models import FutureMessage, Photo, Video
from accounts.serializers import UserSerializer


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "image", "uploaded_at"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "video", "uploaded_at"]


class FutureMessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    photo = PhotoSerializer(many=True, read_only=True)
    video = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = FutureMessage
        fields = [
            "id",
            "title",
            "message",
            "delivery_date",
            "is_opened",
            "created_by",
            "reflection_questions",
            "mood",
            "life_stage",
            "photo",
            "video",
        ]
