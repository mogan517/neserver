from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='templates')
import sys
app.config["MYSQL_HOST"] = '47.101.59.109'
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = 'mogan'
app.config["MYSQL_PASSWORD"] = 'nease.net'
app.config["MYSQL_DB"] = 'flaskapp'
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
mysql = MySQL(app)
# app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/article/<int:aid>')
def article(aid):
    cur = mysql.connection.cursor()
    resultValue1 = cur.execute('SELECT * FROM Articles WHERE ArticleId = {0}'.format(aid))
    article = cur.fetchall()
    print(article)
    return render_template('article.html', article=article, aid=aid)
@app.route('/articlelist')
def articlelist():
    cur = mysql.connection.cursor()
    resultValue1 = cur.execute('SELECT * FROM Articles')
    allarticle = cur.fetchall()
    return render_template('article.html', allarticle=allarticle)
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
@app.route("/postarticle", methods=['GET', 'POST'])
def postarticle():
    if request.method == "POST":
        userPost = request.form
        title = userPost['Title']
        photo = userPost['Photo']
        img = convertToBinaryData(photo)
        ss = userPost['Snapshot']
        content = userPost['Content']
        cur = mysql.connection.cursor()
        insert_stmt = (
          "INSERT INTO Articles (Photo,Title,Content,Snapshot) "
          "VALUES (%s,%s,%s,%s)"
        )
        cur.execute(insert_stmt, [img, title, content, ss])
        mysql.connection.commit()
        cur.close()
    return render_template('postarticle.html')

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
    return render_template('regist.html')



if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
