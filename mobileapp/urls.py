"""Mobiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from mobileapp.views import add_new_mobile,view_mobile,edit_mobile,delete_mobile,home,buyer_details,view_orders,\
        registration,signin,signout,adminpage,edit_order,cancel_order,search,filter
from django.urls import path

urlpatterns = [
        path('add',add_new_mobile,name='add_mobile'),
        path('view/<int:id>',view_mobile,name='view'),
        path('edit/<int:id>',edit_mobile,name='edit'),
        path('delete/<int:id>',delete_mobile,name='delete'),
        path('',home,name='home'),
        path('buyer/<int:id>',buyer_details,name='buyer'),
        path('orders',view_orders,name='order'),
        path("registration",registration,name='registraion'),
        path('signin',signin,name='signin'),
        path('signout',signout,name='signout'),
        path('admin',adminpage,name='admin'),
        path('editorder/<int:id>',edit_order,name='editorder'),
        path('cancelorder/<int:id>',cancel_order,name='cancelorder'),
        path('search',search,name='search'),
        path('filter',filter,name='filter'),

]

