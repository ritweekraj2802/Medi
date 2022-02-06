import json

def get_price(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
    }
    code = None
       
    code = None
    
    request_json = request.get_json()
    if request.args and 'code' in request.args:
        code = request.args.get('code')
    elif request_json and 'message' in request_json:
        code = request_json['code']
    
    print(code)
    if code == None or code.isnumeric() == False:
        return ("error: cpt not provided or provided in the wrong format",200, headers)
    price_data = json.load("prices.json")
    price = price_data[code]
    return (price, 200, headers)

