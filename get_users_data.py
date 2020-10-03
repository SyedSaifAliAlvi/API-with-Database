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


def get_users():
    try:
        cursor = connection.cursor()
        query = "select PersonID,LastName,FirstName,Address,City from Persons"
        cursor.execute(query)
        data = cursor.fetchall()
        data = list(map(list,data))
        reponse ={}
        for i in range(len(data)):
            tempResponse = {}
            tempResponse['Id'] = data[i][0]
            tempResponse['LastName'] = data[i][1]
            tempResponse['FirstName']=data[i][2]
            tempResponse['Address']=data[i][3]
            tempResponse['City']=data[i][4]
            reponse[i+1]=tempResponse
        Bigresponse = success200(reponse)
        print("Success get method at",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cursor.close()
        connection.commit()
        return Bigresponse

    except:
        responseObject = error500()
        print("Fail get method at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return responseObject


