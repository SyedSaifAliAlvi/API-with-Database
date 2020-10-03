import pymysql
import json
import os
import datetime
from apiResponses import error400, error500, success200

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


def insert_user(body):
    try:
        if body is not None:
            if isinstance(body, str):
                post_message = json.loads(body)
            else:
                post_message = body
            Pid = post_message.get('id')
            lastName = post_message.get('ln')
            firstName = post_message.get('fn')
            address = post_message.get('addr')
            City = post_message.get('city')

            cursor = connection.cursor()
            query = "insert into Persons(PersonID,LastName,FirstName,Address,City) value " \
                    "({0},\"{1}\",\"{2}\",\"{3}\"," \
                    "\"{4}\")".format(Pid,lastName,firstName,address,City)
            cursor.execute(query)
            Bigresponse = success200("Data has been submitted successfully")
            cursor.close()
            connection.commit()
            print("Success post method at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return Bigresponse

        else:
            message = "Body not present"
            responseObject = error400(message)
            print("failed post method at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return responseObject
    except:
        responseObject = error500()
        print("failed post method at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return responseObject
