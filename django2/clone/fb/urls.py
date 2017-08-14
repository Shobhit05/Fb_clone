from django.conf.urls import url

from . import views

from . import like_unlike

from . import respond_friend_request


urlpatterns = [
    # url(r'^facebook/$', views.index,name='index'),
     
     url(r'^facebook/$', views.index,name='index'),
     
     url(r'^facebook/(?P<id>\d+)/$',views.detail,name='detail'),
     
     url(r'^myprofile/$', views.myprofile,name='myprofile'),
    
     url(r'^like/(?P<id>\d+)/$',like_unlike.like,name='like'),
     url(r'^unlike/(?P<id>\d+)/$',like_unlike.unlike,name='unlike'),
     url(r'^unlikefromdetail/(?P<id>\d+)/$',like_unlike.unlikefromdetail,name='unlikefromdetail'),
     url(r'^likefromdetail/(?P<id>\d+)/$',like_unlike.likefromdetail,name='likefromdetail'),
     url(r'^facebook/article/(?P<id>\d+)/$',like_unlike.like,name='article'),


     url(r'^profile/(?P<pk>\d+)/$',views.profile1,name='profile'),
     
     url(r'^addfriend/(?P<friend>[\w\-]+)/$',respond_friend_request.addfriend,name='addfriend'),
     url(r'^unfriend/(?P<name>[\w\-]+)/$',respond_friend_request.unfriend,name='unfriend'),
     url(r'^accept/(?P<addfriend>[\w\-]+)/$',respond_friend_request.accept,name='acceptfriend'),
     url(r'^cancelrequest/(?P<name>[\w\-]+)/$',respond_friend_request.cancelrequest,name='cancelrequest'),
     

     url(r'^edit_favorites/', views.edit_favorites,name='edit_facvorites'),
      ]


