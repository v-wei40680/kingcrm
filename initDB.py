import sys, os, datetime

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd)
print(pwd)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "PerfectCRM.settings")

import django
django.setup()

from django.contrib.auth.models import User
print('init DB')

from crm.models import *

try:
    m1 = Menus(name='crm', url_name='/kingadmin/')
    m1.save()
    print('save menus')
except:
    m1 = Menus.objects.first()

try:
    r1 = Role(name='sales')
    r1.save()
except:
    r1 = Role.objects.first()
r1.menus.add(m1)

u1 = User.objects.first()
try:
    up1 = UserProfile(name='bar', user=u1)
    up1.save()
except:
    up1 = UserProfile.objects.first()
up1.role.add(r1)

try:
    b1 = Branch(name='大学城')
    b1.save()
except:
    b1 = Branch.objects.first()

try:
    c1 = Course(name='python基础', price=999, period=1, outline='nothing')
    c1.save()
except:
    c1 = Course.objects.first()

try:
    ct1 = ContractTemplate(name='python基础合同', content='合同内容')
    ct1.save()
except:
    ct1 = ContractTemplate.objects.first()

try:
    cl1 = ClassList(branch=b1, course=c1, semester=1, start_date=datetime.date.today())
    cl1.save()
except:
    cl1 = ClassList.objects.first()
cl1.teachers.add(up1)

s1 = Student(customer=ci1)
s1.save()
s1.class_grades.add(cl1)

stuEnroll1 = StudentEnrollment(customer=ci1, class_grade=cl1,  consultant=up1)
stuEnroll1.save()