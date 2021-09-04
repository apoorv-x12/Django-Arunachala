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