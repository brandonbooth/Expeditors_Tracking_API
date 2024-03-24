import requests
import json
import csv

access_token = 'your_access_token' # replace with your_access_token

data_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

def request_data(url,headers):
    response = requests.get(url, headers=headers)
    return response

data_url = 'https://api.expeditors.com/tracking/v2/shipments?sizeLimit=90&offset=20&start=2024-01-01T12:00:00&end=2024-03-30T13:00:00'

r = request_data(data_url, data_headers)

jsonResponse = json.loads(r.text)

if 'error' in jsonResponse:
    print(r.status_code)
    print(jsonResponse)
    #print(jsonResponse['error'])
    if jsonResponse['error'] == 'invalid_token':
        print('Requesting new token...')
        exit()
    else:
        exit()

data_file = open('data_file.csv', 'w')

csv_writer = csv.writer(data_file, lineterminator='\n')

# counter variable used if writing headers to the CSV file
#count = 0

for data in jsonResponse:
    # if count == 0:
    #     header = data.keys()
    #     csv_writer.writerow(header)
    #     count += 1    
    csv_writer.writerow(data.values())
data_file.close()

print('Script completed...')