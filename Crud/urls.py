from django.conf.urls import url
from Crud import views

urlpatterns =[

    url('create',views.kingcreate),
    url('index', views.kingindex),
    url('update/(?P<sn>[0-9]+)', views.kingupdate),
    url('delete/(?P<id>[0-9]+)', views.kingdelete),
    url('osdcreate',views.idcreate),
    url('osdindex', views.idindex),
    url('idupdate/(?P<sn>[0-9]+)', views.idupdate),
    url('iddelete/(?P<id>[0-9]+)', views.iddelete),
]



