from rest_framework import serializers
from .models import Profile, Company

# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ("user", "profile_photo", "bio", "contact")

# Company serializer
class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ("user", "title", "description", "image", "url", "location", "date")