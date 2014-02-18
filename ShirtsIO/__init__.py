from helpers import validate_params
from request import ShirtsIORequest


class ShirtsIOClient(object):
    """
    A Python Client for the Shirts.io API
    """

    def __init__(self, api_key):
        """
        Initializes the ShirtsIOClient object, creating the ShirtsIORequest
        object which deals with all request formatting.

        :param api_key: a string, the user specific secret, received
                             from the /access_token endpoint

        :returns: None
        """
        self.request = ShirtsIORequest(api_key)

    def categories(self, category_id=None):
        resource_url = 'products/category/'

        if category_id is not None:
            resource_url += str(category_id) + '/'

        return self.send_api_request("get", resource_url)

    def products(self, product_id, get_inventory=False, **kwargs):
        resource_url = 'products/' + str(product_id) + '/'
        required_params = []
        optional_params = []

        if get_inventory:
            required_params = ['color']
            optional_params = ['state']

        return self.send_api_request("get", resource_url, kwargs, required_params, optional_params)

    def quote(self, **kwargs):
        resource_url = 'quote/'
        required_params = ['garment', 'print']
        optional_params = ['print_type', 'personalization', 'address_count', 'extra_screens', 'ship_type',
                           'international_garments']

        return self.send_api_request("get", resource_url, kwargs, required_params, optional_params)

    def order(self, **kwargs):
        resource_url = 'order/'
        required_params = ['test', 'price', 'garment', 'print', 'addresses']
        optional_params = ['print_type', 'personalization', 'address_count', 'extra_screens', 'ship_type']

        return self.send_api_request("post", resource_url, kwargs, required_params, optional_params)

    def status(self, order_id):
        resource_url = 'status/' + str(order_id) + '/'
        return self.send_api_request('get', resource_url)

    def send_api_request(self, method, url, params={}, required_params=[], optional_params=[]):
        """
        Sends the url with parameters to the requested url, validating them
        to make sure that they are what we expect to have passed to us

        :param method: a string, the request method you want to make
        :param params: a dict, the parameters used for the API request
        :param valid_parameters: a list, the list of valid parameters
        :param needs_api_key: a boolean, whether or not your request needs an api key injected

        :returns: a dict parsed from the JSON response
        """

        files = []
        if 'data' in params:
            if isinstance(params['data'], list):
                files = [('data[' + str(idx) + ']', data, open(data, 'rb').read()) for idx, data in
                         enumerate(params['data'])]
            else:
                files = [('data', params['data'], open(params['data'], 'rb').read())]
            del params['data']

        validate_params(required_params, optional_params, params)
        if method == "get":
            return self.request.get(url, params)
        elif method == "post":
            return self.request.post(url, params, files)
