from django.contrib import admin
from .models import Article,Category

#actions
def make_published(modeladmin, request, queryset):
     row_updated = queryset.update(status='p')

     message = "شدند"
     if row_updated == 1:
          message = "شد"  

     modeladmin.message_user(request,'{} مقاله منتشر {}'.format(row_updated, message))

make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
     row_updated = queryset.update(status='d')
     message = "شدند"
     if row_updated == 1:
          message = "شد"  
     
     modeladmin.message_user(request,'{}  مقاله پیش‌نویس {}'.format(row_updated, message))
     
make_draft.short_description = "پیش‌نویس مقالات انتخاب شده"

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('position','title','slug','parent','status')
     list_filter = (['status'])
     search_fields = ('title','slug')
     prepopulated_fields = {'slug':('title',)}



admin.site.register(Category,CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
     list_display = ('title','thumbnail_tag','slug','author','jpublish','status','category_to_str')
     list_filter = ('publish','status','author')
     search_fields = ('title','description')
     prepopulated_fields = {'slug':('title',)}
     ordering = ['-status','-publish']
     actions = [make_published,make_draft]


admin.site.register(Article,ArticleAdmin)


