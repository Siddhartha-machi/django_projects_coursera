from django.urls import path

from ads.api_views import Ad_list, Ad_detail

urlpatterns = [
    path("ads/", Ad_list, name="api_ad_list"),
    path("ads/<int:pk>/", Ad_detail, name="api_ad_detail"),
]