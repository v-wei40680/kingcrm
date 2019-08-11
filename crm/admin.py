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
admin.site.register(ContractTemplate)
admin.site.register(StudentEnrollment)
admin.site.register(PaymentRecord)


class CustomerAdmin(admin.ModelAdmin):
    #显示
    list_display = ['name','source','contact_type','contact','consultant','consult_content','status','date']
    #过滤
    list_filter = ['source','consultant','status','date']
    #搜索，consultant是外键，必须加“__字段名”
    search_fields = ['contact','consultant__name']
    # readonly_fields = ['contact', 'status']
    filter_horizontal = ['consult_courses']
    list_per_page = 8
    actions = ['change_status',]

    def change_status(self, request, querysets):
        querysets.update(status=2)

admin.site.register(CustomerInfo,CustomerAdmin)

