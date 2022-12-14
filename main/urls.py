from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("issues", views.issue, name="issue"),
    path("faq", views.faq, name="faq"),
]