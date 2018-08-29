from django.conf.urls import url,include


from rest_framework import routers
from .views import emp_viewset,index

router = routers.DefaultRouter()

router.register('api', emp_viewset)
urlpatterns = [

    #url(r'^app/',emp_viewset) ,  # function based views
    url(r'^', include(router.urls)),

    url(r'^app/',index)

]