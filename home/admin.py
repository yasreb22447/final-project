from django.contrib import admin
from .models import universities
from .models import canada, germany, USA
# Register your models here.
admin.site.register(universities)
admin.site.register(canada)
admin.site.register(germany)
admin.site.register(USA)