from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# NoTE with router, you dont need the url path, instead use the way below
# For router viewse, Also do not put .as_view() even though it is also a class
router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee') # NOTE THAT if using modelViewset, you dont need to put BASENAME


urlpatterns = [
    path('students/', views.studentsView), # this api endpoint is to fetch all the students
    path('student/<int:pk>/', views.studentDetailView), # this api endpoint handle pull individual put and delete request

    # path('employees/', views.Employees.as_view()),#this is an example of class based view
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view())

    path('', include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),#this is an example of class based view
    path('comments/', views.CommentsView.as_view()),#this is an example of class based view

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view())

 ]