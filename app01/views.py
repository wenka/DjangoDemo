from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# from django.contrib.auth import authenticate
from django.contrib import auth
from django import forms
from app01.models import User_Info, Score_Info
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
import pymysql
import json


# Create your views here.
class UserForm(forms.Form):
    # id=forms.CharField(label='ID')
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')


class ChangeForm(forms.Form):
    username = forms.CharField(label='用户名')
    old_password = forms.CharField(label='原密码', widget=forms.PasswordInput())
    new_password = forms.CharField(label='新密码', widget=forms.PasswordInput())
    repeat_password = forms.CharField(label='确认密码', widget=forms.PasswordInput())


class ScoreForm(forms.Form):
    java = forms.FloatField(label='Java成绩')
    python = forms.FloatField(label='Python成绩')


# @csrf_protect
# def Login(request):
#     username=request.POST.get('username')
#     context={'username':username}
#     return render(request,'login.html',context)
#
# @csrf_protect
# def Login_verify(request):
#     # request.GET
#     # username=request.GET['username']
#     # password=request.GET['password']
#     username = request.POST['username']
#     password = request.POST['password']
#     context={'username':username}
#     conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='information_management')
#     cursor=conn.cursor()
#     effect_row=cursor.execute('select * from app01_user_info')
#     row_3=cursor.fetchall()
#     for i in range(effect_row):
#         if username==row_3[i][1] and password==row_3[i][2]:
#             return render(request,'index.html',context)
#         else:
#             i+=1
#     cursor.close()
#     conn.close()
#     if i>=effect_row:
#         return render(request,'login.html',context)

# def Login(request):
#     username=request.POST.get('username')
#     password=request.POST.get('password')
#     context={'username':username,'password':password}
#     return render(request,'login.html',context)
#
# def Login_verify(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         userinfo={'username':username,'password':password}
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             # return HttpResponseRedirect('index.html')
#             return HttpResponse('111111')
#         else:
#             # return render(request,'login.html',userinfo)
#             return HttpResponse('aaaaaaaa')

@csrf_protect
def Login(request):
    uf = UserForm(request.POST)
    if uf.is_valid():
        username = uf.cleaned_data['username']
        password = uf.cleaned_data['password']
        user = User_Info.objects.filter(username=username)
        request.session['username'] = username
        if user:
            passwd = User_Info.objects.filter(username=username, password=password)
            if passwd:
                info = '登录成功'
                return HttpResponseRedirect('/index/')
                # return render(request,'index.html',{'uf':uf})
            else:
                info = 'Please check your password'
                return HttpResponse(json.dumps({"msg": info}), content_type="application/json")
        elif len(user) == 0:
            info = 'Please check your username'
            return HttpResponse(json.dumps({"msg": info}), content_type="application/json")
    else:
        uf = UserForm()
    # return render_to_response('login.html',{'uf':uf})
    return render(request, 'login.html', {'uf': uf})


def Regist1(request):
    id = request.POST.get('id')
    # id=request.POST['id']
    username = request.POST.get('username')
    password = request.POST.get('password')
    repeat_password = request.POST.get('repeat_password')
    context = {"id": id, "username": username, "password": password}
    return render(request, "regist.html", context)


def Regist(request):
    id = request.POST.get('id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    repeat_password = request.POST.get('repeat_password')
    state = None
    if password == '' or repeat_password == '':
        state = 'empty'
        return HttpResponse('password can not be empty')
    elif password != repeat_password:
        state = 'repeat_error'
        return HttpResponse('repeat password is wrong')
    else:
        if User_Info.objects.filter(id=id):
            state = 'id_exist'
            return HttpResponse('The id is already exist')
        else:
            new_user = User_Info.objects.create(id=id, username=username, password=password)
            new_user.save()
            state = 'success'
    content = {
        'state': state,
    }
    if state == 'success':
        # return render_to_response(request,{'state':state})
        # return render(request,'login.html',content)
        return HttpResponseRedirect('/login/')


# @csrf_protect
# def Regist1(request):
#     uf=UserForm(request.POST)
#     if uf.is_valid():
#         username=uf.cleaned_data['username']
#         password=uf.cleaned_data['username']
#         #判断用户名密码是否与已经存在的匹配
#         user=User_Info.objects.filter(username=username)
#         if user:
#             info='用户名已经存在！'
#         elif len(user)==0:
#             info='注册成功'
#             user=User_Info()
#             user.username=username
#             user.password=password
#             user.save()
#         return HttpResponse(info)
#     else:
#         uf=UserForm()
#     return render(request,'regist.html',{'uf':uf})

def Index(request):
    # uf=UserForm(request.POST)
    username = request.session.get('username')
    return render(request, 'index.html', {'username': username})


def Logout(request):
    response = HttpResponse('Logout!')
    # 清理cookie中保存的username
    del request.session['username']
    return response


def All_Score_Info(request):
    username = request.session.get('username')
    score_list = Score_Info.objects.all()
    context = {'username': username, 'score_list': score_list}
    return render(request, 'score_info.html', context)
    # 输入网址httphttp://127.0.0.1:8000/all_score_info/?username=aa会显示用户名aa
    # username=request.GET['username']
    # return render(request,'score_info.html',{'username':username})


# def base(request):
#     return render_to_response('base.html')
#
# def User_Info(request):
#     username=request.POST['username']
#     user_list=User_Info(username).objects.get
#     return render(request,'user_info.html',{'user':user_list})


# 获取某一个人的成绩信息（先把姓名查询出来，然后获取他的id，然后再根据id来查询某一个人的成绩）
def get_score(request):
    username = request.session.get('username')
    user = User_Info.objects.get(username=username)
    id = user.id
    score = Score_Info.objects.get(userID_id=id)
    context = {'user': user, 'score': score}
    return render(request, 'score.html', context)


def Add_Score(request):
    userID_id = request.POST.get('userID_id')
    java = request.POST.get('java')
    python = request.POST.get('python')
    context = {'userID_id': userID_id, 'java': java, 'python': python}
    return render(request, 'add_score.html', context)


def Add_Score1(request):
    userID_id = request.POST.get('userID_id')
    java = request.POST.get('java')
    python = request.POST.get('python')
    user = User_Info.objects.filter(id=userID_id)
    if user:
        new_score = Score_Info.objects.create(id=userID_id, java=java, python=python, userID_id=userID_id)
        return HttpResponseRedirect('/all_score_info')


@csrf_protect
def Delete_Score(request, pk):
    score = Score_Info.objects.filter(userID_id=pk)
    score.delete()
    return HttpResponseRedirect('/all_score_info')


@csrf_protect
def Set_Password(request):
    uf = ChangeForm(request.POST)
    if uf.is_valid():
        username = uf.cleaned_data['username']
        old_password = uf.cleaned_data['old_password']
        new_password = uf.cleaned_data['new_password']
        repeat_password = uf.cleaned_data['repeat_password']
        user = User_Info.objects.filter(username=username)
        if new_password == repeat_password:
            if user:
                passwd = User_Info.objects.filter(username=username, password=old_password)
                if passwd:
                    User_Info.objects.filter(username=username, password=old_password).update(password=new_password)
                    info = '密码修改成功'
                    return HttpResponseRedirect('/login/')
                    # return render(request,'login.html',{'uf':uf})
                else:
                    info = '请检查原密码是否输入正确！'
                    return HttpResponse(info)
            elif len(user) == 0:
                info = '请检查用户名是否正确！'
                return HttpResponse(info)
        else:
            info = 'repeat password error'
    else:
        uf = ChangeForm()
    return render(request, 'set_password.html', {'uf': uf})


def Update_Score(request, pk):
    score = Score_Info.objects.get(userID_id=pk)
    return render_to_response('update_score.html', {'score': score})


def Update_Score1(request):
    pk = request.POST.get('id')
    java = request.POST.get('java')
    python = request.POST.get('python')
    score = Score_Info.objects.filter(userID_id=pk)
    score.update(java=java, python=python)
    return HttpResponseRedirect('/all_score_info')
