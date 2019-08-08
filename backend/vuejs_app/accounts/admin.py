from django.contrib import admin
from django.utils.safestring import mark_safe
from accounts.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birth_date',
        'username',
        'email',
    )
    fields = (
        'username',
        'password',
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
        'groups',
        'user_permissions',
        'date_joined',
        'last_login',
        'first_name',
        'last_name',
        'birth_date',
        'photo',
        'avatar_image'
    )
    readonly_fields = (
        'avatar_image',
    )

    def avatar_image(self, obj):
        width = obj.photo.width if obj.photo.width < 300 else 300
        height = obj.photo.height / (obj.photo.width / width)
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=width,
            height=height,
            )
        )


admin.site.register(User, UserAdmin)
