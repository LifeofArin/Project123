import pymysql as mysql


def ConnectionPool():
    dbe = mysql.connect(host="localhost", port=3306, user="root", password="rootarin123", db="virustotal")
    cmd = dbe.cursor()
    return (dbe, cmd)