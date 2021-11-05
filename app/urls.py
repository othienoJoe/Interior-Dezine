from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.index, name="index"),
	path("profile/", views.profile, name="profile"),
	path("accounts/profile/", views.profile, name="profile"),
	path("profile/update/", views.update_profile, name="update_profile"),
	path("company/save/", views.save_company, name="save_company"),
	path("company/<int:company_id>/", views.company_details, name="company_details"),
	path("company/delete/<int:id>/", views.delete_company, name="delete_company"),
	path("company/rate/<int:id>/", views.rate_company, name="rate_company"),
	path("search/", views.search_company, name="search_company"),
	# api
	url(r'^api/profile/$', views.ProfileList.as_view()),
	url(r'^api/project/$', views.CompanyList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
