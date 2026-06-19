from django.db import models
from django.utils.text import slugify

# مدل برای پست‌های بلاگ (Journal)
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    summary = models.TextField(help_text="A short preview of the post.")
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True,
        help_text="Upload a cozy image for this post."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# مدل برای نظرات مشتریان (Testimonials) که در اسکرین‌شات‌ها بود
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., Toronto, ON")
    rating = models.IntegerField(default=5, choices=[(i, f"{i} Stars") for i in range(1, 6)])
    quote = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client_name} - {self.rating} Stars"

# مدل برای دریافت ایمیل‌های خبرنامه (Newsletter Signups)
class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True)
    signed_up_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
