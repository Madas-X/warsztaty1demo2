from flask import Flask
from names import namesgenerator
from callouts import simpleSF

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/generate')
def generate_random_name():
    return namesgenerator.get_random_name()

@app.route('/sf')
def sfCallout() -> None:
    returned = simpleSF.getSF()
    print(returned)
    return str(returned.get('CreatedDate'))


if __name__ == '__main__':
    app.run()
