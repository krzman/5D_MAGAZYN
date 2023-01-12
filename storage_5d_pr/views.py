from django.shortcuts import render
from django.views import View
from storage_5d_pr.templates import *


# Create your views here.

class Main(View):
    def get(self, request):
        return render(request, 'main.html')
