from django.db import models

# Navbar
class About(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title


class AcademicAffairs(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Administration(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Department(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class AcademicCenter(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class ExtramurailCenter(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class ExchangeProgram(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Utility(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Form(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Partnership(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

# Carousel
class CarouselImages(models.Model):
	image = models.CharField(max_length=2000, help_text = "Add the image to the static folder and give the image name here.")

class Announcement(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

# Middle 3 columns
class ResearchInnovation(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class UpcomingEvent(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	date = models.DateField()
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class QuickLink(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

# Footer 3 Columns
class Resource(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Programm(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Current(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=2000, default="#")
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title
		