from django.contrib import admin
from .models import Standard, Subject, Youtube, Qpaper, Notes, Books, Contactinfo, GalleryImage
# Register your models here.
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Youtube)
admin.site.register(Qpaper)
admin.site.register(Notes)
admin.site.register(Books)
admin.site.register(Contactinfo)
admin.site.register(GalleryImage)