from simple_salesforce import Salesforce


def get_sf(id):
    sf = Salesforce(
        instance='eu19.salesforce.com',
        username='warsztaty@pollub.dev',
        password='PILJjb2mM0HX34CePj0z',
        security_token='dJs1RhNsGsCdq80hasgpJOFn')

    contact = sf.Contact.get(id)
    return contact
