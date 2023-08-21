from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.StuViewset import StuViewset
router=routers.DefaultRouter()
router.register(r'Stu_details',StuViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
