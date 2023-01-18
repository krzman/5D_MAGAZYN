"""storage_5d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from storage_5d_pr.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('workers_add/', WorkersAdd.as_view(), name='workers_add'),
    path('workers_list/', WrokersList.as_view(), name='workers_list'),
    path('tools_add/', ToolAdd.as_view(), name='tools_add'),
    path('tools_list/', ToolList.as_view(), name='tools_list'),
    re_path(r'^construction/(?P<construction_id>\d+)/$', ConstructionView.as_view(), name='construction'),
    re_path(r'^workers_edit/(?P<pk>\d+)/$', WorkersUpdate.as_view(), name='workers_update'),
    re_path(r'^tools-edit/(?P<pk>\d+)/$', ToolsUpdate.as_view(), name='tools_update'),
    path('history/', HistoryView.as_view(), name='history'),
    re_path(r'^history/(?P<tool_nr>\d+\D\d+)/$', HistorySingle.as_view(), name='history_single'),
]
