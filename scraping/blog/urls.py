from django.conf.urls import url , include
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^tree', views.XML_Tree.as_view(), name='use'),
    url(r'^list', views.List_view, name = 'back'),
    ]
