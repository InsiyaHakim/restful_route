# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "users":User.object.all()
    }
    return render(request,'first/index.html',context)

def new(request):
    return render(request,'first/create.html')

def create(request):
    if request.method == "POST":
        error=User.object.creating_db(request.POST)
        if len(error)>0:
            for error in error:
                messages.error(request, error)
            return redirect("main:new")
        else:
            return redirect("main:index")
    else:
        return redirect("main:new")

def show(request,user_id):
    user=User.object.get(id=user_id)
    context={
        "users":user
    }
    return render(request,"first/show.html",context)

def delete(request,user_id):
    User.object.get(id=user_id).delete()
    return redirect("main:index")

def edit(request,user_id):
    user=User.object.get(id=user_id)
    context={
        "users":user
    }
    return render(request,'first/edit.html',context)

def update(request,user_id):
    if request.method == "POST":
        error=User.object.updating_db(request.POST,user_id)
        if len(error)>0:
            for error in error:
                messages.error(request, error)
            print "ok"
            return redirect("/user/"+str(user_id)+"/edit")
        else:
            print "updated"
            return redirect("/user/"+str(user_id)+"/edit")
    else:
        return redirect("main:index")

