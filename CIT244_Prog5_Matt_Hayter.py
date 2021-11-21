# CIT 244 - Program 5 - Matt Hayter

import sqlite3 as db
from bottle import route, run, request, response, template, static_file


@route('/', method = 'GET')    #login page
def index():
    return template('login')



@route('/login', method = 'POST')    #after clicking submit
def login():
    user = request.forms.get("user")
    pw = request.forms.get("pw")

    con = db.connect("travel_expenses.db")
    cur = con.cursor()
    sql = "SELECT * FROM members WHERE username= ? and password = ?"

    cur.execute(sql, (user,pw))
    result = cur.fetchone()
    cur.close()


    if (result):
        return template('tech_menu')

    else:
        m = {'msg': "login failed", 'img':'<img src="static/NO.gif" />'}
        return template('status', m)


@route('/showTrips', method = ['GET', 'POST'])    #display trips
def table():
    if request.method == 'GET':
        return template('trip_form')
    
    else:
        user = request.forms.get("username")
        con = db.connect('travel_expenses.db')
        cur = con.cursor()
        
        sql = "SELECT * FROM trips WHERE username = ?"
        cur.execute(sql, (user,))

        rows = cur.fetchall()
        cur.close()
        
        if rows:
            data = {"rows": rows, "user": user}   
            return template('show_trips', data)

        else:
            m = {'msg':'no such username', 'img':'<img src="static/NO.gif" />'}
            return template('status', m)

     

@route('/enterTrip', method = ['GET', 'POST'])      #user inserts a trip to table
def tech_load():
    if request.method == 'GET':
        return template('add_trip')

    else:
        user = request.forms.get("user")
        date = request.forms.get("date")
        dest = request.forms.get("dest")
        miles = request.forms.get("miles")
        gal = request.forms.get("gal")


        try:
            con = db.connect('travel_expenses.db')
            cur = con.cursor()

            data = (None, user, date, dest, miles, gal)

            sql = "INSERT INTO trips VALUES (?, ?, ?, ?, ?, ?)"

            cur.execute(sql, data)
            con.commit()
            cur.close()
        
            m = {'msg': "insert trip successful", 'img':'<img src="static/YES.gif" />'}
            return template('status', m)

        except:
            m = {'msg': "insert trip was NOT successful", 'img':'<img src="static/NO.gif" />'}
            return template('status', m)


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./images')


run(host = 'localhost', port = 8080)