from django.contrib import admin



from . models import Person,Post,Connection,LikePost,Addrequest,CommentPost,LoginDetail




class PostAdmin(admin.ModelAdmin):
	list_display=['person','post','timestamp','like']

class LikePostAdmin(admin.ModelAdmin):
	list_display=['post_id','person',]

class ConnectionAdmin(admin.ModelAdmin):
	list_display=['user','friend']


class AddrequestAdmin(admin.ModelAdmin):
	list_display=['person','requests']

class CommenrtPostAdmin(admin.ModelAdmin):
	list_display=['post_id','person','person_id','comment']

class LoginDetailsAdmin(admin.ModelAdmin):
	list_display=["person","lastlogin","ipaddress"]

admin.site.register(Post,PostAdmin)
admin.site.register(Person)
admin.site.register(LikePost,LikePostAdmin)
admin.site.register(Connection,ConnectionAdmin)
admin.site.register(Addrequest, AddrequestAdmin)
admin.site.register(CommentPost,CommenrtPostAdmin)
admin.site.register(LoginDetail,LoginDetailsAdmin)

