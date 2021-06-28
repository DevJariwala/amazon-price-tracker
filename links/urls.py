from django.urls import path,include
from . import views

urlpatterns = [
  
    path('',views.home_view,name="home_view"),
    path('delete/<int:item_id>/',views.delete_item,name="delete_item"),
    path('update/',views.update_prices,name='update_prices'),
]