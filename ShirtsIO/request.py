import requests
from requests.exceptions import RequestException
import json


class ShirtsIORequest(object):
    """
    A simple request object that lets us query the Shirts.io API
    """

    def __init__(self, api_key):
        self.host = 'https://www.shirts.io/api/v1/'
        self.api_key = api_key

    def get(self, url, params={}):
        """
        Issues a GET request against the API, properly formatting the params

        :param url: a string, the url you are requesting
        :param params: a dict, the key-value of all the paramaters needed
                       in the request
        :returns: a dict parsed of the JSON response
        """

        params.update({'api_key': self.api_key})
        try:
            response = requests.get(self.host + url, params=params)
        except RequestException as e:
            response = e.args

        return self.json_parse(response.content)

    def post(self, url, params={}, files=None):
        """
        Issues a POST request against the API, allows for multipart data uploads

        :param url: a string, the url you are requesting
        :param params: a dict, the key-value of all the parameters needed
                       in the request
        :param files: a list, the list of tuples of files

        :returns: a dict parsed of the JSON response
        """
        params.update({'api_key': self.api_key})
        try:
            response = requests.post(self.host + url, data=params, files=files)
            return self.json_parse(response.content)
        except RequestException as e:
            return self.json_parse(e.args)

    def json_parse(self, content):
        """
        Wraps and abstracts content validation and JSON parsing
        to make sure the user gets the correct response.
        
        :param content: The content returned from the web request to be parsed as json
        
        :returns: a dict of the json response
        """
        try:
            data = json.loads(content)
        except ValueError, e:
            return {'meta': { 'status': 500, 'msg': 'Server Error'}, 'response': {"error": "Malformed JSON or HTML was returned."}}
        
        #We only really care about the response if we succeed
        #and the error if we fail
        if 'error' in data:
            return {'meta': { 'status': 400, 'msg': 'Bad Request'}, 'response': {"error": data['error']}}
        elif 'result' in data:
            return data['result']
        else:
            return {}