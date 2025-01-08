from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('book/', views.book_data, name="book"),
    path('todo/', views.todo_list, name="todo_list"),
    path('todo/create/', views.create_todo, name="create_todo"),  # Corrected pattern
    path('todo/complete_todo/<int:id>/', views.complete_todo, name="complete_todo"),
    path('todo/delete_todo/<int:id>/', views.delete_todo, name="delete_todo"),
]