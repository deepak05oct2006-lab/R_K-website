from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, GalleryImage, Testimonial
from .forms import ContactForm


def home(request):
    context = {
        'services': Service.objects.all()[:6],
        'gallery': GalleryImage.objects.all()[:8],
        'testimonials': Testimonial.objects.all()[:6],
        'form': ContactForm(),
    }
    return render(request, 'core/home.html', context)


def services(request):
    return render(request, 'core/services.html', {'services': Service.objects.all()})


def gallery(request):
    cat = request.GET.get('cat')
    images = GalleryImage.objects.all()
    if cat in ('paint', 'polish'):
        images = images.filter(category=cat)
    return render(request, 'core/gallery.html', {'gallery': images, 'cat': cat})


def about(request):
    return render(request, 'core/about.html', {'testimonials': Testimonial.objects.all()})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! We'll contact you shortly.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
