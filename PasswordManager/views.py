from django.shortcuts import render, redirect
from django.template import loader
from .models import Entry
from django.http import HttpResponse
from django.core.exceptions import ValidationError


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    # get data from db
    entries = Entry.objects.all()
    # decrypt password
    for entry in entries:
        entry.password = entry.decryptPassword()
    # pass data to template
    context = {
        'entries': entries,
    }
    return HttpResponse(template.render(context, request))


def create(request):
    if request.method == "POST":
        # get all post data
        data = request.POST
        # print(data)
        # validation
        try:
            if data.get("password") != data.get("confirmPassword"):
                raise ValidationError("Passwords do not match")
        except ValidationError as e:
            error_message = e.message
            return render(request, 'create.html', {'error_message': error_message,
                                                   'url': data.get("url"), 'username': data.get("username"),
                                                   'note': data.get("note")})
        # set data to model
        entry = Entry(url=data.get("url"), username=data.get("username"), password=data.get("password"),
                      note=data.get("note"))
        # hash password
        print(entry.encryptPassword())
        # save to db
        entry.save()
        # redirect to index
        return redirect("index")
    else:
        # display create form
        return render(request, "create.html")


def view(request, entry_id):
    template = loader.get_template('view.html')
    # get data from db
    entry = Entry.objects.get(id=entry_id)
    entry.password = entry.decryptPassword()
    # pass data to template
    context = {
        'entry': entry,
    }
    return HttpResponse(template.render(context, request))


def edit(request, entry_id):
    if request.method == "POST":
        # get all post data
        data = request.POST
        # print(data)
        # validation
        try:
            if data.get("password") != data.get("confirmPassword"):
                raise ValidationError("Passwords do not match")
        except ValidationError as e:
            error_message = e.message
            return render(request, 'edit.html', {'error_message': error_message,
                                                 'url': data.get("url"), 'username': data.get("username"),
                                                 'note': data.get("note")})
        #get data from db
        entry = Entry.objects.get(id=entry_id)
        # set data to model
        entry.url = data.get("url")
        entry.username = data.get("username")
        entry.password = data.get("password")
        entry.note = data.get("note")
        # hash password
        print(entry.encryptPassword())
        # save to db
        entry.save()
        # redirect to index
        return redirect("index")
    else:
        # display edit form
        template = loader.get_template('edit.html')
        # get data from db
        entry = Entry.objects.get(id=entry_id)
        entry.password = entry.decryptPassword()
        # pass data to template
        context = {
            'entry': entry,
        }
        return HttpResponse(template.render(context, request))


def delete(request, entry_id):
    # get data from db
    entry = Entry.objects.get(id=entry_id)
    # delete from db
    entry.delete()
    # redirect to index
    return redirect("index")
