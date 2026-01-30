from django.shortcuts import render

def landing(req):
    return render(req ,'landing.html')

def registration(req):
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('number')
    p=req.POST.get('Password')
    i=req.FILES.get('image')
    a=req.FILES.get('audio')
    v=req.FILES.get('video')
    r=req.FILES.get('resume')
    q = req.POST.getlist('qualification')
    g= req.POST.get('gender')
    s= req.POST.get('state')
    print(n,e,c,p,i,a,v,r, q,g,s,sep=",")
    return render(req, 'Registration.html')
    # return render(req, 'Registration.html')

def login(req):
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('number')
    p=req.POST.get('Password')
    i=req.FILES.get('image')
    a=req.FILES.get('audio')
    v=req.FILES.get('video')
    r=req.FILES.get('resume')
    q = req.POST.getlist('qualification')
    g= req.POST.get('gender')
    s= req.POST.get('state')
    response = render(req, 'login.html')
    response.set_cookie('name',n)
    response.set_cookie('email',e)
    response.set_cookie('number',c)
    response.set_cookie('password',p)
    response.set_cookie('image',i)
    response.set_cookie('audio',a)
    response.set_cookie('video',v)
    response.set_cookie('resume',r)
    response.set_cookie('qualification',q)
    response.set_cookie('gender',g)
    response.set_cookie('state',s)
    return response


def get_cookie(req):
    print(req.COOKIES)
    n = req.COOKIES.get('name')
    e=req.COOKIES.get('email')
    c=req.COOKIES.get('number')
    p=req.COOKIES.get('Password')
    i=req.COOKIES.get('image')
    a=req.COOKIES.get('audio')
    v=req.COOKIES.get('video')
    r=req.COOKIES.get('resume')
    q = req.COOKIES.get('qualification')
    g= req.COOKIES.get('gender')
    s= req.COOKIES.get('state')
    get= {'name':n, 'email':e, 'password':p, 'number':c,'qualification':q, 'gender':g , 'state':s,'image':i}
    return render(req, 'login.html',{'data': get}) 
    


def delete_cookie (req):
    response = render(req, 'login.html',{'msg1':'cookies delete'})
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('number')
    response.delete_cookie('number')
    response.delete_cookie('password')
    response.delete_cookie('image')
    response.delete_cookie('audio')
    response.delete_cookie('video')
    response.delete_cookie('resume')
    response.delete_cookie('qualification')
    response.delete_cookie('gender')
    response.delete_cookie('state')
    return response