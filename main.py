from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/search',methods = ['POST', 'GET'])
def search():
        if request.method == 'POST':
           import sqlite3
           username = request.form['username']
           conn = sql.connect("mydatabase.db")
           cur = conn.cursor()
           sql = ("SELECT username FROM Twitters where number_follower=(select max(number_follower) from Twitters)")
           cur.execute(sql)
           mydata = (cur.fetchall())
           return render_template("search.html",mydata=mydata)

if __name__ == '__main__':
   app.run(debug = True)
