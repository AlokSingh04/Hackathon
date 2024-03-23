from django.shortcuts import render
import _mysql_connector as sql
fn='',
ln='',
g='',
em='',
mn=''




# Create your views here.
def bookaction(request):
    global fn,ln,g,em,mn
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",password="tarun",database="tourism")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="First_Name":
                fn=value
            if key=="Last_Name":
                ln=value
            if key=="Gender":
                g=value
            if key=="Email":
                em=value
            if key=="Mobile_Number":
                mn=value
        c = "insert into users('{}','{}','{}','{}','{}')".format(fn,ln,g,em,mn)
        cursor.execute(c)
        m.commit()
    return render(request,'register.html')
    