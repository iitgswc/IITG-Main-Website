from django.db import models

# Navbar
class About(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class AcademicAffairs(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Administration(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Department(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class AcademicCenter(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class ExtramurailCenter(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class ExchangeProgram(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Utility(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Form(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Partnership(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

# Carousel
class CarouselImages(models.Model):
	image = models.CharField(max_length=200, help_text = "Add the image to the static folder and give the image name here.")

class Announcement(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

# Middle 3 columns
class ResearchInnovation(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class UpcomingEvent(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	date = models.DateField()
	is_active = models.BooleanField(default=True)

class QuickLink(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

# Footer 3 Columns
class Resource(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Programm(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)

class Current(models.Model):
	title = models.CharField(max_length=20)
	link = models.CharField(max_length=200, default="#")
	is_active = models.BooleanField(default=True)
