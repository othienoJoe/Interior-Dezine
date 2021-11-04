from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Company(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	description = models.TextField()
	image = CloudinaryField("image")
	url = models.URLField(blank=True)
	location = models.CharField(max_length=100, default="Nairobi")
	date = models.DateTimeField(auto_now_add=True, null=True)

	@classmethod
	def search_by_title(cls, search_term):
			companies = cls.objects.filter(title__icontains=search_term)
			return companies

	@classmethod
	def get_company_by_id(cls, id):
			company = cls.objects.get(id=id)
			return company

	@classmethod
	def get_all_companies(cls):
			companies = cls.objects.all()
			return companies

	@classmethod
	def get_all_companies_by_user(cls, user):
			companies = cls.objects.filter(user=user)
			return companies

	# update project
	def update_company(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)
		self.save()

	def save_company(self):
		self.save()

	def delete_company(self):
		self.delete()

	def __str__(self):
		return self.title


# profile models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=250, blank=True, null=True)
    contact = models.CharField(max_length=250, blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username

# rating models
class Rating(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	design_rate = models.IntegerField(default=0, blank=True, null=True)
	usability_rate = models.IntegerField(default=0, blank=True, null=True)
	content_rate = models.IntegerField(default=0, blank=True, null=True)
	avg_rate = models.IntegerField(default=0, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, null=True)

	def save_rating(self):
		self.save()

	def delete_rating(self):
		self.delete()

	@classmethod
	def filter_by_id(cls, id):
		rating = Rating.objects.filter(id=id).first()
		return rating

	def __str__(self):
		return self.user.username