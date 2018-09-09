# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def creating_db(self,form_data):
        error=[]
        f_name=str(form_data['f_name'])
        l_name=str(form_data['l_name'])
        email=str(form_data['email'])
        fname=f_name.capitalize()
        lname=l_name.capitalize()

        if str.isalpha(f_name) == False or str.isalpha(l_name)==False:
            error.append("first name and last name should have any digit!!!")
        if len(f_name) <= 1:
            error.append("first name must be 8 characters")
        if len(l_name) <= 1:
            error.append("last name must be 8 characters")
        if not EMAIL_REGEX.match(email):
            error.append("invalid email")
        if len(error)>0:
            return error
        else:
            self.create(f_name=fname, l_name=lname, email=email)
            return error

    def updating_db(self,form_data,user_id):

        error=[]
        name=str(form_data['f_name'])
        l_name=str(form_data['l_name'])
        email=str(form_data['email'])

        if str.isalpha(name) == False or str.isalpha(l_name) == False:
            error.append("first name and last name shouldn't have any digit!!!")
        if len(name) <= 1:
            error.append("first name must be 8 characters")
        if len(l_name) <= 1:
            error.append("last name must be 8 characters")
        if not EMAIL_REGEX.match(email):
            error.append("invalid email")
        if len(error)>0:
            return error
        else:
            user=self.get(id=user_id)
            user.f_name=name
            user.l_name=l_name
            user.email=email
            user.save()
            return error


class User(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    object=UserManager()