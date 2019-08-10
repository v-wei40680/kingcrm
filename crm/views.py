from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from crm import models
from . import form

# Create your views here.
def dashboard(request):
    return render(request, 'crm/dashboard.html')

@login_required
def stu_enrollment(request):

    customers = models.CustomerInfo.objects.all()
    class_lists = models.ClassList.objects.all()

    if request.method == 'POST':
        #获取提交的客户id和班级id，然后生成报名链接
        customer_id = request.POST.get('customer_id')
        class_grade_id = request.POST.get('class_grade_id')
        enrollment_obj = models.StudentEnrollment.objects.create(
            customer_id = customer_id,
            class_grade_id = class_grade_id,
            consultant_id = request.user.userprofile.id
        )
        #生成链接返回到前端
        enrollment_link = "http://localhost:8000/crm/enrollment/%s"% enrollment_obj.id

    return render(request,'crm/stu_enrollment.html',locals())

def enrollment(request,enrollment_id):
    '''学员在线报名表地址'''

    enrollment_obj = models.StudentEnrollment.objects.get(id=enrollment_id)

    if request.method == 'POST':
        customer_form = form.CustomerForm(instance=enrollment_obj.customer,data=request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return HttpResponse("你已成功提交报名信息，请等待审核，欢迎加入仙剑奇侠传")
    else:
        customer_form = form.CustomerForm(instance=enrollment_obj.customer)

    return render(request,'crm/enrollment.html',locals())
