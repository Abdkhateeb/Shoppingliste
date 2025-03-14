from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Item
from django.contrib import messages

# ✅ Login-Ansicht
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('item_list')
    return render(request, 'shoppinglist/login.html')

# ✅ Logout-Ansicht
def user_logout(request):
    logout(request)
    return redirect('login')

# ✅ Einkaufsliste anzeigen & neues Item hinzufügen
@login_required
def item_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        if name and quantity:
            Item.objects.create(name=name, quantity=int(quantity), user=request.user)
        return redirect('item_list')
    
    items = Item.objects.filter(user=request.user)
    return render(request, 'shoppinglist/item_list.html', {'items': items})

# ✅ Ein Item als "gekauft" markieren
@login_required
def purchase_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    item.purchased = True
    item.save()
    return redirect('item_list')

# ✅ Item löschen
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    item.delete()
    return redirect('item_list')


def user_logout(request):
    logout(request)
    messages.success(request, "Du wurdest erfolgreich ausgeloggt.")
    return redirect('login')
