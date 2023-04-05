from django.urls import re_path
from . import views

urlpatterns = [
    
    re_path(r'^cart/$', views.cart, name="cart"),
    re_path(r'^checkout/$', views.checkout, name="checkout"),
    re_path(r'^update_item/$', views.updateItem, name="update_item"),
    re_path(r'^process_order/$', views.processOrder, name="process_order"),    
    re_path(r'^$', views.store, name="store"),
]