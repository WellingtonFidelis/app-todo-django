"""todo_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo.views import (
    TodosView, 
    AddTodoView, 
    UpdateTodoView, 
    DeleteTodoView,
    EditTodoView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodosView, name="todos"),
    path("add-todo/", AddTodoView, name="add-todo"),
    path("update-todo/<int:pk>/", UpdateTodoView, name="update-todo"),
    path("edit-todo/<int:pk>/", EditTodoView, name="edit-todo"),
    path("delete-todo/<int:pk>/", DeleteTodoView, name="delete-todo"),
]
