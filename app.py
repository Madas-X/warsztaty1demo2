import json

from flask import Flask
from callouts import simpleSF
from callouts import standard
from names import namesgenerator

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/generate')
def generate_random_name():
    return namesgenerator.get_random_name()


@app.route('/simpleSF/<contact_id>')
def sfCallout(contact_id):
    returned = simpleSF.get_sf(contact_id)
    return json.dumps(returned)


@app.route('/standardSF/<contact_id>')
def standard_sf(contact_id):
    instance = standard.StandardCallout()
    instance.authorize()
    return instance.get_contact(contact_id).text


if __name__ == '__main__':
    app.run()
