from django.shortcuts import render


def home(request):
    """view for home page"""
    return render(request, 'home.html')


def about(request):
    """view for about us page"""
    return render(request, 'about.html')


def contact(request):
    """ view for contact us page"""
    return render(request, 'contact.html')


def service(request):
    """view for service page"""
    return render(request, 'service.html')


def faq(request):
    """view for frequently asked questions page"""
    return render(request, 'faq.html')
