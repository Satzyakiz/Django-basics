from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = 'first_app'
#The above line make the below in HTML possible
# href="{% url "first_app:list"%}
urlpatterns = [
    path('abc/',views.CBV.as_view(), name ='index'),
    path('',views.SchoolListView.as_view(),name='list'),
    #name makes it possible to understand first_app:list(url) in line 7(commented)
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>[-\w]+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>[-\w]+)/$',views.SchoolDeleteView.as_view(),name='delete'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),

]
