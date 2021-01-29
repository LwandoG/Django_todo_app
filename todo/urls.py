from django.urls import path
from . import views
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-home'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
    path('todo/new/', TodoCreateView.as_view(), name='todo-create'),
    path('about/', views.about, name='about')
]
