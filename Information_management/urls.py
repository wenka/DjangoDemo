"""Information_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login),
    # url(r'^login_verify/$',views.Login_verify),
    url(r'^index/', views.Index, name='index'),
    url(r'^', views.Index, name='index'),
    url(r'^logout/', views.Logout),
    url(r'^all_score_info/', views.All_Score_Info, name='all_score_info'),
    url(r'^regist1/$', views.Regist1),
    url(r'^register/$', views.Regist),
    # url(r'^base/',views.base),
    url(r'^user_info/', views.User_Info),
    url(r'^set_password/', views.Set_Password),
    url(r'^score/', views.get_score, name='score'),
    url(r'^add_score/$', views.Add_Score, name='add_score'),
    url(r'^add_score1/', views.Add_Score1),
    # url(r'^delete_score/(?P<userID_id>[0-9]+)$',views.Delete_Score,name='delete_score1'),
    url(r'^delete_score/(?P<pk>[0-9]+)$', views.Delete_Score),
    url(r'^update_score/(?P<pk>[0-9]+)$', views.Update_Score),
    url(r'^update_score1/', views.Update_Score1),
]
