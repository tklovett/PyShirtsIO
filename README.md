# PyShirtsIO

[![Build Status](https://travis-ci.org/tklovett/PyShirtsIO.png?branch=master)](https://travis-ci.org/tklovett/PyShirtsIO)

## Create a client

A `ShirtsIO.ShirtsIOClient` is the object through which all calls to the Shirts.io API are made.
Creating one is this easy:

``` python
import ShirtsIO
client = ShirtsIO.ShirtsIOClient('<api_key>')
client.product_categories() # returns a list of available product categories
```

## Supported Methods

``` python
client.products.categories()    # get a list of product categories
client.products.categories(3)   # get a list of products in category 3
client.products(5)              # get details for product 5
client.products(5, inventory_info=True, state='PA')              # get details for product 5 including inventory in PA
client.quote({})                # get a quote for the specified order
client.order.create({})         # place the specified order
client.status(2)                # get the status of order 2
client.webhooks()               # ger a list of registered webhooks
client.webhooks.create("")     # add the specified webhook URL
client.webhooks.delete("")     # delete the specified webhook URL
```

## Using the interactive console

This client comes with an interactive console. You'll have to provide your
API key on the first run, but it will then be stored for future use (in ~/.pyshirtsio).

You'll need `pyyaml` installed to run it, but then it's just:

``` bash
$ python interactive-console.py
```

## Running tests

The tests (and coverage reports) are run with nose, like this:

``` bash
python setup.py test
```

# Copyright and License

This is a derivative work of [PyTumblr](https://github.com/tumblr/pytumblr/)
under its Apache [License](https://github.com/tumblr/pytumblr/blob/master/LICENSE).
Any code in this source left unmodified from PyTumblr is Copyright 2013 Tumblr, Inc.

This work is licensed under the The MIT License (MIT).

Copyright (c) 2014 Thomas Lovett


