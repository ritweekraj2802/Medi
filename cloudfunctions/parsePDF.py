import os
import pdftables_api
import functions_framework
import requests
import base64
import json

url = "https://pdftables.com/api"

@functions_framework.http
def parsePDF(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
        }
        return ('', 204, headers)
    headers = {
        'Access-Control-Allow-Origin': '*',
    }
    json_data = request.get_json()
    if request.args and 'pdf-data' in request.args:
        pdfdata = base64.b64decode(request.args.get('pdf-data'))
    elif json_data and 'pdf-data' in json_data:
        # Get the PDF data and deocde it
        pdfdata = base64.b64decode(json_data['pdf-data'])
    
    # secret key for api, and format we want the returned file in
    params = (
    ('key', 'uxr7dt4hqwrb'), # invalid api key <----
    ('format', 'csv'),
    )
    # our data we send the api
    files = {
    'f': (pdfdata),
    }
    
    # sending and recv the request & response
    response = requests.post('https://pdftables.com/api', params=params, files=files)

    
    # return the csv file
    # return response.content
    
    # parse the response
    codePrice = {}
    for s in response.text.split('\n'):
        if(',,' in s or "Code" in s or s == ''):
            continue
        t = s.split('$')
        if(len(list(t)) == 1):
            continue
        code = t[0][:5] # First 5 characters are the code
        price = t[1] # The price is what is left
        codePrice[code] = price
    # return response.text
    return (json.dumps(codePrice), 200, headers) # return a string representation of the dictionary
