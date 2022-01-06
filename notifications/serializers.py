from django.db import models
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "type",
            "text",
            "link",
            "seen",
            "image",
            "created_at",
        ]
        read_only_fields = ("id", "created_at")
