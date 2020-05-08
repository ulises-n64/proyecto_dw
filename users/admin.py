from users.models import Perfil
from django.contrib import admin

# Register your models here.
@admin.register(Perfil)
class perfilAdmin(admin.ModelAdmin):
    list_display=('user','phone_number','website', 'picture')
    search_fields=('user__email','user__username','user__first_name','user__last_name',)
    list_filter=('modified', 'user__is_active','user__is_staff', )
    