from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
def index(request):  # Home page
	company = Company.objects.all()
	# get the latest company from the database
	latest_company = company[0]
	# get company rating
	rating = Rating.objects.filter(project_id=latest_company.id).first()

	return render(
		request, "index.html", {"companies": company, "project_home": latest_company, "rating": rating}
  )

# single company page
def Company_details(request, project_id):
	company = Company.objects.get(id=project_id)
	# get company rating
	rating = Rating.objects.filter(company = company)
	return render(request, "company.html", {"project": company, "rating": rating})