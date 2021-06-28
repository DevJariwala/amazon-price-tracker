from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AddLinkForm
from .models import Link


# Create your views here.

# def temp(request):
#     return render(request,'links/main.html')

def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Oops ... couldn't get the name or price "
        except:
            error = "Oops ... something went wrong"

    form = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()

    if items_no>0:
        discount_list = []
        for item in qs:
            if(item.old_price > item.current_price):
                discount_list.append(item)
            no_discounted = len(discount_list)

    context={
        'qs':qs,
        'items_no':items_no,
        'no_discounted':no_discounted,
        'form':form,
        'error':error,
    }


    return render(request,'links/main.html',context)



def delete_item(request,item_id):
    # print(todo_id)
    Link.objects.get(id=item_id).delete()
    # models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


def update_prices(request):
    qs=Link.objects.all()
    for link in qs:
        link.save()
    
    return HttpResponseRedirect("/")


