from django.shortcuts import render


def home(request):
    """view for home page"""
    return render(request, 'home.html')


def about(request):
    """view for about us page"""
    return render(request, 'about.hmtl')


def contact(request):
    """ view for contact us page"""
    return render(request, 'contact.hmtl')


def service(request):
    """view for service page"""
    return render(request, 'service.hmtl')


def faq(request):
    """view for frequently asked questions page"""
    return render(request, 'faq.html')
