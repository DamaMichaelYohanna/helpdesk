from django.shortcuts import render, reverse, redirect

from main.models import Issue


def home(request):
    """view for home page"""
    return render(request, 'home.html')


def about(request):
    """view for about us page"""
    return render(request, 'about.html')


def contact(request):
    """ view for contact us page"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return redirect(reverse("main:home"))

    else:
        return render(request, 'contact.html')


def issue(request):
    """view for service page"""
    ticket = request.GET.get("ticket")
    if ticket:
        track_issue = Issue.objects.get(ref=ticket)
        print(track_issue.complainant)
        return render(request, 'issues.html', {'issue': track_issue})

    return render(request, 'issues.html')


def faq(request):
    """view for frequently asked questions page"""
    return render(request, 'faq.html')
