from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import BookForm
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(request):
    context = {}
    return render(request, "myApp/home.html",context)

def book_data(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['bk_name']
            number = form.cleaned_data['bk_number']
            book1 = Book.objects.create(bk_name = name, 
            bk_number = number)
            book1.save()
    form = BookForm()
    return render(request, "myApp/book.html",{'form':form})



#create a todo list
def todo_list(request):
    todos = Todo.objects.order_by('-id')
    return render(request, 'myApp/index.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        if not description:
            return render(request, "todo/create.html",{"error": "Description is required"})
        Todo.objects.create(title=title, description=description)
        return redirect('/todo')
    return render(request, "todo/create.html")

def complete_todo(request,id):
   todo = get_object_or_404(Todo, id=id)
   todo.completed = True 
   todo.save()
   return redirect('todo_list')

def delete_todo(request,id):
   todo = get_object_or_404(Todo, id=id)
   todo.delete()
   return redirect('todo_list')