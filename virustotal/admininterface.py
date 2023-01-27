from django.shortcuts import render
from . import pool


def admininterface(request):
    return render(request, 'adminlogin.html')

def AdminDashboard(request):
    return render(request, 'admindashboard.html')

def CheckAdminLogin(request):
    try:
        email = request.POST['email']
        password = request.POST['password']

        dbe, cmd = pool.ConnectionPool()
        q = "select * from admin where email = '{}' and password = '{}'".format(email, password)
        cmd.execute(q)
        result = cmd.fetchone()
        if (result):
            return render(request, "admindashboard.html", {'result': result})
        else:
            return render(request, "adminlogin.html", {'result': result, 'msg': 'Invalid Email / Password '})
        dbe.close()
    except Exception as e:
        print(e)
        return render(request, "adminlogin.html", {'result': {}, 'msg': 'Server Error'})

def adduser(request):
    return render(request, 'adduser.html')

def usersumbit(request):
    try:
        email = request.POST['email']
        password = request.POST['password']

        q = "insert into virustotal.user(email,password) values('{}','{}')".format(email,password)
        db, cmd = pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, "adduser.html", {'msg': "Record successfully submitted !"})
    except:
        return render(request, "adminlogin.html")

def blockuser(request):
    iduser = request.GET['iduser']

    q = "delete from virustotal.user where iduser = {}".format(iduser)
    db, cmd = pool.ConnectionPool()
    cmd.execute(q)
    db.commit()
    db.close()
    return render(request, "DisplayAllUser.html")


