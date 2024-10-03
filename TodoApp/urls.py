from django.urls import path
from . import views

urlpatterns = [
    path('home',views.HomeView.as_view(),name='home'),
    path('add',views.AddTask.as_view(),name='add'),
    path('list',views.TaskList.as_view(),name='list'),
    path('edit/<int:pk>',views.TaskUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>',views.TaskDeleteView.as_view(),name='delete'),
    path('detail/<int:pk>',views.TaskDetailView.as_view(),name='detail'),
    path('update_status',views.TaskCompleteView.as_view(),name='update_status'),
]
