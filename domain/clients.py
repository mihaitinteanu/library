class Client:
    """
    A class to represent a client with an id 'client_id',
    name 'client_name' and the social security number
    'ssn'. The class also contains getter methods for
    each of the attributes of the client.
    Attributes:
        client_id: The id of the client
        name: The name of the client
        cnp: The CNP (social security number) of the client
    """
    def __init__(self, client_id, name, cnp):
        self.client_id = client_id
        self.name = name
        self.cnp = cnp

    def get_client_id(self):
        return self.client_id

    def get_name(self):
        return self.name

    def get_cnp(self):
        return self.cnp