from django.conf.urls import url

from . import views




urlpatterns = [
    # url(r'^facebook/$', views.index,name='index'),
     url(r'^facebook/$', views.index,name='index'),
     url(r'^facebook/(?P<id>\d+)/$',views.detail,name='detail'),
     url(r'^myprofile/$', views.myprofile,name='myprofile'),
     url(r'^like/(?P<id>\d+)/$',views.like,name='like'),

     # url(r'^comment/(?P<id>\d+)',views.comment,name='comment'),

     url(r'^unlike/(?P<id>\d+)/$',views.unlike,name='unlike'),
     url(r'^unlikefromdetail/(?P<id>\d+)/$',views.unlikefromdetail,name='unlikefromdetail'),
     url(r'^likefromdetail/(?P<id>\d+)/$',views.likefromdetail,name='likefromdetail'),
     url(r'^profile/(?P<pk>\d+)/$',views.profile1,name='profile'),

     url(r'^facebook/article/(?P<id>\d+)/$',views.like,name='article'),
     url(r'^addfriend/(?P<friend>[\w\-]+)/$',views.addfriend,name='addfriend'),
     url(r'^unfriend/(?P<name>[\w\-]+)/$',views.unfriend,name='unfriend'),
     url(r'^accept/(?P<addfriend>[\w\-]+)/$',views.accept,name='acceptfriend'),
     url(r'^cancelrequest/(?P<name>[\w\-]+)/$',views.cancelrequest,name='cancelrequest'),
     url(r'^edit_favorites/', views.edit_favorites,name='edit_facvorites'),
      ]


