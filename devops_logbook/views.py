from tempfile import template
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views import View
from .models import Task, Tag
from .forms import TaskForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView


class Index(View):
    
    # template_name = 'index.html'

    def post(self, request):
        if request.method == 'POST':
                form = TaskForm(request.POST)
                if form.is_valid():
                    if 'tags' not in request.POST:
                        copy = request.POST.copy()
                        copy['tags'] = '-'
                        f = form.save(commit=False)
                        f.tags = copy['tags']
                        f.time = now().__format__("%Y-%m-%d - %H:%M")
                        form.save()
                    else: 
                        f = form.save(commit=False)
                        f.tags = request.POST.getlist('tags')
                        f.time = now().__format__("%Y-%m-%d - %H:%M")
                        form.save()
        return redirect('/')
    
    def get(self, request):
        model = Task.objects.all().order_by('-time').values()
        tags = Tag.objects.values().all()
        form = TaskForm()
        con = {'context': list(model), 'form': form, 'tags': list(tags)}
        return render(request, "index.html", con)
        



# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             user = authenticate(request, username=clean_data['username'], password=clean_data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return main(request)
#                 else:
#                     return HttpResponse('Disabled Account!')
#             else:
#                 return HttpResponse('Invalid login!')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})