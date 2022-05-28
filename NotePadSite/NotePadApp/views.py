from django.shortcuts import render, redirect
from django.contrib import messages

## import todo form and models

from .forms import NotePadAppForm
from .models import NotePadApp


###############################################

def index(request):
    item_list = NotePadApp.objects.order_by("-date")
    if request.method == "POST":
        form = NotePadAppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('NotePadApp')
    form = NotePadAppForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "NotePad",
    }
    return render(request, 'index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = NotePadApp.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('NotePadApp')