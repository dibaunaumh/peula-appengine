from django.http import HttpResponse
from letters.models import Letter, Organization
from django.shortcuts import render_to_response, get_object_or_404
from letters.social_media import get_mentions
from django.contrib.auth.models import User

def home(request):
    list = Letter.objects.all()
    return render_to_response("list.html", locals())


def org_page(request, org):
    organization = get_object_or_404(Organization, name=org)
    mentions = get_mentions(org)
    return render_to_response("org.html", locals())


def setup(request):
    authorized = False
    if "token" in request.GET:
        if request.GET["token"] == "clementine":
            authorized = True
    if not authorized:
        return HttpResponse("You're not authorized.")
    admin = User()
    admin.username = "admin"
    admin.email = "admin@admin.com"
    admin.is_staff = True
    admin.is_active = True
    admin.is_superuser = True
    admin.password = "sha1$5328e$f9bd59b590632eb09965c3b118c9fbbfff9725f4"
    admin.save()
    return HttpResponse("Admin user created")