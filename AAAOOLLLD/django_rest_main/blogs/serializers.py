from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments =  CommentSerializer(many=True, read_only=True) # NOTETHAT refer to  the related_name='comments' in the models.py WHERE WE configure the nested serializers
    class Meta:
        model = Blog
        fields = '__all__'