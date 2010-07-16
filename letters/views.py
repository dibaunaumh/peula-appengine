from django.http import HttpResponse
from letters.models import Letter, Organization
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from letters.social_media import get_mentions
from django.core import serializers
from letters.forms import LetterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt




def org_page(request, org):
    organization = get_object_or_404(Organization, name=org)
    mentions = get_mentions(org)
    return render_to_response("org.html", locals())



def search_similar_letters(request, prefix):
    letters = Letter.objects.filter(subject__contains=prefix)
    json = serializers.serialize("json", letters)
    return HttpResponse(json)

@login_required
@csrf_exempt
def add_letter(request):
    if request.POST:
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = LetterForm()
    return render_to_response("edit_letter.html", locals())



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