from django.views import View
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy,reverse
from django.views import generic
from . import models
from . import forms
from  django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetConfirmView
import time


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'main.html'
    
class AddTask(LoginRequiredMixin,generic.CreateView):
    model = models.Task
    fields = ['title','description','priority','category']
    template_name = 'addTask.html'
    success_url = '/todo/list'
    context_object_name= 'task'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] ='Add a new' 
        context["action"] ='Add Task' 
        return context
    
    
    
class TaskList(LoginRequiredMixin,generic.ListView):
    model =  models.Task
    template_name = 'tasksList.html'
    context_object_name= 'tasks'
  
    def get_queryset(self):
        self.sort_priority = self.request.GET.get('sort_priority', 'l_to_h')
        self.sort_id = self.request.GET.get('sort_id','descending')
        
        if self.sort_id == 'ascending' and self.sort_priority =='__':
            return  models.Task.objects.order_by('id')
        elif self.sort_id ==  'descending' and self.sort_priority =='__':
            return models.Task.objects.order_by('-id')
        
        elif self.sort_priority =='l_to_h' and self.sort_id == 'ascending':
            return models.Task.objects.order_by('priority_order','id')
        elif self.sort_priority == 'h_to_l' and self.sort_id == 'ascending':
            return models.Task.objects.order_by('-priority_order','id')
        
        elif self.sort_priority =='l_to_h' and self.sort_id == 'descending':
            return models.Task.objects.order_by('priority_order','-id')
        elif self.sort_priority == 'h_to_l' and self.sort_id == 'descending':
            return models.Task.objects.order_by('-priority_order','-id')
        else:
            return models.Task.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sort_priority"] = self.sort_priority
        context["sort_id"] = self.sort_id
        
        return context
    
    
class TaskUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = models.Task
    fields = ['title','description','priority','category']
    template_name = "addTask.html"
    success_url = '/todo/list'
    context_object_name= 'task'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["name"] = 'Edit'
        context["action"] ='Edit Task' 
        
        return context
    
class TaskDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = models.Task
    template_name = "delete.html"
    success_url = '/todo/list'
    
class TaskDetailView(LoginRequiredMixin,generic.DetailView):
    model = models.Task
    template_name = "detail.html"

class TaskCompleteView(LoginRequiredMixin,generic.View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.getlist('complete')
        models.Task.objects.update(completed = False)
        models.Task.objects.filter(id__in=task_id).update(completed = True)
        return redirect('list')
    
class Register(generic.CreateView):
    model = User
    form_class= forms.RegisterForm
    success_url='/accounts/login'
    template_name ='registration/register.html'

class ChangePassword(PasswordChangeView):
    form_class = forms.PasswordChange  # Ensure this matches your custom form class
    success_url = '/accounts/password-change/done/'  # Use `reverse_lazy` for URL resolution
    template_name = 'registration/password_change.html'
    
class ChangePasswordDone(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/password_change_done.html')

    def post(self, request, *args, **kwargs):
        return redirect(reverse('login'))

class ResetPassword(PasswordResetView):
    html_email_template_name = 'registration/password_reset_email.html'
    form_class =forms.PasswordReset
    template_name = 'registration/password_reset.html'
    success_url = '/accounts/password-reset/done/'
    
class ResetPasswordConfirm(PasswordResetConfirmView):
    
    form_class = forms.PasswordResetConfirm
    success_url = '/accounts/reset/complete/'
    template_name = 'registration/password_reset_confrim.html'
    
class  ResetPasswordDone(View):
    def get(self,request,*args, **kwargs):
        return render(request,'registration/password_reset_done.html')
    def post(self,request,*args, **kwargs):
        return redirect(reverse('login'))
    
class  ResetDone(View):
    def get(self,request,*args, **kwargs):
        return render(request,'registration/reset_done.html')
    def post(self,request,*args, **kwargs):
        return redirect(reverse('login'))
        


    
    

    
