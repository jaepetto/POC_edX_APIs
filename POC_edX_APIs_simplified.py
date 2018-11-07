import requests
import json

lms_base_url = "" # e.g. https://edx.org
token = "" # e.g. XXXXXXXXXXXXXXXXXXXXXXXX

enrollment_endpoint = "{}/api/enrollment/v1/enrollment".format(lms_base_url)
enrollment_request_headers = {'Authorization': "Bearer {}".format(token),
                              'Content-Type': 'application/json'}
enrollment_request = requests.get(enrollment_endpoint, headers=enrollment_request_headers)
if enrollment_request.status_code == 200:
    courses = json.loads(enrollment_request.text)
    print json.dumps(courses, sort_keys=True, indent=4, separators=(',', ': '))
