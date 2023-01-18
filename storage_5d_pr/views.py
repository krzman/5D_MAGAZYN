# Import django module
import http.client

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Import project module
from storage_5d_pr.forms import *
from storage_5d_pr.models import *


# Helper function
def history_add(login_user=None, tool_nr=None, tool_type=None, tool_producer=None, workers=None, construction=None,
                comment=None):
    data = {
        'user': login_user,
        'tool_nr': tool_nr,
        'tool_type': tool_type,
        'tool_producer': tool_producer,
        'workers': workers,
        'construction': construction,
        'comment': comment,
    }
    History.objects.create(**data)


# Create your views here.

# Main page / login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            form = FormLogin()
            context = {'form': form}
            return render(request, 'login.html', context=context)

    def post(self, request):
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
        context = {
            'mess': 'Wprowadzono złe dane',
            'form': form,
        }
        return render(request, 'login.html', context=context)


# Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# ---------------------------------------------------------------------------
#           CREATE

# Page add workers
class WorkersAdd(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Workers
    fields = ['name', 'surname', 'phone', 'company']
    template_name = 'workers-add.html'
    success_url = reverse_lazy('workers_list')

    # Add taks to history
    def form_valid(self, form):
        comment = 'Dodano'
        user = self.request.user
        object = form.save(commit=False)
        history_add(user, workers=object, comment=comment)
        return super().form_valid(form)


# Page add tool
class ToolAdd(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = FormToolsAdd
    template_name = 'tools-add.html'
    success_url = reverse_lazy('tools_list')

    # Add taks to history
    def form_valid(self, form):
        comment = 'Dodano'
        user = self.request.user
        object = form.save(commit=False)
        history_add(user, object.nr, object.type, object.producer, object.workers, object.construction, comment)
        return super().form_valid(form)


# --------------------------------------------------------------------------------
#           LIST

# Page list all workers
class WrokersList(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        workers = Workers.objects.all()
        context = {
            'workers': workers
        }
        return render(request, 'workers-list.html', context=context)


# Page list all tools
class ToolList(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        tools = Tools.objects.all()
        context = {
            'tools': tools
        }
        return render(request, 'tools-list.html', context=context)


# Page single construtcion with tools
class ConstructionView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, construction_id):
        construction = Construction.objects.get(id=construction_id)
        tools = Tools.objects.all().filter(construction_id=construction_id)
        context = {
            'construction': construction,
            'tools': tools
        }
        return render(request, 'construction.html', context=context)


# --------------------------------------------------------------------------------------
#           UPDATE

class WorkersUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Workers
    fields = '__all__'
    template_name = 'workers-edit.html'
    success_url = reverse_lazy('workers_list')

    # Add taks to history
    def form_valid(self, form):
        user = self.request.user
        object = form.save(commit=False)
        if object.active:
            comment = 'Aktywny'
        else:
            comment = 'Nieaktywny'
        history_add(user, workers=object, comment=comment)
        return super().form_valid(form)


class ToolsUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Tools
    fields = '__all__'
    template_name = 'tools-edit.html'
    success_url = reverse_lazy('tools_list')

    # Add taks to history
    def form_valid(self, form):
        comment = 'Edycja'
        user = self.request.user
        object = form.save(commit=False)
        history_add(user, object.nr, object.type, object.producer, object.workers, object.construction, comment)
        return super().form_valid(form)


# -------------------------------------------------------------------------------------
#           HISTORY
class HistoryView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        history = History.objects.all()
        context = {
            'history': history
        }
        return render(request, 'history.html', context=context)


class HistorySingle(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, tool_nr):
        history = History.objects.all().filter(tool_nr=tool_nr)
        single = True
        context = {
            'history': history,
            'single': single
        }
        return render(request, 'history.html', context=context)
