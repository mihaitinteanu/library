class ClientRepository:
    """
    Class to store all the clients related operations (CRUD).
    Attributes:
        clients: a dictionary with the clients registered in the repository;
        the key is the id of the client and the value is the client object;
    """
    def __init__(self):
        self.clients = {}

    def add_client(self, client):
        """
        Method to add a new client to the repository.
        :param client: a Client object to be added
        :return: None
        """
        client_id = client.get_client_id()
        if client_id in self.clients.keys():
            raise ValueError('Client already registered.')
        self.clients[client_id] = client

    def get_clients(self):
        """
        Method to get all clients registered in the repository.
        :return: a list with the clients registered in the repository
        """
        return list(self.clients.values())

    def del_client(self, client_id):
        """
        Method to delete a client from the repository.
        :param client_id: the id of the client to be deleted
        :return: None
        """
        if client_id not in self.clients.keys():
            raise ValueError('Client not registered.')
        del self.clients[client_id]

    def update_client(self, updated_client):
        """
        Method to update a client in the repository.
        :param updated_client: a Client object to be updated
        :return: None
        """
        updated_client_id = updated_client.get_client_id()
        if updated_client_id not in self.clients.keys():
            raise ValueError('Client not registered.')
        self.clients[updated_client_id] = updated_client