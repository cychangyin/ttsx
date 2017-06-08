from django.conf.urls import url
import views

urlpatterns=[
    url('^$',views.list),
    url('^handle/$',views.handle),

]