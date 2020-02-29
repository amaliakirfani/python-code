from flaskext.mysql import MySQL
from flask import request
from flask import render_template, Flask
from flask import jsonify
import pymysql

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'amalia'
app.config['MYSQL_DATABASE_DB'] = 'amalia'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/absensi', methods=['POST'])
def absensi():
    rfid_id=request.json['rfid_id']

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("select * from mahasiswa where rfid_id=%s", rfid_id)
    mahasiswa = cursor.fetchone() 

    if mahasiswa is None:
        sql = "Insert into mahasiswa (rfid_id) values (%s)"
        data = (rfid_id)
        cursor.execute(sql,data)
        conn.commit()
        res = jsonify({
            "Message" : "ID Successfully Added"
        })
        return res
    else:
        res = jsonify({
        "Message" : "ID Already There"
        })
        return res


if __name__=="__main__":
    app.run(port=5000,host="172.16.18.246", debug=True)