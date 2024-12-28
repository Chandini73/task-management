import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import ImageUploadForm
from .models import Category, Task,ImageUpload
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils import timezone


# Create your views here.
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        n = request.POST['uname']
        p = request.POST['upass']
        # print(n)
        # print(p)
        u = authenticate(username=n, password=p)
        # print(u)
        if u is not None:
            login(request, u)
            return redirect('/category_list')
        else:
            context = {'errmsg': 'Invalid UserName and Password'}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        context = {}
        n = request.POST['uname']
        p = request.POST['upass']
        cp = request.POST['ucpass']
        if n == '' or p == '' or cp == '':
            context['errmsg'] = 'Field can not be NULL'
            return render(request, 'register.html', context)
        elif len(p) < 8:
            context['errmsg'] = 'Password must be 8 Characters'
            return render(request, 'register.html', context)
        elif p != cp:
            context['errmsg'] = 'Password and Confirm password must be same'
            return render(request, 'register.html', context)
        else:
            try:
                u = User.objects.create(username=n, email=n)
                u.set_password(p)
                u.save()
                context['success'] = 'User Created Successfully'
                return render(request, 'register.html', context)
            except Exception:
                context['errmsg'] = 'User Already Exists, Please Login..!'
                return render(request, 'register.html', context)


def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()
    return redirect(reverse('category_list.html'))


def create_task(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        print(f"Title: {title}, Start Date: {start_date}, End Date: {end_date}, Priority: {priority}")

        task = Task.objects.create(
            title=title,
            start_date=start_date,
            end_date=end_date,
            priority=priority,
            description=description,

        )

        # Redirect to the task list page
        return redirect('category_list')
    else:
        categories = Category.objects.all()
        return render(request, 'create_task.html', {'categories': categories})


def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        # Update task fields based on form data
        task.title = request.POST.get('title')
        task.start_date = request.POST.get('start_date')
        task.end_date = request.POST.get('end_date')
        task.priority = request.POST.get('priority')
        task.description = request.POST.get('description')
        task.save()
        return redirect('category_list')
    else:
        # Render update task page with task data
        return render(request, 'update_task.html', {'task': task})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'create_category.html')


def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')


def category_task(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'category_task.html', {'category': category})


def task_chart(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'task_chart.html', {'tasks': tasks})


def home(request):
    # template = loader.get_template('home.html')
    return render(request, 'home.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_success')  # Redirect to a success page or render some template
    else:
        form = ImageUploadForm()
    images = ImageUpload.objects.all()
    return render(request, 'upload_image.html', {'form': form, 'images': images})


def image_success(request):
    return render(request, 'image_success.html')