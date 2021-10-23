import json
import os
import requests


def lambda_handler(event, context):
    responseStatus = 'SUCCESS'
    responseData = {}

    if event['RequestType'] == 'Delete':
        sendResponse(event, context, responseStatus, responseData)

    responseData = {'Success': 'Test Passed.', 'timeInfo': getTimeInfo()}
    sendResponse(event, context, responseStatus, responseData)


def sendResponse(event, context, responseStatus, responseData):
    responseBody = {'Status': responseStatus,
                    'Reason': 'See the details in CloudWatch Log Stream: ' + context.log_stream_name,
                    'PhysicalResourceId': context.log_stream_name,
                    'StackId': event['StackId'],
                    'RequestId': event['RequestId'],
                    'LogicalResourceId': event['LogicalResourceId'],
                    'Data': responseData}
    print('RESPONSE BODY:n' + json.dumps(responseBody))
    try:
        req = requests.put(event['ResponseURL'], data=json.dumps(responseBody))
        if req.status_code != 200:
            print(req.text)
            raise Exception(
                'Recieved non 200 response while sending response to CFN.')
        return
    except requests.exceptions.RequestException as e:
        print(e)
        raise


def getTimeInfo():
    timeZone = os.environ['TTIMEZONE']
    print('timeZone:n' + timeZone)
    url = "http://worldtimeapi.org/api/timezone/" + timeZone
    data = json.loads(requests.request("GET", url, headers={}, data={}).text)
    return f'abbreviation: {data["abbreviation"]} datetime: {data["datetime"]} day_of_week: {data["day_of_week"]} day_of_year: {data["day_of_year"]} dst: {str(data["dst"]).lower()} dst_from: {data["dst_from"]} dst_until: {data["dst_until"]} timezone: {data["timezone"]} unixtime: {data["unixtime"]} utc_offset: {data["utc_offset"]}'


if __name__ == '__main__':
    lambda_handler('event', 'handler')
