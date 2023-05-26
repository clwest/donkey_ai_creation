
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['email', 'username', 'is_staff', 'is_superuser', ] # new
  
  fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
  add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
  
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = "Donkey Betz AI"
admin.site.site_title = "Donkey Betz"
admin.site.index_title = "Donkey Betz AI Starter"
