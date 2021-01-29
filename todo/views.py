from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def home(request):
    context = {'todos': Todo.objects.all()}
    return render(request, 'todo/home.html', context)


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/home.html'
    context_object_name = 'todos'
    ordering = ['-date_posted']


class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['content', 'state']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ['state', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'todo/about.html')
