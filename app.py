from flask import Flask
import mysql.connector


app = Flask(__name__)


def favorite_message():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'mydb',
        'port': '3306'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    print('YOU ARE CONNECTED TO MYSQLDB!!')
    message = 'SUCCESSFULL CONECTION!!'
    connection.close()

    return message


@app.route('/')
def index():
    return favorite_message()



if __name__ == '__main__':
    app.run(host='0.0.0.0')
