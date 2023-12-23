from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
import json


app = Flask(__name__)
with open('./db_info/config.json') as config_file:
    config = json.load(config_file)
#configure db
app.config["MYSQL_HOST"]=config['db_config']['host']
app.config["MYSQL_USER"] = config['db_config']['user']
app.config["MYSQL_PASSWORD"] = config['db_config']['password']
app.config["MYSQL_DB"] = config['db_config']['database']


mysql=MySQL(app)



@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/booking.html')
def book():
    return render_template('booking.html')

@app.route('/', methods=['POST','GET'])
def booking():
    if request.method=='POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        source_location = request.form['source']
        destination_location = request.form['destination']
        travel_date = request.form['date']
        passenger_count = request.form['passenger_count']
        selected_bus = request.form['busSelect']
        bus_type = request.form['acSelect']
        selected_berth = request.form['berthSelect']
        fare_amount = request.form['fare']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO BOOKINGS(first_name,last_name,source_location,destination_location,travel_date,passenger_count,selected_bus,bus_type,selected_berth,fare_amount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    ,(first_name,last_name,source_location,destination_location,travel_date,passenger_count,selected_bus,bus_type,selected_berth,fare_amount))
        mysql.connection.commit()
        cur.close()
        return render_template('tickets.html',**locals())
    return "Successfull"
    
@app.route('/tickets.html')
def tickets():
    return render_template('tickets.html')





if __name__ == '__main__':
    app.run(debug=True)