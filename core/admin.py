from django.contrib import admin
from .models import BlogPost, Testimonial, NewsletterSignup, ContactMessage

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')

@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'signed_up_at')
    readonly_fields = ('signed_up_at',)


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    readonly_fields = ('timestamp',)