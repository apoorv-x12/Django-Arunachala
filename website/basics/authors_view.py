from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

def authors_list(request):
    try:
        con=sqlite3.connect("db.sqlite3")
        cur=con.cursor()
        cur.execute("select * from authors")
        authors=cur.fetchall()
        con.close()
        return render(request,'db/authors_list.html', {'authors': authors})
    except Exception as ex:
        print('error:',ex)
        return render(request,'db/authors_list.html')

def add_author(request):
    if request.method=='GET':
        return render(request,'db/add_author.html')
    else:
         # Process data sent from client
        fullname=request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        try:
            con=sqlite3.connect(r"db.sqlite3")#he used r before "db.sqlite3" but  was fine without r as well though
            cur=con.cursor()
            cur.execute("insert into authors(fullname,email,mobile) values(?,?,?)",(fullname,email,mobile))
            con.commit()                                           #he used f before string
            return render(request,'db/add_author.html', {'message': f'added [{fullname}] !',
            'fullname':fullname,"email":email,'mobile':mobile})
            # he used [{fullname}] in above although {fullname} was working fine as well
        except Exception as ex:
            print('error:',ex)
            return render(request,'db/add_author.html',{'message':f'cannot add {fullname}','fullname':fullname,
           "email":email,'mobile':mobile})
        finally:
            con.close() #imp *********always close connection in finally 