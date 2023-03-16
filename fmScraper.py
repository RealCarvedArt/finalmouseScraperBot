import requests
import json

# make a GET request to obtain the JSON data
response = requests.get('https://www.finalmouse.com/products.json')

# parse the response body
products_data = json.loads(response.text)

# for each product
for product in products_data['products']:
    # render the product name
    print(product['title'])
    # render the product price
    for var in product["variants"]:
        print('$' + var['price'])
    # render the product slug
    slug = (product['handle'])
    print('https://www.finalmouse.com/products/' + slug)
    # render the product id
    print(product['id'])
    # render space
    print( )
