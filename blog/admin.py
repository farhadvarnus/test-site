from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("title", "author", "status", "counted_view",
                    "created_date", "updated_date")
    list_filter = ("status", "author")
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)
