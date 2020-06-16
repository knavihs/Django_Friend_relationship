from django.contrib import admin
from .models import People,Relationship,Posts
# Register your models here.
admin.site.register(People)
admin.site.register(Relationship)
admin.site.register(Posts)