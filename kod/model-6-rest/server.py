from bottle import route, run, response
import json

_brands = [
    {'id': 1, "name": "Alfa Romeo"},
    {'id': 2, "name": "Mercedes"},
]

_cars = []

@route('/brands/')
def brands():
    response.content_type = "application/json"
    return json.dumps(_brands)

@route('/brands/<id>', method='PUT'):
def update_brand(id):
    pass

@route('/brands/<id>', method='DELETE')
def delete_brand(id):
    for brand in _brands:
        if brand['id'] == int(id):
            del _brands[brand]
            break


run(host='localhost', port=8080, debug=True)
