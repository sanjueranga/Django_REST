from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello_user),
    path('all/',views.get_all),
    path('create/',views.create_user),
    path('edit/<int:user_id>', views.manage_user), 
    path('delete/<int:user_id>',views.manage_user)
]
