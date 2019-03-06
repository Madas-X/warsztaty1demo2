import requests


class StandardCallout:

    def __init__(self):
        self.access_token = None
        self.instance_url = None

    salesforce = 'https://login.salesforce.com/services/oauth2/token'
    params = {
        "grant_type": "password",
        "client_id": "3MVG9T46ZAw5GTfWOF_ttZauxH9aqB6ZzHjvCgLk09xn4Q6xnSV6ODeIqEVVm3SOfIvSL_CsnTha94k8GPer1",
    # Consumer Key
        "client_secret": "B2EA1178172C7C1EF7E98EE74DA5EB98DC82E5F3CEC42272B5B4AA514F191E90",  # Consumer Secret
        "username": "warsztaty@pollub.dev",  # The email you use to login
        "password": "PILJjb2mM0HX34CePj0z"  # Concat your password and your security token
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
