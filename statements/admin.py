from django.contrib import admin
from .models import HalaqaCriteria, Teachers, TeachersName, Leave, HalaqaName, HalaqaType, HalaqaTime
# Register your models here.
from import_export.admin import ImportExportModelAdmin
    
class TeachersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...

admin.site.register(Teachers, TeachersAdmin)  
admin.site.register(TeachersName)  
admin.site.register(Leave)
admin.site.register(HalaqaName)
admin.site.register(HalaqaType)
admin.site.register(HalaqaCriteria)
admin.site.register(HalaqaTime)

# البرنامج أدناه لإضافة اسماء المستخدمين في منصة الإدارة
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserResource(resources.ModelResource):
    def before_import_row(self,row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)   
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class UserAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)