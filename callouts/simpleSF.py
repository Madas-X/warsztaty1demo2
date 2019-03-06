from simple_salesforce import Salesforce
import os

def get_sf(id):
    sf = Salesforce(
        instance=os.environ.get('INSTANCE', None),
        username=os.environ.get('USERNAME', None),
        password=os.environ.get('PASSWORD', None),
        security_token=os.environ.get('SECURITY_TOKEN', None))

    contact = sf.Contact.get(id)
    return contact
