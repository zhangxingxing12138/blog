from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^list/$',views.blog_list,name='blog_list'),
    url(r'^category/(?P<cid>[0-9]+)/$', views.blog_list),
    url(r'^tags/(?P<tid>[0-9]+)/$', views.blog_list),
    url(r'^blog/(?P<bid>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^comment/(?P<bid>[0-9]+)$', views.CommentView, name='comment'),
    url(r'^login/', views.loginin, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^active/(?P<active_code>[a-zA-Z0-9]+)', views.ActiveView.as_view(), name='active'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^forget/', views.forget),
    url(r'^newpwd/', views.newpwd),
    url(r'^reset/(?P<active_code>[a-zA-Z0-9]+)', views.reset),






]
