import requests
from bs4 import BeautifulSoup

def cpt_description(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
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
    
    request_json = request.get_json()
    if request.args and 'code' in request.args:
        code = request.args.get('code')
    elif request_json and 'message' in request_json:
        code = request_json['code']
 
    if code == None or code.isnumeric() == False:
        return "error: cpt not provided or provided in the wrong format"

    URL = "https://www.aapc.com/codes/cpt-codes/" + code
    r = requests.get(URL)
   
    soup = BeautifulSoup(r.content, "html.parser")
      
    text = soup.find('div', attrs = {'id':'cpt_layterms'}) 
    layman_text = str(text.find('p')).strip('<p>').strip('</')

    return (layman_text, 200, headers)


