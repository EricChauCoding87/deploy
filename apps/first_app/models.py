# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

# Create your models here.
class UsersManager(models.Manager):
    def regValidation(self,postData):
        errors = {}
        if Users.objects.filter(user_name = postData['UN']):
         	errors['user_name'] = "An account associated with that username already exists."
        if len(postData['FN']) < 3 or not postData['FN'].isalpha():
        	errors['full_name'] = "Full name must be at least 3 characters long, and use only alphabetical characters."
        if len(postData['PW']) < 8:
        	errors['pword_length'] = "Password must be at least 8 characters long."
        if postData['PW'] != postData['PWC']:
        	errors['pwconf'] = "Password confirmation must match password."
        print errors
        return errors

    def logValidation(self,postData):
        user = Users.objects.filter(user_name = postData['UN'])
        errors = {}
        if not user:
        	errors['UN'] = "Please enter a valid username."
        if user and not bcrypt.checkpw(postData['PW'].encode('utf8'), user[0].password.encode('utf8')):
        	errors['PW'] = "Invalid password."
        print errors
        return errors

class TravelManager(models.Manager):
    def travValidation(self,postData):
        errors={}
        if len(postData['DSTNTN']) <= 0:
            errors['dest_length'] = "You need to complete form"
        if len(postData['DESC']) <= 0:
            errors['desc_length'] = "You need to complete form"
        if len(postData['FROM']) <= 0:
            errors['from_length'] = "You need to complete form"
        if len(postData['TO']) <= 0:
            errors['to_length'] = "You need to complete form"
#        if len(postData['FROM']) >= len(postData['TO']):
            errors['amount'] = "Travel date to should not be before travel date from"
#       now = datetime.strptime(str(datetime.today()+'00:00:00.000000'),'%Y-%m-%d %H:%M:%S') unsupported operand types for + 'datetime.datetime' and 'unicode'
        start = postData['FROM']
        end = postData['TO']
        if datetime.strptime(start, '%Y-%m-%d %H:%M:%S') < datetime.strptime(now):            
            errors['less'] = "From date must be in the future"
        if end < start:
            errors['more'] = "To date must be set further in the future than from date"
        print errors
        return errors

#2018-04-01 21:12:01.795000        

class Users(models.Model):
    full_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UsersManager()
    def __repr__(self):
        return "<{} {} {}>".format(self.full_name, self.user_name, self.password)

class Travel(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateTimeField(auto_now=True)
    travel_date_to = models.DateTimeField(auto_now=True)
    trips = models.ManyToManyField(Users, related_name="trips")
    added_by = models.ForeignKey(Users, related_name="travels", null=True)
    objects = TravelManager()
    def __repr__(self):
        return "<{} {} {} {}>".format(self.destination, self.description, self.travel_date_from, self.travel_date_to)
    