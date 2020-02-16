from flaskext.mysql import MySQL
from flask import request
from flask import render_template, Flask
from flask import jsonify

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
    
@app.route('/inputmahasiswa', methods=['POST'])
def inputmahasiswa():
    # nama = request.form['nama']
    # nim = request.form['nim']
    # tgl_lahir = request.form['tgl_lahir']
    nim = request.json['nim']
    nama = request.json['nama']
    tgl_lahir = request.json['tgl_lahir']
    
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "Insert into mahasiswa (nama,nim,tgl_lahir) values (%s,%s,%s)"
    data = (nama,nim,tgl_lahir)
    cursor.execute(sql,data)
    conn.commit()
    result = jsonify({ 
        "Message" : "ID Succesfully Added"
    })
    return result

if __name__=="__main__":
    app.run(port=2000, debug=True)