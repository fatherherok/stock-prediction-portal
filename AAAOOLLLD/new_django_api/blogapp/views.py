from django.shortcuts import render
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer, BlogSerializer, UpdateUserProfileSerializer
from rest_framework.pagination import PageNumberPagination

class BlogListPagination(PageNumberPagination):
    page_size = 1




@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    paginator = BlogListPagination()
    paginated_blogs = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(paginated_blogs, many=True)
    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # return serialized user data (password is write_only so not included)
        return Response(UserRegistrationSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    # serializer = UpdateUserProfileSerializer(user, data=request.data)
    serializer = UpdateUserProfileSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        # return serialized user data (password is write_only so not included)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user = request.user
    serializer = BlogSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        # pass author as kwarg so serializer.create gets it
        blog = serializer.save(author=user)
        return Response(BlogSerializer(blog).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog(request, pk): #pk means primary key
    user = request.user
    blog = Blog.objects.get(id=pk)
    if blog.author != user:
        return Response({"error": "You are not the author of this blog"}, status=status.HTTP_403_FORBIDDEN) 
    serializer =  BlogSerializer(blog, data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_blog(request, pk): #pk means primary key
    user = request.user
    blog = Blog.objects.get(id=pk)
    if blog.author != user:
        return Response({"error": "You are not the author of this blog"}, status=status.HTTP_403_FORBIDDEN) 
    blog.delete()
    return Response({"message":"Blog deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)