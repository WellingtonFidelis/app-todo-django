from django.shortcuts import render

# Create your views here.

def TodoView(request):
  return render(
    request,
    "todo/todo.html"
  )