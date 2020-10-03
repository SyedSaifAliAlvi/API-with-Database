import json


def error400(message):
    response = {}
    response["statusCode"] = 400
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'
    response['headers']['Access-Control-Allow-Origin'] = '*'
    response['headers']['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers,' \
                                                          'Access-Control-Allow-Methods'
    response['headers']['Access-Control-Allow-Methods'] = 'POST,PATCH,OPTIONS'
    response['Body'] = message
    return response


def error500():
    response = {}
    response["statusCode"] = 500
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'
    response['headers']['Access-Control-Allow-Origin'] = '*'
    response['headers']['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers' \
                                                          ',Access-Control-Allow-Methods'
    response['headers']['Access-Control-Allow-Methods'] = 'POST,PATCH,OPTIONS'
    response['Body'] = "Error"
    return response


def success200(responseObject):
    response = {}
    response["statusCode"] = 200
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'
    response['headers']['Access-Control-Allow-Origin'] = '*'
    response['headers']['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers,' \
                                                          'Access-Control-Allow-Methods'
    response['headers']['Access-Control-Allow-Methods'] = 'POST,PATCH,OPTIONS'
    response['body'] = json.dumps(responseObject, default=str)
    return response
