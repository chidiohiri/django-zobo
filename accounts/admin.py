from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Additional Info',  
            {
                'fields': ('first_name', 'email'),
            }
        ),
    )

admin.site.register(User, CustomUserAdmin)
