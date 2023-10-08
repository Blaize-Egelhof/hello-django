from django.shortcuts import render , redirect , get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.

#Remeber that when we create things here , they are useless ! They need to be referenced , so as an exmaple in urls's create a URL , ensure that url triggers a function mentioned below here, make sure you import , and make sure the trigger to run all this is set in the HTML


def get_todo_list(request):  #Request refers to the clients git/post request
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context) # returning the Items models objects as a variable to manipulate later in the todo_list.html


def add_item(request):  
        if request.method == 'POST': 
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('get_todo_list')

        form = ItemForm()
        context = {
            'form': form
        }

        return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    item = get_object_or_404(Item,id=item_id)
    if request.method == 'POST': 
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context ) 

def toggle_item(request,item_id):
    item = get_object_or_404(Item,id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')

def delete_item(request,item_id):
    item = get_object_or_404(Item,id=item_id)
    item.delete()
    return redirect('get_todo_list')


