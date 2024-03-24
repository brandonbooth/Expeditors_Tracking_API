import requests
import base64

client_id = 'your_client_id' # replace with your_client_id
client_secret = 'your_client_secret' # replace with your_client_secret
to_encode = client_id + ':' + client_secret
base64_encoded_id_secret = base64.b64encode(to_encode.encode()).decode()

token_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic {}'.format(base64_encoded_id_secret)
}

token_params = {'grant_type': 'client_credentials'}

token_url = 'https://api.expeditors.com/tracking/v2/oauth2/token'

def request_access_token(url,headers,params):
    response = requests.post(url, headers=headers, params=params)
    return response

r = request_access_token(token_url, token_headers,token_params)

print(r.status_code)
print(r.text)

access_token = r.json()['access_token']
print(access_token)