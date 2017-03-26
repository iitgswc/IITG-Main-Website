from django.shortcuts import render
from .models import *

# main home page view
def Main(request):
	context = {}

	# get data from database and add to the context variable
	# About
	about = About.objects.filter(is_active=True)
	# Academics
	academic = AcademicAffairs.objects.filter(is_active=True)
	# Administration
	administration = Administration.objects.filter(is_active=True)
	# Department
	department = Department.objects.filter(is_active=True)
	# Center
	center = AcademicCenter.objects.filter(is_active=True)
	# ExtramurailCenter
	emcenter = ExtramurailCenter.objects.filter(is_active=True)
	# Utility
	utility = Utility.objects.filter(is_active=True)
	# Form
	form = Form.objects.filter(is_active=True)
	# Partnership
	partnership = Partnership.objects.filter(is_active=True)
	# Exchange prog
	exchangeprog = ExchangeProgram.objects.filter(is_active=True)
	# CarouselImage
	carouselimages = CarouselImages.objects.all()
	# Announcement 
	announcement = Announcement.objects.filter(is_active=True)
	# ResearchInnovation
	researchinnovation = ResearchInnovation.objects.filter(is_active=True)
	# UpcomingEvent
	upcomingevent = UpcomingEvent.objects.filter(is_active=True)
	# QuickLink
	quicklink = QuickLink.objects.filter(is_active=True)
	# Resource
	resource = Resource.objects.filter(is_active=True)
	# Programm
	programm = Programm.objects.filter(is_active=True)
	# Current
	current = Current.objects.filter(is_active=True)

	# updating the context variable
	context = {
		'current' : current,
		'about' : about,
		'academic' : academic,
		'programm' : programm,
		'resource' : resource,
		'emcenter' : emcenter,
		'exchangeprog' : exchangeprog,
		
		'quicklink' : quicklink,
		'upcomingevent' : upcomingevent,
		'researchinnovation' : researchinnovation,
		
		'announcement' : announcement,
		'carouselimages' : carouselimages,
		'partnership' : partnership,
		'form' : form,
		'utility' : utility,
		'center' : center,
		'department' : department,
		'administration' : administration
	}

	# rendering the view
	return render(request, 'main/main.html', context)
