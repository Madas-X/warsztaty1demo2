from simple_salesforce import Salesforce


def getSF():
    sf = Salesforce(
        instance='eu19.salesforce.com',
        username='warsztaty@pollub.dev',
        password='PILJjb2mM0HX34CePj0z',
        security_token='dJs1RhNsGsCdq80hasgpJOFn')

    contact = sf.Contact.get('0031i000005BRohAAG')
    return contact