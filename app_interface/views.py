from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_interface.models import Interface
from app_interface.forms import InterfaceForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    # ALL INTERFACES:
    query = request.GET.get('q')
    if not query:
        query = ''
    if query == '':
        all_interfaces = Interface.objects.all()
    else:
        all_interfaces = Interface.objects.filter(Q(name__icontains=query))

    # Pagination:
    paginator_all_interfaces = Paginator(all_interfaces, 10)
    page = request.GET.get('pg')
    all_interfaces = paginator_all_interfaces.get_page(page)

    return render(request, 'index.html', {'interfaces': all_interfaces})
    

def view_interface(request, interface_id):
    interface_obj = Interface.objects.get(pk=interface_id)
    return render(request, 'view.html', {'interface_obj': interface_obj})


@login_required
def my_interfaces(request):
    if request.method == "POST":
        form = InterfaceForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, ("New interface is successfully added!"))
        else: 
            messages.error(request, ("New interface couldn't be saved!"))
        return redirect('my_interfaces')
    else:
        # MY INTERFACES:
        query = request.GET.get('q')
        if not query:
            query = ''
        if query == '':
            my_interfaces = Interface.objects.filter(owner=request.user)
        else:
            my_interfaces = Interface.objects.filter(Q(name__icontains=query)).filter(owner=request.user)

        # Pagination:
        paginator_my_interfaces = Paginator(my_interfaces, 10)
        page = request.GET.get('pg')
        my_interfaces = paginator_my_interfaces.get_page(page)

        return render(request, 'my_interfaces.html', {'interfaces': my_interfaces})
    
      
@login_required
def delete_interface(request, interface_id):
    interface = Interface.objects.get(pk=interface_id)
    if interface.owner == request.user:
        interface.delete()
        messages.success(request, (f"Interface '{interface.name}' is successfully deleted!"))
    else:
        messages.error(request, ("Access restricted, you are NOT allowed!"))

    return redirect('my_interfaces')


@login_required
def edit_interface(request, interface_id):
    if request.method == "POST":
        interface = Interface.objects.get(pk=interface_id)
        form = InterfaceForm(request.POST or None, instance = interface)
        if form.is_valid():
            form.save()

        messages.success(request, (f"Interface '{interface.name}' is successfully updated!"))
        return redirect('my_interfaces')
    else:
        interface_obj = Interface.objects.get(pk=interface_id)
        return render(request, 'edit.html', {'interface_obj': interface_obj})


@login_required
def complete_interface(request, interface_id):
    interface = Interface.objects.get(pk=interface_id)
    if interface.owner == request.user:
        interface.isOwned = True
        interface.save()
        messages.success(request, (f"Interface '{interface.name}' is successfully completed"))
    else:
        messages.error(request, ("Access restricted, you are NOT allowed!"))

    return redirect('my_interfaces')


@login_required
def pending_interface(request, interface_id):
    interface = Interface.objects.get(pk=interface_id)
    if interface.owner == request.user:
        interface.isOwned = False
        interface.save()
        messages.success(request, (f"Interface '{interface.name}' is opened again"))
    else:
        messages.error(request, ("Access restricted, you are NOT allowed!"))

    return redirect('my_interfaces')

