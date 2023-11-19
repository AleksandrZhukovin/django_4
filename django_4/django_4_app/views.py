from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm, RegistrationForm, LoginForm
from django.contrib.auhth.models import User
from django.contrib.auth import authenticate, login


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/registration')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def home(request):
    projects = Project.objects.all()
    user = request.user
    context = {'user': user, 'projeccts': projects}
    return render(request, 'home.html', context)


def project(request, **kwargs):
    p = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['deadline']
            status = form.cleaned_data['status']
            priority = form.cleaned_data['priority']
            task = Task(name=name, deadline=deadline, status=status, priority=priority, project=p)
            task.save()
            return redirect(f'/project/{p.id}')
    else:
        form = TaskForm()
        tasks = Task.objects.filter(project=p)
        return render(request, 'project.html', {'project': p, 'tasks': tasks, 'form': form})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = Project(name=name)
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        context = {'form': form}
        return render(request, 'project_create.html', context)


# def page1(request):
#     if request.method == 'POST':
#         data = request.POST
#         name = data['name']
#         surname = data['surname']
#         age = data['age']
#         dir = Director(name=name, surname=surname, age=age)
#         dir.save()
#     return render(request, 'page1.html')
#
# def page2(request):
#     dirs = Director.objects.all()
#
#     return render(request, 'page2.html', {'data': dirs})
#
# # CRUD - Create Read Update Delete
# def page3(request):
#     if request.method == 'POST':
#         form = FilmForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['title']
#             genre = form.cleaned_data['genre']
#             year = form.cleaned_data['year']
#             dir = Director.objects.get(id=1)
#             film = Film(title=name, genre=genre, year=year, director=dir)
#             film.save()
#             return render(request, 'page3.html', {'form': form})
#     else:
#         form = FilmForm()
#         return render(request, 'page3.html', {'form': form})
#
#
# def book_create(request):
#     if request.method == 'POST':
#         form = BookForm1(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             year = form.cleaned_data['year']
#             author = form.cleaned_data['author']
#             book = Book(title=title, year=year, author=author)
#             book.save()
#             return redirect('/create_post')
#     else:
#         form = BookForm1()
#         return render(request, 'page3.html', {'form': form})
#
#
# def  form_page(request):
#     form = LoginForm()
#     return render(request, 'page3.html', {'form': form})
