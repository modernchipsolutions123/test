"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/',views.display),
    path('nam/<str:name>',views.name),

     path('det/',views.details),
     path('stu/<str:name>/<int:age>',views.stu_dis),

     path('emp/<int:emp_id>/<str:emp_name>',views.emp_det),

     path('add/',views.add),


]
