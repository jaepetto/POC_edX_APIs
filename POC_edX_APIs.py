import requests
import json

lms_base_url = ""  # e.g. http://edx.org
client_id = ""  # e.g. 123456
client_secret = ""  # e.g. 123456
username = ""  # e.g. admin
password = ""  # e.g. secret

token_endpoint = "{}/oauth2/access_token/".format(lms_base_url)
token_request_data = {'client_id': client_id,
                      'client_secret': client_secret,
                      'grant_type': 'password',
                      'username': username,
                      'password': password}

token_request = requests.post(token_endpoint, data=token_request_data)
if token_request.status_code == 200:
    token_request_response = json.loads(token_request.text)
    access_token = token_request_response['access_token']

    enrollment_endpoint = "{}/api/enrollment/v1/enrollment".format(lms_base_url)
    enrollment_request_headers = {'Authorization': "Bearer {}".format(access_token),
                                  'Content-Type': 'application/json'}
    enrollment_request = requests.get(enrollment_endpoint, headers=enrollment_request_headers)
    if enrollment_request.status_code == 200:
        courses = json.loads(enrollment_request.text)
        print json.dumps(courses, sort_keys=True, indent=4, separators=(',', ': '))
