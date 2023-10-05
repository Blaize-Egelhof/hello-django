from django.shortcuts import render , redirect
from .models import Item
# Create your views here.

#Remeber that when we create things here , they are useless ! They need to be referenced , so as an exmaple in urls's create a URL , ensure that url triggers a function mentioned below here, make sure you import , and make sure the trigger to run all this is set in the HTML


def get_todo_list(request):  #Request refers to the clients git/post request
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context) # returning the Items models objects as a variable to manipulate later in the todo_list.html


def add_item(request):  
        if request.method == 'POST' : 
            name= request.POST.get('item_name')
            done= 'done' in request.POST
            Item.objects.create(name=name , done = done )
            print("Item created successfully")
            return redirect('get_todo_list')
        return render(request, 'todo/add_item.html')