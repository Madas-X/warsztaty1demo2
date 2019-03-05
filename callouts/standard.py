import requests

credentials = 'piotr.piesiak@advance-auto.com/token', 'a6KZyDLtBD45bKvzYjiOUOTBjnJz7Vgw1YUsxVpu'
session = requests.Session()
session.auth = credentials
zendesk = 'https://aap.zendesk.com'