from django.contrib import admin
from .models import studentUser, college, instructor, adminUser, organisation,category,db_subcategory

# Register your models here.
admin.site.register(studentUser)
admin.site.register(college)
admin.site.register(instructor)
admin.site.register(adminUser)
admin.site.register(organisation)
admin.site.register(category)
admin.site.register(db_subcategory)