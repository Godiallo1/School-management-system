from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.student, name="students"),
    path('new_student/', views.new_student, name="new_student"),
    path('update_student/<int:pk>', views.update_student, name="update_student"),
    path('delete_student/<int:pk>', views.delete_stud, name="delete_student")
]