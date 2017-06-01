from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register/$',views.register),
    url(r'^post1/$',views.post1),
    url(r'^post2/$',views.post2),
    url(r'^login/$',views.login),
    url(r'^post3/$',views.post3),
]