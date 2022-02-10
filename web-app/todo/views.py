from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import TodoModel
# Create your views here.


def TodosView(request):
    todos = TodoModel.objects.all()
    context = {
        "todos": todos
    }
    return render(request, "todo/todos.html", context)


@require_http_methods(["POST"])
def AddTodoView(request):
    todo = None
    title = request.POST.get("title", "")

    if title:
        todo = TodoModel.objects.create(
            title=title
        )

    context = {
        "todo": todo
    }
    return render(request, "todo/partials/todo.html", context)

@require_http_methods(["PUT"])
def UpdateTodoView(request, pk):
    todo = TodoModel.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    context = {
        "todo": todo
    }
    return render(request, "todo/partials/todo.html", context)

@require_http_methods(["DELETE"])
def DeleteTodoView(request, pk):
    todo = TodoModel.objects.get(pk=pk)
    todo.is_done = True
    todo.delete()
    context = {
        "todo": todo
    }
    return HttpResponse()