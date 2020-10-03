import pymysql
import os
from apiResponses import error500, success200
import datetime

endpoint = os.environ.get('endpoint')
username = os.environ.get('username')
password = os.environ.get('password')
name = os.environ.get('name')
port = int(os.environ.get('port'))

try:
    connection = pymysql.connect(endpoint, user=username, passwd=password, db=name, port=port)
    print("SUCCESS: Connection to RDS mysql instance succeeded")
except:
    print("ERROR: Unexpected error: Could not connect to MySql instance.")


def get_user(id):
    try:
        cursor = connection.cursor()
        query = "select PersonID,LastName,FirstName,Address,City from Persons where " \
                "PersonID={0}".format(id)
        cursor.execute(query)
        data = cursor.fetchall()
        data = list(map(list,data))
        tempResponse = {}
        tempResponse['Id'] = data[0][0]
        tempResponse['LastName'] = data[0][1]
        tempResponse['FirstName']=data[0][2]
        tempResponse['Address']=data[0][3]
        tempResponse['City']=data[0][4]
        Bigresponse = success200(tempResponse)
        print("Success get method at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cursor.close()
        connection.commit()
        return Bigresponse

    except:
        responseObject = error500()
        print("Fail get method at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return responseObject


