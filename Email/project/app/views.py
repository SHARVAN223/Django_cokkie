from django.shortcuts import render ,redirect

from django.core.mail import send_mail

from app.models import Student as stu
import random

def landing(req):
    return render(req, 'landing.html')

def register (req):
    return render(req,'register.html')
    


def contact(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        q = req.POST.get('query')
    
        send_mail( "Django email",
                f'this information regrading your company Name:{n},Email:{e},Contact:{c},Query:{q}',
                "sharvan70458@gmail.com",
                [e],
                fail_silently=False,
)
    return redirect('landing') 


def login(req):
    return render(req,'login.html')

def forget(req):
    return render(req, 'forget.html')


def enteremail(req):
    if req.method=='POST':
        e=req.POST.get('email')
        user=stu.objects.filter(Email=e)
        if not user:
            msg='please enter valid email'
            return render(req,'forget.html',{'msg':msg})
        else:
            otp = random.randint(111111,999999)
            req.session['otp'] = otp
            req.session['email'] = e
            send_mail( "Django email",
                f'your forget password otp is pass{otp}',
                "sharvan70458@gmail.com",
                [e],
                fail_silently=False,
            )
            return render(req, 'changePassword.html')
    return render(req,'landing.html')


def changePassword(req):
    return render(req, 'changePassword.html' )
    

def reset(req):
    if req.method == 'POST':
        e_otp = req.POST.get('otp')
        n_pass = req.POST.get('n_pass')
        c_pass = req.POST.get('c_pass')
        otp = req.session.get('otp')
        if int(otp) == int(e_otp):
            if n_pass == c_pass:
                e= req.session.get('email')
                userdata = stu.objects.get(Email=e)
                userdata.Password = n_pass
                userdata.save()
                msg1 = 'password reset succesfully'
                return render(req,'login.html',{'msg1':msg1})
            else:
                msg2 = 'new_password and Conform_password not match'
                return render(req,'changePassword.html',{'msg2':msg2})
    else:
        msg3 = 'invalid otp'
        return render(req,'changePassword.html',{'msg':msg3})