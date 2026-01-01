from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password", "bio", "profile_picture", "facebook", "youtube", "instagram", "twitter"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user_model = get_user_model()
        new_user = user_model.objects.create_user(
            email=validated_data.get("email"),
            username=validated_data.get("username"),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            password=validated_data.get("password"),
        )
        return new_user


class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
        ]


class BlogSerializer(serializers.ModelSerializer):
    # make author read-only so clients can't impersonate other users
    author = SimpleAuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "author",
            "category",
            "content",
            "featured_image",
            "published_date",
            "created",
            "updated",
            "is_draft",
        ]
        read_only_fields = ("slug", "created", "updated", "published_date")

    # allow the view to pass 'author' when saving, or fallback to request.user if present in context
    def create(self, validated_data, author=None):
        if author is None:
            request = self.context.get("request", None)
            if request and hasattr(request, "user"):
                author = request.user
        validated_data["author"] = author
        return super().create(validated_data)
