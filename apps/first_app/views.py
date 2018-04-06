# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from models import *
from datetime import datetime
import bcrypt
# the index function is called when root is visited
def main(request):
    return render(request,'main.html')

def register(request):
	msgs = Users.objects.regValidation(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
			return redirect('/')
	else:
		hashedpw = bcrypt.hashpw(request.POST['PW'].encode(), bcrypt.gensalt())
		Users.objects.create(full_name = request.POST['FN'], user_name = request.POST['UN'], password=hashedpw)
		user = Users.objects.last()
		request.session['logged_in'] = user.id
		print request.session['logged_in']
        print "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        return redirect('/travels')

def login(request):
	msgs = Users.objects.logValidation(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
			messages.error(request, v, extra_tags=k)
			print msgs
			return redirect('/')
	else:
		user = Users.objects.get(user_name=request.POST['UN'])
		request.session['logged_in'] = user.id
		return redirect('/travels')








def travels(request):
	if Users.objects.get(id=request.session['logged_in']) == Users.objects.last():
		status = "registered"
	else:
		status = "logged in"

	context = {
			'user': Users.objects.get(id=request.session['logged_in']),
			'travel_minus_user': Travel.objects.exclude(id=request.session['logged_in']),
			'users_minus_user': Users.objects.exclude(id=request.session['logged_in']),
			'user_faves': Travel.objects.filter(trips=request.session['logged_in']),
			'all_users': Users.objects.all(),
			'all_travel': Travel.objects.all(),
			'status': status,
		}
	return render(request, 'travels.html', context)

def destination(request, id):
	a = Users.objects.get(id=request.session['logged_in']),
#	b = Travel.trips
#	b.exclude(id)
#	trips = Travel.trips.all()
#	trips.save()
	a = Travel.objects.get(id=id)
#	b = Users.objects.get(id=request.session['logged_in'])
	c = a.added_by
	d = a.trips.exclude(id = request.session['logged_in'])
	b = Users.objects.get(id=request.session['logged_in'])
	context = {
		'user': c,
		'destination': Travel.objects.get(id=id),
		'planned_by': Travel.objects.filter(id=id),
		'trips': d,

	}
	return render(request,'destination.html',context)

def add_travel_plan(request):
    return render(request, 'add.html')

def process_add(request):
	now = datetime.now()
	start = request.POST['FROM']
	end = request.POST['TO']
	msgs = Travel.objects.travValidation(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
			print msgs
			return redirect ('/travels/add')
	else:
		a = Travel.objects.create(destination=request.POST['DSTNTN'],description=request.POST['DESC'],travel_date_from=request.POST['FROM'],travel_date_to=request.POST['TO'],added_by=Users.objects.get(id=request.session['logged_in'])) 
#		b = Users.objects.get(id=request.session['logged_in'])
#		a.added_by.add(b)
		print a
	return redirect('/travels')

def join(request, id):
	a = Travel.objects.get(id=id)
	b = Users.objects.get(id=request.session['logged_in'])
	a.trips.add(b)
	a.save()
	return redirect('/travels')

def remove(request, id):
	a = Travel.objects.get(id=id)
	b = Users.objects.get(id=request.session['logged_in'])
	a.trips.remove(b)
	return redirect('/travels')


def logout(request):
	request.session.clear()
	return redirect('/')