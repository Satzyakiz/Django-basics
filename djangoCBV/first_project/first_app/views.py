from django.urls import reverse_lazy
from django.shortcuts import render
#from django.http import HttpResponse
# from first_app.models import Topic,Webpage,AccessRecord
from first_app.models import School,Student
#the above line can also be written as:
#from . import School,Student
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)  #--CBV
# Create your views here.

# def index(request):
#     my_dict = {'insert_me': " Hello I am from views.py. This is wonderful. "}
#     return render(request,'first_app/index.html', context = my_dict)

# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records': webpages_list}
#     return render(request,'first_app/index.html',context=date_dict)

class CBV(View):
    """docstring forCBV."""
    def get(self,request):
        return HttpResponse("Class Based Views are cool !")
class IndexView(TemplateView):
    template_name = 'first_app/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic Injection'
        return context
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    #if context_object_name was not written
    #return school_list; if name was Satan, it would return satan_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'first_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = School
class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = School
class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("first_app:list")
