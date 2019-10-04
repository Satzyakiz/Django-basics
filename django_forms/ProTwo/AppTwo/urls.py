from django.urls import path
from AppTwo import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('',views.view,name='view'),
    path('users/',views.users,name='users')
    #path('admin/', admin.site.urls),
]
