import requests
import os

class StandardCallout:

    def __init__(self):
        self.access_token = None
        self.instance_url = None

    salesforce = 'https://login.salesforce.com/services/oauth2/token'
    params = {
        "grant_type": "password",
        "client_id": os.environ.get('CONSUMER_KEY', None),
    # Consumer Key
        "client_secret": os.environ.get('CONSUMER_SECRET', None),  # Consumer Secret
        "username": os.environ.get('USERNAME', None),  # The email you use to login
        "password": os.environ.get('PASSWORD', None)  # Concat your password and your security token
    }

    def authorize(self):
        response = requests.post(self.salesforce, params=self.params)
        self.access_token = response.json().get("access_token")
        self.instance_url = response.json().get("instance_url")
        return response

    def get_contact(self, contact_id):
        response = requests.get(self.instance_url + '/services/data/v44.0/sobjects/Contact/' + contact_id,
                                headers={"Authorization": "Bearer %s" % self.access_token})
        return response
