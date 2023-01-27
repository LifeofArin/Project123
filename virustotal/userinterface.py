from django.shortcuts import render
from . import pool


def userlogin(request):
    return render(request, "userlogin.html")

def userinterface(request):
    return render(request, "userdashboard.html")


def CheckUserLogin(request):
    try:

        email = request.POST['email']
        password = request.POST['password']
        db, cmd = pool.ConnectionPool()
        q = "select * from user where email = '{}' and password = '{}'".format(email, password)
        cmd.execute(q)
        result = cmd.fetchone()

        if (result):
            return render(request, "userdashboard.html", {'result': result})
        else:
            return render(request, "userlogin.html", {'result': result, 'msg': "Invalid Email/Password"})
        db.close()
    except Exception as e:
        return render(request, "userlogin.html", {'result': []})


def DisplayAllUser(request):
    try:
        dbe, cmd = pool.ConnectionPool()
        q = "select * from user"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        print(rows)
        return render(request, "DisplayAllUser.html", {'rows': rows})
    except Exception as e:
        print(e)
        return render(request, "DisplayAllUser.html", {'rows': []})

def userupdate(request):
    iduser = request.GET['iduser']
    return render(request, "edituser.html", {'iduser': iduser})

def edituser(request):
    iduser = request.GET['iduser']
    email = request.POST['email']
    password = request.POST['password']


    try:
        dbe, cmd = pool.ConnectionPool()
        q = "update virustotal.user set email = '{}', password = '{}' where iduser = {}".format(email, password, iduser)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return render(request, "edituser.html", {'msg': "Record successfully updated !"})
    except Exception as e:
        return render(request, "edituser.html")

