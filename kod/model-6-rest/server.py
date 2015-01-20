from bottle import route, run, response, request
import json
from random import randint

_brands = [
    {'id': 1, "name": "Alfa Romeo"},
    {'id': 2, "name": "Mercedes"},
]

_cars = [
    {'id': 1, "manufactured": 1901, "brand_id": 1}
]

@route('/brands')
def brands():
    response.content_type = "application/json"
    return json.dumps(_brands)

@route('/cars')
def cars():
    response.content_type = "application/json"
    return json.dumps(_cars)

@route('/cars', method='UPDATE')
def update_cars():
    global _cars
    _cars = json.loads(request.body.read().decode('utf-8'))
    for i, car in enumerate(_cars):
        if not car.get('id'):
            _cars[i]['id'] = randint(1, 1000)


@route('/cars/<id>', method='DELETE')
def delete_car(id):
    for i, c in enumerate(_cars):
        if c['id'] == int(id):
            del _cars[i]

run(host='localhost', port=8080, debug=True)
