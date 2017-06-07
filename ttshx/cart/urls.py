from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.list),
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^count_change/$',views.count_change),
    url(r'^delete/$',views.delete),
]