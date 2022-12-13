from django.conf.urls import url
from filters import views

app_name = "filter"
urlpatterns = [
url(r'^other',views.other,name="other"),
url(r'^relative',views.Cbview.as_view(),name="relative"),
]
