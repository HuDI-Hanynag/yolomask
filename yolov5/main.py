import userinput

import maskupdates
import appTime



import requests
import json
import time
import base64
payload = {}
ID = {}


tenant = "hydev"
tenant = input('Tenant name (default is {}): '.format(tenant))

user = userinput.UserData()
auth_key = user.getUserData()
sourceId = input('Enter source id: ')
ID["id"] = sourceId

encoded = base64.b64encode(bytes(auth_key,'utf-8')).decode('ascii')
headers = {
    'Authorization': "Basic {}".format(encoded),
    'Content-Type': "application/json",
    'Accept': "application/vnd.com.nsn.cumulocity.measurement+json"
    }
# ToDo: Refactor the following
url = "https://hydev.mciotextension.eu1.mindsphere.io/measurement/measurements"

while True:
    
    maskpeople = maskupdates.PCData()
    payload = maskpeople.getPayloadData()
    payload["time"] = appTime.getCurrentTime()
    payload["source"] = ID
    payload["type"] = "c8y_PCInformation"
    payload_json = json.dumps(payload)
    response = requests.post(url=url, data=payload_json, headers=headers)

    if response.status_code == 201:
        print('Mask Updated successfully')
    else:
        print('Could not update the series')

    time.sleep(1)

    
    
