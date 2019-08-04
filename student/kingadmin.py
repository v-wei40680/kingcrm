# student/kingadmin.py

from kingadmin.sites import site
from student import models

print('student kingadmin.....')

#注册model
class TestAdmin(object):
    list_display = ['name']

site.register(models.Test,TestAdmin)
