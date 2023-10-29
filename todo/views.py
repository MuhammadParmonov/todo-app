from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Todo
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        return render(request, "index.html", {"todos": todos})
    
class CreateTodoView(LoginRequiredMixin, View):
    def post(self, request):
        body = request.POST.get("body")
        # categor_id = request.POST.get("category")
        # category = Category.objects.filter(id=categor_id).first()
        if body:
            Todo.objects.create(user=request.user, body=body)
        return redirect("index")
    
class ActionView(LoginRequiredMixin, View):
    def post(self, request, todo_id, action):
        todo = Todo.objects.filter(id=todo_id, user=request.user).first
        if todo:
            if action == 'done':
                todo.done = True
                todo.save()
            elif action == 'delete':
                todo.delete()
        return redirect("index")