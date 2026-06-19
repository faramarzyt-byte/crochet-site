from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost, Testimonial, NewsletterSignup
from .forms import ContactForm
from django.core.paginator import Paginator



def home(request):
    # گرفتن ۳ نظر فعال و ۳ پست آخر بلاگ
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    
    # مدیریت فرم خبرنامه (Newsletter)
    if request.method == 'POST' and 'email' in request.POST:
        email = request.POST.get('email')
        if email:
            # ایجاد ایمیل اگر از قبل نباشد (برای جلوگیری از خطای تکراری)
            obj, created = NewsletterSignup.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Welcome to our inner circle! Thank you for subscribing.")
            else:
                messages.info(request, "You are already subscribed to our newsletter!")
            return redirect('home')

    context = {
        'testimonials': testimonials,
        'recent_posts': recent_posts
    }
    return render(request, 'home.html', context)


def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog.html", {
        "page_obj": page_obj
    })




# صفحه جزییات هر پست بلاگ
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    related_posts = BlogPost.objects.exclude(id=post.id)[:3]

    return render(request, "blog_detail.html", {
        "post": post,
        "related_posts": related_posts
    })


def about(request):
    return render(request, 'about.html')





def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
