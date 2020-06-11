from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='templates')

app.config["MYSQL_HOST"] = '47.101.59.109'
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = 'mogan'
app.config["MYSQL_PASSWORD"] = 'nease.net'
app.config["MYSQL_DB"] = 'flaskapp'

mysql = MySQL(app)
# app = Flask(__name__)
# app.config['sfs新i4用sfs户注册regitrstionSERVER_NAME'] = "127.0.0.1:5001"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nice/<int:lid>')
def nice(lid):
    cur = mysql.connection.cursor()
    resultValue1 = cur.execute('SELECT * FROM Articles WHERE ArticleId = {0}'.format(lid))
    ddd = cur.fetchall()
    return render_template('detail.html', ddd=ddd, lid=lid)
@app.route('/nicelist')
def listp():
    cur = mysql.connection.cursor()
    resultValue1 = cur.execute('SELECT * FROM Articles')
    ddd = cur.fetchall()
    return  render_template('detail.html',ddd=ddd)
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
@app.route("/registration",methods=['GET','POST'])
def registration():
    if request.method == "POST":
        userDetails  = request.form
        name = userDetails['name']
        email = userDetails['email']
        msg = userDetails['msg']
        cur = mysql.connection.cursor()
        insert_stmt = (
          "INSERT INTO users (name,email,msg) "
          "VALUES (%s,%s,%s)"
        )
        cur.execute(insert_stmt, [name,email,msg])
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return  render_template('ok.html')



if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)
