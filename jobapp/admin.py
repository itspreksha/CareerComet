from django.contrib import admin
from .models import *


admin.site.register(Category)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
    
admin.site.register(Applicant,ApplicantAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','is_closed','timestamp')

admin.site.register(Job,JobAdmin)

class BookmarkJobAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
admin.site.register(BookmarkJob,BookmarkJobAdmin)

class EmployeeFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name', 'feedback_text', 'created_at')
admin.site.register(EmployeeFeedback)

class EmployerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'employer_name', 'feedback_text', 'created_at')
admin.site.register(EmployerFeedback)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'qualification', 'experience')
admin.site.register(JobSeeker)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'location')
admin.site.register(Company)