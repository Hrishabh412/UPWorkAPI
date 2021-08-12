# UPWorkAPI
Code is in Dev Branch https://github.com/Hrishabh412/UPWorkAPI/tree/dev
This is an API to retrive multiple table data which are connected through primary and foreign keys.
There are five tables.
To access each table data we need to use different user with slitly changing it.
I've deployed the API in HerokuAPP. but getting some errors. because for lack of time i left it there.
Heroku link is below for all table, we can modify Tablename at the end.
https://newapi-rishabh.herokuapp.com/branch/

we can perform GET,POST and DELETE for now, can add PUT also.

For testing purpose Use POSTMAN Application.

please find below links to retieve the data.
Customer table - http://127.0.0.1:8000/customer/
Branch table - http://127.0.0.1:8000/branch/
Loan Amount data - http://127.0.0.1:8000/loanamount/
Customer Home Addredd data - http://127.0.0.1:8000/customerhome/
Customer Office Data - http://127.0.0.1:8000/customeroffice/

Are the table sharing same primary key of Customer Table (customerid) as per requirement.
this API contain BasicAuthentication, so to user this please use:
username - Mohit
Password - mohit

We also add session authentication and Token Authentication, but this API is for testing purpose. so I kept it simple.
https://github.com/Hrishabh412/UPWorkAPI This is GitHub repo link.

also to retrieve data from API, we can save it in CSV file.
below code is to download the file.
we can change the URL to access the data of different tables.
also we need to change column names.

import requests
import json
from csv import DictWriter

url = "http://127.0.0.1:8000/customer/"

payload = " \r\n   "
headers = {
  'Authorization': 'Basic TW9oaXQ6bW9oaXQ=',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

with open('Branch Details.csv', 'w') as f:
    csv_writer=DictWriter(f, fieldnames=["id","customerid", "agreementdate","lrn","tenor","advemi","mob"])
    csv_writer.writeheader()
    for i in response.json():
        csv_writer.writerows([i])
        
     
<---------------------------------------------------------------------------------->


code for LOAN AMount table data:

import requests
import json
from csv import DictWriter
url = "http://127.0.0.1:8000/loanamount/"

payload = " \r\n   "
headers = {
  'Authorization': 'Basic TW9oaXQ6bW9oaXQ=',
  'Content-Type': 'application/json',
}

response = requests.request("GET", url, headers=headers, data=payload)


with open('Loan Amount data.csv', 'w') as f:
    csv_writer=DictWriter(f, fieldnames=["id","customerid", "agreementdate","lrn","tenor","advemi","mob"])
    csv_writer.writeheader()
    for i in response.json():
        csv_writer.writerows([i])
        
 <----------------------------------------------------------------------------------->
        
for BRANCH DATA:

import requests
import json
from csv import DictWriter
url = "http://127.0.0.1:8000/branch/"

payload = " \r\n   "
headers = {
  'Authorization': 'Token 6cf4df309c548bb40940aa78a298c8abd0c49869',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=xy8w50rpS2Lh8o0FAeqMEHEMgzKxJLuqvZ09CJ3jZRcUerWNmf61GXUPX1W4xp0H'
}

response = requests.request("GET", url, headers=headers, data=payload)


with open('Branch Details.csv', 'w') as f:
    csv_writer=DictWriter(f, fieldnames=['id',"customerid","zonename", "regionname", "areaname","branchname","branchcode"])
    csv_writer.writeheader()
    for i in response.json():
        csv_writer.writerows([i])
#print(response.text)


we will be getting different files for different tables.



*NOTE* ---> if any doubt, feel free to Contact (8764124447)
