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
        # self.shirtsio_request = ShirtsIORequest(api_key)
        self.ApiResourceMixin.set_api_key(api_key)
        self.products = self.ProductsResource()
        self.quote = self.QuoteResource()
        self.status = self.StatusResource()
        self.webhooks = self.WebhooksResource()

    class ApiResourceMixin(object):

        @classmethod
        def set_api_key(cls, key):
            cls.api_key = key
            cls.request = ShirtsIORequest(key)

        def get(self, url, params={}):
            return self.request.get(url, params)

        def post(self, url, data={}):
            return self.request.post(url, data)

    class ProductsResource(ApiResourceMixin):
        endpoint = 'products/'

        def categories(self, category_id=None):
            if category_id:
                return self.get(self.endpoint + 'category/' + str(category_id))
            else:
                return self.get(self.endpoint + 'category/')

        def __call__(self, product_id, inventory_info=False, **kwargs):
            if inventory_info:
                required_params = ['color']
                optional_params = ['state']
                validate_params(required_params, optional_params, kwargs)
                return self.get(self.endpoint + str(product_id), kwargs)
            else:
                return self.get(self.endpoint + str(product_id))

    class QuoteResource(ApiResourceMixin):
        endpoint = 'quote/'

        def __call__(self, params):
            required_params = ['garment', 'print']
            optional_params = ['print_type', 'personalization', 'address_count', 'extra_screens', 'ship_type',
                               'international_garments']
            validate_params(required_params, optional_params, params)
            return self.get(self.endpoint, params)

    class OrderResource(ApiResourceMixin):
        endpoint = 'order/'

        def create(self, **kwargs):
            required_params = ['test', 'price', 'garment', 'print', 'addresses']
            optional_params = ['print_type', 'personalization', 'address_count', 'extra_screens', 'ship_type']
            validate_params(required_params, optional_params, kwargs)
            return self.post(self.endpoint, kwargs)

    class StatusResource(ApiResourceMixin):
        endpoint = 'status/'

        def __call__(self, order_id):
            return self.get(self.endpoint + str(order_id) + '/')

    class WebhooksResource(ApiResourceMixin):
        endpoint = 'webhooks/'

        def __call__(self):
            return self.get(self.endpoint + 'list/')

        def create(self, url):
            return self.post(self.endpoint + 'register/', {'url': "'%s'" % url})

        def delete(self, url):
            return self.post(self.endpoint + 'delete/', {'url': "'%s'" % url})
