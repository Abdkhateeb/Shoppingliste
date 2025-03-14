from django.urls import path
from .views import item_list, purchase_item, delete_item
from .views import user_login, user_logout
urlpatterns = [
    path('', item_list, name='item_list'),
    path('purchase/<int:item_id>/', purchase_item, name='purchase_item'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
]
