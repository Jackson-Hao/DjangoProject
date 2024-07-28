from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    from .models import MyModel
    object_list = MyModel.objects.all()
    context = {'object_list': object_list}
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pwd']
        hobby = request.POST['haihao']
        age = request.POST['age']
        if password == '123':
            return render(request, 'login.html', {'error_msg': 
            '密码正确，您是{}，密码为{}，爱好是{}，年龄是{}'.format(username,password,hobby,age)})
        else:
            return render(request, 'login.html', {'error_msg': '密码错误！！！'})
    return render(request, 'login.html')