from django.contrib import admin
from .models import BookTable


class BookTableAdmin(admin.ModelAdmin):
    list_display = ("user", "guest", "jdate", "phone_number")
    list_filter = ("date", "guest")
    search_fields = ("phone_number", "date")


admin.site.register(BookTable, BookTableAdmin)
