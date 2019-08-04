from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Role)
# admin.site.register(CustomerInfo)
admin.site.register(Student)
admin.site.register(CustomerFollowUp)
admin.site.register(Course)
admin.site.register(ClassList)
admin.site.register(CourseRecord)
admin.site.register(StudyRecord)
admin.site.register(Branch)
admin.site.register(Menus)
admin.site.register(UserProfile)


class CustomerAdmin(admin.ModelAdmin):
    #显示
    list_display = ['name','source','contact_type','contact','consultant','consult_content','status','date']
    #过滤
    list_filter = ['source','consultant','status','date']
    #搜索，consultant是外键，必须加“__字段名”
    search_fields = ['contact','consultant__name']

admin.site.register(CustomerInfo,CustomerAdmin)

