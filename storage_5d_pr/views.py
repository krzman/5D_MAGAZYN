# Import django module
from django.shortcuts import render
from django.views import View

# Import project module
from storage_5d_pr.templates import *
from storage_5d_pr.forms import *


# Create your views here.

class Main(View):
    def get(self, request):
        form = FormLogin()
        context = {'form': form}
        return render(request, 'main.html', context=context)
