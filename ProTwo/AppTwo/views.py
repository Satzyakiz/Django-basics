from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def index(request):
    return HttpResponse("<em> My Second App </em>")

def view(request):
    var = {'insert_me': "Woo HOO" }
    return render(request,'AppTwo/index.html', context = var)

def users(request):
    info = User.objects.order_by('email')
    details = {'users':info}
    return render(request,'AppTwo/users.html',context=details)
