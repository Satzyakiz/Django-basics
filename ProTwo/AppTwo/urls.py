from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from AppTwo import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('',views.view,name='view'),
    path('users/',views.users,name='users')
    #path('admin/', admin.site.urls),
]
