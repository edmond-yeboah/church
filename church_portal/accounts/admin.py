from django.contrib import admin
from accounts.models import Customusers
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Customusers()
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', 
            {'fields':
                (
                    'admin',
                    'tel',
                    'age',
                    'bio',
                )
            }
        ),
    )
    
admin.site.register(Customusers, CustomUserAdmin)
