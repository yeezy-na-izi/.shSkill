from django.contrib import admin
from user.models import Account, SocialNetworks, Student, Coordinator, Teacher

admin.site.register(Account)
admin.site.register(SocialNetworks)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Coordinator)
